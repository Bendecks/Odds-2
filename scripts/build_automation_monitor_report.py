import os
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

run_number = os.getenv('GITHUB_RUN_NUMBER', 'local')
run_id = os.getenv('GITHUB_RUN_ID', 'local')
run_attempt = os.getenv('GITHUB_RUN_ATTEMPT', 'local')
sha = os.getenv('GITHUB_SHA', 'local')
event_name = os.getenv('GITHUB_EVENT_NAME', 'local')
ref = os.getenv('GITHUB_REF_NAME', 'local')

now = datetime.now(timezone.utc).isoformat()

status = {
    'generated_at_utc': now,
    'github_run_number': run_number,
    'github_run_id': run_id,
    'github_run_attempt': run_attempt,
    'github_sha': sha,
    'github_event_name': event_name,
    'github_ref': ref,
    'scheduled_monitoring_enabled': True,
    'schedule': '0 */12 * * *',
    'expected_frequency_hours': 12,
}

pd.DataFrame([status]).to_csv(output_dir / 'automation_monitor_report.csv', index=False)

markdown = [
    '# Automation Monitor Report',
    '',
    f'Generated UTC: {now}',
    f'GitHub run number: {run_number}',
    f'GitHub run id: {run_id}',
    f'GitHub run attempt: {run_attempt}',
    f'GitHub event: {event_name}',
    f'GitHub SHA: {sha}',
    f'GitHub ref: {ref}',
    '',
    '## Schedule',
    '',
    '- Scheduled monitoring: enabled',
    '- Cron: `0 */12 * * *`',
    '- Expected frequency: every 12 hours',
    '',
    '## Interpretation',
    '',
]

if event_name == 'schedule':
    markdown.append('This was an automatic scheduled monitoring run.')
elif event_name == 'push':
    markdown.append('This was triggered by a code/data change.')
elif event_name == 'workflow_dispatch':
    markdown.append('This was manually triggered.')
else:
    markdown.append('Run trigger type is non-standard or local.')

(output_dir / 'automation_monitor_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(status)
