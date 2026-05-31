# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2315
Unique bookmakers: 2
Unique market names: 41
Bet365 market rows: 2174

## Market types found

- Goals total / Over-Under: 688
- Other / Unknown: 537
- Handicap / Spread: 482
- Half-time / Period: 145
- 1X2 / Match result: 128
- Both teams to score: 123
- Correct score: 108
- Double chance: 104

## Bet365 market types found

- Goals total / Over-Under: 629
- Other / Unknown: 537
- Handicap / Spread: 418
- Half-time / Period: 145
- Both teams to score: 123
- 1X2 / Match result: 110
- Correct score: 108
- Double chance: 104

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 108
- Spread: 108
- Totals: 108
- Goals Over/Under: 108
- Spread HT: 108
- Correct Score: 108
- Half Time Result: 108
- Double Chance: 104
- Alternative Goal Line: 100
- Alternative Asian Handicap: 100
- Corners Totals: 77
- Corners: 77
- Corners 2-Way: 77
- Corners Totals HT: 75
- Totals HT: 71
- Both Teams To Score: 41
- European Handicap: 41
- 1st Half Handicap: 41
- Specials: 41
- Team Total Goals Home: 41
- Both Teams To Score HT: 41
- Exact Total Goals: 41
- Both Teams To Score 2H: 41
- Team Total Goals Away: 41
- Alternative Total Goals: 41
- Number of Goals In Match: 41
- 1st Half Goal Line: 37
- Alternative Corners: 26
- Total Corners: 26

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.