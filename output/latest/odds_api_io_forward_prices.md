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
Events discovery rows: 111
Events max pages: 4
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 30
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Asteras Tripolis, Kifisia, Panetolikos, Celta
Selected event IDs: 71401082, 71378882, 70812400, 67126090, 67126084, 61624642, 71338618, 69880310, 70906726, 71364784, 70812402, 62670417, 64055859, 71378884, 68158786, 68158768, 68158784, 68158760, 61624640, 71085528, 71378874, 70448538, 70448540, 71378878, 71411500, 70448542
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 112
Event selection diagnostic rows: 2983
Selected event rows: 26
Priced event rows: 10
Price rows: 10
Errors/status rows: 20

## Provider rate-limit headers

Header rows captured: 7
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 82
Latest x-ratelimit-reset: 2026-05-12T17:19:34Z
Latest retry-after: None

- 2026-05-12 16:45 | Modena FC vs Juve Stabia | odds_api_io_Bet365_ML | 2.2/3.1/3.6
- 2026-05-12 17:00 | Central Espanol Reserve vs Defensor Sporting | odds_api_io_Bet365_ML | 3.0/3.6/2.1
- 2026-05-12 17:00 | Hapoel Tel Aviv FC vs Hapoel Petah Tikva FC | odds_api_io_Bet365_ML | 1.222/5.5/9.0
- 2026-05-12 17:00 | IFK Varnamo vs Orebro SK | odds_api_io_Bet365_ML | 2.05/3.2/3.4
- 2026-05-12 17:00 | Landskrona BoIS vs Norrby IF | odds_api_io_Bet365_ML | 2.0/3.2/3.5
- 2026-05-12 17:00 | RC Celta de Vigo vs Levante UD | odds_api_io_Bet365_ML | 1.9/3.7/3.9
- 2026-05-12 17:00 | Real Madrid vs Borussia Dortmund | odds_api_io_Bet365_ML | 1.727/3.7/3.8
- 2026-05-12 17:00 | Wadi Degla SC vs Ismaily SC | odds_api_io_Bet365_ML | 2.0/2.9/3.6
- 2026-05-12 17:15 | Botev Plovdiv vs FC Arda Kardzhali | odds_api_io_Bet365_ML | 3.4/3.0/2.2
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat | odds_api_io_Bet365_ML | 2.2/2.7/3.3

## Event selection diagnostics

- src=events_bookmaker_filtered | query=TS Galaxy FC | target=TS Galaxy FC vs Mamelodi Sundowns | candidate=TS Galaxy FC vs Mamelodi Sundowns | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Varnamo | target=IFK Varnamo vs Orebro SK | candidate=IFK Varnamo vs Orebro SK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Red Star FC | target=Red Star FC vs Rodez Aveyron Football | candidate=Red Star FC vs Rodez Aveyron Football | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Tel Aviv FC | target=Hapoel Tel Aviv FC vs Hapoel Petah Tikva FC | candidate=Hapoel Tel Aviv FC vs Hapoel Petah Tikva FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Penarol Montevideo | target=Penarol Montevideo vs Nacional de Montevideo | candidate=Penarol Montevideo vs Nacional de Montevideo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Beitar Jerusalem FC | target=Beitar Jerusalem FC vs Hapoel Be`er Sheva FC | candidate=Beitar Jerusalem FC vs Hapoel Be`er Sheva FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=RC Celta de Vigo | target=RC Celta de Vigo vs Levante UD | candidate=RC Celta de Vigo vs Levante UD | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Nassr Club | target=Al Nassr Club vs Al Hilal SFC | candidate=Al Nassr Club vs Al Hilal SFC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Servette Geneva | target=Servette Geneva vs Lausanne-Sport | candidate=Servette Geneva vs Lausanne-Sport | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Modena FC | target=Modena FC vs Juve Stabia | candidate=Modena FC vs Juve Stabia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cerro Largo FC | target=Cerro Largo FC vs Boston River | candidate=Cerro Largo FC vs Boston River | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Central Espanol Reserve | target=Central Espanol Reserve vs Defensor Sporting | candidate=Central Espanol Reserve vs Defensor Sporting | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Real Madrid | target=Real Madrid vs Borussia Dortmund | candidate=Real Madrid vs Borussia Dortmund | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sparta Prague | target=Sparta Prague vs FC Viktoria Plzen | candidate=Sparta Prague vs FC Viktoria Plzen | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Landskrona BoIS | target=Landskrona BoIS vs Norrby IF | candidate=Landskrona BoIS vs Norrby IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Luzern | target=FC Luzern vs FC Zurich | candidate=FC Luzern vs FC Zurich | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Newells Old Boys | target=Newells Old Boys vs CA Quilmes Reserve | candidate=Newells Old Boys vs CA Quilmes Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Racing Club Avellaneda | target=Racing Club Avellaneda vs Velez Sarsfield Reserve | candidate=Racing Club Avellaneda vs Velez Sarsfield Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Real Betis Seville | target=Real Betis Seville vs Elche CF | candidate=Real Betis Seville vs Elche CF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Wadi Degla SC | target=Wadi Degla SC vs Ismaily SC | candidate=Wadi Degla SC vs Ismaily SC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Asteras Tripolis'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Kifisia'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Panetolikos'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Celta'; best=0.48
- multi_odds_match: No multi-odds payload matched event 70812402
- multi_odds_match: No multi-odds payload matched event 62670417
- multi_odds_match: No multi-odds payload matched event 64055859
- multi_odds_match: No multi-odds payload matched event 71378884
- multi_odds_match: No multi-odds payload matched event 68158786
- multi_odds_match: No multi-odds payload matched event 68158768