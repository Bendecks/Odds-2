# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.
Uses /v3/events/search against a known upcoming fixture, then /v3/odds for one eligible future event.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 2 / 2
Max events: 8
Discovery mode: events_search_targeted_from_fixture
Search query: Tottenham
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: single_event_documented_endpoint
Fixture rows: 1
Eligible future fixture rows: 1
Price rows: 1
Errors/status rows: 0

- 2026-05-11 19:00 | Tottenham Hotspur vs Leeds United | 1.84/3.985/4.525