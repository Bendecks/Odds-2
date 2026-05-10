from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

alignment_path = output_dir / 'market_alignment_report.csv'
sample_path = output_dir / 'sample_size_report.csv'
clv_path = output_dir / 'clv_trend_report.csv'
risk_path = output_dir / 'strategy_risk_report.csv'

markdown = [
    '# System Readiness Report',
    '',
]

score = 0
reasons = []


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()

alignment = safe_read_csv(alignment_path)
if len(alignment):
    gap = alignment.iloc[0].get('average_alignment_gap')

    if pd.notna(gap):
        if gap < 0.08:
            score += 30
            reasons.append('Excellent market alignment.')
        elif gap < 0.14:
            score += 20
            reasons.append('Moderate market alignment.')
        else:
            score += 10
            reasons.append('Weak market alignment.')

sample = safe_read_csv(sample_path)
if len(sample):
    settled = sample.iloc[0].get('settled_predictions', 0)

    if settled >= 1500:
        score += 30
        reasons.append('Large settlement sample.')
    elif settled >= 750:
        score += 20
        reasons.append('Moderate settlement sample.')
    elif settled >= 250:
        score += 12
        reasons.append('Early settlement sample.')
    else:
        score += 5
        reasons.append('Very small settlement sample.')

clv = safe_read_csv(clv_path)
if len(clv):
    beat_rate = clv.iloc[0].get('beat_closing_line_rate')

    if pd.notna(beat_rate):
        if beat_rate >= 0.56:
            score += 25
            reasons.append('Strong CLV performance.')
        elif beat_rate >= 0.51:
            score += 15
            reasons.append('Positive CLV performance.')
        elif beat_rate >= 0.48:
            score += 8
            reasons.append('Neutral CLV performance.')
        else:
            score += 2
            reasons.append('Weak CLV performance.')

risk = safe_read_csv(risk_path)
if len(risk):
    risk_level = str(risk.iloc[0].get('risk_level', 'high'))

    if risk_level == 'controlled':
        score += 15
        reasons.append('Controlled volatility profile.')
    elif risk_level == 'moderate':
        score += 10
        reasons.append('Moderate volatility profile.')
    else:
        score += 3
        reasons.append('High volatility profile.')

candidate_path = output_dir / 'candidate_bets.parquet'

if candidate_path.exists():
    try:
        candidates = pd.read_parquet(candidate_path)
    except Exception:
        candidates = pd.DataFrame()

    if 1 <= len(candidates) <= 15:
        score += 10
        reasons.append('Candidate volume appears realistic.')
    elif len(candidates) == 0:
        score += 3
        reasons.append('No candidate bets available.')
    else:
        score += 5
        reasons.append('Candidate volume may still be noisy.')

if not reasons:
    reasons.append('Not enough diagnostics available yet.')

if score >= 85:
    readiness = 'controlled_experimental_ready'
elif score >= 60:
    readiness = 'paper_tracking_ready'
else:
    readiness = 'observation_only'

summary = {
    'readiness_score': score,
    'readiness_status': readiness,
}

pd.DataFrame([summary]).to_csv(output_dir / 'system_readiness_report.csv', index=False)

markdown.extend([
    f'Readiness score: {score}/110',
    f'Readiness status: {readiness}',
    '',
    '## Reasons',
    '',
])

for reason in reasons:
    markdown.append(f'- {reason}')

(output_dir / 'system_readiness_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
