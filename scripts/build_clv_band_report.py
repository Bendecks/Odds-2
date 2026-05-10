from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
clv_path = output_dir / 'clv_results.parquet'

markdown = [
    '# CLV Probability Band Report',
    '',
]

expected_columns = [
    'probability_band',
    'rows',
    'avg_clv_delta',
    'beat_closing_line_rate',
    'avg_ev',
]

if not clv_path.exists():
    report = pd.DataFrame(columns=expected_columns)
    markdown.append('No CLV dataset available.')
else:
    df = pd.read_parquet(clv_path)

    if len(df) == 0:
        report = pd.DataFrame(columns=expected_columns)
        markdown.append('CLV dataset is empty.')
    else:
        df['opening_probability'] = pd.to_numeric(df['opening_probability'], errors='coerce')
        df['clv_delta'] = pd.to_numeric(df['clv_delta'], errors='coerce')
        df['opening_ev'] = pd.to_numeric(df['opening_ev'], errors='coerce')

        bins = [0.0, 0.35, 0.45, 0.50, 0.55, 1.0]
        rows = []

        for start, end in zip(bins[:-1], bins[1:]):
            subset = df[
                (df['opening_probability'] >= start)
                & (df['opening_probability'] < end)
            ]

            if len(subset) == 0:
                continue

            avg_clv = subset['clv_delta'].dropna().mean()
            beat_rate = subset['beat_closing_line'].fillna(False).mean()
            avg_ev = subset['opening_ev'].dropna().mean()

            rows.append({
                'probability_band': f'{start:.2f}-{end:.2f}',
                'rows': int(len(subset)),
                'avg_clv_delta': round(float(avg_clv), 4) if pd.notna(avg_clv) else None,
                'beat_closing_line_rate': round(float(beat_rate), 4),
                'avg_ev': round(float(avg_ev), 4) if pd.notna(avg_ev) else None,
            })

            markdown.append(
                f'- {start:.2f}-{end:.2f} | rows={len(subset)} | '
                f'avg_clv={round(float(avg_clv),4) if pd.notna(avg_clv) else "n/a"} | '
                f'beat_rate={round(float(beat_rate),4)} | '
                f'avg_ev={round(float(avg_ev),4) if pd.notna(avg_ev) else "n/a"}'
            )

        report = pd.DataFrame(rows)

for col in expected_columns:
    if col not in report.columns:
        report[col] = None

report = report[expected_columns]
report.to_csv(output_dir / 'clv_band_report.csv', index=False)
(output_dir / 'clv_band_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report)
