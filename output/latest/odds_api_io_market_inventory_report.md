# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 104
Market rows seen: 2074
Unique bookmakers: 2
Unique market names: 58
Bet365 market rows: 1978

## Market types found

- Goals total / Over-Under: 598
- Other / Unknown: 532
- Handicap / Spread: 410
- 1X2 / Match result: 125
- Half-time / Period: 124
- Correct score: 102
- Double chance: 99
- Both teams to score: 84

## Bet365 market types found

- Goals total / Over-Under: 566
- Other / Unknown: 532
- Handicap / Spread: 367
- Half-time / Period: 124
- 1X2 / Match result: 104
- Correct score: 102
- Double chance: 99
- Both teams to score: 84

## Most common Bet365 market names

- ML: 104
- Draw No Bet: 102
- Spread: 102
- Totals: 102
- Goals Over/Under: 102
- Spread HT: 102
- Correct Score: 102
- Half Time Result: 102
- Double Chance: 99
- Alternative Asian Handicap: 91
- Alternative Goal Line: 91
- Totals HT: 80
- Corners Totals: 71
- Corners Totals HT: 71
- Corners: 71
- Corners 2-Way: 71
- Alternative Corners: 28
- Total Corners: 28
- Both Teams To Score: 28
- European Handicap: 28
- Specials: 28
- Team Total Goals Away: 28
- 1st Half Handicap: 28
- Both Teams To Score 2H: 28
- Team Total Goals Home: 28
- Number of Goals In Match: 28
- Both Teams To Score HT: 28
- Alternative Total Goals: 28
- Exact Total Goals: 28
- 1st Half Goal Line: 22

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.