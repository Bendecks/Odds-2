# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 3 / 8
Max discovery calls: 7
Events bookmaker: Bet365
Events discovery rows: 162
Events max pages: 4
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 30
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 69195816, 71325526, 71111302, 61651664, 71372286, 67817690, 71348330, 67817692, 71240286, 67817694, 71372284, 71240276, 70478154, 71161224, 71436762, 61651656, 71378880, 71338142, 70478164, 71336688, 69880304, 71325988, 68746468, 69880306, 70316166, 71338854, 71338856, 70906728, 71228890, 68492514
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 162
Event selection diagnostic rows: 4425
Selected event rows: 30
Priced event rows: 10
Price rows: 10
Errors/status rows: 20

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 70
Latest x-ratelimit-reset: 2026-05-12T07:49:01Z
Latest retry-after: None

- 2026-05-12 07:30 | Canberra White Eagles FC vs Queanbeyan City FC | odds_api_io_Bet365_ML | 7.0/5.0/1.3
- 2026-05-12 08:45 | Brothers Union vs Mohammedan SC Dhaka | odds_api_io_Bet365_ML | 3.6/3.6/1.8
- 2026-05-12 09:45 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | odds_api_io_Bet365_ML | 10.0/6.25/1.181
- 2026-05-12 10:00 | FC Oleksandriya vs FC Zorya Luhansk | odds_api_io_Bet365_ML | 3.6/3.2/1.909
- 2026-05-12 10:30 | Cerro Porteno Asuncion vs Guarani Asuncion | odds_api_io_Bet365_ML | 2.05/3.75/2.75
- 2026-05-12 10:30 | Gangwon FC vs Daejeon Citizen FC | odds_api_io_Bet365_ML | 2.1/3.1/3.3
- 2026-05-12 10:30 | Gold Coast Knights vs Gold Coast United FC | odds_api_io_Bet365_ML | 1.055/12.0/29.0
- 2026-05-12 10:30 | Gwangju FC vs FC Seoul | odds_api_io_Bet365_ML | 8.0/4.2/1.38
- 2026-05-12 10:30 | Hellenic Athletic Club vs Darwin Hearts FC | odds_api_io_Bet365_ML | 4.0/4.5/1.571
- 2026-05-12 10:30 | Incheon United FC vs FC Pohang Steelers | odds_api_io_Bet365_ML | 2.625/2.9/2.7

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Canberra White Eagles FC | target=Canberra White Eagles FC vs Queanbeyan City FC | candidate=Canberra White Eagles FC vs Queanbeyan City FC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Deportivo Maldonado Reserve | target=Deportivo Maldonado Reserve vs Racing Club Montevideo | candidate=Deportivo Maldonado Reserve vs Racing Club Montevideo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gangwon FC | target=Gangwon FC vs Daejeon Citizen FC | candidate=Gangwon FC vs Daejeon Citizen FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Wasl | target=AL Wasl vs AL Jazira | candidate=AL Wasl vs AL Jazira | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gwangju FC | target=Gwangju FC vs FC Seoul | candidate=Gwangju FC vs FC Seoul | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gwelup Croatia SC Reserves | target=Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | candidate=Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sportivo Ameliano | target=Sportivo Ameliano vs Deportivo Recoleta Reserve | candidate=Sportivo Ameliano vs Deportivo Recoleta Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Epitsentr Kamianets-Podilskyi | target=FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | candidate=FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Liepaja | target=FK Liepaja vs Ogre United | candidate=FK Liepaja vs Ogre United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cerro Porteno Asuncion | target=Cerro Porteno Asuncion vs Guarani Asuncion | candidate=Cerro Porteno Asuncion vs Guarani Asuncion | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hellenic Athletic Club | target=Hellenic Athletic Club vs Darwin Hearts FC | candidate=Hellenic Athletic Club vs Darwin Hearts FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Singida Black Stars SC | target=Singida Black Stars SC vs Namungo FC | candidate=Singida Black Stars SC vs Namungo FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra White Eagles FC | target=Canberra White Eagles FC vs Queanbeyan City FC | candidate=Canberra White Eagles FC vs Queanbeyan City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Pharco FC | target=Pharco FC vs Modern Sport FC | candidate=Pharco FC vs Modern Sport FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sunshine Coast Wanderers FC | target=Sunshine Coast Wanderers FC vs Eastern Suburbs FC | candidate=Sunshine Coast Wanderers FC vs Eastern Suburbs FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fardu Ferghana | target=Fardu Ferghana vs Xorazm Fk Urganch | candidate=Fardu Ferghana vs Xorazm Fk Urganch | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=URA FC | target=URA FC vs Calvary | candidate=URA FC vs Calvary | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Incheon United FC | target=Incheon United FC vs FC Pohang Steelers | candidate=Incheon United FC vs FC Pohang Steelers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Murdoch University Melville FC Reserves | target=Murdoch University Melville FC Reserves vs Joondalup City FC Reserve | candidate=Murdoch University Melville FC Reserves vs Joondalup City FC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sur SC | target=Sur SC vs Al-Khaboora | candidate=Sur SC vs Al-Khaboora | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71372284
- multi_odds_match: No multi-odds payload matched event 71240276
- multi_odds_match: No multi-odds payload matched event 70478154
- multi_odds_match: No multi-odds payload matched event 71161224
- multi_odds_match: No multi-odds payload matched event 71436762
- multi_odds_match: No multi-odds payload matched event 61651656
- multi_odds_match: No multi-odds payload matched event 71378880
- multi_odds_match: No multi-odds payload matched event 71338142
- multi_odds_match: No multi-odds payload matched event 70478164
- multi_odds_match: No multi-odds payload matched event 71336688