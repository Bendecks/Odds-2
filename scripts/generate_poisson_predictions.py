import json
from pathlib import Path

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

# Reduced home advantage to avoid systematic overconfidence.
home_advantage_multiplier = 1 + ((league_home_avg / max(league_away_avg, 0.01)) - 1) * 0.30

latest_round = matches.tail(10).copy()

predictions = []


def calibrate_three_way_probabilities(home_win: float, draw: float, away_win: float) -> tuple[float, float, float]:
    """Apply conservative probability calibration without relying on future results.

    The current system is research-only with negative CLV and evidence of overconfidence.
    This transform deliberately reduces extreme 1X2 views before EV calculation.
    """
    probs = pd.Series([home_win, draw, away_win], dtype='float64')

    # Base shrinkage toward a neutral 1X2 prior.
    neutral = pd.Series([1 / 3, 1 / 3, 1 / 3], dtype='float64')
    probs = (probs * 0.68) + (neutral * 0.32)

    # Extra compression for any selection above 0.50. This directly addresses the
    # probability-band diagnostics where the highest band is performing poorly.
    max_idx = probs.idxmax()
    if probs.iloc[max_idx] > 0.50:
        excess = probs.iloc[max_idx] - 0.50
        reduction = excess * 0.55
        probs.iloc[max_idx] -= reduction
        other_idx = [i for i in probs.index if i != max_idx]
        probs.iloc[other_idx] += reduction / 2

    # Hard guardrail: no current probability should imply more certainty than the
    # diagnostics support. Renormalise after clipping.
    probs = probs.clip(lower=0.18, upper=0.54)
    probs = probs / probs.sum()

    return tuple(probs.tolist())


for _, row in latest_round.iterrows():
    home = mappings.get(row['HomeTeam'], row['HomeTeam'])
    away = mappings.get(row['AwayTeam'], row['AwayTeam'])

    if home not in team_strengths.index or away not in team_strengths.index:
        continue

    home_row = team_strengths.loc[home]
    away_row = team_strengths.loc[away]

    # More conservative weighting.
    home_attack = (
        home_row['home_attack_strength'] * 0.35
        + home_row['recent_attack_strength'] * 0.25
        + 0.40
    )

    away_attack = (
        away_row['away_attack_strength'] * 0.35
        + away_row['recent_attack_strength'] * 0.25
        + 0.40
    )

    home_defense = (
        home_row['home_defense_strength'] * 0.35
        + home_row['recent_defense_strength'] * 0.25
        + 0.40
    )

    away_defense = (
        away_row['away_defense_strength'] * 0.35
        + away_row['recent_defense_strength'] * 0.25
        + 0.40
    )

    expected_home_goals = (
        league_home_avg
        * home_attack
        * away_defense
        * home_advantage_multiplier
    )

    expected_away_goals = (
        league_away_avg
        * away_attack
        * home_defense
    )

    # Stronger shrinkage toward league averages.
    expected_home_goals = (expected_home_goals * 0.60) + (league_home_avg * 0.40)
    expected_away_goals = (expected_away_goals * 0.60) + (league_away_avg * 0.40)

    expected_home_goals = max(min(expected_home_goals, 3.0), 0.55)
    expected_away_goals = max(min(expected_away_goals, 2.6), 0.45)

    home_win = 0
    draw = 0
    away_win = 0

    for h in range(7):
        for a in range(7):
            p = poisson.pmf(h, expected_home_goals) * poisson.pmf(a, expected_away_goals)

            if h > a:
                home_win += p
            elif h == a:
                draw += p
            else:
                away_win += p

    normalization = home_win + draw + away_win

    if normalization > 0:
        home_win /= normalization
        draw /= normalization
        away_win /= normalization

    home_win, draw, away_win = calibrate_three_way_probabilities(home_win, draw, away_win)

    predictions.append({
        'home_team': home,
        'away_team': away,
        'expected_home_goals': round(expected_home_goals, 3),
        'expected_away_goals': round(expected_away_goals, 3),
        'home_advantage_multiplier': round(home_advantage_multiplier, 3),
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
print(f'Generated {len(predictions_df)} conservatively calibrated Poisson predictions')
