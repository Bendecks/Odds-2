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
    'calibration_risk',
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

    predictions['calibration_risk'] = 'normal'
    predictions.loc[predictions['probability'].fillna(0) >= 0.50, 'calibration_risk'] = 'high_probability_band'
    predictions.loc[predictions['probability_edge'].fillna(0) >= 0.14, 'calibration_risk'] = 'large_probability_edge'
    predictions.loc[predictions['alignment_penalty'].fillna(0) >= 0.18, 'calibration_risk'] = 'market_misalignment'

    predictions['rejection_reason'] = ''

    sane = predictions[
        (predictions['market_odds'].fillna(0).between(1.60, 3.40))
        & (predictions['probability'].fillna(0).between(0.34, 0.54))
        & (predictions['probability_edge'].fillna(0).between(0.025, 0.14))
        & (predictions['ev'].fillna(0).between(0.04, 0.24))
        & (predictions['alignment_penalty'].fillna(1).between(0.00, 0.18))
    ].copy()

    rejected = predictions[~predictions.index.isin(sane.index)].copy()

    if len(rejected):
        rejected['rejection_reason'] = 'outside_calibration_aware_quality_filters'

    if len(sane):
        # Penalise the exact signal types that current diagnostics flag as unsafe:
        # high model probability, large model-market disagreement and oversized EV.
        sane['signal_strength'] = (
            (sane['ev'].fillna(0) * 0.32)
            + (sane['probability_edge'].fillna(0) * 0.30)
            + (sane['probability'].fillna(0) * 0.08)
            + ((1 - sane['alignment_penalty'].fillna(1)) * 0.18)
            - (sane['alignment_penalty'].fillna(1) * 0.12)
        ).round(4)

        sane['confidence_tier'] = 'watchlist'

        sane.loc[
            (sane['signal_strength'] >= 0.20)
            & (sane['alignment_penalty'] <= 0.14)
            & (sane['probability'] < 0.52),
            'confidence_tier'
        ] = 'medium'

        # Disabled for now: diagnostics do not support high-confidence labelling.
        sane['confidence_tier'] = sane['confidence_tier'].replace({'high': 'medium'})

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
    markdown.append('No candidate bets passed the current calibration-aware quality filters.')
else:
    markdown.append('Research/paper-test only. No real-money recommendation.')
    markdown.append('')
    for _, row in filtered.iterrows():
        markdown.append(
            f"- {row['prediction_id']} | tier={row['confidence_tier']} | "
            f"EV={round(float(row['ev']),4)} | "
            f"Strength={round(float(row['signal_strength']),4)} | "
            f"Penalty={round(float(row['alignment_penalty']),4)} | "
            f"Calibration risk={row['calibration_risk']}"
        )

markdown.extend([
    '',
    f'Rejected signals: {len(rejected)}',
])

(output_dir / 'candidate_bets.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(filtered)} calibration-aware candidate bets')
print(f'Rejected {len(rejected)} lower-quality signals')
print(filtered.head())
