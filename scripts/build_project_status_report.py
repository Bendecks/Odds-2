from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

report_files = {
    'free_data_status': output_dir / 'free_data_status.md',
    'betting_performance': output_dir / 'betting_performance_report.md',
    'model_health': output_dir / 'model_health_report.md',
    'daily_betting_card': output_dir / 'daily_betting_card.md',
    'market_alignment': output_dir / 'market_alignment_report.md',
    'market_proxy_quality': output_dir / 'market_proxy_quality_report.md',
    'probability_distribution': output_dir / 'probability_distribution_report.md',
    'historical_coverage': output_dir / 'historical_coverage_report.md',
}

markdown = [
    '# Project Status Report',
    '',
    'This file is the main AI-readable summary of the current Odds-2 system state.',
    '',
]

for label, path in report_files.items():
    markdown.extend([
        f'## {label}',
        '',
    ])

    if path.exists():
        text = path.read_text(encoding='utf-8').strip()
        # Keep this compact so new chats can read it fast.
        lines = [line for line in text.splitlines() if line.strip()]
        markdown.extend(lines[:25])
    else:
        markdown.append('Report not available yet.')

    markdown.append('')

# Machine-readable simple status.
status = {
    'reports_checked': len(report_files),
    'reports_available': sum(1 for path in report_files.values() if path.exists()),
}

pd.DataFrame([status]).to_csv(output_dir / 'project_status_summary.csv', index=False)

(output_dir / 'project_status_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(status)
