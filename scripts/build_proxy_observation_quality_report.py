from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
paper_path = output_dir / 'paper_test_picks.csv'
value_path = output_dir / 'automatic_forward_value_snapshots.csv'


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


paper = safe_read_csv(paper_path)
value = safe_read_csv(value_path)

for frame in [paper, value]:
    for col in ['ev', 'probability', 'market_odds', 'probability_edge', 'alignment_penalty']:
        if col in frame.columns:
            frame[col] = pd.to_numeric(frame[col], errors='coerce')

summary = {
    'value_snapshot_rows': int(len(value)),
    'paper_proxy_observation_rows': int(len(paper)),
    'positive_ev_value_rows': int((value.get('ev', pd.Series(dtype=float)) > 0).sum()) if len(value) else 0,
    'suppressed_band_observation_rows': int((paper.get('suppression_action', pd.Series(dtype=str)).astype(str) == 'proxy_suppressed_band_observe_only').sum()) if len(paper) else 0,
    'distinct_matches': int(paper[['home_team', 'away_team']].drop_duplicates().shape[0]) if len(paper) and {'home_team', 'away_team'}.issubset(paper.columns) else 0,
    'distinct_sources': int(paper['source_name'].nunique()) if len(paper) and 'source_name' in paper.columns else 0,
    'real_money_ready': False,
}

if len(paper):
    summary.update({
        'max_ev': round(float(paper['ev'].max()), 6) if 'ev' in paper.columns else None,
        'avg_ev': round(float(paper['ev'].mean()), 6) if 'ev' in paper.columns else None,
        'max_probability_edge': round(float(paper['probability_edge'].max()), 6) if 'probability_edge' in paper.columns else None,
        'avg_match_confidence': round(float(paper['match_confidence'].mean()), 6) if 'match_confidence' in paper.columns else None,
    })
else:
    summary.update({'max_ev': None, 'avg_ev': None, 'max_probability_edge': None, 'avg_match_confidence': None})

pd.DataFrame([summary]).to_csv(output_dir / 'proxy_observation_quality_report.csv', index=False)

by_selection = pd.DataFrame()
if len(paper) and 'selection' in paper.columns:
    by_selection = paper.groupby('selection').agg(
        rows=('selection', 'size'),
        avg_ev=('ev', 'mean'),
        max_ev=('ev', 'max'),
        avg_probability=('probability', 'mean'),
        avg_edge=('probability_edge', 'mean'),
    ).reset_index()
    by_selection.to_csv(output_dir / 'proxy_observation_by_selection.csv', index=False)
else:
    by_selection = pd.DataFrame(columns=['selection', 'rows', 'avg_ev', 'max_ev', 'avg_probability', 'avg_edge'])
    by_selection.to_csv(output_dir / 'proxy_observation_by_selection.csv', index=False)

markdown = [
    '# Proxy Observation Quality Report',
    '',
    'Quality diagnostics for automatic delayed-market proxy paper observations.',
    'This is not real-money ready and does not override suppression rules for candidate bets.',
    '',
    f"Value snapshot rows: {summary['value_snapshot_rows']}",
    f"Paper proxy observation rows: {summary['paper_proxy_observation_rows']}",
    f"Positive EV value rows: {summary['positive_ev_value_rows']}",
    f"Suppressed-band observation rows: {summary['suppressed_band_observation_rows']}",
    f"Distinct matches: {summary['distinct_matches']}",
    f"Distinct sources: {summary['distinct_sources']}",
    f"Max EV: {summary['max_ev']}",
    f"Average EV: {summary['avg_ev']}",
    f"Max probability edge: {summary['max_probability_edge']}",
    f"Average match confidence: {summary['avg_match_confidence']}",
    '',
    '## By selection',
    '',
]

if len(by_selection):
    for _, row in by_selection.iterrows():
        markdown.append(
            f"- {row['selection']}: rows={int(row['rows'])}, avg_ev={round(float(row['avg_ev']),4)}, max_ev={round(float(row['max_ev']),4)}"
        )
else:
    markdown.append('No proxy observations available yet.')

(output_dir / 'proxy_observation_quality_report.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
