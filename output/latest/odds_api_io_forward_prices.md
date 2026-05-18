# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 4 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 187
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Leganes
Selected event IDs: 69254658, 71498954, 71498946, 71498952, 71498944, 71498942, 71498950, 71498948, 67604816, 71474802, 69109004, 63004427, 69254652, 71521626, 71478622, 71501436, 70906790, 70906786, 70906788, 70906784, 69880328, 68311606, 68311608, 67126550, 69880330, 67126110, 70812670, 70812668, 70812674, 68311610, 70812672, 61062319, 67126556, 67126106, 71305170, 68310906, 69744652, 67849990, 69744644, 67849992, 68156634, 69744646, 69744650, 71521628, 68751772, 71500630, 71500628, 71500632, 71500636, 71500634, 71546786, 61623906, 67122874, 67119320, 67122892, 71500526, 71551938, 68306816, 68306820, 68306818, 68306822, 61301249, 71532644, 71324794, 71460006, 68822886, 68215838, 70322856, 69255024, 69255036, 68097896, 68215850, 68097910, 68215846, 71534234, 68687654, 71532648, 71218650, 68215840
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 187
Event selection diagnostic rows: 11818
Selected event rows: 79
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 59
Latest x-ratelimit-reset: 2026-05-18T15:53:11Z
Latest retry-after: None

- 2026-05-18 15:00 | Club Deportivo Magallanes vs Deportes Recoleta | odds_api_io_Bet365_ML | 1.48/4.333/4.5
- 2026-05-18 15:20 | AL Nasr SC (OMA) vs Samail SC | odds_api_io_Bet365_ML | 1.65/3.4/5.0
- 2026-05-18 15:20 | Al Shabab vs Al-Seeb | odds_api_io_Bet365_ML | 3.1/3.25/2.2
- 2026-05-18 15:20 | Al-Khaboora vs Al-Rustaq | odds_api_io_Bet365_ML | 1.6/3.5/5.25
- 2026-05-18 15:20 | Bahla Club vs Al Nahda | odds_api_io_Bet365_ML | 3.2/3.0/2.15
- 2026-05-18 15:20 | Ibri vs Dhofar SCSC | odds_api_io_Bet365_ML | 3.1/3.0/2.2
- 2026-05-18 15:20 | Oman Club vs Sur SC | odds_api_io_Bet365_ML | 2.2/3.2/2.9
- 2026-05-18 15:20 | Sohar vs Saham | odds_api_io_Bet365_ML | 2.55/2.875/2.7
- 2026-05-18 15:30 | FC Haka Valkeakoski vs HJK Klubi 04 | odds_api_io_Bet365_ML | 1.363/4.5/6.0
- 2026-05-18 15:30 | NK Samobor vs GNK Dinamo Zagreb | odds_api_io_Bet365_ML | 9.5/6.25/1.222

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Club Deportivo Magallanes | target=Club Deportivo Magallanes vs Deportes Recoleta | candidate=Club Deportivo Magallanes vs Deportes Recoleta | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Guayaquil City FC | target=Guayaquil City FC vs Orense SC | candidate=Guayaquil City FC vs Orense SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CSDC Espanol | target=CSDC Espanol vs Club Mercedes | candidate=CSDC Espanol vs Club Mercedes | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Jerusalem FC | target=Hapoel Jerusalem FC vs Ironi Tiberias | candidate=Hapoel Jerusalem FC vs Ironi Tiberias | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kuwait SC | target=Kuwait SC vs Al Arabi | candidate=Kuwait SC vs Al Arabi | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Desimpain | target=Desimpain vs G3X FC | candidate=Desimpain vs G3X FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Orgryte IS | target=Orgryte IS vs IFK Goteborg | candidate=Orgryte IS vs IFK Goteborg | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Waterford FC | target=Waterford FC vs Drogheda United FC | candidate=Waterford FC vs Drogheda United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Falcons FC | target=Falcons FC vs Bst Galaxy | candidate=Falcons FC vs Bst Galaxy | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Deportivo Shalon | target=Deportivo Shalon vs 22 de Octubre | candidate=Deportivo Shalon vs 22 de Octubre | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Haifa FC | target=Hapoel Haifa FC vs Bnei Sakhnin FC | candidate=Hapoel Haifa FC vs Bnei Sakhnin FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cruzeiro EC MG | target=Cruzeiro EC MG vs SC Corinthians SP | candidate=Cruzeiro EC MG vs SC Corinthians SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ibri | target=Ibri vs Dhofar SCSC | candidate=Ibri vs Dhofar SCSC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PFC Dobrudzha Dobrich | target=PFC Dobrudzha Dobrich vs POFC Botev Vratsa | candidate=PFC Dobrudzha Dobrich vs POFC Botev Vratsa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fylkir Reykjavik | target=Fylkir Reykjavik vs IR Reykjavik | candidate=Fylkir Reykjavik vs IR Reykjavik | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SJK Akatemia/2 | target=SJK Akatemia/2 vs VPS Akatemia | candidate=SJK Akatemia/2 vs VPS Akatemia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Mokawloon Al Arab | target=Al Mokawloon Al Arab vs Wadi Degla SC | candidate=Al Mokawloon Al Arab vs Wadi Degla SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Internacional FC De Palmira | target=Internacional FC De Palmira vs Tigres FC | candidate=Internacional FC De Palmira vs Tigres FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Ula | target=AL Ula vs Al-Orobah | candidate=AL Ula vs Al-Orobah | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Nacional de Montevideo | target=Nacional de Montevideo vs Cerro Largo FC | candidate=Nacional de Montevideo vs Cerro Largo FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Leganes'; best=0.0
- multi_odds_match: No multi-odds payload matched event 69109004
- multi_odds_match: No multi-odds payload matched event 63004427
- multi_odds_match: No multi-odds payload matched event 69254652
- multi_odds_match: No multi-odds payload matched event 71521626
- multi_odds_match: No multi-odds payload matched event 71478622
- multi_odds_match: No multi-odds payload matched event 71501436
- multi_odds_match: No multi-odds payload matched event 70906790
- multi_odds_match: No multi-odds payload matched event 70906786
- multi_odds_match: No multi-odds payload matched event 70906788