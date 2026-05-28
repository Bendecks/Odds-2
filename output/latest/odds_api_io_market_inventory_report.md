# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 106
Market rows seen: 2228
Unique bookmakers: 2
Unique market names: 62
Bet365 market rows: 2089

## Market types found

- Other / Unknown: 650
- Goals total / Over-Under: 598
- Handicap / Spread: 449
- 1X2 / Match result: 127
- Half-time / Period: 122
- Correct score: 106
- Double chance: 104
- Both teams to score: 72

## Bet365 market types found

- Other / Unknown: 650
- Goals total / Over-Under: 540
- Handicap / Spread: 389
- Half-time / Period: 122
- 1X2 / Match result: 106
- Correct score: 106
- Double chance: 104
- Both teams to score: 72

## Most common Bet365 market names

- ML: 106
- Draw No Bet: 106
- Spread: 106
- Totals: 106
- Goals Over/Under: 106
- Spread HT: 106
- Correct Score: 106
- Half Time Result: 106
- Double Chance: 104
- Totals HT: 90
- Alternative Asian Handicap: 81
- Alternative Goal Line: 81
- Corners Totals: 57
- Corners Totals HT: 54
- Corners: 54
- Corners 2-Way: 54
- Both Teams To Score: 24
- European Handicap: 24
- Both Teams To Score 2H: 24
- Team Total Goals Home: 24
- Number of Goals In Match: 24
- Specials: 24
- 1st Half Handicap: 24
- Alternative Total Goals: 24
- Team Total Goals Away: 24
- Exact Total Goals: 24
- Both Teams To Score HT: 24
- Total Corners: 21
- Alternative Corners: 21
- First 10 Minutes (00:00 - 09:59): 18

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.