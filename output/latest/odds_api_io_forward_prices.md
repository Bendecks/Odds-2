# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Prioritizes model-covered forward fixtures, selects searched events by home/away match confidence, then uses documented /v3/odds/multi for selected events.
Parses documented EventResponse.bookmakers -> markets -> odds -> home/draw/away schema.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 3 / 6
Max events per search: 10
Max priced events: 3
Minimum event match confidence: 0.72
Discovery mode: model_covered_search_then_match_confidence_then_multi_odds
Query source: forward_fixture_predictions
Search queries used: Napoli, Tottenham, Vallecano
Selected event IDs: 
Bookmakers parameter mode: explicit_selected_bookmakers
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: multi_event_documented_endpoint
Odds parse mode: bookmakers_market_odds_schema
Selected bookmakers: 
Selected markets: 
Fixture rows: 11
Event selection diagnostic rows: 11
Selected event rows: 0
Priced event rows: 0
Price rows: 0
Errors/status rows: 3

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 91
Latest x-ratelimit-reset: 2026-05-11T21:17:32Z
Latest retry-after: None


## Event selection diagnostics

- query=Vallecano | target=Vallecano vs Girona | candidate=Valencia CF vs Rayo Vallecano | confidence=0.5229 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Vila Nova FC GO vs Anapolis FC GO | confidence=0.4853 | selected=False | reason=below_min_event_match_confidence
- query=Napoli | target=Napoli vs Bologna | candidate=Cagliari Calcio vs SSC Napoli | confidence=0.4255 | selected=False | reason=below_min_event_match_confidence

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Napoli'; best=0.5164
- event_selection: No event above confidence 0.72 for query 'Tottenham'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Vallecano'; best=0.5229