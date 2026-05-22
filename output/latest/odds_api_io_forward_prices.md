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
Events discovery rows: 746
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 71186824, 71186826, 71186828, 71589718, 68492538, 70906796, 70906794, 70708886, 62036296, 70906792, 67790442, 69920644, 70479408, 62037524, 71589682, 69924674, 67845760, 71183116, 67604820, 62036298, 63185791, 68538256, 70683976, 71037644, 70318296, 69670720, 69670722, 69670724, 61737344, 61737340, 69670718, 61737342, 62038140, 62037514, 70654946, 66918146, 61898644, 61911610, 62274234, 67845762, 61467303, 61286603, 71579030, 66606322, 71621906, 61687634, 67919634, 67919910, 70162040, 71589720, 61898646, 70684202, 70730322, 71613278, 70730376, 67149482, 67919638, 71613276, 67126566, 68377678, 68344658, 67473272, 68311612, 61541440, 68377682, 68344660, 68311614, 69921776, 69972736, 71589722, 70730784, 67473280, 67919642, 69880344, 62036912, 61940286, 68344662, 61902050, 61902060, 61902062
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 746
Event selection diagnostic rows: 56520
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 6
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 52
Latest x-ratelimit-reset: 2026-05-22T15:13:59Z
Latest retry-after: None

- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol | odds_api_io_Bet365_ML | 1.8/4.1/3.75
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca | odds_api_io_Bet365_ML | 2.2/3.6/3.0
- 2026-05-22 14:30 | Pafos FC vs APOEL Nikosia | odds_api_io_Bet365_ML | 1.85/3.6/4.1
- 2026-05-22 15:00 | AS Armee vs FC Brakna | odds_api_io_Bet365_ML | 2.45/2.9/2.7
- 2026-05-22 15:00 | FK Auda Riga vs FK Liepaja | odds_api_io_Bet365_ML | 2.1/3.2/3.1
- 2026-05-22 15:00 | FK Septemvri Sofia vs PFC Dobrudzha Dobrich | odds_api_io_Bet365_ML | 1.533/4.333/5.5
- 2026-05-22 15:00 | FK Spartak 1918 Varna vs FC Lokomotiv 1929 Sofia | odds_api_io_Bet365_ML | 1.6/3.8/5.5
- 2026-05-22 15:00 | FK Zeleznicar Pancevo vs FK Cukaricki Belgrade | odds_api_io_Bet365_ML | 1.75/4.0/4.0
- 2026-05-22 15:00 | Korona II Kielce SA vs MKS Czarni Polaniec | odds_api_io_Bet365_ML | 2.3/3.5/2.55
- 2026-05-22 15:00 | POFC Botev Vratsa vs PFK Beroe Stara Zagora | odds_api_io_Bet365_ML | 2.25/3.3/3.1

## Event selection diagnostics

- src=events_bookmaker_filtered | query=AC Omonia Nicosia | target=AC Omonia Nicosia vs Apollon Limassol | candidate=AC Omonia Nicosia vs Apollon Limassol | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AS Armee | target=AS Armee vs FC Brakna | candidate=AS Armee vs FC Brakna | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Zaglebie Sosnowiec | target=Zaglebie Sosnowiec vs KKS 1925 Kalisz | candidate=Zaglebie Sosnowiec vs KKS 1925 Kalisz | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hestrafors IF | target=Hestrafors IF vs Jonsereds IF | candidate=Hestrafors IF vs Jonsereds IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Chomutov | target=FC Chomutov vs FK Seko Louny | candidate=FC Chomutov vs FK Seko Louny | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Karlshamn | target=IFK Karlshamn vs Vaxjo Norra | candidate=IFK Karlshamn vs Vaxjo Norra | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Jitex Molndal BK | target=Jitex Molndal BK vs IFK Goteborg | candidate=Jitex Molndal BK vs IFK Goteborg | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sumqayit FK | target=Sumqayit FK vs Qarabag FK | candidate=Sumqayit FK vs Qarabag FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Djurgardens IF | target=Djurgardens IF vs IF Brommapojkarna | candidate=Djurgardens IF vs IF Brommapojkarna | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Djoliba AC | target=Djoliba AC vs Usfas Bamako | candidate=Djoliba AC vs Usfas Bamako | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SV Leobendorf | target=SV Leobendorf vs Favoritner AC | candidate=SV Leobendorf vs Favoritner AC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SV Allerheiligen | target=SV Allerheiligen vs SV Tillmitsch | candidate=SV Allerheiligen vs SV Tillmitsch | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Vg-62 | target=Vg-62 vs Jyty Turku | candidate=Vg-62 vs Jyty Turku | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Auda Riga | target=FK Auda Riga vs FK Liepaja | candidate=FK Auda Riga vs FK Liepaja | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dakar Sacre Coeur | target=Dakar Sacre Coeur vs Teungueth FC | candidate=Dakar Sacre Coeur vs Teungueth FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tampere United | target=Tampere United vs JJK Jyvaskyla | candidate=Tampere United vs JJK Jyvaskyla | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SC Red Star Penzing | target=SC Red Star Penzing vs SK Slovan HAC | candidate=SC Red Star Penzing vs SK Slovan HAC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Marbella FC | target=Marbella FC vs CD Teruel | candidate=Marbella FC vs CD Teruel | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Broendby IF | target=Broendby IF vs Kolding IF | candidate=Broendby IF vs Kolding IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kuopion Palloseura | target=Kuopion Palloseura vs IF Gnistan | candidate=Kuopion Palloseura vs IF Gnistan | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 67790442
- multi_odds_match: No multi-odds payload matched event 69920644
- multi_odds_match: No multi-odds payload matched event 70479408
- multi_odds_match: No multi-odds payload matched event 62037524
- multi_odds_match: No multi-odds payload matched event 71589682
- multi_odds_match: No multi-odds payload matched event 69924674
- multi_odds_match: No multi-odds payload matched event 67845760
- multi_odds_match: No multi-odds payload matched event 71183116
- multi_odds_match: No multi-odds payload matched event 67604820
- multi_odds_match: No multi-odds payload matched event 62036298