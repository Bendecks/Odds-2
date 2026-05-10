from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'

if settled_path.exists():
    settled = pd.read_parquet(settled_path)
else:
    settled = pd.DataFrame()

markdown = [
    '# Probability Calibration Report',
    '',
]

rows = []

if len(settled) == 0:
    markdown.append('No settled predictions available yet.')
else:
    # Backward compatibility for legacy records.
    if 'opening_probability' not in settled.columns:
        settled['opening_probability'] = None
    if 'won' not in settled.columns:
        settled['won'] = False

    settled['opening_probability'] = pd.to_numeric(settled['opening_probability'], errors='coerce')
    settled['won'] = settled['won'].fillna(False).astype(bool)
    settled = settled.dropna(subset=['opening_probability'])

    if len(settled) == 0:
        markdown.append('No settled predictions with probability values available yet.')
    else:
        bins = [0.0, 0.35, 0.45, 0.55, 0.65, 1.0]

        for start, end in zip(bins[:-1], bins[1:]):
            bucket = settled[
                (settled['opening_probability'] >= start)
                & (settled['opening_probability'] < end)
            ]

            if len(bucket) == 0:
                continue

            actual_win_rate = bucket['won'].mean()
            expected_probability = bucket['opening_probability'].mean()
            calibration_error = abs(expected_probability - actual_win_rate)

            rows.append({
                'range': f'{start:.2f}-{end:.2f}',
                'bets': int(len(bucket)),
                'expected_probability': round(float(expected_probability), 4),
                'actual_win_rate': round(float(actual_win_rate), 4),
                'calibration_error': round(float(calibration_error), 4),
            })

            markdown.append(
                f"- {start:.2f}-{end:.2f}: expected={expected_probability:.4f}, actual={actual_win_rate:.4f}, error={calibration_error:.4f}, bets={len(bucket)}"
            )

report_df = pd.DataFrame(rows)

expected_columns = [
    'range',
    'bets',
    'expected_probability',
    'actual_win_rate',
    'calibration_error',
]

for col in expected_columns:
    if col not in report_df.columns:
        report_df[col] = None

report_df = report_df[expected_columns]
report_df.to_csv(output_dir / 'probability_calibration_report.csv', index=False)

if len(report_df.dropna(subset=['calibration_error'])):
    mean_error = report_df['calibration_error'].dropna().mean()
else:
    mean_error = None

markdown.extend([
    '',
    f"Average calibration error: {round(float(mean_error),4) if mean_error is not None else 'n/a'}",
])

(output_dir / 'probability_calibration_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report_df)
