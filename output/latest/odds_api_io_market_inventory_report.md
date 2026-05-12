# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 10
Events seen in raw odds: 44
Market rows seen: 845
Unique bookmakers: 2
Unique market names: 39
Bet365 market rows: 784

## Market types found

- Goals total / Over-Under: 277
- Other / Unknown: 174
- Handicap / Spread: 160
- 1X2 / Match result: 53
- Half-time / Period: 51
- Double chance: 44
- Correct score: 44
- Both teams to score: 42

## Bet365 market types found

- Goals total / Over-Under: 249
- Other / Unknown: 174
- Handicap / Spread: 136
- Half-time / Period: 51
- 1X2 / Match result: 44
- Double chance: 44
- Correct score: 44
- Both teams to score: 42

## Most common Bet365 market names

- ML: 44
- Draw No Bet: 44
- Double Chance: 44
- Spread: 44
- Totals: 44
- Goals Over/Under: 44
- Spread HT: 44
- Half Time Result: 44
- Correct Score: 44
- Totals HT: 37
- Corners Totals: 28
- Corners Totals HT: 28
- Corners: 28
- Corners 2-Way: 28
- Both Teams To Score: 14
- European Handicap: 14
- Alternative Total Goals: 14
- Alternative Goal Line: 14
- Team Total Goals Home: 14
- Alternative Asian Handicap: 14
- Both Teams To Score 2H: 14
- Exact Total Goals: 14
- Specials: 14
- 1st Half Handicap: 14
- Both Teams To Score HT: 14
- Team Total Goals Away: 14
- Number of Goals In Match: 14
- Alternative Corners: 12
- Total Corners: 12
- 1st Half Goal Line: 7

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.