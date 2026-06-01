# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 4 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 89
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Magic United TFA, Central Espanol Reserve
Selected event IDs: 68160960, 71561886, 71715902, 68160588, 68160590, 71838078, 71772916, 71732886, 71561888, 70771302, 71772918, 69688536, 71580506, 71685296, 71685292, 71399404, 68774178, 71718866, 71773918, 71378120, 71399478, 67919956, 70771304, 71544086, 69829658, 68311638, 71580516, 71685300, 71685298, 68310934, 71741536, 71604168, 71301328, 71633100, 71737152, 71772922, 71718926, 67921118, 71772920, 68971786, 71718930, 67119354, 67125798, 67125796, 68269904, 70321100, 71732910, 71666558, 70688018, 70698922, 68306858, 71842028, 71585574, 71378240, 68822926, 68687682, 69255072, 71737154, 68097928, 71229566, 68097932, 70321616, 70323324, 70379216, 68687674, 71804372, 68880438, 69091342, 71792742, 71792738, 71804388, 68093892, 71590092, 68311640, 68310936, 69829662, 71766878, 71468722, 67905222, 71772926
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 93
Event selection diagnostic rows: 3980
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 61
Latest x-ratelimit-reset: 2026-06-01T03:37:04Z
Latest retry-after: None

- 2026-06-01 08:15 | FC Bulleen Lions vs Port Melbourne Sharks SC | odds_api_io_Bet365_ML | 1.125/8.5/12.0
- 2026-06-01 09:00 | Vietnam vs Timor-Leste | odds_api_io_Bet365_ML | 1.04/17.0/29.0
- 2026-06-01 10:00 | Vanraure Hachinohe FC vs Fukushima United FC | odds_api_io_Bet365_ML | 1.666/3.3/4.75
- 2026-06-01 10:30 | FC Bulleen Lions vs Port Melbourne Sharks | odds_api_io_Bet365_ML | 1.333/5.0/6.5
- 2026-06-01 10:30 | Melbourne Victory vs Melbourne Knights | odds_api_io_Bet365_ML | 2.75/4.0/2.0
- 2026-06-01 11:00 | Pakistan vs Bangladesh | odds_api_io_Bet365_ML | 1.9/3.1/3.8
- 2026-06-01 12:30 | Juventud de Las Piedras vs Montevideo Wanderers | odds_api_io_Bet365_ML | 2.375/3.4/2.625
- 2026-06-01 13:00 | Bulawayo Chiefs FC vs Manica Diamonds FC | odds_api_io_Bet365_ML | 2.15/2.7/3.6
- 2026-06-01 13:00 | Indonesia vs Myanmar | odds_api_io_Bet365_ML | 1.166/7.5/12.0
- 2026-06-01 13:00 | Japan vs Ivory Coast | odds_api_io_Bet365_ML | 3.75/3.7/1.727

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Athletic Club MG | target=Athletic Club MG vs Atletico Mineiro MG | candidate=Athletic Club MG vs Atletico Mineiro MG | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Boston River | target=CA Boston River vs Liverpool Montevideo | candidate=CA Boston River vs Liverpool Montevideo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Turkiye | target=Turkiye vs North Macedonia | candidate=Turkiye vs North Macedonia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Skovde AIK | target=Skovde AIK vs Jonkopings Sodra IF | candidate=Skovde AIK vs Jonkopings Sodra IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SC Recife PE | target=SC Recife PE vs Paysandu SC PA | candidate=SC Recife PE vs Paysandu SC PA | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Racing Club Montevideo | target=Racing Club Montevideo vs La Luz FC Reserves | candidate=Racing Club Montevideo vs La Luz FC Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Wadi Degla SC | target=Wadi Degla SC vs Enppi Club | candidate=Wadi Degla SC vs Enppi Club | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Najaf | target=AL Najaf vs Al Zawraa | candidate=AL Najaf vs Al Zawraa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Wales | target=Wales vs Ghana | candidate=Wales vs Ghana | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Talaba | target=AL Talaba vs AL Karkh | candidate=AL Talaba vs AL Karkh | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lyn 1896 FK II | target=Lyn 1896 FK II vs FK Gjoevik-Lyn | candidate=Lyn 1896 FK II vs FK Gjoevik-Lyn | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=EC Sao Jose RS | target=EC Sao Jose RS vs Ypiranga RS | candidate=EC Sao Jose RS vs Ypiranga RS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Arlanda | target=FC Arlanda vs Gefle IF | candidate=FC Arlanda vs Gefle IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Jeunesse Canach | target=FC Jeunesse Canach vs Residence Walferdange | candidate=FC Jeunesse Canach vs Residence Walferdange | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA River Plate (URU) | target=CA River Plate (URU) vs Colon FC Reserve | candidate=CA River Plate (URU) vs Colon FC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SC FC Voluntari | target=SC FC Voluntari vs AFC Hermannstadt | candidate=SC FC Voluntari vs AFC Hermannstadt | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ser Caxias RS | target=Ser Caxias RS vs EC Juventude RS | candidate=Ser Caxias RS vs EC Juventude RS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Wurzburger Kickers | target=FC Wurzburger Kickers vs 1. FC Lokomotive Leipzig | candidate=FC Wurzburger Kickers vs 1. FC Lokomotive Leipzig | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Argentino de Quilmes | target=Argentino de Quilmes vs CA Ituzaingo | candidate=Argentino de Quilmes vs CA Ituzaingo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Vard Haugesund | target=Vard Haugesund vs Aasane Fotball 2 | candidate=Vard Haugesund vs Aasane Fotball 2 | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71772918
- multi_odds_match: No multi-odds payload matched event 69688536
- multi_odds_match: No multi-odds payload matched event 71580506
- multi_odds_match: No multi-odds payload matched event 71685296
- multi_odds_match: No multi-odds payload matched event 71685292
- multi_odds_match: No multi-odds payload matched event 71399404
- multi_odds_match: No multi-odds payload matched event 68774178
- multi_odds_match: No multi-odds payload matched event 71718866
- multi_odds_match: No multi-odds payload matched event 71773918
- multi_odds_match: No multi-odds payload matched event 71378120