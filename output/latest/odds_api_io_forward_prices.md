# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.
Uses documented /v3/events/search first because docs specify it searches upcoming events, then /v3/odds for one eligible future event.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 2 / 2
Max events: 8
Discovery mode: targeted_events_search_then_single_event_odds
Search query used: Tottenham
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: single_event_documented_endpoint
Fixture rows: 1
Eligible future fixture rows: 1
Price rows: 1
Errors/status rows: 0

- 2026-05-11 19:00 | Tottenham Hotspur vs Leeds United | 1.789/4.045/4.775