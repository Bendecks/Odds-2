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
Events discovery rows: 190
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Bahcesehir Koleji, EC Pinheiros SP
Selected event IDs: 71495872, 71636230, 68492546, 71575786, 71522064, 68492548, 71685808, 71401842, 67920372, 61737354, 71536140, 69924118, 67017078, 67921098, 67017080, 67017076, 67919648, 67017084, 67920624, 67017086, 68158860, 67919934, 71298362, 61688398, 71666556, 61688404, 67126118, 67921102, 61688408, 71566876, 71205860, 68158838, 68158864, 68158862, 68751814, 71576560, 68158834, 68158848, 71668818, 70531730, 70531740, 70531732, 70531744, 71443814, 71284938, 71564468, 70898358, 71288930, 68194746, 68194722, 71335398, 70531728, 70076026, 70075252, 70531738, 70531742, 70075250, 70076024, 70075178, 70075176, 70531726, 69091126, 68989096, 68989098, 69091130, 69091132, 68989102, 70075204, 70075682, 70075658, 70075660, 70075202, 70075684, 69910676, 69910678, 71267616, 69910680, 69910944, 71553982, 71652968
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 193
Event selection diagnostic rows: 12133
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 35
Latest x-ratelimit-reset: 2026-05-26T15:39:17Z
Latest retry-after: None

- 2026-05-26 15:00 | FC Alashkert Yerevan vs FC Shirak Gyumri | odds_api_io_Bet365_ML | 1.27/5.0/9.0
- 2026-05-26 15:00 | Club Yanapuma vs Club Alianza Lima | odds_api_io_Bet365_ML | 11.0/8.5/1.166
- 2026-05-26 15:00 | FS Jelgava vs FK Liepaja | odds_api_io_Bet365_ML | 3.8/3.4/1.8
- 2026-05-26 15:00 | IFK Mariehamn vs FC Lahti | odds_api_io_Bet365_ML | 4.2/3.25/1.727
- 2026-05-26 15:30 | JaPS vs Kuopion Palloseura | odds_api_io_Bet365_ML | 9.5/5.5/1.25
- 2026-05-26 16:00 | BFC Daugavpils vs FK Auda Riga | odds_api_io_Bet365_ML | 3.3/3.6/1.85
- 2026-05-26 16:00 | FC Banik Ostrava vs FC Silon Taborsko | odds_api_io_Bet365_ML | 1.285/5.0/9.0
- 2026-05-26 16:00 | BK Olympic vs Ariana FC | odds_api_io_Bet365_ML | 2.4/3.6/2.4
- 2026-05-26 16:00 | Brodd vs Odds BK 2 | odds_api_io_Bet365_ML | 1.6/4.5/4.0
- 2026-05-26 16:00 | FK Sloga Doboj vs FK Rudar Prijedor | odds_api_io_Bet365_ML | 1.48/3.6/6.25

## Event selection diagnostics

- src=events_bookmaker_filtered | query=BK Olympic | target=BK Olympic vs Ariana FC | candidate=BK Olympic vs Ariana FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=New England Mutiny | target=New England Mutiny vs Vermont Green | candidate=New England Mutiny vs Vermont Green | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fluminense FC RJ | target=Fluminense FC RJ vs Cruzeiro EC MG | candidate=Fluminense FC RJ vs Cruzeiro EC MG | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Armenio | target=CD Armenio vs Argentino de Merlo | candidate=CD Armenio vs Argentino de Merlo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FS Jelgava | target=FS Jelgava vs FK Liepaja | candidate=FS Jelgava vs FK Liepaja | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Granada CF | target=Granada CF vs Madrid CFF | candidate=Granada CF vs Madrid CFF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CS Dock Sud | target=CS Dock Sud vs Real Pilar FC | candidate=CS Dock Sud vs Real Pilar FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Palestino | target=CD Palestino vs Deportivo Riestra AFBC | candidate=CD Palestino vs Deportivo Riestra AFBC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Edgewater Castle | target=Edgewater Castle vs River Light FC | candidate=Edgewater Castle vs River Light FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gil Vicente FC | target=Gil Vicente FC vs Santa Clara | candidate=Gil Vicente FC vs Santa Clara | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Millonarios FC | target=Millonarios FC vs CD O´Higgins | candidate=Millonarios FC vs CD O´Higgins | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Nigeria | target=Nigeria vs Zimbabwe | candidate=Nigeria vs Zimbabwe | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Stallion Laguna FC | target=Stallion Laguna FC vs Dynamic Herb Cebu FC | candidate=Stallion Laguna FC vs Dynamic Herb Cebu FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Nona FC | target=Nona FC vs Sporting Jax II | candidate=Nona FC vs Sporting Jax II | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Argentinos Juniors Reserve | target=Argentinos Juniors Reserve vs CA Banfield | candidate=Argentinos Juniors Reserve vs CA Banfield | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Racing Club Avellaneda | target=Racing Club Avellaneda vs CA Tigre Reserve | candidate=Racing Club Avellaneda vs CA Tigre Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Club Comunicaciones | target=Club Comunicaciones vs CD UAI Urquiza | candidate=Club Comunicaciones vs CD UAI Urquiza | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gremio FB Porto Alegrense RS | target=Gremio FB Porto Alegrense RS vs Montevideo City Torque | candidate=Gremio FB Porto Alegrense RS vs Montevideo City Torque | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dalian Yingbo B | target=Dalian Yingbo B vs Shandong Taishan B | candidate=Dalian Yingbo B vs Shandong Taishan B | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Brown de Adrogue | target=CA Brown de Adrogue vs CA Talleres de Remedios | candidate=CA Brown de Adrogue vs CA Talleres de Remedios | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71536140
- multi_odds_match: No multi-odds payload matched event 69924118
- multi_odds_match: No multi-odds payload matched event 67017078
- multi_odds_match: No multi-odds payload matched event 67921098
- multi_odds_match: No multi-odds payload matched event 67017080
- multi_odds_match: No multi-odds payload matched event 67017076
- multi_odds_match: No multi-odds payload matched event 67919648
- multi_odds_match: No multi-odds payload matched event 67017084
- multi_odds_match: No multi-odds payload matched event 67920624
- multi_odds_match: No multi-odds payload matched event 67017086