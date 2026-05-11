import json
import runpy
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

raw_dir = Path('data/raw/upcoming')
output_dir = Path('output/latest')
raw_dir.mkdir(parents=True, exist_ok=True)
output_dir.mkdir(parents=True, exist_ok=True)

LEAGUES = {
    'premier_league': {
        'id': '4328',
        'url': 'https://www.thesportsdb.com/api/v1/json/3/eventsnextleague.php?id=4328',
    },
}

rows = []
errors = []
fetched_at = datetime.now(timezone.utc).isoformat()

for league, cfg in LEAGUES.items():
    try:
        with urllib.request.urlopen(cfg['url'], timeout=30) as response:
            payload = json.loads(response.read().decode('utf-8'))
        events = payload.get('events') or []
    except Exception as exc:
        errors.append({'league': league, 'error': repr(exc)})
        events = []

    for event in events:
        rows.append({
            'fixture_id': event.get('idEvent'),
            'league': league,
            'league_id': cfg['id'],
            'season': event.get('strSeason'),
            'match_date': event.get('dateEvent'),
            'match_time': event.get('strTime'),
            'home_team': event.get('strHomeTeam'),
            'away_team': event.get('strAwayTeam'),
            'source': 'thesportsdb_eventsnextleague',
            'fetched_at_utc': fetched_at,
        })

fixtures = pd.DataFrame(rows)
expected_columns = [
    'fixture_id', 'league', 'league_id', 'season', 'match_date', 'match_time',
    'home_team', 'away_team', 'source', 'fetched_at_utc'
]
for col in expected_columns:
    if col not in fixtures.columns:
        fixtures[col] = None
fixtures = fixtures[expected_columns]

fixtures.to_parquet(raw_dir / 'upcoming_fixtures.parquet', index=False)
fixtures.to_csv(raw_dir / 'upcoming_fixtures.csv', index=False)
fixtures.to_csv(output_dir / 'upcoming_fixtures.csv', index=False)

markdown = [
    '# Upcoming Fixtures',
    '',
    'Fixture source: TheSportsDB eventsnextleague API.',
    'Odds source: not included. Manual odds fallback is parked; automatic forward price source remains the active target.',
    '',
    f'Fixtures found: {len(fixtures)}',
    '',
]

if len(fixtures):
    for _, row in fixtures.iterrows():
        markdown.append(
            f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | {row['league']}"
        )
else:
    markdown.append('No upcoming fixtures returned.')

if errors:
    markdown.extend(['', '## Errors', ''])
    for error in errors:
        markdown.append(f"- {error['league']}: {error['error']}")

(output_dir / 'upcoming_fixtures.md').write_text('\n'.join(markdown), encoding='utf-8')

result_script = Path('scripts/fetch_forward_fixture_results.py')
if result_script.exists():
    try:
        runpy.run_path(str(result_script), run_name='__main__')
    except Exception as exc:
        print(f'Forward fixture result fetch skipped: {exc!r}')

print(f'Fetched {len(fixtures)} upcoming fixtures')
