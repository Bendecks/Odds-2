from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
card_path = output_dir / 'candidate_bets.parquet'

if card_path.exists():
    candidates = pd.read_parquet(card_path)
else:
    candidates = pd.DataFrame()

markdown = [
    '# Market Sanity Report',
    '',
]

if len(candidates) == 0:
    markdown.append('No active candidate bets to evaluate.')
else:
    candidates['market_implied_probability'] = 1 / candidates['market_odds'].replace(0, pd.NA)
    candidates['probability_gap'] = (
        candidates['probability'] - candidates['market_implied_probability']
    )

    avg_gap = candidates['probability_gap'].mean()
    avg_ev = candidates['ev'].mean()

    markdown.extend([
        f'Candidate bets: {len(candidates)}',
        f'Average probability gap: {round(float(avg_gap),4)}',
        f'Average EV: {round(float(avg_ev),4)}',
        '',
    ])

    extreme = candidates[candidates['probability_gap'] > 0.20]

    if len(extreme):
        markdown.append('WARNING: Some candidates are still extremely far from market consensus.')
    else:
        markdown.append('Candidate bets are within acceptable research guardrails.')

(output_dir / 'market_sanity_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
