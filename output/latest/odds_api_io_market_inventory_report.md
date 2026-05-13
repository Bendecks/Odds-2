# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 1861
Unique bookmakers: 2
Unique market names: 44
Bet365 market rows: 1730

## Market types found

- Goals total / Over-Under: 558
- Handicap / Spread: 400
- Other / Unknown: 359
- 1X2 / Match result: 126
- Half-time / Period: 122
- Correct score: 110
- Double chance: 108
- Both teams to score: 78

## Bet365 market types found

- Goals total / Over-Under: 512
- Other / Unknown: 359
- Handicap / Spread: 331
- Half-time / Period: 122
- 1X2 / Match result: 110
- Correct score: 110
- Double chance: 108
- Both teams to score: 78

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Correct Score: 110
- Half Time Result: 110
- Double Chance: 108
- Spread HT: 108
- Totals HT: 96
- Alternative Asian Handicap: 51
- Alternative Goal Line: 47
- Corners Totals: 36
- Corners Totals HT: 36
- Corners 2-Way: 36
- Corners: 36
- Both Teams To Score: 26
- Team Total Goals Home: 26
- Alternative Total Goals: 26
- Team Total Goals Away: 26
- Both Teams To Score 2H: 26
- Exact Total Goals: 26
- Specials: 26
- 1st Half Handicap: 26
- Both Teams To Score HT: 26
- Number of Goals In Match: 26
- European Handicap: 24
- Total Corners: 20
- Alternative Corners: 20
- Method of Victory: 13

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.