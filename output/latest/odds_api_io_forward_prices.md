# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 6 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 245
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Atromitos, Kifisia, Panetolikos
Selected event IDs: 71423472, 71581926, 71474764, 70926698, 70926696, 61651686, 63637933, 70945952, 70479398, 63637931, 71426280, 70946042, 70946044, 68746498, 71489164, 68746506, 68746504, 67845766, 71039182, 71589706, 70232106, 68492534, 70926700, 70224452, 70479402, 71549302, 70232108, 71575764, 71575766, 70684194, 69109006, 71523852, 71352614, 71055200, 70232110, 71530418, 71563848, 71579104, 71558146, 67126672, 68320188, 61902056, 69923684, 67919630, 70684198, 68492536, 70224454, 61466383, 70663780, 69880336, 71530420, 64055897, 64055885, 64055887, 64055889, 64055893, 64055899, 71553438, 68158798, 68751798, 68751810, 68751792, 68158824, 68158796, 68194650, 68158794, 71166642, 70479404, 64055901, 68751806, 68158810, 71352616, 61737338, 61737346, 70207436, 70207438, 71514078
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 246
Event selection diagnostic rows: 16559
Selected event rows: 77
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 6
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 64
Latest x-ratelimit-reset: 2026-05-21T03:07:59Z
Latest retry-after: None

- 2026-05-21 07:00 | Khangarid vs Central Stallions FC | odds_api_io_Bet365_ML | 3.25/4.0/1.8
- 2026-05-21 08:00 | Maccabi Petah Tikva vs Beitar Jerusalem | odds_api_io_Bet365_ML | 2.55/3.2/2.5
- 2026-05-21 11:30 | Libertad Asuncion vs Sportivo Trinidense | odds_api_io_Bet365_ML | 1.2/5.5/10.0
- 2026-05-21 12:00 | Adama City FC vs Welwalo Adigrat | odds_api_io_Bet365_ML | 2.7/2.75/2.625
- 2026-05-21 12:00 | Arba Minch Ketema vs Sidama Bunna SC | odds_api_io_Bet365_ML | 4.5/3.0/1.75
- 2026-05-21 12:30 | FC Shakhtar Donetsk vs Kolos Kovalivka | odds_api_io_Bet365_ML | 1.285/4.333/9.5
- 2026-05-21 13:00 | Cabrayil vs Simal | odds_api_io_Bet365_ML | 2.75/3.7/2.05
- 2026-05-21 13:00 | FC Fard Alborz vs FC Pars Jonoubi Jam | odds_api_io_Bet365_ML | 2.4/2.6/3.2
- 2026-05-21 13:00 | Jkt Tanzania vs Fountain Gate FC | odds_api_io_Bet365_ML | 1.666/3.2/5.0
- 2026-05-21 13:00 | Moik Baku vs Difai Agsu | odds_api_io_Bet365_ML | 1.909/3.4/3.4

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Namungo FC | target=Namungo FC vs Mbeya City FC | candidate=Namungo FC vs Mbeya City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Zeljeznicar Sarajevo | target=FK Zeljeznicar Sarajevo vs NK Siroki Brijeg | candidate=FK Zeljeznicar Sarajevo vs NK Siroki Brijeg | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Kholood | target=Al-Kholood vs Al-Fateh SC | candidate=Al-Kholood vs Al-Fateh SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CR Vasco da Gama RJ | target=CR Vasco da Gama RJ vs America FC MG | candidate=CR Vasco da Gama RJ vs America FC MG | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Grei Kvinner Elite FK | target=Grei Kvinner Elite FK vs Lyn | candidate=Grei Kvinner Elite FK vs Lyn | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Killas | target=FC Killas vs FC Melgar | candidate=FC Killas vs FC Melgar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=KF Ferizaj | target=KF Ferizaj vs KF Dukagjini | candidate=KF Ferizaj vs KF Dukagjini | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Mohun Bagan Super Giant | target=Mohun Bagan Super Giant vs Sporting Club Delhi | candidate=Mohun Bagan Super Giant vs Sporting Club Delhi | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Jamshedpur FC | target=Jamshedpur FC vs Odisha FC | candidate=Jamshedpur FC vs Odisha FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FF Jaro Akademia | target=FF Jaro Akademia vs VPS Akatemia | candidate=FF Jaro Akademia vs VPS Akatemia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IK Tord | target=IK Tord vs Skara FC | candidate=IK Tord vs Skara FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Ittihad Club | target=Al-Ittihad Club vs Al Qadsiah | candidate=Al-Ittihad Club vs Al Qadsiah | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cabrayil | target=Cabrayil vs Simal | candidate=Cabrayil vs Simal | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Boca Juniors | target=Boca Juniors vs CA River Plate (ARG) | candidate=Boca Juniors vs CA River Plate (ARG) | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ilzer SV | target=Ilzer SV vs USV Gnas | candidate=Ilzer SV vs USV Gnas | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IA Akranes | target=IA Akranes vs IBV Vestmannaeyjar | candidate=IA Akranes vs IBV Vestmannaeyjar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Odd BK | target=Odd BK vs KFUM Oslo | candidate=Odd BK vs KFUM Oslo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SK Treibach | target=SK Treibach vs FC Gleisdorf 09 | candidate=SK Treibach vs FC Gleisdorf 09 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Atlantis FC/2 | target=Atlantis FC/2 vs Toolon Taisto | candidate=Atlantis FC/2 vs Toolon Taisto | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Neom SC | target=Neom SC vs Al-Ittifaq FC | candidate=Neom SC vs Al-Ittifaq FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Atromitos'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Kifisia'; best=0.505
- event_selection: No event above confidence 0.72 for query 'Panetolikos'; best=0.0
- multi_odds_match: No multi-odds payload matched event 71426280
- multi_odds_match: No multi-odds payload matched event 70946042
- multi_odds_match: No multi-odds payload matched event 70946044
- multi_odds_match: No multi-odds payload matched event 68746498
- multi_odds_match: No multi-odds payload matched event 71489164
- multi_odds_match: No multi-odds payload matched event 68746506
- multi_odds_match: No multi-odds payload matched event 68746504