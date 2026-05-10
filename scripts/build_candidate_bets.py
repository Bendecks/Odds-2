from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

predictions = pd.read_parquet(output_dir / 'prediction_snapshots_latest.parquet')

# Stronger filtering to reduce noise.
filtered = predictions[
    (predictions['ev'] >= 0.10)
    & (predictions['probability'] >= 0.42)
].copy()

filtered['signal_strength'] = (
    filtered['ev'] * filtered['probability']
).round(4)

filtered = filtered.sort_values('signal_strength', ascending=False)

# Keep only strongest signals.
filtered = filtered.head(5)

filtered.to_parquet(output_dir / 'candidate_bets.parquet', index=False)
filtered.to_csv(output_dir / 'candidate_bets.csv', index=False)

markdown = ['# Candidate Bets', '']

for _, row in filtered.iterrows():
    markdown.append(
        f"- {row['prediction_id']} | EV={round(row['ev'],4)} | Prob={round(row['probability'],4)}"
    )

(output_dir / 'candidate_bets.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(filtered)} strong candidate bets')
print(filtered.head())
