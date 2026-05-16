# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 3008
Unique bookmakers: 2
Unique market names: 63
Bet365 market rows: 2816

## Market types found

- Other / Unknown: 985
- Goals total / Over-Under: 827
- Handicap / Spread: 576
- Both teams to score: 156
- 1X2 / Match result: 139
- Half-time / Period: 121
- Double chance: 102
- Correct score: 102

## Bet365 market types found

- Other / Unknown: 985
- Goals total / Over-Under: 748
- Handicap / Spread: 493
- Both teams to score: 156
- Half-time / Period: 121
- 1X2 / Match result: 109
- Double chance: 102
- Correct score: 102

## Most common Bet365 market names

- ML: 109
- Spread: 109
- Totals: 109
- Spread HT: 105
- Draw No Bet: 102
- Double Chance: 102
- Goals Over/Under: 102
- Half Time Result: 102
- Correct Score: 102
- Totals HT: 93
- Corners Totals: 82
- Corners 2-Way: 82
- Corners: 82
- Corners Totals HT: 80
- Alternative Goal Line: 63
- Alternative Asian Handicap: 63
- Both Teams To Score: 52
- European Handicap: 52
- Alternative Total Goals: 52
- Team Total Goals Away: 52
- Number of Goals In Match: 52
- Team Total Goals Home: 52
- Both Teams To Score 2H: 52
- Both Teams To Score HT: 52
- Exact Total Goals: 52
- Specials: 52
- 1st Half Handicap: 52
- Total Corners: 50
- Alternative Corners: 50
- Corners Spread: 32

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.