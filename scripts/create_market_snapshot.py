from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

raw_dir = Path('data/raw/multiseason')
output_dir = Path('output/latest')
snapshot_dir = Path('data/market_snapshots')

output_dir.mkdir(parents=True, exist_ok=True)
snapshot_dir.mkdir(parents=True, exist_ok=True)

market = pd.read_parquet(raw_dir / 'combined_multiseason.parquet')

# Use most recent season only for current market simulation.
if 'source_season' in market.columns:
    market = market[market['source_season'] == '2425'].copy()

market = market.sort_values(['Date', 'Time']).reset_index(drop=True)

# Simulate recent bookmaker market state.
# We intentionally use a rolling recent window instead of tail(10) randomness.
snapshot = market.tail(30).copy().reset_index(drop=True)

snapshot_timestamp = datetime.now(timezone.utc).isoformat()

snapshot['snapshot_created_at_utc'] = snapshot_timestamp
snapshot['snapshot_source'] = 'football-data.co.uk-closing-market-proxy'
snapshot['snapshot_type'] = 'closing_market_proxy'
snapshot['market_proxy_quality'] = 'historical_closing_lines'

# Normalize bookmaker structure.
snapshot['market_home_odds'] = pd.to_numeric(snapshot.get('PSCH'), errors='coerce')
snapshot['market_draw_odds'] = pd.to_numeric(snapshot.get('PSCD'), errors='coerce')
snapshot['market_away_odds'] = pd.to_numeric(snapshot.get('PSCA'), errors='coerce')

# Fallback to Bet365 if Pinnacle closing unavailable.
for market_col, fallback_col in [
    ('market_home_odds', 'B365CH'),
    ('market_draw_odds', 'B365CD'),
    ('market_away_odds', 'B365CA'),
]:
    fallback_values = pd.to_numeric(snapshot.get(fallback_col), errors='coerce')
    snapshot[market_col] = snapshot[market_col].fillna(fallback_values)

snapshot['market_overround'] = (
    (1 / snapshot['market_home_odds'])
    + (1 / snapshot['market_draw_odds'])
    + (1 / snapshot['market_away_odds'])
)

snapshot['market_overround'] = snapshot['market_overround'].round(4)

snapshot = snapshot[
    snapshot['market_overround'].between(1.01, 1.20)
].copy()

columns = [
    'snapshot_created_at_utc',
    'snapshot_source',
    'snapshot_type',
    'market_proxy_quality',
    'market_overround',
    'source_league',
    'source_season',
    'Date',
    'Time',
    'HomeTeam',
    'AwayTeam',
    'market_home_odds',
    'market_draw_odds',
    'market_away_odds',
    'PSCH',
    'PSCD',
    'PSCA',
    'B365CH',
    'B365CD',
    'B365CA',
]

available_columns = [c for c in columns if c in snapshot.columns]
snapshot = snapshot[available_columns]

snapshot.to_parquet(output_dir / 'market_snapshot_latest.parquet', index=False)
snapshot.to_csv(output_dir / 'market_snapshot_latest.csv', index=False)

historical_name = f'market_snapshot_{datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")}.parquet'
snapshot.to_parquet(snapshot_dir / historical_name, index=False)

snapshot.to_parquet(snapshot_dir / 'market_snapshot_latest.parquet', index=False)

summary = pd.DataFrame([
    {
        'rows': len(snapshot),
        'avg_overround': round(float(snapshot['market_overround'].mean()), 4) if len(snapshot) else None,
        'snapshot_source': 'football-data.co.uk-closing-market-proxy',
    }
])

summary.to_csv(output_dir / 'market_snapshot_summary.csv', index=False)

print(f'Created improved market snapshot with {len(snapshot)} rows')
print(summary)
