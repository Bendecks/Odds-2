# Odds 2

Data Integrity Foundation V1 for iPhone → bet365 PDF → GitHub Actions.

This repo intentionally starts with data quality, not betting rules.

## Strategic shift

The project now prioritizes:

- Pre-match value betting
- Closing Line Value (CLV) tracking
- Historical modelling
- Free and stable data sources
- GitHub-native automation

The project intentionally avoids fragile live scraping architectures in the MVP.

## Primary data stack

### Historical odds

- football-data.co.uk
- Pinnacle closing odds
- Asian handicap datasets
- Over/Under datasets

### Team strength and modelling

- ClubElo
- FBRef
- Understat
- soccerdata

### Infrastructure

- Python
- GitHub Actions
- Parquet
- DuckDB
- Pandas

## Current MVP goals

1. Download historical football odds.
2. Download ClubElo ratings.
3. Build fair odds scaffolding.
4. Track CLV against Pinnacle closing prices.
5. Build deterministic data pipelines.
6. Archive snapshots for future modelling.

## Workflow

Run GitHub Action:

```text
Free Betting Data Stack
```

## Current scripts

```text
scripts/fetch_football_data.py
scripts/fetch_clubelo.py
scripts/build_fair_odds.py
```

## Key outputs

```text
data/raw/
data/model/
```

## Planned next phase

- Poisson goal models
- EV calculations
- Telegram alerts
- Team-name canonical mapping
- CLV dashboards
- Betfair integration
- Selective Pinnacle snapshots
