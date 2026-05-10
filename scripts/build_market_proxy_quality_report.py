from pathlib import Path

import pandas as pd

snapshot_path = Path('output/latest/market_snapshot_latest.parquet')
output_dir = Path('output/latest')

markdown = [
    '# Market Proxy Quality Report',
    '',
]

if not snapshot_path.exists():
    markdown.append('No market snapshot available.')
else:
    df = pd.read_parquet(snapshot_path)

    if len(df):
        summary = {
            'rows': int(len(df)),
            'avg_overround': round(float(df['market_overround'].mean()), 4),
            'median_overround': round(float(df['market_overround'].median()), 4),
            'min_overround': round(float(df['market_overround'].min()), 4),
            'max_overround': round(float(df['market_overround'].max()), 4),
        }

        markdown.extend([
            f"Rows: {summary['rows']}",
            f"Average overround: {summary['avg_overround']}",
            f"Median overround: {summary['median_overround']}",
            f"Min overround: {summary['min_overround']}",
            f"Max overround: {summary['max_overround']}",
            '',
        ])

        if summary['avg_overround'] < 1.02:
            quality = 'sharp_market_proxy'
        elif summary['avg_overround'] < 1.08:
            quality = 'reasonable_market_proxy'
        else:
            quality = 'weak_market_proxy'

        markdown.append(f'Market proxy quality: {quality}')

        pd.DataFrame([summary]).to_csv(
            output_dir / 'market_proxy_quality_report.csv',
            index=False,
        )

(output_dir / 'market_proxy_quality_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
