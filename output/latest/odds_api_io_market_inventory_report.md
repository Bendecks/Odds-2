# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2081
Unique bookmakers: 2
Unique market names: 36
Bet365 market rows: 1938

## Market types found

- Goals total / Over-Under: 622
- Handicap / Spread: 448
- Other / Unknown: 422
- Half-time / Period: 149
- 1X2 / Match result: 128
- Double chance: 108
- Correct score: 108
- Both teams to score: 96

## Bet365 market types found

- Goals total / Over-Under: 577
- Other / Unknown: 422
- Handicap / Spread: 368
- Half-time / Period: 149
- 1X2 / Match result: 110
- Double chance: 108
- Correct score: 108
- Both teams to score: 96

## Most common Bet365 market names

- ML: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- Draw No Bet: 108
- Double Chance: 108
- Correct Score: 108
- Alternative Goal Line: 76
- Alternative Asian Handicap: 76
- Totals HT: 71
- Corners Totals: 63
- Corners Totals HT: 63
- Corners: 63
- Corners 2-Way: 63
- 1st Half Goal Line: 39
- Both Teams To Score: 32
- European Handicap: 32
- Team Total Goals Away: 32
- Team Total Goals Home: 32
- Both Teams To Score 2H: 32
- Exact Total Goals: 32
- Number of Goals In Match: 32
- Total Corners: 32
- Alternative Total Goals: 32
- Specials: 32
- 1st Half Handicap: 32
- Alternative Corners: 32
- Both Teams To Score HT: 32

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.