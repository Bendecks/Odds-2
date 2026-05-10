from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

predictions = pd.read_parquet(output_dir / 'poisson_predictions.parquet')
market_snapshot = pd.read_parquet(output_dir / 'market_snapshot_latest.parquet')

latest_market = market_snapshot.tail(len(predictions)).copy()
latest_market = latest_market.reset_index(drop=True)
predictions = predictions.reset_index(drop=True)

results = []

for idx, row in predictions.iterrows():
    market_row = latest_market.iloc[idx]

    home_odds = market_row.get('market_home_odds', market_row.get('B365H'))
    draw_odds = market_row.get('market_draw_odds', market_row.get('B365D'))
    away_odds = market_row.get('market_away_odds', market_row.get('B365A'))

    home_odds = pd.to_numeric(home_odds, errors='coerce')
    draw_odds = pd.to_numeric(draw_odds, errors='coerce')
    away_odds = pd.to_numeric(away_odds, errors='coerce')

    home_ev = (row['home_win_probability'] * home_odds) - 1 if pd.notna(home_odds) else None
    draw_ev = (row['draw_probability'] * draw_odds) - 1 if pd.notna(draw_odds) else None
    away_ev = (row['away_win_probability'] * away_odds) - 1 if pd.notna(away_odds) else None

    results.append({
        'snapshot_created_at_utc': market_row.get('snapshot_created_at_utc'),
        'snapshot_source': market_row.get('snapshot_source'),
        'market_overround': market_row.get('market_overround'),
        'home_team': row['home_team'],
        'away_team': row['away_team'],
        'home_win_probability': row['home_win_probability'],
        'draw_probability': row['draw_probability'],
        'away_win_probability': row['away_win_probability'],
        'market_home_odds': home_odds,
        'market_draw_odds': draw_odds,
        'market_away_odds': away_odds,
        'fair_home_odds': row['fair_home_odds'],
        'fair_draw_odds': row['fair_draw_odds'],
        'fair_away_odds': row['fair_away_odds'],
        'home_ev': round(home_ev, 4) if home_ev is not None else None,
        'draw_ev': round(draw_ev, 4) if draw_ev is not None else None,
        'away_ev': round(away_ev, 4) if away_ev is not None else None,
    })

results_df = pd.DataFrame(results)

results_df.to_parquet(output_dir / 'ev_results.parquet', index=False)
results_df.to_csv(output_dir / 'ev_results.csv', index=False)

value_bets = results_df[
    (results_df['home_ev'].fillna(-999) > 0.05)
    | (results_df['draw_ev'].fillna(-999) > 0.05)
    | (results_df['away_ev'].fillna(-999) > 0.05)
]

value_bets.to_csv(output_dir / 'value_bets.csv', index=False)

print(value_bets.head())
print(f'Found {len(value_bets)} potential value bets')
