# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 14
Events seen in raw odds: 42
Market rows seen: 735
Unique bookmakers: 2
Unique market names: 45
Bet365 market rows: 699

## Market types found

- Goals total / Over-Under: 221
- Other / Unknown: 179
- Handicap / Spread: 142
- 1X2 / Match result: 48
- Half-time / Period: 47
- Double chance: 40
- Correct score: 40
- Both teams to score: 18

## Bet365 market types found

- Goals total / Over-Under: 212
- Other / Unknown: 179
- Handicap / Spread: 121
- Half-time / Period: 47
- 1X2 / Match result: 42
- Double chance: 40
- Correct score: 40
- Both teams to score: 18

## Most common Bet365 market names

- ML: 42
- Spread: 42
- Totals: 42
- Spread HT: 42
- Draw No Bet: 40
- Double Chance: 40
- Goals Over/Under: 40
- Correct Score: 40
- Half Time Result: 40
- Totals HT: 37
- Corners Totals: 31
- Corners Totals HT: 31
- Corners 2-Way: 31
- Corners: 31
- Alternative Asian Handicap: 21
- Alternative Goal Line: 21
- Total Corners: 7
- Alternative Corners: 7
- Both Teams To Score: 6
- European Handicap: 6
- Exact Total Goals: 6
- Specials: 6
- Team Total Goals Away: 6
- Both Teams To Score HT: 6
- Number of Goals In Match: 6
- 1st Half Handicap: 6
- Both Teams To Score 2H: 6
- Alternative Total Goals: 6
- Team Total Goals Home: 6
- 1st Half Goal Line: 5

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.