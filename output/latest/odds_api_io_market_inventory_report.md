# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2506
Unique bookmakers: 2
Unique market names: 46
Bet365 market rows: 2363

## Market types found

- Goals total / Over-Under: 751
- Other / Unknown: 694
- Handicap / Spread: 455
- 1X2 / Match result: 133
- Both teams to score: 129
- Half-time / Period: 124
- Double chance: 110
- Correct score: 110

## Bet365 market types found

- Goals total / Over-Under: 695
- Other / Unknown: 694
- Handicap / Spread: 391
- Both teams to score: 129
- Half-time / Period: 124
- 1X2 / Match result: 110
- Double chance: 110
- Correct score: 110

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Double Chance: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Correct Score: 110
- Half Time Result: 110
- Totals HT: 96
- Corners Totals: 86
- Corners: 82
- Corners 2-Way: 82
- Corners Totals HT: 80
- Both Teams To Score: 43
- European Handicap: 43
- 1st Half Handicap: 43
- Alternative Asian Handicap: 43
- Both Teams To Score HT: 43
- Specials: 43
- Team Total Goals Away: 43
- Alternative Goal Line: 43
- Both Teams To Score 2H: 43
- Alternative Total Goals: 43
- Number of Goals In Match: 43
- Exact Total Goals: 43
- Team Total Goals Home: 43
- Total Corners: 41
- Alternative Corners: 41
- First 10 Minutes (00:00 - 09:59): 28

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.