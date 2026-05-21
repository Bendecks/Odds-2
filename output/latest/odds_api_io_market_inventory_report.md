# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 90
Market rows seen: 1996
Unique bookmakers: 2
Unique market names: 52
Bet365 market rows: 1894

## Market types found

- Goals total / Over-Under: 585
- Other / Unknown: 581
- Handicap / Spread: 379
- Half-time / Period: 100
- 1X2 / Match result: 98
- Double chance: 90
- Correct score: 88
- Both teams to score: 75

## Bet365 market types found

- Other / Unknown: 581
- Goals total / Over-Under: 542
- Handicap / Spread: 328
- Half-time / Period: 100
- 1X2 / Match result: 90
- Double chance: 90
- Correct score: 88
- Both teams to score: 75

## Most common Bet365 market names

- ML: 90
- Draw No Bet: 90
- Double Chance: 90
- Spread: 90
- Totals: 90
- Goals Over/Under: 90
- Spread HT: 90
- Half Time Result: 90
- Correct Score: 88
- Corners Totals: 80
- Totals HT: 78
- Corners Totals HT: 78
- Corners 2-Way: 78
- Corners: 78
- Alternative Goal Line: 61
- Alternative Asian Handicap: 61
- Both Teams To Score: 25
- European Handicap: 25
- Number of Goals In Match: 25
- 1st Half Handicap: 25
- Team Total Goals Away: 25
- Both Teams To Score 2H: 25
- Team Total Goals Home: 25
- Both Teams To Score HT: 25
- Specials: 25
- Alternative Total Goals: 25
- Exact Total Goals: 25
- Alternative Corners: 24
- Total Corners: 24
- Corners Spread: 19

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.