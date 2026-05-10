from pathlib import Path

import pandas as pd

prediction_log = Path('data/predictions/prediction_log.jsonl')
market_path = Path('data/raw/premier_league_2425.parquet')
output_dir = Path('output/latest')

if not prediction_log.exists():
    print('No prediction log found')
    raise SystemExit(0)

predictions = pd.read_json(prediction_log, lines=True)
market = pd.read_parquet(market_path)

market['Date'] = market['Date'].astype(str)

settled = []

for _, pred in predictions.iterrows():
    if pred['settlement_status'] == 'settled':
        settled.append(pred.to_dict())
        continue

    match = market[
        (market['HomeTeam'] == pred['home_team'])
        & (market['AwayTeam'] == pred['away_team'])
        & (market['Date'] == pred['match_date'])
    ]

    if match.empty:
        settled.append(pred.to_dict())
        continue

    match = match.iloc[0]

    result = match['FTR']

    won = False

    if pred['selection'] == 'home' and result == 'H':
        won = True
    elif pred['selection'] == 'draw' and result == 'D':
        won = True
    elif pred['selection'] == 'away' and result == 'A':
        won = True

    roi = pred['market_odds'] - 1 if won else -1

    updated = pred.to_dict()
    updated['settlement_status'] = 'settled'
    updated['match_result'] = result
    updated['won'] = won
    updated['roi_units'] = round(float(roi), 4)

    settled.append(updated)

settled_df = pd.DataFrame(settled)

settled_df.to_parquet(output_dir / 'settled_predictions.parquet', index=False)
settled_df.to_csv(output_dir / 'settled_predictions.csv', index=False)

summary = {
    'total_predictions': int(len(settled_df)),
    'settled_predictions': int((settled_df['settlement_status'] == 'settled').sum()),
    'wins': int((settled_df.get('won', False) == True).sum()),
    'total_roi_units': round(float(settled_df.get('roi_units', pd.Series(dtype=float)).fillna(0).sum()), 4),
}

summary_df = pd.DataFrame([summary])
summary_df.to_csv(output_dir / 'performance_summary.csv', index=False)

print(summary)
