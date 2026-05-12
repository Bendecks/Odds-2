from pathlib import Path
import re

import pandas as pd

output_dir = Path('output/latest')
raw_dir = Path('data/raw/odds_api_io')
raw_dir.mkdir(parents=True, exist_ok=True)

prices_path = output_dir / 'odds_api_io_forward_prices.csv'
predictions_path = output_dir / 'forward_fixture_predictions.csv'
accepted_path = output_dir / 'odds_api_io_forward_prices.csv'
rejected_path = output_dir / 'odds_api_io_forward_prices_rejected.csv'
summary_path = output_dir / 'odds_api_io_price_quality_summary.csv'
report_path = output_dir / 'odds_api_io_price_quality_report.md'

EXCLUDED_PATTERN = re.compile(
    r'(\bu\s?\d{2}\b|\bunder\s?\d{2}\b|\breserve\b|\breserves\b|\breserver\b|\byouth\b|\bacademy\b|\bb\s?team\b|\bii\b)',
    re.IGNORECASE,
)

price_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'source_name', 'source_type', 'market_home_odds', 'market_draw_odds',
    'market_away_odds', 'price_captured_at_utc', 'source_quality', 'raw_source_url'
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def norm_team(value) -> str:
    text = str(value or '').lower().strip()
    replacements = {
        'lisboa': 'benfica',
        'sl benfica': 'benfica',
        'sp braga': 'braga',
        'sporting braga': 'braga',
        'sc braga': 'braga',
        'rayo vallecano': 'vallecano',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    for token in ['hotspur', 'united', 'utd', 'town', 'city', 'fc', 'afc', 'cf', 'sc', 'sl', '.', ',', '&']:
        text = text.replace(token, ' ')
    return ' '.join(text.split())


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', utc=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(value, errors='coerce')
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def is_youth_or_reserve_match(row) -> bool:
    text = ' '.join([
        str(row.get('home_team') or ''),
        str(row.get('away_team') or ''),
        str(row.get('league') or ''),
    ])
    return bool(EXCLUDED_PATTERN.search(text))


prices = safe_read_csv(prices_path)
predictions = safe_read_csv(predictions_path)

if len(prices):
    for col in price_columns:
        if col not in prices.columns:
            prices[col] = None
    prices = prices[price_columns].copy()
else:
    prices = pd.DataFrame(columns=price_columns)

prediction_keys = set()
if len(predictions):
    for _, row in predictions.iterrows():
        key = (
            parse_date(row.get('match_date')),
            norm_team(row.get('home_team')),
            norm_team(row.get('away_team')),
        )
        if all(key):
            prediction_keys.add(key)

accepted_rows = []
rejected_rows = []
youth_reserve_rejected_rows = 0
for _, row in prices.iterrows():
    direct_key = (
        parse_date(row.get('match_date')),
        norm_team(row.get('home_team')),
        norm_team(row.get('away_team')),
    )
    swapped_key = (
        parse_date(row.get('match_date')),
        norm_team(row.get('away_team')),
        norm_team(row.get('home_team')),
    )
    row_dict = row.to_dict()
    row_dict['quality_direct_key'] = '|'.join([str(x) for x in direct_key])
    row_dict['quality_swapped_key'] = '|'.join([str(x) for x in swapped_key])
    if is_youth_or_reserve_match(row):
        row_dict['quality_status'] = 'rejected_youth_or_reserve_match'
        rejected_rows.append(row_dict)
        youth_reserve_rejected_rows += 1
    elif direct_key in prediction_keys:
        row_dict['quality_status'] = 'accepted_direct_home_away_match'
        accepted_rows.append(row_dict)
    elif swapped_key in prediction_keys:
        row_dict['quality_status'] = 'rejected_swapped_home_away_match'
        rejected_rows.append(row_dict)
    else:
        row_dict['quality_status'] = 'rejected_no_direct_forward_prediction_match'
        rejected_rows.append(row_dict)

accepted = pd.DataFrame(accepted_rows)
rejected = pd.DataFrame(rejected_rows)

for col in price_columns:
    if col not in accepted.columns:
        accepted[col] = None
accepted = accepted[price_columns]
accepted.to_csv(accepted_path, index=False)
accepted.to_csv(raw_dir / 'odds_api_io_forward_prices_quality_accepted.csv', index=False)

if not len(rejected):
    rejected = pd.DataFrame(columns=price_columns + ['quality_direct_key', 'quality_swapped_key', 'quality_status'])
rejected.to_csv(rejected_path, index=False)
rejected.to_csv(raw_dir / 'odds_api_io_forward_prices_quality_rejected.csv', index=False)

summary = {
    'input_price_rows': int(len(prices)),
    'accepted_price_rows': int(len(accepted)),
    'rejected_price_rows': int(len(rejected)),
    'rejected_youth_or_reserve_rows': int(youth_reserve_rejected_rows),
    'forward_prediction_rows': int(len(predictions)),
    'quality_rule': 'accept_only_direct_senior_home_away_match_against_forward_fixture_predictions',
}
pd.DataFrame([summary]).to_csv(summary_path, index=False)

markdown = [
    '# Odds-API.io Price Quality Filter',
    '',
    'Filters raw Odds-API.io prices before they are used as automatic forward prices.',
    'A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.',
    'Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.',
    'Swapped home/away matches are rejected because venue affects both model probabilities and market odds.',
    '',
    f"Input price rows: {summary['input_price_rows']}",
    f"Accepted price rows: {summary['accepted_price_rows']}",
    f"Rejected price rows: {summary['rejected_price_rows']}",
    f"Rejected U-/reserve rows: {summary['rejected_youth_or_reserve_rows']}",
    f"Forward prediction rows: {summary['forward_prediction_rows']}",
    f"Rule: {summary['quality_rule']}",
    '',
]
if len(rejected):
    markdown.extend(['## Rejected prices', ''])
    for _, row in rejected.head(40).iterrows():
        markdown.append(
            f"- {row.get('match_date')} | {row.get('home_team')} vs {row.get('away_team')} | "
            f"{row.get('source_name')} | status={row.get('quality_status')}"
        )
else:
    markdown.append('No rejected prices.')

report_path.write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
