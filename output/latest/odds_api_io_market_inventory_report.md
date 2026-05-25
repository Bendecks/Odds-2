# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2777
Unique bookmakers: 2
Unique market names: 69
Bet365 market rows: 2629

## Market types found

- Other / Unknown: 814
- Goals total / Over-Under: 801
- Handicap / Spread: 533
- Both teams to score: 156
- Half-time / Period: 131
- 1X2 / Match result: 122
- Double chance: 110
- Correct score: 110

## Bet365 market types found

- Other / Unknown: 814
- Goals total / Over-Under: 729
- Handicap / Spread: 469
- Both teams to score: 156
- Half-time / Period: 131
- 1X2 / Match result: 110
- Double chance: 110
- Correct score: 110

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 110
- Double Chance: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- Correct Score: 110
- Totals HT: 89
- Alternative Goal Line: 81
- Alternative Asian Handicap: 81
- Corners Totals: 80
- Corners Totals HT: 80
- Corners: 80
- Corners 2-Way: 80
- Both Teams To Score: 52
- European Handicap: 52
- Team Total Goals Away: 52
- 1st Half Handicap: 52
- Both Teams To Score HT: 52
- Both Teams To Score 2H: 52
- Alternative Total Goals: 52
- Exact Total Goals: 52
- Team Total Goals Home: 52
- Specials: 52
- Number of Goals In Match: 52
- Alternative Corners: 50
- Total Corners: 50
- Anytime Goalscorer: 37

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.