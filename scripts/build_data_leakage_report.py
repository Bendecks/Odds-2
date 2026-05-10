from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
raw_current_path = Path('data/raw/premier_league_2425.parquet')
pred_path = output_dir / 'prediction_log_latest.parquet'

markdown = [
    '# Data Leakage Report',
    '',
]

summary = {
    'prediction_rows': 0,
    'unique_prediction_ids': 0,
    'duplicate_prediction_ids': 0,
    'settled_same_day_proxy_warning': False,
    'risk_level': 'unknown',
}

if pred_path.exists():
    predictions = pd.read_parquet(pred_path)
    summary['prediction_rows'] = int(len(predictions))

    if 'prediction_id' in predictions.columns:
        summary['unique_prediction_ids'] = int(predictions['prediction_id'].nunique())
        summary['duplicate_prediction_ids'] = int(len(predictions) - predictions['prediction_id'].nunique())

    if 'match_date' in predictions.columns:
        date_counts = predictions['match_date'].value_counts().head(5)
        markdown.extend([
            '## Top match dates in prediction log',
            '',
        ])
        for date, count in date_counts.items():
            markdown.append(f'- {date}: {count}')
else:
    markdown.append('No prediction log available.')

if raw_current_path.exists() and pred_path.exists():
    raw = pd.read_parquet(raw_current_path)
    predictions = pd.read_parquet(pred_path)

    if {'HomeTeam', 'AwayTeam', 'Date'}.issubset(raw.columns) and {'home_team', 'away_team', 'match_date'}.issubset(predictions.columns):
        merged = predictions.merge(
            raw[['HomeTeam', 'AwayTeam', 'Date', 'FTR']].rename(columns={
                'HomeTeam': 'home_team',
                'AwayTeam': 'away_team',
                'Date': 'match_date',
            }),
            on=['home_team', 'away_team', 'match_date'],
            how='left',
        )

        known_results = merged['FTR'].notna().sum() if 'FTR' in merged.columns else 0
        if known_results > 0:
            summary['settled_same_day_proxy_warning'] = True
            markdown.append('')
            markdown.append(f'Known historical result matches found in predictions: {int(known_results)}')

if summary['duplicate_prediction_ids'] > 0 or summary['settled_same_day_proxy_warning']:
    summary['risk_level'] = 'medium'
else:
    summary['risk_level'] = 'low'

pd.DataFrame([summary]).to_csv(output_dir / 'data_leakage_report.csv', index=False)

markdown.extend([
    '',
    '## Summary',
    '',
    f"Prediction rows: {summary['prediction_rows']}",
    f"Unique prediction IDs: {summary['unique_prediction_ids']}",
    f"Duplicate prediction IDs: {summary['duplicate_prediction_ids']}",
    f"Known-result proxy warning: {summary['settled_same_day_proxy_warning']}",
    f"Risk level: {summary['risk_level']}",
    '',
    '## Interpretation',
    '',
])

if summary['settled_same_day_proxy_warning']:
    markdown.append('Current setup uses historical proxy markets, so performance metrics must be treated as research diagnostics, not forward-looking validation.')
else:
    markdown.append('No obvious leakage warning detected in current diagnostic checks.')

(output_dir / 'data_leakage_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
