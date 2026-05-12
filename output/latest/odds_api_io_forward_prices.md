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
Events discovery rows: 113
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Asteras Tripolis, Kifisia, Panetolikos, Celta, Betis, Aberdeen, Dundee United, Kilmarnock, Osasuna, BC Olympiakos Piraeus, Levadeiakos, Volos NFC
Selected event IDs: 71428876, 71172384, 70379156, 71289488, 70401284, 71354552, 67912056, 69090796, 71344616, 71344526, 71297420, 71172360, 70379158, 71218642, 71428878, 70401308, 70424976, 71297438, 71218644, 67645510, 67644942, 67817696, 67817698, 67817700, 70906782, 70231954, 70231952, 70905772, 68685980, 61062283, 70231844, 70231854, 61624648, 67126096, 67126086, 67126088, 67126098, 67126092, 70315368, 70905774, 70722406, 71282488, 61624654, 61062299, 71406950, 70674830, 70674826, 71019438, 70674828, 70315360, 71242306, 70784812, 61624638, 61624644, 71325020, 71428928, 71076888
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: European Handicap, ML
Fixture rows: 115
Event selection diagnostic rows: 6835
Selected event rows: 57
Priced event rows: 10
Price rows: 10
Errors/status rows: 58

## Provider rate-limit headers

Header rows captured: 14
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 0
Latest x-ratelimit-reset: 2026-05-12T21:55:16Z
Latest retry-after: None

- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe | odds_api_io_Bet365_ML | 2.4/2.9/3.3
- 2026-05-12 22:00 | Deportivo Tachira vs Metropolitanos FC | odds_api_io_Bet365_ML | 1.571/3.4/5.5
- 2026-05-12 22:00 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | odds_api_io_Bet365_European Handicap | 3.5/21.0/41.0
- 2026-05-12 22:30 | Londrina EC PR vs Sao Bernardo FC | odds_api_io_Bet365_ML | 2.3/2.75/3.7
- 2026-05-12 22:30 | SC Internacional RS vs Athletic Club Sjdr MG | odds_api_io_Bet365_ML | 1.285/5.25/10.0
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC | odds_api_io_Bet365_ML | 5.0/3.2/1.666
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride | odds_api_io_Bet365_ML | 2.9/3.5/2.0
- 2026-05-12 23:00 | LVU Rush vs West Chester United SC USL2 | odds_api_io_Bet365_ML | 5.0/4.75/1.42
- 2026-05-12 23:00 | Mahaut Soca Strikers vs Middleham United FC | odds_api_io_Bet365_ML | 1.55/4.333/4.333
- 2026-05-12 23:00 | St Andrew Lions vs Ellerton FC | odds_api_io_Bet365_ML | 4.75/4.1/1.55

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Club Aurora | target=Club Aurora vs Cdt Real Oruro | candidate=Club Aurora vs Cdt Real Oruro | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bogota FC | target=Bogota FC vs Barranquilla FC | candidate=Bogota FC vs Barranquilla FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Norrkoping FK | target=IFK Norrkoping FK vs Nordic United FC | candidate=IFK Norrkoping FK vs Nordic United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Helsingborgs IF | target=Helsingborgs IF vs IK Oddevold | candidate=Helsingborgs IF vs IK Oddevold | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Arsenal WFC | target=Arsenal WFC vs Everton FC | candidate=Arsenal WFC vs Everton FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Olancho FC | target=Olancho FC vs FC Motagua Tegucigalpa | candidate=Olancho FC vs FC Motagua Tegucigalpa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Belgrano de Cordoba | target=CA Belgrano de Cordoba vs Union de Santa Fe | candidate=CA Belgrano de Cordoba vs Union de Santa Fe | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IK Brage | target=IK Brage vs Ostersunds FK | candidate=IK Brage vs Ostersunds FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Osters IF | target=Osters IF vs Sandvikens IF | candidate=Osters IF vs Sandvikens IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PFC Ludogorets 1945 Razgrad | target=PFC Ludogorets 1945 Razgrad vs PFC Levski Sofia | candidate=PFC Ludogorets 1945 Razgrad vs PFC Levski Sofia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=GV Club Deportivo San Jose de Oruro | target=GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | candidate=GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Vojvodina Novi Sad | target=FK Vojvodina Novi Sad vs FK Crvena Zvezda Belgrade | candidate=FK Vojvodina Novi Sad vs FK Crvena Zvezda Belgrade | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cruzeiro EC MG | target=Cruzeiro EC MG vs Goias EC GO | candidate=Cruzeiro EC MG vs Goias EC GO | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PAOK Thessaloniki | target=PAOK Thessaloniki vs AEK Athens | candidate=PAOK Thessaloniki vs AEK Athens | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Olympiacos Piraeus | target=Olympiacos Piraeus vs Panathinaikos Athens | candidate=Olympiacos Piraeus vs Panathinaikos Athens | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=MKS Arka Gdynia | target=MKS Arka Gdynia vs Gornik Zabrze | candidate=MKS Arka Gdynia vs Gornik Zabrze | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Villarreal | target=Villarreal vs Sevilla | candidate=Villarreal CF vs Sevilla FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Londrina EC PR | target=Londrina EC PR vs Sao Bernardo FC | candidate=Londrina EC PR vs Sao Bernardo FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Espanyol Barcelona | target=Espanyol Barcelona vs Athletic Bilbao | candidate=Espanyol Barcelona vs Athletic Bilbao | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Argentinos Juniors | target=Argentinos Juniors vs CA Huracan | candidate=Argentinos Juniors vs CA Huracan | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Asteras Tripolis'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Kifisia'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Panetolikos'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Celta'; best=0.48
- event_selection: No event above confidence 0.72 for query 'Betis'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Aberdeen'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Dundee United'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Kilmarnock'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Osasuna'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Levadeiakos'; best=0.0