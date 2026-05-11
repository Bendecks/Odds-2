import hashlib
import runpy
from pathlib import Path

import pandas as pd
from scipy.stats import poisson

output_dir = Path('output/latest')
model_dir = Path('data/model')
raw_dir = Path('data/raw')

fixtures_path = output_dir / 'upcoming_fixtures.csv'
match_report_path = output_dir / 'fixture_model_match_report.csv'
team_strength_path = model_dir / 'team_strengths.parquet'
historical_path = raw_dir / 'premier_league_2425.parquet'

expected_columns = [
    'prediction_id', 'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team',
    'league', 'sample_phase', 'expected_home_goals', 'expected_away_goals',
    'home_win_probability', 'draw_probability', 'away_win_probability',
    'fair_home_odds', 'fair_draw_odds', 'fair_away_odds', 'model_source',
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def safe_read_parquet(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_parquet(path)
    except Exception:
        return pd.DataFrame()


def calibrate_three_way_probabilities(home_win: float, draw: float, away_win: float) -> tuple[float, float, float]:
    probs = pd.Series([home_win, draw, away_win], dtype='float64')
    neutral = pd.Series([1 / 3, 1 / 3, 1 / 3], dtype='float64')
    probs = (probs * 0.68) + (neutral * 0.32)
    max_idx = probs.idxmax()
    if probs.iloc[max_idx] > 0.50:
        excess = probs.iloc[max_idx] - 0.50
        reduction = excess * 0.55
        probs.iloc[max_idx] -= reduction
        other_idx = [i for i in probs.index if i != max_idx]
        probs.iloc[other_idx] += reduction / 2
    probs = probs.clip(lower=0.18, upper=0.54)
    probs = probs / probs.sum()
    return tuple(probs.tolist())


fixtures = safe_read_csv(fixtures_path)
match_report = safe_read_csv(match_report_path)
team_strengths = safe_read_parquet(team_strength_path)
history = safe_read_parquet(historical_path)
rows = []

if len(history):
    league_home_avg = pd.to_numeric(history.get('FTHG'), errors='coerce').mean()
    league_away_avg = pd.to_numeric(history.get('FTAG'), errors='coerce').mean()
else:
    league_home_avg = 1.45
    league_away_avg = 1.20

home_advantage_multiplier = 1 + ((league_home_avg / max(league_away_avg, 0.01)) - 1) * 0.30

if len(fixtures) and len(match_report) and len(team_strengths):
    match_lookup = {}
    for _, row in match_report.dropna(subset=['matched_model_team']).iterrows():
        match_lookup[(str(row.get('fixture_id')), str(row.get('side')))] = row.get('matched_model_team')

    for _, fixture in fixtures.iterrows():
        fixture_id = str(fixture.get('fixture_id'))
        home_model = match_lookup.get((fixture_id, 'home_team'))
        away_model = match_lookup.get((fixture_id, 'away_team'))

        if not home_model or not away_model:
            continue
        if home_model not in team_strengths.index or away_model not in team_strengths.index:
            continue

        home_row = team_strengths.loc[home_model]
        away_row = team_strengths.loc[away_model]

        home_attack = home_row['home_attack_strength'] * 0.35 + home_row['recent_attack_strength'] * 0.25 + 0.40
        away_attack = away_row['away_attack_strength'] * 0.35 + away_row['recent_attack_strength'] * 0.25 + 0.40
        home_defense = home_row['home_defense_strength'] * 0.35 + home_row['recent_defense_strength'] * 0.25 + 0.40
        away_defense = away_row['away_defense_strength'] * 0.35 + away_row['recent_defense_strength'] * 0.25 + 0.40

        expected_home_goals = league_home_avg * home_attack * away_defense * home_advantage_multiplier
        expected_away_goals = league_away_avg * away_attack * home_defense
        expected_home_goals = (expected_home_goals * 0.60) + (league_home_avg * 0.40)
        expected_away_goals = (expected_away_goals * 0.60) + (league_away_avg * 0.40)
        expected_home_goals = max(min(expected_home_goals, 3.0), 0.55)
        expected_away_goals = max(min(expected_away_goals, 2.6), 0.45)

        home_win = draw = away_win = 0.0
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
        prediction_key = f"{fixture_id}|{fixture.get('match_date')}|{fixture.get('home_team')}|{fixture.get('away_team')}|forward_fixture_model"
        prediction_id = hashlib.sha256(prediction_key.encode('utf-8')).hexdigest()[:20]

        rows.append({
            'prediction_id': prediction_id,
            'fixture_id': fixture.get('fixture_id'),
            'match_date': fixture.get('match_date'),
            'match_time': fixture.get('match_time'),
            'home_team': fixture.get('home_team'),
            'away_team': fixture.get('away_team'),
            'league': fixture.get('league'),
            'sample_phase': 'upcoming_fixture_probability_only',
            'expected_home_goals': round(float(expected_home_goals), 3),
            'expected_away_goals': round(float(expected_away_goals), 3),
            'home_win_probability': round(float(home_win), 4),
            'draw_probability': round(float(draw), 4),
            'away_win_probability': round(float(away_win), 4),
            'fair_home_odds': round(1 / float(home_win), 2) if home_win > 0 else None,
            'fair_draw_odds': round(1 / float(draw), 2) if draw > 0 else None,
            'fair_away_odds': round(1 / float(away_win), 2) if away_win > 0 else None,
            'model_source': 'conservative_poisson_forward_fixture',
        })

predictions = pd.DataFrame(rows)
for col in expected_columns:
    if col not in predictions.columns:
        predictions[col] = None
predictions = predictions[expected_columns]

predictions.to_csv(output_dir / 'forward_fixture_predictions.csv', index=False)
predictions.to_parquet(output_dir / 'forward_fixture_predictions.parquet', index=False)

summary = {
    'upcoming_fixture_rows': int(len(fixtures)),
    'forward_fixture_prediction_rows': int(len(predictions)),
    'probability_only': True,
    'has_market_prices': False,
    'ready_for_price_join': bool(len(predictions) > 0),
}
pd.DataFrame([summary]).to_csv(output_dir / 'forward_fixture_prediction_summary.csv', index=False)

markdown = [
    '# Forward Fixture Predictions',
    '',
    'Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.',
    '',
    f"Upcoming fixture rows: {summary['upcoming_fixture_rows']}",
    f"Forward fixture prediction rows: {summary['forward_fixture_prediction_rows']}",
    f"Ready for price join: {summary['ready_for_price_join']}",
    '',
]

if len(predictions):
    for _, row in predictions.iterrows():
        markdown.append(
            f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | "
            f"H={row['home_win_probability']} D={row['draw_probability']} A={row['away_win_probability']} | "
            f"fair={row['fair_home_odds']}/{row['fair_draw_odds']}/{row['fair_away_odds']}"
        )
else:
    markdown.append('No forward fixture predictions built. Check fixture/model team matching first.')

(output_dir / 'forward_fixture_predictions.md').write_text('\n'.join(markdown), encoding='utf-8')

logger = Path('scripts/log_forward_fixture_predictions.py')
if logger.exists():
    try:
        runpy.run_path(str(logger), run_name='__main__')
    except Exception as exc:
        print(f'Forward fixture prediction logger skipped: {exc!r}')

print(summary)
