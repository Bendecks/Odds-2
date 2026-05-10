from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
clv_path = output_dir / 'clv_results.parquet'

markdown = [
    '# CLV Trend Report',
    '',
]

if not clv_path.exists():
    markdown.append('No CLV results available yet.')
else:
    df = pd.read_parquet(clv_path)

    if len(df) == 0:
        markdown.append('CLV dataset is empty.')
    else:
        numeric_cols = ['clv_home', 'clv_draw', 'clv_away']

        for col in numeric_cols:
            if col not in df.columns:
                df[col] = None

        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        summary = {
            'rows': int(len(df)),
            'avg_clv_home': round(float(df['clv_home'].mean()), 4) if df['clv_home'].notna().any() else None,
            'avg_clv_draw': round(float(df['clv_draw'].mean()), 4) if df['clv_draw'].notna().any() else None,
            'avg_clv_away': round(float(df['clv_away'].mean()), 4) if df['clv_away'].notna().any() else None,
        }

        pd.DataFrame([summary]).to_csv(output_dir / 'clv_trend_report.csv', index=False)

        markdown.extend([
            f"Rows: {summary['rows']}",
            f"Average home CLV: {summary['avg_clv_home']}",
            f"Average draw CLV: {summary['avg_clv_draw']}",
            f"Average away CLV: {summary['avg_clv_away']}",
            '',
        ])

        avg_values = [
            v for v in [
                summary['avg_clv_home'],
                summary['avg_clv_draw'],
                summary['avg_clv_away'],
            ] if v is not None
        ]

        if avg_values:
            avg_total = sum(avg_values) / len(avg_values)

            if avg_total > 0:
                interpretation = 'positive_clv_signal'
            elif avg_total > -0.02:
                interpretation = 'neutral_clv_signal'
            else:
                interpretation = 'negative_clv_signal'

            markdown.append(f'CLV interpretation: {interpretation}')

(output_dir / 'clv_trend_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
