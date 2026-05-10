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
created_at = datetime.now(timezone.utc).isoformat()

predictions = pd.read_parquet(output_dir / 'ev_results.parquet')
market = pd.read_parquet('data/raw/premier_league_2425.parquet')

latest_market = market.tail(len(predictions)).copy().reset_index(drop=True)
predictions = predictions.reset_index(drop=True)

prediction_log_path = log_dir / 'prediction_log.jsonl'
snapshot_log_path = log_dir / 'prediction_snapshots.jsonl'

existing_prediction_ids = set()

if prediction_log_path.exists():
    existing_df = pd.read_json(prediction_log_path, lines=True)
    if 'prediction_id' in existing_df.columns:
        existing_prediction_ids = set(existing_df['prediction_id'].astype(str).tolist())

prediction_records = []
snapshot_records = []

for idx, row in predictions.iterrows():
    market_row = latest_market.iloc[idx]
    match_date = str(market_row.get('Date', ''))
    match_time = str(market_row.get('Time', ''))
    home_team = row['home_team']
    away_team = row['away_team']

    event_base = f'{match_date}|{match_time}|{home_team}|{away_team}'
    event_id = hashlib.sha256(event_base.encode('utf-8')).hexdigest()[:16]

    markets = [
        {
            'selection': 'home',
            'probability': row.get('home_win_probability'),
            'fair_odds': row['fair_home_odds'],
            'market_odds': row['market_home_odds'],
            'ev': row['home_ev'],
        },
        {
            'selection': 'draw',
            'probability': row.get('draw_probability'),
            'fair_odds': row['fair_draw_odds'],
            'market_odds': row['market_draw_odds'],
            'ev': row['draw_ev'],
        },
        {
            'selection': 'away',
            'probability': row.get('away_win_probability'),
            'fair_odds': row['fair_away_odds'],
            'market_odds': row['market_away_odds'],
            'ev': row['away_ev'],
        },
    ]

    for market_prediction in markets:
        prediction_key = f"{event_id}|1x2|{market_prediction['selection']}"
        prediction_id = hashlib.sha256(prediction_key.encode('utf-8')).hexdigest()[:20]

        snapshot_key = (
            f"{prediction_id}|{run_number}|{sha}|"
            f"{round(float(market_prediction['market_odds']), 4)}|"
            f"{round(float(market_prediction['fair_odds']), 4)}"
        )
        snapshot_id = hashlib.sha256(snapshot_key.encode('utf-8')).hexdigest()[:20]

        ev_threshold = 0.08
        probability_threshold = 0.35

        is_candidate = bool(
            market_prediction['ev'] > ev_threshold
            and market_prediction['probability'] > probability_threshold
        )

        snapshot_records.append({
            'snapshot_id': snapshot_id,
            'prediction_id': prediction_id,
            'event_id': event_id,
            'created_at_utc': created_at,
            'github_run_number': run_number,
            'github_run_id': run_id,
            'github_sha': sha,
            'market_odds': market_prediction['market_odds'],
            'fair_odds': market_prediction['fair_odds'],
            'probability': market_prediction['probability'],
            'ev': market_prediction['ev'],
            'is_candidate': is_candidate,
        })

        if prediction_id in existing_prediction_ids:
            continue

        prediction_records.append({
            'prediction_id': prediction_id,
            'event_id': event_id,
            'created_at_utc': created_at,
            'first_seen_run_number': run_number,
            'first_seen_run_id': run_id,
            'first_seen_sha': sha,
            'match_date': match_date,
            'match_time': match_time,
            'home_team': home_team,
            'away_team': away_team,
            'market': '1x2',
            'selection': market_prediction['selection'],
            'opening_market_odds': market_prediction['market_odds'],
            'opening_fair_odds': market_prediction['fair_odds'],
            'opening_probability': market_prediction['probability'],
            'opening_ev': market_prediction['ev'],
            'is_candidate': is_candidate,
            'settlement_status': 'pending',
        })

prediction_df = pd.DataFrame(prediction_records)
snapshot_df = pd.DataFrame(snapshot_records)

# Always write latest snapshot output so downstream steps have a stable file.
snapshot_df.to_parquet(output_dir / 'prediction_snapshots_latest.parquet', index=False)
snapshot_df.to_csv(output_dir / 'prediction_snapshots_latest.csv', index=False)

if len(prediction_df) == 0:
    # If no new predictions, expose current known predictions for downstream reporting.
    if prediction_log_path.exists():
        existing_df = pd.read_json(prediction_log_path, lines=True)
        existing_df.to_parquet(output_dir / 'prediction_log_latest.parquet', index=False)
        existing_df.to_csv(output_dir / 'prediction_log_latest.csv', index=False)
    else:
        prediction_df.to_parquet(output_dir / 'prediction_log_latest.parquet', index=False)
        prediction_df.to_csv(output_dir / 'prediction_log_latest.csv', index=False)
    print('No new unique predictions generated')
else:
    prediction_df.to_parquet(output_dir / 'prediction_log_latest.parquet', index=False)
    prediction_df.to_csv(output_dir / 'prediction_log_latest.csv', index=False)

    with prediction_log_path.open('a', encoding='utf-8') as f:
        for record in prediction_records:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')

with snapshot_log_path.open('a', encoding='utf-8') as f:
    for record in snapshot_records:
        f.write(json.dumps(record, ensure_ascii=False) + '\n')

candidate_count = int(snapshot_df['is_candidate'].sum()) if len(snapshot_df) else 0

print(f'Logged {len(prediction_records)} new stable predictions')
print(f'Logged {len(snapshot_records)} prediction snapshots')
print(f'Candidate snapshots after filtering: {candidate_count}')
