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
Events discovery rows: 350
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 67807412, 68686544, 71590346, 69195338, 68680082, 67878260, 67690900, 67692628, 71715888, 68162412, 67808488, 69195340, 71717824, 67904764, 71715896, 71715900, 67692630, 71715894, 67904970, 71717832, 68916330, 68161352, 71715898, 68050054, 71715892, 68161354, 69195342, 71127922, 67904458, 67904172, 67904966, 67904462, 69767376, 67904460, 67692638, 69767378, 68048892, 67692636, 68046552, 68046554, 69767382, 67693566, 67904176, 68916332, 61911564, 67904464, 67149490, 68046556, 71499312, 71730320, 67920380, 61688424, 71609786, 61688414, 61688420, 71609792, 70822488, 71685814, 61688418, 71580852, 68663512, 68663500, 68663502, 67915604, 68663508, 68663510, 68320206, 67845770, 68377610, 67915876, 68663506, 71234494, 66918152, 68995200, 68377724, 71557240, 68377726, 67920388, 68995202, 67126588
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 349
Event selection diagnostic rows: 24840
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 53
Latest x-ratelimit-reset: 2026-05-31T03:15:31Z
Latest retry-after: None

- 2026-05-31 03:00 | Broadmeadow Magic FC vs Lambton Jaffas FC | odds_api_io_Bet365_ML | 1.7/4.2/3.5
- 2026-05-31 04:00 | South Hobart FC 2 vs Hobart United FC | odds_api_io_Bet365_ML | 1.09/10.0/17.0
- 2026-05-31 04:00 | Veertien Mie FC vs FC Fujizakura | odds_api_io_Bet365_ML | 4.5/3.4/1.727
- 2026-05-31 04:30 | Canberra Olympic vs West Canberra Wanderers FC | odds_api_io_Bet365_ML | 1.04/15.0/34.0
- 2026-05-31 04:30 | Clarence Zebras FC vs South East United FC | odds_api_io_Bet365_ML | 1.333/5.25/6.5
- 2026-05-31 04:30 | Magic United Tfa vs Lions FC | odds_api_io_Bet365_ML | 11.0/6.25/1.166
- 2026-05-31 04:30 | Sydney United 58 FC vs Sutherland Sharks | odds_api_io_Bet365_ML | 1.571/4.1/4.2
- 2026-05-31 04:40 | Bulls FC Academy vs Western City Rangers FC | odds_api_io_Bet365_ML | 1.142/7.0/12.0
- 2026-05-31 05:00 | Blaublitz Akita vs Hokkaido Consadole Sapporo | odds_api_io_Bet365_ML | 2.2/3.1/2.9
- 2026-05-31 05:00 | Boroondara Eagles vs Essendon Royals SC | odds_api_io_Bet365_ML | 3.6/3.9/1.75

## Event selection diagnostics

- src=events_bookmaker_filtered | query=ST Albans Saints Dinamo SC | target=ST Albans Saints Dinamo SC vs Preston Lions FC | candidate=ST Albans Saints Dinamo SC vs Preston Lions FC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Hoang Anh Gia Lai | target=Hoang Anh Gia Lai vs Hanoi FC | candidate=Hoang Anh Gia Lai vs Hanoi FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Boroondara Eagles | target=Boroondara Eagles vs Essendon Royals SC | candidate=Boroondara Eagles vs Essendon Royals SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Clarence Zebras FC | target=Clarence Zebras FC vs South East United FC | candidate=Clarence Zebras FC vs South East United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Broadmeadow Magic FC | target=Broadmeadow Magic FC vs Lambton Jaffas FC | candidate=Broadmeadow Magic FC vs Lambton Jaffas FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Veertien Mie FC | target=Veertien Mie FC vs FC Fujizakura | candidate=Veertien Mie FC vs FC Fujizakura | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cong An TP Ho Chi Minh City FC | target=Cong An TP Ho Chi Minh City FC vs The Cong - Viettel FC | candidate=Cong An TP Ho Chi Minh City FC vs The Cong - Viettel FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gil Vicente FC | target=Gil Vicente FC vs Rio Ave FC | candidate=Gil Vicente FC vs Rio Ave FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Perth Azzurri | target=Perth Azzurri vs Sorrento FC | candidate=Perth Azzurri vs Sorrento FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra Croatia FC | target=Canberra Croatia FC vs Belconnen United | candidate=Canberra Croatia FC vs Belconnen United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=TSG Hoffenheim | target=TSG Hoffenheim vs 1. FC Cologne | candidate=TSG Hoffenheim vs 1. FC Cologne | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=BK Hacken | target=BK Hacken vs Hammarby IF | candidate=BK Hacken vs Hammarby IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Darwin Hearts FC | target=Darwin Hearts FC vs Palmerston Rovers | candidate=Darwin Hearts FC vs Palmerston Rovers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Shimizu S-Pulse | target=Shimizu S-Pulse vs Yokohama F Marinos | candidate=Shimizu S-Pulse vs Yokohama F Marinos | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Odds BK 2 | target=Odds BK 2 vs Akra | candidate=Odds BK 2 vs Akra | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Japan | target=Japan vs Iceland | candidate=Japan vs Iceland | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Real Oviedo Vetusta | target=Real Oviedo Vetusta vs CD Coria | candidate=Real Oviedo Vetusta vs CD Coria | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Viking FK 2 | target=Viking FK 2 vs Brodd | candidate=Viking FK 2 vs Brodd | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sydney Olympic FC | target=Sydney Olympic FC vs Western Sydney Wanderers Youth | candidate=Sydney Olympic FC vs Western Sydney Wanderers Youth | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Montedio Yamagata | target=Montedio Yamagata vs Matsumoto Yamaga FC | candidate=Montedio Yamagata vs Matsumoto Yamaga FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 67808488
- multi_odds_match: No multi-odds payload matched event 69195340
- multi_odds_match: No multi-odds payload matched event 71717824
- multi_odds_match: No multi-odds payload matched event 67904764
- multi_odds_match: No multi-odds payload matched event 71715896
- multi_odds_match: No multi-odds payload matched event 71715900
- multi_odds_match: No multi-odds payload matched event 67692630
- multi_odds_match: No multi-odds payload matched event 71715894
- multi_odds_match: No multi-odds payload matched event 67904970
- multi_odds_match: No multi-odds payload matched event 71717832