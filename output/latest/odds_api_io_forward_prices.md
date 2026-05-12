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
Events discovery rows: 126
Events max pages: 4
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 30
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: PFC Cherno More Varna, AL Faisaly (Jor), Kifisia, Panetolikos
Selected event IDs: 71085582, 71338858, 71085578, 71085580, 70232094, 71328286, 70232096, 71421816, 68492516, 71216798, 71338146, 64055855, 71336690, 71344696, 71401082, 70430016, 71378882, 70812400, 67126090, 67126084, 61624642, 71338618, 69880310, 70906726, 71364784, 70812402, 70906728, 71228890
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 129
Event selection diagnostic rows: 3419
Selected event rows: 28
Priced event rows: 10
Price rows: 10
Errors/status rows: 20

## Provider rate-limit headers

Header rows captured: 7
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 85
Latest x-ratelimit-reset: 2026-05-12T16:04:33Z
Latest retry-after: None

- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | odds_api_io_Bet365_ML | 2.1/3.5/3.0
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan | odds_api_io_Bet365_ML | 1.48/4.333/4.75
- 2026-05-12 15:30 | FK Mlada Boleslav vs Dukla Prague | odds_api_io_Bet365_ML | 1.9/3.5/3.5
- 2026-05-12 15:30 | FC Zlin vs FK Teplice | odds_api_io_Bet365_ML | 3.0/3.2/2.2
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon | odds_api_io_Bet365_ML | 2.2/3.25/3.3
- 2026-05-12 16:00 | FC Elva vs Paide Linnameeskond | odds_api_io_Bet365_ML | 34.0/15.0/1.045
- 2026-05-12 16:00 | Panaitolikos Agrinio vs AE Larissa FC | odds_api_io_Bet365_ML | 2.375/3.0/3.2
- 2026-05-12 16:00 | Rayon Sports FC vs Gorilla FC | odds_api_io_Bet365_ML | 1.571/3.3/5.75
- 2026-05-12 16:00 | Riga FC vs FK Auda Riga | odds_api_io_Bet365_ML | 1.6/3.9/4.333
- 2026-05-12 16:00 | Sarpsborg 08 FF vs Hoenefoss BK | odds_api_io_Bet365_ML | 9.5/5.5/1.222

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Rayon Sports FC | target=Rayon Sports FC vs Gorilla FC | candidate=Rayon Sports FC vs Gorilla FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Samger FC | target=Samger FC vs Real de Banjul | candidate=Samger FC vs Real de Banjul | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Riga FC | target=Riga FC vs FK Auda Riga | candidate=Riga FC vs FK Auda Riga | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Landskrona BoIS | target=Landskrona BoIS vs Norrby IF | candidate=Landskrona BoIS vs Norrby IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Wahda FC | target=AL Wahda FC vs Khorfakkan | candidate=AL Wahda FC vs Khorfakkan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Botev Plovdiv | target=Botev Plovdiv vs FC Arda Kardzhali | candidate=Botev Plovdiv vs FC Arda Kardzhali | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sarpsborg 08 FF | target=Sarpsborg 08 FF vs Hoenefoss BK | candidate=Sarpsborg 08 FF vs Hoenefoss BK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Varnamo | target=IFK Varnamo vs Orebro SK | candidate=IFK Varnamo vs Orebro SK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Viking FK | target=Viking FK vs Haugesund | candidate=Viking FK vs Haugesund | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Zlin | target=FC Zlin vs FK Teplice | candidate=FC Zlin vs FK Teplice | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Panaitolikos Agrinio | target=Panaitolikos Agrinio vs AE Larissa FC | candidate=Panaitolikos Agrinio vs AE Larissa FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Tel Aviv FC | target=Hapoel Tel Aviv FC vs Hapoel Petah Tikva FC | candidate=Hapoel Tel Aviv FC vs Hapoel Petah Tikva FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=RC Celta de Vigo | target=RC Celta de Vigo vs Levante UD | candidate=RC Celta de Vigo vs Levante UD | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Modena FC | target=Modena FC vs Juve Stabia | candidate=Modena FC vs Juve Stabia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Real Madrid | target=Real Madrid vs Borussia Dortmund | candidate=Real Madrid vs Borussia Dortmund | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Elva | target=FC Elva vs Paide Linnameeskond | candidate=FC Elva vs Paide Linnameeskond | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Hussein Irbid | target=Al Hussein Irbid vs Al Wehdat | candidate=Al Hussein Irbid vs Al Wehdat | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Kholood | target=Al-Kholood vs Al-Okhdood Club | candidate=Al-Kholood vs Al-Okhdood Club | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Central Espanol Reserve | target=Central Espanol Reserve vs Defensor Sporting | candidate=Central Espanol Reserve vs Defensor Sporting | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=1. FC Slovacko Uherske Hradiste | target=1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | candidate=1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Kifisia'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Panetolikos'; best=0.0
- multi_odds_match: No multi-odds payload matched event 71338146
- multi_odds_match: No multi-odds payload matched event 64055855
- multi_odds_match: No multi-odds payload matched event 71336690
- multi_odds_match: No multi-odds payload matched event 71344696
- multi_odds_match: No multi-odds payload matched event 71401082
- multi_odds_match: No multi-odds payload matched event 70430016
- multi_odds_match: No multi-odds payload matched event 71378882
- multi_odds_match: No multi-odds payload matched event 70812400