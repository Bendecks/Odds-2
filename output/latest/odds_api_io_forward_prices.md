# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 7 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 1080
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 71218648, 69090834, 68159812, 69195806, 69462618, 68050292, 69463270, 69460604, 68161316, 68161318, 68160928, 69460608, 69463268, 68050020, 69460602, 67693058, 69462620, 68050296, 68050294, 68050024, 69462622, 67807386, 68728636, 67266628, 68160148, 67266624, 67807382, 67266620, 67266626, 69195810, 67905672, 67648300, 68162376, 68161700, 67807384, 68161702, 68916292, 69768174, 69768168, 68161320, 68916294, 68728642, 68162378, 71415288, 67648142, 69768170, 68162380, 69768176, 68160930, 67645554, 68050028, 69194910, 69115732, 68916296, 67648460, 67647982, 67647980, 69115734, 69768172, 68050300, 67647984, 69115740, 68916298, 68051602, 68051606, 68159822, 67648144, 68048864, 68048860, 68051604, 68048858, 69195812, 68048862, 67905676, 68161324, 67807824, 69460610, 67905196, 67905194, 67905674
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 1069
Event selection diagnostic rows: 83240
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 7
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 41
Latest x-ratelimit-reset: 2026-05-16T02:56:18Z
Latest retry-after: None

- 2026-05-16 02:15 | CD Marathon San Pedro Sula vs CD Olimpia Tegucigalpa | odds_api_io_Bet365_ML | 2.5/3.0/2.625
- 2026-05-16 02:30 | Ballard FC vs FC Olympia | odds_api_io_Bet365_ML | 1.142/7.5/12.0
- 2026-05-16 02:30 | Essendon Royals SC U20 vs South Melbourne FC U20 | odds_api_io_Bet365_ML | 3.6/3.75/1.75
- 2026-05-16 02:30 | O'Connor Knights SC vs Canberra Croatia FC | odds_api_io_Bet365_ML | 2.3/5.25/2.1
- 2026-05-16 02:30 | Waterside Karori vs Western Suburbs FC | odds_api_io_Bet365_ML | 17.0/8.0/1.125
- 2026-05-16 02:45 | Adelaide Atletico Victory Reserves vs Eastern United Reserve | odds_api_io_Bet365_ML | 2.1/5.0/2.3
- 2026-05-16 02:45 | Nomads United AFC vs Ferrymead Bays | odds_api_io_Bet365_ML | 2.45/4.0/2.2
- 2026-05-16 03:00 | Bay Olympic vs Auckland United FC | odds_api_io_Bet365_ML | 6.5/5.0/1.333
- 2026-05-16 03:00 | Bentleigh Greens SC vs Heidelberg United FC | odds_api_io_Bet365_ML | 2.05/4.75/2.375
- 2026-05-16 03:00 | Dandenong Thunder FC vs ST Albans Saints Dinamo SC | odds_api_io_Bet365_ML | 2.375/4.2/2.15

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Wellington Phoenix FC Reserve | target=Wellington Phoenix FC Reserve vs Island Bay United | candidate=Wellington Phoenix FC Reserve vs Island Bay United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Wellington Olympic | target=Wellington Olympic vs Petone FC | candidate=Wellington Olympic vs Petone FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Keilor Park SC | target=Keilor Park SC vs Boroondara Eagles | candidate=Keilor Park SC vs Boroondara Eagles | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Chuncheon FC | target=Chuncheon FC vs Jeonbuk FC II | candidate=Chuncheon FC vs Jeonbuk FC II | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Marathon San Pedro Sula | target=CD Marathon San Pedro Sula vs CD Olimpia Tegucigalpa | candidate=CD Marathon San Pedro Sula vs CD Olimpia Tegucigalpa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Charlestown Azzurri FC | target=Charlestown Azzurri FC vs Adamstown Rosebud JFC | candidate=Charlestown Azzurri FC vs Adamstown Rosebud JFC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Perth Redstar FC | target=Perth Redstar FC vs Armadale SC | candidate=Perth Redstar FC vs Armadale SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Melbourne Srbija | target=FC Melbourne Srbija vs Brunswick City SC | candidate=FC Melbourne Srbija vs Brunswick City SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Curtin University SC Reserves | target=Curtin University SC Reserves vs Murdoch University Melville FC Reserves | candidate=Curtin University SC Reserves vs Murdoch University Melville FC Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Manningham United Blues FC | target=Manningham United Blues FC vs Brunswick Juventus FC | candidate=Manningham United Blues FC vs Brunswick Juventus FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fremantle City FC | target=Fremantle City FC vs Olympic Kingsway SC | candidate=Fremantle City vs Olympic Kingsway SC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Belconnen United FC | target=Belconnen United FC vs Monaro Panthers FC | candidate=Belconnen United FC vs Monaro Panthers FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=The Cove FC Reserves | target=The Cove FC Reserves vs Adelaide Croatia Raiders SC Reserve | candidate=The Cove FC Reserves vs Adelaide Croatia Raiders SC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sturt Lions Reserve | target=Sturt Lions Reserve vs Croydon Kings FC Reserve | candidate=Sturt Lions Reserve vs Croydon Kings FC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Melbourne Srbija | target=FC Melbourne Srbija vs Brunswick City SC | candidate=FC Melbourne Srbija vs Brunswick City SC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Tokyo Verdy Beleza | target=Tokyo Verdy Beleza vs Albirex Niigata | candidate=Tokyo Verdy Beleza vs Albirex Niigata | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Avondale FC | target=Avondale FC vs Spring Hills FC | candidate=Avondale FC vs Spring Hills FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Rochedale Rovers | target=Rochedale Rovers vs Magic United TFA | candidate=Rochedale Rovers vs Magic United TFA | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Jubilo Iwata | target=Jubilo Iwata vs Fujieda MYFC | candidate=Jubilo Iwata vs Fujieda MYFC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sturt Lions | target=Sturt Lions vs Croydon FC | candidate=Sturt Lions vs Croydon FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 68160928
- multi_odds_match: No multi-odds payload matched event 69460608
- multi_odds_match: No multi-odds payload matched event 69463268
- multi_odds_match: No multi-odds payload matched event 68050020
- multi_odds_match: No multi-odds payload matched event 69460602
- multi_odds_match: No multi-odds payload matched event 67693058
- multi_odds_match: No multi-odds payload matched event 69462620
- multi_odds_match: No multi-odds payload matched event 68050296
- multi_odds_match: No multi-odds payload matched event 68050294
- multi_odds_match: No multi-odds payload matched event 68050024