# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 10
Events seen in raw odds: 50
Market rows seen: 1083
Unique bookmakers: 2
Unique market names: 43
Bet365 market rows: 1031

## Market types found

- Goals total / Over-Under: 336
- Other / Unknown: 257
- Handicap / Spread: 217
- Both teams to score: 66
- 1X2 / Match result: 56
- Half-time / Period: 51
- Double chance: 50
- Correct score: 50

## Bet365 market types found

- Goals total / Over-Under: 319
- Other / Unknown: 257
- Handicap / Spread: 188
- Both teams to score: 66
- Half-time / Period: 51
- 1X2 / Match result: 50
- Double chance: 50
- Correct score: 50

## Most common Bet365 market names

- ML: 50
- Draw No Bet: 50
- Double Chance: 50
- Spread: 50
- Totals: 50
- Goals Over/Under: 50
- Spread HT: 50
- Correct Score: 50
- Half Time Result: 50
- Totals HT: 49
- Corners Totals: 32
- Corners Totals HT: 32
- Corners: 32
- Corners 2-Way: 32
- Alternative Asian Handicap: 32
- Alternative Goal Line: 31
- Both Teams To Score: 22
- European Handicap: 22
- 1st Half Handicap: 22
- Alternative Total Goals: 22
- Both Teams To Score HT: 22
- Team Total Goals Away: 22
- Specials: 22
- Both Teams To Score 2H: 22
- Exact Total Goals: 22
- Number of Goals In Match: 22
- Team Total Goals Home: 22
- Alternative Corners: 18
- Total Corners: 18
- First 10 Minutes (00:00 - 09:59): 12

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.