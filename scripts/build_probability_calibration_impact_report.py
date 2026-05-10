from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
adjustments_path = output_dir / 'probability_calibration_adjustments.csv'

markdown = [
    '# Probability Calibration Impact Report',
    '',
]

expected_columns = [
    'probability_band',
    'calibration_action',
    'rows',
    'avg_raw_probability',
    'avg_multiplier',
]

if not adjustments_path.exists() or adjustments_path.stat().st_size == 0:
    report = pd.DataFrame(columns=expected_columns)
    markdown.append('No calibration adjustments available.')
else:
    try:
        adjustments = pd.read_csv(adjustments_path)
    except Exception:
        adjustments = pd.DataFrame()

    if len(adjustments) == 0:
        report = pd.DataFrame(columns=expected_columns)
        markdown.append('Calibration adjustments are empty.')
    else:
        adjustments['raw_probability'] = pd.to_numeric(adjustments.get('raw_probability'), errors='coerce')
        adjustments['multiplier'] = pd.to_numeric(adjustments.get('multiplier'), errors='coerce')

        rows = []
        for (band, action), subset in adjustments.groupby(['probability_band', 'calibration_action'], dropna=False):
            rows.append({
                'probability_band': band,
                'calibration_action': action,
                'rows': int(len(subset)),
                'avg_raw_probability': round(float(subset['raw_probability'].dropna().mean()), 4) if len(subset['raw_probability'].dropna()) else None,
                'avg_multiplier': round(float(subset['multiplier'].dropna().mean()), 4) if len(subset['multiplier'].dropna()) else None,
            })

        report = pd.DataFrame(rows)

for col in expected_columns:
    if col not in report.columns:
        report[col] = None
report = report[expected_columns]
report.to_csv(output_dir / 'probability_calibration_impact_report.csv', index=False)

if len(report):
    for _, row in report.iterrows():
        markdown.append(
            f"- {row['probability_band']} | action={row['calibration_action']} | "
            f"rows={row['rows']} | avg_raw_prob={row['avg_raw_probability']} | "
            f"avg_multiplier={row['avg_multiplier']}"
        )
else:
    markdown.append('No impact rows generated.')

(output_dir / 'probability_calibration_impact_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report)
