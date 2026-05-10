from pathlib import Path

import pandas as pd

multiseason_path = Path('data/raw/multiseason/combined_multiseason.parquet')
output_dir = Path('output/latest')

markdown = [
    '# Historical Coverage Report',
    '',
]

if not multiseason_path.exists():
    markdown.append('No multi-season dataset available.')
else:
    df = pd.read_parquet(multiseason_path)

    summary = (
        df.groupby(['source_season', 'source_league'])
        .size()
        .reset_index(name='matches')
        .sort_values(['source_season', 'source_league'])
    )

    summary.to_csv(output_dir / 'historical_coverage_report.csv', index=False)

    markdown.extend([
        f'Total matches: {len(df)}',
        f'Total leagues: {df["source_league"].nunique()}',
        f'Total seasons: {df["source_season"].nunique()}',
        '',
        '## Coverage',
        '',
    ])

    for _, row in summary.iterrows():
        markdown.append(
            f"- {row['source_season']} | {row['source_league']} | matches={row['matches']}"
        )

(output_dir / 'historical_coverage_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
