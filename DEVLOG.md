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
- scripts/generate_poisson_predictions.py
- scripts/calculate_ev.py
- scripts/log_predictions.py
- scripts/settle_predictions.py
- scripts/validate_free_sources.py

---

## Major milestone reached

The project now:

1. Downloads historical odds automatically
2. Downloads ClubElo ratings automatically
3. Builds basic strength ratings
4. Generates Poisson predictions
5. Calculates expected value against bookmaker odds
6. Logs predictions persistently
7. Automatically settles predictions against historical results
8. Calculates primitive ROI tracking
9. Persists machine-readable validation history
10. Commits workflow outputs back into the repository automatically

This means the repository itself now acts as:
- persistent AI memory
- workflow telemetry
- validation archive
- historical debugging system
- prediction archive
- performance tracking system

---

## Prediction tracking architecture

### Prediction lifecycle

1. Generate prediction
2. Store prediction with deterministic event_id
3. Persist prediction in JSONL archive
4. Re-check fixture results later
5. Settle prediction
6. Calculate ROI
7. Build historical performance summaries

### Core files

Persistent archive:
- data/predictions/prediction_log.jsonl

Latest outputs:
- output/latest/prediction_log_latest.parquet
- output/latest/settled_predictions.parquet
- output/latest/performance_summary.csv

---

## Validation strategy

Workflow now validates:

1. football-data parquet generation
2. ClubElo parquet generation
3. Team strength model generation
4. Poisson prediction generation
5. EV calculation generation
6. Prediction log generation
7. Prediction settlement generation
8. Required columns
9. Row counts

Validation output:

- output/latest/free_data_status.json
- output/latest/free_data_status.md
- output/history/

---

## Important architectural shift

The system is no longer just:
- a modelling pipeline

It is now becoming:
- a measurable betting research platform

Key distinction:
- every prediction becomes auditable
- model quality can be evaluated over time
- AI can eventually self-evaluate historical edge

---

## Current roadmap

### High priority

- Better Poisson calibration
- Proper attack/defense weighting
- Home advantage modelling
- CLV tracker
- Telegram alerts
- Market snapshot ingestion

### Medium priority

- Betfair integration
- Pinnacle snapshot logic
- Asian handicap support
- Kelly Criterion sizing
- Streamlit dashboard

### Long-term

- Multi-model ensemble
- Injury/news ingestion
- AI-assisted pick explanations
- Automated bankroll management

---

## Avoid for now

- Heavy live scraping
- Selenium/Playwright systems
- High-frequency polling
- Broad live arbitrage systems

---

## Important operational rule

After workflow completion:
- inspect artifacts automatically
- inspect validation reports
- inspect failures before next commits
- batch multiple fixes into single commits when possible
- minimize required human intervention
