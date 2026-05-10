from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'
clv_path = output_dir / 'clv_results.parquet'

markdown = [
    '# Sample Phase Performance Report',
    '',
    'Separates historical proxy research from paper forward-testing diagnostics.',
    '',
]

expected_columns = [
    'sample_phase',
    'settled_rows',
    'win_rate',
    'roi_units',
    'avg_roi_per_bet',
    'clv_rows',
    'avg_clv_delta',
    'beat_closing_line_rate',
    'recommended_usage',
]


def safe_read_parquet(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_parquet(path)
    except Exception:
        return pd.DataFrame()


settled = safe_read_parquet(settled_path)
clv = safe_read_parquet(clv_path)

if len(settled) and 'sample_phase' not in settled.columns:
    settled['sample_phase'] = 'historical_proxy_research'
if len(clv) and 'sample_phase' not in clv.columns:
    clv['sample_phase'] = 'historical_proxy_research'

rows = []
phases = set()
if len(settled):
    phases.update(settled['sample_phase'].fillna('unknown').astype(str).unique())
if len(clv):
    phases.update(clv['sample_phase'].fillna('unknown').astype(str).unique())

for phase in sorted(phases):
    settled_subset = settled[settled['sample_phase'].fillna('unknown').astype(str) == phase].copy() if len(settled) else pd.DataFrame()
    clv_subset = clv[clv['sample_phase'].fillna('unknown').astype(str) == phase].copy() if len(clv) else pd.DataFrame()

    if len(settled_subset):
        if 'won' not in settled_subset.columns:
            settled_subset['won'] = False
        if 'roi_units' not in settled_subset.columns:
            settled_subset['roi_units'] = 0.0
        settled_subset['won'] = settled_subset['won'].fillna(False).astype(bool)
        settled_subset['roi_units'] = pd.to_numeric(settled_subset['roi_units'], errors='coerce').fillna(0)

    if len(clv_subset):
        clv_subset['clv_delta'] = pd.to_numeric(clv_subset.get('clv_delta'), errors='coerce')
        if 'beat_closing_line' not in clv_subset.columns:
            clv_subset['beat_closing_line'] = False

    avg_clv = clv_subset['clv_delta'].dropna().mean() if len(clv_subset) else None
    beat_rate = clv_subset['beat_closing_line'].fillna(False).astype(bool).mean() if len(clv_subset) else None
    avg_roi = settled_subset['roi_units'].mean() if len(settled_subset) else None
    win_rate = settled_subset['won'].mean() if len(settled_subset) else None

    if phase == 'paper_forward_test':
        recommended_usage = 'paper_forward_tracking_only'
    elif phase == 'historical_proxy_research':
        recommended_usage = 'diagnostics_only_not_forward_validation'
    else:
        recommended_usage = 'diagnostics_only'

    rows.append({
        'sample_phase': phase,
        'settled_rows': int(len(settled_subset)),
        'win_rate': round(float(win_rate), 4) if win_rate is not None and pd.notna(win_rate) else None,
        'roi_units': round(float(settled_subset['roi_units'].sum()), 4) if len(settled_subset) else 0,
        'avg_roi_per_bet': round(float(avg_roi), 4) if avg_roi is not None and pd.notna(avg_roi) else None,
        'clv_rows': int(len(clv_subset)),
        'avg_clv_delta': round(float(avg_clv), 4) if avg_clv is not None and pd.notna(avg_clv) else None,
        'beat_closing_line_rate': round(float(beat_rate), 4) if beat_rate is not None and pd.notna(beat_rate) else None,
        'recommended_usage': recommended_usage,
    })

report = pd.DataFrame(rows)
for col in expected_columns:
    if col not in report.columns:
        report[col] = None
report = report[expected_columns]

report.to_csv(output_dir / 'phase_performance_report.csv', index=False)

if len(report) == 0:
    markdown.append('No sample phase data available yet.')
else:
    for _, row in report.iterrows():
        markdown.append(
            f"- {row['sample_phase']} | settled={row['settled_rows']} | "
            f"avg_roi={row['avg_roi_per_bet']} | clv_rows={row['clv_rows']} | "
            f"avg_clv={row['avg_clv_delta']} | beat_rate={row['beat_closing_line_rate']} | "
            f"usage={row['recommended_usage']}"
        )

(output_dir / 'phase_performance_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(report)
