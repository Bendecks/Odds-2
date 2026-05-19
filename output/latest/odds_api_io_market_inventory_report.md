# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 108
Market rows seen: 2045
Unique bookmakers: 2
Unique market names: 49
Bet365 market rows: 1918

## Market types found

- Goals total / Over-Under: 648
- Other / Unknown: 438
- Handicap / Spread: 399
- 1X2 / Match result: 125
- Half-time / Period: 117
- Double chance: 108
- Correct score: 108
- Both teams to score: 102

## Bet365 market types found

- Goals total / Over-Under: 599
- Other / Unknown: 438
- Handicap / Spread: 338
- Half-time / Period: 117
- 1X2 / Match result: 108
- Double chance: 108
- Correct score: 108
- Both teams to score: 102

## Most common Bet365 market names

- ML: 108
- Draw No Bet: 108
- Double Chance: 108
- Spread: 108
- Totals: 108
- Goals Over/Under: 108
- Spread HT: 108
- Correct Score: 108
- Half Time Result: 108
- Totals HT: 99
- Corners Totals: 64
- Corners Totals HT: 58
- Corners 2-Way: 58
- Corners: 58
- Both Teams To Score: 34
- European Handicap: 34
- Alternative Goal Line: 34
- Both Teams To Score HT: 34
- 1st Half Handicap: 34
- Number of Goals In Match: 34
- Team Total Goals Away: 34
- Alternative Total Goals: 34
- Exact Total Goals: 34
- Alternative Asian Handicap: 34
- Specials: 34
- Team Total Goals Home: 34
- Both Teams To Score 2H: 34
- Total Corners: 24
- Alternative Corners: 24
- First 10 Minutes (00:00 - 09:59): 17

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.