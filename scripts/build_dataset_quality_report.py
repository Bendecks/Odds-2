from pathlib import Path

import pandas as pd

raw_dir = Path('data/raw/multileague')
output_dir = Path('output/latest')

combined_path = raw_dir / 'combined_multileague_2425.parquet'

markdown = [
    '# Dataset Quality Report',
    '',
]

if not combined_path.exists():
    markdown.append('No multi-league dataset available yet.')
else:
    df = pd.read_parquet(combined_path)

    markdown.extend([
        f'Total rows: {len(df)}',
        f'Total leagues: {df["source_league"].nunique()}',
        '',
        '## League distribution',
        '',
    ])

    distribution = (
        df.groupby('source_league')
        .size()
        .reset_index(name='rows')
        .sort_values('rows', ascending=False)
    )

    distribution.to_csv(output_dir / 'dataset_league_distribution.csv', index=False)

    for _, row in distribution.iterrows():
        markdown.append(f"- {row['source_league']}: {row['rows']} rows")

    markdown.extend([
        '',
        '## Missing values',
        '',
    ])

    important = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'PSCH', 'PSCA']

    for col in important:
        missing = int(df[col].isna().sum()) if col in df.columns else 'missing_column'
        markdown.append(f'- {col}: {missing}')

(output_dir / 'dataset_quality_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
