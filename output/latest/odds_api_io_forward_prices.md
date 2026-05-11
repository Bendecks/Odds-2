# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.
Uses the documented single-event /v3/odds endpoint when a future non-settled event is available.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 1 / 2
Max events: 8
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: single_event_documented_endpoint
Fixture rows: 8
Eligible future fixture rows: 0
Price rows: 0
Errors/status rows: 1


## Errors / Status

- event_selection: No future non-settled event available in fetched odds-api.io events; skipped odds call