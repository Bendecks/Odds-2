# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2963
Unique bookmakers: 2
Unique market names: 62
Bet365 market rows: 2838

## Market types found

- Other / Unknown: 864
- Goals total / Over-Under: 847
- Handicap / Spread: 577
- Both teams to score: 201
- 1X2 / Match result: 128
- Half-time / Period: 128
- Correct score: 110
- Double chance: 108

## Bet365 market types found

- Other / Unknown: 864
- Goals total / Over-Under: 802
- Handicap / Spread: 515
- Both teams to score: 201
- Half-time / Period: 128
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
- Half Time Result: 110
- Correct Score: 110
- Double Chance: 108
- Totals HT: 92
- Alternative Goal Line: 91
- Alternative Asian Handicap: 91
- Corners Totals: 80
- Corners Totals HT: 80
- Corners: 80
- Corners 2-Way: 80
- Both Teams To Score: 67
- European Handicap: 67
- Number of Goals In Match: 67
- 1st Half Handicap: 67
- Exact Total Goals: 67
- Team Total Goals Away: 67
- Specials: 67
- Both Teams To Score 2H: 67
- Both Teams To Score HT: 67
- Alternative Total Goals: 67
- Team Total Goals Home: 67
- Total Corners: 55
- Alternative Corners: 55
- Corners Spread: 28

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.