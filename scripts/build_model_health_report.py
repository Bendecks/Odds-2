from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

performance_path = output_dir / 'betting_performance_report.parquet'
clv_path = output_dir / 'clv_results.parquet'
settled_path = output_dir / 'settled_predictions.parquet'

performance = pd.read_parquet(performance_path) if performance_path.exists() else pd.DataFrame()
clv = pd.read_parquet(clv_path) if clv_path.exists() else pd.DataFrame()
settled = pd.read_parquet(settled_path) if settled_path.exists() else pd.DataFrame()

health = {
    'model_state': 'unknown',
    'largest_problem': 'unknown',
    'recommended_focus': 'continue calibration',
}

if len(performance):
    row = performance.iloc[0]

    clv_rate = float(row.get('beat_closing_line_rate', 0))
    roi = float(row.get('total_roi_units', 0))

    if clv_rate < 0.5:
        health['model_state'] = 'not_beating_market'
        health['largest_problem'] = 'negative_clv'
        health['recommended_focus'] = 'improve calibration and snapshots'
    elif roi < 0:
        health['model_state'] = 'possible_variance'
        health['largest_problem'] = 'negative_roi'
        health['recommended_focus'] = 'continue paper testing'
    else:
        health['model_state'] = 'promising'
        health['largest_problem'] = 'small_sample_size'
        health['recommended_focus'] = 'increase sample size'

health_df = pd.DataFrame([health])
health_df.to_csv(output_dir / 'model_health_report.csv', index=False)

markdown = [
    '# Model Health Report',
    '',
    f"Model state: {health['model_state']}",
    f"Largest problem: {health['largest_problem']}",
    f"Recommended focus: {health['recommended_focus']}",
    '',
    f"Tracked CLV rows: {len(clv)}",
    f"Settled predictions: {len(settled)}",
]

(output_dir / 'model_health_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(health)
