from pathlib import Path

import pandas as pd

raw_dir = Path('data/raw')
model_dir = Path('data/model')
multiseason_path = raw_dir / 'multiseason' / 'combined_multiseason.parquet'
multileague_path = raw_dir / 'multileague' / 'combined_multileague_2425.parquet'

model_dir.mkdir(parents=True, exist_ok=True)

if multiseason_path.exists():
    matches = pd.read_parquet(multiseason_path)
    source_label = 'multiseason'
elif multileague_path.exists():
    matches = pd.read_parquet(multileague_path)
    source_label = 'multileague'
else:
    matches = pd.read_parquet(raw_dir / 'premier_league_2425.parquet')
    source_label = 'premier_league_only'

required_cols = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']
missing = [c for c in required_cols if c not in matches.columns]

if missing:
    raise ValueError(f'Missing required columns: {missing}')

matches = matches.dropna(subset=['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG'])

# Weighted recency. Newer seasons matter more.
if 'source_season' in matches.columns:
    season_weights = {
        '2223': 0.60,
        '2324': 0.85,
        '2425': 1.00,
    }

    matches['season_weight'] = matches['source_season'].astype(str).map(season_weights).fillna(1.0)
else:
    matches['season_weight'] = 1.0

league_home_avg = (
    (matches['FTHG'] * matches['season_weight']).sum()
    / matches['season_weight'].sum()
)

league_away_avg = (
    (matches['FTAG'] * matches['season_weight']).sum()
    / matches['season_weight'].sum()
)

league_goal_avg = (league_home_avg + league_away_avg) / 2

teams = sorted(set(matches['HomeTeam']).union(set(matches['AwayTeam'])))
rows = []

for team in teams:
    home_matches = matches[matches['HomeTeam'] == team].copy()
    away_matches = matches[matches['AwayTeam'] == team].copy()

    def weighted_avg(values, weights, fallback):
        if len(values) == 0:
            return fallback
        return (values * weights).sum() / weights.sum()

    home_attack = weighted_avg(
        home_matches['FTHG'],
        home_matches['season_weight'],
        league_home_avg,
    )

    home_defense = weighted_avg(
        home_matches['FTAG'],
        home_matches['season_weight'],
        league_away_avg,
    )

    away_attack = weighted_avg(
        away_matches['FTAG'],
        away_matches['season_weight'],
        league_away_avg,
    )

    away_defense = weighted_avg(
        away_matches['FTHG'],
        away_matches['season_weight'],
        league_home_avg,
    )

    team_recent = pd.concat([
        pd.DataFrame({
            'goals_for': home_matches['FTHG'],
            'goals_against': home_matches['FTAG'],
            'weight': home_matches['season_weight'],
        }),
        pd.DataFrame({
            'goals_for': away_matches['FTAG'],
            'goals_against': away_matches['FTHG'],
            'weight': away_matches['season_weight'],
        }),
    ]).tail(8)

    recent_attack = weighted_avg(
        team_recent['goals_for'],
        team_recent['weight'],
        league_goal_avg,
    ) / league_goal_avg

    recent_defense = weighted_avg(
        team_recent['goals_against'],
        team_recent['weight'],
        league_goal_avg,
    ) / league_goal_avg

    rows.append({
        'team': team,
        'source_dataset': source_label,
        'home_attack_strength': home_attack / league_home_avg,
        'home_defense_strength': home_defense / league_away_avg,
        'away_attack_strength': away_attack / league_away_avg,
        'away_defense_strength': away_defense / league_home_avg,
        'recent_attack_strength': recent_attack,
        'recent_defense_strength': recent_defense,
        'matches_played': int((matches['HomeTeam'].eq(team) | matches['AwayTeam'].eq(team)).sum()),
    })

ratings = pd.DataFrame(rows).set_index('team').fillna(1.0)

ratings['attack_strength'] = (
    ratings['home_attack_strength'] * 0.35
    + ratings['away_attack_strength'] * 0.35
    + ratings['recent_attack_strength'] * 0.30
)

ratings['defense_strength'] = (
    ratings['home_defense_strength'] * 0.35
    + ratings['away_defense_strength'] * 0.35
    + ratings['recent_defense_strength'] * 0.30
)

ratings.to_parquet(model_dir / 'team_strengths.parquet')
ratings.to_csv(model_dir / 'team_strengths.csv')

summary = pd.DataFrame([
    {
        'source_dataset': source_label,
        'teams': len(ratings),
        'matches': len(matches),
        'league_home_avg': round(float(league_home_avg), 4),
        'league_away_avg': round(float(league_away_avg), 4),
    }
])

summary.to_csv(model_dir / 'model_dataset_summary.csv', index=False)

print('Generated weighted multi-season strength model')
print(summary)
