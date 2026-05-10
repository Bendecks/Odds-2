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
    pd.DataFrame().to_csv(output_dir / 'signal_performance_report.csv', index=False)
    raise SystemExit(0)

settled = pd.read_parquet(settled_path)

if len(settled) == 0:
    markdown.append('Settled predictions dataset is empty.')
    (output_dir / 'signal_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'signal_performance_report.csv', index=False)
    raise SystemExit(0)

for col in ['opening_ev', 'ev', 'signal_strength', 'roi_units']:
    if col not in settled.columns:
        settled[col] = 0.0

if 'won' not in settled.columns:
    if 'settlement_result' in settled.columns:
        settled['won'] = settled['settlement_result'].astype(str).str.lower().eq('won')
    else:
        settled['won'] = False

settled['won'] = settled['won'].fillna(False).astype(bool)
settled['roi_units'] = pd.to_numeric(settled['roi_units'], errors='coerce').fillna(0)
settled['signal_strength'] = pd.to_numeric(settled['signal_strength'], errors='coerce').fillna(0)

# Legacy compatibility: older predictions store opening_ev, newer snapshots may store ev.
settled['effective_ev'] = pd.to_numeric(settled['ev'], errors='coerce')
settled['opening_ev'] = pd.to_numeric(settled['opening_ev'], errors='coerce')
settled['effective_ev'] = settled['effective_ev'].fillna(settled['opening_ev']).fillna(0)

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
        'avg_ev': round(float(subset['effective_ev'].mean()), 4),
        'avg_signal_strength': round(float(subset['signal_strength'].mean()), 4),
        'roi_units': round(float(subset['roi_units'].sum()), 4),
        'avg_roi_units': round(float(subset['roi_units'].mean()), 4),
    })

report = pd.DataFrame(rows)

expected_cols = [
    'signal_band',
    'bets',
    'win_rate',
    'avg_ev',
    'avg_signal_strength',
    'roi_units',
    'avg_roi_units',
]

for col in expected_cols:
    if col not in report.columns:
        report[col] = None

report = report[expected_cols]
report.to_csv(output_dir / 'signal_performance_report.csv', index=False)

markdown.append(f'Total settled predictions: {len(settled)}')
markdown.append('')

for _, row in report.dropna(subset=['signal_band']).iterrows():
    markdown.append(
        f"- {row['signal_band']} | bets={row['bets']} | "
        f"win_rate={row['win_rate']} | roi={row['roi_units']} | "
        f"avg_roi={row['avg_roi_units']} | avg_ev={row['avg_ev']} | "
        f"avg_strength={row['avg_signal_strength']}"
    )

markdown.extend([
    '',
    '## Interpretation',
    '',
])

valid_report = report.dropna(subset=['signal_band'])

if len(valid_report):
    best = valid_report.sort_values('avg_roi_units', ascending=False).iloc[0]
    markdown.append(
        f"Best current signal group by ROI: {best['signal_band']} with avg ROI {best['avg_roi_units']}"
    )
else:
    markdown.append('Not enough signal data yet.')

(output_dir / 'signal_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report)
