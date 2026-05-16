# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 1699
Unique bookmakers: 2
Unique market names: 36
Bet365 market rows: 1532

## Market types found

- Goals total / Over-Under: 523
- Handicap / Spread: 360
- Other / Unknown: 278
- Half-time / Period: 141
- 1X2 / Match result: 136
- Correct score: 110
- Double chance: 109
- Both teams to score: 42

## Bet365 market types found

- Goals total / Over-Under: 466
- Other / Unknown: 278
- Handicap / Spread: 276
- Half-time / Period: 141
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 109
- Both teams to score: 42

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Correct Score: 110
- Half Time Result: 110
- Double Chance: 109
- Totals HT: 78
- Corners Totals: 45
- Corners Totals HT: 45
- Corners: 45
- Corners 2-Way: 45
- 1st Half Goal Line: 31
- Alternative Goal Line: 22
- Alternative Asian Handicap: 22
- European Handicap: 16
- Team Total Goals Home: 16
- Specials: 16
- Exact Total Goals: 16
- Total Corners: 16
- Alternative Corners: 16
- Team Total Goals Away: 16
- Number of Goals In Match: 16
- Both Teams To Score: 14
- Both Teams To Score 2H: 14
- Both Teams To Score HT: 14
- Alternative Total Goals: 14
- 1st Half Handicap: 14

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.