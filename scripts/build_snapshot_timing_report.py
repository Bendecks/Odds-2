from pathlib import Path

import pandas as pd

snapshot_dir = Path('data/market_snapshots')
output_dir = Path('output/latest')

files = sorted(snapshot_dir.glob('*.parquet'))

markdown = [
    '# Snapshot Timing Report',
    '',
]

rows = []

for file in files:
    try:
        df = pd.read_parquet(file)

        timestamp_col = None
        for candidate in ['snapshot_created_at_utc', 'created_at_utc']:
            if candidate in df.columns:
                timestamp_col = candidate
                break

        if timestamp_col is None:
            rows.append({
                'file': file.name,
                'rows': len(df),
                'timestamp_column': 'missing',
                'first_snapshot': 'n/a',
                'last_snapshot': 'n/a',
            })
            continue

        ts = pd.to_datetime(df[timestamp_col], errors='coerce')

        rows.append({
            'file': file.name,
            'rows': len(df),
            'timestamp_column': timestamp_col,
            'first_snapshot': str(ts.min()),
            'last_snapshot': str(ts.max()),
        })

    except Exception as exc:
        rows.append({
            'file': file.name,
            'rows': 0,
            'timestamp_column': 'error',
            'first_snapshot': 'error',
            'last_snapshot': str(exc),
        })

report = pd.DataFrame(rows)

expected_columns = ['file', 'rows', 'timestamp_column', 'first_snapshot', 'last_snapshot']
for col in expected_columns:
    if col not in report.columns:
        report[col] = None

report = report[expected_columns]
report.to_csv(output_dir / 'snapshot_timing_report.csv', index=False)

markdown.append(f'Total snapshot files: {len(report)}')
markdown.append('')

if len(report):
    for _, row in report.tail(10).iterrows():
        markdown.append(
            f"- {row['file']} | rows={row['rows']} | ts_col={row['timestamp_column']} | first={row['first_snapshot']} | last={row['last_snapshot']}"
        )
else:
    markdown.append('No snapshot files available yet.')

(output_dir / 'snapshot_timing_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report.tail())
