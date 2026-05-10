from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

candidate_path = output_dir / 'candidate_bets.parquet'
snapshot_path = output_dir / 'prediction_snapshots_latest.parquet'
prediction_log_path = output_dir / 'prediction_log_latest.parquet'

if candidate_path.exists():
    candidates = pd.read_parquet(candidate_path)
else:
    candidates = pd.DataFrame()

snapshots = pd.read_parquet(snapshot_path) if snapshot_path.exists() else pd.DataFrame()
predictions = pd.read_parquet(prediction_log_path) if prediction_log_path.exists() else pd.DataFrame()

if len(candidates) and len(predictions):
    candidates = candidates.merge(
        predictions[
            [
                'prediction_id',
                'match_date',
                'match_time',
                'home_team',
                'away_team',
                'selection',
            ]
        ].drop_duplicates('prediction_id'),
        on='prediction_id',
        how='left',
    )

markdown = [
    '# Daily Betting Card',
    '',
    'Status: research/paper-test only. No real-money recommendation yet.',
    '',
]

if len(candidates) == 0:
    markdown.append('No qualifying bets today.')
else:
    for _, row in candidates.iterrows():
        match_title = f"{row.get('home_team', 'Unknown')} vs {row.get('away_team', 'Unknown')}"
        selection = str(row.get('selection', 'unknown')).upper()

        markdown.extend([
            f"## {match_title}",
            '',
            f"- Date/time: {row.get('match_date', '')} {row.get('match_time', '')}",
            f"- Selection: {selection}",
            f"- Market: 1X2",
            f"- Market odds: {round(float(row['market_odds']), 2)}",
            f"- Fair odds: {round(float(row['fair_odds']), 2)}",
            f"- Model probability: {round(float(row['probability']), 4)}",
            f"- EV: {round(float(row['ev']), 4)}",
            f"- Signal strength: {round(float(row['signal_strength']), 4)}",
            f"- Prediction ID: {row['prediction_id']}",
            '',
        ])

markdown.extend([
    '## Snapshot summary',
    '',
    f"Snapshot rows: {len(snapshots)}",
    f"Candidate rows: {len(candidates)}",
])

(output_dir / 'daily_betting_card.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Built daily betting card with {len(candidates)} bets')
