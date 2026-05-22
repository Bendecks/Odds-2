# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 1994
Unique bookmakers: 2
Unique market names: 36
Bet365 market rows: 1850

## Market types found

- Goals total / Over-Under: 635
- Other / Unknown: 429
- Handicap / Spread: 415
- Half-time / Period: 126
- 1X2 / Match result: 117
- Correct score: 110
- Double chance: 108
- Both teams to score: 54

## Bet365 market types found

- Goals total / Over-Under: 570
- Other / Unknown: 429
- Handicap / Spread: 343
- Half-time / Period: 126
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 108
- Both teams to score: 54

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
- Totals HT: 94
- Corners Totals: 83
- Corners Totals HT: 83
- Corners 2-Way: 83
- Corners: 83
- Alternative Asian Handicap: 75
- Alternative Goal Line: 75
- Both Teams To Score: 18
- European Handicap: 18
- Number of Goals In Match: 18
- Total Corners: 18
- Alternative Total Goals: 18
- Both Teams To Score 2H: 18
- Both Teams To Score HT: 18
- Team Total Goals Home: 18
- Alternative Corners: 18
- Exact Total Goals: 18
- 1st Half Handicap: 18
- Specials: 18
- Team Total Goals Away: 18
- 1st Half Goal Line: 16

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.