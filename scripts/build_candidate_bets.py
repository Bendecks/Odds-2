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
    'model_market_ratio',
    'ev',
    'signal_strength',
    'confidence_tier',
    'alignment_penalty',
    'is_candidate',
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
        predictions['probability'].fillna(0)
        - predictions['market_implied_probability'].fillna(0)
    )

    predictions['model_market_ratio'] = (
        predictions['probability'].fillna(0)
        / predictions['market_implied_probability'].replace(0, pd.NA)
    )

    predictions['alignment_penalty'] = (
        predictions['model_market_ratio'].fillna(1) - 1
    ).abs()

    predictions['rejection_reason'] = ''

    sane = predictions[
        (predictions['market_odds'].fillna(0).between(1.50, 3.20))
        & (predictions['probability'].fillna(0).between(0.34, 0.72))
        & (predictions['probability_edge'].fillna(0).between(0.03, 0.20))
        & (predictions['ev'].fillna(0).between(0.05, 0.35))
    ].copy()

    rejected = predictions[~predictions.index.isin(sane.index)].copy()

    if len(rejected):
        rejected['rejection_reason'] = 'outside_dynamic_quality_filters'

    if len(sane):
        sane['signal_strength'] = (
            (sane['ev'].fillna(0) * 0.40)
            + (sane['probability_edge'].fillna(0) * 0.35)
            + (sane['probability'].fillna(0) * 0.10)
            + ((1 - sane['alignment_penalty'].fillna(1)) * 0.15)
        ).round(4)

        sane['confidence_tier'] = 'watchlist'

        sane.loc[
            (sane['signal_strength'] >= 0.22)
            & (sane['alignment_penalty'] <= 0.18),
            'confidence_tier'
        ] = 'medium'

        sane.loc[
            (sane['signal_strength'] >= 0.28)
            & (sane['alignment_penalty'] <= 0.12),
            'confidence_tier'
        ] = 'high'

        sane = sane.sort_values(
            ['confidence_tier', 'signal_strength'],
            ascending=[False, False],
        )

        filtered = sane.head(5)
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
    markdown.append('No candidate bets passed the current quality filters.')
else:
    for _, row in filtered.iterrows():
        markdown.append(
            f"- {row['prediction_id']} | tier={row['confidence_tier']} | "
            f"EV={round(float(row['ev']),4)} | "
            f"Strength={round(float(row['signal_strength']),4)} | "
            f"Penalty={round(float(row['alignment_penalty']),4)}"
        )

markdown.extend([
    '',
    f'Rejected signals: {len(rejected)}',
])

(output_dir / 'candidate_bets.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(filtered)} graded candidate bets')
print(f'Rejected {len(rejected)} lower-quality signals')
print(filtered.head())
