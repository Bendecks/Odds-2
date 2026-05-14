# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2369
Unique bookmakers: 2
Unique market names: 64
Bet365 market rows: 2198

## Market types found

- Other / Unknown: 682
- Goals total / Over-Under: 636
- Handicap / Spread: 471
- Half-time / Period: 136
- 1X2 / Match result: 128
- Correct score: 110
- Double chance: 107
- Both teams to score: 99

## Bet365 market types found

- Other / Unknown: 682
- Goals total / Over-Under: 571
- Handicap / Spread: 383
- Half-time / Period: 136
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 107
- Both teams to score: 99

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Half Time Result: 110
- Correct Score: 110
- Spread HT: 109
- Double Chance: 107
- Totals HT: 83
- Corners Totals: 53
- Corners: 52
- Corners 2-Way: 52
- Corners Totals HT: 42
- Alternative Goal Line: 38
- Alternative Asian Handicap: 38
- Both Teams To Score: 33
- European Handicap: 33
- Alternative Total Goals: 33
- Exact Total Goals: 33
- Both Teams To Score 2H: 33
- Team Total Goals Home: 33
- Number of Goals In Match: 33
- Team Total Goals Away: 33
- Specials: 33
- Both Teams To Score HT: 33
- 1st Half Handicap: 33
- Total Corners: 27
- Alternative Corners: 27
- 1st Half Goal Line: 26

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.