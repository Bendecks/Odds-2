# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2231
Unique bookmakers: 2
Unique market names: 52
Bet365 market rows: 2111

## Market types found

- Goals total / Over-Under: 653
- Other / Unknown: 536
- Handicap / Spread: 480
- Half-time / Period: 125
- 1X2 / Match result: 122
- Both teams to score: 108
- Double chance: 105
- Correct score: 102

## Bet365 market types found

- Goals total / Over-Under: 607
- Other / Unknown: 536
- Handicap / Spread: 418
- Half-time / Period: 125
- 1X2 / Match result: 110
- Both teams to score: 108
- Double chance: 105
- Correct score: 102

## Most common Bet365 market names

- ML: 110
- Spread: 110
- Totals: 110
- Spread HT: 110
- Goals Over/Under: 108
- Half Time Result: 108
- Double Chance: 105
- Draw No Bet: 104
- Correct Score: 102
- Totals HT: 95
- Alternative Asian Handicap: 84
- Alternative Goal Line: 84
- Corners Totals: 53
- Corners Totals HT: 53
- Corners: 53
- Corners 2-Way: 53
- Alternative Corners: 40
- Total Corners: 40
- Both Teams To Score: 36
- European Handicap: 36
- Both Teams To Score 2H: 36
- 1st Half Handicap: 36
- Team Total Goals Away: 36
- Alternative Total Goals: 36
- Specials: 36
- Both Teams To Score HT: 36
- Exact Total Goals: 36
- Number of Goals In Match: 36
- Team Total Goals Home: 36
- Corners Spread: 17

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.