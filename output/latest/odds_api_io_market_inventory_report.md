# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 14
Events seen in raw odds: 62
Market rows seen: 1675
Unique bookmakers: 2
Unique market names: 64
Bet365 market rows: 1605

## Market types found

- Other / Unknown: 523
- Goals total / Over-Under: 485
- Handicap / Spread: 312
- Both teams to score: 96
- 1X2 / Match result: 69
- Half-time / Period: 66
- Double chance: 62
- Correct score: 62

## Bet365 market types found

- Other / Unknown: 523
- Goals total / Over-Under: 452
- Handicap / Spread: 282
- Both teams to score: 96
- Half-time / Period: 66
- 1X2 / Match result: 62
- Double chance: 62
- Correct score: 62

## Most common Bet365 market names

- ML: 62
- Draw No Bet: 62
- Double Chance: 62
- Spread: 62
- Totals: 62
- Goals Over/Under: 62
- Spread HT: 62
- Correct Score: 62
- Half Time Result: 62
- Totals HT: 58
- Corners: 55
- Corners 2-Way: 55
- Alternative Goal Line: 54
- Alternative Asian Handicap: 54
- Corners Totals: 53
- Corners Totals HT: 53
- Both Teams To Score: 32
- European Handicap: 32
- Alternative Total Goals: 32
- Specials: 32
- Number of Goals In Match: 32
- Both Teams To Score HT: 32
- Team Total Goals Home: 32
- Team Total Goals Away: 32
- Exact Total Goals: 32
- Both Teams To Score 2H: 32
- 1st Half Handicap: 32
- Alternative Corners: 32
- Total Corners: 32
- First 10 Minutes (00:00 - 09:59): 26

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.