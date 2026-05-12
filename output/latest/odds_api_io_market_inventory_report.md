# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 4632
Unique bookmakers: 2
Unique market names: 71
Bet365 market rows: 4462

## Market types found

- Other / Unknown: 1955
- Goals total / Over-Under: 1119
- Handicap / Spread: 805
- Both teams to score: 282
- 1X2 / Match result: 134
- Half-time / Period: 118
- Double chance: 110
- Correct score: 109

## Bet365 market types found

- Other / Unknown: 1955
- Goals total / Over-Under: 1043
- Handicap / Spread: 736
- Both teams to score: 282
- Half-time / Period: 118
- Double chance: 110
- 1X2 / Match result: 109
- Correct score: 109

## Most common Bet365 market names

- Double Chance: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- ML: 109
- Draw No Bet: 109
- Correct Score: 109
- Corners Totals: 105
- Corners: 105
- Corners 2-Way: 105
- Totals HT: 102
- Corners Totals HT: 101
- European Handicap: 96
- Specials: 96
- Number of Goals In Match: 96
- Exact Total Goals: 96
- Alternative Corners: 96
- Alternative Asian Handicap: 96
- Alternative Goal Line: 96
- Total Corners: 96
- Both Teams To Score: 94
- Alternative Total Goals: 94
- Team Total Goals Away: 94
- Both Teams To Score HT: 94
- 1st Half Handicap: 94
- Team Total Goals Home: 94
- Both Teams To Score 2H: 94
- First 10 Minutes (00:00 - 09:59): 91

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.