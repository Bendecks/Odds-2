import pandas as pd
import numpy as np
from pathlib import Path

raw_dir = Path('data/raw')
model_dir = Path('data/model')
model_dir.mkdir(parents=True, exist_ok=True)

matches = pd.read_parquet(raw_dir / 'premier_league_2425.parquet')

required_cols = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
missing = [c for c in required_cols if c not in matches.columns]

if missing:
    raise ValueError(f'Missing required columns: {missing}')

league_home_avg = matches['FTHG'].mean()
league_away_avg = matches['FTAG'].mean()

home_strength = matches.groupby('HomeTeam')['FTHG'].mean() / league_home_avg
away_defense = matches.groupby('AwayTeam')['FTAG'].mean() / league_away_avg

ratings = pd.DataFrame({
    'attack_strength': home_strength,
    'defense_strength': away_defense
}).fillna(1.0)

ratings.to_parquet(model_dir / 'team_strengths.parquet')

print('Generated basic fair-odds scaffold')
print(ratings.head())
