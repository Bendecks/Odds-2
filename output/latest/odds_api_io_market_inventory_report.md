# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 14
Events seen in raw odds: 62
Market rows seen: 1677
Unique bookmakers: 2
Unique market names: 65
Bet365 market rows: 1609

## Market types found

- Other / Unknown: 535
- Goals total / Over-Under: 483
- Handicap / Spread: 306
- Both teams to score: 99
- 1X2 / Match result: 73
- Half-time / Period: 65
- Double chance: 58
- Correct score: 58

## Bet365 market types found

- Other / Unknown: 535
- Goals total / Over-Under: 459
- Handicap / Spread: 273
- Both teams to score: 99
- Half-time / Period: 65
- 1X2 / Match result: 62
- Double chance: 58
- Correct score: 58

## Most common Bet365 market names

- ML: 62
- Spread: 62
- Totals: 62
- Spread HT: 62
- Totals HT: 59
- Draw No Bet: 58
- Double Chance: 58
- Goals Over/Under: 58
- Correct Score: 58
- Half Time Result: 58
- Corners Totals: 55
- Corners Totals HT: 55
- Corners: 55
- Corners 2-Way: 55
- Alternative Asian Handicap: 41
- Alternative Goal Line: 41
- Alternative Corners: 34
- Total Corners: 34
- Both Teams To Score: 33
- European Handicap: 33
- Number of Goals In Match: 33
- Team Total Goals Away: 33
- 1st Half Handicap: 33
- Exact Total Goals: 33
- Team Total Goals Home: 33
- Both Teams To Score HT: 33
- Both Teams To Score 2H: 33
- Alternative Total Goals: 33
- Specials: 33
- First 10 Minutes (00:00 - 09:59): 26

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.