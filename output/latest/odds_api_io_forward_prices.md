# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 14 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 157
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Levadeiakos, Volos NFC, Olympiakos, PAOK, Brest, Espanol, Hearts, Lens, Man City, Motherwell, Rangers, Santiago Wanderers
Selected event IDs: 67645510, 67644942, 67817696, 67817698, 67817700, 70906782, 70231954, 70231952, 70905772, 68685980, 61062283, 70231844, 70231854, 61624648, 67126096, 67126086, 67126088, 67126098, 67126092, 70315368, 70905774, 70722406, 71282488, 61624654, 61062299, 71406950, 70674830, 70674826, 71019438, 70674828, 70315360, 71242306, 70784812, 61624638, 61624644, 71325020, 71428928, 70452650, 70401280, 70401282, 71297426, 71172386, 66299148, 71172362, 66299150, 66299152, 70401292, 66299154, 66299156, 66299158, 66299160, 71428930, 70401310, 70401296, 66299162, 70401286, 66299166, 66299168, 66299164, 71297590, 66299170, 66299172, 66299174, 70318288, 70906780, 70267784, 69254646
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 194
Event selection diagnostic rows: 10066
Selected event rows: 67
Priced event rows: 10
Price rows: 10
Errors/status rows: 68

## Provider rate-limit headers

Header rows captured: 14
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 81
Latest x-ratelimit-reset: 2026-05-13T03:28:43Z
Latest retry-after: None

- 2026-05-13 10:00 | Machida Zelvia vs Tokyo Verdy | odds_api_io_Bet365_ML | 1.8/3.25/5.0
- 2026-05-13 10:00 | Vissel Kobe vs Kyoto Sanga FC | odds_api_io_Bet365_ML | 1.7/3.6/5.0
- 2026-05-13 10:30 | FC Anyang vs Gimcheon Sangmu FC | odds_api_io_Bet365_ML | 2.35/3.1/2.875
- 2026-05-13 10:30 | Bucheon FC 1995 vs Jeonbuk FC | odds_api_io_Bet365_ML | 4.1/3.3/1.8
- 2026-05-13 10:30 | Ulsan HD FC vs Jeju SK FC | odds_api_io_Bet365_ML | 1.85/3.3/4.0
- 2026-05-13 12:15 | PFC Slavia Sofia vs PFC Dobrudzha Dobrich | odds_api_io_Bet365_ML | 2.6/3.4/2.5
- 2026-05-13 14:00 | APO Levadiakos FC vs OFI Crete | odds_api_io_Bet365_ML | 1.615/4.2/5.0
- 2026-05-13 14:00 | Volos NPS vs Aris Thessaloniki | odds_api_io_Bet365_ML | 4.0/3.5/1.9
- 2026-05-13 14:45 | PFC CSKA Sofia vs FC CSKA 1948 | odds_api_io_Bet365_ML | 2.2/3.1/3.5
- 2026-05-13 15:00 | Forge FC Hamilton vs FC Supra Du Quebec | odds_api_io_Bet365_ML | 1.666/4.5/3.6

## Event selection diagnostics

- src=events_search_fallback | query=Santiago Wanderers | target=Santiago Wanderers vs Union Espanola | candidate=Santiago Wanderers vs Union Espanola | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Olympiacos Piraeus | target=Olympiacos Piraeus vs Panathinaikos Athens | candidate=Olympiacos Piraeus vs Panathinaikos Athens | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=MKS Arka Gdynia | target=MKS Arka Gdynia vs Gornik Zabrze | candidate=MKS Arka Gdynia vs Gornik Zabrze | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Septemvri Sofia | target=FK Septemvri Sofia vs FK Spartak 1918 Varna | candidate=FK Septemvri Sofia vs FK Spartak 1918 Varna | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Helsingborgs IF | target=Helsingborgs IF vs IK Oddevold | candidate=Helsingborgs IF vs IK Oddevold | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Forge FC Hamilton | target=Forge FC Hamilton vs FC Supra Du Quebec | candidate=Forge FC Hamilton vs FC Supra Du Quebec | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IK Brage | target=IK Brage vs Ostersunds FK | candidate=IK Brage vs Ostersunds FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Espanyol Barcelona | target=Espanyol Barcelona vs Athletic Bilbao | candidate=Espanyol Barcelona vs Athletic Bilbao | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Mjallby AIF | target=Mjallby AIF vs Hammarby IF | candidate=Mjallby AIF vs Hammarby IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Norrkoping FK | target=IFK Norrkoping FK vs Nordic United FC | candidate=IFK Norrkoping FK vs Nordic United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Falkenbergs FF | target=Falkenbergs FF vs Varbergs BoIS | candidate=Falkenbergs FF vs Varbergs BoIS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PAOK Thessaloniki | target=PAOK Thessaloniki vs AEK Athens | candidate=PAOK Thessaloniki vs AEK Athens | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Villarreal | target=Villarreal vs Sevilla | candidate=Villarreal CF vs Sevilla FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PFC CSKA Sofia | target=PFC CSKA Sofia vs FC CSKA 1948 | candidate=PFC CSKA Sofia vs FC CSKA 1948 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Stade Brest 29 | target=Stade Brest 29 vs Strasbourg Alsace | candidate=Stade Brest 29 vs Strasbourg Alsace | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PFC Ludogorets 1945 Razgrad | target=PFC Ludogorets 1945 Razgrad vs PFC Levski Sofia | candidate=PFC Ludogorets 1945 Razgrad vs PFC Levski Sofia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hobro IK | target=Hobro IK vs Aarhus Fremad | candidate=Hobro IK vs Aarhus Fremad | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Osters IF | target=Osters IF vs Sandvikens IF | candidate=Osters IF vs Sandvikens IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Volos NPS | target=Volos NPS vs Aris Thessaloniki | candidate=Volos NPS vs Aris Thessaloniki | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Glasgow Rangers | target=Glasgow Rangers vs Hibernian FC | candidate=Glasgow Rangers vs Hibernian FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Levadeiakos'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Volos NFC'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Olympiakos'; best=0.6304
- event_selection: No event above confidence 0.72 for query 'PAOK'; best=0.6029
- event_selection: No event above confidence 0.72 for query 'Brest'; best=0.5979
- event_selection: No event above confidence 0.72 for query 'Espanol'; best=0.6029
- event_selection: No event above confidence 0.72 for query 'Hearts'; best=0.4911
- event_selection: No event above confidence 0.72 for query 'Lens'; best=0.6418
- event_selection: No event above confidence 0.72 for query 'Man City'; best=0.5467
- event_selection: No event above confidence 0.72 for query 'Motherwell'; best=0.5533