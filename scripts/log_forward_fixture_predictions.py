import json
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
log_dir = Path('data/predictions')
log_dir.mkdir(parents=True, exist_ok=True)

predictions_path = output_dir / 'forward_fixture_predictions.csv'
log_path = log_dir / 'forward_fixture_prediction_log.jsonl'

expected_columns = [
    'prediction_id', 'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team',
    'league', 'sample_phase', 'expected_home_goals', 'expected_away_goals',
    'home_win_probability', 'draw_probability', 'away_win_probability',
    'fair_home_odds', 'fair_draw_odds', 'fair_away_odds', 'model_source',
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=expected_columns)
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame(columns=expected_columns)


def safe_read_jsonl(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=expected_columns)
    try:
        return pd.read_json(path, lines=True)
    except Exception:
        return pd.DataFrame(columns=expected_columns)


current = safe_read_csv(predictions_path)
for col in expected_columns:
    if col not in current.columns:
        current[col] = None
current = current[expected_columns]

existing = safe_read_jsonl(log_path)
existing_ids = set(existing['prediction_id'].astype(str).tolist()) if len(existing) and 'prediction_id' in existing.columns else set()

new_rows = current[~current['prediction_id'].astype(str).isin(existing_ids)].copy() if len(current) else pd.DataFrame(columns=expected_columns)

if len(new_rows):
    with log_path.open('a', encoding='utf-8') as handle:
        for record in new_rows.to_dict(orient='records'):
            handle.write(json.dumps(record, ensure_ascii=False, default=str) + '\n')

full_log = safe_read_jsonl(log_path)
for col in expected_columns:
    if col not in full_log.columns:
        full_log[col] = None
full_log = full_log[expected_columns]
full_log.to_csv(output_dir / 'forward_fixture_prediction_log_latest.csv', index=False)

summary = {
    'current_forward_fixture_predictions': int(len(current)),
    'new_forward_fixture_predictions_logged': int(len(new_rows)),
    'total_forward_fixture_predictions_logged': int(len(full_log)),
    'log_type': 'probability_only_no_market_prices',
}
pd.DataFrame([summary]).to_csv(output_dir / 'forward_fixture_prediction_log_status.csv', index=False)

markdown = [
    '# Forward Fixture Prediction Log',
    '',
    'Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.',
    '',
    f"Current forward fixture predictions: {summary['current_forward_fixture_predictions']}",
    f"New forward fixture predictions logged: {summary['new_forward_fixture_predictions_logged']}",
    f"Total forward fixture predictions logged: {summary['total_forward_fixture_predictions_logged']}",
    f"Log type: {summary['log_type']}",
    '',
]

if len(full_log):
    for _, row in full_log.tail(20).iterrows():
        markdown.append(
            f"- {row.get('match_date')} {row.get('match_time')} | {row.get('home_team')} vs {row.get('away_team')} | "
            f"H={row.get('home_win_probability')} D={row.get('draw_probability')} A={row.get('away_win_probability')}"
        )
else:
    markdown.append('No forward fixture probability predictions logged yet.')

(output_dir / 'forward_fixture_prediction_log.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
