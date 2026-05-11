import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
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

rows = []
fixture_rows = []
errors = []
calls_used = 0
fetched_at = datetime.now(timezone.utc).isoformat()
today = datetime.now(timezone.utc).date()
discovery_mode = 'multi_targeted_events_search_then_single_event_odds'
parse_mode = 'bookmakers_market_odds_schema'


def get_json(url: str, label: str):
    global calls_used
    if calls_used >= max_calls:
        raise RuntimeError('ODDS_API_IO_MAX_CALLS reached')
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            calls_used += 1
            text = response.read().decode('utf-8')
            (raw_dir / f'{label}_latest.json').write_text(text, encoding='utf-8')
            return json.loads(text)
    except urllib.error.HTTPError as exc:
        calls_used += 1
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


def choose_search_queries() -> list[str]:
    if search_query:
        return [q.strip() for q in search_query.split(',') if len(q.strip()) >= 3][:max_price_events]
    fixtures = safe_read_csv(output_dir / 'football_data_upcoming_fixtures.csv')
    queries = []
    if len(fixtures):
        fixtures['parsed_date'] = pd.to_datetime(fixtures.get('match_date'), errors='coerce', utc=True)
        upcoming = fixtures[fixtures['parsed_date'].dt.date >= today].copy()
        if 'match_time' in upcoming.columns:
            upcoming = upcoming.sort_values(['parsed_date', 'match_time'], na_position='last')
        else:
            upcoming = upcoming.sort_values(['parsed_date'], na_position='last')
        for _, fixture in upcoming.iterrows():
            for col in ['home_team', 'away_team']:
                value = str(fixture.get(col) or '').strip()
                if len(value) >= 3 and value.lower() not in {q.lower() for q in queries}:
                    queries.append(value)
                    break
            if len(queries) >= max_price_events:
                break
    if not queries:
        queries = ['Tottenham']
    return queries[:max_price_events]


def parse_datetime(value):
    parsed = pd.to_datetime(value, errors='coerce', utc=True)
    if pd.isna(parsed):
        return None, None, None
    return parsed, parsed.date().isoformat(), parsed.time().isoformat(timespec='minutes')


def event_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ['events', 'data', 'results']:
            if isinstance(payload.get(key), list):
                return payload.get(key)
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

if not api_key:
    errors.append({'stage': 'config', 'error': 'ODDS_API_IO_KEY missing'})
else:
    for query in choose_search_queries():
        if calls_used >= max_calls or len(rows) >= max_price_events:
            break
        try:
            search_queries_used.append(query)
            search_url = f"{base_url}/events/search?" + urllib.parse.urlencode({
                'apiKey': api_key,
                'query': query,
            })
            search_payload = get_json(search_url, f"events_search_{len(search_queries_used)}")
            search_rows = normalize_events(event_items(search_payload)[:max_events], 'odds_api_io_events_search')
            fixture_rows.extend(search_rows)
            eligible_rows = [row for row in eligible(search_rows) if row.get('raw_event_id') not in seen_event_ids]

            if not eligible_rows:
                errors.append({'stage': 'event_selection', 'error': f'No future non-settled event available from targeted search query {query!r}; skipped odds call'})
                continue

            if calls_used >= max_calls:
                break
            meta = eligible_rows[0]
            seen_event_ids.add(meta['raw_event_id'])
            try:
                params = {
                    'apiKey': api_key,
                    'eventId': meta['raw_event_id'],
                    'bookmakers': bookmakers,
                }
                odds_url = f"{base_url}/odds?" + urllib.parse.urlencode(params)
                odds_payload = get_json(odds_url, f"odds_{meta['raw_event_id']}")
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
                        'source_quality': 'free_api_market_proxy_capped_single_event_call',
                        'raw_source_url': 'https://api.odds-api.io/v3/odds',
                    })
                else:
                    errors.append({'stage': 'odds_parse', 'error': f'No 1X2 odds found for event {meta.get("raw_event_id")} from query {query!r}'})
            except Exception as exc:
                errors.append({'stage': 'odds_request_or_parse', 'error': repr(exc)})
        except Exception as exc:
            errors.append({'stage': 'events_search_or_parse', 'error': repr(exc)})

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

summary = {
    'enabled': bool(api_key),
    'calls_used': calls_used,
    'max_calls': max_calls,
    'max_events': max_events,
    'max_price_events': max_price_events,
    'discovery_mode': discovery_mode,
    'search_queries_used': ', '.join(search_queries_used),
    'fixture_rows': int(len(fixtures)),
    'priced_event_rows': int(len(prices)),
    'price_rows': int(len(prices)),
    'errors': int(len(errors)),
    'bookmakers_param_mode': 'explicit_selected_bookmakers',
    'bookmakers_requested': bookmakers,
    'odds_endpoint_mode': 'single_event_documented_endpoint',
    'odds_parse_mode': parse_mode,
    'selected_bookmakers': ', '.join(sorted(set(selected_bookmakers))),
    'selected_markets': ', '.join(sorted(set(selected_markets))),
    'source_quality': 'free_api_market_proxy_capped_calls',
}
pd.DataFrame([summary]).to_csv(output_dir / 'odds_api_io_forward_price_status.csv', index=False)

markdown = [
    '# odds-api.io Forward Price Fetch',
    '',
    'Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.',
    'Uses documented /v3/events/search for multiple targeted upcoming-event queries, then /v3/odds for at most one event per query.',
    'Parses documented EventResponse.bookmakers -> markets -> odds -> home/draw/away schema.',
    'Not real-money ready until validated against forward results and other sources.',
    '',
    f"Enabled: {summary['enabled']}",
    f"Calls used: {summary['calls_used']} / {summary['max_calls']}",
    f"Max events per search: {summary['max_events']}",
    f"Max priced events: {summary['max_price_events']}",
    f"Discovery mode: {summary['discovery_mode']}",
    f"Search queries used: {summary['search_queries_used']}",
    f"Bookmakers parameter mode: {summary['bookmakers_param_mode']}",
    f"Bookmakers requested: {summary['bookmakers_requested']}",
    f"Odds endpoint mode: {summary['odds_endpoint_mode']}",
    f"Odds parse mode: {summary['odds_parse_mode']}",
    f"Selected bookmakers: {summary['selected_bookmakers']}",
    f"Selected markets: {summary['selected_markets']}",
    f"Fixture rows: {summary['fixture_rows']}",
    f"Priced event rows: {summary['priced_event_rows']}",
    f"Price rows: {summary['price_rows']}",
    f"Errors/status rows: {summary['errors']}",
    '',
]
if len(prices):
    for _, row in prices.head(20).iterrows():
        markdown.append(f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | {row['source_name']} | {row['market_home_odds']}/{row['market_draw_odds']}/{row['market_away_odds']}")
if errors:
    markdown.extend(['', '## Errors / Status', ''])
    for error in errors[:10]:
        markdown.append(f"- {error['stage']}: {error['error']}")

(output_dir / 'odds_api_io_forward_prices.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
