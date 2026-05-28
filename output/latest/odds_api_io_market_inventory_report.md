# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 1858
Unique bookmakers: 2
Unique market names: 50
Bet365 market rows: 1812

## Market types found

- Goals total / Over-Under: 557
- Other / Unknown: 417
- Handicap / Spread: 365
- Half-time / Period: 124
- 1X2 / Match result: 116
- Correct score: 109
- Double chance: 107
- Both teams to score: 63

## Bet365 market types found

- Goals total / Over-Under: 535
- Other / Unknown: 417
- Handicap / Spread: 347
- Half-time / Period: 124
- 1X2 / Match result: 110
- Correct score: 109
- Double chance: 107
- Both teams to score: 63

## Most common Bet365 market names

- ML: 110
- Totals: 110
- Spread HT: 110
- Draw No Bet: 109
- Goals Over/Under: 109
- Half Time Result: 109
- Correct Score: 109
- Spread: 108
- Double Chance: 107
- Totals HT: 96
- Alternative Goal Line: 83
- Alternative Asian Handicap: 83
- Corners Totals: 62
- Corners Totals HT: 58
- Corners 2-Way: 58
- Corners: 58
- Both Teams To Score: 21
- European Handicap: 21
- Alternative Total Goals: 21
- Team Total Goals Home: 21
- Exact Total Goals: 21
- 1st Half Handicap: 21
- Number of Goals In Match: 21
- Specials: 21
- Both Teams To Score 2H: 21
- Both Teams To Score HT: 21
- Team Total Goals Away: 21
- Alternative Corners: 16
- Total Corners: 16
- 1st Half Goal Line: 14

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.