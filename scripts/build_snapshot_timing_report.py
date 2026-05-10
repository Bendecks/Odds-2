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

        if 'created_at_utc' not in df.columns:
            continue

        ts = pd.to_datetime(df['created_at_utc'], errors='coerce')

        rows.append({
            'file': file.name,
            'rows': len(df),
            'first_snapshot': str(ts.min()),
            'last_snapshot': str(ts.max()),
        })

    except Exception as exc:
        rows.append({
            'file': file.name,
            'rows': 0,
            'first_snapshot': 'error',
            'last_snapshot': str(exc),
        })

report = pd.DataFrame(rows)
report.to_csv(output_dir / 'snapshot_timing_report.csv', index=False)

markdown.append(f'Total snapshot files: {len(report)}')
markdown.append('')

if len(report):
    for _, row in report.tail(10).iterrows():
        markdown.append(
            f"- {row['file']} | rows={row['rows']} | first={row['first_snapshot']} | last={row['last_snapshot']}"
        )
else:
    markdown.append('No snapshot files available yet.')

(output_dir / 'snapshot_timing_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report.tail())
