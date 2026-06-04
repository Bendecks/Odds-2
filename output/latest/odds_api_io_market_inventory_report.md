# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2412
Unique bookmakers: 2
Unique market names: 64
Bet365 market rows: 2271

## Market types found

- Goals total / Over-Under: 691
- Other / Unknown: 688
- Handicap / Spread: 481
- 1X2 / Match result: 127
- Half-time / Period: 118
- Double chance: 110
- Correct score: 110
- Both teams to score: 87

## Bet365 market types found

- Other / Unknown: 688
- Goals total / Over-Under: 629
- Handicap / Spread: 419
- Half-time / Period: 118
- 1X2 / Match result: 110
- Double chance: 110
- Correct score: 110
- Both teams to score: 87

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
- Totals HT: 102
- Alternative Asian Handicap: 91
- Alternative Goal Line: 91
- Corners Totals: 77
- Corners Totals HT: 73
- Corners: 73
- Corners 2-Way: 73
- European Handicap: 31
- Alternative Total Goals: 31
- Exact Total Goals: 31
- Specials: 31
- 1st Half Handicap: 31
- Total Corners: 31
- Number of Goals In Match: 31
- Alternative Corners: 31
- Both Teams To Score: 29
- Team Total Goals Away: 29
- Team Total Goals Home: 29
- Both Teams To Score 2H: 29
- Both Teams To Score HT: 29
- First 10 Minutes (00:00 - 09:59): 21

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.