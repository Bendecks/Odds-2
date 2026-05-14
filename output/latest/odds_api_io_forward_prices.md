# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 8 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 643
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Valencia, Girona, Real Madrid
Selected event IDs: 61624656, 71354678, 71426252, 68042486, 71128218, 69880380, 70401294, 70401306, 70401302, 71475334, 71426254, 71128220, 70401290, 70401298, 70379168, 70401304, 71475330, 71450704, 71452804, 71451454, 71454736, 69460606, 67693536, 70968242, 68162372, 68160934, 68160922, 67905666, 70968246, 67905668, 62083172, 62204956, 61974264, 69165688, 67878238, 68161886, 67878230, 67878228, 71240192, 68160142, 68161694, 67807822, 67692234, 67807380, 70926670, 70090086, 70090088, 68161704, 67691594, 68160146, 67903672, 68161696, 69767360, 68663472, 68664046, 70090090, 69767598, 70969284, 70968250, 71474752, 70968262, 61974266, 68995142, 68995140, 68995144, 68995146, 68995148, 67343112, 70995260, 70995264, 68042490, 71357268, 70929720, 70926672, 71056744, 63185777, 71492822
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 647
Event selection diagnostic rows: 48522
Selected event rows: 77
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 8
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 79
Latest x-ratelimit-reset: 2026-05-14T20:01:53Z
Latest retry-after: None

- 2026-05-14 19:30 | Real Madrid vs Real Oviedo | odds_api_io_Bet365_ML | 1.25/6.25/9.5
- 2026-05-14 20:00 | Astillero FC (Ecu) vs Guayaquil City FC | odds_api_io_Bet365_ML | 4.333/3.75/1.615
- 2026-05-14 20:00 | Club 3 De Noviembre vs Deportivo Capiata | odds_api_io_Bet365_ML | 2.45/3.0/2.7
- 2026-05-14 20:00 | Libertad Asuncion vs CS 2 de Mayo | odds_api_io_Bet365_ML | 1.8/3.3/3.8
- 2026-05-14 20:30 | Red Bull Bragantino SP vs SC Corinthians SP | odds_api_io_Bet365_ML | 5.75/3.8/1.48
- 2026-05-14 20:30 | Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | odds_api_io_Bet365_ML | 2.05/3.0/3.6
- 2026-05-14 21:00 | Chapecoense SC vs Botafogo FR RJ | odds_api_io_Bet365_ML | 3.2/3.3/2.25
- 2026-05-14 22:00 | AC Goianiense GO vs CA Paranaense PR | odds_api_io_Bet365_ML | 3.25/3.0/2.35
- 2026-05-14 22:00 | AD Confianca SE vs Gremio FB Porto Alegrense RS | odds_api_io_Bet365_ML | 4.1/3.4/1.9
- 2026-05-14 22:00 | Tigres FC vs Envigado FC | odds_api_io_Bet365_ML | 4.2/3.2/1.95

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Shanghai Port FC | target=Shanghai Port FC vs Zhejiang FC | candidate=Shanghai Port FC vs Zhejiang FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bentleigh Greens SC | target=Bentleigh Greens SC vs Heidelberg United FC | candidate=Bentleigh Greens SC vs Heidelberg United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Club Fernando de La Mora | target=Club Fernando de La Mora vs Independiente Campo Grande | candidate=Club Fernando de La Mora vs Independiente Campo Grande | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Ittihad Ahli of Aleppo | target=Al Ittihad Ahli of Aleppo vs Al-Shorta SC | candidate=Al Ittihad Ahli of Aleppo vs Al-Shorta SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Libertad Asuncion | target=Libertad Asuncion vs Sportivo 2 de Mayo | candidate=Libertad Asuncion vs Sportivo 2 de Mayo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Balcatta FC | target=Balcatta FC vs Fremantle City FC | candidate=Balcatta FC vs Fremantle City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dalian Kewei | target=Dalian Kewei vs Nantong Zhiyun | candidate=Dalian Kewei vs Nantong Zhiyun | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Shenzhen 2028 FC | target=Shenzhen 2028 FC vs Shaanxi Union FC | candidate=Shenzhen 2028 FC vs Shaanxi Union FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kingston City FC | target=Kingston City FC vs Eastern Lions SC | candidate=Kingston City FC vs Eastern Lions SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Vinotinto FC Ecuador | target=Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | candidate=Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dandenong City SC | target=Dandenong City SC vs Oakleigh Cannons | candidate=Dandenong City SC vs Oakleigh Cannons | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CR Brasil AL | target=CR Brasil AL vs Fortaleza EC CE | candidate=CR Brasil AL vs Fortaleza EC CE | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Municipal Limeno | target=Municipal Limeno vs CD FAS Santa Ana | candidate=Municipal Limeno vs CD FAS Santa Ana | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cong An TP Ho Chi Minh City FC | target=Cong An TP Ho Chi Minh City FC vs SHB Da Nang | candidate=Cong An TP Ho Chi Minh City FC vs SHB Da Nang | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dalian Yingbo FC | target=Dalian Yingbo FC vs Qingdao West Coast FC | candidate=Dalian Yingbo FC vs Qingdao West Coast FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Melbourne Knights FC | target=Melbourne Knights FC vs Eltham Redbacks FC | candidate=Melbourne Knights vs Eltham Redbacks FC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Hangzhou Linping Wuyue | target=Hangzhou Linping Wuyue vs Foshan Nanshi FC | candidate=Hangzhou Linping Wuyue vs Foshan Nanshi FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SC Corinthians SP | target=SC Corinthians SP vs Barra FC SC | candidate=SC Corinthians SP vs Barra FC SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Essendon Royals SC | target=Essendon Royals SC vs Moreland City FC | candidate=Essendon Royals SC vs Moreland City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Penang FA | target=Penang FA vs Brunei DPMM FC | candidate=Penang FA vs Brunei DPMM FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Valencia'; best=0.5979
- event_selection: No event above confidence 0.72 for query 'Girona'; best=0.4911
- event_selection: No event above confidence 0.72 for query 'Real Madrid'; best=0.4388
- multi_odds_match: No multi-odds payload matched event 71426254
- multi_odds_match: No multi-odds payload matched event 71128220
- multi_odds_match: No multi-odds payload matched event 70401290
- multi_odds_match: No multi-odds payload matched event 70401298
- multi_odds_match: No multi-odds payload matched event 70379168
- multi_odds_match: No multi-odds payload matched event 70401304
- multi_odds_match: No multi-odds payload matched event 71475330