# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2593
Unique bookmakers: 2
Unique market names: 62
Bet365 market rows: 2425

## Market types found

- Goals total / Over-Under: 823
- Other / Unknown: 644
- Handicap / Spread: 492
- Both teams to score: 153
- 1X2 / Match result: 140
- Half-time / Period: 123
- Correct score: 110
- Double chance: 108

## Bet365 market types found

- Goals total / Over-Under: 751
- Other / Unknown: 644
- Handicap / Spread: 426
- Both teams to score: 153
- Half-time / Period: 123
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 108

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Correct Score: 110
- Half Time Result: 110
- Double Chance: 108
- Totals HT: 97
- Corners Totals: 91
- Corners Totals HT: 89
- Corners: 89
- Corners 2-Way: 89
- Alternative Goal Line: 80
- Alternative Asian Handicap: 80
- Both Teams To Score: 51
- European Handicap: 51
- 1st Half Handicap: 51
- Both Teams To Score 2H: 51
- Team Total Goals Home: 51
- Specials: 51
- Number of Goals In Match: 51
- Both Teams To Score HT: 51
- Alternative Total Goals: 51
- Exact Total Goals: 51
- Team Total Goals Away: 51
- Alternative Corners: 48
- Total Corners: 48
- First 10 Minutes (00:00 - 09:59): 18

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.