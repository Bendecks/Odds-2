# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2742
Unique bookmakers: 2
Unique market names: 70
Bet365 market rows: 2612

## Market types found

- Other / Unknown: 841
- Goals total / Over-Under: 772
- Handicap / Spread: 519
- Both teams to score: 150
- 1X2 / Match result: 134
- Half-time / Period: 116
- Double chance: 106
- Correct score: 104

## Bet365 market types found

- Other / Unknown: 841
- Goals total / Over-Under: 724
- Handicap / Spread: 461
- Both teams to score: 150
- Half-time / Period: 116
- 1X2 / Match result: 110
- Double chance: 106
- Correct score: 104

## Most common Bet365 market names

- ML: 110
- Goals Over/Under: 110
- Spread: 108
- Totals: 108
- Half Time Result: 108
- Double Chance: 106
- Spread HT: 106
- Draw No Bet: 104
- Correct Score: 104
- Totals HT: 100
- Alternative Asian Handicap: 83
- Alternative Goal Line: 83
- Corners Totals: 75
- Corners: 75
- Corners 2-Way: 75
- Corners Totals HT: 73
- Alternative Corners: 50
- Total Corners: 50
- Both Teams To Score: 50
- European Handicap: 50
- Number of Goals In Match: 50
- Exact Total Goals: 50
- Specials: 50
- Alternative Total Goals: 50
- Both Teams To Score HT: 50
- Team Total Goals Home: 50
- 1st Half Handicap: 50
- Both Teams To Score 2H: 50
- Team Total Goals Away: 50
- First 10 Minutes (00:00 - 09:59): 30

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.