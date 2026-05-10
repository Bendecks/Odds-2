import json
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

checks = []

def add_check(name, path, required_columns=None):
    path = Path(path)
    result = {
        'name': name,
        'path': str(path),
        'exists': path.exists(),
        'ok': False,
        'rows': None,
        'columns': [],
        'missing_columns': [],
        'error': None,
    }

    if not path.exists():
        result['error'] = 'File not found'
        checks.append(result)
        return

    try:
        df = pd.read_parquet(path)
        result['rows'] = int(len(df))
        result['columns'] = list(df.columns)
        if required_columns:
            result['missing_columns'] = [c for c in required_columns if c not in df.columns]
        result['ok'] = result['rows'] > 0 and not result['missing_columns']
    except Exception as exc:
        result['error'] = repr(exc)

    checks.append(result)

add_check(
    'football-data.co.uk Premier League 24/25',
    'data/raw/premier_league_2425.parquet',
    required_columns=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'],
)

add_check(
    'ClubElo latest snapshot',
    'data/raw/clubelo_latest.parquet',
    required_columns=['Club', 'Elo'],
)

add_check(
    'Basic team strength model',
    'data/model/team_strengths.parquet',
    required_columns=['attack_strength', 'defense_strength'],
)

add_check(
    'Poisson predictions',
    'output/latest/poisson_predictions.parquet',
    required_columns=['home_team', 'away_team', 'fair_home_odds'],
)

add_check(
    'Expected value calculations',
    'output/latest/ev_results.parquet',
    required_columns=['home_ev', 'draw_ev', 'away_ev'],
)

run_number = os.getenv('GITHUB_RUN_NUMBER', 'local')
run_attempt = os.getenv('GITHUB_RUN_ATTEMPT', 'local')
run_id = os.getenv('GITHUB_RUN_ID', 'local')
sha = os.getenv('GITHUB_SHA', 'local')
ref = os.getenv('GITHUB_REF_NAME', 'local')

status = {
    'generated_at_utc': datetime.now(timezone.utc).isoformat(),
    'github_run_number': run_number,
    'github_run_attempt': run_attempt,
    'github_run_id': run_id,
    'github_sha': sha,
    'github_ref': ref,
    'overall_ok': all(c['ok'] for c in checks),
    'checks': checks,
}

output_dir = Path('output/latest')
history_dir = Path('output/history')
output_dir.mkdir(parents=True, exist_ok=True)
history_dir.mkdir(parents=True, exist_ok=True)

json_text = json.dumps(status, indent=2)
json_path = output_dir / 'free_data_status.json'
md_path = output_dir / 'free_data_status.md'
history_json_path = history_dir / f'free_data_status_run_{run_number}_attempt_{run_attempt}.json'

json_path.write_text(json_text, encoding='utf-8')
history_json_path.write_text(json_text, encoding='utf-8')

lines = [
    '# Free Data Source Status',
    '',
    f"Generated UTC: `{status['generated_at_utc']}`",
    f"GitHub run: `{run_number}` attempt `{run_attempt}`",
    f"GitHub SHA: `{sha}`",
    '',
    f"Overall status: `{'OK' if status['overall_ok'] else 'FAILED'}`",
    '',
    '| Source | OK | Rows | Missing columns | Error |',
    '|---|---:|---:|---|---|',
]

for check in checks:
    lines.append(
        f"| {check['name']} | {check['ok']} | {check['rows']} | "
        f"{', '.join(check['missing_columns']) if check['missing_columns'] else ''} | "
        f"{check['error'] or ''} |"
    )

md_text = '\n'.join(lines) + '\n'
md_path.write_text(md_text, encoding='utf-8')
(history_dir / f'free_data_status_run_{run_number}_attempt_{run_attempt}.md').write_text(md_text, encoding='utf-8')

print(json_text)

if not status['overall_ok']:
    raise SystemExit(1)
