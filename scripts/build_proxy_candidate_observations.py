from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
value_path = output_dir / 'automatic_forward_value_snapshots.parquet'
rules_path = output_dir / 'signal_suppression_rules.csv'

expected_columns = [
    'snapshot_id', 'prediction_id', 'fixture_id', 'match_date', 'match_time',
    'home_team', 'away_team', 'league', 'sample_phase', 'source_name', 'source_type',
    'source_quality', 'selection', 'market_odds', 'fair_odds', 'probability',
    'probability_band', 'market_implied_probability', 'probability_edge', 'ev',
    'model_market_ratio', 'alignment_penalty', 'calibration_risk', 'suppression_action',
    'proxy_candidate_tier', 'proxy_candidate_score', 'proxy_candidate_reason',
    'real_money_ready'
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


def norm_team(value) -> str:
    text = str(value or '').lower().strip()
    for token in ['hotspur', 'united', 'utd', 'fc', 'afc', 'cf', '.', ',', '&']:
        text = text.replace(token, ' ')
    return ' '.join(text.split())


value = safe_read_parquet(value_path)
rules = safe_read_csv(rules_path)
pre_dedupe_rows = 0
reason = ''

if len(value) == 0:
    proxy = pd.DataFrame(columns=expected_columns)
    reason = 'No automatic forward value snapshots available.'
else:
    df = value.copy()
    for col, default in {
        'ev': 0.0,
        'probability': 0.0,
        'market_odds': 0.0,
        'fair_odds': 0.0,
        'market_implied_probability': 0.0,
        'probability_edge': 0.0,
        'league': 'unknown',
        'sample_phase': 'unknown',
        'source_name': 'unknown',
        'source_type': 'unknown',
        'source_quality': 'unknown',
        'selection': 'unknown',
    }.items():
        if col not in df.columns:
            df[col] = default

    for col in ['ev', 'probability', 'market_odds', 'fair_odds', 'market_implied_probability', 'probability_edge']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['sample_phase'] = df['sample_phase'].fillna('unknown').astype(str)
    df = df[df['sample_phase'] == 'automatic_forward_price_proxy'].copy()
    if len(df) == 0:
        proxy = pd.DataFrame(columns=expected_columns)
        reason = 'No automatic_forward_price_proxy rows available.'
    else:
        if 'model_market_ratio' not in df.columns:
            df['model_market_ratio'] = df['probability'].fillna(0) / df['market_implied_probability'].replace(0, pd.NA)
        else:
            df['model_market_ratio'] = pd.to_numeric(df['model_market_ratio'], errors='coerce')
        if 'alignment_penalty' not in df.columns:
            df['alignment_penalty'] = (df['model_market_ratio'].fillna(1) - 1).abs()
        else:
            df['alignment_penalty'] = pd.to_numeric(df['alignment_penalty'], errors='coerce')
        df['probability_band'] = df['probability'].apply(probability_band)

        df['calibration_risk'] = 'normal'
        df.loc[df['source_type'].astype(str).str.contains('proxy', case=False, na=False), 'calibration_risk'] = 'proxy_price_source'
        df.loc[df['probability'].fillna(0) >= 0.50, 'calibration_risk'] = 'high_probability_band'
        df.loc[df['probability_edge'].fillna(0).abs() >= 0.16, 'calibration_risk'] = 'large_probability_edge'
        df.loc[df['alignment_penalty'].fillna(0) >= 0.45, 'calibration_risk'] = 'market_misalignment'

        df['suppression_action'] = 'none'
        if len(rules):
            for _, rule in rules.iterrows():
                rule_type = str(rule.get('rule_type'))
                target = str(rule.get('target'))
                action = str(rule.get('action'))
                if rule_type == 'probability_band':
                    mask = df['probability_band'].astype(str) == target
                elif rule_type == 'league':
                    mask = df['league'].astype(str) == target
                else:
                    continue
                if action == 'suppress':
                    df.loc[mask, 'suppression_action'] = 'proxy_suppressed_band_observe_only'
                elif action == 'downweight':
                    df.loc[mask & (df['suppression_action'] == 'none'), 'suppression_action'] = 'proxy_downweight_observe_only'
                elif action == 'monitor':
                    df.loc[mask & (df['suppression_action'] == 'none'), 'suppression_action'] = 'proxy_monitor_observe_only'

        base_filter = (
            df['market_odds'].fillna(0).between(1.35, 8.00)
            & df['probability'].fillna(0).between(0.22, 0.62)
            & df['probability_edge'].fillna(0).between(0.000, 0.25)
            & df['ev'].fillna(0).between(0.000, 0.80)
            & df['alignment_penalty'].fillna(1).between(0.00, 0.65)
        )
        proxy = df[base_filter].copy()
        pre_dedupe_rows = int(len(proxy))

        if len(proxy):
            action_weight = proxy['suppression_action'].map({
                'none': 1.0,
                'proxy_monitor_observe_only': 0.88,
                'proxy_downweight_observe_only': 0.68,
                'proxy_suppressed_band_observe_only': 0.42,
            }).fillna(0.75)
            source_weight = proxy['source_name'].astype(str).map(lambda x: 1.05 if 'odds_api_io' in x else 0.90)
            risk_weight = proxy['calibration_risk'].map({
                'normal': 1.0,
                'proxy_price_source': 0.86,
                'high_probability_band': 0.82,
                'large_probability_edge': 0.76,
                'market_misalignment': 0.68,
            }).fillna(0.80)
            proxy['proxy_candidate_score'] = (
                ((proxy['ev'].fillna(0) * 0.30)
                 + (proxy['probability_edge'].fillna(0) * 0.26)
                 + ((1 - proxy['alignment_penalty'].fillna(1)) * 0.24)
                 + (proxy['probability'].fillna(0) * 0.10))
                * action_weight
                * source_weight
                * risk_weight
            ).round(4)
            proxy['proxy_candidate_tier'] = 'proxy_watchlist'
            proxy.loc[(proxy['proxy_candidate_score'] >= 0.18) & (proxy['alignment_penalty'] <= 0.35) & (proxy['suppression_action'] == 'none'), 'proxy_candidate_tier'] = 'proxy_candidate_like'
            proxy.loc[proxy['suppression_action'].astype(str).str.contains('suppressed', na=False), 'proxy_candidate_tier'] = 'suppressed_proxy_watchlist'
            proxy['proxy_candidate_reason'] = 'proxy_candidate_observation_not_real_money'
            proxy['real_money_ready'] = False
            proxy['dedupe_home'] = proxy['home_team'].apply(norm_team)
            proxy['dedupe_away'] = proxy['away_team'].apply(norm_team)
            proxy['dedupe_selection'] = proxy['selection'].astype(str).str.lower().str.strip()
            proxy = proxy.sort_values(['proxy_candidate_score', 'ev', 'market_odds'], ascending=False)
            proxy = proxy.drop_duplicates(['match_date', 'dedupe_home', 'dedupe_away', 'dedupe_selection'], keep='first')
            proxy = proxy.drop(columns=['dedupe_home', 'dedupe_away', 'dedupe_selection'], errors='ignore')
            proxy = proxy.sort_values(['proxy_candidate_score'], ascending=False).head(12)
            reason = ''
        else:
            proxy = pd.DataFrame(columns=expected_columns)
            reason = 'Automatic proxy value rows exist, but none passed proxy-candidate observation filters.'

for col in expected_columns:
    if col not in proxy.columns:
        proxy[col] = None
proxy = proxy[expected_columns]
proxy.to_csv(output_dir / 'proxy_candidate_observations.csv', index=False)
proxy.to_parquet(output_dir / 'proxy_candidate_observations.parquet', index=False)

summary = {
    'automatic_value_rows': int(len(value)),
    'pre_dedupe_proxy_candidate_observation_rows': pre_dedupe_rows,
    'proxy_candidate_observation_rows': int(len(proxy)),
    'proxy_candidate_like_rows': int((proxy['proxy_candidate_tier'] == 'proxy_candidate_like').sum()) if len(proxy) else 0,
    'suppressed_proxy_watchlist_rows': int((proxy['proxy_candidate_tier'] == 'suppressed_proxy_watchlist').sum()) if len(proxy) else 0,
    'dedupe_strategy': 'match_date_normalized_teams_selection_keep_best_score',
    'real_money_ready': False,
}
pd.DataFrame([summary]).to_csv(output_dir / 'proxy_candidate_observation_summary.csv', index=False)

markdown = [
    '# Proxy Candidate Observations',
    '',
    'Intermediate layer between paper-test picks and real candidate bets.',
    'These rows are proxy/paper observations only and must not be treated as real-money candidates.',
    'Deduplicated by match date, normalized teams, and selection; best proxy score is kept.',
    '',
    f"Automatic value rows: {summary['automatic_value_rows']}",
    f"Pre-dedupe proxy candidate observation rows: {summary['pre_dedupe_proxy_candidate_observation_rows']}",
    f"Proxy candidate observation rows: {summary['proxy_candidate_observation_rows']}",
    f"Proxy candidate-like rows: {summary['proxy_candidate_like_rows']}",
    f"Suppressed proxy watchlist rows: {summary['suppressed_proxy_watchlist_rows']}",
    f"Dedupe strategy: {summary['dedupe_strategy']}",
    f"Real-money ready: {summary['real_money_ready']}",
    '',
]

if len(proxy):
    for _, row in proxy.iterrows():
        markdown.append(
            f"- {row['match_date']} | {row['home_team']} vs {row['away_team']} | "
            f"selection={str(row['selection']).upper()} | source={row['source_name']} | odds={row['market_odds']} | "
            f"prob={row['probability']} | EV={row['ev']} | edge={row['probability_edge']} | "
            f"penalty={row['alignment_penalty']} | tier={row['proxy_candidate_tier']} | score={row['proxy_candidate_score']}"
        )
else:
    markdown.append(reason or 'No proxy candidate observations available.')

(output_dir / 'proxy_candidate_observations.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
