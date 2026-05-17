# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2269
Unique bookmakers: 2
Unique market names: 39
Bet365 market rows: 2140

## Market types found

- Goals total / Over-Under: 738
- Other / Unknown: 519
- Handicap / Spread: 439
- 1X2 / Match result: 122
- Half-time / Period: 122
- Both teams to score: 117
- Correct score: 109
- Double chance: 103

## Bet365 market types found

- Goals total / Over-Under: 691
- Other / Unknown: 519
- Handicap / Spread: 369
- Half-time / Period: 122
- Both teams to score: 117
- 1X2 / Match result: 110
- Correct score: 109
- Double chance: 103

## Most common Bet365 market names

- ML: 110
- Spread: 110
- Totals: 110
- Draw No Bet: 109
- Goals Over/Under: 109
- Correct Score: 109
- Spread HT: 108
- Half Time Result: 108
- Double Chance: 103
- Totals HT: 93
- Corners Totals: 93
- Corners: 93
- Corners 2-Way: 93
- Corners Totals HT: 91
- Alternative Goal Line: 47
- Alternative Asian Handicap: 47
- Both Teams To Score: 39
- European Handicap: 39
- Specials: 39
- 1st Half Handicap: 39
- Alternative Total Goals: 39
- Total Corners: 39
- Both Teams To Score HT: 39
- Team Total Goals Away: 39
- Number of Goals In Match: 39
- Both Teams To Score 2H: 39
- Alternative Corners: 39
- Exact Total Goals: 39
- Team Total Goals Home: 39
- First 10 Minutes (00:00 - 09:59): 19

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.