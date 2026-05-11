# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 10 / 10
Max discovery calls: 9
Events bookmaker: Bet365
Events discovery rows: 128
Events max pages: 3
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 10
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Huesca, Napoli, Tottenham, Vallecano, Benfica, Estrela, Gil Vicente
Selected event IDs: 71231662
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: 1xbet
Selected markets: 3-Way Result
Fixture rows: 143
Event selection diagnostic rows: 1295
Selected event rows: 1
Priced event rows: 1
Price rows: 1
Errors/status rows: 6

## Provider rate-limit headers

Header rows captured: 10
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 50
Latest x-ratelimit-reset: 2026-05-11T22:22:15Z
Latest retry-after: None

- 2026-05-13 18:00 | SC Braga vs Benfica Lisboa | odds_api_io_1xbet_3-Way Result | 8.6/18.5/1.025

## Event selection diagnostics

- src=events_search_fallback | query=Benfica | target=Benfica vs Sp Braga | candidate=SC Braga vs Benfica Lisboa | confidence=0.8175 | selected=True | reason=
- src=events_search_fallback | query=Benfica | target=Benfica vs Sp Braga | candidate=FC Porto B vs SL Benfica B | confidence=0.58 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Santa Clara | target=Santa Clara vs Nacional | candidate=SC Internacional RS vs Athletic Club Sjdr MG | confidence=0.5675 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Guimaraes | target=Guimaraes vs Casa Pia | candidate=Maringa FC PR vs Guarani FC SP | confidence=0.538 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Santa Clara | target=Santa Clara vs Nacional | candidate=Atletico Nacional Medellin vs Internacional de Bogota. | confidence=0.5271 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Vallecano | target=Vallecano vs Girona | candidate=Valencia CF vs Rayo Vallecano | confidence=0.5229 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Louisville Bats vs Indianapolis Indians | confidence=0.5164 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Benfica | target=Benfica vs Sp Braga | candidate=Quinta Dos Lombos vs SL Benfica | confidence=0.5 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Vallecano | target=Vallecano vs Girona | candidate=Sol de America Villa Elisa vs Guairena FC | confidence=0.5 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Charleston Riverdogs vs Kannapolis Cannon Ballers | confidence=0.4911 | selected=False | reason=below_min_event_match_confidence
- src=events_search_fallback | query=Napoli | target=Napoli vs Bologna | candidate=Vila Nova FC GO vs Anapolis FC GO | confidence=0.4853 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Santa Clara | target=Santa Clara vs Nacional | candidate=Penarol Montevideo vs Nacional de Montevideo | confidence=0.4834 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Benfica | target=Benfica vs Sp Braga | candidate=Deportivo Cali vs CA Bucaramanga | confidence=0.4632 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Vallecano | target=Vallecano vs Girona | candidate=Millonarios FC vs Llaneros FC | confidence=0.4494 | selected=False | reason=below_min_event_match_confidence

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Huesca'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Napoli'; best=0.5164
- event_selection: No event above confidence 0.72 for query 'Tottenham'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Vallecano'; best=0.5229
- event_selection: No event above confidence 0.72 for query 'Estrela'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Gil Vicente'; best=0.0