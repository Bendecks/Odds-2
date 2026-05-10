from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

settled = pd.read_parquet(output_dir / 'settled_predictions.parquet')
clv = pd.read_parquet(output_dir / 'clv_results.parquet')

candidate_bets = settled[settled['is_candidate'] == True].copy()

summary = {
    'total_predictions': int(len(settled)),
    'candidate_predictions': int(len(candidate_bets)),
    'settled_predictions': int((settled['settlement_status'] == 'settled').sum()),
    'wins': int((settled.get('won', False) == True).sum()),
    'total_roi_units': round(float(settled.get('roi_units', pd.Series(dtype=float)).fillna(0).sum()), 4),
    'average_roi_per_bet': round(float(settled.get('roi_units', pd.Series(dtype=float)).fillna(0).mean()), 4),
    'beat_closing_line_rate': round(float(clv['beat_closing_line'].mean()), 4) if len(clv) else 0,
    'average_clv_delta': round(float(clv['clv_delta'].mean()), 4) if len(clv) else 0,
}

summary_df = pd.DataFrame([summary])

summary_df.to_csv(output_dir / 'betting_performance_report.csv', index=False)
summary_df.to_parquet(output_dir / 'betting_performance_report.parquet', index=False)

markdown = [
    '# Betting Performance Report',
    '',
    f"Total predictions: {summary['total_predictions']}",
    f"Candidate predictions: {summary['candidate_predictions']}",
    f"Settled predictions: {summary['settled_predictions']}",
    f"Wins: {summary['wins']}",
    f"Total ROI units: {summary['total_roi_units']}",
    f"Average ROI per bet: {summary['average_roi_per_bet']}",
    f"Beat closing line rate: {summary['beat_closing_line_rate']}",
    f"Average CLV delta: {summary['average_clv_delta']}",
]

(output_dir / 'betting_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
