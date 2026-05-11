from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
fixtures_path = output_dir / 'upcoming_fixtures.csv'
market_snapshot_path = output_dir / 'market_snapshot_latest.csv'
manual_forward_path = output_dir / 'manual_forward_snapshots.csv'

markdown = [
    '# Automatic Forward Source Report',
    '',
    'Purpose: distinguish true automatic forward sources from historical market proxy and paused manual fallback.',
    '',
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


fixtures = safe_read_csv(fixtures_path)
market_snapshot = safe_read_csv(market_snapshot_path)
manual_forward = safe_read_csv(manual_forward_path)

market_proxy_types = []
if len(market_snapshot) and 'snapshot_type' in market_snapshot.columns:
    market_proxy_types = sorted(set(market_snapshot['snapshot_type'].dropna().astype(str).tolist()))

has_upcoming_fixtures = len(fixtures) > 0
has_automatic_forward_odds = False
has_historical_market_proxy = any('proxy' in item for item in market_proxy_types) or len(market_snapshot) > 0
has_manual_forward = len(manual_forward) > 0

status = 'automatic_forward_not_ready'
blocker = 'automatic odds/proxy source missing'

if not has_upcoming_fixtures:
    blocker = 'fixtures missing'
elif has_automatic_forward_odds:
    status = 'automatic_forward_ready'
    blocker = 'none'
elif has_manual_forward:
    status = 'manual_forward_available_optional'
    blocker = 'automatic source still missing'
elif has_historical_market_proxy:
    blocker = 'only historical market proxy available; not valid for forward picks'

summary = {
    'upcoming_fixture_rows': int(len(fixtures)),
    'historical_market_proxy_rows': int(len(market_snapshot)),
    'manual_forward_rows': int(len(manual_forward)),
    'has_upcoming_fixtures': bool(has_upcoming_fixtures),
    'has_automatic_forward_odds': bool(has_automatic_forward_odds),
    'has_historical_market_proxy': bool(has_historical_market_proxy),
    'automatic_forward_status': status,
    'blocker': blocker,
}

pd.DataFrame([summary]).to_csv(output_dir / 'automatic_forward_source_report.csv', index=False)

markdown.extend([
    f"Upcoming fixture rows: {summary['upcoming_fixture_rows']}",
    f"Historical market proxy rows: {summary['historical_market_proxy_rows']}",
    f"Manual forward rows: {summary['manual_forward_rows']}",
    f"Has upcoming fixtures: {summary['has_upcoming_fixtures']}",
    f"Has automatic forward odds: {summary['has_automatic_forward_odds']}",
    f"Has historical market proxy: {summary['has_historical_market_proxy']}",
    f"Automatic forward status: {summary['automatic_forward_status']}",
    f"Blocker: {summary['blocker']}",
    '',
    '## Interpretation',
    '',
])

if status == 'automatic_forward_ready':
    markdown.append('The system has an automatic forward source available.')
elif has_upcoming_fixtures:
    markdown.append('Fixtures are available, but there is no automatic forward odds/source yet. Historical closing-market proxy must remain research-only.')
else:
    markdown.append('No upcoming fixture source is currently available.')

(output_dir / 'automatic_forward_source_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
