# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.
Uses the documented single-event /v3/odds endpoint: one events call plus one odds call by default.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 2 / 2
Max events: 8
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: single_event_documented_endpoint
Fixture rows: 8
Price rows: 0
Errors: 1


## Errors

- odds_parse: No 1X2 odds found in single-event odds response