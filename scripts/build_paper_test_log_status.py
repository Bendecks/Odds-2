from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
log_path = Path('data/predictions/paper_test_log.jsonl')

FORWARD_PHASES = {'paper_forward_test', 'live_forward_snapshot', 'upcoming_fixture', 'automatic_forward_price_proxy'}

expected_columns = [
    'snapshot_id', 'prediction_id', 'match_date', 'home_team', 'away_team', 'sample_phase',
    'selection', 'market_odds', 'probability', 'ev', 'paper_test_tier',
    'paper_test_score', 'paper_test_reason', 'suppression_action'
]


def empty_frame() -> pd.DataFrame:
    return pd.DataFrame(columns=expected_columns)


if log_path.exists() and log_path.stat().st_size > 0:
    try:
        raw = pd.read_json(log_path, lines=True)
    except Exception:
        raw = empty_frame()
else:
    raw = empty_frame()

for col in expected_columns:
    if col not in raw.columns:
        raw[col] = None

if len(raw):
    raw['sample_phase'] = raw['sample_phase'].fillna('unknown').astype(str)
    valid = raw[raw['sample_phase'].isin(FORWARD_PHASES)].copy()
    invalid = raw[~raw['sample_phase'].isin(FORWARD_PHASES)].copy()
else:
    valid = empty_frame()
    invalid = empty_frame()

valid = valid[expected_columns]
invalid = invalid[expected_columns]

valid.to_csv(output_dir / 'paper_test_log_latest.csv', index=False)
invalid.to_csv(output_dir / 'invalid_paper_test_log_rows.csv', index=False)

proxy_rows = int((valid['sample_phase'] == 'automatic_forward_price_proxy').sum()) if len(valid) else 0
summary = {
    'raw_log_rows': int(len(raw)),
    'valid_forward_log_rows': int(len(valid)),
    'valid_proxy_observation_rows': proxy_rows,
    'invalid_historical_proxy_log_rows': int(len(invalid)),
    'has_valid_forward_log': bool(len(valid) > 0),
}

pd.DataFrame([summary]).to_csv(output_dir / 'paper_test_log_status.csv', index=False)

markdown = [
    '# Paper Test Log Status',
    '',
    f"Raw log rows: {summary['raw_log_rows']}",
    f"Valid forward/proxy log rows: {summary['valid_forward_log_rows']}",
    f"Valid automatic proxy observation rows: {summary['valid_proxy_observation_rows']}",
    f"Invalid historical/proxy log rows excluded: {summary['invalid_historical_proxy_log_rows']}",
    f"Has valid forward log: {summary['has_valid_forward_log']}",
    '',
]

if len(valid):
    markdown.extend(['## Valid rows', ''])
    for _, row in valid.tail(20).iterrows():
        markdown.append(
            f"- {row.get('match_date')} | {row.get('home_team')} vs {row.get('away_team')} | "
            f"selection={row.get('selection')} | phase={row.get('sample_phase')} | tier={row.get('paper_test_tier')}"
        )

if len(invalid):
    markdown.extend(['', '## Invalid rows excluded', ''])
    for _, row in invalid.head(20).iterrows():
        markdown.append(
            f"- {row.get('match_date')} | {row.get('home_team')} vs {row.get('away_team')} | phase={row.get('sample_phase')}"
        )

(output_dir / 'paper_test_log_status.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
