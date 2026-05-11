# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Prioritizes model-covered forward fixtures for search queries, then uses documented /v3/odds/multi for selected events.
Parses documented EventResponse.bookmakers -> markets -> odds -> home/draw/away schema.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 4 / 6
Max events per search: 10
Max priced events: 3
Discovery mode: model_covered_search_then_multi_odds
Query source: forward_fixture_predictions
Search queries used: Napoli, Tottenham, Vallecano
Selected event IDs: 69057010, 61624652
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: multi_event_documented_endpoint
Odds parse mode: bookmakers_market_odds_schema
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 11
Selected event rows: 2
Priced event rows: 1
Price rows: 1
Errors/status rows: 2

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 31
Latest x-ratelimit-reset: 2026-05-11T20:13:08Z
Latest retry-after: None

- 2026-05-14 17:00 | Valencia CF vs Rayo Vallecano | odds_api_io_Bet365_ML | 2.25/3.4/3.2

## Errors / Status

- event_selection: No future non-settled event available from targeted search query 'Tottenham'; skipped
- multi_odds_match: No multi-odds payload matched event 69057010