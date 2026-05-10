from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'

markdown = [
    '# Filter Feedback Report',
    '',
]

if not settled_path.exists():
    markdown.append('No settled predictions available.')
    (output_dir / 'filter_feedback_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'filter_feedback_report.csv', index=False)
    raise SystemExit(0)

settled = pd.read_parquet(settled_path)

if len(settled) == 0:
    markdown.append('Settled predictions dataset is empty.')
    (output_dir / 'filter_feedback_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'filter_feedback_report.csv', index=False)
    raise SystemExit(0)

if 'won' not in settled.columns:
    if 'settlement_result' in settled.columns:
        settled['won'] = settled['settlement_result'].astype(str).str.lower().eq('won')
    else:
        settled['won'] = False

settled['won'] = settled['won'].fillna(False).astype(bool)

for col in ['opening_ev', 'ev', 'signal_strength', 'alignment_penalty', 'roi_units']:
    if col not in settled.columns:
        settled[col] = 0.0

for col in ['opening_ev', 'ev', 'signal_strength', 'alignment_penalty', 'roi_units']:
    settled[col] = pd.to_numeric(settled[col], errors='coerce').fillna(0)

settled['effective_ev'] = settled['ev'].fillna(settled['opening_ev']).fillna(0)

summary = {
    'avg_ev_win': round(float(settled.loc[settled['won'], 'effective_ev'].mean()), 4)
    if settled['won'].any()
    else None,
    'avg_ev_loss': round(float(settled.loc[~settled['won'], 'effective_ev'].mean()), 4)
    if (~settled['won']).any()
    else None,
    'avg_signal_win': round(float(settled.loc[settled['won'], 'signal_strength'].mean()), 4)
    if settled['won'].any()
    else None,
    'avg_signal_loss': round(float(settled.loc[~settled['won'], 'signal_strength'].mean()), 4)
    if (~settled['won']).any()
    else None,
    'avg_alignment_penalty_win': round(float(settled.loc[settled['won'], 'alignment_penalty'].mean()), 4)
    if settled['won'].any()
    else None,
    'avg_alignment_penalty_loss': round(float(settled.loc[~settled['won'], 'alignment_penalty'].mean()), 4)
    if (~settled['won']).any()
    else None,
    'roi_total': round(float(settled['roi_units'].sum()), 4),
    'avg_roi': round(float(settled['roi_units'].mean()), 4),
}

pd.DataFrame([summary]).to_csv(output_dir / 'filter_feedback_report.csv', index=False)

markdown.extend([
    f"Average EV (wins): {summary['avg_ev_win']}",
    f"Average EV (losses): {summary['avg_ev_loss']}",
    f"Average signal strength (wins): {summary['avg_signal_win']}",
    f"Average signal strength (losses): {summary['avg_signal_loss']}",
    f"Average alignment penalty (wins): {summary['avg_alignment_penalty_win']}",
    f"Average alignment penalty (losses): {summary['avg_alignment_penalty_loss']}",
    f"Total ROI units: {summary['roi_total']}",
    f"Average ROI per bet: {summary['avg_roi']}",
    '',
    '## Suggested direction',
    '',
])

if summary['avg_alignment_penalty_win'] is not None and summary['avg_alignment_penalty_loss'] is not None:
    if summary['avg_alignment_penalty_win'] < summary['avg_alignment_penalty_loss']:
        markdown.append('- Lower alignment penalties appear healthier.')
    else:
        markdown.append('- Alignment penalty filter may require recalibration.')

if summary['avg_signal_win'] is not None and summary['avg_signal_loss'] is not None:
    if summary['avg_signal_win'] > summary['avg_signal_loss']:
        markdown.append('- Higher signal strength currently correlates positively.')
    else:
        markdown.append('- Signal strength weighting may require review.')

(output_dir / 'filter_feedback_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
