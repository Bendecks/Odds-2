from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
clv_band_path = output_dir / 'clv_band_report.csv'
league_path = output_dir / 'league_performance_report.csv'

rules = []
markdown = [
    '# Signal Suppression Rules',
    '',
    'Research-only guardrails generated from settled proxy/paper diagnostics.',
    '',
]


def safe_read(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


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
            rules.append({
                'rule_type': 'probability_band',
                'target': band,
                'action': 'suppress',
                'reason': f'avg_clv_delta={round(float(avg_clv),4)} with rows={rows}',
            })
        elif rows >= 5 and pd.notna(beat_rate) and float(beat_rate) < 0.40:
            rules.append({
                'rule_type': 'probability_band',
                'target': band,
                'action': 'downweight',
                'reason': f'beat_closing_line_rate={round(float(beat_rate),4)} with rows={rows}',
            })
        elif rows >= 10 and pd.notna(beat_rate) and float(beat_rate) >= 0.55 and pd.notna(avg_clv) and float(avg_clv) > -0.10:
            # This is not an approval signal. It only marks the band as worth observing
            # while the whole system remains research-only.
            rules.append({
                'rule_type': 'probability_band',
                'target': band,
                'action': 'monitor',
                'reason': f'healthier watchlist band: avg_clv_delta={round(float(avg_clv),4)}, beat_rate={round(float(beat_rate),4)}, rows={rows}',
            })

league = safe_read(league_path)
if len(league):
    league['avg_roi_per_bet'] = pd.to_numeric(league.get('avg_roi_per_bet'), errors='coerce')
    league['bets'] = pd.to_numeric(league.get('bets'), errors='coerce').fillna(0)

    for _, row in league.iterrows():
        bets = int(row.get('bets', 0)) if pd.notna(row.get('bets')) else 0
        avg_roi = row.get('avg_roi_per_bet')
        league_name = str(row.get('league', 'unknown'))

        if bets >= 30 and pd.notna(avg_roi) and float(avg_roi) < -0.08:
            rules.append({
                'rule_type': 'league',
                'target': league_name,
                'action': 'downweight',
                'reason': f'avg_roi_per_bet={round(float(avg_roi),4)} with bets={bets}',
            })

rules_df = pd.DataFrame(rules)
expected_columns = ['rule_type', 'target', 'action', 'reason']
for col in expected_columns:
    if col not in rules_df.columns:
        rules_df[col] = None
rules_df = rules_df[expected_columns]

rules_df.to_csv(output_dir / 'signal_suppression_rules.csv', index=False)

if len(rules_df) == 0:
    markdown.append('No suppression rules triggered yet.')
else:
    for _, row in rules_df.iterrows():
        markdown.append(
            f"- {row['rule_type']}={row['target']} | action={row['action']} | {row['reason']}"
        )

(output_dir / 'signal_suppression_rules.md').write_text('\n'.join(markdown), encoding='utf-8')

print(rules_df)
