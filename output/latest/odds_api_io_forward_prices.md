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
Events discovery rows: 104
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Chen, Yu Fei, Feng Y Z / Huang D P
Selected event IDs: 71685300, 71685298, 71741536, 71604168, 71301328, 71633100, 71737152, 71772922, 71718926, 67921118, 71772920, 68971786, 71718930, 67119354, 67125798, 67125796, 68269904, 70321100, 71732910, 70688018, 70698922, 68306858, 71842028, 71585574, 71378240, 68822926, 68687682, 71324788, 69255072, 71737154, 68097928, 71229566, 68097932, 70321616, 70323324, 70379216, 68687674, 71804372, 68880438, 69091342, 71792742, 71792738, 71804388, 71800584, 71127924, 71828240, 71770128, 71826656, 71561984, 70946098, 70946102, 70946168, 70946170, 70946092, 71828236, 71685306, 71685310, 71685304, 71685302, 68538278, 68093892, 71749910, 71550280, 71740898, 70771288, 61906404, 71772924, 71772926, 71772928, 70346072, 71590092, 71772930, 68311640, 68310936, 68158876, 68158896, 68158880, 68158884, 71863238, 71863280
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 106
Event selection diagnostic rows: 5235
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 62
Latest x-ratelimit-reset: 2026-06-01T18:15:22Z
Latest retry-after: None

- 2026-06-01 17:30 | AL Najaf vs Al Zawraa | odds_api_io_Bet365_ML | 5.25/4.333/1.444
- 2026-06-01 17:30 | AL Talaba vs AL Karkh | odds_api_io_Bet365_ML | 1.85/3.5/3.4
- 2026-06-01 17:30 | FC Jeunesse Canach vs Residence Walferdange | odds_api_io_Bet365_ML | 1.666/3.7/4.1
- 2026-06-01 17:30 | SC FC Voluntari vs AFC Hermannstadt | odds_api_io_Bet365_ML | 2.35/3.25/2.8
- 2026-06-01 17:30 | Turkiye vs North Macedonia | odds_api_io_Bet365_ML | 1.2/5.5/13.0
- 2026-06-01 18:00 | Athletic Club MG vs Atletico Mineiro MG | odds_api_io_Bet365_ML | 2.9/3.25/2.15
- 2026-06-01 18:00 | CA Boston River vs Liverpool Montevideo | odds_api_io_Bet365_ML | 3.0/3.1/2.3
- 2026-06-01 18:00 | CA River Plate (URU) vs Colon FC Reserve | odds_api_io_Bet365_ML | 2.55/3.0/2.625
- 2026-06-01 18:00 | EC Sao Jose RS vs Ypiranga RS | odds_api_io_Bet365_ML | 2.4/3.1/2.625
- 2026-06-01 18:00 | Lyn 1896 FK II vs FK Gjoevik-Lyn | odds_api_io_Bet365_ML | 2.45/3.9/2.375

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Colon de Santa Fe Reserve | target=Colon de Santa Fe Reserve vs CA Huracan | candidate=Colon de Santa Fe Reserve vs CA Huracan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Najaf | target=AL Najaf vs Al Zawraa | candidate=AL Najaf vs Al Zawraa | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=Feng Y Z / Huang D P | target=Feng Y Z / Huang D P vs Wong J / Cheng S Y | candidate=Feng Y Z / Huang D P vs Wong J / Cheng S Y | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=Chen, Yu Fei | target=Chen, Yu Fei vs Christophersen, Line | candidate=Chen, Yu Fei vs Christophersen, Line | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Fard Alborz | target=FC Fard Alborz vs Sanat Mes Kerman FC | candidate=FC Fard Alborz vs Sanat Mes Kerman FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Argentino de Quilmes | target=Argentino de Quilmes vs CA Ituzaingo | candidate=Argentino de Quilmes vs CA Ituzaingo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Fenix Pilar | target=CA Fenix Pilar vs Canuelas FC | candidate=CA Fenix Pilar vs Canuelas FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Havadar SC | target=Havadar SC vs Navad Urmia FC | candidate=Havadar SC vs Navad Urmia FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Podbeskidzie Bielsko-Biała | target=Podbeskidzie Bielsko-Biała vs Slask II Wroclaw | candidate=Podbeskidzie Bielsko-Biała vs Slask II Wroclaw | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Turkiye | target=Turkiye vs North Macedonia | candidate=Turkiye vs North Macedonia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=China | target=China vs Congo Dr Youth | candidate=China vs Congo Dr Youth | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Brunei Darussalam | target=Brunei Darussalam vs Timor-Leste | candidate=Brunei Darussalam vs Timor-Leste | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Malaysia | target=Malaysia vs Singapore | candidate=Malaysia vs Singapore | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Rosengaard 1917 | target=FC Rosengaard 1917 vs Angelholms FF | candidate=FC Rosengaard 1917 vs Angelholms FF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Assyriska FF | target=Assyriska FF vs Enkopings SK | candidate=Assyriska FF vs Enkopings SK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Banfield | target=CA Banfield vs CA Sarmiento de Junin | candidate=CA Banfield vs CA Sarmiento de Junin | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Guairena FC | target=Guairena FC vs Club 3 De Noviembre | candidate=Guairena FC vs Club 3 De Noviembre | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ario Eslamshahr | target=Ario Eslamshahr vs Shahrdari Nowshahr | candidate=Ario Eslamshahr vs Shahrdari Nowshahr | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Mes Shahr-e Babak | target=Mes Shahr-e Babak vs Sanat Naft Abadan FC | candidate=Mes Shahr-e Babak vs Sanat Naft Abadan FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lyn 1896 FK II | target=Lyn 1896 FK II vs FK Gjoevik-Lyn | candidate=Lyn 1896 FK II vs FK Gjoevik-Lyn | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71772920
- multi_odds_match: No multi-odds payload matched event 68971786
- multi_odds_match: No multi-odds payload matched event 71718930
- multi_odds_match: No multi-odds payload matched event 67119354
- multi_odds_match: No multi-odds payload matched event 67125798
- multi_odds_match: No multi-odds payload matched event 67125796
- multi_odds_match: No multi-odds payload matched event 68269904
- multi_odds_match: No multi-odds payload matched event 70321100
- multi_odds_match: No multi-odds payload matched event 71732910
- multi_odds_match: No multi-odds payload matched event 70688018