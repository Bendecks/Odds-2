from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
clv_path = output_dir / 'clv_results.parquet'

markdown = [
    '# CLV Trend Report',
    '',
]

summary = {
    'rows': 0,
    'avg_clv_delta': None,
    'beat_closing_line_rate': None,
    'positive_clv_rows': 0,
    'negative_clv_rows': 0,
    'interpretation': 'no_data',
}

if not clv_path.exists():
    markdown.append('No CLV results available yet.')
else:
    df = pd.read_parquet(clv_path)

    if len(df) == 0:
        markdown.append('CLV dataset is empty.')
    else:
        # Current CLV schema uses clv_delta and beat_closing_line.
        # Keep legacy support for clv_home/clv_draw/clv_away if those columns appear later.
        if 'clv_delta' in df.columns:
            df['clv_delta'] = pd.to_numeric(df['clv_delta'], errors='coerce')
            avg_clv_delta = df['clv_delta'].dropna().mean()
            positive_rows = int((df['clv_delta'] > 0).sum())
            negative_rows = int((df['clv_delta'] < 0).sum())
        else:
            legacy_cols = [c for c in ['clv_home', 'clv_draw', 'clv_away'] if c in df.columns]
            if legacy_cols:
                for col in legacy_cols:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
                legacy_values = df[legacy_cols].stack().dropna()
                avg_clv_delta = legacy_values.mean() if len(legacy_values) else None
                positive_rows = int((legacy_values > 0).sum()) if len(legacy_values) else 0
                negative_rows = int((legacy_values < 0).sum()) if len(legacy_values) else 0
            else:
                avg_clv_delta = None
                positive_rows = 0
                negative_rows = 0

        if 'beat_closing_line' in df.columns:
            beat_rate = df['beat_closing_line'].fillna(False).astype(bool).mean()
        elif avg_clv_delta is not None:
            beat_rate = positive_rows / len(df) if len(df) else None
        else:
            beat_rate = None

        if avg_clv_delta is None or pd.isna(avg_clv_delta):
            interpretation = 'no_usable_clv_data'
        elif avg_clv_delta > 0:
            interpretation = 'positive_clv_signal'
        elif avg_clv_delta > -0.02:
            interpretation = 'neutral_clv_signal'
        else:
            interpretation = 'negative_clv_signal'

        summary = {
            'rows': int(len(df)),
            'avg_clv_delta': round(float(avg_clv_delta), 4) if avg_clv_delta is not None and pd.notna(avg_clv_delta) else None,
            'beat_closing_line_rate': round(float(beat_rate), 4) if beat_rate is not None and pd.notna(beat_rate) else None,
            'positive_clv_rows': positive_rows,
            'negative_clv_rows': negative_rows,
            'interpretation': interpretation,
        }

        markdown.extend([
            f"Rows: {summary['rows']}",
            f"Average CLV delta: {summary['avg_clv_delta']}",
            f"Beat closing line rate: {summary['beat_closing_line_rate']}",
            f"Positive CLV rows: {summary['positive_clv_rows']}",
            f"Negative CLV rows: {summary['negative_clv_rows']}",
            '',
            f"CLV interpretation: {summary['interpretation']}",
        ])

pd.DataFrame([summary]).to_csv(output_dir / 'clv_trend_report.csv', index=False)
(output_dir / 'clv_trend_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
