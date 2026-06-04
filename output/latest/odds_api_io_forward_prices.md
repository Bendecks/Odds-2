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
Events discovery rows: 289
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Indonesia, Japan
Selected event IDs: 68664088, 61927920, 61541464, 71561890, 61915082, 71782694, 68050334, 71601902, 61541472, 70314476, 61541462, 61909690, 71834376, 70314468, 71561936, 71814506, 71834548, 61927926, 71749276, 71782698, 71652336, 61541460, 71834888, 56319305, 70872820, 71632302, 71443988, 71399594, 69924130, 71859964, 71859970, 71859962, 71859966, 69924696, 71445234, 71814430, 68311644, 69923708, 68320210, 70730796, 71399598, 71814432, 68310940, 71402260, 68344686, 71509102, 71322902, 68158872, 68158894, 68158868, 71508692, 71585582, 68158882, 71917810, 71732912, 71443868, 71228780, 70844458, 70844460, 70844456, 71585584, 70844462, 71705042, 69880386, 71732914, 68158900, 68158874, 71508910, 71813128, 71355914, 68989284, 71170360, 70351024, 69829866, 68162414, 68161356, 68161736, 67878266, 71803506, 71803446
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 307
Event selection diagnostic rows: 20136
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 64
Latest x-ratelimit-reset: 2026-06-04T03:37:32Z
Latest retry-after: None

- 2026-06-04 09:00 | DH van Hien vs K. Khanh Hoa | odds_api_io_Bet365_ML | 1.2/5.5/13.0
- 2026-06-04 09:00 | Dornbirner SV vs FC Rotenberg | odds_api_io_Bet365_ML | 1.833/3.8/3.25
- 2026-06-04 09:00 | FC Lustenau vs VfB Hohenems | odds_api_io_Bet365_ML | 2.55/3.75/2.3
- 2026-06-04 09:00 | Myanmar vs Vietnam | odds_api_io_Bet365_ML | 7.0/5.0/1.3
- 2026-06-04 09:00 | FC Raika Volders vs SC Mils | odds_api_io_Bet365_ML | 2.1/3.75/2.7
- 2026-06-04 11:00 | Maldives vs Pakistan | odds_api_io_Bet365_ML | 2.0/3.2/3.3
- 2026-06-04 11:00 | Modbury Jets SC Reserve vs Fulham United FC Reserve | odds_api_io_Bet365_ML | 1.222/6.5/7.5
- 2026-06-04 12:00 | Cambodia vs Bhutan | odds_api_io_Bet365_ML | 1.142/6.25/15.0
- 2026-06-04 12:00 | FC Lauterach vs SV Kuchl | odds_api_io_Bet365_ML | 5.0/5.25/1.38
- 2026-06-04 12:30 | FC Kattaqorgon vs Fardu Ferghana | odds_api_io_Bet365_ML | 1.75/3.6/3.7

## Event selection diagnostics

- src=events_search_fallback | query=Japan | target=Japan vs Mongolia | candidate=Japan vs Mongolia | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=Indonesia | target=Indonesia vs Kuwait | candidate=Indonesia vs Kuwait | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=US Goree | target=US Goree vs Stade de Mbour | candidate=US Goree vs Stade de Mbour | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Osasco Sporting SP | target=Osasco Sporting SP vs AE Velo Clube SP | candidate=Osasco Sporting SP vs AE Velo Clube SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Afghanistan | target=Afghanistan vs Bangladesh | candidate=Afghanistan vs Bangladesh | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sweden | target=Sweden vs Greece | candidate=Sweden vs Greece | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bentleigh Greens SC | target=Bentleigh Greens SC vs Boroondara Eagles | candidate=Bentleigh Greens SC vs Boroondara Eagles | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AFC Eskilstuna | target=AFC Eskilstuna vs Karlbergs BK | candidate=AFC Eskilstuna vs Karlbergs BK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ben Aknoun | target=Ben Aknoun vs USM Alger | candidate=Ben Aknoun vs USM Alger | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Slovenia | target=Slovenia vs Bosnia and Herzegovina | candidate=Slovenia vs Bosnia and Herzegovina | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dornbirner SV | target=Dornbirner SV vs FC Rotenberg | candidate=Dornbirner SV vs FC Rotenberg | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Stocksund | target=IFK Stocksund vs FC Stockholm Internazionale | candidate=IFK Stocksund vs FC Stockholm Internazionale | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Solvesborgs GIF | target=Solvesborgs GIF vs Torns IF | candidate=Solvesborgs GIF vs Torns IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sundby BK | target=Sundby BK vs Holbaek B&I | candidate=Sundby BK vs Holbaek B&I | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Wolfurt | target=FC Wolfurt vs SV Ludesch | candidate=FC Wolfurt vs SV Ludesch | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=America FC SP | target=America FC SP vs CA Juventus SP | candidate=America FC SP vs CA Juventus SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Mexico | target=Mexico vs Serbia | candidate=Mexico vs Serbia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=DH van Hien | target=DH van Hien vs K. Khanh Hoa | candidate=DH van Hien vs K. Khanh Hoa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Dornbirn | target=FC Dornbirn vs SVG Reichenau | candidate=FC Dornbirn vs SVG Reichenau | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Talleres de Cordoba Reserve | target=CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve | candidate=CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 61541462
- multi_odds_match: No multi-odds payload matched event 61909690
- multi_odds_match: No multi-odds payload matched event 71834376
- multi_odds_match: No multi-odds payload matched event 70314468
- multi_odds_match: No multi-odds payload matched event 71561936
- multi_odds_match: No multi-odds payload matched event 71814506
- multi_odds_match: No multi-odds payload matched event 71834548
- multi_odds_match: No multi-odds payload matched event 61927926
- multi_odds_match: No multi-odds payload matched event 71749276
- multi_odds_match: No multi-odds payload matched event 71782698