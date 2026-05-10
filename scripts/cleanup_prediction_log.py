from pathlib import Path

import pandas as pd

jsonl_path = Path('data/predictions/prediction_log.jsonl')

if not jsonl_path.exists():
    print('Prediction log does not exist')
    raise SystemExit(0)

predictions = pd.read_json(jsonl_path, lines=True)

before = len(predictions)

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
print(f'Prediction archive now contains {after} unique predictions')
