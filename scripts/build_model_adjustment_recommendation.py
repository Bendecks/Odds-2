from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
prob_path = output_dir / 'probability_band_report.csv'
league_path = output_dir / 'league_performance_report.csv'
clv_path = output_dir / 'clv_trend_report.csv'

markdown = [
    '# Model Adjustment Recommendation',
    '',
]

recommendations = []
flags = []


def safe_read(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()

prob = safe_read(prob_path)
if len(prob):
    prob['avg_roi'] = pd.to_numeric(prob.get('avg_roi'), errors='coerce')
    prob['avg_probability'] = pd.to_numeric(prob.get('avg_probability'), errors='coerce')
    prob['actual_win_rate'] = pd.to_numeric(prob.get('actual_win_rate'), errors='coerce')

    high_prob = prob[prob['avg_probability'] >= 0.50]
    low_prob = prob[prob['avg_probability'] < 0.50]

    if len(high_prob) and high_prob['avg_roi'].mean() < 0:
        flags.append('High probability bands are currently negative ROI.')
        recommendations.append('Reduce confidence in favorites and add extra shrinkage above 0.50 probability.')

    if len(low_prob) and low_prob['avg_roi'].mean() > 0:
        flags.append('Lower probability bands are currently performing better.')
        recommendations.append('Investigate underdog/moderate-price markets before expanding favorite exposure.')

    prob['calibration_gap'] = (prob['actual_win_rate'] - prob['avg_probability']).abs()

    if prob['calibration_gap'].mean() > 0.08:
        flags.append('Probability calibration gap is material.')
        recommendations.append('Prioritize probability calibration before adding complex model features.')

league = safe_read(league_path)
if len(league):
    league['avg_roi_per_bet'] = pd.to_numeric(league.get('avg_roi_per_bet'), errors='coerce')
    best = league.sort_values('avg_roi_per_bet', ascending=False).head(1)
    worst = league.sort_values('avg_roi_per_bet', ascending=True).head(1)

    if len(best):
        flags.append(f"Best league so far: {best.iloc[0].get('league')} avg_roi={best.iloc[0].get('avg_roi_per_bet')}")
    if len(worst):
        flags.append(f"Worst league so far: {worst.iloc[0].get('league')} avg_roi={worst.iloc[0].get('avg_roi_per_bet')}")

clv = safe_read(clv_path)
if len(clv):
    beat_rate = clv.iloc[0].get('beat_closing_line_rate')
    if pd.notna(beat_rate) and float(beat_rate) < 0.50:
        flags.append(f'CLV beat rate below 50%: {round(float(beat_rate),4)}')
        recommendations.append('Treat all recommendations as paper-tracking until CLV improves above neutral.')

if not recommendations:
    recommendations.append('Continue collecting data before changing model behavior.')

markdown.extend(['## Flags', ''])
for flag in flags or ['No major flags detected.']:
    markdown.append(f'- {flag}')

markdown.extend(['', '## Recommended model changes', ''])
for rec in dict.fromkeys(recommendations):
    markdown.append(f'- {rec}')

summary = {
    'flags': len(flags),
    'recommendations': len(set(recommendations)),
    'top_recommendation': list(dict.fromkeys(recommendations))[0],
}

pd.DataFrame([summary]).to_csv(output_dir / 'model_adjustment_recommendation.csv', index=False)
(output_dir / 'model_adjustment_recommendation.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
