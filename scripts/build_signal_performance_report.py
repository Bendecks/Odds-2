from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'

markdown = [
    '# Signal Performance Report',
    '',
]

if not settled_path.exists():
    markdown.append('No settled predictions available yet.')
    (output_dir / 'signal_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    raise SystemExit(0)

settled = pd.read_parquet(settled_path)

if len(settled) == 0:
    markdown.append('Settled predictions dataset is empty.')
    (output_dir / 'signal_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    raise SystemExit(0)

for col in ['ev', 'signal_strength']:
    if col not in settled.columns:
        settled[col] = 0.0

settled['ev'] = pd.to_numeric(settled['ev'], errors='coerce').fillna(0)
settled['signal_strength'] = pd.to_numeric(settled['signal_strength'], errors='coerce').fillna(0)

if 'settlement_result' not in settled.columns:
    settled['settlement_result'] = 'unknown'

settled['won'] = settled['settlement_result'].astype(str).str.lower().eq('won')

bands = [
    ('weak', settled['signal_strength'] < 0.18),
    ('medium', (settled['signal_strength'] >= 0.18) & (settled['signal_strength'] < 0.28)),
    ('strong', settled['signal_strength'] >= 0.28),
]

rows = []

for name, mask in bands:
    subset = settled[mask]

    if len(subset) == 0:
        continue

    rows.append({
        'signal_band': name,
        'bets': int(len(subset)),
        'win_rate': round(float(subset['won'].mean()), 4),
        'avg_ev': round(float(subset['ev'].mean()), 4),
        'avg_signal_strength': round(float(subset['signal_strength'].mean()), 4),
    })

report = pd.DataFrame(rows)
report.to_csv(output_dir / 'signal_performance_report.csv', index=False)

markdown.append(f'Total settled predictions: {len(settled)}')
markdown.append('')

for _, row in report.iterrows():
    markdown.append(
        f"- {row['signal_band']} | bets={row['bets']} | "
        f"win_rate={row['win_rate']} | avg_ev={row['avg_ev']} | "
        f"avg_strength={row['avg_signal_strength']}"
    )

markdown.extend([
    '',
    '## Interpretation',
    '',
])

if len(report):
    best = report.sort_values('win_rate', ascending=False).iloc[0]
    markdown.append(
        f"Best current signal group: {best['signal_band']} with win rate {best['win_rate']}"
    )
else:
    markdown.append('Not enough signal data yet.')

(output_dir / 'signal_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report)
