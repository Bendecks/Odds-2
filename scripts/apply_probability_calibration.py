from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
prediction_path = output_dir / 'poisson_predictions.parquet'
clv_band_path = output_dir / 'clv_band_report.csv'

markets = [
    ('home_win_probability', 'fair_home_odds'),
    ('draw_probability', 'fair_draw_odds'),
    ('away_win_probability', 'fair_away_odds'),
]


def probability_band(probability: float) -> str:
    if pd.isna(probability):
        return 'unknown'
    for start, end in [(0.00, 0.35), (0.35, 0.45), (0.45, 0.50), (0.50, 0.55), (0.55, 1.00)]:
        if start <= float(probability) < end:
            return f'{start:.2f}-{end:.2f}'
    return 'unknown'


def load_band_multipliers() -> dict:
    if not clv_band_path.exists() or clv_band_path.stat().st_size == 0:
        return {}
    try:
        bands = pd.read_csv(clv_band_path)
    except Exception:
        return {}

    if len(bands) == 0:
        return {}

    bands['rows'] = pd.to_numeric(bands.get('rows'), errors='coerce').fillna(0)
    bands['avg_clv_delta'] = pd.to_numeric(bands.get('avg_clv_delta'), errors='coerce')
    bands['beat_closing_line_rate'] = pd.to_numeric(bands.get('beat_closing_line_rate'), errors='coerce')

    result = {}
    for _, row in bands.iterrows():
        band = str(row.get('probability_band'))
        rows = int(row.get('rows', 0)) if pd.notna(row.get('rows')) else 0
        avg_clv = row.get('avg_clv_delta')
        beat_rate = row.get('beat_closing_line_rate')

        multiplier = 1.0
        action = 'none'

        if rows >= 5 and pd.notna(avg_clv) and float(avg_clv) < -0.75:
            multiplier = 0.88
            action = 'strong_shrink'
        elif rows >= 5 and pd.notna(avg_clv) and float(avg_clv) < -0.25:
            multiplier = 0.94
            action = 'mild_shrink'
        elif rows >= 5 and pd.notna(beat_rate) and float(beat_rate) < 0.40:
            multiplier = 0.95
            action = 'mild_shrink'
        elif rows >= 10 and pd.notna(beat_rate) and float(beat_rate) >= 0.55 and pd.notna(avg_clv) and float(avg_clv) > -0.10:
            multiplier = 1.01
            action = 'monitor_hold'

        result[band] = {
            'multiplier': multiplier,
            'action': action,
            'rows': rows,
            'avg_clv_delta': round(float(avg_clv), 4) if pd.notna(avg_clv) else None,
            'beat_closing_line_rate': round(float(beat_rate), 4) if pd.notna(beat_rate) else None,
        }

    return result


band_rules = load_band_multipliers()
report_rows = []

if prediction_path.exists():
    predictions = pd.read_parquet(prediction_path)
else:
    predictions = pd.DataFrame()

if len(predictions):
    calibrated = predictions.copy()

    for idx, row in calibrated.iterrows():
        adjusted = []

        for prob_col, _ in markets:
            raw_probability = pd.to_numeric(row.get(prob_col), errors='coerce')
            if pd.isna(raw_probability):
                raw_probability = 0.0

            band = probability_band(raw_probability)
            rule = band_rules.get(band, {'multiplier': 1.0, 'action': 'none'})
            value = float(raw_probability) * float(rule.get('multiplier', 1.0))
            adjusted.append(value)

            report_rows.append({
                'home_team': row.get('home_team'),
                'away_team': row.get('away_team'),
                'probability_column': prob_col,
                'raw_probability': round(float(raw_probability), 6),
                'probability_band': band,
                'calibration_action': rule.get('action', 'none'),
                'multiplier': rule.get('multiplier', 1.0),
            })

        total = sum(adjusted)
        if total <= 0:
            adjusted = [1 / 3, 1 / 3, 1 / 3]
        else:
            adjusted = [value / total for value in adjusted]

        for (prob_col, odds_col), value in zip(markets, adjusted):
            calibrated.at[idx, prob_col] = round(float(value), 4)
            calibrated.at[idx, odds_col] = round(1 / float(value), 2) if value > 0 else None

    calibrated.to_parquet(prediction_path, index=False)
    calibrated.to_csv(output_dir / 'poisson_predictions.csv', index=False)
else:
    calibrated = predictions

adjustments = pd.DataFrame(report_rows)
expected_adjustment_cols = [
    'home_team', 'away_team', 'probability_column', 'raw_probability',
    'probability_band', 'calibration_action', 'multiplier',
]
for col in expected_adjustment_cols:
    if col not in adjustments.columns:
        adjustments[col] = None
adjustments = adjustments[expected_adjustment_cols]
adjustments.to_csv(output_dir / 'probability_calibration_adjustments.csv', index=False)

if len(adjustments):
    summary = adjustments.groupby(['probability_band', 'calibration_action']).size().reset_index(name='adjustments')
else:
    summary = pd.DataFrame(columns=['probability_band', 'calibration_action', 'adjustments'])
summary.to_csv(output_dir / 'probability_calibration_rules.csv', index=False)

markdown = [
    '# Probability Calibration Layer',
    '',
    f'Prediction rows: {len(predictions)}',
    f'Band rules available: {len(band_rules)}',
    '',
]

if len(summary):
    for _, item in summary.iterrows():
        markdown.append(f"- {item['probability_band']} | {item['calibration_action']} | adjustments={item['adjustments']}")
else:
    markdown.append('No probability adjustments generated.')

(output_dir / 'probability_calibration_layer.md').write_text('\n'.join(markdown), encoding='utf-8')

print('\n'.join(markdown))
