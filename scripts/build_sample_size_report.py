from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'
clv_path = output_dir / 'clv_results.parquet'

markdown = [
    '# Sample Size Report',
    '',
]

settled = pd.read_parquet(settled_path) if settled_path.exists() else pd.DataFrame()
clv = pd.read_parquet(clv_path) if clv_path.exists() else pd.DataFrame()

settled_count = int(len(settled))
clv_count = int(len(clv))

if settled_count < 250:
    readiness = 'too_small'
elif settled_count < 750:
    readiness = 'early_reading'
elif settled_count < 1500:
    readiness = 'moderate_confidence'
else:
    readiness = 'stronger_sample'

summary = {
    'settled_predictions': settled_count,
    'clv_rows': clv_count,
    'sample_readiness': readiness,
}

pd.DataFrame([summary]).to_csv(output_dir / 'sample_size_report.csv', index=False)

markdown.extend([
    f'Settled predictions: {settled_count}',
    f'CLV rows: {clv_count}',
    f'Sample readiness: {readiness}',
    '',
])

if readiness == 'too_small':
    markdown.append('Interpretation: Sample is too small for real confidence. Continue observation.')
elif readiness == 'early_reading':
    markdown.append('Interpretation: Early pattern reading is possible, but not enough for trust.')
elif readiness == 'moderate_confidence':
    markdown.append('Interpretation: Calibration signals are becoming meaningful.')
else:
    markdown.append('Interpretation: Sample size is large enough for stronger conclusions.')

(output_dir / 'sample_size_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
