from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

inputs = {
    'forward': output_dir / 'forward_test_readiness_report.csv',
    'readiness': output_dir / 'system_readiness_report.csv',
    'clv': output_dir / 'clv_trend_report.csv',
    'leakage': output_dir / 'data_leakage_report.csv',
    'candidates': output_dir / 'candidate_bets.parquet',
}

markdown = ['# Daily Decision Report', '']
reasons = []
decision = 'do_not_use_real_money'

def safe_csv(path):
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()

forward = safe_csv(inputs['forward'])
if len(forward):
    forward_status = str(forward.iloc[0].get('forward_test_status', 'unknown'))
    reasons.append(f'Forward test status: {forward_status}')
else:
    forward_status = 'unknown'
    reasons.append('Forward test status unavailable.')

readiness = safe_csv(inputs['readiness'])
if len(readiness):
    readiness_status = str(readiness.iloc[0].get('readiness_status', 'unknown'))
    score = readiness.iloc[0].get('readiness_score')
    reasons.append(f'Readiness: {readiness_status} score={score}')
else:
    readiness_status = 'unknown'
    reasons.append('Readiness unavailable.')

clv = safe_csv(inputs['clv'])
if len(clv):
    beat_rate = clv.iloc[0].get('beat_closing_line_rate')
    avg_delta = clv.iloc[0].get('avg_clv_delta')
    reasons.append(f'CLV beat rate: {beat_rate}; avg delta: {avg_delta}')
else:
    beat_rate = None
    reasons.append('CLV unavailable.')

leakage = safe_csv(inputs['leakage'])
if len(leakage):
    leakage_risk = str(leakage.iloc[0].get('risk_level', 'unknown'))
    reasons.append(f'Leakage risk: {leakage_risk}')
else:
    leakage_risk = 'unknown'
    reasons.append('Leakage diagnostics unavailable.')

if inputs['candidates'].exists():
    try:
        candidates = pd.read_parquet(inputs['candidates'])
    except Exception:
        candidates = pd.DataFrame()
else:
    candidates = pd.DataFrame()

reasons.append(f'Candidate bets: {len(candidates)}')

# Deliberately conservative decisioning.
if leakage_risk != 'low':
    decision = 'ignore_picks_proxy_research_only'
elif len(candidates) == 0:
    decision = 'no_action_no_candidates'
elif readiness_status == 'controlled_experimental_ready' and beat_rate is not None and float(beat_rate) >= 0.54:
    decision = 'paper_track_candidates_only'
elif readiness_status in ['paper_tracking_ready', 'controlled_experimental_ready']:
    decision = 'paper_track_candidates_only'
else:
    decision = 'observe_only'

summary = {
    'daily_decision': decision,
    'candidate_count': int(len(candidates)),
    'readiness_status': readiness_status,
    'forward_status': forward_status,
    'leakage_risk': leakage_risk,
}

pd.DataFrame([summary]).to_csv(output_dir / 'daily_decision_report.csv', index=False)

markdown.extend([
    f'Daily decision: {decision}',
    '',
    '## Reasons',
    '',
])

for reason in reasons:
    markdown.append(f'- {reason}')

markdown.extend(['', '## Instruction', ''])

if decision == 'paper_track_candidates_only':
    markdown.append('Paper-track candidates only. Do not use real money.')
elif decision == 'ignore_picks_proxy_research_only':
    markdown.append('Ignore current picks as betting candidates; use only for proxy research diagnostics.')
elif decision == 'no_action_no_candidates':
    markdown.append('No candidates passed filters. No action.')
else:
    markdown.append('Continue observation only.')

(output_dir / 'daily_decision_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
