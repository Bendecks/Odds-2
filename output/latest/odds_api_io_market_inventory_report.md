# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2157
Unique bookmakers: 2
Unique market names: 59
Bet365 market rows: 1981

## Market types found

- Goals total / Over-Under: 641
- Other / Unknown: 498
- Handicap / Spread: 431
- 1X2 / Match result: 140
- Half-time / Period: 135
- Correct score: 110
- Double chance: 109
- Both teams to score: 93

## Bet365 market types found

- Goals total / Over-Under: 582
- Other / Unknown: 498
- Handicap / Spread: 344
- Half-time / Period: 135
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 109
- Both teams to score: 93

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Half Time Result: 110
- Correct Score: 110
- Double Chance: 109
- Spread HT: 109
- Totals HT: 84
- Corners: 67
- Corners 2-Way: 67
- Corners Totals: 65
- Corners Totals HT: 59
- Both Teams To Score: 31
- European Handicap: 31
- Alternative Asian Handicap: 31
- Alternative Goal Line: 31
- Team Total Goals Home: 31
- 1st Half Handicap: 31
- Exact Total Goals: 31
- Both Teams To Score HT: 31
- Both Teams To Score 2H: 31
- Alternative Total Goals: 31
- Number of Goals In Match: 31
- Specials: 31
- Team Total Goals Away: 31
- Total Corners: 28
- Alternative Corners: 28
- 1st Half Goal Line: 25

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.