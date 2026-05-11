import json
import os
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
raw_dir = Path('data/raw/api_football')
raw_dir.mkdir(parents=True, exist_ok=True)
output_dir.mkdir(parents=True, exist_ok=True)

api_key = os.getenv('API_FOOTBALL_KEY')
max_calls = int(os.getenv('API_FOOTBALL_MAX_CALLS', '0'))
max_fixtures = int(os.getenv('API_FOOTBALL_MAX_FIXTURES', '5'))
base_url = 'https://v3.football.api-sports.io'

# Disabled by default because the free quota is only 100 requests/day.
# To test: set API_FOOTBALL_MAX_CALLS=1 or 2 in workflow/env.

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


def get_json(path: str, params: dict):
    global calls_used
    if calls_used >= max_calls:
        raise RuntimeError('API_FOOTBALL_MAX_CALLS reached')
    url = f"{base_url}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={'x-apisports-key': api_key})
    with urllib.request.urlopen(req, timeout=30) as response:
        calls_used += 1
        return json.loads(response.read().decode('utf-8'))


def parse_fixture(item: dict):
    fixture = item.get('fixture') or {}
    teams = item.get('teams') or {}
    league = item.get('league') or {}
    home = (teams.get('home') or {}).get('name')
    away = (teams.get('away') or {}).get('name')
    date_value = fixture.get('date')
    parsed = pd.to_datetime(date_value, errors='coerce', utc=True)
    match_date = parsed.date().isoformat() if pd.notna(parsed) else None
    match_time = parsed.time().isoformat(timespec='minutes') if pd.notna(parsed) else None
    fixture_id = fixture.get('id')
    return {
        'fixture_id': f'api_football_{fixture_id}' if fixture_id is not None else None,
        'league': league.get('name'),
        'league_id': league.get('id'),
        'season': league.get('season'),
        'match_date': match_date,
        'match_time': match_time,
        'home_team': home,
        'away_team': away,
        'source': 'api_football_fixtures',
        'fetched_at_utc': fetched_at,
        'raw_fixture_id': fixture_id,
    }


def extract_1x2(odds_item: dict):
    bookmakers = odds_item.get('bookmakers') or []
    for bookmaker in bookmakers:
        bets = bookmaker.get('bets') or []
        for bet in bets:
            name = str(bet.get('name') or '').lower()
            if name not in ['match winner', '1x2', 'fulltime result']:
                continue
            values = bet.get('values') or []
            parsed = {}
            for value in values:
                key = str(value.get('value') or '').lower()
                odd = pd.to_numeric(value.get('odd'), errors='coerce')
                if pd.isna(odd):
                    continue
                if key in ['home', '1']:
                    parsed['home'] = float(odd)
                elif key in ['draw', 'x']:
                    parsed['draw'] = float(odd)
                elif key in ['away', '2']:
                    parsed['away'] = float(odd)
            if {'home', 'draw', 'away'}.issubset(parsed):
                return parsed['home'], parsed['draw'], parsed['away'], bookmaker.get('name')
    return None, None, None, None

if not api_key:
    errors.append({'stage': 'config', 'error': 'API_FOOTBALL_KEY missing'})
elif max_calls <= 0:
    errors.append({'stage': 'disabled', 'error': 'API_FOOTBALL_MAX_CALLS is 0; no calls made by design'})
else:
    try:
        today = datetime.now(timezone.utc).date().isoformat()
        fixtures_payload = get_json('/fixtures', {'date': today, 'timezone': 'UTC'})
        (raw_dir / 'fixtures_latest.json').write_text(json.dumps(fixtures_payload, indent=2), encoding='utf-8')
        fixtures = fixtures_payload.get('response') or []
        for item in fixtures[:max_fixtures]:
            meta = parse_fixture(item)
            if meta.get('fixture_id') and meta.get('home_team') and meta.get('away_team'):
                fixture_rows.append(meta)

        # This endpoint can be expensive under free quota. Only call it if budget remains.
        if fixture_rows and calls_used < max_calls:
            for meta in fixture_rows[:max_fixtures]:
                if calls_used >= max_calls:
                    break
                raw_id = meta.get('raw_fixture_id')
                if raw_id is None:
                    continue
                odds_payload = get_json('/odds', {'fixture': raw_id})
                (raw_dir / f'odds_{raw_id}.json').write_text(json.dumps(odds_payload, indent=2), encoding='utf-8')
                for odds_item in odds_payload.get('response') or []:
                    h, d, a, bookmaker = extract_1x2(odds_item)
                    if h and d and a:
                        rows.append({
                            'fixture_id': meta.get('fixture_id'),
                            'match_date': meta.get('match_date'),
                            'match_time': meta.get('match_time'),
                            'home_team': meta.get('home_team'),
                            'away_team': meta.get('away_team'),
                            'league': meta.get('league'),
                            'source_name': f'api_football_{bookmaker or "bookmaker"}',
                            'source_type': 'free_api_market_proxy',
                            'market_home_odds': round(float(h), 4),
                            'market_draw_odds': round(float(d), 4),
                            'market_away_odds': round(float(a), 4),
                            'price_captured_at_utc': fetched_at,
                            'source_quality': 'free_api_market_proxy_disabled_by_default',
                            'raw_source_url': 'https://v3.football.api-sports.io/odds',
                        })
                        break
    except Exception as exc:
        errors.append({'stage': 'request_or_parse', 'error': repr(exc)})

prices = pd.DataFrame(rows)
for col in price_columns:
    if col not in prices.columns:
        prices[col] = None
prices = prices[price_columns]
prices.to_csv(raw_dir / 'api_football_forward_prices.csv', index=False)
prices.to_csv(output_dir / 'api_football_forward_prices.csv', index=False)

fixtures = pd.DataFrame(fixture_rows)
for col in fixture_columns:
    if col not in fixtures.columns:
        fixtures[col] = None
fixtures = fixtures[fixture_columns]
fixtures.to_csv(raw_dir / 'api_football_forward_fixtures.csv', index=False)
fixtures.to_csv(output_dir / 'api_football_forward_fixtures.csv', index=False)

summary = {
    'enabled': bool(api_key),
    'calls_used': calls_used,
    'max_calls': max_calls,
    'max_fixtures': max_fixtures,
    'fixture_rows': int(len(fixtures)),
    'price_rows': int(len(prices)),
    'errors': int(len(errors)),
    'source_quality': 'free_api_market_proxy_disabled_by_default',
}
pd.DataFrame([summary]).to_csv(output_dir / 'api_football_forward_price_status.csv', index=False)

markdown = [
    '# API-Football Forward Price Fetch',
    '',
    'Optional API source. Disabled by default because free quota is limited.',
    'Set API_FOOTBALL_MAX_CALLS=1 or 2 only for controlled tests.',
    '',
    f"Enabled: {summary['enabled']}",
    f"Calls used: {summary['calls_used']} / {summary['max_calls']}",
    f"Max fixtures: {summary['max_fixtures']}",
    f"Fixture rows: {summary['fixture_rows']}",
    f"Price rows: {summary['price_rows']}",
    f"Errors/status rows: {summary['errors']}",
    '',
]
if len(prices):
    for _, row in prices.head(20).iterrows():
        markdown.append(f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | {row['market_home_odds']}/{row['market_draw_odds']}/{row['market_away_odds']}")
if errors:
    markdown.extend(['', '## Status / Errors', ''])
    for error in errors[:10]:
        markdown.append(f"- {error['stage']}: {error['error']}")

(output_dir / 'api_football_forward_prices.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
