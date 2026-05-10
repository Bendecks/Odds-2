from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

candidate_path = output_dir / 'candidate_bets.parquet'

if candidate_path.exists():
    candidates = pd.read_parquet(candidate_path)
else:
    candidates = pd.DataFrame()

markdown = [
    '# Daily Betting Card',
    '',
]

if len(candidates) == 0:
    markdown.append('No qualifying bets today.')
else:
    for _, row in candidates.iterrows():
        markdown.extend([
            f"## Prediction {row['prediction_id']}",
            '',
            f"- EV: {round(float(row['ev']), 4)}",
            f"- Probability: {round(float(row['probability']), 4)}",
            f"- Market Odds: {round(float(row['market_odds']), 2)}",
            f"- Fair Odds: {round(float(row['fair_odds']), 2)}",
            f"- Signal Strength: {round(float(row['signal_strength']), 4)}",
            '',
        ])

(output_dir / 'daily_betting_card.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Built daily betting card with {len(candidates)} bets')
