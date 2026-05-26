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
Events discovery rows: 124
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: EC Pinheiros SP
Selected event IDs: 69910672, 69910674, 69910938, 71375928, 69910940, 69910942, 71577454, 71577456, 71719708, 71495872, 71636230, 68492546, 71575786, 71522064, 68492548, 71685808, 71401842, 67920372, 71536140, 69924118, 67017078, 67921098, 67017080, 67017076, 67919648, 67017084, 67920624, 67017086, 68158860, 67919934, 71298362, 61688398, 71666556, 61688404, 67126118, 67921102, 61688408, 71566876, 71205860, 68158838, 68158864, 68158862, 68751814, 71576560, 68158834, 68158848, 70531730, 70531740, 70531732, 70531744, 71443814, 71284938, 71564468, 70898358, 71288930, 68194746, 68194722, 71335398, 70531728, 70076026, 70075252, 70531738, 70531742, 70075250, 70076024, 70075178, 70075176, 70531726, 69091126, 68989096, 68989098, 69091130, 69091132, 68989102, 70075204, 70075682, 70075658, 70075660, 70075202, 71652968
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 125
Event selection diagnostic rows: 6767
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 62
Latest x-ratelimit-reset: 2026-05-26T03:05:59Z
Latest retry-after: None

- 2026-05-26 07:30 | Taian Tiankuang vs Dalian Kewei | odds_api_io_Bet365_ML | 2.05/2.8/3.5
- 2026-05-26 08:00 | Shanghai Port B vs Lanzhou Longyuan Athletic | odds_api_io_Bet365_ML | 1.666/3.4/4.5
- 2026-05-26 08:00 | Shenzhen 2028 FC vs Wenzhou Professional FC | odds_api_io_Bet365_ML | 2.15/3.0/3.25
- 2026-05-26 09:30 | Logan Lightning vs Palm Beach SC | odds_api_io_Bet365_ML | 2.8/4.0/2.0
- 2026-05-26 11:30 | Hangzhou Linping Wuyue vs Hubei Istar | odds_api_io_Bet365_ML | 3.0/3.0/2.2
- 2026-05-26 11:35 | Chengdu Rongcheng B vs Guizhou Guiyang Athletic | odds_api_io_Bet365_ML | 3.7/3.2/1.909
- 2026-05-26 12:00 | Goztepe vs Arnavutkoy Belediyesi Futbol SK | odds_api_io_Bet365_ML | 1.5/4.5/4.5
- 2026-05-26 12:00 | Trabzonspor vs Manisa Futbol Kulubu | odds_api_io_Bet365_ML | 1.45/4.5/5.0
- 2026-05-26 13:00 | Cape Town City FC vs Milford FC | odds_api_io_Bet365_ML | 1.909/3.1/3.75
- 2026-05-26 15:00 | FC Alashkert Yerevan vs FC Shirak Gyumri | odds_api_io_Bet365_ML | 1.25/5.0/9.5

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Lyn 1896 FK II | target=Lyn 1896 FK II vs Drobak-Frogn | candidate=Lyn 1896 FK II vs Drobak-Frogn | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Estudiantes de La Plata | target=Estudiantes de La Plata vs Independiente Medellin | candidate=Estudiantes de La Plata vs Independiente Medellin | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kalamazoo FC | target=Kalamazoo FC vs Midwest United FC | candidate=Kalamazoo FC vs Midwest United FC | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=EC Pinheiros SP | target=EC Pinheiros SP vs SC Corinthians Paulista | candidate=EC Pinheiros SP vs SC Corinthians Paulista | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Taian Tiankuang | target=Taian Tiankuang vs Dalian Kewei | candidate=Taian Tiankuang vs Dalian Kewei | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hangzhou Linping Wuyue | target=Hangzhou Linping Wuyue vs Hubei Istar | candidate=Hangzhou Linping Wuyue vs Hubei Istar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Deportivo Merlo | target=Deportivo Merlo vs CSD Liniers | candidate=Deportivo Merlo vs CSD Liniers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Delaware FC | target=Delaware FC vs Philadelphia Lone Star Usl2 | candidate=Delaware FC vs Philadelphia Lone Star Usl2 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gremio FB Porto Alegrense RS | target=Gremio FB Porto Alegrense RS vs Montevideo City Torque | candidate=Gremio FB Porto Alegrense RS vs Montevideo City Torque | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Defensa Y Justicia Reserve | target=Defensa Y Justicia Reserve vs Independiente Reserve | candidate=Defensa Y Justicia Reserve vs Independiente Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Palestino | target=CD Palestino vs Deportivo Riestra AFBC | candidate=CD Palestino vs Deportivo Riestra AFBC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Nona FC | target=Nona FC vs Sporting Jax II | candidate=Nona FC vs Sporting Jax II | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gil Vicente FC | target=Gil Vicente FC vs Santa Clara | candidate=Gil Vicente FC vs Santa Clara | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=New England Mutiny | target=New England Mutiny vs Vermont Green | candidate=New England Mutiny vs Vermont Green | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Club Comunicaciones | target=Club Comunicaciones vs CD UAI Urquiza | candidate=Club Comunicaciones vs CD UAI Urquiza | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Honka | target=FC Honka vs VJS | candidate=FC Honka vs VJS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fluminense FC RJ | target=Fluminense FC RJ vs Cruzeiro EC MG | candidate=Fluminense FC RJ vs Cruzeiro EC MG | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Estudiantes de Rio Cuarto Reserve | target=Estudiantes de Rio Cuarto Reserve vs Boca Juniors | candidate=Estudiantes de Rio Cuarto Reserve vs Boca Juniors | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Chengdu Rongcheng B | target=Chengdu Rongcheng B vs Guizhou Guiyang Athletic | candidate=Chengdu Rongcheng B vs Guizhou Guiyang Athletic | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Club Yanapuma | target=Club Yanapuma vs Club Alianza Lima | candidate=Club Yanapuma vs Club Alianza Lima | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71636230
- multi_odds_match: No multi-odds payload matched event 68492546
- multi_odds_match: No multi-odds payload matched event 71575786
- multi_odds_match: No multi-odds payload matched event 71522064
- multi_odds_match: No multi-odds payload matched event 68492548
- multi_odds_match: No multi-odds payload matched event 71685808
- multi_odds_match: No multi-odds payload matched event 71401842
- multi_odds_match: No multi-odds payload matched event 67920372
- multi_odds_match: No multi-odds payload matched event 71536140
- multi_odds_match: No multi-odds payload matched event 69924118