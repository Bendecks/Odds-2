from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

reports = [
    'system_readiness_report.csv',
    'forward_test_readiness_report.csv',
    'clv_trend_report.csv',
    'clv_band_report.csv',
    'probability_calibration_rules.csv',
    'signal_suppression_rules.csv',
    'rule_action_summary.csv',
    'phase_performance_report.csv',
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
    compact = ', '.join([f'{k}={v}' for k, v in row.items()][:6])
    markdown.append(f'- {report_name}: {compact}')

markdown.extend([
    '',
    '## Current strategic focus',
    '',
    '- Improve CLV performance before relaxing candidate filters.',
    '- Keep probability distribution conservative while CLV is negative.',
    '- Evaluate whether the CLV-band probability calibration layer improves future CLV.',
    '- Use CLV probability-band diagnostics to suppress toxic bands.',
    '- Keep historical proxy research separate from paper forward-testing.',
    '- Use league-specific evaluation only as diagnostics until samples are larger.',
    '- Do not add real-money features.',
])

(output_dir / 'project_handoff_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print('Generated project handoff report')
