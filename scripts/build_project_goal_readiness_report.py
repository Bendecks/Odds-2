from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')


def read_csv(path: str) -> pd.DataFrame:
    file_path = output_dir / path
    if not file_path.exists() or file_path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(file_path)
    except Exception:
        return pd.DataFrame()


free_status = read_csv('free_data_status.csv')
value_summary = read_csv('automatic_forward_value_snapshot_summary.csv')
paper_status = read_csv('paper_test_log_status.csv')
proxy_quality = read_csv('proxy_observation_quality_report.csv')
forward_summary = read_csv('forward_fixture_prediction_summary.csv')
calibration_summary = read_csv('forward_probability_calibration_summary.csv')
performance = read_csv('betting_performance_summary.csv')

# Pull robust scalar values.
def scalar(df: pd.DataFrame, column: str, default=None):
    if len(df) and column in df.columns:
        value = df.iloc[0][column]
        if pd.notna(value):
            return value
    return default

forward_predictions = int(scalar(forward_summary, 'forward_fixture_prediction_rows', 0) or 0)
value_snapshots = int(scalar(value_summary, 'value_snapshot_rows', 0) or 0)
positive_ev_rows = int(scalar(value_summary, 'positive_ev_rows', 0) or 0)
paper_log_rows = int(scalar(paper_status, 'valid_forward_log_rows', 0) or 0)
proxy_obs_rows = int(scalar(proxy_quality, 'paper_proxy_observation_rows', 0) or 0)
settled_forward_rows = int(scalar(calibration_summary, 'settled_rows', 0) or 0)
accuracy = scalar(calibration_summary, 'accuracy', None)
avg_brier = scalar(calibration_summary, 'avg_brier_score', None)

# Conservative project milestones.
stages = [
    {
        'stage': 'historical_proxy_research',
        'status': 'complete_but_negative_clv',
        'target': 'Historical pipeline runs and exposes calibration/CLV weaknesses.',
        'current': 'Historical outputs exist; CLV trend remains negative.',
        'done_when': 'Use only for model diagnostics, not betting decisions.',
    },
    {
        'stage': 'automatic_proxy_odds_ingestion',
        'status': 'working',
        'target': 'Free automatic odds proxy exists and validates.',
        'current': f'{value_snapshots} value snapshots from delayed proxy prices.',
        'done_when': 'Keep Football-Data as baseline; add optional API source for fresher odds.',
    },
    {
        'stage': 'paper_forward_testing',
        'status': 'started_not_mature',
        'target': 'At least 50-100 logged proxy observations across several matchdays.',
        'current': f'{paper_log_rows} valid forward/proxy log rows.',
        'done_when': 'Minimum 50 observations before drawing early conclusions; 100+ preferred.',
    },
    {
        'stage': 'forward_probability_calibration',
        'status': 'not_ready',
        'target': 'Settled forward rows available for Brier/accuracy/calibration review.',
        'current': f'{settled_forward_rows} settled forward rows.',
        'done_when': '20+ settled rows for first weak signal; 100+ for meaningful calibration.',
    },
    {
        'stage': 'real_money_readiness',
        'status': 'not_ready',
        'target': 'Stable positive CLV, calibrated probabilities and reliable fresh odds.',
        'current': 'No real-money gate is open; candidate bets remain 0.',
        'done_when': 'Positive/neutral CLV over forward sample, stable calibration, and fresh odds source verified.',
    },
]

if paper_log_rows >= 50 and settled_forward_rows >= 20:
    overall = 'paper_testing_maturing'
elif paper_log_rows > 0:
    overall = 'proxy_paper_testing_started'
elif value_snapshots > 0:
    overall = 'proxy_value_layer_ready'
else:
    overall = 'research_only'

next_goal = 'Grow forward proxy sample, deduplicate fixtures, improve model-covered league filtering, and add optional odds-api.io/API-Football adapters.'

summary = {
    'overall_project_stage': overall,
    'forward_predictions': forward_predictions,
    'value_snapshots': value_snapshots,
    'positive_ev_rows': positive_ev_rows,
    'proxy_observation_rows': proxy_obs_rows,
    'valid_forward_log_rows': paper_log_rows,
    'settled_forward_rows': settled_forward_rows,
    'accuracy': accuracy,
    'avg_brier_score': avg_brier,
    'real_money_ready': False,
    'next_goal': next_goal,
}

pd.DataFrame([summary]).to_csv(output_dir / 'project_goal_readiness_summary.csv', index=False)
pd.DataFrame(stages).to_csv(output_dir / 'project_goal_readiness_stages.csv', index=False)

markdown = [
    '# Project Goal Readiness Report',
    '',
    f"Overall project stage: `{overall}`",
    '',
    '## Current counts',
    '',
    f"- Forward fixture predictions: {forward_predictions}",
    f"- Automatic value snapshots: {value_snapshots}",
    f"- Positive EV proxy rows: {positive_ev_rows}",
    f"- Proxy observation rows: {proxy_obs_rows}",
    f"- Valid forward/proxy log rows: {paper_log_rows}",
    f"- Settled forward rows: {settled_forward_rows}",
    f"- Real-money ready: False",
    '',
    '## Stage checklist',
    '',
]

for stage in stages:
    markdown.extend([
        f"### {stage['stage']}",
        f"Status: `{stage['status']}`",
        f"Target: {stage['target']}",
        f"Current: {stage['current']}",
        f"Done when: {stage['done_when']}",
        '',
    ])

markdown.extend([
    '## Practical definition of done',
    '',
    'The project is not in goal when it can generate one exciting pick. It is in goal when it can repeatedly produce forward observations, settle them, and show that calibration and market alignment are not obviously bad.',
    '',
    'Minimum paper-test goal:',
    '- 50+ forward/proxy observations logged',
    '- 20+ settled forward observations',
    '- no duplicate fixture inflation',
    '- proxy source clearly separated from real-money readiness',
    '',
    'Real-money goal remains much stricter:',
    '- 100+ settled forward observations',
    '- stable calibration/Brier trend',
    '- non-negative CLV/market alignment trend',
    '- fresh odds source verified, not only delayed proxy',
    '- candidate bet gate can remain 0 until these are met',
    '',
    f'Next goal: {next_goal}',
])

(output_dir / 'project_goal_readiness_report.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
