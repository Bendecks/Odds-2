from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
config_dir = Path('data/config')
config_dir.mkdir(parents=True, exist_ok=True)

fixtures_path = output_dir / 'upcoming_fixtures.csv'
source_config_path = config_dir / 'forward_price_sources.csv'
normalized_path = output_dir / 'automatic_forward_prices.csv'

expected_source_columns = [
    'source_name', 'source_type', 'enabled', 'requires_key', 'status', 'notes'
]
expected_price_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'source_name', 'source_type', 'market_home_odds', 'market_draw_odds',
    'market_away_odds', 'price_captured_at_utc', 'source_quality'
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


if not source_config_path.exists():
    sources = pd.DataFrame([
        {
            'source_name': 'none_configured',
            'source_type': 'placeholder',
            'enabled': False,
            'requires_key': False,
            'status': 'not_configured',
            'notes': 'Add free automatic forward price sources here when identified.',
        }
    ])
    sources.to_csv(source_config_path, index=False)
else:
    sources = safe_read_csv(source_config_path)

for col in expected_source_columns:
    if col not in sources.columns:
        sources[col] = None
sources = sources[expected_source_columns]

fixtures = safe_read_csv(fixtures_path)
price_rows = []

# Adapter scaffold only. No automatic source is enabled yet, so this creates an
# empty normalized price table with stable columns for downstream scripts.
prices = pd.DataFrame(price_rows)
for col in expected_price_columns:
    if col not in prices.columns:
        prices[col] = None
prices = prices[expected_price_columns]
prices.to_csv(normalized_path, index=False)

summary = {
    'fixture_rows': int(len(fixtures)),
    'configured_sources': int(len(sources)),
    'enabled_sources': int((sources['enabled'].astype(str).str.lower() == 'true').sum()) if len(sources) else 0,
    'automatic_price_rows': int(len(prices)),
    'adapter_status': 'ready_no_sources_enabled',
}

pd.DataFrame([summary]).to_csv(output_dir / 'forward_price_source_adapter.csv', index=False)

markdown = [
    '# Forward Price Source Adapter',
    '',
    'This is a scaffold for automatic/free forward price sources.',
    'Manual Bet365 input remains parked as an optional fallback.',
    '',
    f"Fixture rows: {summary['fixture_rows']}",
    f"Configured sources: {summary['configured_sources']}",
    f"Enabled sources: {summary['enabled_sources']}",
    f"Automatic price rows: {summary['automatic_price_rows']}",
    f"Adapter status: {summary['adapter_status']}",
    '',
    '## Config file',
    '',
    '`data/config/forward_price_sources.csv`',
]

(output_dir / 'forward_price_source_adapter.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
