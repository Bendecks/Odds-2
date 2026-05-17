# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 5 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 583
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 66299200, 69195814, 67807388, 68728640, 67645066, 69195322, 71495134, 71213396, 67692600, 68050298, 67691606, 67645068, 67648306, 67648148, 67645560, 67648464, 67648302, 67648308, 67904436, 67692602, 67807826, 68162384, 68916302, 67648466, 67648304, 67648150, 68916304, 67647988, 67694246, 68728646, 67645072, 67645070, 67904150, 71127906, 67648462, 68051600, 67694248, 70813618, 67904152, 67904438, 69767364, 67692606, 71423418, 69767366, 70968254, 67692246, 68046518, 70968234, 68046520, 67817706, 71465130, 68046516, 67817708, 67692610, 71000982, 67904440, 62778613, 62778611, 62778617, 66053720, 62083182, 62160254, 62181558, 62160252, 62181556, 62415644, 62181566, 62161250, 67648468, 71457340, 71000984, 63039311, 62161254, 71483872, 61061679, 67817710, 71300072, 71483564, 71483754, 71299758
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 583
Event selection diagnostic rows: 43480
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 41
Latest x-ratelimit-reset: 2026-05-17T02:58:57Z
Latest retry-after: None

- 2026-05-17 02:30 | San Jose Earthquakes vs FC Dallas | odds_api_io_Bet365_ML | 2.0/3.75/3.4
- 2026-05-17 02:45 | Canberra White Eagles FC vs Canberra Juventus FC | odds_api_io_Bet365_ML | 29.0/13.0/1.05
- 2026-05-17 03:00 | Broadmeadow Magic FC vs Edgeworth FC | odds_api_io_Bet365_ML | 1.85/3.6/3.4
- 2026-05-17 04:00 | Okayama Yunogo Belle vs Nittaidai FC | odds_api_io_Bet365_ML | 1.5/4.0/5.0
- 2026-05-17 04:00 | V-Varen Nagasaki vs Vissel Kobe | odds_api_io_Bet365_ML | 4.75/3.5/1.75
- 2026-05-17 04:30 | Canberra Olympic vs Tuggeranong United FC | odds_api_io_Bet365_ML | 1.02/21.0/51.0
- 2026-05-17 04:30 | Diavorosso Hiroshima vs Yamato Sylphid | odds_api_io_Bet365_ML | 1.727/3.2/4.5
- 2026-05-17 04:30 | Fukien vs Kwong Wah | odds_api_io_Bet365_ML | 1.42/5.0/4.75
- 2026-05-17 04:40 | Bulls FC Academy vs Manly United FC | odds_api_io_Bet365_ML | 1.7/3.9/3.7
- 2026-05-17 04:45 | Adelaide Olympic FC Reserve vs Cumberland United Reserve | odds_api_io_Bet365_ML | 1.615/5.25/3.2

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Iwaki FC | target=Iwaki FC vs Matsumoto Yamaga FC | candidate=Iwaki FC vs Matsumoto Yamaga FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ferencvarosi TC II | target=Ferencvarosi TC II vs Pecsi MFC | candidate=Ferencvarosi TC II vs Pecsi MFC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Debreceni VSC II | target=Debreceni VSC II vs Tiszaujvaros | candidate=Debreceni VSC II vs Tiszaujvaros | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=V-Varen Nagasaki | target=V-Varen Nagasaki vs Vissel Kobe | candidate=V-Varen Nagasaki vs Vissel Kobe | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bucheon FC 1995 | target=Bucheon FC 1995 vs FC Pohang Steelers | candidate=Bucheon FC 1995 vs FC Pohang Steelers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=RB Omiya Ardija | target=RB Omiya Ardija vs AC Nagano Parceiro | candidate=RB Omiya Ardija vs AC Nagano Parceiro | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hwaseong FC | target=Hwaseong FC vs Busan I Park | candidate=Hwaseong FC vs Busan I Park | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Paksi FC II | target=Paksi FC II vs Majosi SE | candidate=Paksi FC II vs Majosi SE | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kagoshima United | target=Kagoshima United vs Roasso Kumamoto | candidate=Kagoshima United vs Roasso Kumamoto | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fagiano Okayama | target=Fagiano Okayama vs Shimizu S-Pulse | candidate=Fagiano Okayama vs Shimizu S-Pulse | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra White Eagles FC | target=Canberra White Eagles FC vs Canberra Juventus FC | candidate=Canberra White Eagles FC vs Canberra Juventus FC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Club Deportiva Minera | target=Club Deportiva Minera vs CD Coria | candidate=Club Deportiva Minera vs CD Coria | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=JEF United Chiba | target=JEF United Chiba vs Kashima Antlers | candidate=JEF United Chiba vs Kashima Antlers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lee Man FC | target=Lee Man FC vs Tai Po FC | candidate=Lee Man FC vs Tai Po FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra White Eagles FC | target=Canberra White Eagles FC vs Canberra Juventus FC | candidate=Canberra White Eagles FC vs Canberra Juventus FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bali United | target=Bali United vs Bhayangkara Presisi Indonesia FC | candidate=Bali United vs Bhayangkara Presisi Indonesia FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bulls FC Academy U23 | target=Bulls FC Academy U23 vs Manly United FC | candidate=Bulls FC Academy U23 vs Manly United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Ryukyu | target=FC Ryukyu vs Gainare Tottori | candidate=FC Ryukyu vs Gainare Tottori | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Garuda FC | target=Garuda FC vs Palmerston Rovers | candidate=Garuda FC vs Palmerston Rovers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Adelaide Olympic FC Reserve | target=Adelaide Olympic FC Reserve vs Cumberland United Reserve | candidate=Adelaide Olympic FC Reserve vs Cumberland United Reserve | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 67691606
- multi_odds_match: No multi-odds payload matched event 67645068
- multi_odds_match: No multi-odds payload matched event 67648306
- multi_odds_match: No multi-odds payload matched event 67648148
- multi_odds_match: No multi-odds payload matched event 67645560
- multi_odds_match: No multi-odds payload matched event 67648464
- multi_odds_match: No multi-odds payload matched event 67648302
- multi_odds_match: No multi-odds payload matched event 67648308
- multi_odds_match: No multi-odds payload matched event 67904436
- multi_odds_match: No multi-odds payload matched event 67692602