from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
snapshot_path = output_dir / 'prediction_snapshots_latest.parquet'
prediction_log_path = output_dir / 'prediction_log_latest.parquet'
suppression_rules_path = output_dir / 'signal_suppression_rules.csv'

expected_columns = [
    'snapshot_id', 'prediction_id', 'event_id', 'created_at_utc',
    'github_run_number', 'github_run_id', 'github_sha',
    'match_date', 'match_time', 'home_team', 'away_team',
    'league', 'season', 'sample_phase', 'selection',
    'market_odds', 'fair_odds', 'probability', 'probability_band',
    'market_implied_probability', 'probability_edge', 'model_market_ratio',
    'ev', 'signal_strength', 'confidence_tier', 'alignment_penalty',
    'calibration_risk', 'suppression_action', 'is_candidate', 'rejection_reason',
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def safe_read_parquet(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_parquet(path)
    except Exception:
        return pd.DataFrame()


def probability_band(probability: float) -> str:
    if pd.isna(probability):
        return 'unknown'
    for start, end in [(0.00, 0.35), (0.35, 0.45), (0.45, 0.50), (0.50, 0.55), (0.55, 1.00)]:
        if start <= float(probability) < end:
            return f'{start:.2f}-{end:.2f}'
    return 'unknown'


def attach_match_metadata(df: pd.DataFrame) -> pd.DataFrame:
    log = safe_read_parquet(prediction_log_path)
    if len(df) == 0 or len(log) == 0 or 'prediction_id' not in df.columns or 'prediction_id' not in log.columns:
        return df

    metadata_cols = [
        'prediction_id', 'match_date', 'match_time', 'home_team', 'away_team',
        'league', 'season', 'sample_phase', 'selection'
    ]
    metadata_cols = [col for col in metadata_cols if col in log.columns]
    if len(metadata_cols) <= 1:
        return df

    merged = df.merge(
        log[metadata_cols].drop_duplicates('prediction_id'),
        on='prediction_id',
        how='left',
        suffixes=('', '_log'),
    )

    for col in metadata_cols:
        if col == 'prediction_id':
            continue
        log_col = f'{col}_log'
        if log_col in merged.columns:
            if col in merged.columns:
                merged[col] = merged[col].fillna(merged[log_col])
            else:
                merged[col] = merged[log_col]

    return merged


if not snapshot_path.exists():
    filtered = pd.DataFrame(columns=expected_columns)
    rejected = pd.DataFrame(columns=expected_columns)
else:
    predictions = safe_read_parquet(snapshot_path)
    predictions = attach_match_metadata(predictions)

    if len(predictions) == 0:
        filtered = pd.DataFrame(columns=expected_columns)
        rejected = pd.DataFrame(columns=expected_columns)
    else:
        defaults = {
            'ev': 0.0,
            'probability': 0.0,
            'market_odds': 0.0,
            'fair_odds': 0.0,
            'match_date': '',
            'match_time': '',
            'home_team': 'unknown',
            'away_team': 'unknown',
            'league': 'unknown',
            'season': 'unknown',
            'sample_phase': 'historical_proxy_research',
            'selection': 'unknown',
        }
        for col, default in defaults.items():
            if col not in predictions.columns:
                predictions[col] = default

        for col in ['ev', 'probability', 'market_odds', 'fair_odds']:
            predictions[col] = pd.to_numeric(predictions[col], errors='coerce')

        predictions['market_implied_probability'] = 1 / predictions['market_odds'].replace(0, pd.NA)
        predictions['probability_edge'] = predictions['probability'].fillna(0) - predictions['market_implied_probability'].fillna(0)
        predictions['model_market_ratio'] = predictions['probability'].fillna(0) / predictions['market_implied_probability'].replace(0, pd.NA)
        predictions['alignment_penalty'] = (predictions['model_market_ratio'].fillna(1) - 1).abs()
        predictions['probability_band'] = predictions['probability'].apply(probability_band)

        predictions['calibration_risk'] = 'normal'
        predictions.loc[predictions['probability'].fillna(0) >= 0.50, 'calibration_risk'] = 'high_probability_band'
        predictions.loc[predictions['probability_edge'].fillna(0) >= 0.14, 'calibration_risk'] = 'large_probability_edge'
        predictions.loc[predictions['alignment_penalty'].fillna(0) >= 0.18, 'calibration_risk'] = 'market_misalignment'

        predictions['suppression_action'] = 'none'
        rules = safe_read_csv(suppression_rules_path)
        if len(rules):
            for _, rule in rules.iterrows():
                rule_type = str(rule.get('rule_type'))
                target = str(rule.get('target'))
                action = str(rule.get('action'))
                if rule_type == 'probability_band':
                    mask = predictions['probability_band'].astype(str) == target
                elif rule_type == 'league':
                    mask = predictions['league'].astype(str) == target
                else:
                    continue
                if action == 'suppress':
                    predictions.loc[mask, 'suppression_action'] = 'suppress'
                elif action == 'downweight':
                    predictions.loc[mask & (predictions['suppression_action'] != 'suppress'), 'suppression_action'] = 'downweight'
                elif action == 'monitor':
                    predictions.loc[mask & (predictions['suppression_action'] == 'none'), 'suppression_action'] = 'monitor'

        sane = predictions[
            (predictions['suppression_action'] != 'suppress')
            & (predictions['market_odds'].fillna(0).between(1.65, 3.60))
            & (predictions['probability'].fillna(0).between(0.34, 0.50))
            & (predictions['probability_edge'].fillna(0).between(0.02, 0.12))
            & (predictions['ev'].fillna(0).between(0.035, 0.18))
            & (predictions['alignment_penalty'].fillna(1).between(0.00, 0.15))
        ].copy()

        rejected = predictions[~predictions.index.isin(sane.index)].copy()
        if len(rejected):
            rejected['rejection_reason'] = 'outside_suppression_aware_quality_filters'
            rejected.loc[rejected['suppression_action'] == 'suppress', 'rejection_reason'] = 'suppressed_by_signal_suppression_rules'
            rejected.loc[rejected['suppression_action'] == 'monitor', 'rejection_reason'] = rejected['rejection_reason'].fillna('monitor_zone_filtered_by_quality_rules')

        if len(sane):
            downweight_multiplier = sane['suppression_action'].map({'downweight': 0.60, 'monitor': 0.90}).fillna(1.0)
            sane['signal_strength'] = (
                ((sane['ev'].fillna(0) * 0.28)
                + (sane['probability_edge'].fillna(0) * 0.28)
                + (sane['probability'].fillna(0) * 0.08)
                + ((1 - sane['alignment_penalty'].fillna(1)) * 0.20)
                - (sane['alignment_penalty'].fillna(1) * 0.16))
                * downweight_multiplier
            ).round(4)
            sane['confidence_tier'] = 'watchlist'
            sane.loc[
                (sane['signal_strength'] >= 0.18)
                & (sane['alignment_penalty'] <= 0.12)
                & (sane['probability'] < 0.50)
                & (sane['suppression_action'].isin(['none', 'monitor'])),
                'confidence_tier'
            ] = 'medium'
            filtered = sane.sort_values(['confidence_tier', 'signal_strength'], ascending=[False, False]).head(5)
        else:
            filtered = pd.DataFrame(columns=expected_columns)

for name in ['filtered', 'rejected']:
    frame = locals().get(name, pd.DataFrame())
    for col in expected_columns:
        if col not in frame.columns:
            frame[col] = None
    locals()[name] = frame[expected_columns]

filtered.to_parquet(output_dir / 'candidate_bets.parquet', index=False)
filtered.to_csv(output_dir / 'candidate_bets.csv', index=False)
rejected.to_csv(output_dir / 'rejected_candidate_signals.csv', index=False)

markdown = ['# Candidate Bets', '']
if len(filtered) == 0:
    markdown.append('No candidate bets passed the current suppression-aware quality filters.')
else:
    markdown.append('Research/paper-test only. No real-money recommendation.')
    markdown.append('')
    for _, row in filtered.iterrows():
        markdown.append(
            f"- {row['prediction_id']} | {row['home_team']} vs {row['away_team']} | "
            f"tier={row['confidence_tier']} | EV={round(float(row['ev']),4)} | "
            f"Strength={round(float(row['signal_strength']),4)} | "
            f"Penalty={round(float(row['alignment_penalty']),4)} | Band={row['probability_band']} | "
            f"Suppression={row['suppression_action']} | Calibration risk={row['calibration_risk']}"
        )
markdown.extend(['', f'Rejected signals: {len(rejected)}'])
(output_dir / 'candidate_bets.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(filtered)} suppression-aware candidate bets')
print(f'Rejected {len(rejected)} lower-quality signals')
print(filtered.head())
