import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import poisson

raw_dir = Path('data/raw')
model_dir = Path('data/model')
output_dir = Path('output/latest')
config_dir = Path('data/config')

output_dir.mkdir(parents=True, exist_ok=True)

matches = pd.read_parquet(raw_dir / 'premier_league_2425.parquet')
team_strengths = pd.read_parquet(model_dir / 'team_strengths.parquet')

mapping_path = config_dir / 'team_name_mapping.json'

if mapping_path.exists():
    mappings = json.loads(mapping_path.read_text(encoding='utf-8'))
else:
    mappings = {}

league_home_avg = matches['FTHG'].mean()
league_away_avg = matches['FTAG'].mean()

latest_round = matches.tail(10).copy()

predictions = []

for _, row in latest_round.iterrows():
    home = mappings.get(row['HomeTeam'], row['HomeTeam'])
    away = mappings.get(row['AwayTeam'], row['AwayTeam'])

    if home not in team_strengths.index or away not in team_strengths.index:
        continue

    home_attack = team_strengths.loc[home, 'attack_strength']
    away_defense = team_strengths.loc[away, 'defense_strength']

    expected_home_goals = league_home_avg * home_attack * away_defense
    expected_away_goals = league_away_avg

    home_win = 0
    draw = 0
    away_win = 0

    for h in range(6):
        for a in range(6):
            p = poisson.pmf(h, expected_home_goals) * poisson.pmf(a, expected_away_goals)
            if h > a:
                home_win += p
            elif h == a:
                draw += p
            else:
                away_win += p

    predictions.append({
        'home_team': home,
        'away_team': away,
        'expected_home_goals': round(expected_home_goals, 3),
        'expected_away_goals': round(expected_away_goals, 3),
        'home_win_probability': round(home_win, 4),
        'draw_probability': round(draw, 4),
        'away_win_probability': round(away_win, 4),
        'fair_home_odds': round(1 / home_win, 2) if home_win > 0 else None,
        'fair_draw_odds': round(1 / draw, 2) if draw > 0 else None,
        'fair_away_odds': round(1 / away_win, 2) if away_win > 0 else None,
    })

predictions_df = pd.DataFrame(predictions)

predictions_df.to_parquet(output_dir / 'poisson_predictions.parquet', index=False)
predictions_df.to_csv(output_dir / 'poisson_predictions.csv', index=False)

print(predictions_df.head())
print(f'Generated {len(predictions_df)} Poisson predictions')
