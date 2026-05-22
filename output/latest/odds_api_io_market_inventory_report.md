# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 1995
Unique bookmakers: 2
Unique market names: 41
Bet365 market rows: 1874

## Market types found

- Goals total / Over-Under: 616
- Other / Unknown: 420
- Handicap / Spread: 411
- Half-time / Period: 132
- 1X2 / Match result: 118
- Double chance: 110
- Correct score: 110
- Both teams to score: 78

## Bet365 market types found

- Goals total / Over-Under: 550
- Other / Unknown: 420
- Handicap / Spread: 364
- Half-time / Period: 132
- 1X2 / Match result: 110
- Double chance: 110
- Correct score: 110
- Both teams to score: 78

## Most common Bet365 market names

- ML: 110
- Double Chance: 110
- Spread: 110
- Totals: 110
- Goals Over/Under: 110
- Correct Score: 110
- Half Time Result: 110
- Draw No Bet: 108
- Spread HT: 108
- Totals HT: 88
- Alternative Asian Handicap: 84
- Alternative Goal Line: 82
- Corners Totals: 58
- Corners Totals HT: 58
- Corners: 58
- Corners 2-Way: 58
- Both Teams To Score: 26
- European Handicap: 26
- Team Total Goals Away: 26
- Both Teams To Score HT: 26
- 1st Half Handicap: 26
- Specials: 26
- Both Teams To Score 2H: 26
- Team Total Goals Home: 26
- Number of Goals In Match: 26
- Alternative Total Goals: 26
- Exact Total Goals: 26
- 1st Half Goal Line: 22
- Total Corners: 22
- Alternative Corners: 22

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.