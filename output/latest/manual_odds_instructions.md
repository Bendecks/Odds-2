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

- 2026-05-09 17:00 | Besiktas Istanbul vs Trabzonspor
- 2026-05-09 17:00 | Eyupspor vs Caykur Rizespor
- 2026-05-09 17:00 | Galatasaray Istanbul vs Antalyaspor
- 2026-05-09 17:00 | Genclerbirligi SK vs Kasimpasa Istanbul
- 2026-05-09 17:00 | Goztepe Izmir vs Gaziantep FK
- 2026-05-09 17:00 | Istanbul Basaksehir vs Samsunspor
- 2026-05-09 17:00 | Kocaelispor vs Fatih Karagumruk Istanbul
- 2026-05-09 17:00 | Konyaspor vs Fenerbahce Istanbul
- 2026-05-11 20:15 | Benfica vs Sp Braga
- 2026-05-11 20:15 | Estrela vs Famalicao
- 2026-05-11 20:15 | Gil Vicente vs Arouca
- 2026-05-11 20:15 | Guimaraes vs Casa Pia
- 2026-05-11 19:30 | Huesca vs Sociedad B
- 2026-05-11 19:45 | Napoli vs Bologna
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon
- 2026-05-11 20:15 | Santa Clara vs Nacional
- 2026-05-11 20:15 | Tondela vs Moreirense
- 2026-05-11 20:00 | Tottenham vs Leeds
- 2026-05-11 20:00 | Vallecano vs Girona

## After filling odds

Run the workflow again. Expected result:

- `manual_forward_snapshots` becomes greater than 0
- `paper_test_picks` may become greater than 0
- `candidate_bets` may still remain 0, which is acceptable