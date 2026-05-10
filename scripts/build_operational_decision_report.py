from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

candidate_path = output_dir / 'candidate_bets.parquet'
alignment_path = output_dir / 'market_alignment_report.csv'

markdown = [
    '# Operational Decision Report',
    '',
]

status = 'observe_only'
reasoning = []

if alignment_path.exists():
    alignment = pd.read_csv(alignment_path)

    if len(alignment):
        avg_gap = alignment.iloc[0].get('average_alignment_gap')

        if pd.notna(avg_gap):
            reasoning.append(f'Average alignment gap: {round(float(avg_gap),4)}')

            if avg_gap < 0.10:
                status = 'experimental_betting_ready'
            elif avg_gap < 0.16:
                status = 'paper_tracking_ready'
            else:
                status = 'observe_only'

if candidate_path.exists():
    candidates = pd.read_parquet(candidate_path)
    reasoning.append(f'Candidate bets: {len(candidates)}')

markdown.extend([
    f'System status: {status}',
    '',
    '## Reasoning',
    '',
])

for item in reasoning:
    markdown.append(f'- {item}')

markdown.extend([
    '',
    '## Current interpretation',
    '',
])

if status == 'observe_only':
    markdown.append('Model should continue gathering calibration and CLV data before trust increases.')
elif status == 'paper_tracking_ready':
    markdown.append('Model is suitable for paper-tracking and controlled monitoring.')
else:
    markdown.append('Model is stable enough for small-scale experimental evaluation.')

(output_dir / 'operational_decision_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(status)
