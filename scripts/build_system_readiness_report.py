from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

alignment_path = output_dir / 'market_alignment_report.csv'
sample_path = output_dir / 'sample_size_report.csv'

markdown = [
    '# System Readiness Report',
    '',
]

score = 0
reasons = []

if alignment_path.exists():
    alignment = pd.read_csv(alignment_path)

    if len(alignment):
        gap = alignment.iloc[0].get('average_alignment_gap')

        if pd.notna(gap):
            if gap < 0.08:
                score += 40
                reasons.append('Excellent market alignment.')
            elif gap < 0.14:
                score += 25
                reasons.append('Moderate market alignment.')
            else:
                score += 10
                reasons.append('Weak market alignment.')

if sample_path.exists():
    sample = pd.read_csv(sample_path)

    if len(sample):
        settled = sample.iloc[0].get('settled_predictions', 0)

        if settled >= 1500:
            score += 40
            reasons.append('Large settlement sample.')
        elif settled >= 750:
            score += 25
            reasons.append('Moderate settlement sample.')
        elif settled >= 250:
            score += 15
            reasons.append('Early settlement sample.')
        else:
            score += 5
            reasons.append('Very small settlement sample.')

candidate_path = output_dir / 'candidate_bets.parquet'

if candidate_path.exists():
    candidates = pd.read_parquet(candidate_path)

    if 1 <= len(candidates) <= 15:
        score += 20
        reasons.append('Candidate volume appears realistic.')
    elif len(candidates) == 0:
        score += 5
        reasons.append('No candidate bets available.')
    else:
        score += 10
        reasons.append('Candidate volume may still be noisy.')

if score >= 80:
    readiness = 'controlled_experimental_ready'
elif score >= 55:
    readiness = 'paper_tracking_ready'
else:
    readiness = 'observation_only'

summary = {
    'readiness_score': score,
    'readiness_status': readiness,
}

pd.DataFrame([summary]).to_csv(output_dir / 'system_readiness_report.csv', index=False)

markdown.extend([
    f'Readiness score: {score}/100',
    f'Readiness status: {readiness}',
    '',
    '## Reasons',
    '',
])

for reason in reasons:
    markdown.append(f'- {reason}')

(output_dir / 'system_readiness_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
