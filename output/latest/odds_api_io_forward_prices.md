# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 4 / 6
Events bookmaker: Bet365
Events discovery rows: 10
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
Fixture rows: 21
Event selection diagnostic rows: 41
Selected event rows: 0
Priced event rows: 0
Price rows: 0
Errors/status rows: 3

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 83
Latest x-ratelimit-reset: 2026-05-11T21:17:32Z
Latest retry-after: None


## Event selection diagnostics

- src=events_search_fallback | query=Vallecano | target=Vallecano vs Girona | candidate=Valencia CF vs Rayo Vallecano | confidence=0.5229 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Vallecano | target=Vallecano vs Girona | candidate=Sol de America Villa Elisa vs Guairena FC | confidence=0.5 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Vila Nova FC GO vs Anapolis FC GO | confidence=0.4853 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Cagliari Calcio vs SSC Napoli | confidence=0.4255 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Napoli | target=Napoli vs Bologna | candidate=SC Internacional RS vs Botafogo Fr RJ | confidence=0.3505 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Napoli | target=Napoli vs Bologna | candidate=Millonarios FC vs America de Cali Sa | confidence=0.3472 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Vallecano | target=Vallecano vs Girona | candidate=Millonarios FC vs America de Cali Sa | confidence=0.3464 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Tottenham | target=Tottenham vs Leeds | candidate=Loud SC vs Funkbol Clube | confidence=0.3409 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Napoli | target=Napoli vs Bologna | candidate=Piaui PI vs Ferroviario AC CE | confidence=0.3393 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Napoli | target=Napoli vs Bologna | candidate=Deportivo Saprissa vs Sporting FC | confidence=0.3343 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Napoli | target=Napoli vs Bologna | candidate=Independiente Medellin vs Fortaleza FC | confidence=0.3304 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Vallecano | target=Vallecano vs Girona | candidate=CR Flamengo RJ vs Ferroviaria SP | confidence=0.3239 | selected=False | reason=below_min_event_match_confidence

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Napoli'; best=0.5164
- event_selection: No event above confidence 0.72 for query 'Tottenham'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Vallecano'; best=0.5229