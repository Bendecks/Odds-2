from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
prediction_log_path = output_dir / 'forward_fixture_prediction_log_latest.csv'
results_path = output_dir / 'forward_fixture_results.csv'

expected_columns = [
    'prediction_id', 'fixture_id', 'match_date', 'home_team', 'away_team',
    'predicted_selection', 'predicted_probability', 'actual_selection',
    'is_correct', 'brier_score', 'settlement_status'
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


predictions = safe_read_csv(prediction_log_path)
results = safe_read_csv(results_path)
rows = []

if len(predictions) and len(results):
    merged = predictions.merge(
        results[['fixture_id', 'home_score', 'away_score', 'result_status']],
        on='fixture_id',
        how='left',
    )

    for _, row in merged.iterrows():
        probs = {
            'home': pd.to_numeric(row.get('home_win_probability'), errors='coerce'),
            'draw': pd.to_numeric(row.get('draw_probability'), errors='coerce'),
            'away': pd.to_numeric(row.get('away_win_probability'), errors='coerce'),
        }
        probs = {key: float(value) for key, value in probs.items() if pd.notna(value)}
        predicted_selection = max(probs, key=probs.get) if probs else None
        predicted_probability = probs.get(predicted_selection) if predicted_selection else None

        actual_selection = None
        is_correct = None
        brier_score = None
        settlement_status = 'unsettled'

        if row.get('result_status') == 'final_or_result_available':
            home_score = pd.to_numeric(row.get('home_score'), errors='coerce')
            away_score = pd.to_numeric(row.get('away_score'), errors='coerce')
            if pd.notna(home_score) and pd.notna(away_score):
                settlement_status = 'settled'
                if home_score > away_score:
                    actual_selection = 'home'
                elif home_score == away_score:
                    actual_selection = 'draw'
                else:
                    actual_selection = 'away'
                is_correct = bool(predicted_selection == actual_selection)
                brier_score = sum(
                    (probs.get(selection, 0.0) - (1.0 if selection == actual_selection else 0.0)) ** 2
                    for selection in ['home', 'draw', 'away']
                )

        rows.append({
            'prediction_id': row.get('prediction_id'),
            'fixture_id': row.get('fixture_id'),
            'match_date': row.get('match_date'),
            'home_team': row.get('home_team'),
            'away_team': row.get('away_team'),
            'predicted_selection': predicted_selection,
            'predicted_probability': round(predicted_probability, 6) if predicted_probability is not None else None,
            'actual_selection': actual_selection,
            'is_correct': is_correct,
            'brier_score': round(float(brier_score), 6) if brier_score is not None else None,
            'settlement_status': settlement_status,
        })

calibration = pd.DataFrame(rows)
for col in expected_columns:
    if col not in calibration.columns:
        calibration[col] = None
calibration = calibration[expected_columns]
calibration.to_csv(output_dir / 'forward_probability_calibration_report.csv', index=False)

settled = calibration[calibration['settlement_status'] == 'settled'].copy() if len(calibration) else pd.DataFrame()
summary = {
    'forward_probability_rows': int(len(calibration)),
    'settled_rows': int(len(settled)),
    'unsettled_rows': int((calibration['settlement_status'] != 'settled').sum()) if len(calibration) else 0,
    'accuracy': round(float(settled['is_correct'].mean()), 4) if len(settled) else None,
    'avg_brier_score': round(float(pd.to_numeric(settled['brier_score'], errors='coerce').mean()), 6) if len(settled) else None,
}
pd.DataFrame([summary]).to_csv(output_dir / 'forward_probability_calibration_summary.csv', index=False)

markdown = [
    '# Forward Probability Calibration Report',
    '',
    'Probability-only forward calibration. No odds, no stakes, no real-money signal.',
    '',
    f"Forward probability rows: {summary['forward_probability_rows']}",
    f"Settled rows: {summary['settled_rows']}",
    f"Unsettled rows: {summary['unsettled_rows']}",
    f"Accuracy: {summary['accuracy']}",
    f"Average Brier score: {summary['avg_brier_score']}",
    '',
]

if len(calibration):
    for _, row in calibration.tail(20).iterrows():
        markdown.append(
            f"- {row['match_date']} | {row['home_team']} vs {row['away_team']} | "
            f"pred={row['predicted_selection']} ({row['predicted_probability']}) | "
            f"actual={row['actual_selection']} | status={row['settlement_status']}"
        )
else:
    markdown.append('No forward probability rows available yet.')

(output_dir / 'forward_probability_calibration_report.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
