# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 3 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 125
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Leganes
Selected event IDs: 68160160, 61651668, 61651676, 67699618, 71500626, 71360370, 69880326, 68746500, 69880324, 69254658, 71498954, 71498946, 71498952, 71498944, 71498942, 71498950, 71498948, 67604816, 71474802, 69109004, 63004427, 69254652, 71501436, 70906790, 70906786, 70906788, 70906784, 69880328, 68311606, 68311608, 67126550, 69880330, 67126110, 70812670, 70812668, 70812674, 68311610, 70812672, 61062319, 67126556, 67126106, 68310906, 69744652, 67849990, 69744644, 67849992, 68156634, 69744646, 69744650, 68751772, 71500630, 71500628, 71500632, 71500636, 71500634, 61623906, 67122874, 67119320, 67122892, 71500526, 71551938, 68306816, 68306820, 68306818, 68306822, 61301249, 71532644, 71324794, 71460006, 68822886, 68215838, 70322856, 69255024, 69255036, 68097896, 68215850, 68097910, 68215846, 71534234
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 125
Event selection diagnostic rows: 6854
Selected event rows: 79
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 67
Latest x-ratelimit-reset: 2026-05-18T03:10:49Z
Latest retry-after: None

- 2026-05-18 09:30 | South Melbourne FC vs Caroline Springs George Cross FC | odds_api_io_Bet365_ML | 7.5/5.5/1.25
- 2026-05-18 10:00 | FK Kudrivka vs LNZ Cherkasy | odds_api_io_Bet365_ML | 6.5/3.9/1.42
- 2026-05-18 10:00 | FC Zorya Luhansk vs FC Polissya Zhytomyr | odds_api_io_Bet365_ML | 5.25/4.0/1.533
- 2026-05-18 11:30 | Tanjong Pagar United vs Hougang United FC | odds_api_io_Bet365_ML | 5.5/5.0/1.4
- 2026-05-18 12:30 | Defensor Sporting vs Albion FC | odds_api_io_Bet365_ML | 1.615/3.75/4.75
- 2026-05-18 13:00 | FC Shirak Gyumri vs FC Urartu Yerevan | odds_api_io_Bet365_ML | 4.5/4.2/1.533
- 2026-05-18 14:00 | Kahrabaa Ismailia vs Haras El Hodood | odds_api_io_Bet365_ML | 1.75/3.0/4.5
- 2026-05-18 14:00 | Kerala Blasters FC vs FC Goa | odds_api_io_Bet365_ML | 3.3/3.25/2.0
- 2026-05-18 14:00 | Talaea El Gaish vs Pharco FC | odds_api_io_Bet365_ML | 1.75/2.875/5.25
- 2026-05-18 15:00 | Club Deportivo Magallanes vs Deportes Recoleta | odds_api_io_Bet365_ML | 1.4/4.5/5.5

## Event selection diagnostics

- src=events_bookmaker_filtered | query=South Melbourne FC | target=South Melbourne FC vs Caroline Springs George Cross FC | candidate=South Melbourne FC vs Caroline Springs George Cross FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cruzeiro EC MG | target=Cruzeiro EC MG vs SC Corinthians SP | candidate=Cruzeiro EC MG vs SC Corinthians SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Desimpain | target=Desimpain vs G3X FC | candidate=Desimpain vs G3X FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AFC Hermannstadt | target=AFC Hermannstadt vs Fotbal Club FCSB | candidate=AFC Hermannstadt vs Fotbal Club FCSB | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Farul Constanta | target=FC Farul Constanta vs Metaloglobus Bucuresti | candidate=FC Farul Constanta vs Metaloglobus Bucuresti | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AFC Eskilstuna | target=AFC Eskilstuna vs FC Arlanda | candidate=AFC Eskilstuna vs FC Arlanda | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Nasr SC (OMA) | target=AL Nasr SC (OMA) vs Samail SC | candidate=AL Nasr SC (OMA) vs Samail SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Inter Miami CF II | target=Inter Miami CF II vs Crown Legacy FC | candidate=Inter Miami CF II vs Crown Legacy FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IK Oddevold | target=IK Oddevold vs Orebro SK | candidate=IK Oddevold vs Orebro SK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=HB Torshavn | target=HB Torshavn vs Eb/Streymur | candidate=HB Torshavn vs Eb/Streymur | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Santa Cruz | target=CD Santa Cruz vs Deportes Temuco | candidate=CD Santa Cruz vs Deportes Temuco | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bahla Club | target=Bahla Club vs Al Nahda | candidate=Bahla Club vs Al Nahda | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=MKS Arka Gdynia | target=MKS Arka Gdynia vs Bruk-Bet Termalica Nieciecza | candidate=MKS Arka Gdynia vs Bruk-Bet Termalica Nieciecza | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Shirak Gyumri | target=FC Shirak Gyumri vs FC Urartu Yerevan | candidate=FC Shirak Gyumri vs FC Urartu Yerevan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ibri | target=Ibri vs Dhofar SCSC | candidate=Ibri vs Dhofar SCSC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Petrolul Ploiesti | target=FC Petrolul Ploiesti vs ASC Otelul Galati | candidate=FC Petrolul Ploiesti vs ASC Otelul Galati | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Orgryte IS | target=Orgryte IS vs IFK Goteborg | candidate=Orgryte IS vs IFK Goteborg | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Uberlandia EC MG | target=Uberlandia EC MG vs Betim Futebol MG | candidate=Uberlandia EC MG vs Betim Futebol MG | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AD Confianca SE | target=AD Confianca SE vs Maranhao AC MA | candidate=AD Confianca SE vs Maranhao AC MA | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Oman Club | target=Oman Club vs Sur SC | candidate=Oman Club vs Sur SC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Leganes'; best=0.0
- multi_odds_match: No multi-odds payload matched event 71498954
- multi_odds_match: No multi-odds payload matched event 71498946
- multi_odds_match: No multi-odds payload matched event 71498952
- multi_odds_match: No multi-odds payload matched event 71498944
- multi_odds_match: No multi-odds payload matched event 71498942
- multi_odds_match: No multi-odds payload matched event 71498950
- multi_odds_match: No multi-odds payload matched event 71498948
- multi_odds_match: No multi-odds payload matched event 67604816
- multi_odds_match: No multi-odds payload matched event 71474802