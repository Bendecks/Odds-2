import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
raw_dir = Path('data/raw/odds_api_io')
raw_dir.mkdir(parents=True, exist_ok=True)
output_dir.mkdir(parents=True, exist_ok=True)

api_key = os.getenv('ODDS_API_IO_KEY')
base_url = 'https://api.odds-api.io/v3'
max_events = int(os.getenv('ODDS_API_IO_MAX_EVENTS', '10'))
max_calls = int(os.getenv('ODDS_API_IO_MAX_CALLS', '6'))
max_price_events = int(os.getenv('ODDS_API_IO_MAX_PRICE_EVENTS', '3'))
min_event_match_confidence = float(os.getenv('ODDS_API_IO_MIN_EVENT_MATCH_CONFIDENCE', '0.72'))
bookmakers = os.getenv('ODDS_API_IO_BOOKMAKERS', 'Bet365,1xbet').strip()
search_query = os.getenv('ODDS_API_IO_SEARCH_QUERY', '').strip()

price_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'source_name', 'source_type', 'market_home_odds', 'market_draw_odds',
    'market_away_odds', 'price_captured_at_utc', 'source_quality', 'raw_source_url'
]
fixture_columns = [
    'fixture_id', 'league', 'league_id', 'season', 'match_date', 'match_time',
    'home_team', 'away_team', 'source', 'fetched_at_utc', 'event_status'
]
selection_diag_columns = [
    'query', 'target_home_team', 'target_away_team', 'target_match_date',
    'candidate_event_id', 'candidate_home_team', 'candidate_away_team', 'candidate_match_date',
    'event_match_confidence', 'selected', 'rejection_reason'
]

rows = []
fixture_rows = []
errors = []
rate_limit_rows = []
selection_diag_rows = []
calls_used = 0
fetched_at = datetime.now(timezone.utc).isoformat()
today = datetime.now(timezone.utc).date()
discovery_mode = 'model_covered_search_then_match_confidence_then_multi_odds'
parse_mode = 'bookmakers_market_odds_schema'
query_source = 'unknown'


def record_rate_limit_headers(label: str, status_code, headers):
    row = {
        'captured_at_utc': datetime.now(timezone.utc).isoformat(),
        'label': label,
        'status_code': status_code,
        'x_ratelimit_limit': headers.get('x-ratelimit-limit') if headers else None,
        'x_ratelimit_remaining': headers.get('x-ratelimit-remaining') if headers else None,
        'x_ratelimit_reset': headers.get('x-ratelimit-reset') if headers else None,
        'retry_after': headers.get('retry-after') if headers else None,
    }
    rate_limit_rows.append(row)
    (raw_dir / f'{label}_headers_latest.json').write_text(json.dumps(row, indent=2), encoding='utf-8')


def get_json(url: str, label: str):
    global calls_used
    if calls_used >= max_calls:
        raise RuntimeError('ODDS_API_IO_MAX_CALLS reached')
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            calls_used += 1
            record_rate_limit_headers(label, response.status, response.headers)
            text = response.read().decode('utf-8')
            (raw_dir / f'{label}_latest.json').write_text(text, encoding='utf-8')
            return json.loads(text)
    except urllib.error.HTTPError as exc:
        calls_used += 1
        record_rate_limit_headers(label, exc.code, exc.headers)
        body = exc.read().decode('utf-8', errors='replace')
        (raw_dir / f'{label}_error.txt').write_text(body, encoding='utf-8')
        raise RuntimeError(f'HTTP {exc.code}: {body[:300]}')


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def norm_team(value) -> str:
    text = str(value or '').lower().strip()
    for token in ['hotspur', 'united', 'utd', 'town', 'city', 'fc', 'afc', 'cf', '.', ',', '&']:
        text = text.replace(token, ' ')
    return ' '.join(text.split())


def team_similarity(a, b) -> float:
    left = norm_team(a)
    right = norm_team(b)
    if not left or not right:
        return 0.0
    if left == right:
        return 1.0
    if left in right or right in left:
        return 0.92
    return SequenceMatcher(None, left, right).ratio()


def fixture_confidence(target_home, target_away, candidate_home, candidate_away) -> float:
    direct = (team_similarity(target_home, candidate_home) + team_similarity(target_away, candidate_away)) / 2
    swapped = (team_similarity(target_home, candidate_away) + team_similarity(target_away, candidate_home)) / 2
    return round(max(direct, swapped), 4)


def parse_datetime(value):
    parsed = pd.to_datetime(value, errors='coerce', utc=True)
    if pd.isna(parsed):
        return None, None, None
    return parsed, parsed.date().isoformat(), parsed.time().isoformat(timespec='minutes')


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', utc=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(value, errors='coerce')
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def add_fixture_targets(frame: pd.DataFrame, targets: list[dict]) -> list[dict]:
    if not len(frame):
        return targets
    df = frame.copy()
    if 'match_date' in df.columns:
        df['parsed_date'] = pd.to_datetime(df.get('match_date'), errors='coerce', utc=True)
        df = df[(df['parsed_date'].isna()) | (df['parsed_date'].dt.date >= today)].copy()
    sort_cols = [col for col in ['parsed_date', 'match_time'] if col in df.columns]
    if sort_cols:
        df = df.sort_values(sort_cols, na_position='last')

    existing_keys = {(str(t.get('home_team')).lower(), str(t.get('away_team')).lower()) for t in targets}
    for _, fixture in df.iterrows():
        home = str(fixture.get('home_team') or '').strip()
        away = str(fixture.get('away_team') or '').strip()
        if len(home) < 3 or len(away) < 3:
            continue
        key = (home.lower(), away.lower())
        if key in existing_keys:
            continue
        targets.append({
            'query': home,
            'home_team': home,
            'away_team': away,
            'match_date': parse_date(fixture.get('match_date')),
        })
        existing_keys.add(key)
        if len(targets) >= max_price_events:
            break
    return targets


def choose_search_targets() -> list[dict]:
    global query_source
    if search_query:
        query_source = 'env_override'
        targets = []
        for q in [q.strip() for q in search_query.split(',') if len(q.strip()) >= 3][:max_price_events]:
            targets.append({'query': q, 'home_team': q, 'away_team': '', 'match_date': None})
        return targets

    targets = []
    predictions = safe_read_csv(output_dir / 'forward_fixture_predictions.csv')
    targets = add_fixture_targets(predictions, targets)
    if targets:
        query_source = 'forward_fixture_predictions'
        return targets[:max_price_events]

    fixtures = safe_read_csv(output_dir / 'football_data_upcoming_fixtures.csv')
    targets = add_fixture_targets(fixtures, targets)
    if targets:
        query_source = 'football_data_upcoming_fixtures_fallback'
        return targets[:max_price_events]

    query_source = 'static_fallback'
    return [{'query': 'Tottenham', 'home_team': 'Tottenham', 'away_team': '', 'match_date': None}]


def event_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ['events', 'data', 'results']:
            if isinstance(payload.get(key), list):
                return payload.get(key)
    return []


def odds_response_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        if 'bookmakers' in payload and 'id' in payload:
            return [payload]
        for key in ['events', 'data', 'results', 'odds']:
            if isinstance(payload.get(key), list):
                return payload.get(key)
        values = [v for v in payload.values() if isinstance(v, dict) and 'bookmakers' in v]
        if values:
            return values
    return []


def normalize_events(events, source_label):
    event_meta = {}
    for event in events:
        event_id = event.get('id') or event.get('eventId') or event.get('event_id')
        if event_id is None:
            continue
        event_id = str(event_id)
        home = event.get('home') or event.get('homeTeam') or event.get('home_team')
        away = event.get('away') or event.get('awayTeam') or event.get('away_team')
        date_value = event.get('date') or event.get('startTime') or event.get('commence_time') or event.get('start_time')
        parsed_date, match_date, match_time = parse_datetime(date_value)
        league = None
        if isinstance(event.get('league'), dict):
            league = event['league'].get('slug') or event['league'].get('name')
        league = league or event.get('league') or 'football'
        status = str(event.get('status') or 'unknown').lower()
        event_meta[event_id] = {
            'fixture_id': f'odds_api_io_{event_id}',
            'raw_event_id': event_id,
            'league': league,
            'league_id': league,
            'season': 'upcoming',
            'match_date': match_date,
            'match_time': match_time,
            'parsed_date': parsed_date,
            'home_team': home,
            'away_team': away,
            'source': source_label,
            'event_status': status,
            'fetched_at_utc': fetched_at,
        }
    return [meta for meta in event_meta.values() if meta.get('home_team') and meta.get('away_team')]


def eligible(fixtures):
    return [
        meta for meta in fixtures
        if meta.get('parsed_date') is not None
        and meta['parsed_date'].date() >= today
        and meta.get('event_status') not in {'settled', 'cancelled', 'finished', 'closed'}
    ]


def choose_best_event_for_target(target, event_rows, seen_event_ids):
    candidates = [row for row in eligible(event_rows) if row.get('raw_event_id') not in seen_event_ids]
    best = None
    best_score = 0.0
    for row in candidates:
        score = fixture_confidence(target.get('home_team'), target.get('away_team'), row.get('home_team'), row.get('away_team'))
        date_penalty = 0.0
        if target.get('match_date') and row.get('match_date') and target.get('match_date') != row.get('match_date'):
            date_penalty = 0.08
        adjusted = round(max(score - date_penalty, 0), 4)
        selected = False
        rejection_reason = ''
        if adjusted < min_event_match_confidence:
            rejection_reason = 'below_min_event_match_confidence'
        selection_diag_rows.append({
            'query': target.get('query'),
            'target_home_team': target.get('home_team'),
            'target_away_team': target.get('away_team'),
            'target_match_date': target.get('match_date'),
            'candidate_event_id': row.get('raw_event_id'),
            'candidate_home_team': row.get('home_team'),
            'candidate_away_team': row.get('away_team'),
            'candidate_match_date': row.get('match_date'),
            'event_match_confidence': adjusted,
            'selected': selected,
            'rejection_reason': rejection_reason,
        })
        if adjusted > best_score:
            best = row
            best_score = adjusted
    if best is None or best_score < min_event_match_confidence:
        return None, best_score
    for diag in selection_diag_rows:
        if diag.get('candidate_event_id') == best.get('raw_event_id') and diag.get('query') == target.get('query'):
            diag['selected'] = True
            diag['rejection_reason'] = ''
    best['event_match_confidence'] = best_score
    best['target_home_team'] = target.get('home_team')
    best['target_away_team'] = target.get('away_team')
    return best, best_score


def number(value):
    parsed = pd.to_numeric(value, errors='coerce')
    if pd.isna(parsed):
        return None
    return float(parsed)


def market_is_match_winner(name: str) -> bool:
    text = str(name or '').strip().lower()
    return text in {'ml', 'moneyline', 'match winner', 'match_winner', 'full time result', 'fulltime result', '1x2'}


def extract_three_way_odds(odds_payload):
    bookmaker_payload = odds_payload.get('bookmakers') if isinstance(odds_payload, dict) else None
    if isinstance(bookmaker_payload, dict):
        requested = [item.strip().lower() for item in bookmakers.split(',') if item.strip()]
        ordered_bookmakers = []
        for wanted in requested:
            ordered_bookmakers.extend([name for name in bookmaker_payload.keys() if str(name).lower() == wanted])
        ordered_bookmakers.extend([name for name in bookmaker_payload.keys() if name not in ordered_bookmakers])

        for bookmaker_name in ordered_bookmakers:
            markets = bookmaker_payload.get(bookmaker_name) or []
            if not isinstance(markets, list):
                continue
            preferred_markets = [m for m in markets if market_is_match_winner(m.get('name'))]
            preferred_markets.extend([m for m in markets if m not in preferred_markets])
            for market in preferred_markets:
                odds_items = market.get('odds') or []
                if isinstance(odds_items, dict):
                    odds_items = [odds_items]
                for odds_item in odds_items:
                    if not isinstance(odds_item, dict):
                        continue
                    h = number(odds_item.get('home'))
                    d = number(odds_item.get('draw'))
                    a = number(odds_item.get('away'))
                    if h and d and a and min(h, d, a) > 1:
                        return h, d, a, bookmaker_name, market.get('name')

    candidates = []

    def walk(obj):
        if isinstance(obj, dict):
            lower_keys = {str(k).lower(): k for k in obj.keys()}
            has_home = any(k in lower_keys for k in ['home', '1', 'h'])
            has_draw = any(k in lower_keys for k in ['draw', 'x'])
            has_away = any(k in lower_keys for k in ['away', '2', 'a'])
            if has_home and has_draw and has_away:
                h = number(obj.get(lower_keys.get('home')) or obj.get(lower_keys.get('1')) or obj.get(lower_keys.get('h')))
                d = number(obj.get(lower_keys.get('draw')) or obj.get(lower_keys.get('x')))
                a = number(obj.get(lower_keys.get('away')) or obj.get(lower_keys.get('2')) or obj.get(lower_keys.get('a')))
                if h and d and a and min(h, d, a) > 1:
                    candidates.append((h, d, a, 'unknown_bookmaker', 'unknown_market'))
            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for value in obj:
                walk(value)

    walk(odds_payload)
    return candidates[0] if candidates else (None, None, None, None, None)

search_queries_used = []
selected_bookmakers = []
selected_markets = []
seen_event_ids = set()
selected_events = []

if not api_key:
    errors.append({'stage': 'config', 'error': 'ODDS_API_IO_KEY missing'})
else:
    for target in choose_search_targets():
        if calls_used >= max_calls or len(selected_events) >= max_price_events:
            break
        query = target.get('query')
        try:
            search_queries_used.append(str(query))
            search_url = f"{base_url}/events/search?" + urllib.parse.urlencode({
                'apiKey': api_key,
                'query': query,
            })
            search_payload = get_json(search_url, f"events_search_{len(search_queries_used)}")
            search_rows = normalize_events(event_items(search_payload)[:max_events], 'odds_api_io_events_search')
            fixture_rows.extend(search_rows)
            selected, score = choose_best_event_for_target(target, search_rows, seen_event_ids)
            if selected is None:
                errors.append({'stage': 'event_selection', 'error': f'No event above confidence {min_event_match_confidence} for query {query!r}; best={score}'})
                continue
            seen_event_ids.add(selected['raw_event_id'])
            selected_events.append(selected)
        except Exception as exc:
            errors.append({'stage': 'events_search_or_parse', 'error': repr(exc)})

    if selected_events and calls_used < max_calls:
        try:
            event_ids = ','.join([meta['raw_event_id'] for meta in selected_events[:10]])
            params = {
                'apiKey': api_key,
                'eventIds': event_ids,
                'bookmakers': bookmakers,
            }
            multi_url = f"{base_url}/odds/multi?" + urllib.parse.urlencode(params)
            multi_payload = get_json(multi_url, 'odds_multi')
            odds_items = odds_response_items(multi_payload)
            odds_by_id = {str(item.get('id') or item.get('eventId') or item.get('event_id')): item for item in odds_items if isinstance(item, dict)}

            for meta in selected_events:
                odds_payload = odds_by_id.get(str(meta['raw_event_id']))
                if odds_payload is None and len(selected_events) == 1 and isinstance(multi_payload, dict) and 'bookmakers' in multi_payload:
                    odds_payload = multi_payload
                if odds_payload is None:
                    errors.append({'stage': 'multi_odds_match', 'error': f'No multi-odds payload matched event {meta.get("raw_event_id")}'})
                    continue
                home_odds, draw_odds, away_odds, selected_bookmaker, selected_market = extract_three_way_odds(odds_payload)
                if home_odds:
                    selected_bookmakers.append(str(selected_bookmaker))
                    selected_markets.append(str(selected_market))
                    rows.append({
                        'fixture_id': meta.get('fixture_id'),
                        'match_date': meta.get('match_date'),
                        'match_time': meta.get('match_time'),
                        'home_team': meta.get('home_team'),
                        'away_team': meta.get('away_team'),
                        'league': meta.get('league'),
                        'source_name': f'odds_api_io_{selected_bookmaker}_{selected_market}',
                        'source_type': 'free_api_market_proxy',
                        'market_home_odds': round(home_odds, 4),
                        'market_draw_odds': round(draw_odds, 4),
                        'market_away_odds': round(away_odds, 4),
                        'price_captured_at_utc': fetched_at,
                        'source_quality': 'free_api_market_proxy_capped_multi_event_call',
                        'raw_source_url': 'https://api.odds-api.io/v3/odds/multi',
                    })
                else:
                    errors.append({'stage': 'odds_parse', 'error': f'No 1X2 odds found in multi-odds payload for event {meta.get("raw_event_id")}'})
        except Exception as exc:
            errors.append({'stage': 'multi_odds_request_or_parse', 'error': repr(exc)})

prices = pd.DataFrame(rows)
for col in price_columns:
    if col not in prices.columns:
        prices[col] = None
prices = prices[price_columns]
prices.to_csv(raw_dir / 'odds_api_io_forward_prices.csv', index=False)
prices.to_csv(output_dir / 'odds_api_io_forward_prices.csv', index=False)

fixtures = pd.DataFrame(fixture_rows)
if len(fixtures):
    fixtures = fixtures.drop_duplicates(['fixture_id'], keep='first')
for col in fixture_columns:
    if col not in fixtures.columns:
        fixtures[col] = None
fixtures = fixtures[fixture_columns]
fixtures.to_csv(raw_dir / 'odds_api_io_forward_fixtures.csv', index=False)
fixtures.to_csv(output_dir / 'odds_api_io_forward_fixtures.csv', index=False)

selection_diag = pd.DataFrame(selection_diag_rows)
for col in selection_diag_columns:
    if col not in selection_diag.columns:
        selection_diag[col] = None
selection_diag = selection_diag[selection_diag_columns]
selection_diag.to_csv(raw_dir / 'odds_api_io_event_selection_diagnostics.csv', index=False)
selection_diag.to_csv(output_dir / 'odds_api_io_event_selection_diagnostics.csv', index=False)

rate_df = pd.DataFrame(rate_limit_rows)
rate_df.to_csv(raw_dir / 'odds_api_io_rate_limit_headers.csv', index=False)
rate_df.to_csv(output_dir / 'odds_api_io_rate_limit_headers.csv', index=False)
latest_rate = rate_limit_rows[-1] if rate_limit_rows else {}

summary = {
    'enabled': bool(api_key),
    'calls_used': calls_used,
    'max_calls': max_calls,
    'max_events': max_events,
    'max_price_events': max_price_events,
    'min_event_match_confidence': min_event_match_confidence,
    'discovery_mode': discovery_mode,
    'query_source': query_source,
    'search_queries_used': ', '.join(search_queries_used),
    'selected_event_ids': ', '.join([meta['raw_event_id'] for meta in selected_events]),
    'fixture_rows': int(len(fixtures)),
    'event_selection_diagnostic_rows': int(len(selection_diag)),
    'selected_event_rows': int(len(selected_events)),
    'priced_event_rows': int(len(prices)),
    'price_rows': int(len(prices)),
    'errors': int(len(errors)),
    'bookmakers_param_mode': 'explicit_selected_bookmakers',
    'bookmakers_requested': bookmakers,
    'odds_endpoint_mode': 'multi_event_documented_endpoint',
    'odds_parse_mode': parse_mode,
    'selected_bookmakers': ', '.join(sorted(set(selected_bookmakers))),
    'selected_markets': ', '.join(sorted(set(selected_markets))),
    'rate_limit_header_rows': int(len(rate_limit_rows)),
    'latest_rate_limit_limit': latest_rate.get('x_ratelimit_limit'),
    'latest_rate_limit_remaining': latest_rate.get('x_ratelimit_remaining'),
    'latest_rate_limit_reset': latest_rate.get('x_ratelimit_reset'),
    'latest_retry_after': latest_rate.get('retry_after'),
    'source_quality': 'free_api_market_proxy_capped_multi_call',
}
pd.DataFrame([summary]).to_csv(output_dir / 'odds_api_io_forward_price_status.csv', index=False)

markdown = [
    '# odds-api.io Forward Price Fetch',
    '',
    'Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.',
    'Prioritizes model-covered forward fixtures, selects searched events by home/away match confidence, then uses documented /v3/odds/multi for selected events.',
    'Parses documented EventResponse.bookmakers -> markets -> odds -> home/draw/away schema.',
    'Captures provider rate-limit headers from each authenticated API response.',
    'Not real-money ready until validated against forward results and other sources.',
    '',
    f"Enabled: {summary['enabled']}",
    f"Calls used: {summary['calls_used']} / {summary['max_calls']}",
    f"Max events per search: {summary['max_events']}",
    f"Max priced events: {summary['max_price_events']}",
    f"Minimum event match confidence: {summary['min_event_match_confidence']}",
    f"Discovery mode: {summary['discovery_mode']}",
    f"Query source: {summary['query_source']}",
    f"Search queries used: {summary['search_queries_used']}",
    f"Selected event IDs: {summary['selected_event_ids']}",
    f"Bookmakers parameter mode: {summary['bookmakers_param_mode']}",
    f"Bookmakers requested: {summary['bookmakers_requested']}",
    f"Odds endpoint mode: {summary['odds_endpoint_mode']}",
    f"Odds parse mode: {summary['odds_parse_mode']}",
    f"Selected bookmakers: {summary['selected_bookmakers']}",
    f"Selected markets: {summary['selected_markets']}",
    f"Fixture rows: {summary['fixture_rows']}",
    f"Event selection diagnostic rows: {summary['event_selection_diagnostic_rows']}",
    f"Selected event rows: {summary['selected_event_rows']}",
    f"Priced event rows: {summary['priced_event_rows']}",
    f"Price rows: {summary['price_rows']}",
    f"Errors/status rows: {summary['errors']}",
    '',
    '## Provider rate-limit headers',
    '',
    f"Header rows captured: {summary['rate_limit_header_rows']}",
    f"Latest x-ratelimit-limit: {summary['latest_rate_limit_limit']}",
    f"Latest x-ratelimit-remaining: {summary['latest_rate_limit_remaining']}",
    f"Latest x-ratelimit-reset: {summary['latest_rate_limit_reset']}",
    f"Latest retry-after: {summary['latest_retry_after']}",
    '',
]
if len(prices):
    for _, row in prices.head(20).iterrows():
        markdown.append(f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | {row['source_name']} | {row['market_home_odds']}/{row['market_draw_odds']}/{row['market_away_odds']}")
if len(selection_diag):
    markdown.extend(['', '## Event selection diagnostics', ''])
    for _, row in selection_diag.sort_values('event_match_confidence', ascending=False).head(20).iterrows():
        markdown.append(
            f"- query={row['query']} | target={row['target_home_team']} vs {row['target_away_team']} | "
            f"candidate={row['candidate_home_team']} vs {row['candidate_away_team']} | confidence={row['event_match_confidence']} | selected={row['selected']} | reason={row['rejection_reason']}"
        )
if errors:
    markdown.extend(['', '## Errors / Status', ''])
    for error in errors[:10]:
        markdown.append(f"- {error['stage']}: {error['error']}")

(output_dir / 'odds_api_io_forward_prices.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
