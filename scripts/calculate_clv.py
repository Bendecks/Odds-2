from pathlib import Path

import pandas as pd

prediction_log_path = Path('output/latest/prediction_log_latest.parquet')
market_path = Path('data/raw/premier_league_2425.parquet')
output_dir = Path('output/latest')

predictions = pd.read_parquet(prediction_log_path)
market = pd.read_parquet(market_path)

market['Date'] = market['Date'].astype(str)

clv_records = []

for _, pred in predictions.iterrows():
    match = market[
        (market['HomeTeam'] == pred['home_team'])
        & (market['AwayTeam'] == pred['away_team'])
        & (market['Date'] == pred['match_date'])
    ]

    if match.empty:
        continue

    match = match.iloc[0]

    if pred['selection'] == 'home':
        closing_odds = match.get('PSCH')
    elif pred['selection'] == 'draw':
        closing_odds = match.get('PSCD')
    else:
        closing_odds = match.get('PSCA')

    # New stable schema uses opening_market_odds.
    # Legacy schema used market_odds. Keep both supported.
    opening_odds = pred.get('opening_market_odds')
    if pd.isna(opening_odds) and 'market_odds' in pred:
        opening_odds = pred.get('market_odds')

    if pd.isna(closing_odds) or pd.isna(opening_odds):
        continue

    clv_delta = float(opening_odds) - float(closing_odds)
    beat_closing_line = clv_delta > 0

    clv_records.append({
        'prediction_id': pred['prediction_id'],
        'home_team': pred['home_team'],
        'away_team': pred['away_team'],
        'selection': pred['selection'],
        'opening_odds': opening_odds,
        'closing_odds': closing_odds,
        'clv_delta': round(clv_delta, 4),
        'beat_closing_line': beat_closing_line,
    })

clv_df = pd.DataFrame(clv_records)

expected_columns = [
    'prediction_id',
    'home_team',
    'away_team',
    'selection',
    'opening_odds',
    'closing_odds',
    'clv_delta',
    'beat_closing_line',
]

for col in expected_columns:
    if col not in clv_df.columns:
        clv_df[col] = None

clv_df = clv_df[expected_columns]

clv_df.to_parquet(output_dir / 'clv_results.parquet', index=False)
clv_df.to_csv(output_dir / 'clv_results.csv', index=False)

summary = {
    'tracked_predictions': int(len(clv_df)),
    'beat_closing_line_count': int(clv_df['beat_closing_line'].fillna(False).sum()) if len(clv_df) else 0,
    'beat_closing_line_rate': round(float(clv_df['beat_closing_line'].fillna(False).mean()), 4) if len(clv_df) else 0,
    'average_clv_delta': round(float(clv_df['clv_delta'].dropna().mean()), 4) if len(clv_df['clv_delta'].dropna()) else 0,
}

pd.DataFrame([summary]).to_csv(output_dir / 'clv_summary.csv', index=False)

print(summary)
