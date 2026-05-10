from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
settled_path = output_dir / 'settled_predictions.parquet'

markdown = [
    '# Bankroll Simulation Report',
    '',
]

if not settled_path.exists():
    markdown.append('No settled predictions available.')
    (output_dir / 'bankroll_simulation_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'bankroll_simulation_report.csv', index=False)
    raise SystemExit(0)

settled = pd.read_parquet(settled_path)

if len(settled) == 0:
    markdown.append('Settled predictions dataset is empty.')
    (output_dir / 'bankroll_simulation_report.md').write_text('\n'.join(markdown), encoding='utf-8')
    pd.DataFrame().to_csv(output_dir / 'bankroll_simulation_report.csv', index=False)
    raise SystemExit(0)

if 'roi_units' not in settled.columns:
    settled['roi_units'] = 0.0

settled['roi_units'] = pd.to_numeric(settled['roi_units'], errors='coerce').fillna(0)

bankroll = 100.0
peak = bankroll
max_drawdown = 0.0
curve = []

for idx, row in settled.reset_index(drop=True).iterrows():
    bankroll += float(row['roi_units'])
    peak = max(peak, bankroll)

    drawdown = peak - bankroll
    max_drawdown = max(max_drawdown, drawdown)

    curve.append({
        'bet_number': idx + 1,
        'bankroll': round(bankroll, 4),
        'drawdown': round(drawdown, 4),
    })

curve_df = pd.DataFrame(curve)
curve_df.to_csv(output_dir / 'bankroll_curve.csv', index=False)

summary = {
    'starting_bankroll': 100.0,
    'ending_bankroll': round(bankroll, 4),
    'profit_units': round(bankroll - 100.0, 4),
    'roi_percent': round(((bankroll - 100.0) / 100.0) * 100, 4),
    'max_drawdown': round(max_drawdown, 4),
    'bets': int(len(settled)),
}

pd.DataFrame([summary]).to_csv(output_dir / 'bankroll_simulation_report.csv', index=False)

markdown.extend([
    f"Starting bankroll: {summary['starting_bankroll']}",
    f"Ending bankroll: {summary['ending_bankroll']}",
    f"Profit units: {summary['profit_units']}",
    f"ROI percent: {summary['roi_percent']}",
    f"Max drawdown: {summary['max_drawdown']}",
    f"Settled bets: {summary['bets']}",
])

(output_dir / 'bankroll_simulation_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
