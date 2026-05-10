from pathlib import Path

import pandas as pd

LEAGUES = {
    'E0': 'premier_league',
    'SP1': 'la_liga',
    'D1': 'bundesliga',
    'I1': 'serie_a',
    'F1': 'ligue_1',
}

BASE_URL = 'https://www.football-data.co.uk/mmz4281/2425/{}.csv'

output_dir = Path('data/raw/multileague')
output_dir.mkdir(parents=True, exist_ok=True)

combined = []

for code, name in LEAGUES.items():
    url = BASE_URL.format(code)

    try:
        df = pd.read_csv(url)
        df['source_league'] = name
        df['source_code'] = code

        df.to_parquet(output_dir / f'{name}_2425.parquet', index=False)
        combined.append(df)

        print(f'Loaded {name}: {len(df)} rows')

    except Exception as exc:
        print(f'Failed loading {name}: {exc}')

if combined:
    merged = pd.concat(combined, ignore_index=True)
    merged.to_parquet(output_dir / 'combined_multileague_2425.parquet', index=False)
    merged.to_csv(output_dir / 'combined_multileague_2425.csv', index=False)

    print(f'Combined rows: {len(merged)}')
else:
    print('No league data loaded')
