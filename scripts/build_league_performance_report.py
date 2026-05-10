from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'

markdown = ['# League Performance Report', '']

if not settled_path.exists():
    markdown.append('No settled predictions available.')
    (output_dir / 'league_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'league_performance_report.csv', index=False)
    raise SystemExit(0)

settled = pd.read_parquet(settled_path)

if len(settled) == 0:
    markdown.append('Settled predictions dataset is empty.')
    (output_dir / 'league_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'league_performance_report.csv', index=False)
    raise SystemExit(0)

if 'league' not in settled.columns:
    settled['league'] = 'unknown'

if 'roi_units' not in settled.columns:
    settled['roi_units'] = 0.0

if 'won' not in settled.columns:
    settled['won'] = False

settled['roi_units'] = pd.to_numeric(settled['roi_units'], errors='coerce').fillna(0)
settled['won'] = settled['won'].fillna(False).astype(bool)

rows = []

for league, subset in settled.groupby('league'):
    rows.append({
        'league': league,
        'bets': int(len(subset)),
        'win_rate': round(float(subset['won'].mean()), 4),
        'roi_units': round(float(subset['roi_units'].sum()), 4),
        'avg_roi_per_bet': round(float(subset['roi_units'].mean()), 4),
    })

report = pd.DataFrame(rows).sort_values('avg_roi_per_bet', ascending=False)
report.to_csv(output_dir / 'league_performance_report.csv', index=False)

markdown.append(f'Total leagues: {len(report)}')
markdown.append('')

for _, row in report.iterrows():
    markdown.append(
        f"- {row['league']} | bets={row['bets']} | "
        f"win_rate={row['win_rate']} | roi={row['roi_units']} | "
        f"avg_roi={row['avg_roi_per_bet']}"
    )

(output_dir / 'league_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report.head())
