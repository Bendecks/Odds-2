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
    'market_implied_probability',
    'probability_edge',
    'ev',
    'is_candidate',
    'signal_strength',
]

if not snapshot_path.exists():
    filtered = pd.DataFrame(columns=expected_columns)
else:
    predictions = pd.read_parquet(snapshot_path)

    for col in ['ev', 'probability', 'market_odds', 'fair_odds']:
        if col not in predictions.columns:
            predictions[col] = 0.0

    predictions['market_implied_probability'] = 1 / predictions['market_odds'].replace(0, pd.NA)
    predictions['probability_edge'] = (
        predictions['probability'].fillna(0) - predictions['market_implied_probability'].fillna(0)
    )

    # Tight research-only filter. This intentionally prefers no bet over noisy bets.
    filtered = predictions[
        (predictions['ev'].fillna(0) >= 0.12)
        & (predictions['probability'].fillna(0) >= 0.45)
        & (predictions['probability_edge'].fillna(0) >= 0.04)
        & (predictions['market_odds'].fillna(0).between(1.45, 3.50))
    ].copy()

    if len(filtered):
        # Penalize very short or very long odds; reward probability edge and EV jointly.
        filtered['odds_stability_penalty'] = (filtered['market_odds'] - 2.1).abs() / 10
        filtered['signal_strength'] = (
            (filtered['ev'].fillna(0) * 0.55)
            + (filtered['probability_edge'].fillna(0) * 0.35)
            + (filtered['probability'].fillna(0) * 0.10)
            - filtered['odds_stability_penalty'].fillna(0)
        ).round(4)
        filtered = filtered.sort_values('signal_strength', ascending=False).head(3)
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
            f"- {row['prediction_id']} | EV={round(float(row['ev']),4)} | "
            f"Prob={round(float(row['probability']),4)} | Edge={round(float(row['probability_edge']),4)}"
        )

(output_dir / 'candidate_bets.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(filtered)} tightly filtered candidate bets')
print(filtered.head())
