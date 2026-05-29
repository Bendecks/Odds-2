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
Events discovery rows: 615
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 69254676, 67912710, 69670734, 68492550, 67604830, 67845768, 67845774, 69109020, 70683984, 69924692, 68538272, 67604832, 71732830, 69972748, 69972742, 71732828, 68538274, 62036316, 71482568, 71288188, 69670736, 71737510, 68954852, 61911566, 68959610, 67017092, 67604834, 65653558, 70684212, 71727738, 61911562, 71284974, 62274248, 61911556, 69108842, 70730328, 68538276, 69920658, 71530436, 69670738, 67920378, 61906394, 61466401, 69924500, 67015224, 67843320, 61927912, 70730382, 61902074, 68954856, 67015212, 68377704, 69880356, 61466395, 70730738, 67912704, 67015214, 68320812, 68377708, 68377594, 70730330, 69880346, 67126586, 67015220, 67912708, 62274236, 67015210, 66053756, 68492552, 68320196, 61898656, 61902078, 68344672, 67015222, 68344674, 62274240, 68320198, 61894080, 71520322, 71704018
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 615
Event selection diagnostic rows: 46040
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 52
Latest x-ratelimit-reset: 2026-05-29T15:37:59Z
Latest retry-after: None

- 2026-05-29 15:00 | Deportes Temuco vs Santiago Wanderers | odds_api_io_Bet365_ML | 3.4/3.6/1.85
- 2026-05-29 15:00 | FC Dila Gori vs FC Samgurali Tskaltubo | odds_api_io_Bet365_ML | 2.0/3.0/3.5
- 2026-05-29 15:00 | FK Babrungas Plunge vs FK Minija 2017 | odds_api_io_Bet365_ML | 3.6/3.5/1.833
- 2026-05-29 15:00 | Riga FC vs Grobinas SC/LFS | odds_api_io_Bet365_ML | 1.142/7.5/13.0
- 2026-05-29 15:30 | FC Haka Valkeakoski vs JIPPO | odds_api_io_Bet365_ML | 2.1/3.4/2.875
- 2026-05-29 15:30 | HJK Helsinki vs VIFK | odds_api_io_Bet365_ML | 1.02/17.0/51.0
- 2026-05-29 15:30 | HPS vs Kuopion Palloseura | odds_api_io_Bet365_ML | 3.3/3.9/1.8
- 2026-05-29 15:30 | Huima/Urho vs GBK Kokkola | odds_api_io_Bet365_ML | 1.666/4.333/3.8
- 2026-05-29 15:30 | KaaPo vs LTU | odds_api_io_Bet365_ML | 1.48/4.75/4.333
- 2026-05-29 15:30 | Kopa vs Lautp | odds_api_io_Bet365_ML | 4.5/4.5/1.48

## Event selection diagnostics

- src=events_bookmaker_filtered | query=KFUM Oslo | target=KFUM Oslo vs Tromsoe IL | candidate=KFUM Oslo vs Tromsoe IL | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Aalesunds FK | target=Aalesunds FK vs HamKam | candidate=Aalesunds FK vs HamKam | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hoersholm-Usseroed IK | target=Hoersholm-Usseroed IK vs FA 2000 | candidate=Hoersholm-Usseroed IK vs FA 2000 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tampereen Ilves 2 | target=Tampereen Ilves 2 vs HJS | candidate=Tampereen Ilves 2 vs HJS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Nacka FC | target=Nacka FC vs Nykopings BIS | candidate=Nacka FC vs Nykopings BIS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Pogon Sokol Lubaczow | target=Pogon Sokol Lubaczow vs Star Starachowice | candidate=Pogon Sokol Lubaczow vs Star Starachowice | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=HPS | target=HPS vs Kuopion Palloseura | candidate=HPS vs Kuopion Palloseura | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=TPV Tampere | target=TPV Tampere vs Tampere United | candidate=TPV Tampere vs Tampere United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Dinamo Bucuresti 1948 | target=FC Dinamo Bucuresti 1948 vs Fotbal Club FCSB | candidate=FC Dinamo Bucuresti 1948 vs Fotbal Club FCSB | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SC Zulimanit | target=SC Zulimanit vs Tou | candidate=SC Zulimanit vs Tou | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SV Donau Klagenfurt | target=SV Donau Klagenfurt vs SV Spittal/Drau | candidate=SV Donau Klagenfurt vs SV Spittal/Drau | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ghazl El Mahallah | target=Ghazl El Mahallah vs Haras El Hodood | candidate=Ghazl El Mahallah vs Haras El Hodood | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Torns IF | target=Torns IF vs Linero IF | candidate=Torns IF vs Linero IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fehring 1947 | target=Fehring 1947 vs SV Lebring | candidate=Fehring 1947 vs SV Lebring | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Andorra | target=Andorra vs Iraq | candidate=Andorra vs Iraq | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=ASV Siegendorf | target=ASV Siegendorf vs ASK Horitschon/U | candidate=ASV Siegendorf vs ASK Horitschon/U | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kungsangens IF | target=Kungsangens IF vs IK Franke | candidate=Kungsangens IF vs IK Franke | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Stadlau | target=FC Stadlau vs Simmeringer SC | candidate=FC Stadlau vs Simmeringer SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SK Brann | target=SK Brann vs Sarpsborg 08 | candidate=SK Brann vs Sarpsborg 08 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=BK Fremad Amager | target=BK Fremad Amager vs Skive IK | candidate=BK Fremad Amager vs Skive IK | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 68538272
- multi_odds_match: No multi-odds payload matched event 67604832
- multi_odds_match: No multi-odds payload matched event 71732830
- multi_odds_match: No multi-odds payload matched event 69972748
- multi_odds_match: No multi-odds payload matched event 69972742
- multi_odds_match: No multi-odds payload matched event 71732828
- multi_odds_match: No multi-odds payload matched event 68538274
- multi_odds_match: No multi-odds payload matched event 62036316
- multi_odds_match: No multi-odds payload matched event 71482568
- multi_odds_match: No multi-odds payload matched event 71288188