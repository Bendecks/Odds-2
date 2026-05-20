# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2160
Unique bookmakers: 2
Unique market names: 43
Bet365 market rows: 2004

## Market types found

- Goals total / Over-Under: 682
- Other / Unknown: 484
- Handicap / Spread: 419
- 1X2 / Match result: 129
- Half-time / Period: 124
- Double chance: 109
- Correct score: 108
- Both teams to score: 105

## Bet365 market types found

- Goals total / Over-Under: 613
- Other / Unknown: 484
- Handicap / Spread: 351
- Half-time / Period: 124
- 1X2 / Match result: 110
- Double chance: 109
- Correct score: 108
- Both teams to score: 105

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- Double Chance: 109
- Correct Score: 108
- Totals HT: 96
- Corners Totals: 65
- Corners 2-Way: 65
- Corners Totals HT: 63
- Corners: 63
- Both Teams To Score: 35
- European Handicap: 35
- Specials: 35
- Team Total Goals Home: 35
- Both Teams To Score HT: 35
- Number of Goals In Match: 35
- Alternative Total Goals: 35
- Exact Total Goals: 35
- Both Teams To Score 2H: 35
- 1st Half Handicap: 35
- Team Total Goals Away: 35
- Alternative Goal Line: 31
- Alternative Asian Handicap: 31
- Total Corners: 29
- Alternative Corners: 29
- Method of Victory: 17

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.