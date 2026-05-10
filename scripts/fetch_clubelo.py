import pandas as pd
from pathlib import Path

url = 'http://api.clubelo.com/2026-05-01'

output_dir = Path('data/raw')
output_dir.mkdir(parents=True, exist_ok=True)

print('Downloading ClubElo ratings...')

df = pd.read_csv(url)

output_path = output_dir / 'clubelo_latest.parquet'
df.to_parquet(output_path, index=False)

print(f'Saved {len(df)} ClubElo rows to {output_path}')
