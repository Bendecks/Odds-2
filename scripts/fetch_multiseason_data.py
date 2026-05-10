from pathlib import Path

import pandas as pd

LEAGUES = {
    'E0': 'premier_league',
    'SP1': 'la_liga',
    'D1': 'bundesliga',
    'I1': 'serie_a',
    'F1': 'ligue_1',
}

SEASONS = ['2223', '2324', '2425']
BASE_URL = 'https://www.football-data.co.uk/mmz4281/{}/{}.csv'

output_dir = Path('data/raw/multiseason')
output_dir.mkdir(parents=True, exist_ok=True)

frames = []

for season in SEASONS:
    for code, league_name in LEAGUES.items():
        url = BASE_URL.format(season, code)

        try:
            df = pd.read_csv(url)
            df['source_league'] = league_name
            df['source_code'] = code
            df['source_season'] = season

            frames.append(df)

            print(f'Loaded {league_name} {season}: {len(df)} rows')

        except Exception as exc:
            print(f'Failed {league_name} {season}: {exc}')

if frames:
    combined = pd.concat(frames, ignore_index=True)

    combined.to_parquet(output_dir / 'combined_multiseason.parquet', index=False)
    combined.to_csv(output_dir / 'combined_multiseason.csv', index=False)

    summary = (
        combined.groupby(['source_season', 'source_league'])
        .size()
        .reset_index(name='rows')
    )

    summary.to_csv(output_dir / 'multiseason_summary.csv', index=False)

    print(f'Total rows: {len(combined)}')
else:
    print('No multi-season data loaded')
