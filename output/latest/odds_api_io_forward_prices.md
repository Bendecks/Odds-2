# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.
Uses documented /v3/events with sport+limit, then /v3/odds for one eligible future event.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 1 / 2
Max events: 8
Discovery mode: events_endpoint_documented_sport_limit
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: single_event_documented_endpoint
Fixture rows: 8
Eligible future fixture rows: 0
Price rows: 0
Errors/status rows: 1


## Errors / Status

- event_selection: No future non-settled event available from documented events endpoint; skipped odds call