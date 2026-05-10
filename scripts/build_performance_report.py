from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

settled = pd.read_parquet(output_dir / 'settled_predictions.parquet')
clv = pd.read_parquet(output_dir / 'clv_results.parquet')

candidate_path = output_dir / 'candidate_bets.parquet'
if candidate_path.exists():
    current_candidates = pd.read_parquet(candidate_path)
else:
    current_candidates = pd.DataFrame()

historical_candidates = settled[settled['is_candidate'] == True].copy()

settled_roi = settled.get('roi_units', pd.Series(dtype=float)).fillna(0)
current_candidate_count = int(len(current_candidates))

summary = {
    'total_predictions': int(len(settled)),
    'historical_candidate_predictions': int(len(historical_candidates)),
    'current_candidate_bets': current_candidate_count,
    'settled_predictions': int((settled['settlement_status'] == 'settled').sum()),
    'wins': int((settled.get('won', False) == True).sum()),
    'total_roi_units': round(float(settled_roi.sum()), 4),
    'average_roi_per_bet': round(float(settled_roi.mean()), 4) if len(settled_roi) else 0,
    'beat_closing_line_rate': round(float(clv['beat_closing_line'].fillna(False).mean()), 4) if len(clv) else 0,
    'average_clv_delta': round(float(clv['clv_delta'].dropna().mean()), 4) if len(clv['clv_delta'].dropna()) else 0,
}

if summary['beat_closing_line_rate'] >= 0.53 and summary['average_clv_delta'] > 0:
    readiness = 'paper-test-promising'
elif summary['beat_closing_line_rate'] >= 0.50:
    readiness = 'paper-test-only'
else:
    readiness = 'research-only'

summary['readiness'] = readiness
summary['recommendation'] = 'NO REAL MONEY - continue research' if readiness == 'research-only' else 'Paper test only'

summary_df = pd.DataFrame([summary])

summary_df.to_csv(output_dir / 'betting_performance_report.csv', index=False)
summary_df.to_parquet(output_dir / 'betting_performance_report.parquet', index=False)

markdown = [
    '# Betting Performance Report',
    '',
    f"Readiness: {summary['readiness']}",
    f"Recommendation: {summary['recommendation']}",
    '',
    f"Total predictions: {summary['total_predictions']}",
    f"Historical candidate predictions: {summary['historical_candidate_predictions']}",
    f"Current candidate bets: {summary['current_candidate_bets']}",
    f"Settled predictions: {summary['settled_predictions']}",
    f"Wins: {summary['wins']}",
    f"Total ROI units: {summary['total_roi_units']}",
    f"Average ROI per bet: {summary['average_roi_per_bet']}",
    f"Beat closing line rate: {summary['beat_closing_line_rate']}",
    f"Average CLV delta: {summary['average_clv_delta']}",
    '',
    '## Interpretation',
    '',
]

if readiness == 'research-only':
    markdown.append('The model is not ready for real-money betting. Focus remains on CLV improvement, calibration and realistic market snapshots.')
else:
    markdown.append('The model may be suitable for paper-testing only. Real-money betting should still wait for a longer observation period.')

(output_dir / 'betting_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
