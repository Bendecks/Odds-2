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
Events discovery rows: 150
Events max pages: 4
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 30
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 71240276, 70478154, 71161224, 71436762, 61651656, 71378880, 71338142, 70478164, 71336688, 69880304, 71325988, 68746468, 69880306, 70316166, 71338854, 71338856, 70906728, 71228890, 68492514, 71372082, 61651662, 71231390, 61651650, 62036882, 71085582, 71338858, 71085578, 71085580, 70232094, 71328286
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 150
Event selection diagnostic rows: 4065
Selected event rows: 30
Priced event rows: 10
Price rows: 10
Errors/status rows: 20

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 67
Latest x-ratelimit-reset: 2026-05-12T11:43:15Z
Latest retry-after: None

- 2026-05-12 11:00 | Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | odds_api_io_Bet365_ML | 1.45/4.5/4.75
- 2026-05-12 11:00 | Singida Black Stars SC vs Namungo FC | odds_api_io_Bet365_ML | 1.42/3.8/6.5
- 2026-05-12 11:15 | Murdoch University Melville FC Reserves vs Joondalup City FC Reserve | odds_api_io_Bet365_ML | 2.4/4.333/2.15
- 2026-05-12 12:00 | Fardu Ferghana vs Xorazm Fk Urganch | odds_api_io_Bet365_ML | 2.4/3.2/2.625
- 2026-05-12 12:30 | FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | odds_api_io_Bet365_ML | 6.25/3.6/1.48
- 2026-05-12 13:00 | Deportivo Maldonado Reserve vs Racing Club Montevideo | odds_api_io_Bet365_ML | 2.45/3.25/2.55
- 2026-05-12 13:00 | Namdhari FC vs Gokulam Kerala FC | odds_api_io_Bet365_ML | 2.625/3.4/2.3
- 2026-05-12 13:15 | TRA United vs Jkt Tanzania | odds_api_io_Bet365_ML | 2.05/2.9/3.5
- 2026-05-12 13:50 | Sur SC vs Al-Khaboora | odds_api_io_Bet365_ML | 1.95/2.875/4.0
- 2026-05-12 14:00 | El Gouna FC vs Kahrabaa Ismailia | odds_api_io_Bet365_ML | 2.375/2.625/3.1

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Gwelup Croatia SC Reserves | target=Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | candidate=Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Elva | target=FC Elva vs Paide Linnameeskond | candidate=FC Elva vs Paide Linnameeskond | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Wahda FC | target=AL Wahda FC vs Khorfakkan | candidate=AL Wahda FC vs Khorfakkan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=1. FC Slovacko Uherske Hradiste | target=1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | candidate=1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Zaglebie Lubin II | target=Zaglebie Lubin II vs Mkp Carina Gubin | candidate=Zaglebie Lubin II vs Mkp Carina Gubin | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=TRA United | target=TRA United vs Jkt Tanzania | candidate=TRA United vs Jkt Tanzania | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Veres Rivne | target=Veres Rivne vs FC Kryvbas Kriviy Rih | candidate=Veres Rivne vs FC Kryvbas Kriviy Rih | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=MFK Chrudim | target=MFK Chrudim vs FK Pribram | candidate=MFK Chrudim vs FK Pribram | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sur SC | target=Sur SC vs Al-Khaboora | candidate=Sur SC vs Al-Khaboora | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=El Gouna FC | target=El Gouna FC vs Kahrabaa Ismailia | candidate=El Gouna FC vs Kahrabaa Ismailia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Namdhari FC | target=Namdhari FC vs Gokulam Kerala FC | candidate=Namdhari FC vs Gokulam Kerala FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Mlada Boleslav | target=FK Mlada Boleslav vs Dukla Prague | candidate=FK Mlada Boleslav vs Dukla Prague | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=URA FC | target=URA FC vs Calvary | candidate=URA FC vs Calvary | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Pharco FC | target=Pharco FC vs Modern Sport FC | candidate=Pharco FC vs Modern Sport FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Mohun Bagan Super Giant | target=Mohun Bagan Super Giant vs Inter Kashi FC | candidate=Mohun Bagan Super Giant vs Inter Kashi FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Inter Turku | target=FC Inter Turku vs JS Hercules | candidate=FC Inter Turku vs JS Hercules | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=JS Omrane | target=JS Omrane vs Avenir S Marsa | candidate=JS Omrane vs Avenir S Marsa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Singida Black Stars SC | target=Singida Black Stars SC vs Namungo FC | candidate=Singida Black Stars SC vs Namungo FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PFC Cherno More Varna | target=PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | candidate=PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Wasl | target=AL Wasl vs AL Jazira | candidate=AL Wasl vs AL Jazira | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71325988
- multi_odds_match: No multi-odds payload matched event 68746468
- multi_odds_match: No multi-odds payload matched event 69880306
- multi_odds_match: No multi-odds payload matched event 70316166
- multi_odds_match: No multi-odds payload matched event 71338854
- multi_odds_match: No multi-odds payload matched event 71338856
- multi_odds_match: No multi-odds payload matched event 70906728
- multi_odds_match: No multi-odds payload matched event 71228890
- multi_odds_match: No multi-odds payload matched event 68492514
- multi_odds_match: No multi-odds payload matched event 71372082