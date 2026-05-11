# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.
Uses documented /v3/events with sport+limit first; if no future event is found, uses one targeted /v3/events/search fallback. With max_calls=2 this prevents odds calls when discovery fails.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 2 / 2
Max events: 8
Discovery mode: events_endpoint_then_targeted_search_fallback
Search query used: Tottenham
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: single_event_documented_endpoint
Fixture rows: 9
Eligible future fixture rows: 1
Price rows: 0
Errors/status rows: 0
