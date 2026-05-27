# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 1792
Unique bookmakers: 2
Unique market names: 32
Bet365 market rows: 1717

## Market types found

- Goals total / Over-Under: 570
- Other / Unknown: 405
- Handicap / Spread: 344
- 1X2 / Match result: 114
- Half-time / Period: 105
- Double chance: 95
- Correct score: 93
- Both teams to score: 66

## Bet365 market types found

- Goals total / Over-Under: 544
- Other / Unknown: 405
- Handicap / Spread: 314
- Half-time / Period: 105
- 1X2 / Match result: 95
- Double chance: 95
- Correct score: 93
- Both teams to score: 66

## Most common Bet365 market names

- ML: 95
- Double Chance: 95
- Spread: 95
- Totals: 95
- Goals Over/Under: 95
- Spread HT: 95
- Half Time Result: 95
- Draw No Bet: 93
- Correct Score: 93
- Totals HT: 85
- Corners Totals: 82
- Corners Totals HT: 80
- Corners 2-Way: 80
- Corners: 80
- Alternative Goal Line: 80
- Alternative Asian Handicap: 80
- Both Teams To Score: 22
- European Handicap: 22
- Both Teams To Score HT: 22
- Exact Total Goals: 22
- Team Total Goals Home: 22
- 1st Half Handicap: 22
- Alternative Total Goals: 22
- Number of Goals In Match: 22
- Specials: 22
- Both Teams To Score 2H: 22
- Team Total Goals Away: 22
- Alternative Corners: 19
- Total Corners: 19
- 1st Half Goal Line: 10

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.