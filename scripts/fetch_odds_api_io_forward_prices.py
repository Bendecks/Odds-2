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
max_events = int(os.getenv('ODDS_API_IO_MAX_EVENTS', '8'))
max_calls = int(os.getenv('ODDS_API_IO_MAX_CALLS', '2'))
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
discovery_mode = 'events_endpoint_then_targeted_search_fallback'


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


def choose_search_query() -> str:
    if search_query:
        return search_query
    fixtures = safe_read_csv(output_dir / 'football_data_upcoming_fixtures.csv')
    if len(fixtures):
        fixtures['parsed_date'] = pd.to_datetime(fixtures.get('match_date'), errors='coerce', utc=True)
        upcoming = fixtures[fixtures['parsed_date'].dt.date >= today].copy()
        if len(upcoming):
            for col in ['home_team', 'away_team']:
                value = str(upcoming.iloc[0].get(col) or '').strip()
                if len(value) >= 3:
                    return value
    return 'Tottenham'


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


def extract_three_way_odds(odds_payload):
    candidates = []

    def walk(obj):
        if isinstance(obj, dict):
            lower_keys = {str(k).lower(): k for k in obj.keys()}
            has_home = any(k in lower_keys for k in ['home', '1', 'h'])
            has_draw = any(k in lower_keys for k in ['draw', 'x'])
            has_away = any(k in lower_keys for k in ['away', '2', 'a'])
            if has_home and has_draw and has_away:
                h = obj.get(lower_keys.get('home')) or obj.get(lower_keys.get('1')) or obj.get(lower_keys.get('h'))
                d = obj.get(lower_keys.get('draw')) or obj.get(lower_keys.get('x'))
                a = obj.get(lower_keys.get('away')) or obj.get(lower_keys.get('2')) or obj.get(lower_keys.get('a'))
                h = pd.to_numeric(h, errors='coerce')
                d = pd.to_numeric(d, errors='coerce')
                a = pd.to_numeric(a, errors='coerce')
                if pd.notna(h) and pd.notna(d) and pd.notna(a) and min(h, d, a) > 1:
                    candidates.append((float(h), float(d), float(a)))
            for value in obj.values():
                walk(value)
        elif isinstance(obj, list):
            for value in obj:
                walk(value)

    walk(odds_payload)
    return candidates[0] if candidates else (None, None, None)

eligible_rows = []
used_search_query = None

if not api_key:
    errors.append({'stage': 'config', 'error': 'ODDS_API_IO_KEY missing'})
else:
    try:
        events_url = f"{base_url}/events?" + urllib.parse.urlencode({
            'apiKey': api_key,
            'sport': 'football',
            'limit': max_events,
        })
        events_payload = get_json(events_url, 'events')
        event_rows = normalize_events(event_items(events_payload)[:max_events], 'odds_api_io_events')
        fixture_rows.extend(event_rows)
        eligible_rows = eligible(event_rows)

        if not eligible_rows and calls_used < max_calls:
            used_search_query = choose_search_query()
            search_url = f"{base_url}/events/search?" + urllib.parse.urlencode({
                'apiKey': api_key,
                'query': used_search_query,
            })
            search_payload = get_json(search_url, 'events_search_fallback')
            search_rows = normalize_events(event_items(search_payload)[:max_events], 'odds_api_io_events_search_fallback')
            fixture_rows.extend(search_rows)
            eligible_rows = eligible(search_rows)

        if not eligible_rows:
            errors.append({'stage': 'event_selection', 'error': 'No future non-settled event available from documented events endpoint or targeted search fallback; skipped odds call'})

        if eligible_rows and calls_used < max_calls:
            try:
                meta = eligible_rows[0]
                params = {
                    'apiKey': api_key,
                    'eventId': meta['raw_event_id'],
                    'bookmakers': bookmakers,
                }
                odds_url = f"{base_url}/odds?" + urllib.parse.urlencode(params)
                odds_payload = get_json(odds_url, f"odds_{meta['raw_event_id']}")
                home_odds, draw_odds, away_odds = extract_three_way_odds(odds_payload)
                if home_odds:
                    rows.append({
                        'fixture_id': meta.get('fixture_id'),
                        'match_date': meta.get('match_date'),
                        'match_time': meta.get('match_time'),
                        'home_team': meta.get('home_team'),
                        'away_team': meta.get('away_team'),
                        'league': meta.get('league'),
                        'source_name': 'odds_api_io_single_event_proxy',
                        'source_type': 'free_api_market_proxy',
                        'market_home_odds': round(home_odds, 4),
                        'market_draw_odds': round(draw_odds, 4),
                        'market_away_odds': round(away_odds, 4),
                        'price_captured_at_utc': fetched_at,
                        'source_quality': 'free_api_market_proxy_capped_single_event_call',
                        'raw_source_url': 'https://api.odds-api.io/v3/odds',
                    })
                else:
                    errors.append({'stage': 'odds_parse', 'error': 'No 1X2 odds found in single-event odds response'})
            except Exception as exc:
                errors.append({'stage': 'odds_request_or_parse', 'error': repr(exc)})
    except Exception as exc:
        errors.append({'stage': 'events_or_parse', 'error': repr(exc)})

prices = pd.DataFrame(rows)
for col in price_columns:
    if col not in prices.columns:
        prices[col] = None
prices = prices[price_columns]
prices.to_csv(raw_dir / 'odds_api_io_forward_prices.csv', index=False)
prices.to_csv(output_dir / 'odds_api_io_forward_prices.csv', index=False)

fixtures = pd.DataFrame(fixture_rows)
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
    'discovery_mode': discovery_mode,
    'search_query_used': used_search_query,
    'fixture_rows': int(len(fixtures)),
    'eligible_future_fixture_rows': int(len(eligible_rows)),
    'price_rows': int(len(prices)),
    'errors': int(len(errors)),
    'bookmakers_param_mode': 'explicit_selected_bookmakers',
    'bookmakers_requested': bookmakers,
    'odds_endpoint_mode': 'single_event_documented_endpoint',
    'source_quality': 'free_api_market_proxy_capped_calls',
}
pd.DataFrame([summary]).to_csv(output_dir / 'odds_api_io_forward_price_status.csv', index=False)

markdown = [
    '# odds-api.io Forward Price Fetch',
    '',
    'Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.',
    'Uses documented /v3/events with sport+limit first; if no future event is found, uses one targeted /v3/events/search fallback. With max_calls=2 this prevents odds calls when discovery fails.',
    'Not real-money ready until validated against forward results and other sources.',
    '',
    f"Enabled: {summary['enabled']}",
    f"Calls used: {summary['calls_used']} / {summary['max_calls']}",
    f"Max events: {summary['max_events']}",
    f"Discovery mode: {summary['discovery_mode']}",
    f"Search query used: {summary['search_query_used']}",
    f"Bookmakers parameter mode: {summary['bookmakers_param_mode']}",
    f"Bookmakers requested: {summary['bookmakers_requested']}",
    f"Odds endpoint mode: {summary['odds_endpoint_mode']}",
    f"Fixture rows: {summary['fixture_rows']}",
    f"Eligible future fixture rows: {summary['eligible_future_fixture_rows']}",
    f"Price rows: {summary['price_rows']}",
    f"Errors/status rows: {summary['errors']}",
    '',
]
if len(prices):
    for _, row in prices.head(20).iterrows():
        markdown.append(f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | {row['market_home_odds']}/{row['market_draw_odds']}/{row['market_away_odds']}")
if errors:
    markdown.extend(['', '## Errors / Status', ''])
    for error in errors[:10]:
        markdown.append(f"- {error['stage']}: {error['error']}")

(output_dir / 'odds_api_io_forward_prices.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
