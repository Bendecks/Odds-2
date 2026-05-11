from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
prices_path = output_dir / 'automatic_forward_prices.csv'
predictions_path = output_dir / 'forward_fixture_predictions.csv'
value_path = output_dir / 'automatic_forward_value_snapshots.csv'


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


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
        return None
    return parsed.date().isoformat()


prices = safe_read_csv(prices_path)
predictions = safe_read_csv(predictions_path)
values = safe_read_csv(value_path)

for df in [prices, predictions, values]:
    if len(df):
        if 'match_date' in df.columns:
            df['coverage_match_date'] = df['match_date'].apply(parse_date)
        if 'home_team' in df.columns:
            df['coverage_home'] = df['home_team'].apply(norm_team)
        if 'away_team' in df.columns:
            df['coverage_away'] = df['away_team'].apply(norm_team)

if len(prices):
    if 'source_name' not in prices.columns:
        prices['source_name'] = ''
    prices['is_fresh_api_price'] = prices['source_name'].astype(str).str.contains('odds_api_io|api_football', case=False, na=False)
    prices['is_odds_api_io'] = prices['source_name'].astype(str).str.contains('odds_api_io', case=False, na=False)
    prices['coverage_key'] = prices['coverage_match_date'].astype(str) + '|' + prices['coverage_home'].astype(str) + '|' + prices['coverage_away'].astype(str)
else:
    prices = pd.DataFrame(columns=['is_fresh_api_price', 'is_odds_api_io', 'coverage_key', 'source_name', 'source_type', 'source_quality'])

if len(predictions):
    predictions['coverage_key'] = predictions['coverage_match_date'].astype(str) + '|' + predictions['coverage_home'].astype(str) + '|' + predictions['coverage_away'].astype(str)
else:
    predictions = pd.DataFrame(columns=['coverage_key'])

price_keys = set(prices['coverage_key'].dropna().astype(str)) if len(prices) else set()
fresh_keys = set(prices.loc[prices['is_fresh_api_price'], 'coverage_key'].dropna().astype(str)) if len(prices) else set()
odds_api_io_keys = set(prices.loc[prices['is_odds_api_io'], 'coverage_key'].dropna().astype(str)) if len(prices) else set()

coverage_rows = []
if len(predictions):
    for _, row in predictions.iterrows():
        key = str(row.get('coverage_key'))
        match_prices = prices[prices['coverage_key'].astype(str) == key].copy() if len(prices) else pd.DataFrame()
        coverage_rows.append({
            'prediction_id': row.get('prediction_id'),
            'match_date': row.get('match_date'),
            'home_team': row.get('home_team'),
            'away_team': row.get('away_team'),
            'league': row.get('league'),
            'has_any_automatic_price': key in price_keys,
            'has_fresh_api_price': key in fresh_keys,
            'has_odds_api_io_price': key in odds_api_io_keys,
            'automatic_price_rows': int(len(match_prices)),
            'fresh_api_price_rows': int(match_prices['is_fresh_api_price'].sum()) if len(match_prices) else 0,
            'odds_api_io_price_rows': int(match_prices['is_odds_api_io'].sum()) if len(match_prices) else 0,
            'source_names': ', '.join(sorted(match_prices['source_name'].dropna().astype(str).unique())) if len(match_prices) and 'source_name' in match_prices.columns else '',
        })
coverage = pd.DataFrame(coverage_rows)
coverage_columns = [
    'prediction_id', 'match_date', 'home_team', 'away_team', 'league',
    'has_any_automatic_price', 'has_fresh_api_price', 'has_odds_api_io_price',
    'automatic_price_rows', 'fresh_api_price_rows', 'odds_api_io_price_rows', 'source_names'
]
for col in coverage_columns:
    if col not in coverage.columns:
        coverage[col] = None
coverage = coverage[coverage_columns]
coverage.to_csv(output_dir / 'forward_price_coverage_report.csv', index=False)

source_summary = pd.DataFrame(columns=['source_name', 'source_type', 'source_quality', 'price_rows'])
if len(prices) and 'source_name' in prices.columns:
    for col in ['source_type', 'source_quality']:
        if col not in prices.columns:
            prices[col] = ''
    source_summary = prices.groupby(['source_name', 'source_type', 'source_quality'], dropna=False).size().reset_index(name='price_rows')
source_summary.to_csv(output_dir / 'forward_price_source_summary.csv', index=False)

summary = {
    'forward_prediction_rows': int(len(predictions)),
    'automatic_price_rows': int(len(prices)),
    'value_snapshot_rows': int(len(values)),
    'matches_with_any_automatic_price': int(coverage['has_any_automatic_price'].sum()) if len(coverage) else 0,
    'matches_with_fresh_api_price': int(coverage['has_fresh_api_price'].sum()) if len(coverage) else 0,
    'matches_with_odds_api_io_price': int(coverage['has_odds_api_io_price'].sum()) if len(coverage) else 0,
    'fresh_api_match_coverage_rate': round(float(coverage['has_fresh_api_price'].mean()), 4) if len(coverage) else 0.0,
    'odds_api_io_match_coverage_rate': round(float(coverage['has_odds_api_io_price'].mean()), 4) if len(coverage) else 0.0,
    'real_money_ready': False,
}
pd.DataFrame([summary]).to_csv(output_dir / 'forward_price_coverage_summary.csv', index=False)

markdown = [
    '# Forward Price Coverage Report',
    '',
    'Measures automatic price coverage for forward predictions.',
    'Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.',
    '',
    f"Forward prediction rows: {summary['forward_prediction_rows']}",
    f"Automatic price rows: {summary['automatic_price_rows']}",
    f"Value snapshot rows: {summary['value_snapshot_rows']}",
    f"Matches with any automatic price: {summary['matches_with_any_automatic_price']}",
    f"Matches with fresh API price: {summary['matches_with_fresh_api_price']}",
    f"Matches with odds-api.io price: {summary['matches_with_odds_api_io_price']}",
    f"Fresh API match coverage rate: {summary['fresh_api_match_coverage_rate']}",
    f"odds-api.io match coverage rate: {summary['odds_api_io_match_coverage_rate']}",
    f"Real-money ready: {summary['real_money_ready']}",
    '',
    '## Match coverage',
    '',
]
if len(coverage):
    for _, row in coverage.iterrows():
        markdown.append(
            f"- {row['match_date']} | {row['home_team']} vs {row['away_team']} | "
            f"any={row['has_any_automatic_price']} | fresh_api={row['has_fresh_api_price']} | "
            f"odds_api_io={row['has_odds_api_io_price']} | rows={row['automatic_price_rows']} | sources={row['source_names']}"
        )
else:
    markdown.append('No forward predictions available for coverage measurement.')

markdown.extend(['', '## Source summary', ''])
if len(source_summary):
    for _, row in source_summary.iterrows():
        markdown.append(f"- {row['source_name']} | {row['source_type']} | rows={int(row['price_rows'])}")
else:
    markdown.append('No automatic price sources available.')

(output_dir / 'forward_price_coverage_report.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
