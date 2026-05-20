# Manual Odds Entry Instructions

Purpose: create real forward paper-test snapshots from Bet365 pre-match 1X2 odds.

Do not stake real money from this system.

## What to fill

Open `data/manual/manual_odds_template.csv` and fill these columns only:

- `market_home_odds`
- `market_draw_odds`
- `market_away_odds`
- `odds_captured_at_utc`

Use decimal odds from Bet365 1X2 / Full Time Result before kickoff.

## Current rows needing odds

- 2026-05-21 19:30 | Anderlecht vs St Truiden
- 2026-05-21 16:00 | Atromitos vs Panserraikos
- 2026-05-21 19:30 | Gent vs St. Gilloise
- 2026-05-21 17:00 | Kifisia vs Larisa
- 2026-05-21 19:30 | Mechelen vs Club Brugge
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis
- 2026-05-24 15:00:00 | Brighton and Hove Albion vs Manchester United

## After filling odds

Run the workflow again. Expected result:

- `manual_forward_snapshots` becomes greater than 0
- `paper_test_picks` may become greater than 0
- `candidate_bets` may still remain 0, which is acceptable