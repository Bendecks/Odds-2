# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_EVENTS.
Uses documented /v3/events/search first because docs specify it searches upcoming events, then /v3/odds for one eligible future event.
Parses documented EventResponse.bookmakers -> markets -> odds -> home/draw/away schema.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 2 / 2
Max events: 8
Discovery mode: targeted_events_search_then_single_event_odds
Search query used: Tottenham
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: single_event_documented_endpoint
Odds parse mode: bookmakers_market_odds_schema
Selected bookmaker: Bet365
Selected market: ML
Fixture rows: 2
Eligible future fixture rows: 2
Price rows: 1
Errors/status rows: 0

- 2026-05-11 19:00 | Tottenham Hotspur vs Leeds United | odds_api_io_Bet365_ML | 1.75/3.9/4.333