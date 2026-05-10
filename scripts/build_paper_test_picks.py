import json
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
log_dir = Path('data/predictions')
log_dir.mkdir(parents=True, exist_ok=True)

snapshot_path = output_dir / 'prediction_snapshots_latest.parquet'
prediction_log_path = output_dir / 'prediction_log_latest.parquet'
rules_path = output_dir / 'signal_suppression_rules.csv'
paper_log_path = log_dir / 'paper_test_log.jsonl'

expected_columns = [
    'snapshot_id', 'prediction_id', 'event_id', 'created_at_utc',
    'match_date', 'match_time', 'home_team', 'away_team',
    'league', 'season', 'sample_phase', 'selection',
    'market_odds', 'fair_odds', 'probability', 'probability_band',
    'market_implied_probability', 'probability_edge', 'model_market_ratio',
    'ev', 'alignment_penalty', 'calibration_risk', 'suppression_action',
    'paper_test_tier', 'paper_test_score', 'paper_test_reason',
]


def safe_read_parquet(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_parquet(path)
    except Exception:
        return pd.DataFrame()


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def probability_band(probability: float) -> str:
    if pd.isna(probability):
        return 'unknown'
    for start, end in [(0.00, 0.35), (0.35, 0.45), (0.45, 0.50), (0.50, 0.55), (0.55, 1.00)]:
        if start <= float(probability) < end:
            return f'{start:.2f}-{end:.2f}'
    return 'unknown'


def attach_metadata(df: pd.DataFrame) -> pd.DataFrame:
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
        suffixes=('', '_log')
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


def existing_logged_ids() -> set:
    if not paper_log_path.exists() or paper_log_path.stat().st_size == 0:
        return set()
    try:
        existing = pd.read_json(paper_log_path, lines=True)
    except Exception:
        return set()
    if 'prediction_id' not in existing.columns:
        return set()
    return set(existing['prediction_id'].astype(str).tolist())


snapshots = attach_metadata(safe_read_parquet(snapshot_path))
rules = safe_read_csv(rules_path)

if len(snapshots) == 0:
    paper = pd.DataFrame(columns=expected_columns)
else:
    for col, default in {
        'ev': 0.0,
        'probability': 0.0,
        'market_odds': 0.0,
        'fair_odds': 0.0,
        'league': 'unknown',
        'season': 'unknown',
        'sample_phase': 'historical_proxy_research',
        'selection': 'unknown',
        'match_date': '',
        'match_time': '',
        'home_team': 'unknown',
        'away_team': 'unknown',
    }.items():
        if col not in snapshots.columns:
            snapshots[col] = default

    for col in ['ev', 'probability', 'market_odds', 'fair_odds']:
        snapshots[col] = pd.to_numeric(snapshots[col], errors='coerce')

    snapshots['market_implied_probability'] = 1 / snapshots['market_odds'].replace(0, pd.NA)
    snapshots['probability_edge'] = snapshots['probability'].fillna(0) - snapshots['market_implied_probability'].fillna(0)
    snapshots['model_market_ratio'] = snapshots['probability'].fillna(0) / snapshots['market_implied_probability'].replace(0, pd.NA)
    snapshots['alignment_penalty'] = (snapshots['model_market_ratio'].fillna(1) - 1).abs()
    snapshots['probability_band'] = snapshots['probability'].apply(probability_band)

    snapshots['calibration_risk'] = 'normal'
    snapshots.loc[snapshots['probability'].fillna(0) >= 0.50, 'calibration_risk'] = 'high_probability_band'
    snapshots.loc[snapshots['probability_edge'].fillna(0).abs() >= 0.16, 'calibration_risk'] = 'large_probability_edge'
    snapshots.loc[snapshots['alignment_penalty'].fillna(0) >= 0.45, 'calibration_risk'] = 'market_misalignment'

    snapshots['suppression_action'] = 'none'
    if len(rules):
        for _, rule in rules.iterrows():
            rule_type = str(rule.get('rule_type'))
            target = str(rule.get('target'))
            action = str(rule.get('action'))
            if rule_type == 'probability_band':
                mask = snapshots['probability_band'].astype(str) == target
            elif rule_type == 'league':
                mask = snapshots['league'].astype(str) == target
            else:
                continue
            if action == 'suppress':
                snapshots.loc[mask, 'suppression_action'] = 'suppress'
            elif action == 'downweight':
                snapshots.loc[mask & (snapshots['suppression_action'] != 'suppress'), 'suppression_action'] = 'downweight'
            elif action == 'monitor':
                snapshots.loc[mask & (snapshots['suppression_action'] == 'none'), 'suppression_action'] = 'monitor'

    paper = snapshots[
        (snapshots['suppression_action'] != 'suppress')
        & (snapshots['market_odds'].fillna(0).between(1.45, 7.50))
        & (snapshots['probability'].fillna(0).between(0.32, 0.57))
        & (snapshots['probability_edge'].fillna(0).between(0.000, 0.18))
        & (snapshots['ev'].fillna(0).between(0.00, 0.60))
        & (snapshots['alignment_penalty'].fillna(1).between(0.00, 0.48))
    ].copy()

    if len(paper):
        action_weight = paper['suppression_action'].map({'monitor': 0.92, 'downweight': 0.65}).fillna(1.0)
        risk_weight = paper['calibration_risk'].map({'market_misalignment': 0.70, 'large_probability_edge': 0.78, 'high_probability_band': 0.85}).fillna(1.0)
        paper['paper_test_score'] = (
            ((paper['ev'].fillna(0) * 0.28)
             + (paper['probability_edge'].fillna(0) * 0.26)
             + ((1 - paper['alignment_penalty'].fillna(1)) * 0.28)
             + (paper['probability'].fillna(0) * 0.10))
            * action_weight
            * risk_weight
        ).round(4)
        paper['paper_test_tier'] = 'observation'
        paper.loc[
            (paper['paper_test_score'] >= 0.18)
            & (paper['alignment_penalty'] <= 0.30),
            'paper_test_tier'
        ] = 'priority_observation'
        paper['paper_test_reason'] = 'loose_paper_tracking_not_real_money'
        paper = paper.sort_values(['paper_test_tier', 'paper_test_score'], ascending=[False, False]).head(7)
    else:
        paper = pd.DataFrame(columns=expected_columns)

for col in expected_columns:
    if col not in paper.columns:
        paper[col] = None
paper = paper[expected_columns]

paper.to_parquet(output_dir / 'paper_test_picks.parquet', index=False)
paper.to_csv(output_dir / 'paper_test_picks.csv', index=False)

logged_ids = existing_logged_ids()
new_rows = paper[~paper['prediction_id'].astype(str).isin(logged_ids)].copy() if len(paper) else pd.DataFrame(columns=expected_columns)

if len(new_rows):
    with paper_log_path.open('a', encoding='utf-8') as handle:
        for record in new_rows.to_dict(orient='records'):
            handle.write(json.dumps(record, ensure_ascii=False, default=str) + '\n')

if paper_log_path.exists() and paper_log_path.stat().st_size > 0:
    try:
        paper_log = pd.read_json(paper_log_path, lines=True)
    except Exception:
        paper_log = pd.DataFrame(columns=expected_columns)
else:
    paper_log = pd.DataFrame(columns=expected_columns)

paper_log.to_csv(output_dir / 'paper_test_log_latest.csv', index=False)

markdown = [
    '# Paper Test Picks',
    '',
    'Observation-only picks. These are not real-money recommendations.',
    'Purpose: collect forward-test CLV and settlement evidence quickly without weakening real-money guardrails.',
    '',
    f'Current paper-test picks: {len(paper)}',
    f'Newly logged paper-test picks: {len(new_rows)}',
    f'Total logged paper-test picks: {len(paper_log)}',
    '',
]

if len(paper) == 0:
    markdown.append('No paper-test picks passed the loose observation filter.')
else:
    for _, row in paper.iterrows():
        markdown.append(
            f"- {row['home_team']} vs {row['away_team']} | selection={str(row['selection']).upper()} | "
            f"odds={round(float(row['market_odds']),2)} | prob={round(float(row['probability']),4)} | "
            f"EV={round(float(row['ev']),4)} | edge={round(float(row['probability_edge']),4)} | "
            f"penalty={round(float(row['alignment_penalty']),4)} | band={row['probability_band']} | "
            f"rule={row['suppression_action']} | tier={row['paper_test_tier']}"
        )

(output_dir / 'paper_test_picks.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(paper)} paper-test picks')
print(f'Logged {len(new_rows)} new paper-test picks')
print(f'Total logged paper-test picks: {len(paper_log)}')
print(paper.head())
