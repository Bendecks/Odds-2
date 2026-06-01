# Odds-API.io Market Inventory

Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.
This report does not activate new markets. It only shows what may be available for future model expansion.

Raw files scanned: 22
Events seen in raw odds: 110
Market rows seen: 2575
Unique bookmakers: 2
Unique market names: 60
Bet365 market rows: 2443

## Market types found

- Goals total / Over-Under: 773
- Other / Unknown: 685
- Handicap / Spread: 495
- Both teams to score: 141
- 1X2 / Match result: 133
- Half-time / Period: 128
- Double chance: 110
- Correct score: 110

## Bet365 market types found

- Goals total / Over-Under: 717
- Other / Unknown: 685
- Handicap / Spread: 442
- Both teams to score: 141
- Half-time / Period: 128
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
- Correct Score: 110
- Half Time Result: 110
- Totals HT: 92
- Corners Totals: 88
- Alternative Goal Line: 84
- Alternative Asian Handicap: 84
- Corners Totals HT: 80
- Corners: 80
- Corners 2-Way: 80
- Both Teams To Score: 47
- European Handicap: 47
- 1st Half Handicap: 47
- Exact Total Goals: 47
- Alternative Corners: 47
- Both Teams To Score HT: 47
- Team Total Goals Away: 47
- Number of Goals In Match: 47
- Team Total Goals Home: 47
- Total Corners: 47
- Alternative Total Goals: 47
- Both Teams To Score 2H: 47
- Specials: 47
- First 10 Minutes (00:00 - 09:59): 24

## Expansion assessment

- 1X2 / match result is already active.
- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.
- Both Teams To Score may also be possible after goal expectation quality is checked.
- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.
- New sports should stay inventory-only for now; each sport needs a separate probability model.