# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2382
Unique bookmakers: 2
Unique market names: 39
Bet365 market rows: 2252

## Market types found

- Goals total / Over-Under: 738
- Other / Unknown: 561
- Handicap / Spread: 490
- Half-time / Period: 131
- 1X2 / Match result: 124
- Both teams to score: 120
- Correct score: 110
- Double chance: 108

## Bet365 market types found

- Goals total / Over-Under: 689
- Other / Unknown: 561
- Handicap / Spread: 423
- Half-time / Period: 131
- Both teams to score: 120
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 108

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Correct Score: 110
- Half Time Result: 110
- Double Chance: 108
- Alternative Asian Handicap: 105
- Alternative Goal Line: 105
- Corners Totals: 92
- Corners Totals HT: 92
- Corners: 92
- Corners 2-Way: 92
- Totals HT: 87
- Both Teams To Score: 40
- European Handicap: 40
- Number of Goals In Match: 40
- Alternative Total Goals: 40
- Specials: 40
- Both Teams To Score HT: 40
- 1st Half Handicap: 40
- Both Teams To Score 2H: 40
- Team Total Goals Home: 40
- Team Total Goals Away: 40
- Exact Total Goals: 40
- Alternative Corners: 38
- Total Corners: 38
- 1st Half Goal Line: 21

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.