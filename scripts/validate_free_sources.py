import json
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

status = {
    'generated_at_utc': datetime.now(timezone.utc).isoformat(),
    'overall_ok': all(c['ok'] for c in checks),
    'checks': checks,
}

output_dir = Path('output/latest')
output_dir.mkdir(parents=True, exist_ok=True)

json_path = output_dir / 'free_data_status.json'
md_path = output_dir / 'free_data_status.md'

json_path.write_text(json.dumps(status, indent=2), encoding='utf-8')

lines = [
    '# Free Data Source Status',
    '',
    f"Generated UTC: `{status['generated_at_utc']}`",
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

md_path.write_text('\n'.join(lines) + '\n', encoding='utf-8')

print(json.dumps(status, indent=2))

if not status['overall_ok']:
    raise SystemExit(1)
