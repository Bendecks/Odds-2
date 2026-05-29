# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2336
Unique bookmakers: 2
Unique market names: 42
Bet365 market rows: 2234

## Market types found

- Goals total / Over-Under: 697
- Other / Unknown: 540
- Handicap / Spread: 478
- Both teams to score: 147
- Half-time / Period: 132
- 1X2 / Match result: 122
- Double chance: 110
- Correct score: 110

## Bet365 market types found

- Goals total / Over-Under: 654
- Other / Unknown: 540
- Handicap / Spread: 431
- Both teams to score: 147
- Half-time / Period: 132
- 1X2 / Match result: 110
- Double chance: 110
- Correct score: 110

## Most common Bet365 market names

- ML: 110
- Double Chance: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Spread HT: 110
- Half Time Result: 110
- Correct Score: 110
- Draw No Bet: 109
- Alternative Goal Line: 93
- Alternative Asian Handicap: 93
- Totals HT: 88
- Corners Totals HT: 59
- Corners: 59
- Corners 2-Way: 59
- Corners Totals: 57
- Both Teams To Score: 49
- European Handicap: 49
- Team Total Goals Away: 49
- Both Teams To Score 2H: 49
- Alternative Total Goals: 49
- 1st Half Handicap: 49
- Exact Total Goals: 49
- Both Teams To Score HT: 49
- Number of Goals In Match: 49
- Specials: 49
- Team Total Goals Home: 49
- Total Corners: 34
- Alternative Corners: 34
- 1st Half Goal Line: 22

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.