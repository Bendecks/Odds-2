# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 4 / 8
Max discovery calls: 7
Events bookmaker: Bet365
Events discovery rows: 145
Events max pages: 4
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 30
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: FC Epitsentr Kamianets-Podilskyi
Selected event IDs: 71378880, 71338142, 70478164, 71336688, 69880304, 71325988, 68746468, 69880306, 70316166, 71338854, 71338856, 70906728, 71228890, 68492514, 71372082, 61651662, 71231390, 61651650, 62036882, 71085582, 71338858, 71085578, 71085580, 70232094, 71328286, 70232096, 71421816, 68492516, 71216798, 61651656
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 146
Event selection diagnostic rows: 3945
Selected event rows: 30
Priced event rows: 10
Price rows: 10
Errors/status rows: 20

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 88
Latest x-ratelimit-reset: 2026-05-12T13:33:31Z
Latest retry-after: None

- 2026-05-12 13:00 | Deportivo Maldonado Reserve vs Racing Club Montevideo | odds_api_io_Bet365_ML | 2.4/3.3/2.625
- 2026-05-12 13:00 | Namdhari FC vs Gokulam Kerala FC | odds_api_io_Bet365_ML | 3.0/3.5/2.05
- 2026-05-12 13:15 | TRA United vs Jkt Tanzania | odds_api_io_Bet365_ML | 2.15/2.9/3.3
- 2026-05-12 13:50 | Sur SC vs Al-Khaboora | odds_api_io_Bet365_ML | 1.85/2.9/4.333
- 2026-05-12 14:00 | El Gouna FC vs Kahrabaa Ismailia | odds_api_io_Bet365_ML | 2.55/2.6/2.9
- 2026-05-12 14:00 | FC Inter Turku vs JS Hercules | odds_api_io_Bet365_ML | 1.012/23.0/67.0
- 2026-05-12 14:00 | Mohun Bagan Super Giant vs Inter Kashi FC | odds_api_io_Bet365_ML | 1.166/6.25/13.0
- 2026-05-12 14:00 | Pharco FC vs Modern Sport FC | odds_api_io_Bet365_ML | 3.0/2.6/2.55
- 2026-05-12 14:00 | URA FC vs Calvary | odds_api_io_Bet365_ML | 1.333/4.5/7.5
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr | odds_api_io_Bet365_ML | 2.1/3.7/2.8

## Event selection diagnostics

- src=events_bookmaker_filtered | query=FC Metalist 1925 Kharkiv | target=FC Metalist 1925 Kharkiv vs Karpaty Lviv | candidate=FC Metalist 1925 Kharkiv vs Karpaty Lviv | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Riga FC | target=Riga FC vs FK Auda Riga | candidate=Riga FC vs FK Auda Riga | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sarpsborg 08 FF | target=Sarpsborg 08 FF vs Hoenefoss BK | candidate=Sarpsborg 08 FF vs Hoenefoss BK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Liepaja | target=FK Liepaja vs Ogre United | candidate=FK Liepaja vs Ogre United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Rayon Sports FC | target=Rayon Sports FC vs Gorilla FC | candidate=Rayon Sports FC vs Gorilla FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=URA FC | target=URA FC vs Calvary | candidate=URA FC vs Calvary | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Veres Rivne | target=Veres Rivne vs FC Kryvbas Kriviy Rih | candidate=Veres Rivne vs FC Kryvbas Kriviy Rih | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=MFK Chrudim | target=MFK Chrudim vs FK Pribram | candidate=MFK Chrudim vs FK Pribram | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sur SC | target=Sur SC vs Al-Khaboora | candidate=Sur SC vs Al-Khaboora | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=El Gouna FC | target=El Gouna FC vs Kahrabaa Ismailia | candidate=El Gouna FC vs Kahrabaa Ismailia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=JS Omrane | target=JS Omrane vs Avenir S Marsa | candidate=JS Omrane vs Avenir S Marsa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Zaglebie Lubin II | target=Zaglebie Lubin II vs Mkp Carina Gubin | candidate=Zaglebie Lubin II vs Mkp Carina Gubin | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=1. FC Slovacko Uherske Hradiste | target=1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | candidate=1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Wasl | target=AL Wasl vs AL Jazira | candidate=AL Wasl vs AL Jazira | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=FC Epitsentr Kamianets-Podilskyi | target=FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | candidate=FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Elva | target=FC Elva vs Paide Linnameeskond | candidate=FC Elva vs Paide Linnameeskond | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Pharco FC | target=Pharco FC vs Modern Sport FC | candidate=Pharco FC vs Modern Sport FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PFC Cherno More Varna | target=PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | candidate=PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Mlada Boleslav | target=FK Mlada Boleslav vs Dukla Prague | candidate=FK Mlada Boleslav vs Dukla Prague | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Ittihad Kalba | target=AL Ittihad Kalba vs AL Nasr | candidate=AL Ittihad Kalba vs AL Nasr | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71338856
- multi_odds_match: No multi-odds payload matched event 70906728
- multi_odds_match: No multi-odds payload matched event 71228890
- multi_odds_match: No multi-odds payload matched event 68492514
- multi_odds_match: No multi-odds payload matched event 71372082
- multi_odds_match: No multi-odds payload matched event 61651662
- multi_odds_match: No multi-odds payload matched event 71231390
- multi_odds_match: No multi-odds payload matched event 61651650
- multi_odds_match: No multi-odds payload matched event 62036882
- multi_odds_match: No multi-odds payload matched event 71085582