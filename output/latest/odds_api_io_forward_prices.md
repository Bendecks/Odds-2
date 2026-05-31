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
Events discovery rows: 255
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 68320824, 67919660, 67915884, 70698918, 71425978, 71813848, 71482576, 71749908, 70844446, 67993598, 67473284, 70688010, 71234496, 68306848, 68310928, 67915888, 67915606, 61688416, 68822932, 61688422, 69109024, 67915880, 68214676, 61688410, 66886826, 68822928, 71620932, 68306856, 70688012, 68306850, 70571058, 71732868, 71748832, 71668244, 71748834, 67915608, 67915610, 67017970, 71285000, 71813852, 67017972, 71725764, 71501236, 67126134, 68377618, 67017974, 71679672, 67126142, 67604836, 67017980, 67017982, 67920652, 67017984, 69254680, 71477054, 71706464, 67119372, 67122994, 63534087, 71402660, 71750688, 71378116, 70351018, 71826016, 71396974, 70688014, 67915874, 70688016, 71753152, 71719642, 61623936, 71826654, 67681886, 68097934, 71740604, 61623950, 61623940, 61623954, 61623946, 70844454
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 255
Event selection diagnostic rows: 17240
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 48
Latest x-ratelimit-reset: 2026-05-31T14:12:09Z
Latest retry-after: None

- 2026-05-31 13:45 | IFK Lidingo FK vs Falu BS FK | odds_api_io_Bet365_ML | 3.9/3.9/1.666
- 2026-05-31 14:00 | Aalesund FK 2 vs Strindheim TF | odds_api_io_Bet365_ML | 2.1/4.5/2.5
- 2026-05-31 14:00 | Arendal FK vs Sotra SK | odds_api_io_Bet365_ML | 3.2/3.6/1.9
- 2026-05-31 14:00 | Augnablik Kopavogur vs Hottur/Huginn | odds_api_io_Bet365_ML | 2.55/4.0/2.15
- 2026-05-31 14:00 | Brighton and Hove Albion WFC vs Manchester City WFC | odds_api_io_Bet365_ML | 7.0/4.5/1.363
- 2026-05-31 14:00 | Club Highland Players vs 10 de Noviembre Wilstermann Cooperativas | odds_api_io_Bet365_ML | 2.8/3.7/2.05
- 2026-05-31 14:00 | Czechia vs Kosovo | odds_api_io_Bet365_ML | 1.8/3.3/4.0
- 2026-05-31 14:00 | Ebk vs HJK Akatemia | odds_api_io_Bet365_ML | 1.333/5.0/6.0
- 2026-05-31 14:00 | Ellidi vs Ulfanir | odds_api_io_Bet365_ML | 1.7/4.5/3.25
- 2026-05-31 14:00 | FC Hoyvik vs NSI Runavik II | odds_api_io_Bet365_ML | 2.35/3.9/2.3

## Event selection diagnostics

- src=events_bookmaker_filtered | query=IFK Lidingo FK | target=IFK Lidingo FK vs Falu BS FK | candidate=IFK Lidingo FK vs Falu BS FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cape Verde | target=Cape Verde vs Serbia | candidate=Cape Verde vs Serbia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FBC Melgar | target=FBC Melgar vs Alianza Atletico | candidate=FBC Melgar vs Alianza Atletico | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Red Bull Bragantino SP | target=Red Bull Bragantino SP vs SC Internacional RS | candidate=Red Bull Bragantino SP vs SC Internacional RS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ebk | target=Ebk vs HJK Akatemia | candidate=Ebk vs HJK Akatemia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dragonas IDV | target=Dragonas IDV vs Universidad Catolica Del Ecuador | candidate=Dragonas IDV vs Universidad Catolica Del Ecuador | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CE Europa | target=CE Europa vs RC Celta Fortuna | candidate=CE Europa vs RC Celta Fortuna | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Levanger FK | target=Levanger FK vs IK Junkeren | candidate=Levanger FK vs IK Junkeren | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ostersunds FK | target=Ostersunds FK vs Orebro SK | candidate=Ostersunds FK vs Orebro SK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Arendal FK | target=Arendal FK vs Sotra SK | candidate=Arendal FK vs Sotra SK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Racing Santander | target=Racing Santander vs Cadiz CF | candidate=Racing Santander vs Cadiz CF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IR Reykjavik | target=IR Reykjavik vs IF Vestri | candidate=IR Reykjavik vs IF Vestri | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Karlbergs BK | target=Karlbergs BK vs FBK Karlstad | candidate=Karlbergs BK vs FBK Karlstad | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kongsvinger IL Toppfotball | target=Kongsvinger IL Toppfotball vs Aasane Fotball | candidate=Kongsvinger IL Toppfotball vs Aasane Fotball | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=RC Deportivo De La Coruna | target=RC Deportivo De La Coruna vs UD Las Palmas | candidate=RC Deportivo De La Coruna vs UD Las Palmas | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ranheim | target=Ranheim vs Sandnes Ulf | candidate=Ranheim vs Sandnes Ulf | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PK-35 Helsinki | target=PK-35 Helsinki vs HJK Klubi 04 | candidate=PK-35 Helsinki vs HJK Klubi 04 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kari | target=Kari vs Dalvik Reynir | candidate=Kari vs Dalvik Reynir | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Universidad de Concepcion | target=Universidad de Concepcion vs Palestino | candidate=Universidad de Concepcion vs Palestino | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AD Cantolao | target=AD Cantolao vs CDU San Martin | candidate=AD Cantolao vs CDU San Martin | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 67473284
- multi_odds_match: No multi-odds payload matched event 70688010
- multi_odds_match: No multi-odds payload matched event 71234496
- multi_odds_match: No multi-odds payload matched event 68306848
- multi_odds_match: No multi-odds payload matched event 68310928
- multi_odds_match: No multi-odds payload matched event 67915888
- multi_odds_match: No multi-odds payload matched event 67915606
- multi_odds_match: No multi-odds payload matched event 61688416
- multi_odds_match: No multi-odds payload matched event 68822932
- multi_odds_match: No multi-odds payload matched event 61688422