from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'

markdown = [
    '# Strategy Risk Report',
    '',
]

if not settled_path.exists():
    markdown.append('No settled predictions available.')
    (output_dir / 'strategy_risk_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'strategy_risk_report.csv', index=False)
    raise SystemExit(0)

settled = pd.read_parquet(settled_path)

if len(settled) == 0:
    markdown.append('Settled predictions dataset is empty.')
    (output_dir / 'strategy_risk_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'strategy_risk_report.csv', index=False)
    raise SystemExit(0)

if 'won' not in settled.columns:
    settled['won'] = False

if 'roi_units' not in settled.columns:
    settled['roi_units'] = 0.0

settled['won'] = settled['won'].fillna(False).astype(bool)
settled['roi_units'] = pd.to_numeric(settled['roi_units'], errors='coerce').fillna(0)

loss_streak = 0
max_loss_streak = 0

for won in settled['won']:
    if won:
        loss_streak = 0
    else:
        loss_streak += 1
        max_loss_streak = max(max_loss_streak, loss_streak)

volatility = round(float(settled['roi_units'].std()), 4) if len(settled) else 0
avg_roi = round(float(settled['roi_units'].mean()), 4) if len(settled) else 0

risk_level = 'high'

if max_loss_streak <= 4 and volatility < 0.9:
    risk_level = 'controlled'
elif max_loss_streak <= 7 and volatility < 1.2:
    risk_level = 'moderate'

summary = {
    'max_loss_streak': int(max_loss_streak),
    'volatility': volatility,
    'avg_roi_per_bet': avg_roi,
    'risk_level': risk_level,
    'bets': int(len(settled)),
}

pd.DataFrame([summary]).to_csv(output_dir / 'strategy_risk_report.csv', index=False)

markdown.extend([
    f"Max loss streak: {summary['max_loss_streak']}",
    f"Volatility: {summary['volatility']}",
    f"Average ROI per bet: {summary['avg_roi_per_bet']}",
    f"Risk level: {summary['risk_level']}",
    f"Settled bets: {summary['bets']}",
])

(output_dir / 'strategy_risk_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
