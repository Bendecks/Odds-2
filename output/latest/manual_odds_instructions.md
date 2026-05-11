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

- 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United

## After filling odds

Run the workflow again. Expected result:

- `manual_forward_snapshots` becomes greater than 0
- `paper_test_picks` may become greater than 0
- `candidate_bets` may still remain 0, which is acceptable