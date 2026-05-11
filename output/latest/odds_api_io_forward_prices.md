# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 7 / 8
Max discovery calls: 7
Events bookmaker: Bet365
Events discovery rows: 0
Events max pages: 4
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 10
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Huesca, Napoli, Tottenham, Vallecano, Benfica, Estrela
Selected event IDs: 
Multi-odds attempted: False
Multi-odds skipped reason: no_selected_events
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: 
Selected markets: 
Fixture rows: 0
Event selection diagnostic rows: 0
Selected event rows: 0
Priced event rows: 0
Price rows: 0
Errors/status rows: 7

## Provider rate-limit headers

Header rows captured: 7
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 0
Latest x-ratelimit-reset: 2026-05-11T22:22:15Z
Latest retry-after: None


## Errors / Status

- events_bookmaker_filtered: RuntimeError('HTTP 429: {"error":"You have exceeded your rate limit of 100 requests per hour. It resets in 23 minutes and 43 seconds."}')
- events_search_or_parse: RuntimeError('HTTP 429: {"error":"You have exceeded your rate limit of 100 requests per hour. It resets in 23 minutes and 43 seconds."}')
- events_search_or_parse: RuntimeError('HTTP 429: {"error":"You have exceeded your rate limit of 100 requests per hour. It resets in 23 minutes and 42 seconds."}')
- events_search_or_parse: RuntimeError('HTTP 429: {"error":"You have exceeded your rate limit of 100 requests per hour. It resets in 23 minutes and 42 seconds."}')
- events_search_or_parse: RuntimeError('HTTP 429: {"error":"You have exceeded your rate limit of 100 requests per hour. It resets in 23 minutes and 42 seconds."}')
- events_search_or_parse: RuntimeError('HTTP 429: {"error":"You have exceeded your rate limit of 100 requests per hour. It resets in 23 minutes and 42 seconds."}')
- events_search_or_parse: RuntimeError('HTTP 429: {"error":"You have exceeded your rate limit of 100 requests per hour. It resets in 23 minutes and 42 seconds."}')