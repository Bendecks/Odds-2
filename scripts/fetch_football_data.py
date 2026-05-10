import pandas as pd
from pathlib import Path

BASE_URL = 'https://www.football-data.co.uk/mmz4281/2425/E0.csv'

output_dir = Path('data/raw')
output_dir.mkdir(parents=True, exist_ok=True)

print('Downloading football-data.co.uk Premier League data...')

df = pd.read_csv(BASE_URL)

output_path = output_dir / 'premier_league_2425.parquet'
df.to_parquet(output_path, index=False)

print(f'Saved {len(df)} rows to {output_path}')

closing_cols = [c for c in df.columns if 'PS' in c]
print('Detected Pinnacle-related columns:', closing_cols)
