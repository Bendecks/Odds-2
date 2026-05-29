# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2150
Unique bookmakers: 2
Unique market names: 39
Bet365 market rows: 1983

## Market types found

- Goals total / Over-Under: 681
- Other / Unknown: 464
- Handicap / Spread: 435
- 1X2 / Match result: 142
- Half-time / Period: 124
- Correct score: 108
- Double chance: 106
- Both teams to score: 90

## Bet365 market types found

- Goals total / Over-Under: 608
- Other / Unknown: 464
- Handicap / Spread: 375
- Half-time / Period: 124
- 1X2 / Match result: 108
- Correct score: 108
- Double chance: 106
- Both teams to score: 90

## Most common Bet365 market names

- ML: 108
- Spread: 108
- Totals: 108
- Goals Over/Under: 108
- Spread HT: 108
- Correct Score: 108
- Half Time Result: 108
- Draw No Bet: 106
- Double Chance: 106
- Totals HT: 92
- Alternative Asian Handicap: 91
- Alternative Goal Line: 91
- Corners Totals HT: 78
- Corners: 78
- Corners 2-Way: 78
- Corners Totals: 77
- Both Teams To Score: 30
- European Handicap: 30
- Team Total Goals Home: 30
- Both Teams To Score HT: 30
- Number of Goals In Match: 30
- Team Total Goals Away: 30
- 1st Half Handicap: 30
- Both Teams To Score 2H: 30
- Specials: 30
- Alternative Total Goals: 30
- Exact Total Goals: 30
- Total Corners: 25
- Alternative Corners: 25
- 1st Half Goal Line: 16

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.