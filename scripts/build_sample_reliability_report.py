from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'

markdown = [
    '# Sample Reliability Report',
    '',
]

summary = {
    'settled_predictions': 0,
    'reliability_level': 'unknown',
    'recommended_usage': 'observation_only',
}

if not settled_path.exists():
    markdown.append('No settled predictions available.')
else:
    settled = pd.read_parquet(settled_path)

    count = len(settled)
    summary['settled_predictions'] = int(count)

    if count < 50:
        summary['reliability_level'] = 'very_low'
        summary['recommended_usage'] = 'diagnostic_only'
    elif count < 250:
        summary['reliability_level'] = 'low'
        summary['recommended_usage'] = 'paper_tracking_only'
    elif count < 1000:
        summary['reliability_level'] = 'moderate'
        summary['recommended_usage'] = 'controlled_experimental_only'
    else:
        summary['reliability_level'] = 'higher'
        summary['recommended_usage'] = 'advanced_research_ready'

    markdown.extend([
        f'Settled predictions: {count}',
        f'Reliability level: {summary["reliability_level"]}',
        f'Recommended usage: {summary["recommended_usage"]}',
        '',
        '## Interpretation',
        '',
    ])

    if count < 250:
        markdown.append('Current sample size is still too small for reliable profitability conclusions.')
    elif count < 1000:
        markdown.append('System is entering statistically useful territory, but variance remains significant.')
    else:
        markdown.append('Sample size is becoming meaningful for long-term evaluation.')

pd.DataFrame([summary]).to_csv(output_dir / 'sample_reliability_report.csv', index=False)
(output_dir / 'sample_reliability_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
