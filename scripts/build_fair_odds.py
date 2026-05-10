from pathlib import Path

import pandas as pd

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
league_goal_avg = (matches['FTHG'].sum() + matches['FTAG'].sum()) / (len(matches) * 2)

home_for = matches.groupby('HomeTeam')['FTHG'].mean()
home_against = matches.groupby('HomeTeam')['FTAG'].mean()
away_for = matches.groupby('AwayTeam')['FTAG'].mean()
away_against = matches.groupby('AwayTeam')['FTHG'].mean()

teams = sorted(set(matches['HomeTeam']).union(set(matches['AwayTeam'])))
rows = []

for team in teams:
    team_home = matches[matches['HomeTeam'] == team].copy()
    team_away = matches[matches['AwayTeam'] == team].copy()

    team_matches = []
    for _, row in team_home.iterrows():
        team_matches.append({
            'goals_for': row['FTHG'],
            'goals_against': row['FTAG'],
        })
    for _, row in team_away.iterrows():
        team_matches.append({
            'goals_for': row['FTAG'],
            'goals_against': row['FTHG'],
        })

    recent = pd.DataFrame(team_matches).tail(5)

    recent_attack = recent['goals_for'].mean() / league_goal_avg if len(recent) else 1.0
    recent_defense = recent['goals_against'].mean() / league_goal_avg if len(recent) else 1.0

    rows.append({
        'team': team,
        'home_attack_strength': home_for.get(team, league_home_avg) / league_home_avg,
        'home_defense_strength': home_against.get(team, league_away_avg) / league_away_avg,
        'away_attack_strength': away_for.get(team, league_away_avg) / league_away_avg,
        'away_defense_strength': away_against.get(team, league_home_avg) / league_home_avg,
        'recent_attack_strength': recent_attack,
        'recent_defense_strength': recent_defense,
        'matches_played': int((matches['HomeTeam'].eq(team) | matches['AwayTeam'].eq(team)).sum()),
    })

ratings = pd.DataFrame(rows).set_index('team').fillna(1.0)

# Legacy-compatible generic columns.
ratings['attack_strength'] = (
    ratings['home_attack_strength'] + ratings['away_attack_strength'] + ratings['recent_attack_strength']
) / 3
ratings['defense_strength'] = (
    ratings['home_defense_strength'] + ratings['away_defense_strength'] + ratings['recent_defense_strength']
) / 3

ratings.to_parquet(model_dir / 'team_strengths.parquet')
ratings.to_csv(model_dir / 'team_strengths.csv')

print('Generated improved team strength model')
print(ratings.head())
