# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 80
Market rows seen: 1178
Unique bookmakers: 2
Unique market names: 41
Bet365 market rows: 1053

## Market types found

- Goals total / Over-Under: 351
- Handicap / Spread: 241
- Other / Unknown: 216
- Half-time / Period: 103
- 1X2 / Match result: 89
- Double chance: 71
- Correct score: 71
- Both teams to score: 36

## Bet365 market types found

- Goals total / Over-Under: 303
- Other / Unknown: 216
- Handicap / Spread: 182
- Half-time / Period: 103
- 1X2 / Match result: 71
- Double chance: 71
- Correct score: 71
- Both teams to score: 36

## Most common Bet365 market names

- ML: 71
- Draw No Bet: 71
- Double Chance: 71
- Spread: 71
- Totals: 71
- Goals Over/Under: 71
- Spread HT: 71
- Correct Score: 71
- Half Time Result: 71
- Totals HT: 39
- 1st Half Goal Line: 32
- Corners Totals: 32
- Corners Totals HT: 32
- Corners: 32
- Corners 2-Way: 32
- Both Teams To Score: 12
- European Handicap: 12
- Both Teams To Score HT: 12
- Specials: 12
- Alternative Goal Line: 12
- Number of Goals In Match: 12
- Both Teams To Score 2H: 12
- Team Total Goals Away: 12
- Alternative Asian Handicap: 12
- Team Total Goals Home: 12
- 1st Half Handicap: 12
- Alternative Total Goals: 12
- Exact Total Goals: 12
- Method of Victory: 11
- Alternative Corners: 10

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.