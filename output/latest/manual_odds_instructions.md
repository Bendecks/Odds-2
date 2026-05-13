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

- 2026-05-13 20:30 | Alaves vs Barcelona
- 2026-05-13 18:00 | Brest vs Strasbourg
- 2026-05-13 18:00 | Espanol vs Ath Bilbao
- 2026-05-13 20:30 | Getafe vs Mallorca
- 2026-05-13 20:00 | Hearts vs Falkirk
- 2026-05-13 20:00 | Lens vs Paris SG
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete
- 2026-05-13 20:00 | Man City vs Crystal Palace
- 2026-05-13 19:00:00 | Manchester City vs Crystal Palace
- 2026-05-13 20:00 | Motherwell vs Celtic
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos
- 2026-05-13 17:30 | PAOK vs AEK
- 2026-05-13 20:00 | Rangers vs Hibernian
- 2026-05-13 18:00 | Villarreal vs Sevilla
- 2026-05-13 15:00 | Volos NFC vs Aris
- 2026-05-14 19:00 | Girona vs Sociedad
- 2026-05-14 20:30 | Real Madrid vs Oviedo
- 2026-05-14 18:00 | Valencia vs Vallecano

## After filling odds

Run the workflow again. Expected result:

- `manual_forward_snapshots` becomes greater than 0
- `paper_test_picks` may become greater than 0
- `candidate_bets` may still remain 0, which is acceptable