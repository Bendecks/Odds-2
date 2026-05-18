# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2738
Unique bookmakers: 2
Unique market names: 50
Bet365 market rows: 2618

## Market types found

- Goals total / Over-Under: 863
- Other / Unknown: 699
- Handicap / Spread: 532
- Both teams to score: 192
- 1X2 / Match result: 123
- Half-time / Period: 113
- Double chance: 108
- Correct score: 108

## Bet365 market types found

- Goals total / Over-Under: 806
- Other / Unknown: 699
- Handicap / Spread: 482
- Both teams to score: 192
- Half-time / Period: 113
- 1X2 / Match result: 110
- Double chance: 108
- Correct score: 108

## Most common Bet365 market names

- ML: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- Double Chance: 108
- Correct Score: 108
- Draw No Bet: 106
- Totals HT: 105
- Alternative Asian Handicap: 94
- Alternative Goal Line: 94
- Corners Totals: 79
- Corners Totals HT: 79
- Corners: 79
- Corners 2-Way: 79
- European Handicap: 68
- Number of Goals In Match: 68
- Team Total Goals Away: 68
- Team Total Goals Home: 68
- Exact Total Goals: 68
- Specials: 68
- Both Teams To Score: 64
- Alternative Total Goals: 64
- Both Teams To Score 2H: 64
- 1st Half Handicap: 64
- Both Teams To Score HT: 64
- Alternative Corners: 55
- Total Corners: 53
- First 10 Minutes (00:00 - 09:59): 34

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.