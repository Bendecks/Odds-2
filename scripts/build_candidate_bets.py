from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
snapshot_path = output_dir / 'prediction_snapshots_latest.parquet'

expected_columns = [
    'snapshot_id',
    'prediction_id',
    'event_id',
    'created_at_utc',
    'github_run_number',
    'github_run_id',
    'github_sha',
    'market_odds',
    'fair_odds',
    'probability',
    'ev',
    'is_candidate',
    'signal_strength',
]

if not snapshot_path.exists():
    filtered = pd.DataFrame(columns=expected_columns)
else:
    predictions = pd.read_parquet(snapshot_path)

    for col in ['ev', 'probability']:
        if col not in predictions.columns:
            predictions[col] = 0.0

    # Stronger filtering to reduce noise.
    filtered = predictions[
        (predictions['ev'].fillna(0) >= 0.10)
        & (predictions['probability'].fillna(0) >= 0.42)
    ].copy()

    if len(filtered):
        filtered['signal_strength'] = (
            filtered['ev'].fillna(0) * filtered['probability'].fillna(0)
        ).round(4)
        filtered = filtered.sort_values('signal_strength', ascending=False).head(5)
    else:
        filtered = pd.DataFrame(columns=expected_columns)

for col in expected_columns:
    if col not in filtered.columns:
        filtered[col] = None

filtered = filtered[expected_columns]

filtered.to_parquet(output_dir / 'candidate_bets.parquet', index=False)
filtered.to_csv(output_dir / 'candidate_bets.csv', index=False)

markdown = ['# Candidate Bets', '']

if len(filtered) == 0:
    markdown.append('No candidate bets passed the current filters.')
else:
    for _, row in filtered.iterrows():
        markdown.append(
            f"- {row['prediction_id']} | EV={round(float(row['ev']),4)} | Prob={round(float(row['probability']),4)}"
        )

(output_dir / 'candidate_bets.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(filtered)} strong candidate bets')
print(filtered.head())
