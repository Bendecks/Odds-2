import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
log_dir = Path('data/predictions')
log_dir.mkdir(parents=True, exist_ok=True)

run_number = os.getenv('GITHUB_RUN_NUMBER', 'local')
run_id = os.getenv('GITHUB_RUN_ID', 'local')
sha = os.getenv('GITHUB_SHA', 'local')

predictions = pd.read_parquet(output_dir / 'ev_results.parquet')
market = pd.read_parquet('data/raw/premier_league_2425.parquet')

latest_market = market.tail(len(predictions)).copy().reset_index(drop=True)
predictions = predictions.reset_index(drop=True)

records = []

for idx, row in predictions.iterrows():
    market_row = latest_market.iloc[idx]
    match_date = str(market_row.get('Date', ''))
    match_time = str(market_row.get('Time', ''))
    home_team = row['home_team']
    away_team = row['away_team']

    base = f'{match_date}|{match_time}|{home_team}|{away_team}'
    event_id = hashlib.sha256(base.encode('utf-8')).hexdigest()[:16]

    markets = [
        {
            'selection': 'home',
            'probability': None,
            'fair_odds': row['fair_home_odds'],
            'market_odds': row['market_home_odds'],
            'ev': row['home_ev'],
        },
        {
            'selection': 'draw',
            'probability': None,
            'fair_odds': row['fair_draw_odds'],
            'market_odds': row['market_draw_odds'],
            'ev': row['draw_ev'],
        },
        {
            'selection': 'away',
            'probability': None,
            'fair_odds': row['fair_away_odds'],
            'market_odds': row['market_away_odds'],
            'ev': row['away_ev'],
        },
    ]

    for market_prediction in markets:
        prediction_id = hashlib.sha256(
            f"{event_id}|1x2|{market_prediction['selection']}|{run_number}|{sha}".encode('utf-8')
        ).hexdigest()[:20]

        records.append({
            'prediction_id': prediction_id,
            'event_id': event_id,
            'created_at_utc': datetime.now(timezone.utc).isoformat(),
            'github_run_number': run_number,
            'github_run_id': run_id,
            'github_sha': sha,
            'match_date': match_date,
            'match_time': match_time,
            'home_team': home_team,
            'away_team': away_team,
            'market': '1x2',
            **market_prediction,
            'is_candidate': bool(market_prediction['ev'] > 0.05),
            'settlement_status': 'pending',
        })

log_df = pd.DataFrame(records)
log_df.to_parquet(output_dir / 'prediction_log_latest.parquet', index=False)
log_df.to_csv(output_dir / 'prediction_log_latest.csv', index=False)

jsonl_path = log_dir / 'prediction_log.jsonl'
with jsonl_path.open('a', encoding='utf-8') as f:
    for record in records:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

print(f'Logged {len(records)} predictions to {jsonl_path}')
print(log_df[log_df['is_candidate']].head())
