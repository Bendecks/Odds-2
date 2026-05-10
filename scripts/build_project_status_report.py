from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

report_files = {
    'free_data_status': output_dir / 'free_data_status.md',
    'betting_performance': output_dir / 'betting_performance_report.md',
    'model_health': output_dir / 'model_health_report.md',
    'daily_betting_card': output_dir / 'daily_betting_card.md',
    'clv_trend': output_dir / 'clv_trend_report.md',
    'clv_probability_bands': output_dir / 'clv_band_report.md',
    'signal_suppression_rules': output_dir / 'signal_suppression_rules.md',
    'rule_action_summary': output_dir / 'rule_action_summary.md',
    'phase_performance': output_dir / 'phase_performance_report.md',
    'model_adjustment': output_dir / 'model_adjustment_recommendation.md',
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
        lines = [line for line in text.splitlines() if line.strip()]
        markdown.extend(lines[:30])
    else:
        markdown.append('Report not available yet.')

    markdown.append('')

status = {
    'reports_checked': len(report_files),
    'reports_available': sum(1 for path in report_files.values() if path.exists()),
    'includes_clv_band_report': (output_dir / 'clv_band_report.md').exists(),
    'includes_signal_suppression_rules': (output_dir / 'signal_suppression_rules.md').exists(),
    'includes_rule_action_summary': (output_dir / 'rule_action_summary.md').exists(),
    'includes_phase_performance': (output_dir / 'phase_performance_report.md').exists(),
}

pd.DataFrame([status]).to_csv(output_dir / 'project_status_summary.csv', index=False)

(output_dir / 'project_status_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(status)
