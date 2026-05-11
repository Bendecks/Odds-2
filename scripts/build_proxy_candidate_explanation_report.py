from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
proxy_path = output_dir / 'proxy_candidate_observations.csv'
summary_path = output_dir / 'proxy_candidate_observation_summary.csv'
rules_path = output_dir / 'signal_suppression_rules.csv'


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


proxy = safe_read_csv(proxy_path)
summary = safe_read_csv(summary_path)
rules = safe_read_csv(rules_path)

for col in ['market_odds', 'probability', 'probability_edge', 'ev', 'alignment_penalty', 'proxy_candidate_score']:
    if col in proxy.columns:
        proxy[col] = pd.to_numeric(proxy[col], errors='coerce')

explanations = []

if len(proxy):
    for _, row in proxy.iterrows():
        reasons = []
        if str(row.get('suppression_action', '')).startswith('proxy_suppressed'):
            reasons.append('probability_or_league_rule_suppressed')
        if pd.notna(row.get('probability')) and row.get('probability') < 0.35:
            reasons.append('low_probability_band_under_0_35')
        if pd.notna(row.get('probability_edge')) and row.get('probability_edge') < 0.02:
            reasons.append('edge_below_candidate_threshold')
        if pd.notna(row.get('ev')) and row.get('ev') > 0.18:
            reasons.append('ev_above_real_candidate_cap_possible_overconfidence')
        if pd.notna(row.get('alignment_penalty')) and row.get('alignment_penalty') > 0.15:
            reasons.append('market_alignment_penalty_too_high_for_real_candidate')
        if 'odds_api_io' not in str(row.get('source_name', '')):
            reasons.append('delayed_football_data_proxy_not_fresh_api_price')
        if not reasons:
            reasons.append('watchlist_only_pending_forward_settlement')

        improvements = []
        if 'low_probability_band_under_0_35' in reasons:
            improvements.append('collect settled forward results before trusting low-probability selections')
        if 'edge_below_candidate_threshold' in reasons:
            improvements.append('needs stronger model-vs-market edge')
        if 'ev_above_real_candidate_cap_possible_overconfidence' in reasons:
            improvements.append('calibration should reduce overconfident EV spikes')
        if 'market_alignment_penalty_too_high_for_real_candidate' in reasons:
            improvements.append('needs better market alignment or stricter probability calibration')
        if 'delayed_football_data_proxy_not_fresh_api_price' in reasons:
            improvements.append('prefer odds-api.io/API-Football fresh price where available')
        if not improvements:
            improvements.append('monitor until settled forward sample is large enough')

        explanations.append({
            'match_date': row.get('match_date'),
            'home_team': row.get('home_team'),
            'away_team': row.get('away_team'),
            'selection': row.get('selection'),
            'source_name': row.get('source_name'),
            'market_odds': row.get('market_odds'),
            'probability': row.get('probability'),
            'probability_edge': row.get('probability_edge'),
            'ev': row.get('ev'),
            'alignment_penalty': row.get('alignment_penalty'),
            'proxy_candidate_tier': row.get('proxy_candidate_tier'),
            'proxy_candidate_score': row.get('proxy_candidate_score'),
            'primary_blockers': '; '.join(reasons),
            'improvement_needed': '; '.join(improvements),
            'real_money_ready': False,
        })

explanation_df = pd.DataFrame(explanations)
expected_columns = [
    'match_date', 'home_team', 'away_team', 'selection', 'source_name',
    'market_odds', 'probability', 'probability_edge', 'ev', 'alignment_penalty',
    'proxy_candidate_tier', 'proxy_candidate_score', 'primary_blockers',
    'improvement_needed', 'real_money_ready'
]
for col in expected_columns:
    if col not in explanation_df.columns:
        explanation_df[col] = None
explanation_df = explanation_df[expected_columns]
explanation_df.to_csv(output_dir / 'proxy_candidate_explanation_report.csv', index=False)

blocker_rows = []
if len(explanation_df):
    for blockers in explanation_df['primary_blockers'].fillna(''):
        for blocker in [item.strip() for item in blockers.split(';') if item.strip()]:
            blocker_rows.append({'blocker': blocker})
blocker_summary = pd.DataFrame(blocker_rows)
if len(blocker_summary):
    blocker_summary = blocker_summary.value_counts(['blocker']).reset_index(name='rows').sort_values('rows', ascending=False)
else:
    blocker_summary = pd.DataFrame(columns=['blocker', 'rows'])
blocker_summary.to_csv(output_dir / 'proxy_candidate_blocker_summary.csv', index=False)

summary_values = {
    'proxy_candidate_rows': int(len(proxy)),
    'explained_rows': int(len(explanation_df)),
    'distinct_blockers': int(len(blocker_summary)),
    'top_blocker': blocker_summary.iloc[0]['blocker'] if len(blocker_summary) else None,
    'real_money_ready': False,
}
pd.DataFrame([summary_values]).to_csv(output_dir / 'proxy_candidate_explanation_summary.csv', index=False)

markdown = [
    '# Proxy Candidate Explanation Report',
    '',
    'Explains why proxy candidate observations are not promoted to real candidate bets.',
    'This report is paper/proxy-only and never real-money ready.',
    '',
    f"Proxy candidate rows: {summary_values['proxy_candidate_rows']}",
    f"Explained rows: {summary_values['explained_rows']}",
    f"Distinct blockers: {summary_values['distinct_blockers']}",
    f"Top blocker: {summary_values['top_blocker']}",
    f"Real-money ready: {summary_values['real_money_ready']}",
    '',
    '## Blocker summary',
    '',
]

if len(blocker_summary):
    for _, row in blocker_summary.iterrows():
        markdown.append(f"- {row['blocker']}: {int(row['rows'])}")
else:
    markdown.append('No blockers available because there are no proxy candidate rows.')

markdown.extend(['', '## Row explanations', ''])
if len(explanation_df):
    for _, row in explanation_df.head(30).iterrows():
        markdown.append(
            f"- {row['match_date']} | {row['home_team']} vs {row['away_team']} | "
            f"sel={str(row['selection']).upper()} | score={row['proxy_candidate_score']} | "
            f"blockers={row['primary_blockers']} | improve={row['improvement_needed']}"
        )
else:
    markdown.append('No proxy candidate observations to explain.')

(output_dir / 'proxy_candidate_explanation_report.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary_values)
