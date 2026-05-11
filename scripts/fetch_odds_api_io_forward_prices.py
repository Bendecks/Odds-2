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

price_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'source_name', 'source_type', 'market_home_odds', 'market_draw_odds',
    'market_away_odds', 'price_captured_at_utc', 'source_quality', 'raw_source_url'
]
fixture_columns = [
    'fixture_id', 'league', 'league_id', 'season', 'match_date', 'match_time',
    'home_team', 'away_team', 'source', 'fetched_at_utc'
]

rows = []
fixture_rows = []
errors = []
calls_used = 0
fetched_at = datetime.now(timezone.utc).isoformat()


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


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', utc=True)
    if pd.isna(parsed):
        return None, None
    return parsed.date().isoformat(), parsed.time().isoformat(timespec='minutes')


def event_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ['events', 'data', 'results']:
            if isinstance(payload.get(key), list):
                return payload.get(key)
    return []


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
        events = event_items(events_payload)[:max_events]

        event_meta = {}
        for event in events:
            event_id = event.get('id') or event.get('eventId') or event.get('event_id')
            if event_id is None:
                continue
            event_id = str(event_id)
            home = event.get('home') or event.get('homeTeam') or event.get('home_team')
            away = event.get('away') or event.get('awayTeam') or event.get('away_team')
            date_value = event.get('date') or event.get('startTime') or event.get('commence_time') or event.get('start_time')
            match_date, match_time = parse_date(date_value)
            league = None
            if isinstance(event.get('league'), dict):
                league = event['league'].get('slug') or event['league'].get('name')
            league = league or event.get('league') or 'football'
            event_meta[event_id] = {
                'fixture_id': f'odds_api_io_{event_id}',
                'raw_event_id': event_id,
                'league': league,
                'league_id': league,
                'season': 'upcoming',
                'match_date': match_date,
                'match_time': match_time,
                'home_team': home,
                'away_team': away,
                'source': 'odds_api_io_events',
                'fetched_at_utc': fetched_at,
            }
        fixture_rows = [meta for meta in event_meta.values() if meta.get('home_team') and meta.get('away_team')]

        # Use documented single-event endpoint. With max_calls=2 this means one events call + one odds call.
        if fixture_rows and calls_used < max_calls:
            try:
                meta = fixture_rows[0]
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
        errors.append({'stage': 'events_request_or_parse', 'error': repr(exc)})

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
    'fixture_rows': int(len(fixtures)),
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
    'Uses the documented single-event /v3/odds endpoint: one events call plus one odds call by default.',
    'Not real-money ready until validated against forward results and other sources.',
    '',
    f"Enabled: {summary['enabled']}",
    f"Calls used: {summary['calls_used']} / {summary['max_calls']}",
    f"Max events: {summary['max_events']}",
    f"Bookmakers parameter mode: {summary['bookmakers_param_mode']}",
    f"Bookmakers requested: {summary['bookmakers_requested']}",
    f"Odds endpoint mode: {summary['odds_endpoint_mode']}",
    f"Fixture rows: {summary['fixture_rows']}",
    f"Price rows: {summary['price_rows']}",
    f"Errors: {summary['errors']}",
    '',
]
if len(prices):
    for _, row in prices.head(20).iterrows():
        markdown.append(f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | {row['market_home_odds']}/{row['market_draw_odds']}/{row['market_away_odds']}")
if errors:
    markdown.extend(['', '## Errors', ''])
    for error in errors[:10]:
        markdown.append(f"- {error['stage']}: {error['error']}")

(output_dir / 'odds_api_io_forward_prices.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
