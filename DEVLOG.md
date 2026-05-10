# Odds-2 Development Log

## 2026-05-10

### Strategic shift

Project focus changed from:
- live betting scraping

to:
- pre-match value betting
- CLV tracking
- historical modelling
- free stable data sources

Reason:
- Free live odds APIs are too quota-limited.
- Direct bookmaker scraping creates major maintenance overhead.
- Historical closing-line analysis is more realistic for a sustainable MVP.

---

## Current active data sources

### Confirmed targets

- football-data.co.uk
- ClubElo
- soccerdata
- FBRef
- Understat

### Deprioritized

- The Odds API as primary source
- Playwright bookmaker scraping
- Live odds polling

---

## Current architecture

### Stack

- Python
- GitHub Actions
- Parquet
- DuckDB
- Pandas

### Current scripts

- scripts/fetch_football_data.py
- scripts/fetch_clubelo.py
- scripts/build_fair_odds.py
- scripts/validate_free_sources.py

---

## Validation strategy

Workflow now validates:

1. football-data parquet generation
2. ClubElo parquet generation
3. Team strength model generation
4. Required columns
5. Row counts

Validation output:

- output/latest/free_data_status.json
- output/latest/free_data_status.md

---

## Next milestones

### High priority

- Proper Poisson model
- Team-name canonical mapping
- EV calculations
- CLV tracker
- Telegram alerts

### Medium priority

- Betfair integration
- Pinnacle snapshot logic
- Streamlit dashboard

### Avoid for now

- Heavy live scraping
- Selenium/Playwright systems
- High-frequency polling

---

## Important operational rule

After workflow completion:
- inspect artifacts automatically
- inspect validation reports
- inspect failures before next commits
- batch multiple fixes into single commits when possible
