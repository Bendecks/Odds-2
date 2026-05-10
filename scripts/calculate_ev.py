from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

predictions = pd.read_parquet(output_dir / 'poisson_predictions.parquet')
market = pd.read_parquet('data/raw/premier_league_2425.parquet')

latest_market = market.tail(len(predictions)).copy()
latest_market = latest_market.reset_index(drop=True)
predictions = predictions.reset_index(drop=True)

results = []

for idx, row in predictions.iterrows():
    market_row = latest_market.iloc[idx]

    home_odds = market_row.get('B365H')
    draw_odds = market_row.get('B365D')
    away_odds = market_row.get('B365A')

    home_ev = (row['home_win_probability'] * home_odds) - 1
    draw_ev = (row['draw_probability'] * draw_odds) - 1
    away_ev = (row['away_win_probability'] * away_odds) - 1

    results.append({
        'home_team': row['home_team'],
        'away_team': row['away_team'],
        'market_home_odds': home_odds,
        'market_draw_odds': draw_odds,
        'market_away_odds': away_odds,
        'fair_home_odds': row['fair_home_odds'],
        'fair_draw_odds': row['fair_draw_odds'],
        'fair_away_odds': row['fair_away_odds'],
        'home_ev': round(home_ev, 4),
        'draw_ev': round(draw_ev, 4),
        'away_ev': round(away_ev, 4),
    })

results_df = pd.DataFrame(results)

results_df.to_parquet(output_dir / 'ev_results.parquet', index=False)
results_df.to_csv(output_dir / 'ev_results.csv', index=False)

value_bets = results_df[
    (results_df['home_ev'] > 0.05)
    | (results_df['draw_ev'] > 0.05)
    | (results_df['away_ev'] > 0.05)
]

value_bets.to_csv(output_dir / 'value_bets.csv', index=False)

print(value_bets.head())
print(f'Found {len(value_bets)} potential value bets')
