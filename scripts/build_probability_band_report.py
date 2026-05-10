from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'

markdown = ['# Probability Band Report', '']

if not settled_path.exists():
    markdown.append('No settled predictions available.')
    (output_dir / 'probability_band_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'probability_band_report.csv', index=False)
    raise SystemExit(0)

settled = pd.read_parquet(settled_path)

if len(settled) == 0:
    markdown.append('Settled predictions dataset is empty.')
    (output_dir / 'probability_band_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'probability_band_report.csv', index=False)
    raise SystemExit(0)

if 'probability' not in settled.columns:
    settled['probability'] = 0.0

if 'won' not in settled.columns:
    settled['won'] = False

if 'roi_units' not in settled.columns:
    settled['roi_units'] = 0.0

settled['probability'] = pd.to_numeric(settled['probability'], errors='coerce').fillna(0)
settled['roi_units'] = pd.to_numeric(settled['roi_units'], errors='coerce').fillna(0)
settled['won'] = settled['won'].fillna(False).astype(bool)

bands = [
    ('0.30-0.40', 0.30, 0.40),
    ('0.40-0.50', 0.40, 0.50),
    ('0.50-0.60', 0.50, 0.60),
    ('0.60-0.70', 0.60, 0.70),
    ('0.70+', 0.70, 1.01),
]

rows = []

for label, low, high in bands:
    subset = settled[
        (settled['probability'] >= low)
        & (settled['probability'] < high)
    ]

    if len(subset) == 0:
        continue

    rows.append({
        'band': label,
        'bets': int(len(subset)),
        'actual_win_rate': round(float(subset['won'].mean()), 4),
        'avg_probability': round(float(subset['probability'].mean()), 4),
        'avg_roi': round(float(subset['roi_units'].mean()), 4),
    })

report = pd.DataFrame(rows)
report.to_csv(output_dir / 'probability_band_report.csv', index=False)

markdown.append(f'Total probability bands with data: {len(report)}')
markdown.append('')

for _, row in report.iterrows():
    markdown.append(
        f"- {row['band']} | bets={row['bets']} | "
        f"actual={row['actual_win_rate']} | "
        f"predicted={row['avg_probability']} | "
        f"avg_roi={row['avg_roi']}"
    )

(output_dir / 'probability_band_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report)
