from pathlib import Path

import pandas as pd

snapshot_path = Path('output/latest/prediction_snapshots_latest.parquet')
output_dir = Path('output/latest')

markdown = [
    '# Market Alignment Report',
    '',
]

if not snapshot_path.exists():
    markdown.append('No prediction snapshots available.')
else:
    df = pd.read_parquet(snapshot_path)

    if len(df):
        df['market_probability'] = 1 / df['market_odds'].replace(0, pd.NA)
        df['alignment_gap'] = (
            df['probability'] - df['market_probability']
        ).abs()

        avg_gap = df['alignment_gap'].mean()
        median_gap = df['alignment_gap'].median()

        markdown.extend([
            f'Total rows: {len(df)}',
            f'Average alignment gap: {avg_gap:.4f}',
            f'Median alignment gap: {median_gap:.4f}',
            '',
        ])

        if avg_gap > 0.18:
            status = 'poor_alignment'
        elif avg_gap > 0.10:
            status = 'moderate_alignment'
        else:
            status = 'good_alignment'

        markdown.append(f'Market alignment status: {status}')

        summary = pd.DataFrame([
            {
                'rows': len(df),
                'average_alignment_gap': float(avg_gap),
                'median_alignment_gap': float(median_gap),
                'status': status,
            }
        ])

        summary.to_csv(output_dir / 'market_alignment_report.csv', index=False)
else:
    markdown.append('No snapshot data.')

(output_dir / 'market_alignment_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
