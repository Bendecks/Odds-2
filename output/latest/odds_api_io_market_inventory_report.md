# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 10
Events seen in raw odds: 50
Market rows seen: 1126
Unique bookmakers: 2
Unique market names: 45
Bet365 market rows: 1074

## Market types found

- Goals total / Over-Under: 355
- Other / Unknown: 286
- Handicap / Spread: 212
- Both teams to score: 69
- 1X2 / Match result: 55
- Half-time / Period: 53
- Double chance: 48
- Correct score: 48

## Bet365 market types found

- Goals total / Over-Under: 327
- Other / Unknown: 286
- Handicap / Spread: 193
- Both teams to score: 69
- Half-time / Period: 53
- 1X2 / Match result: 50
- Double chance: 48
- Correct score: 48

## Most common Bet365 market names

- ML: 50
- Spread: 50
- Totals: 50
- Spread HT: 50
- Draw No Bet: 48
- Double Chance: 48
- Goals Over/Under: 48
- Correct Score: 48
- Half Time Result: 48
- Totals HT: 47
- Alternative Asian Handicap: 35
- Alternative Goal Line: 35
- Corners Totals: 35
- Corners Totals HT: 35
- Corners 2-Way: 35
- Corners: 35
- Both Teams To Score: 23
- European Handicap: 23
- Specials: 23
- Both Teams To Score 2H: 23
- Number of Goals In Match: 23
- Team Total Goals Home: 23
- Both Teams To Score HT: 23
- Alternative Total Goals: 23
- Exact Total Goals: 23
- Team Total Goals Away: 23
- 1st Half Handicap: 23
- Total Corners: 20
- Alternative Corners: 20
- First 10 Minutes (00:00 - 09:59): 13

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.