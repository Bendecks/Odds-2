from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

leakage_path = output_dir / 'data_leakage_report.csv'
reliability_path = output_dir / 'sample_reliability_report.csv'
readiness_path = output_dir / 'system_readiness_report.csv'
paper_path = output_dir / 'paper_test_picks.parquet'

markdown = [
    '# Forward Test Readiness Report',
    '',
]

status = 'not_ready'
reasons = []


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


leakage = safe_read_csv(leakage_path)
if len(leakage):
    risk = str(leakage.iloc[0].get('risk_level', 'unknown'))
    reasons.append(f'Data leakage risk: {risk}')
else:
    risk = 'unknown'
    reasons.append('Data leakage diagnostics unavailable.')

reliability = safe_read_csv(reliability_path)
if len(reliability):
    usage = str(reliability.iloc[0].get('recommended_usage', 'unknown'))
    reasons.append(f'Sample recommendation: {usage}')
else:
    usage = 'unknown'
    reasons.append('Sample reliability diagnostics unavailable.')

readiness = safe_read_csv(readiness_path)
if len(readiness):
    readiness_status = str(readiness.iloc[0].get('readiness_status', 'unknown'))
    reasons.append(f'System readiness: {readiness_status}')
else:
    readiness_status = 'unknown'
    reasons.append('System readiness diagnostics unavailable.')

paper = safe_read_parquet(paper_path)
forward_paper_picks = len(paper)
reasons.append(f'Forward-eligible paper-test picks: {forward_paper_picks}')

if forward_paper_picks == 0:
    status = 'no_forward_picks_available'
elif risk == 'low' and readiness_status in ['paper_tracking_ready', 'controlled_experimental_ready']:
    status = 'paper_forward_test_ready'
elif readiness_status == 'observation_only':
    status = 'observe_only_with_forward_picks'
else:
    status = 'forward_observation_only'

summary = {
    'forward_test_status': status,
    'leakage_risk': risk,
    'sample_usage': usage,
    'system_readiness': readiness_status,
    'forward_paper_picks': int(forward_paper_picks),
}

pd.DataFrame([summary]).to_csv(output_dir / 'forward_test_readiness_report.csv', index=False)

markdown.extend([
    f'Forward test status: {status}',
    '',
    '## Reasons',
    '',
])

for reason in reasons:
    markdown.append(f'- {reason}')

markdown.extend([
    '',
    '## Interpretation',
    '',
])

if status == 'paper_forward_test_ready':
    markdown.append('The system can be used for forward paper-tracking, but not real-money betting.')
elif status == 'no_forward_picks_available':
    markdown.append('No current paper-test picks are forward-eligible. Historical proxy rows must not be counted as paper-test picks.')
elif status == 'observe_only_with_forward_picks':
    markdown.append('Forward paper picks exist, but the system is still observation-only.')
else:
    markdown.append('The system remains a forward observation/proxy research environment, not a real-money system.')

(output_dir / 'forward_test_readiness_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
