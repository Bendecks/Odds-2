# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 1643
Unique bookmakers: 2
Unique market names: 36
Bet365 market rows: 1506

## Market types found

- Goals total / Over-Under: 476
- Handicap / Spread: 370
- Other / Unknown: 315
- Half-time / Period: 150
- 1X2 / Match result: 104
- Correct score: 101
- Double chance: 97
- Both teams to score: 30

## Bet365 market types found

- Goals total / Over-Under: 412
- Other / Unknown: 315
- Handicap / Spread: 300
- Half-time / Period: 150
- 1X2 / Match result: 101
- Correct score: 101
- Double chance: 97
- Both teams to score: 30

## Most common Bet365 market names

- ML: 101
- Spread: 101
- Totals: 101
- Goals Over/Under: 101
- Spread HT: 101
- Correct Score: 101
- Half Time Result: 101
- Draw No Bet: 97
- Double Chance: 97
- Alternative Asian Handicap: 74
- Alternative Goal Line: 72
- Corners Totals: 55
- Corners Totals HT: 55
- Corners: 55
- Corners 2-Way: 55
- Totals HT: 52
- 1st Half Goal Line: 49
- Both Teams To Score: 10
- European Handicap: 10
- 1st Half Handicap: 10
- Team Total Goals Away: 10
- Alternative Total Goals: 10
- Both Teams To Score 2H: 10
- Team Total Goals Home: 10
- Specials: 10
- Exact Total Goals: 10
- Both Teams To Score HT: 10
- Number of Goals In Match: 10
- Total Corners: 8
- Alternative Corners: 8

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.