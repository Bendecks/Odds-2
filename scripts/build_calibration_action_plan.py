from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

calibration_path = output_dir / 'probability_calibration_report.csv'
alignment_path = output_dir / 'market_alignment_report.csv'
clv_path = output_dir / 'clv_trend_report.csv'
gemini_path = output_dir / 'gemini_ai_review.md'

markdown = [
    '# Calibration Action Plan',
    '',
]

issues = []
actions = []

if alignment_path.exists() and alignment_path.stat().st_size > 0:
    try:
        alignment = pd.read_csv(alignment_path)
        if len(alignment):
            gap = alignment.iloc[0].get('average_alignment_gap')
            if pd.notna(gap):
                if gap > 0.14:
                    issues.append(f'Market alignment is weak: gap={round(float(gap),4)}')
                    actions.append('Increase probability shrinkage and reduce model-market disagreement.')
                elif gap > 0.08:
                    issues.append(f'Market alignment is moderate: gap={round(float(gap),4)}')
                    actions.append('Keep shrinkage active and evaluate calibration by probability band.')
                else:
                    issues.append(f'Market alignment is acceptable: gap={round(float(gap),4)}')
    except Exception as exc:
        issues.append(f'Could not read market alignment report: {exc}')

if clv_path.exists() and clv_path.stat().st_size > 0:
    try:
        clv = pd.read_csv(clv_path)
        if len(clv):
            beat_rate = clv.iloc[0].get('beat_closing_line_rate')
            avg_delta = clv.iloc[0].get('avg_clv_delta')
            if pd.notna(beat_rate):
                if beat_rate < 0.50:
                    issues.append(f'CLV beat rate below target: {round(float(beat_rate),4)}')
                    actions.append('Prioritize CLV-improving calibration before any real-money use.')
                else:
                    issues.append(f'CLV beat rate acceptable/positive: {round(float(beat_rate),4)}')
            if pd.notna(avg_delta):
                issues.append(f'Average CLV delta: {round(float(avg_delta),4)}')
    except Exception as exc:
        issues.append(f'Could not read CLV trend report: {exc}')

if gemini_path.exists():
    gemini_text = gemini_path.read_text(encoding='utf-8')
    if 'Platt' in gemini_text or 'isotonic' in gemini_text:
        actions.append('Evaluate simple calibration layer before adding more model features.')

if not issues:
    issues.append('No major calibration issue detected or insufficient data.')

if not actions:
    actions.append('Continue observation and collect more settled predictions.')

markdown.extend([
    '## Current calibration issues',
    '',
])

for issue in issues:
    markdown.append(f'- {issue}')

markdown.extend([
    '',
    '## Next actions',
    '',
])

for action in dict.fromkeys(actions):
    markdown.append(f'- {action}')

summary = {
    'issues': len(issues),
    'actions': len(set(actions)),
    'top_action': list(dict.fromkeys(actions))[0],
}

pd.DataFrame([summary]).to_csv(output_dir / 'calibration_action_plan.csv', index=False)
(output_dir / 'calibration_action_plan.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
