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

expected_columns = [
    'fixture_id', 'league', 'league_id', 'season', 'match_date', 'match_time',
    'home_team', 'away_team', 'source', 'fetched_at_utc'
]

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

# Run Football-Data proxy fetcher before merging its fixture output.
football_data_script = Path('scripts/fetch_football_data_upcoming_odds.py')
if football_data_script.exists():
    try:
        runpy.run_path(str(football_data_script), run_name='__main__')
    except Exception as exc:
        print(f'{football_data_script} skipped: {exc!r}')

football_data_fixtures_path = output_dir / 'football_data_upcoming_fixtures.csv'
if football_data_fixtures_path.exists() and football_data_fixtures_path.stat().st_size > 0:
    try:
        fd_fixtures = pd.read_csv(football_data_fixtures_path)
        for col in expected_columns:
            if col not in fd_fixtures.columns:
                fd_fixtures[col] = None
        rows.extend(fd_fixtures[expected_columns].to_dict(orient='records'))
    except Exception as exc:
        errors.append({'league': 'football_data_fixtures_proxy', 'error': repr(exc)})

fixtures = pd.DataFrame(rows)
for col in expected_columns:
    if col not in fixtures.columns:
        fixtures[col] = None
fixtures = fixtures[expected_columns]
fixtures = fixtures.dropna(subset=['home_team', 'away_team', 'match_date']).drop_duplicates(['match_date', 'home_team', 'away_team'])

fixtures.to_parquet(raw_dir / 'upcoming_fixtures.parquet', index=False)
fixtures.to_csv(raw_dir / 'upcoming_fixtures.csv', index=False)
fixtures.to_csv(output_dir / 'upcoming_fixtures.csv', index=False)

source_counts = fixtures['source'].value_counts().to_dict() if len(fixtures) and 'source' in fixtures.columns else {}
summary = {
    'fixture_rows': int(len(fixtures)),
    'source_counts': json.dumps(source_counts, sort_keys=True),
    'errors': int(len(errors)),
}
pd.DataFrame([summary]).to_csv(output_dir / 'upcoming_fixture_source_summary.csv', index=False)

markdown = [
    '# Upcoming Fixtures',
    '',
    'Fixture sources: TheSportsDB plus Football-Data fixtures proxy where available.',
    'Primary development target: automatic/free delayed market proxy, not manual Bet365.',
    '',
    f'Fixtures found: {len(fixtures)}',
    f'Source counts: {source_counts}',
    '',
]

if len(fixtures):
    for _, row in fixtures.head(80).iterrows():
        markdown.append(
            f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | {row['league']} | {row['source']}"
        )
else:
    markdown.append('No upcoming fixtures returned.')

if errors:
    markdown.extend(['', '## Errors', ''])
    for error in errors:
        markdown.append(f"- {error['league']}: {error['error']}")

(output_dir / 'upcoming_fixtures.md').write_text('\n'.join(markdown), encoding='utf-8')

for script_path in [
    Path('scripts/fetch_forward_fixture_results.py'),
]:
    if script_path.exists():
        try:
            runpy.run_path(str(script_path), run_name='__main__')
        except Exception as exc:
            print(f'{script_path} skipped: {exc!r}')

print(f'Fetched {len(fixtures)} upcoming fixtures')
