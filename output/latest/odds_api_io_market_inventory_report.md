# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2745
Unique bookmakers: 2
Unique market names: 71
Bet365 market rows: 2602

## Market types found

- Other / Unknown: 898
- Goals total / Over-Under: 740
- Handicap / Spread: 531
- Both teams to score: 123
- 1X2 / Match result: 122
- Half-time / Period: 115
- Double chance: 110
- Correct score: 106

## Bet365 market types found

- Other / Unknown: 898
- Goals total / Over-Under: 679
- Handicap / Spread: 461
- Both teams to score: 123
- Half-time / Period: 115
- 1X2 / Match result: 110
- Double chance: 110
- Correct score: 106

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Double Chance: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- Correct Score: 106
- Totals HT: 105
- Alternative Asian Handicap: 78
- Alternative Goal Line: 78
- Corners Totals: 69
- Corners Totals HT: 65
- Corners 2-Way: 65
- Corners: 65
- European Handicap: 42
- Number of Goals In Match: 42
- Exact Total Goals: 42
- Specials: 42
- Team Total Goals Away: 42
- Team Total Goals Home: 42
- Both Teams To Score: 41
- Alternative Total Goals: 41
- Both Teams To Score 2H: 41
- 1st Half Handicap: 41
- Both Teams To Score HT: 41
- Alternative Corners: 37
- Total Corners: 37
- First 10 Minutes (00:00 - 09:59): 34

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.