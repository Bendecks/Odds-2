# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 2 / 2
Max events: 8
Fixture rows: 8
Price rows: 0
Errors: 1


## Errors

- odds_request_or_parse: RuntimeError('HTTP 403: {"error":"Access denied. You\'re allowed max 2 bookmakers. Allowed: Bet365, 1xbet. To reset your selections, use PUT /bookmakers/selected/clear?apiKey=YOUR_API_KEY or visit https://docs.odds-api.io/api-reference/bookmakers/clear-selected-bookmakers. Upgrade your plan at https://odds-api.io/manage"}')