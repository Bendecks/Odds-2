from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
status_path = output_dir / 'free_data_status.json'

markdown = [
    '# Workflow Failure Hint Report',
    '',
]

rows = []

if status_path.exists():
    try:
        import json
        status = json.loads(status_path.read_text(encoding='utf-8'))
        overall_ok = bool(status.get('overall_ok'))
        checks = status.get('checks', [])
        failed_checks = [c for c in checks if not c.get('ok')]

        rows.append({
            'area': 'validation',
            'status': 'ok' if overall_ok else 'failed',
            'hint': 'Core data/report validation passed.' if overall_ok else 'One or more validation checks failed.',
        })

        for check in failed_checks:
            rows.append({
                'area': check.get('name'),
                'status': 'failed',
                'hint': f"missing={check.get('missing_columns')} error={check.get('error')}",
            })

        if overall_ok:
            rows.append({
                'area': 'post_validation_workflow',
                'status': 'suspect',
                'hint': 'If GitHub Actions still failed after validation, likely cause is artifact commit/push race or upload-artifact step, not model/data logic.',
            })

    except Exception as exc:
        rows.append({
            'area': 'status_read',
            'status': 'failed',
            'hint': repr(exc),
        })
else:
    rows.append({
        'area': 'validation',
        'status': 'unknown',
        'hint': 'free_data_status.json is not available.',
    })

report = pd.DataFrame(rows)
expected_columns = ['area', 'status', 'hint']
for col in expected_columns:
    if col not in report.columns:
        report[col] = None
report = report[expected_columns]
report.to_csv(output_dir / 'workflow_failure_hint_report.csv', index=False)

for _, row in report.iterrows():
    markdown.append(f"- {row['area']} | {row['status']} | {row['hint']}")

(output_dir / 'workflow_failure_hint_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report)
