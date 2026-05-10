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
    'rejection_reason',
]

if not snapshot_path.exists():
    filtered = pd.DataFrame(columns=expected_columns)
    rejected = pd.DataFrame(columns=expected_columns)
else:
    predictions = pd.read_parquet(snapshot_path)

    for col in ['ev', 'probability', 'market_odds', 'fair_odds']:
        if col not in predictions.columns:
            predictions[col] = 0.0

    predictions['market_implied_probability'] = 1 / predictions['market_odds'].replace(0, pd.NA)
    predictions['probability_edge'] = (
        predictions['probability'].fillna(0) - predictions['market_implied_probability'].fillna(0)
    )

    predictions['model_market_ratio'] = predictions['probability'].fillna(0) / predictions['market_implied_probability'].replace(0, pd.NA)
    predictions['rejection_reason'] = ''

    # Sanity guardrails. If the model is wildly far from market, treat it as model-risk, not a bet.
    sane = predictions[
        (predictions['market_odds'].fillna(0).between(1.55, 2.80))
        & (predictions['probability'].fillna(0).between(0.38, 0.68))
        & (predictions['probability_edge'].fillna(0).between(0.04, 0.18))
        & (predictions['model_market_ratio'].fillna(99).between(1.08, 1.35))
        & (predictions['ev'].fillna(0).between(0.08, 0.32))
    ].copy()

    rejected = predictions[~predictions.index.isin(sane.index)].copy()
    if len(rejected):
        rejected['rejection_reason'] = 'outside_sanity_guardrails'

    if len(sane):
        sane['odds_stability_penalty'] = (sane['market_odds'] - 2.05).abs() / 8
        sane['signal_strength'] = (
            (sane['ev'].fillna(0) * 0.45)
            + (sane['probability_edge'].fillna(0) * 0.40)
            + (sane['probability'].fillna(0) * 0.15)
            - sane['odds_stability_penalty'].fillna(0)
        ).round(4)
        filtered = sane.sort_values('signal_strength', ascending=False).head(2)
    else:
        filtered = pd.DataFrame(columns=expected_columns)

for frame_name in ['filtered', 'rejected']:
    frame = locals().get(frame_name, pd.DataFrame())
    for col in expected_columns:
        if col not in frame.columns:
            frame[col] = None
    locals()[frame_name] = frame[expected_columns]

filtered.to_parquet(output_dir / 'candidate_bets.parquet', index=False)
filtered.to_csv(output_dir / 'candidate_bets.csv', index=False)
rejected.to_csv(output_dir / 'rejected_candidate_signals.csv', index=False)

markdown = ['# Candidate Bets', '']

if len(filtered) == 0:
    markdown.append('No candidate bets passed the current sanity guardrails.')
else:
    for _, row in filtered.iterrows():
        markdown.append(
            f"- {row['prediction_id']} | EV={round(float(row['ev']),4)} | "
            f"Prob={round(float(row['probability']),4)} | Edge={round(float(row['probability_edge']),4)}"
        )

markdown.extend([
    '',
    f'Rejected signals: {len(rejected)}',
])

(output_dir / 'candidate_bets.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(filtered)} sanity-checked candidate bets')
print(f'Rejected {len(rejected)} candidate-like signals')
print(filtered.head())
