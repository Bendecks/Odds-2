import json
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
log_dir = Path('data/predictions')
log_dir.mkdir(parents=True, exist_ok=True)

auto_value_path = output_dir / 'automatic_forward_value_snapshots.parquet'
manual_forward_path = output_dir / 'manual_forward_snapshots.parquet'
snapshot_path = output_dir / 'prediction_snapshots_latest.parquet'
rules_path = output_dir / 'signal_suppression_rules.csv'
paper_log_path = log_dir / 'paper_test_log.jsonl'

expected_columns = [
    'snapshot_id', 'prediction_id', 'event_id', 'created_at_utc',
    'match_date', 'match_time', 'home_team', 'away_team',
    'league', 'season', 'sample_phase', 'model_source', 'model_coverage', 'selection',
    'market_odds', 'fair_odds', 'probability', 'probability_band',
    'market_implied_probability', 'probability_edge', 'model_market_ratio',
    'ev', 'alignment_penalty', 'calibration_risk', 'suppression_action',
    'paper_test_tier', 'paper_test_score', 'paper_test_reason',
]

FORWARD_PHASES = {'paper_forward_test', 'live_forward_snapshot', 'upcoming_fixture', 'automatic_forward_price_proxy'}


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


def existing_logged_ids() -> set:
    if not paper_log_path.exists() or paper_log_path.stat().st_size == 0:
        return set()
    try:
        existing = pd.read_json(paper_log_path, lines=True)
    except Exception:
        return set()
    if 'snapshot_id' in existing.columns:
        return set(existing['snapshot_id'].astype(str).tolist())
    if 'prediction_id' in existing.columns:
        return set(existing['prediction_id'].astype(str).tolist())
    return set()


def empty_paper() -> pd.DataFrame:
    return pd.DataFrame(columns=expected_columns)


auto_value = safe_read_parquet(auto_value_path)
manual_forward = safe_read_parquet(manual_forward_path)
historical_snapshots = safe_read_parquet(snapshot_path)
rules = safe_read_csv(rules_path)
reason = ''
source_used = 'automatic_forward_value_snapshots'

if len(auto_value):
    snapshots = auto_value.copy()
elif len(manual_forward):
    snapshots = manual_forward.copy()
    source_used = 'manual_forward_snapshots_optional_fallback'
else:
    snapshots = historical_snapshots.copy()
    source_used = 'prediction_snapshots_latest_forward_only'

if len(snapshots) == 0:
    paper = empty_paper()
    reason = 'No snapshot rows available. Automatic proxy prices or optional manual fallback are needed.'
else:
    for col, default in {
        'ev': 0.0,
        'probability': 0.0,
        'market_odds': 0.0,
        'fair_odds': 0.0,
        'league': 'unknown',
        'season': 'unknown',
        'sample_phase': 'historical_proxy_research',
        'model_source': 'unknown',
        'model_coverage': 'unknown',
        'selection': 'unknown',
        'match_date': '',
        'match_time': '',
        'home_team': 'unknown',
        'away_team': 'unknown',
        'source_quality': 'unknown',
    }.items():
        if col not in snapshots.columns:
            snapshots[col] = default

    snapshots['sample_phase'] = snapshots['sample_phase'].fillna('unknown').astype(str)
    snapshots['model_coverage'] = snapshots['model_coverage'].fillna('unknown').astype(str)
    forward_snapshots = snapshots[snapshots['sample_phase'].isin(FORWARD_PHASES)].copy()

    if len(forward_snapshots) == 0:
        paper = empty_paper()
        reason = 'No forward-eligible rows. Historical proxy rows are excluded from paper-test picks.'
    else:
        for col in ['ev', 'probability', 'market_odds', 'fair_odds']:
            forward_snapshots[col] = pd.to_numeric(forward_snapshots[col], errors='coerce')

        if 'market_implied_probability' not in forward_snapshots.columns:
            forward_snapshots['market_implied_probability'] = 1 / forward_snapshots['market_odds'].replace(0, pd.NA)
        else:
            forward_snapshots['market_implied_probability'] = pd.to_numeric(forward_snapshots['market_implied_probability'], errors='coerce')
        if 'probability_edge' not in forward_snapshots.columns:
            forward_snapshots['probability_edge'] = forward_snapshots['probability'].fillna(0) - forward_snapshots['market_implied_probability'].fillna(0)
        else:
            forward_snapshots['probability_edge'] = pd.to_numeric(forward_snapshots['probability_edge'], errors='coerce')
        forward_snapshots['model_market_ratio'] = forward_snapshots['probability'].fillna(0) / forward_snapshots['market_implied_probability'].replace(0, pd.NA)
        forward_snapshots['alignment_penalty'] = (forward_snapshots['model_market_ratio'].fillna(1) - 1).abs()
        forward_snapshots['probability_band'] = forward_snapshots['probability'].apply(probability_band)

        forward_snapshots['calibration_risk'] = 'normal'
        forward_snapshots.loc[forward_snapshots['sample_phase'] == 'automatic_forward_price_proxy', 'calibration_risk'] = 'proxy_price_source'
        forward_snapshots.loc[forward_snapshots['model_coverage'] == 'baseline_unmatched_fixture', 'calibration_risk'] = 'baseline_coverage_only'
        forward_snapshots.loc[forward_snapshots['probability'].fillna(0) >= 0.50, 'calibration_risk'] = 'high_probability_band'
        forward_snapshots.loc[forward_snapshots['probability_edge'].fillna(0).abs() >= 0.16, 'calibration_risk'] = 'large_probability_edge'
        forward_snapshots.loc[forward_snapshots['alignment_penalty'].fillna(0) >= 0.45, 'calibration_risk'] = 'market_misalignment'
        forward_snapshots.loc[forward_snapshots['model_coverage'] == 'baseline_unmatched_fixture', 'calibration_risk'] = 'baseline_coverage_only'

        forward_snapshots['suppression_action'] = 'none'
        if len(rules):
            for _, rule in rules.iterrows():
                rule_type = str(rule.get('rule_type'))
                target = str(rule.get('target'))
                action = str(rule.get('action'))
                if rule_type == 'probability_band':
                    mask = forward_snapshots['probability_band'].astype(str) == target
                elif rule_type == 'league':
                    mask = forward_snapshots['league'].astype(str) == target
                else:
                    continue
                if action == 'suppress':
                    forward_snapshots.loc[mask, 'suppression_action'] = 'suppress'
                elif action == 'downweight':
                    forward_snapshots.loc[mask & (forward_snapshots['suppression_action'] != 'suppress'), 'suppression_action'] = 'downweight'
                elif action == 'monitor':
                    forward_snapshots.loc[mask & (forward_snapshots['suppression_action'] == 'none'), 'suppression_action'] = 'monitor'

        is_proxy = forward_snapshots['sample_phase'] == 'automatic_forward_price_proxy'
        is_baseline = forward_snapshots['model_coverage'] == 'baseline_unmatched_fixture'
        forward_snapshots.loc[is_proxy & (forward_snapshots['suppression_action'] == 'suppress'), 'suppression_action'] = 'proxy_suppressed_band_observe_only'
        forward_snapshots.loc[is_baseline & (forward_snapshots['suppression_action'] != 'proxy_suppressed_band_observe_only'), 'suppression_action'] = 'baseline_coverage_observe_only'

        paper = forward_snapshots[
            (forward_snapshots['suppression_action'] != 'suppress')
            & (forward_snapshots['market_odds'].fillna(0).between(1.45, 7.50))
            & (forward_snapshots['probability'].fillna(0).between(0.25, 0.58))
            & (forward_snapshots['probability_edge'].fillna(0).between(0.000, 0.22))
            & (forward_snapshots['ev'].fillna(0).between(0.00, 0.70))
            & (forward_snapshots['alignment_penalty'].fillna(1).between(0.00, 0.56))
        ].copy()

        if len(paper):
            action_weight = paper['suppression_action'].map({'monitor': 0.92, 'downweight': 0.65, 'proxy_suppressed_band_observe_only': 0.48, 'baseline_coverage_observe_only': 0.36}).fillna(1.0)
            risk_weight = paper['calibration_risk'].map({'market_misalignment': 0.70, 'large_probability_edge': 0.78, 'high_probability_band': 0.85, 'proxy_price_source': 0.82, 'baseline_coverage_only': 0.45}).fillna(1.0)
            paper['paper_test_score'] = (
                ((paper['ev'].fillna(0) * 0.28)
                 + (paper['probability_edge'].fillna(0) * 0.26)
                 + ((1 - paper['alignment_penalty'].fillna(1)) * 0.28)
                 + (paper['probability'].fillna(0) * 0.10))
                * action_weight
                * risk_weight
            ).round(4)
            paper['paper_test_tier'] = 'proxy_observation'
            paper.loc[(paper['suppression_action'] == 'proxy_suppressed_band_observe_only'), 'paper_test_tier'] = 'suppressed_band_proxy_observation'
            paper.loc[(paper['suppression_action'] == 'baseline_coverage_observe_only'), 'paper_test_tier'] = 'baseline_coverage_observation'
            paper.loc[(paper['paper_test_score'] >= 0.18) & (paper['alignment_penalty'] <= 0.34) & (paper['suppression_action'] != 'proxy_suppressed_band_observe_only') & (paper['suppression_action'] != 'baseline_coverage_observe_only'), 'paper_test_tier'] = 'priority_proxy_observation'
            paper['paper_test_reason'] = 'automatic_forward_proxy_observation_not_real_money'
            paper.loc[paper['suppression_action'] == 'proxy_suppressed_band_observe_only', 'paper_test_reason'] = 'suppressed_band_proxy_observation_not_real_money'
            paper.loc[paper['suppression_action'] == 'baseline_coverage_observe_only', 'paper_test_reason'] = 'baseline_coverage_observation_not_model_signal_not_real_money'
            paper = paper.sort_values(['paper_test_score'], ascending=False).head(7)
        else:
            paper = empty_paper()
            reason = 'Forward proxy rows exist, but none passed paper-test observation filters.'

for col in expected_columns:
    if col not in paper.columns:
        paper[col] = None
paper = paper[expected_columns]

paper.to_parquet(output_dir / 'paper_test_picks.parquet', index=False)
paper.to_csv(output_dir / 'paper_test_picks.csv', index=False)

logged_ids = existing_logged_ids()
id_col = 'snapshot_id' if 'snapshot_id' in paper.columns else 'prediction_id'
new_rows = paper[~paper[id_col].astype(str).isin(logged_ids)].copy() if len(paper) else empty_paper()

if len(new_rows):
    with paper_log_path.open('a', encoding='utf-8') as handle:
        for record in new_rows.to_dict(orient='records'):
            handle.write(json.dumps(record, ensure_ascii=False, default=str) + '\n')

if paper_log_path.exists() and paper_log_path.stat().st_size > 0:
    try:
        paper_log = pd.read_json(paper_log_path, lines=True)
    except Exception:
        paper_log = empty_paper()
else:
    paper_log = empty_paper()

paper_log.to_csv(output_dir / 'paper_test_log_latest.csv', index=False)

markdown = [
    '# Paper Test Picks',
    '',
    'Observation-only picks. These are not real-money recommendations.',
    'Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.',
    'Baseline coverage observations are not model signals. They exist only to test the pipeline and collect settlement evidence.',
    'Suppressed historical bands may be tracked only as proxy observation and remain excluded from real-money readiness.',
    '',
    f'Source used: {source_used}',
    f'Current paper-test picks: {len(paper)}',
    f'Newly logged paper-test picks: {len(new_rows)}',
    f'Total logged paper-test rows: {len(paper_log)}',
    '',
]

if len(paper) == 0:
    markdown.append(reason or 'No paper-test picks passed the forward observation filter.')
else:
    for _, row in paper.iterrows():
        markdown.append(
            f"- {row['home_team']} vs {row['away_team']} | coverage={row['model_coverage']} | selection={str(row['selection']).upper()} | "
            f"odds={round(float(row['market_odds']),2)} | prob={round(float(row['probability']),4)} | "
            f"EV={round(float(row['ev']),4)} | edge={round(float(row['probability_edge']),4)} | "
            f"penalty={round(float(row['alignment_penalty']),4)} | band={row['probability_band']} | "
            f"risk={row['calibration_risk']} | rule={row['suppression_action']} | tier={row['paper_test_tier']}"
        )

(output_dir / 'paper_test_picks.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated {len(paper)} forward-eligible paper-test picks')
print(f'Logged {len(new_rows)} new paper-test picks')
print(f'Total logged paper-test rows: {len(paper_log)}')
print(reason)
print(paper.head())
