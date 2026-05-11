import runpy
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
log_path = Path('data/predictions/paper_test_log.jsonl')

FORWARD_PHASES = {'paper_forward_test', 'live_forward_snapshot', 'upcoming_fixture', 'automatic_forward_price_proxy'}

expected_columns = [
    'snapshot_id', 'prediction_id', 'match_date', 'home_team', 'away_team', 'sample_phase',
    'selection', 'market_odds', 'probability', 'ev', 'paper_test_tier',
    'paper_test_score', 'paper_test_reason', 'suppression_action'
]


def empty_frame() -> pd.DataFrame:
    return pd.DataFrame(columns=expected_columns)


def norm_team(value) -> str:
    text = str(value or '').lower().strip()
    for token in ['hotspur', 'united', 'utd', 'town', 'city', 'fc', 'afc', 'cf', '.', ',', '&']:
        text = text.replace(token, ' ')
    return ' '.join(text.split())


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', dayfirst=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(value, errors='coerce')
    if pd.isna(parsed):
        return str(value or '')
    return parsed.date().isoformat()


if log_path.exists() and log_path.stat().st_size > 0:
    try:
        raw = pd.read_json(log_path, lines=True)
    except Exception:
        raw = empty_frame()
else:
    raw = empty_frame()

for col in expected_columns:
    if col not in raw.columns:
        raw[col] = None

if len(raw):
    raw['sample_phase'] = raw['sample_phase'].fillna('unknown').astype(str)
    valid = raw[raw['sample_phase'].isin(FORWARD_PHASES)].copy()
    invalid = raw[~raw['sample_phase'].isin(FORWARD_PHASES)].copy()
else:
    valid = empty_frame()
    invalid = empty_frame()

if len(valid):
    valid['dedupe_match_date'] = valid['match_date'].apply(parse_date)
    valid['dedupe_home'] = valid['home_team'].apply(norm_team)
    valid['dedupe_away'] = valid['away_team'].apply(norm_team)
    valid['dedupe_selection'] = valid['selection'].astype(str).str.lower().str.strip()
    valid['paper_test_score_num'] = pd.to_numeric(valid['paper_test_score'], errors='coerce').fillna(0)
    valid_deduped = (
        valid.sort_values(['paper_test_score_num', 'ev'], ascending=False)
        .drop_duplicates(['dedupe_match_date', 'dedupe_home', 'dedupe_away', 'dedupe_selection'], keep='first')
        .copy()
    )
    valid_deduped = valid_deduped.drop(columns=['dedupe_match_date', 'dedupe_home', 'dedupe_away', 'dedupe_selection', 'paper_test_score_num'], errors='ignore')
else:
    valid_deduped = empty_frame()

valid_export = valid.drop(columns=['dedupe_match_date', 'dedupe_home', 'dedupe_away', 'dedupe_selection', 'paper_test_score_num'], errors='ignore')
valid_export = valid_export[expected_columns]
invalid = invalid[expected_columns]
valid_deduped = valid_deduped[expected_columns]

valid_export.to_csv(output_dir / 'paper_test_log_latest.csv', index=False)
valid_deduped.to_csv(output_dir / 'paper_test_log_deduped.csv', index=False)
invalid.to_csv(output_dir / 'invalid_paper_test_log_rows.csv', index=False)

proxy_rows = int((valid_export['sample_phase'] == 'automatic_forward_price_proxy').sum()) if len(valid_export) else 0
deduped_proxy_rows = int((valid_deduped['sample_phase'] == 'automatic_forward_price_proxy').sum()) if len(valid_deduped) else 0
summary = {
    'raw_log_rows': int(len(raw)),
    'valid_forward_log_rows': int(len(valid_export)),
    'deduped_forward_log_rows': int(len(valid_deduped)),
    'duplicate_forward_log_rows': int(max(len(valid_export) - len(valid_deduped), 0)),
    'valid_proxy_observation_rows': proxy_rows,
    'deduped_proxy_observation_rows': deduped_proxy_rows,
    'invalid_historical_proxy_log_rows': int(len(invalid)),
    'has_valid_forward_log': bool(len(valid_export) > 0),
}

pd.DataFrame([summary]).to_csv(output_dir / 'paper_test_log_status.csv', index=False)

markdown = [
    '# Paper Test Log Status',
    '',
    f"Raw log rows: {summary['raw_log_rows']}",
    f"Valid forward/proxy log rows: {summary['valid_forward_log_rows']}",
    f"Deduped forward/proxy observation rows: {summary['deduped_forward_log_rows']}",
    f"Duplicate forward/proxy log rows: {summary['duplicate_forward_log_rows']}",
    f"Valid automatic proxy observation rows: {summary['valid_proxy_observation_rows']}",
    f"Deduped automatic proxy observation rows: {summary['deduped_proxy_observation_rows']}",
    f"Invalid historical/proxy log rows excluded: {summary['invalid_historical_proxy_log_rows']}",
    f"Has valid forward log: {summary['has_valid_forward_log']}",
    '',
]

if len(valid_deduped):
    markdown.extend(['## Deduped valid rows', ''])
    for _, row in valid_deduped.tail(20).iterrows():
        markdown.append(
            f"- {row.get('match_date')} | {row.get('home_team')} vs {row.get('away_team')} | "
            f"selection={row.get('selection')} | phase={row.get('sample_phase')} | tier={row.get('paper_test_tier')} | score={row.get('paper_test_score')}"
        )

if len(valid_export):
    markdown.extend(['', '## Raw valid rows', ''])
    for _, row in valid_export.tail(20).iterrows():
        markdown.append(
            f"- {row.get('match_date')} | {row.get('home_team')} vs {row.get('away_team')} | "
            f"selection={row.get('selection')} | phase={row.get('sample_phase')} | tier={row.get('paper_test_tier')}"
        )

if len(invalid):
    markdown.extend(['', '## Invalid rows excluded', ''])
    for _, row in invalid.head(20).iterrows():
        markdown.append(
            f"- {row.get('match_date')} | {row.get('home_team')} vs {row.get('away_team')} | phase={row.get('sample_phase')}"
        )

(output_dir / 'paper_test_log_status.md').write_text('\n'.join(markdown), encoding='utf-8')

quality_script = Path('scripts/build_proxy_observation_quality_report.py')
if quality_script.exists():
    try:
        runpy.run_path(str(quality_script), run_name='__main__')
    except Exception as exc:
        print(f'Proxy observation quality report skipped: {exc!r}')

print(summary)
