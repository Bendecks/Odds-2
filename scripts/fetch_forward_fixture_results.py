import json
import runpy
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
raw_dir = Path('data/raw/forward_results')
raw_dir.mkdir(parents=True, exist_ok=True)

fixtures_path = output_dir / 'upcoming_fixtures.csv'
results_path = output_dir / 'forward_fixture_results.csv'

expected_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team',
    'home_score', 'away_score', 'result_status', 'result_source', 'fetched_at_utc'
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


fixtures = safe_read_csv(fixtures_path)
rows = []
errors = []
fetched_at = datetime.now(timezone.utc).isoformat()

if len(fixtures):
    for _, fixture in fixtures.iterrows():
        fixture_id = fixture.get('fixture_id')
        if pd.isna(fixture_id):
            continue

        url = f'https://www.thesportsdb.com/api/v1/json/3/lookupevent.php?id={fixture_id}'
        event = None
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                payload = json.loads(response.read().decode('utf-8'))
            events = payload.get('events') or []
            event = events[0] if events else None
        except Exception as exc:
            errors.append({'fixture_id': fixture_id, 'error': repr(exc)})

        home_score = None
        away_score = None
        status = 'not_started_or_result_unavailable'

        if event:
            raw_home_score = event.get('intHomeScore')
            raw_away_score = event.get('intAwayScore')
            if raw_home_score not in [None, ''] and raw_away_score not in [None, '']:
                try:
                    home_score = int(raw_home_score)
                    away_score = int(raw_away_score)
                    status = 'final_or_result_available'
                except Exception:
                    status = 'score_parse_failed'

        rows.append({
            'fixture_id': fixture_id,
            'match_date': fixture.get('match_date'),
            'match_time': fixture.get('match_time'),
            'home_team': fixture.get('home_team'),
            'away_team': fixture.get('away_team'),
            'home_score': home_score,
            'away_score': away_score,
            'result_status': status,
            'result_source': 'thesportsdb_lookupevent',
            'fetched_at_utc': fetched_at,
        })

results = pd.DataFrame(rows)
for col in expected_columns:
    if col not in results.columns:
        results[col] = None
results = results[expected_columns]
results.to_csv(results_path, index=False)
results.to_csv(raw_dir / 'forward_fixture_results_latest.csv', index=False)

settled_rows = int((results['result_status'] == 'final_or_result_available').sum()) if len(results) else 0
summary = {
    'fixture_rows_checked': int(len(fixtures)),
    'result_rows': int(len(results)),
    'settled_result_rows': settled_rows,
    'errors': int(len(errors)),
}
pd.DataFrame([summary]).to_csv(output_dir / 'forward_fixture_result_status.csv', index=False)

markdown = [
    '# Forward Fixture Results',
    '',
    'Results for probability-only forward fixture predictions. Used for future calibration checks, not betting settlement.',
    '',
    f"Fixture rows checked: {summary['fixture_rows_checked']}",
    f"Result rows: {summary['result_rows']}",
    f"Settled result rows: {summary['settled_result_rows']}",
    f"Errors: {summary['errors']}",
    '',
]

if len(results):
    for _, row in results.iterrows():
        score = 'not available'
        if row.get('result_status') == 'final_or_result_available':
            score = f"{row.get('home_score')}-{row.get('away_score')}"
        markdown.append(
            f"- {row.get('match_date')} {row.get('match_time')} | {row.get('home_team')} vs {row.get('away_team')} | "
            f"score={score} | status={row.get('result_status')}"
        )
else:
    markdown.append('No fixture result rows available yet.')

if errors:
    markdown.extend(['', '## Errors', ''])
    for error in errors[:20]:
        markdown.append(f"- {error['fixture_id']}: {error['error']}")

(output_dir / 'forward_fixture_results.md').write_text('\n'.join(markdown), encoding='utf-8')

calibration_script = Path('scripts/build_forward_probability_calibration_report.py')
if calibration_script.exists():
    try:
        runpy.run_path(str(calibration_script), run_name='__main__')
    except Exception as exc:
        print(f'Forward probability calibration skipped: {exc!r}')

print(summary)
