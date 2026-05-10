from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

reports = [
    'system_readiness_report.csv',
    'forward_test_readiness_report.csv',
    'clv_trend_report.csv',
    'probability_band_report.csv',
    'model_adjustment_recommendation.csv',
    'sample_reliability_report.csv',
]

markdown = [
    '# Project Handoff Report',
    '',
    f'Generated UTC: {datetime.now(timezone.utc).isoformat()}',
    '',
    '## Core system status',
    '',
]

for report_name in reports:
    path = output_dir / report_name

    if not path.exists() or path.stat().st_size == 0:
        markdown.append(f'- {report_name}: unavailable')
        continue

    try:
        df = pd.read_csv(path)
    except Exception as exc:
        markdown.append(f'- {report_name}: failed to read ({exc})')
        continue

    if len(df) == 0:
        markdown.append(f'- {report_name}: empty')
        continue

    row = df.iloc[0].to_dict()
    compact = ', '.join([f'{k}={v}' for k, v in row.items()][:5])
    markdown.append(f'- {report_name}: {compact}')

markdown.extend([
    '',
    '## Current strategic focus',
    '',
    '- Improve CLV performance.',
    '- Reduce probability overconfidence.',
    '- Continue collecting settled predictions.',
    '- Separate historical proxy research from real forward-testing.',
    '- Improve calibration before adding major model complexity.',
])

(output_dir / 'project_handoff_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print('Generated project handoff report')
