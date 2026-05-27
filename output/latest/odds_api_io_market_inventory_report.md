# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 108
Market rows seen: 1833
Unique bookmakers: 2
Unique market names: 32
Bet365 market rows: 1690

## Market types found

- Goals total / Over-Under: 578
- Handicap / Spread: 389
- Other / Unknown: 366
- 1X2 / Match result: 126
- Half-time / Period: 120
- Double chance: 108
- Correct score: 104
- Both teams to score: 42

## Bet365 market types found

- Goals total / Over-Under: 516
- Other / Unknown: 366
- Handicap / Spread: 326
- Half-time / Period: 120
- 1X2 / Match result: 108
- Double chance: 108
- Correct score: 104
- Both teams to score: 42

## Most common Bet365 market names

- ML: 108
- Double Chance: 108
- Spread: 108
- Totals: 108
- Goals Over/Under: 108
- Spread HT: 108
- Half Time Result: 108
- Draw No Bet: 104
- Correct Score: 104
- Totals HT: 96
- Alternative Goal Line: 82
- Alternative Asian Handicap: 82
- Corners Totals: 70
- Corners Totals HT: 68
- Corners 2-Way: 68
- Corners: 68
- Both Teams To Score: 14
- European Handicap: 14
- Alternative Total Goals: 14
- Both Teams To Score HT: 14
- Exact Total Goals: 14
- Team Total Goals Away: 14
- 1st Half Handicap: 14
- Both Teams To Score 2H: 14
- Number of Goals In Match: 14
- Specials: 14
- Team Total Goals Home: 14
- 1st Half Goal Line: 12
- Alternative Corners: 10
- Total Corners: 10

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.