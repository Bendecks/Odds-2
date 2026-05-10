from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

raw_dir = Path('data/raw')
output_dir = Path('output/latest')
snapshot_dir = Path('data/market_snapshots')

output_dir.mkdir(parents=True, exist_ok=True)
snapshot_dir.mkdir(parents=True, exist_ok=True)

market = pd.read_parquet(raw_dir / 'premier_league_2425.parquet')

# MVP snapshot source:
# football-data historical rows are used as a deterministic stand-in until a real pre-match source is connected.
# This keeps the rest of the pipeline ready for Betfair / selective odds API snapshots.
snapshot = market.tail(10).copy().reset_index(drop=True)

snapshot['snapshot_created_at_utc'] = datetime.now(timezone.utc).isoformat()
snapshot['snapshot_source'] = 'football-data.co.uk-historical-standin'
snapshot['snapshot_type'] = 'historical_proxy'

columns = [
    'snapshot_created_at_utc',
    'snapshot_source',
    'snapshot_type',
    'Date',
    'Time',
    'HomeTeam',
    'AwayTeam',
    'B365H',
    'B365D',
    'B365A',
    'PSCH',
    'PSCD',
    'PSCA',
]

available_columns = [c for c in columns if c in snapshot.columns]
snapshot = snapshot[available_columns]

snapshot.to_parquet(output_dir / 'market_snapshot_latest.parquet', index=False)
snapshot.to_csv(output_dir / 'market_snapshot_latest.csv', index=False)

snapshot.to_parquet(snapshot_dir / 'market_snapshot_latest.parquet', index=False)

print(f'Created market snapshot with {len(snapshot)} rows')
print(snapshot.head())
