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
Events discovery rows: 276
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 69924102, 61927890, 70090084, 71312154, 71343350, 70926662, 67915816, 70318288, 68344646, 70479350, 70344940, 68310884, 70479314, 68377650, 67915570, 68311588, 68310886, 68377654, 70844428, 67920352, 71343346, 68377658, 67919604, 67919608, 67921052, 70926664, 67920356, 69539870, 68344650, 67920350, 70906780, 70981006, 67915820, 68310888, 70774892, 67919620, 67563266, 67915572, 68320174, 67921064, 67919258, 70683964, 70267784, 67921056, 71423498, 70945796, 63637929, 69491788, 70945864, 67915824, 68311590, 71218680, 68310890, 70820616, 70820618, 69924662, 68311592, 68311594, 70648002, 71336696, 71339462, 71339460, 70448376, 70448378, 70774888, 70448380, 71370014, 70906776, 70774898, 61591358, 69757834, 71372084, 61591362, 70820614, 67126094, 61591360, 61591372, 61591366, 61541420, 71203972
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365, Bet365 (no latency)
Selected markets: ML
Fixture rows: 275
Event selection diagnostic rows: 18920
Selected event rows: 80
Priced event rows: 8
Price rows: 8
Errors/status rows: 72

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 83
Latest x-ratelimit-reset: 2026-05-14T03:30:03Z
Latest retry-after: None

- 2026-05-14 08:00 | SJK-J vs FC Kiisto | odds_api_io_Bet365_ML | 4.333/4.5/1.48
- 2026-05-14 09:00 | SV Lochau vs FC Wolfurt | odds_api_io_Bet365_ML | 2.3/3.6/2.55
- 2026-05-14 09:30 | Neroca FC vs Sudeva Delhi FC | odds_api_io_Bet365_ML | 1.7/3.7/3.9
- 2026-05-14 10:00 | FC Barcelona vs CD Tenerife | odds_api_io_Bet365_ML | 1.7/4.75/3.2
- 2026-05-14 10:00 | JaPS vs FC KTP | odds_api_io_Bet365_ML | 5.0/6.0/1.333
- 2026-05-14 10:00 | Sidama Bunna SC vs Hadiya Hossana FC | odds_api_io_Bet365_ML | 1.75/2.9/4.75
- 2026-05-14 11:00 | Hobro IK vs Aarhus Fremad | odds_api_io_Bet365 (no latency)_ML | 2.8/3.1/2.5
- 2026-05-14 11:00 | Mtibwa Sugar FC vs Kmc FC | odds_api_io_Bet365_ML | 1.909/2.9/4.0

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Bjarg | target=Bjarg vs Brattvaag | candidate=Bjarg vs Brattvaag | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Urartu Yerevan | target=FC Urartu Yerevan vs FC Noah Yerevan | candidate=FC Urartu Yerevan vs FC Noah Yerevan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SJK-J | target=SJK-J vs FC Kiisto | candidate=SJK-J vs FC Kiisto | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sidama Bunna SC | target=Sidama Bunna SC vs Hadiya Hossana FC | candidate=Sidama Bunna SC vs Hadiya Hossana FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hobro IK | target=Hobro IK vs Aarhus Fremad | candidate=Hobro IK vs Aarhus Fremad | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SV Kuchl | target=SV Kuchl vs FC Kitzbuhel | candidate=SV Kuchl vs FC Kitzbuhel | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Salzburg Frauen | target=FC Salzburg Frauen vs FK Austria Wien | candidate=FC Salzburg Frauen vs FK Austria Wien | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SK Austria Klagenfurt | target=SK Austria Klagenfurt vs FC Liefering | candidate=SK Austria Klagenfurt vs FC Liefering | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IF Karlstad Fotbol | target=IF Karlstad Fotbol vs IFK Stocksund | candidate=IF Karlstad Fotbol vs IFK Stocksund | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kjp Kouvola | target=Kjp Kouvola vs Lautp | candidate=Kjp Kouvola vs Lautp | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Trelleborgs FF | target=Trelleborgs FF vs Jonkopings Sodra IF | candidate=Trelleborgs FF vs Jonkopings Sodra IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SK Traeff | target=SK Traeff vs Lysekloster | candidate=SK Traeff vs Lysekloster | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Assyriska FF | target=Assyriska FF vs Umea FC | candidate=Assyriska FF vs Umea FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Viking FK 2 | target=Viking FK 2 vs Akra | candidate=Viking FK 2 vs Akra | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Copenhagen | target=FC Copenhagen vs FC Midtjylland | candidate=FC Copenhagen vs FC Midtjylland | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=HB Torshavn | target=HB Torshavn vs Vikingur Gota | candidate=HB Torshavn vs Vikingur Gota | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Vastra Frolunda IF | target=Vastra Frolunda IF vs IK Kongahalla | candidate=Vastra Frolunda IF vs IK Kongahalla | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Angelholms FF | target=Angelholms FF vs Aatvidabergs FF | candidate=Angelholms FF vs Aatvidabergs FF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tvaakers IF | target=Tvaakers IF vs BK Olympic | candidate=Tvaakers IF vs BK Olympic | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Trollhattan | target=FC Trollhattan vs Ariana FC | candidate=FC Trollhattan vs Ariana FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 67915816
- multi_odds_match: No multi-odds payload matched event 68344646
- multi_odds_match: No multi-odds payload matched event 70344940
- multi_odds_match: No multi-odds payload matched event 68310884
- multi_odds_match: No multi-odds payload matched event 70479314
- multi_odds_match: No multi-odds payload matched event 68377650
- multi_odds_match: No multi-odds payload matched event 67915570
- multi_odds_match: No multi-odds payload matched event 68311588
- multi_odds_match: No multi-odds payload matched event 68310886
- multi_odds_match: No multi-odds payload matched event 68377654