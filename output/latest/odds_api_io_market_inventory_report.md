# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2809
Unique bookmakers: 2
Unique market names: 50
Bet365 market rows: 2656

## Market types found

- Goals total / Over-Under: 894
- Other / Unknown: 706
- Handicap / Spread: 538
- Both teams to score: 201
- 1X2 / Match result: 135
- Half-time / Period: 117
- Correct score: 110
- Double chance: 108

## Bet365 market types found

- Goals total / Over-Under: 840
- Other / Unknown: 706
- Handicap / Spread: 464
- Both teams to score: 201
- Half-time / Period: 117
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 108

## Most common Bet365 market names

- ML: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- Correct Score: 110
- Draw No Bet: 108
- Double Chance: 108
- Totals HT: 103
- Corners Totals: 89
- Corners Totals HT: 89
- Corners 2-Way: 89
- Corners: 89
- European Handicap: 71
- Exact Total Goals: 71
- Team Total Goals Home: 71
- Number of Goals In Match: 71
- Specials: 71
- Team Total Goals Away: 71
- Alternative Goal Line: 70
- Alternative Asian Handicap: 70
- Both Teams To Score: 67
- 1st Half Handicap: 67
- Both Teams To Score 2H: 67
- Alternative Total Goals: 67
- Both Teams To Score HT: 67
- Alternative Corners: 59
- Total Corners: 57
- First 10 Minutes (00:00 - 09:59): 33

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.