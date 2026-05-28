# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 6 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 475
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Panadura SC, Baduraliya CC
Selected event IDs: 69924686, 71737390, 71577916, 68774164, 67912706, 69924124, 71530440, 71544082, 67149486, 62274242, 70655020, 69923700, 71401844, 70663592, 71685288, 68158840, 68158856, 68158836, 68158844, 68158842, 71668632, 71729572, 68751826, 71769326, 71602082, 71585136, 71704432, 69829492, 71615192, 71615270, 71562582, 71705028, 71705030, 71615688, 71615454, 68158832, 70075878, 70075876, 71355212, 71762788, 69091202, 69091204, 69091206, 71517962, 70075106, 70075754, 70075108, 70075756, 71705032, 69091222, 68989156, 69460628, 69455902, 69460630, 67693568, 67905690, 68051000, 68160578, 68160192, 68161722, 67878252, 68161724, 68051624, 67807834, 68049818, 70926710, 68161734, 67692262, 68686542, 68162402, 68048882, 68049816, 71127916, 69455900, 69115230, 69455904, 68995188, 70314466, 71639628, 71639506
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 478
Event selection diagnostic rows: 34893
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 6
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 59
Latest x-ratelimit-reset: 2026-05-28T16:25:43Z
Latest retry-after: None

- 2026-05-28 15:45 | Mikkelin Pallo-Kissat vs HaPK Edustus | odds_api_io_Bet365_ML | 1.615/4.75/3.4
- 2026-05-28 16:00 | Deportivo Maldonado Reserve vs Liverpool Montevideo | odds_api_io_Bet365_ML | 2.15/3.6/2.875
- 2026-05-28 16:00 | Puskas Akademia Felcsut vs Ferencvarosi Budapest | odds_api_io_Bet365_ML | 2.6/3.4/2.3
- 2026-05-28 16:00 | FC Tallinn vs Maardu Linnameeskond | odds_api_io_Bet365_ML | 3.25/4.333/1.75
- 2026-05-28 16:00 | FC Torpedo Kutaisi vs FC Gagra | odds_api_io_Bet365_ML | 1.4/4.2/6.5
- 2026-05-28 16:00 | FC Ylivieska vs Lapuan Virkia | odds_api_io_Bet365_ML | 1.615/5.5/3.25
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC | odds_api_io_Bet365_ML | 2.7/3.4/2.25
- 2026-05-28 17:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | odds_api_io_Bet365_ML | 2.1/3.4/2.875
- 2026-05-28 17:00 | Kolding IF vs Dbk Fortuna Hjoerring | odds_api_io_Bet365_ML | 3.9/4.1/1.615
- 2026-05-28 17:00 | FCM Traiskirchen vs SC Neusiedl am See 1919 | odds_api_io_Bet365_ML | 1.363/5.75/5.25

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Mikkelin Pallo-Kissat | target=Mikkelin Pallo-Kissat vs HaPK Edustus | candidate=Mikkelin Pallo-Kissat vs HaPK Edustus | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Assyriska FF | target=Assyriska FF vs Vasalunds IF | candidate=Assyriska FF vs Vasalunds IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Adelaide University FC Reserve | target=Adelaide University FC Reserve vs Adelaide Comets FC Reserves | candidate=Adelaide University FC Reserve vs Adelaide Comets FC Reserves | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=Baduraliya CC | target=Baduraliya CC vs Colombo CC | candidate=Baduraliya CC vs Colombo CC | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=Panadura SC | target=Panadura SC vs Sinhalese Sports Club | candidate=Panadura SC vs Sinhalese Sports Club | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hedensted IF | target=Hedensted IF vs Fuglebakken KFUM | candidate=Hedensted IF vs Fuglebakken KFUM | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=East Fife Lfc | target=East Fife Lfc vs Falkirk FC | candidate=East Fife Lfc vs Falkirk FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PPJ/Ruoholahti | target=PPJ/Ruoholahti vs Mps | candidate=PPJ/Ruoholahti vs Mps | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ningbo Professional FC | target=Ningbo Professional FC vs Nantong Zhiyun | candidate=Ningbo Professional FC vs Nantong Zhiyun | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Atletico Mineiro MG | target=Atletico Mineiro MG vs EC Vitoria BA | candidate=Atletico Mineiro MG vs EC Vitoria BA | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=North Star | target=North Star vs Brisbane Strikers | candidate=North Star FC vs Brisbane Strikers FC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=North Star | target=North Star vs Brisbane Strikers | candidate=North Star vs Brisbane Strikers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD El Nacional | target=CD El Nacional vs CD Universidad Catolica del Ecuador | candidate=CD El Nacional vs CD Universidad Catolica del Ecuador | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SE Palmeiras SP | target=SE Palmeiras SP vs CD Junior FC | candidate=SE Palmeiras SP vs CD Junior FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Torpedo Kutaisi | target=FC Torpedo Kutaisi vs FC Gagra | candidate=FC Torpedo Kutaisi vs FC Gagra | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Piauiense PI | target=CA Piauiense PI vs Santos FC SP | candidate=CA Piauiense PI vs Santos FC SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Casa Pia Lisbon | target=Casa Pia Lisbon vs SCU Torreense | candidate=Casa Pia Lisbon vs SCU Torreense | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Red Bull Bragantino SP | target=Red Bull Bragantino SP vs SC Corinthians SP | candidate=Red Bull Bragantino SP vs SC Corinthians SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Progreso | target=Progreso vs Defensor Sporting | candidate=Progreso vs Defensor Sporting | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Adelaide University | target=Adelaide University vs Adelaide Comets FC | candidate=Adelaide University vs Adelaide Comets FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 70655020
- multi_odds_match: No multi-odds payload matched event 69923700
- multi_odds_match: No multi-odds payload matched event 71401844
- multi_odds_match: No multi-odds payload matched event 70663592
- multi_odds_match: No multi-odds payload matched event 71685288
- multi_odds_match: No multi-odds payload matched event 68158840
- multi_odds_match: No multi-odds payload matched event 68158856
- multi_odds_match: No multi-odds payload matched event 68158836
- multi_odds_match: No multi-odds payload matched event 68158844
- multi_odds_match: No multi-odds payload matched event 68158842