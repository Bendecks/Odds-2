from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

alignment_path = output_dir / 'market_alignment_report.csv'
operational_path = output_dir / 'operational_decision_report.md'

markdown = [
    '# Human Action Report',
    '',
]

actions = []

if alignment_path.exists():
    alignment = pd.read_csv(alignment_path)

    if len(alignment):
        gap = alignment.iloc[0].get('average_alignment_gap')

        if pd.notna(gap):
            if gap > 0.18:
                actions.append('Model alignment still weak. Continue observation only.')
            elif gap > 0.10:
                actions.append('Paper-tracking recommended before real usage.')
            else:
                actions.append('Model alignment acceptable for controlled experiments.')

candidate_path = output_dir / 'candidate_bets.parquet'

if candidate_path.exists():
    candidates = pd.read_parquet(candidate_path)

    if len(candidates) == 0:
        actions.append('No candidate bets currently pass filtering.')
    elif len(candidates) > 20:
        actions.append('Large candidate volume detected. Review filtering strictness.')
    else:
        actions.append(f'{len(candidates)} candidate bets currently available.')

if not actions:
    actions.append('No immediate human action required.')

markdown.extend([
    '## Recommended actions',
    '',
])

for item in actions:
    markdown.append(f'- {item}')

(output_dir / 'human_action_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(actions)
