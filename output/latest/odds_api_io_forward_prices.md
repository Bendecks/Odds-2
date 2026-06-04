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
Events discovery rows: 392
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Japan
Selected event IDs: 71814506, 71834548, 61927926, 71749276, 71782698, 71652336, 71915906, 61541460, 71834888, 56319305, 70872820, 71632302, 71443988, 71399594, 69924130, 71859964, 71859970, 71859962, 71859966, 69924696, 71445234, 71814430, 68311644, 69923708, 68320210, 70730796, 71399598, 71814432, 68310940, 71402260, 68344686, 71509102, 71877094, 71322902, 68158872, 68158868, 71508692, 71585582, 68158882, 71917810, 71732912, 71443868, 71228780, 70844458, 70844460, 70844456, 71585584, 70844462, 71705042, 69880386, 71732914, 68158900, 68158874, 71508910, 71813128, 71355914, 68989284, 71170360, 70351024, 69829866, 71816084, 68162414, 68160964, 68160966, 68161356, 68161736, 67878266, 68160210, 68160212, 68161738, 68161742, 68048894, 71816092, 67692276, 67691646, 71838798, 68051642, 67692278, 68051636, 71893038
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 402
Event selection diagnostic rows: 28211
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 59
Latest x-ratelimit-reset: 2026-06-04T15:32:44Z
Latest retry-after: None

- 2026-06-04 15:00 | Bulgaria vs Albania | odds_api_io_Bet365_ML | 1.42/4.75/4.75
- 2026-06-04 15:00 | Sweden vs Finland | odds_api_io_Bet365_ML | 1.95/3.9/2.875
- 2026-06-04 15:00 | FC Wolfurt vs SV Ludesch | odds_api_io_Bet365_ML | 1.3/5.25/6.0
- 2026-06-04 15:30 | Slovenia vs Bosnia and Herzegovina | odds_api_io_Bet365_ML | 2.6/3.6/2.3
- 2026-06-04 16:00 | Afghanistan vs Bangladesh | odds_api_io_Bet365_ML | 1.333/4.0/9.0
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger | odds_api_io_Bet365_ML | 1.8/3.2/4.333
- 2026-06-04 16:00 | Burundi vs Equatorial Guinea | odds_api_io_Bet365_ML | 4.75/2.9/1.75
- 2026-06-04 16:00 | FC Dornbirn vs SVG Reichenau | odds_api_io_Bet365_ML | 1.55/4.333/4.2
- 2026-06-04 16:00 | Germany vs Denmark | odds_api_io_Bet365_ML | 1.533/4.1/4.5
- 2026-06-04 16:00 | Lebanon vs Yemen | odds_api_io_Bet365_ML | 1.95/2.6/4.333

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Bulgaria | target=Bulgaria vs Albania | candidate=Bulgaria vs Albania | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=Japan | target=Japan vs Fiji | candidate=Japan vs Fiji | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Andorra | target=Andorra vs Liechtenstein | candidate=Andorra vs Liechtenstein | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=San Lorenzo de Almagro Res. | target=San Lorenzo de Almagro Res. vs Velez Sarsfield Reserve | candidate=San Lorenzo de Almagro Res. vs Velez Sarsfield Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cooks Hill United FC Reserve | target=Cooks Hill United FC Reserve vs Belmont Swansea United FC Reserves | candidate=Cooks Hill United FC Reserve vs Belmont Swansea United FC Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Generation Foot | target=Generation Foot vs Ajel de Rufisque | candidate=Generation Foot vs Ajel de Rufisque | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Vinotinto FC Ecuador | target=Vinotinto FC Ecuador vs Cumbaya FC | candidate=Vinotinto FC Ecuador vs Cumbaya FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Deportivo Santani | target=Deportivo Santani vs Resistencia SC | candidate=Deportivo Santani vs Resistencia SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Stocksund | target=IFK Stocksund vs FC Stockholm Internazionale | candidate=IFK Stocksund vs FC Stockholm Internazionale | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Eastern United | target=Eastern United vs The Cove FC | candidate=Eastern United vs The Cove FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lautp | target=Lautp vs Peka | candidate=Lautp vs Peka | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Eltham Redbacks FC | target=Eltham Redbacks FC vs FC Bulleen Lions | candidate=Eltham Redbacks FC vs FC Bulleen Lions | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=IH Hafnarfjordur | target=IH Hafnarfjordur vs Arborg | candidate=IH Hafnarfjordur vs Arborg | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bentleigh Greens SC | target=Bentleigh Greens SC vs Boroondara Eagles | candidate=Bentleigh Greens SC vs Boroondara Eagles | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Solvesborgs GIF | target=Solvesborgs GIF vs Torns IF | candidate=Solvesborgs GIF vs Torns IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Millonarios FC | target=Millonarios FC vs Independiente Medellin | candidate=Millonarios FC vs Independiente Medellin | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Modbury Jets SC | target=Modbury Jets SC vs Fulham United FC | candidate=Modbury Jets SC vs Fulham United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sundby BK | target=Sundby BK vs Holbaek B&I | candidate=Sundby BK vs Holbaek B&I | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Germany | target=Germany vs Denmark | candidate=Germany vs Denmark | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Dornbirn | target=FC Dornbirn vs SVG Reichenau | candidate=FC Dornbirn vs SVG Reichenau | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 70872820
- multi_odds_match: No multi-odds payload matched event 71632302
- multi_odds_match: No multi-odds payload matched event 71443988
- multi_odds_match: No multi-odds payload matched event 71399594
- multi_odds_match: No multi-odds payload matched event 69924130
- multi_odds_match: No multi-odds payload matched event 71859964
- multi_odds_match: No multi-odds payload matched event 71859970
- multi_odds_match: No multi-odds payload matched event 71859962
- multi_odds_match: No multi-odds payload matched event 71859966
- multi_odds_match: No multi-odds payload matched event 69924696