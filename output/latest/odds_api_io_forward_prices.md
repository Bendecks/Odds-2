# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 4 / 6
Events bookmaker: Bet365
Events discovery rows: 0
Events max pages: 1
Events lookahead days: 14
Max events per page/search: 10
Max priced events: 3
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Napoli, Tottenham, Vallecano
Selected event IDs: 
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: 
Selected markets: 
Fixture rows: 11
Event selection diagnostic rows: 11
Selected event rows: 0
Priced event rows: 0
Price rows: 0
Errors/status rows: 4

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 87
Latest x-ratelimit-reset: 2026-05-11T21:17:32Z
Latest retry-after: None


## Event selection diagnostics

- src=events_search_fallback | query=Vallecano | target=Vallecano vs Girona | candidate=Valencia CF vs Rayo Vallecano | confidence=0.5229 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Vila Nova FC GO vs Anapolis FC GO | confidence=0.4853 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Cagliari Calcio vs SSC Napoli | confidence=0.4255 | selected=False | reason=below_min_event_match_confidence

## Errors / Status

- events_bookmaker_filtered: RuntimeError('HTTP 400: {"error":"Invalid \'from\' date format. Use RFC3339 (e.g. 2025-10-28T10:00:00Z)"}')
- event_selection: No event above confidence 0.72 for query 'Napoli'; best=0.5164
- event_selection: No event above confidence 0.72 for query 'Tottenham'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Vallecano'; best=0.5229