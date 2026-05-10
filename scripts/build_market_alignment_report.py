from pathlib import Path

import pandas as pd

snapshot_path = Path('output/latest/prediction_snapshots_latest.parquet')
output_dir = Path('output/latest')

markdown = [
    '# Market Alignment Report',
    '',
]

summary = pd.DataFrame([
    {
        'rows': 0,
        'average_alignment_gap': None,
        'median_alignment_gap': None,
        'status': 'no_data',
    }
])

if not snapshot_path.exists():
    markdown.append('No prediction snapshots available.')
else:
    df = pd.read_parquet(snapshot_path)

    if len(df) == 0:
        markdown.append('No snapshot rows available.')
    else:
        for col in ['market_odds', 'probability']:
            if col not in df.columns:
                df[col] = None

        df['market_odds'] = pd.to_numeric(df['market_odds'], errors='coerce')
        df['probability'] = pd.to_numeric(df['probability'], errors='coerce')

        df = df.dropna(subset=['market_odds', 'probability'])
        df = df[df['market_odds'] > 0]

        if len(df) == 0:
            markdown.append('No usable market/probability rows available.')
        else:
            df['market_probability'] = 1 / df['market_odds']
            df['alignment_gap'] = (
                df['probability'] - df['market_probability']
            ).abs()

            avg_gap = df['alignment_gap'].mean()
            median_gap = df['alignment_gap'].median()

            if pd.isna(avg_gap):
                status = 'no_data'
            elif avg_gap > 0.18:
                status = 'poor_alignment'
            elif avg_gap > 0.10:
                status = 'moderate_alignment'
            else:
                status = 'good_alignment'

            markdown.extend([
                f'Total usable rows: {len(df)}',
                f'Average alignment gap: {avg_gap:.4f}',
                f'Median alignment gap: {median_gap:.4f}',
                '',
                f'Market alignment status: {status}',
            ])

            summary = pd.DataFrame([
                {
                    'rows': len(df),
                    'average_alignment_gap': float(avg_gap),
                    'median_alignment_gap': float(median_gap),
                    'status': status,
                }
            ])

summary.to_csv(output_dir / 'market_alignment_report.csv', index=False)
(output_dir / 'market_alignment_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
