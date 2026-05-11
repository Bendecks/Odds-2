from pathlib import Path
from difflib import get_close_matches

import pandas as pd

output_dir = Path('output/latest')
model_dir = Path('data/model')
config_dir = Path('data/config')
config_dir.mkdir(parents=True, exist_ok=True)

fixtures_path = output_dir / 'upcoming_fixtures.csv'
football_data_proxy_path = output_dir / 'football_data_upcoming_odds.csv'
odds_api_io_proxy_path = output_dir / 'odds_api_io_forward_prices.csv'
market_snapshot_path = output_dir / 'market_snapshot_latest.csv'
manual_forward_path = output_dir / 'manual_forward_snapshots.csv'
ratings_path = model_dir / 'team_strengths.csv'
alias_path = config_dir / 'team_aliases.csv'
source_config_path = config_dir / 'forward_price_sources.csv'
automatic_prices_path = output_dir / 'automatic_forward_prices.csv'
adapter_status_path = output_dir / 'forward_price_source_adapter.csv'

source_columns = ['source_name', 'source_type', 'enabled', 'requires_key', 'status', 'notes']
price_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'source_name', 'source_type', 'market_home_odds', 'market_draw_odds',
    'market_away_odds', 'price_captured_at_utc', 'source_quality'
]
alias_columns = ['source_team', 'model_team', 'note']


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def norm(value) -> str:
    text = str(value or '').lower().strip()
    for token in ['fc', 'afc', 'cf', '.', ',']:
        text = text.replace(token, '')
    text = text.replace('&', 'and')
    return ' '.join(text.split())


fixtures = safe_read_csv(fixtures_path)
football_data_proxy = safe_read_csv(football_data_proxy_path)
odds_api_io_proxy = safe_read_csv(odds_api_io_proxy_path)
market_snapshot = safe_read_csv(market_snapshot_path)
manual_forward = safe_read_csv(manual_forward_path)
ratings = safe_read_csv(ratings_path)
aliases = safe_read_csv(alias_path)

if len(aliases) == 0:
    aliases = pd.DataFrame(columns=alias_columns)
for col in alias_columns:
    if col not in aliases.columns:
        aliases[col] = None
aliases = aliases[alias_columns]
aliases.to_csv(alias_path, index=False)

if source_config_path.exists():
    sources = safe_read_csv(source_config_path)
else:
    sources = pd.DataFrame()
for row in [
    {
        'source_name': 'football_data_fixtures_proxy',
        'source_type': 'delayed_market_proxy',
        'enabled': True,
        'requires_key': False,
        'status': 'enabled_proxy',
        'notes': 'Free Football-Data fixtures odds proxy. Delayed/non-live; paper-test only.',
    },
    {
        'source_name': 'odds_api_io_multi_proxy',
        'source_type': 'free_api_market_proxy',
        'enabled': True,
        'requires_key': True,
        'status': 'enabled_if_secret_available_capped_calls',
        'notes': 'Optional odds-api.io source. Calls are capped by ODDS_API_IO_MAX_CALLS.',
    },
]:
    if len(sources) == 0 or not (sources.get('source_name', pd.Series(dtype=str)).astype(str) == row['source_name']).any():
        sources = pd.concat([sources, pd.DataFrame([row])], ignore_index=True)
for col in source_columns:
    if col not in sources.columns:
        sources[col] = None
sources = sources[source_columns]
sources.to_csv(source_config_path, index=False)

price_frames = []
if len(odds_api_io_proxy):
    price_frames.append(odds_api_io_proxy)
if len(football_data_proxy):
    price_frames.append(football_data_proxy)
prices = pd.concat(price_frames, ignore_index=True) if price_frames else pd.DataFrame(columns=price_columns)
for col in price_columns:
    if col not in prices.columns:
        prices[col] = None
prices = prices[price_columns]
prices.to_csv(automatic_prices_path, index=False)

model_team_col = 'team' if 'team' in ratings.columns else ratings.columns[0] if len(ratings.columns) else 'team'
model_teams = sorted(ratings[model_team_col].dropna().astype(str).unique().tolist()) if len(ratings) else []
model_norm_map = {norm(team): team for team in model_teams}
alias_map = {norm(row['source_team']): row['model_team'] for _, row in aliases.dropna(subset=['source_team', 'model_team']).iterrows()}
match_rows = []

if len(fixtures):
    for _, fixture in fixtures.iterrows():
        for side in ['home_team', 'away_team']:
            source_team = fixture.get(side)
            normalized = norm(source_team)
            match_type = 'unmatched'
            matched_team = None
            suggestion = None
            if normalized in alias_map:
                matched_team = alias_map[normalized]
                match_type = 'alias'
            elif normalized in model_norm_map:
                matched_team = model_norm_map[normalized]
                match_type = 'exact_normalized'
            else:
                close = get_close_matches(normalized, list(model_norm_map.keys()), n=1, cutoff=0.78)
                if close:
                    suggestion = model_norm_map[close[0]]
                    match_type = 'suggested_alias_needed'
            match_rows.append({
                'fixture_id': fixture.get('fixture_id'),
                'match_date': fixture.get('match_date'),
                'match_time': fixture.get('match_time'),
                'side': side,
                'source_team': source_team,
                'normalized_source_team': normalized,
                'matched_model_team': matched_team,
                'match_type': match_type,
                'suggested_model_team': suggestion,
            })

match_report = pd.DataFrame(match_rows)
match_columns = [
    'fixture_id', 'match_date', 'match_time', 'side', 'source_team',
    'normalized_source_team', 'matched_model_team', 'match_type', 'suggested_model_team'
]
for col in match_columns:
    if col not in match_report.columns:
        match_report[col] = None
match_report = match_report[match_columns]
match_report.to_csv(output_dir / 'fixture_model_match_report.csv', index=False)

matched_team_rows = int(match_report['matched_model_team'].notna().sum()) if len(match_report) else 0
unmatched_team_rows = int(match_report['matched_model_team'].isna().sum()) if len(match_report) else 0
ready_for_model_fixture_join = bool(len(match_report) > 0 and unmatched_team_rows == 0)
match_summary = {
    'fixture_rows': int(len(fixtures)),
    'team_rows_checked': int(len(match_report)),
    'matched_team_rows': matched_team_rows,
    'unmatched_team_rows': unmatched_team_rows,
    'suggested_alias_rows': int((match_report['match_type'] == 'suggested_alias_needed').sum()) if len(match_report) else 0,
    'ready_for_model_fixture_join': ready_for_model_fixture_join,
}
pd.DataFrame([match_summary]).to_csv(output_dir / 'fixture_model_match_summary.csv', index=False)

market_proxy_types = []
if len(market_snapshot) and 'snapshot_type' in market_snapshot.columns:
    market_proxy_types = sorted(set(market_snapshot['snapshot_type'].dropna().astype(str).tolist()))

has_upcoming_fixtures = len(fixtures) > 0
has_automatic_forward_odds = len(prices) > 0
has_historical_market_proxy = any('proxy' in item for item in market_proxy_types) or len(market_snapshot) > 0
has_manual_forward = len(manual_forward) > 0
enabled_sources = int((sources['enabled'].astype(str).str.lower() == 'true').sum()) if len(sources) else 0

status = 'automatic_forward_not_ready'
blocker = 'automatic_forward_odds_or_price_proxy_missing'
next_development_step = 'find_or_build_free_automatic_forward_price_source'

if not has_upcoming_fixtures:
    blocker = 'automatic_fixture_source_missing'
    next_development_step = 'add_or_repair_upcoming_fixture_source'
elif not ready_for_model_fixture_join:
    blocker = 'fixture_model_team_matching_incomplete'
    next_development_step = 'add_team_aliases_for_upcoming_fixtures'
elif has_automatic_forward_odds:
    status = 'automatic_forward_proxy_available'
    blocker = 'none_for_proxy_testing'
    next_development_step = 'evaluate_proxy_value_snapshots_and_paper_filters'
elif has_manual_forward:
    status = 'manual_forward_available_but_optional'
    blocker = 'automatic_forward_source_still_missing'
    next_development_step = 'continue_automatic_source_research'
elif has_historical_market_proxy:
    blocker = 'only_historical_market_proxy_available_not_forward_valid'
    next_development_step = 'replace_historical_market_proxy_for_forward_testing'

adapter_summary = {
    'fixture_rows': int(len(fixtures)),
    'configured_sources': int(len(sources)),
    'enabled_sources': enabled_sources,
    'automatic_price_rows': int(len(prices)),
    'odds_api_io_price_rows': int(len(odds_api_io_proxy)),
    'football_data_price_rows': int(len(football_data_proxy)),
    'adapter_status': 'proxy_prices_available' if len(prices) else 'ready_no_proxy_prices_available',
}
pd.DataFrame([adapter_summary]).to_csv(adapter_status_path, index=False)

summary = {
    'upcoming_fixture_rows': int(len(fixtures)),
    'fixture_team_rows_checked': int(len(match_report)),
    'fixture_team_rows_unmatched': unmatched_team_rows,
    'ready_for_model_fixture_join': ready_for_model_fixture_join,
    'historical_market_proxy_rows': int(len(market_snapshot)),
    'manual_forward_rows': int(len(manual_forward)),
    'configured_forward_sources': int(len(sources)),
    'enabled_forward_sources': enabled_sources,
    'automatic_forward_price_rows': int(len(prices)),
    'odds_api_io_price_rows': int(len(odds_api_io_proxy)),
    'football_data_price_rows': int(len(football_data_proxy)),
    'has_upcoming_fixtures': bool(has_upcoming_fixtures),
    'has_automatic_forward_odds': bool(has_automatic_forward_odds),
    'has_historical_market_proxy': bool(has_historical_market_proxy),
    'manual_fallback_mode': 'parked_optional_fallback',
    'automatic_forward_status': status,
    'blocker': blocker,
    'next_development_step': next_development_step,
}

pd.DataFrame([summary]).to_csv(output_dir / 'automatic_forward_source_report.csv', index=False)

markdown = [
    '# Automatic Forward Source Report',
    '',
    'Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.',
    'Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.',
    '',
    f"Upcoming fixture rows: {summary['upcoming_fixture_rows']}",
    f"Fixture team rows unmatched: {summary['fixture_team_rows_unmatched']}",
    f"Ready for model-fixture join: {summary['ready_for_model_fixture_join']}",
    f"Automatic forward price rows: {summary['automatic_forward_price_rows']}",
    f"odds-api.io price rows: {summary['odds_api_io_price_rows']}",
    f"Football-Data price rows: {summary['football_data_price_rows']}",
    f"Automatic forward status: {summary['automatic_forward_status']}",
    f"Blocker: {summary['blocker']}",
    f"Next development step: {summary['next_development_step']}",
    '',
    '## Team matching',
    '',
]

if len(match_report):
    unmatched = match_report[match_report['matched_model_team'].isna()].copy()
    if len(unmatched):
        for _, row in unmatched.head(30).iterrows():
            markdown.append(f"- {row['source_team']} | suggestion={row['suggested_model_team']} | type={row['match_type']}")
    else:
        markdown.append('All fixture teams match the model team table.')
else:
    markdown.append('No fixture rows available for team matching.')

markdown.extend(['', '## Interpretation', ''])
if status == 'automatic_forward_proxy_available':
    markdown.append('Automatic proxy prices are available. Use only for paper-test/proxy observation, not real money.')
elif has_upcoming_fixtures and ready_for_model_fixture_join:
    markdown.append('Fixtures and model matching are available, but there is no automatic forward price source yet.')
elif has_upcoming_fixtures:
    markdown.append('Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.')
else:
    markdown.append('No upcoming fixture source is currently available.')

(output_dir / 'automatic_forward_source_report.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
