# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 11 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 923
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Celtic, Falkirk, Hibernian, Sociedad B
Selected event IDs: 61515296, 61967610, 62227492, 61515276, 61515274, 61515288, 61840784, 61515278, 61967614, 61967622, 61967620, 61967626, 61967618, 61967616, 61515282, 61515292, 62229200, 61967624, 62229202, 62227500, 62229194, 61515284, 61911542, 67915836, 67017924, 71525190, 71466052, 61737724, 71096656, 71439906, 66855362, 71243190, 61730244, 67017926, 71481668, 67015180, 68310894, 68214652, 68954834, 61286593, 67017928, 67473260, 68320788, 67091306, 69342846, 69109000, 63039299, 70023854, 71453378, 71462680, 62036278, 70698894, 61911546, 67015182, 67017930, 61467293, 67015184, 67017932, 70730400, 68377662, 61737730, 71460644, 70698900, 67015186, 70207500, 62274218, 67091308, 66855368, 67017934, 67017936, 70221642, 68320784, 70687992, 67015188, 66855364, 71491072
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 903
Event selection diagnostic rows: 70995
Selected event rows: 76
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 11
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 25
Latest x-ratelimit-reset: 2026-05-16T13:56:57Z
Latest retry-after: None

- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz | odds_api_io_Bet365_ML | 1.909/4.2/3.4
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC | odds_api_io_Bet365_ML | 1.833/3.9/3.2
- 2026-05-16 13:30 | ADO 20 Heemskerk vs VV Scherpenzeel | odds_api_io_Bet365_ML | 2.1/3.4/2.9
- 2026-05-16 13:30 | Bayer Leverkusen vs Hamburger SV | odds_api_io_Bet365_ML | 1.3/6.5/7.5
- 2026-05-16 13:30 | Bayern Munich vs 1. FC Cologne | odds_api_io_Bet365_ML | 1.142/8.5/11.0
- 2026-05-16 13:30 | Borussia Monchengladbach vs TSG Hoffenheim | odds_api_io_Bet365_ML | 4.5/4.5/1.65
- 2026-05-16 13:30 | FC Chernomorets Odessa vs FC Livyi Bereh Kyiv | odds_api_io_Bet365_ML | 2.55/3.1/2.55
- 2026-05-16 13:30 | Eintracht Frankfurt vs VfB Stuttgart | odds_api_io_Bet365_ML | 3.2/4.0/1.8
- 2026-05-16 13:30 | Excelsior Maassluis vs Jong Almere City FC | odds_api_io_Bet365_ML | 2.3/3.75/2.45
- 2026-05-16 13:30 | HHC Hardenberg vs Kozakken Boys Werkendam | odds_api_io_Bet365_ML | 1.9/3.7/3.1

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Waterford FC | target=Waterford FC vs Sligo Rovers | candidate=Waterford FC vs Sligo Rovers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=HHC Hardenberg | target=HHC Hardenberg vs Kozakken Boys Werkendam | candidate=HHC Hardenberg vs Kozakken Boys Werkendam | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Arendal FK | target=Arendal FK vs FK Jerv | candidate=Arendal FK vs FK Jerv | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lyn 1896 FK | target=Lyn 1896 FK vs Kongsvinger IL Toppfotball | candidate=Lyn 1896 FK vs Kongsvinger IL Toppfotball | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SV Togb | target=SV Togb vs Groene Ster | candidate=SV Togb vs Groene Ster | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Odisha FC | target=Odisha FC vs Punjab FC | candidate=Odisha FC vs Punjab FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bryne FK | target=Bryne FK vs Stroemmen IF | candidate=Bryne FK vs Stroemmen IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Irtysh Pavlodar | target=FC Irtysh Pavlodar vs FC Yelimai | candidate=FC Irtysh Pavlodar vs FC Yelimai | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Onsala BK | target=Onsala BK vs Hestrafors IF | candidate=Onsala BK vs Hestrafors IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Taby FK | target=Taby FK vs Sunnersta AIF | candidate=Taby FK vs Sunnersta AIF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CE Carroi | target=CE Carroi vs Inter Club de Escaldes | candidate=CE Carroi vs Inter Club de Escaldes | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=A-Xiii Auhof Center | target=A-Xiii Auhof Center vs WAF Vorwarts Brigittenau | candidate=A-Xiii Auhof Center vs WAF Vorwarts Brigittenau | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Viking FK | target=Viking FK vs IK Start | candidate=Viking FK vs IK Start | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lillestroem SK | target=Lillestroem SK vs Sandefjord Fotball | candidate=Lillestroem SK vs Sandefjord Fotball | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SV Spakenburg | target=SV Spakenburg vs VV Katwijk | candidate=SV Spakenburg vs VV Katwijk | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=UMF Selfoss | target=UMF Selfoss vs Kormakur/Hvot | candidate=UMF Selfoss vs Kormakur/Hvot | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Mariehamn | target=IFK Mariehamn vs Kuopion Palloseura | candidate=IFK Mariehamn vs Kuopion Palloseura | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Independiente Cbba | target=CA Independiente Cbba vs Club Tigres FC | candidate=CA Independiente Cbba vs Club Tigres FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Rosenborg BK | target=Rosenborg BK vs Aalesunds FK | candidate=Rosenborg BK vs Aalesunds FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=ADO 20 Heemskerk | target=ADO 20 Heemskerk vs VV Scherpenzeel | candidate=ADO 20 Heemskerk vs VV Scherpenzeel | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Celtic'; best=0.5933
- event_selection: No event above confidence 0.72 for query 'Falkirk'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Hibernian'; best=0.5281
- event_selection: No event above confidence 0.72 for query 'Sociedad B'; best=0.3153
- multi_odds_match: No multi-odds payload matched event 61967620
- multi_odds_match: No multi-odds payload matched event 61967626
- multi_odds_match: No multi-odds payload matched event 61967618
- multi_odds_match: No multi-odds payload matched event 61967616
- multi_odds_match: No multi-odds payload matched event 61515282
- multi_odds_match: No multi-odds payload matched event 61515292