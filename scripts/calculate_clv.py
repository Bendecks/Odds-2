from pathlib import Path

import pandas as pd

prediction_log_path = Path('output/latest/prediction_log_latest.parquet')
market_path = Path('data/raw/premier_league_2425.parquet')
output_dir = Path('output/latest')

expected_columns = [
    'prediction_id',
    'home_team',
    'away_team',
    'league',
    'season',
    'sample_phase',
    'selection',
    'opening_probability',
    'opening_ev',
    'opening_odds',
    'closing_odds',
    'clv_delta',
    'beat_closing_line',
]

if not prediction_log_path.exists() or not market_path.exists():
    clv_df = pd.DataFrame(columns=expected_columns)
else:
    predictions = pd.read_parquet(prediction_log_path)
    market = pd.read_parquet(market_path)

    if len(predictions) == 0 or len(market) == 0:
        clv_df = pd.DataFrame(columns=expected_columns)
    else:
        market['Date'] = market['Date'].astype(str)
        clv_records = []

        for _, pred in predictions.iterrows():
            for col, default in [
                ('league', 'unknown'),
                ('season', 'unknown'),
                ('sample_phase', 'historical_proxy_research'),
                ('opening_probability', None),
                ('opening_ev', None),
            ]:
                if col not in pred.index:
                    pred[col] = default

            match = market[
                (market['HomeTeam'] == pred.get('home_team'))
                & (market['AwayTeam'] == pred.get('away_team'))
                & (market['Date'] == str(pred.get('match_date')))
            ]

            if match.empty:
                continue

            match = match.iloc[0]

            if pred.get('selection') == 'home':
                closing_odds = match.get('PSCH')
            elif pred.get('selection') == 'draw':
                closing_odds = match.get('PSCD')
            else:
                closing_odds = match.get('PSCA')

            opening_odds = pred.get('opening_market_odds')
            if pd.isna(opening_odds) and 'market_odds' in pred.index:
                opening_odds = pred.get('market_odds')

            opening_odds = pd.to_numeric(opening_odds, errors='coerce')
            closing_odds = pd.to_numeric(closing_odds, errors='coerce')

            if pd.isna(closing_odds) or pd.isna(opening_odds):
                continue

            clv_delta = float(opening_odds) - float(closing_odds)
            beat_closing_line = clv_delta > 0

            clv_records.append({
                'prediction_id': pred.get('prediction_id'),
                'home_team': pred.get('home_team'),
                'away_team': pred.get('away_team'),
                'league': pred.get('league', 'unknown'),
                'season': pred.get('season', 'unknown'),
                'sample_phase': pred.get('sample_phase', 'historical_proxy_research'),
                'selection': pred.get('selection'),
                'opening_probability': pd.to_numeric(pred.get('opening_probability'), errors='coerce'),
                'opening_ev': pd.to_numeric(pred.get('opening_ev'), errors='coerce'),
                'opening_odds': float(opening_odds),
                'closing_odds': float(closing_odds),
                'clv_delta': round(clv_delta, 4),
                'beat_closing_line': beat_closing_line,
            })

        clv_df = pd.DataFrame(clv_records)

for col in expected_columns:
    if col not in clv_df.columns:
        clv_df[col] = None

clv_df = clv_df[expected_columns]

clv_df.to_parquet(output_dir / 'clv_results.parquet', index=False)
clv_df.to_csv(output_dir / 'clv_results.csv', index=False)

summary = {
    'tracked_predictions': int(len(clv_df)),
    'beat_closing_line_count': int(clv_df['beat_closing_line'].fillna(False).sum()) if len(clv_df) else 0,
    'beat_closing_line_rate': round(float(clv_df['beat_closing_line'].fillna(False).mean()), 4) if len(clv_df) else 0,
    'average_clv_delta': round(float(clv_df['clv_delta'].dropna().mean()), 4) if len(clv_df['clv_delta'].dropna()) else 0,
}

pd.DataFrame([summary]).to_csv(output_dir / 'clv_summary.csv', index=False)

# Extra diagnostics for separation of proxy research vs forward paper tracking.
phase_rows = []
if len(clv_df):
    for phase, subset in clv_df.groupby('sample_phase', dropna=False):
        phase_rows.append({
            'sample_phase': phase,
            'rows': int(len(subset)),
            'avg_clv_delta': round(float(subset['clv_delta'].dropna().mean()), 4) if len(subset['clv_delta'].dropna()) else None,
            'beat_closing_line_rate': round(float(subset['beat_closing_line'].fillna(False).mean()), 4),
        })

pd.DataFrame(phase_rows).to_csv(output_dir / 'clv_by_sample_phase.csv', index=False)

print(summary)
