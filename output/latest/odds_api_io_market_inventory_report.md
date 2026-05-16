# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 80
Market rows seen: 1936
Unique bookmakers: 2
Unique market names: 72
Bet365 market rows: 1840

## Market types found

- Other / Unknown: 719
- Goals total / Over-Under: 460
- Handicap / Spread: 356
- Half-time / Period: 92
- 1X2 / Match result: 88
- Both teams to score: 75
- Correct score: 74
- Double chance: 72

## Bet365 market types found

- Other / Unknown: 719
- Goals total / Over-Under: 420
- Handicap / Spread: 312
- Half-time / Period: 92
- 1X2 / Match result: 76
- Both teams to score: 75
- Correct score: 74
- Double chance: 72

## Most common Bet365 market names

- ML: 76
- Goals Over/Under: 76
- Draw No Bet: 74
- Spread: 74
- Totals: 74
- Spread HT: 74
- Half Time Result: 74
- Correct Score: 74
- Double Chance: 72
- Totals HT: 54
- Alternative Asian Handicap: 46
- Alternative Goal Line: 44
- Corners Totals: 42
- Corners 2-Way: 40
- Corners: 40
- Corners Totals HT: 38
- Both Teams To Score: 25
- European Handicap: 25
- Team Total Goals Home: 25
- Alternative Total Goals: 25
- Specials: 25
- Both Teams To Score HT: 25
- Both Teams To Score 2H: 25
- Exact Total Goals: 25
- Number of Goals In Match: 25
- 1st Half Handicap: 25
- Team Total Goals Away: 25
- Total Corners: 23
- Alternative Corners: 23
- Corners Spread: 21

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.