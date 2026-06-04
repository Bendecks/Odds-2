# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2180
Unique bookmakers: 2
Unique market names: 64
Bet365 market rows: 2040

## Market types found

- Goals total / Over-Under: 609
- Other / Unknown: 590
- Handicap / Spread: 442
- 1X2 / Match result: 130
- Half-time / Period: 123
- Correct score: 106
- Double chance: 102
- Both teams to score: 78

## Bet365 market types found

- Other / Unknown: 590
- Goals total / Over-Under: 555
- Handicap / Spread: 376
- Half-time / Period: 123
- 1X2 / Match result: 110
- Correct score: 106
- Double chance: 102
- Both teams to score: 78

## Most common Bet365 market names

- ML: 110
- Draw No Bet: 106
- Spread: 106
- Totals: 106
- Goals Over/Under: 106
- Correct Score: 106
- Half Time Result: 106
- Spread HT: 104
- Double Chance: 102
- Totals HT: 89
- Alternative Goal Line: 78
- Alternative Asian Handicap: 78
- Corners Totals: 60
- Corners Totals HT: 58
- Corners 2-Way: 58
- Corners: 58
- Both Teams To Score: 26
- European Handicap: 26
- Total Corners: 26
- Alternative Corners: 26
- Alternative Total Goals: 26
- Number of Goals In Match: 26
- Team Total Goals Away: 26
- Team Total Goals Home: 26
- Both Teams To Score HT: 26
- Specials: 26
- 1st Half Handicap: 26
- Both Teams To Score 2H: 26
- Exact Total Goals: 26
- 1st Half Goal Line: 17

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.