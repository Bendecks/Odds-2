from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

candidate_path = output_dir / 'candidate_bets.parquet'
snapshot_path = output_dir / 'prediction_snapshots_latest.parquet'
prediction_log_path = output_dir / 'prediction_log_latest.parquet'
suppression_rules_path = output_dir / 'signal_suppression_rules.csv'


def safe_read_parquet(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_parquet(path)
    except Exception:
        return pd.DataFrame()


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


candidates = safe_read_parquet(candidate_path)
snapshots = safe_read_parquet(snapshot_path)
predictions = safe_read_parquet(prediction_log_path)
suppression_rules = safe_read_csv(suppression_rules_path)

if len(candidates) and len(predictions) and 'prediction_id' in predictions.columns:
    merge_cols = [
        'prediction_id',
        'match_date',
        'match_time',
        'home_team',
        'away_team',
        'selection',
    ]
    merge_cols = [col for col in merge_cols if col in predictions.columns]
    candidates = candidates.merge(
        predictions[merge_cols].drop_duplicates('prediction_id'),
        on='prediction_id',
        how='left',
        suffixes=('', '_log'),
    )

markdown = [
    '# Daily Betting Card',
    '',
    'Status: research/paper-test only. No real-money recommendation yet.',
    'Current card is suppression-aware and must not be used for real-money betting.',
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
            f"- League/phase: {row.get('league', 'unknown')} / {row.get('sample_phase', 'unknown')}",
            f"- Selection: {selection}",
            f"- Market: 1X2",
            f"- Market odds: {round(float(row['market_odds']), 2)}",
            f"- Fair odds: {round(float(row['fair_odds']), 2)}",
            f"- Model probability: {round(float(row['probability']), 4)}",
            f"- Probability band: {row.get('probability_band', 'unknown')}",
            f"- EV: {round(float(row['ev']), 4)}",
            f"- Signal strength: {round(float(row['signal_strength']), 4)}",
            f"- Suppression action: {row.get('suppression_action', 'none')}",
            f"- Calibration risk: {row.get('calibration_risk', 'unknown')}",
            f"- Prediction ID: {row['prediction_id']}",
            '',
        ])

markdown.extend([
    '## Snapshot summary',
    '',
    f"Snapshot rows: {len(snapshots)}",
    f"Candidate rows: {len(candidates)}",
    f"Active suppression rules: {len(suppression_rules)}",
])

(output_dir / 'daily_betting_card.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Built daily betting card with {len(candidates)} bets')
