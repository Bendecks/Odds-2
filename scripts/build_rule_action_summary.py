from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
rules_path = output_dir / 'signal_suppression_rules.csv'

markdown = [
    '# Rule Action Summary',
    '',
]

expected_columns = ['action', 'rules', 'targets']

if not rules_path.exists() or rules_path.stat().st_size == 0:
    report = pd.DataFrame(columns=expected_columns)
    markdown.append('No rule file available.')
else:
    try:
        rules = pd.read_csv(rules_path)
    except Exception:
        rules = pd.DataFrame()

    if len(rules) == 0:
        report = pd.DataFrame(columns=expected_columns)
        markdown.append('No active rules.')
    else:
        rows = []
        for action, subset in rules.groupby('action', dropna=False):
            targets = ', '.join(subset['target'].astype(str).tolist()) if 'target' in subset.columns else ''
            rows.append({
                'action': action,
                'rules': int(len(subset)),
                'targets': targets,
            })
            markdown.append(f'- {action}: {len(subset)} rule(s) | targets={targets}')
        report = pd.DataFrame(rows)

for col in expected_columns:
    if col not in report.columns:
        report[col] = None
report = report[expected_columns]
report.to_csv(output_dir / 'rule_action_summary.csv', index=False)
(output_dir / 'rule_action_summary.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report)
