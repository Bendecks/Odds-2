from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

diag_path = output_dir / 'odds_api_io_event_selection_diagnostics.csv'
status_path = output_dir / 'odds_api_io_forward_price_status.csv'
quality_path = output_dir / 'odds_api_io_price_quality_summary.csv'
summary_path = output_dir / 'odds_api_io_discovery_efficiency_summary.csv'
report_path = output_dir / 'odds_api_io_discovery_efficiency_report.md'


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def boolish(value):
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {'true', '1', 'yes'}


diag = safe_read_csv(diag_path)
status = safe_read_csv(status_path)
quality = safe_read_csv(quality_path)

if len(diag):
    diag = diag.copy()
    diag['selected_bool'] = diag.get('selected', False).map(boolish)
    diag['event_match_confidence_num'] = pd.to_numeric(diag.get('event_match_confidence'), errors='coerce')
else:
    diag = pd.DataFrame(columns=['discovery_source', 'query', 'target_home_team', 'target_away_team', 'candidate_home_team', 'candidate_away_team', 'candidate_match_date', 'event_match_confidence_num', 'selected_bool'])

status_row = status.iloc[0].to_dict() if len(status) else {}
quality_row = quality.iloc[0].to_dict() if len(quality) else {}

by_source = []
if len(diag):
    for source, group in diag.groupby('discovery_source', dropna=False):
        by_source.append({
            'discovery_source': source,
            'candidate_rows': int(len(group)),
            'selected_rows': int(group['selected_bool'].sum()),
            'best_confidence': float(group['event_match_confidence_num'].max()) if group['event_match_confidence_num'].notna().any() else None,
            'avg_confidence': float(group['event_match_confidence_num'].mean()) if group['event_match_confidence_num'].notna().any() else None,
        })
source_df = pd.DataFrame(by_source)
source_df.to_csv(output_dir / 'odds_api_io_discovery_efficiency_by_source.csv', index=False)

top_candidates = diag.sort_values('event_match_confidence_num', ascending=False).head(25) if len(diag) else pd.DataFrame()
top_candidates.to_csv(output_dir / 'odds_api_io_top_event_match_candidates.csv', index=False)

summary = {
    'candidate_rows': int(len(diag)),
    'selected_rows': int(diag['selected_bool'].sum()) if len(diag) else 0,
    'calls_used': status_row.get('calls_used'),
    'max_calls': status_row.get('max_calls'),
    'max_discovery_calls': status_row.get('max_discovery_calls'),
    'events_discovery_rows': status_row.get('events_discovery_rows'),
    'search_fallback_used': status_row.get('search_fallback_used'),
    'search_queries_used': status_row.get('search_queries_used'),
    'multi_odds_attempted': status_row.get('multi_odds_attempted'),
    'raw_price_rows_before_quality_filter': quality_row.get('input_price_rows'),
    'accepted_price_rows_after_quality_filter': quality_row.get('accepted_price_rows'),
    'rejected_price_rows_after_quality_filter': quality_row.get('rejected_price_rows'),
    'latest_rate_limit_remaining': status_row.get('latest_rate_limit_remaining'),
    'recommendation': 'Prefer bookmaker-filtered events scan; disable broad search fallback when rate-limit remaining is low or when it mostly produces unrelated events.',
}
pd.DataFrame([summary]).to_csv(summary_path, index=False)

markdown = [
    '# Odds-API.io Discovery Efficiency',
    '',
    'Purpose: show whether API calls are producing usable direct event matches or mostly noisy fallback candidates.',
    '',
    f"Candidate rows: {summary['candidate_rows']}",
    f"Selected rows before price quality filter: {summary['selected_rows']}",
    f"Calls used: {summary['calls_used']} / {summary['max_calls']}",
    f"Max discovery calls: {summary['max_discovery_calls']}",
    f"Events discovery rows: {summary['events_discovery_rows']}",
    f"Search fallback used: {summary['search_fallback_used']}",
    f"Search queries used: {summary['search_queries_used']}",
    f"Multi-odds attempted: {summary['multi_odds_attempted']}",
    f"Raw price rows before quality filter: {summary['raw_price_rows_before_quality_filter']}",
    f"Accepted price rows after quality filter: {summary['accepted_price_rows_after_quality_filter']}",
    f"Rejected price rows after quality filter: {summary['rejected_price_rows_after_quality_filter']}",
    f"Latest rate-limit remaining: {summary['latest_rate_limit_remaining']}",
    '',
    '## By discovery source',
    '',
]
if len(source_df):
    for _, row in source_df.iterrows():
        markdown.append(
            f"- {row['discovery_source']}: candidates={row['candidate_rows']}, selected={row['selected_rows']}, "
            f"best_confidence={row['best_confidence']}, avg_confidence={row['avg_confidence']}"
        )
else:
    markdown.append('- No event-selection diagnostics available.')

markdown.extend(['', '## Top candidates', ''])
if len(top_candidates):
    for _, row in top_candidates.iterrows():
        markdown.append(
            f"- src={row.get('discovery_source')} | query={row.get('query')} | target={row.get('target_home_team')} vs {row.get('target_away_team')} | "
            f"candidate={row.get('candidate_home_team')} vs {row.get('candidate_away_team')} | date={row.get('candidate_match_date')} | "
            f"confidence={row.get('event_match_confidence_num')} | selected={row.get('selected_bool')}"
        )
else:
    markdown.append('- No candidates.')

report_path.write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
