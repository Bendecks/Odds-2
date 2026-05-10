from pathlib import Path

import pandas as pd

jsonl_path = Path('data/predictions/prediction_log.jsonl')

if not jsonl_path.exists():
    print('Prediction log does not exist')
    raise SystemExit(0)

predictions = pd.read_json(jsonl_path, lines=True)

before = len(predictions)

# Normalize legacy records from the pre-snapshot architecture.
legacy_mappings = {
    'github_run_number': 'first_seen_run_number',
    'github_run_id': 'first_seen_run_id',
    'github_sha': 'first_seen_sha',
    'market_odds': 'opening_market_odds',
    'fair_odds': 'opening_fair_odds',
    'probability': 'opening_probability',
    'ev': 'opening_ev',
}

for old_col, new_col in legacy_mappings.items():
    if new_col not in predictions.columns:
        predictions[new_col] = None
    if old_col in predictions.columns:
        predictions[new_col] = predictions[new_col].fillna(predictions[old_col])

required_columns = [
    'prediction_id',
    'event_id',
    'created_at_utc',
    'first_seen_run_number',
    'first_seen_run_id',
    'first_seen_sha',
    'match_date',
    'match_time',
    'home_team',
    'away_team',
    'market',
    'selection',
    'opening_market_odds',
    'opening_fair_odds',
    'opening_probability',
    'opening_ev',
    'is_candidate',
    'settlement_status',
]

for col in required_columns:
    if col not in predictions.columns:
        predictions[col] = None

predictions['settlement_status'] = predictions['settlement_status'].fillna('pending')
predictions['market'] = predictions['market'].fillna('1x2')
predictions['is_candidate'] = predictions['is_candidate'].fillna(False)

predictions = predictions[required_columns + [c for c in predictions.columns if c not in required_columns]]
predictions = predictions.sort_values('created_at_utc')
predictions = predictions.drop_duplicates(subset=['prediction_id'], keep='first')

after = len(predictions)
removed = before - after

predictions.to_json(
    jsonl_path,
    orient='records',
    lines=True,
    force_ascii=False,
)

print(f'Removed {removed} duplicate predictions')
print(f'Prediction archive now contains {after} unique normalized predictions')
