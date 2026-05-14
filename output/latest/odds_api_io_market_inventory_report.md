# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 108
Market rows seen: 2377
Unique bookmakers: 2
Unique market names: 44
Bet365 market rows: 2231

## Market types found

- Goals total / Over-Under: 722
- Other / Unknown: 566
- Handicap / Spread: 471
- Both teams to score: 141
- 1X2 / Match result: 132
- Half-time / Period: 131
- Correct score: 108
- Double chance: 106

## Bet365 market types found

- Goals total / Over-Under: 680
- Other / Unknown: 566
- Handicap / Spread: 391
- Both teams to score: 141
- Half-time / Period: 131
- 1X2 / Match result: 108
- Correct score: 108
- Double chance: 106

## Most common Bet365 market names

- ML: 108
- Draw No Bet: 108
- Spread: 108
- Totals: 108
- Goals Over/Under: 108
- Correct Score: 108
- Half Time Result: 108
- Double Chance: 106
- Spread HT: 106
- Totals HT: 83
- Corners Totals: 74
- Corners Totals HT: 74
- Corners 2-Way: 74
- Corners: 74
- Alternative Asian Handicap: 55
- Alternative Goal Line: 53
- Both Teams To Score: 47
- European Handicap: 47
- Team Total Goals Home: 47
- Number of Goals In Match: 47
- 1st Half Handicap: 47
- Both Teams To Score HT: 47
- Alternative Total Goals: 47
- Both Teams To Score 2H: 47
- Team Total Goals Away: 47
- Specials: 47
- Exact Total Goals: 47
- Total Corners: 45
- Alternative Corners: 45
- 1st Half Goal Line: 23

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.