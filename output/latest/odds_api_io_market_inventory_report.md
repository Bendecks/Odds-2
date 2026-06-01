# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 106
Market rows seen: 2389
Unique bookmakers: 2
Unique market names: 59
Bet365 market rows: 2239

## Market types found

- Goals total / Over-Under: 698
- Other / Unknown: 621
- Handicap / Spread: 485
- 1X2 / Match result: 137
- Half-time / Period: 122
- Both teams to score: 120
- Double chance: 103
- Correct score: 103

## Bet365 market types found

- Goals total / Over-Under: 648
- Other / Unknown: 621
- Handicap / Spread: 416
- Half-time / Period: 122
- Both teams to score: 120
- 1X2 / Match result: 106
- Double chance: 103
- Correct score: 103

## Most common Bet365 market names

- ML: 106
- Spread: 106
- Totals: 106
- Spread HT: 106
- Goals Over/Under: 105
- Half Time Result: 105
- Draw No Bet: 103
- Double Chance: 103
- Correct Score: 103
- Totals HT: 88
- Alternative Goal Line: 84
- Alternative Asian Handicap: 84
- Corners Totals: 76
- Corners Totals HT: 71
- Corners: 71
- Corners 2-Way: 71
- Both Teams To Score: 40
- European Handicap: 40
- 1st Half Handicap: 40
- Team Total Goals Away: 40
- Alternative Corners: 40
- Number of Goals In Match: 40
- Specials: 40
- Both Teams To Score 2H: 40
- Both Teams To Score HT: 40
- Exact Total Goals: 40
- Alternative Total Goals: 40
- Team Total Goals Home: 40
- Total Corners: 40
- First 10 Minutes (00:00 - 09:59): 20

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.