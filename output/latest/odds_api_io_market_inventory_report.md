# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2456
Unique bookmakers: 2
Unique market names: 64
Bet365 market rows: 2323

## Market types found

- Goals total / Over-Under: 746
- Other / Unknown: 625
- Handicap / Spread: 485
- Both teams to score: 135
- 1X2 / Match result: 125
- Half-time / Period: 124
- Correct score: 110
- Double chance: 106

## Bet365 market types found

- Goals total / Over-Under: 703
- Other / Unknown: 625
- Handicap / Spread: 410
- Both teams to score: 135
- Half-time / Period: 124
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 106

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- Correct Score: 110
- Double Chance: 106
- Totals HT: 92
- Corners Totals: 83
- Corners Totals HT: 81
- Corners: 81
- Corners 2-Way: 81
- Alternative Asian Handicap: 70
- Alternative Goal Line: 68
- Both Teams To Score: 45
- European Handicap: 45
- Specials: 45
- Team Total Goals Home: 45
- Alternative Total Goals: 45
- Both Teams To Score 2H: 45
- Number of Goals In Match: 45
- 1st Half Handicap: 45
- Both Teams To Score HT: 45
- Team Total Goals Away: 45
- Alternative Corners: 45
- Total Corners: 45
- Exact Total Goals: 45
- First 10 Minutes (00:00 - 09:59): 17

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.