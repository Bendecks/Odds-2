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
Events discovery rows: 466
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Albacete Basket
Selected event IDs: 69091090, 67693074, 67807400, 69462626, 67808478, 68728652, 67693070, 67645082, 67878250, 68686934, 68728654, 67647994, 69195336, 68680072, 67903692, 69195334, 67647996, 68162398, 69194938, 67691622, 67648474, 67648476, 67904756, 67692622, 67807402, 67648314, 67807832, 67648160, 68160574, 67645570, 67647998, 68160180, 67648478, 67648316, 67645572, 67690880, 68664144, 67692624, 67905688, 71127914, 69767372, 71423492, 69760548, 67904162, 67904962, 67904452, 69767370, 67692620, 69455892, 68046532, 69767374, 62778621, 67645084, 62778619, 67904164, 66053732, 68995180, 71649070, 70223972, 70223974, 61911616, 71609782, 71454146, 71483868, 71483812, 68046534, 61651692, 61651682, 67790440, 61651688, 68046536, 61651690, 71649630, 68320804, 68377700, 68663494, 68377696, 63666487, 68663496, 71562550
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 467
Event selection diagnostic rows: 34127
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 55
Latest x-ratelimit-reset: 2026-05-24T03:06:40Z
Latest retry-after: None

- 2026-05-24 02:50 | Bigfoot FC vs West Seattle Junction FC | odds_api_io_Bet365_ML | 2.05/3.9/2.7
- 2026-05-24 03:00 | Blacktown City FC vs Sydney Olympic FC | odds_api_io_Bet365_ML | 1.38/4.75/5.5
- 2026-05-24 03:00 | Cooks Hill United vs Belmont Swansea United FC | odds_api_io_Bet365_ML | 2.9/4.2/1.85
- 2026-05-24 03:00 | Island Bay United vs Petone FC | odds_api_io_Bet365_ML | 2.6/3.9/2.15
- 2026-05-24 03:00 | Kahibah FC Reserve vs Adamstown Rosebud FC Reserve | odds_api_io_Bet365_ML | 2.4/4.5/2.1
- 2026-05-24 03:00 | Orca Kamogawa FC vs Viamaterasu Miyazaki | odds_api_io_Bet365_ML | 3.0/3.1/2.2
- 2026-05-24 03:00 | Wollongong Wolves FC vs St George FC | odds_api_io_Bet365_ML | 1.571/4.2/4.2
- 2026-05-24 03:55 | Fagiano Okayama vs Cerezo Osaka | odds_api_io_Bet365_ML | 2.7/3.25/2.6
- 2026-05-24 04:00 | Brisbane Roar FC vs Eastern Suburbs FC | odds_api_io_Bet365_ML | 4.333/4.333/1.533
- 2026-05-24 04:00 | Kingborough Lions United FC vs Launceston City | odds_api_io_Bet365_ML | 1.3/5.75/6.0

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Bigfoot FC | target=Bigfoot FC vs West Seattle Junction FC | candidate=Bigfoot FC vs West Seattle Junction FC | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=Albacete Basket | target=Albacete Basket vs AB Castello | candidate=Albacete Basket vs AB Castello | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Illawarra Stingrays | target=Illawarra Stingrays vs Hills United FC | candidate=Illawarra Stingrays vs Hills United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hellenic Athletic Club | target=Hellenic Athletic Club vs Port Darwin FC | candidate=Hellenic Athletic Club vs Port Darwin FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Balcatta FC | target=Balcatta FC vs Perth Redstar FC | candidate=Balcatta FC vs Perth Redstar FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Astorps FF | target=Astorps FF vs Vastra Frolunda IF | candidate=Astorps FF vs Vastra Frolunda IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Zweigen Kanazawa | target=Zweigen Kanazawa vs Kochi United SC | candidate=Zweigen Kanazawa vs Kochi United SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Covadonga | target=CD Covadonga vs CD Mosconia | candidate=CD Covadonga vs CD Mosconia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sparta Prague | target=Sparta Prague vs 1. FC Slovacko Uherske Hradiste | candidate=Sparta Prague vs 1. FC Slovacko Uherske Hradiste | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gold Coast United FC | target=Gold Coast United FC vs Eastern Suburbs FC | candidate=Gold Coast United FC vs Eastern Suburbs FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Becamex Ho Chi Minh City | target=Becamex Ho Chi Minh City vs Song Lam Nghe An | candidate=Becamex Ho Chi Minh City vs Song Lam Nghe An | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Montedio Yamagata | target=Montedio Yamagata vs Shonan Bellmare | candidate=Montedio Yamagata vs Shonan Bellmare | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Giravanz Kitakyushu | target=Giravanz Kitakyushu vs Kagoshima United | candidate=Giravanz Kitakyushu vs Kagoshima United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Wollongong Wolves FC | target=Wollongong Wolves FC vs St George Saints FC | candidate=Wollongong Wolves FC vs St George Saints FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Angby IF | target=Angby IF vs Bollstanas SK | candidate=Angby IF vs Bollstanas SK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Eastern District | target=Eastern District vs North District FC | candidate=Eastern District vs North District FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Island Bay United | target=Island Bay United vs Petone FC | candidate=Island Bay United vs Petone FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Central Stallions FC | target=Central Stallions FC vs Hunters FC | candidate=Central Stallions FC vs Hunters FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=NHK Spring Yokohama FC Seagulls | target=NHK Spring Yokohama FC Seagulls vs AS Harima Albion | candidate=NHK Spring Yokohama FC Seagulls vs AS Harima Albion | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tokyo Verdy | target=Tokyo Verdy vs Yokohama F Marinos | candidate=Tokyo Verdy vs Yokohama F Marinos | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 68728654
- multi_odds_match: No multi-odds payload matched event 67647994
- multi_odds_match: No multi-odds payload matched event 69195336
- multi_odds_match: No multi-odds payload matched event 68680072
- multi_odds_match: No multi-odds payload matched event 67903692
- multi_odds_match: No multi-odds payload matched event 69195334
- multi_odds_match: No multi-odds payload matched event 67647996
- multi_odds_match: No multi-odds payload matched event 68162398
- multi_odds_match: No multi-odds payload matched event 69194938
- multi_odds_match: No multi-odds payload matched event 67691622