# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2851
Unique bookmakers: 2
Unique market names: 70
Bet365 market rows: 2710

## Market types found

- Goals total / Over-Under: 845
- Other / Unknown: 816
- Handicap / Spread: 539
- Both teams to score: 171
- 1X2 / Match result: 141
- Half-time / Period: 125
- Correct score: 108
- Double chance: 106

## Bet365 market types found

- Other / Unknown: 816
- Goals total / Over-Under: 790
- Handicap / Spread: 484
- Both teams to score: 171
- Half-time / Period: 125
- 1X2 / Match result: 110
- Correct score: 108
- Double chance: 106

## Most common Bet365 market names

- ML: 110
- Spread: 110
- Totals: 110
- Spread HT: 109
- Draw No Bet: 108
- Goals Over/Under: 108
- Half Time Result: 108
- Correct Score: 108
- Double Chance: 106
- Totals HT: 95
- Corners Totals: 91
- Alternative Asian Handicap: 91
- Alternative Goal Line: 91
- Corners Totals HT: 87
- Corners: 87
- Corners 2-Way: 87
- Both Teams To Score: 57
- European Handicap: 57
- Team Total Goals Home: 57
- Team Total Goals Away: 57
- Specials: 57
- Both Teams To Score 2H: 57
- Number of Goals In Match: 57
- 1st Half Handicap: 57
- Both Teams To Score HT: 57
- Alternative Total Goals: 57
- Exact Total Goals: 57
- Alternative Corners: 55
- Total Corners: 55
- First 10 Minutes (00:00 - 09:59): 25

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.