# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 108
Market rows seen: 5162
Unique bookmakers: 2
Unique market names: 71
Bet365 market rows: 4983

## Market types found

- Other / Unknown: 2291
- Goals total / Over-Under: 1202
- Handicap / Spread: 897
- Both teams to score: 309
- 1X2 / Match result: 133
- Half-time / Period: 114
- Double chance: 108
- Correct score: 108

## Bet365 market types found

- Other / Unknown: 2291
- Goals total / Over-Under: 1110
- Handicap / Spread: 835
- Both teams to score: 309
- Half-time / Period: 114
- 1X2 / Match result: 108
- Double chance: 108
- Correct score: 108

## Most common Bet365 market names

- ML: 108
- Draw No Bet: 108
- Double Chance: 108
- Spread: 108
- Totals: 108
- Goals Over/Under: 108
- Corners Totals: 108
- Corners Totals HT: 108
- Half Time Result: 108
- Corners 2-Way: 108
- Corners: 108
- Correct Score: 108
- Spread HT: 104
- European Handicap: 104
- Exact Total Goals: 104
- Specials: 104
- Number of Goals In Match: 104
- Both Teams To Score: 103
- Team Total Goals Away: 103
- Team Total Goals Home: 103
- Alternative Asian Handicap: 103
- Alternative Corners: 103
- Both Teams To Score 2H: 103
- Total Corners: 103
- Both Teams To Score HT: 103
- Alternative Goal Line: 103
- Alternative Total Goals: 103
- 1st Half Handicap: 103
- First 10 Minutes (00:00 - 09:59): 100
- Totals HT: 98

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.