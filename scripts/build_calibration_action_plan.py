from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

calibration_path = output_dir / 'probability_calibration_report.csv'
alignment_path = output_dir / 'market_alignment_report.csv'
clv_path = output_dir / 'clv_trend_report.csv'
clv_band_path = output_dir / 'clv_band_report.csv'
suppression_path = output_dir / 'signal_suppression_rules.csv'
gemini_path = output_dir / 'gemini_ai_review.md'

markdown = [
    '# Calibration Action Plan',
    '',
]

issues = []
actions = []
protected_zones = []
suppressed_zones = []


def safe_read(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


alignment = safe_read(alignment_path)
if len(alignment):
    gap = alignment.iloc[0].get('average_alignment_gap')
    if pd.notna(gap):
        if float(gap) > 0.14:
            issues.append(f'Market alignment is weak: gap={round(float(gap),4)}')
            actions.append('Increase probability shrinkage and reduce model-market disagreement.')
        elif float(gap) > 0.08:
            issues.append(f'Market alignment is moderate: gap={round(float(gap),4)}')
            actions.append('Keep shrinkage active and evaluate calibration by probability band.')
        else:
            issues.append(f'Market alignment is acceptable: gap={round(float(gap),4)}')

clv = safe_read(clv_path)
if len(clv):
    beat_rate = clv.iloc[0].get('beat_closing_line_rate')
    avg_delta = clv.iloc[0].get('avg_clv_delta')
    if pd.notna(beat_rate):
        if float(beat_rate) < 0.50:
            issues.append(f'CLV beat rate below target: {round(float(beat_rate),4)}')
            actions.append('Prioritize CLV-improving calibration before any real-money use.')
        else:
            issues.append(f'CLV beat rate acceptable/positive: {round(float(beat_rate),4)}')
    if pd.notna(avg_delta):
        issues.append(f'Average CLV delta: {round(float(avg_delta),4)}')
        if float(avg_delta) < -0.25:
            actions.append('Reduce EV aggressiveness and avoid low-probability false edges.')

clv_band = safe_read(clv_band_path)
if len(clv_band):
    clv_band['avg_clv_delta'] = pd.to_numeric(clv_band.get('avg_clv_delta'), errors='coerce')
    clv_band['beat_closing_line_rate'] = pd.to_numeric(clv_band.get('beat_closing_line_rate'), errors='coerce')
    clv_band['rows'] = pd.to_numeric(clv_band.get('rows'), errors='coerce').fillna(0)

    for _, row in clv_band.iterrows():
        band = str(row.get('probability_band'))
        rows = int(row.get('rows', 0)) if pd.notna(row.get('rows')) else 0
        avg_clv = row.get('avg_clv_delta')
        beat_rate = row.get('beat_closing_line_rate')

        if rows >= 5 and pd.notna(avg_clv) and float(avg_clv) < -0.25:
            suppressed_zones.append(band)
            issues.append(f'CLV-toxic probability band: {band} avg_clv={round(float(avg_clv),4)} rows={rows}')
        elif rows >= 5 and pd.notna(beat_rate) and float(beat_rate) >= 0.50 and pd.notna(avg_clv) and float(avg_clv) > -0.10:
            protected_zones.append(band)
            issues.append(f'Healthier probability band: {band} avg_clv={round(float(avg_clv),4)} beat_rate={round(float(beat_rate),4)} rows={rows}')

    if suppressed_zones:
        actions.append('Keep suppressing CLV-toxic probability bands in candidate selection.')
    if protected_zones:
        actions.append('Use healthier probability bands as paper-watchlist zones, not betting recommendations.')

suppression = safe_read(suppression_path)
if len(suppression):
    actions.append(f'Current suppression rules active: {len(suppression)}.')

if gemini_path.exists():
    gemini_text = gemini_path.read_text(encoding='utf-8')
    if 'Platt' in gemini_text or 'isotonic' in gemini_text:
        actions.append('Evaluate simple calibration layer before adding more model features.')

if not issues:
    issues.append('No major calibration issue detected or insufficient data.')

if not actions:
    actions.append('Continue observation and collect more settled predictions.')

markdown.extend(['## Current calibration issues', ''])
for issue in issues:
    markdown.append(f'- {issue}')

markdown.extend(['', '## Suppressed zones', ''])
for zone in suppressed_zones or ['none']:
    markdown.append(f'- {zone}')

markdown.extend(['', '## Healthier watchlist zones', ''])
for zone in protected_zones or ['none']:
    markdown.append(f'- {zone}')

markdown.extend(['', '## Next actions', ''])
for action in dict.fromkeys(actions):
    markdown.append(f'- {action}')

summary = {
    'issues': len(issues),
    'actions': len(set(actions)),
    'suppressed_zones': len(set(suppressed_zones)),
    'healthier_watchlist_zones': len(set(protected_zones)),
    'top_action': list(dict.fromkeys(actions))[0],
}

pd.DataFrame([summary]).to_csv(output_dir / 'calibration_action_plan.csv', index=False)
(output_dir / 'calibration_action_plan.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
