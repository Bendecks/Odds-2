# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 9 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 298
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Atromitos, Kifisia, Panetolikos, Anderlecht, Gent, Mechelen
Selected event IDs: 70232106, 68492534, 70926700, 70224452, 70479402, 71549302, 70232108, 71575764, 71575766, 70684194, 69109006, 71523852, 71352614, 71055200, 70232110, 71530418, 71563848, 71579104, 71558146, 71633104, 67126672, 68320188, 61902056, 69923684, 67919630, 70684198, 68492536, 70224454, 61466383, 70663780, 69880336, 71530420, 71631772, 64055897, 64055885, 64055887, 64055889, 64055893, 64055899, 71553438, 68158798, 68751798, 68751810, 68751792, 68158824, 68158796, 68194650, 68158794, 71166642, 70479404, 64055901, 68751806, 68158810, 71352616, 71546792, 61737338, 61737346, 70207436, 70207438, 71514078, 71443804, 70207440, 68971758, 68097924, 71538008, 71355038, 71558148, 70844436, 70687996, 70844442, 70844440, 70844438, 71426282, 70844444
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 306
Event selection diagnostic rows: 20878
Selected event rows: 74
Priced event rows: 6
Price rows: 6
Errors/status rows: 74

## Provider rate-limit headers

Header rows captured: 9
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 39
Latest x-ratelimit-reset: 2026-05-21T15:39:27Z
Latest retry-after: None

- 2026-05-21 15:00 | Negelle Arsi vs Shire Endaselassie FC | odds_api_io_Bet365_ML | 1.85/2.6/5.0
- 2026-05-21 15:30 | Coastal Union FC vs Simba SC | odds_api_io_Bet365_ML | 9.0/4.5/1.27
- 2026-05-21 15:30 | Qatar vs Sudan | odds_api_io_Bet365_ML | 1.083/8.5/29.0
- 2026-05-21 16:00 | AE Kifisia FC vs AE Larissa FC | odds_api_io_Bet365_ML | 2.3/3.1/3.3
- 2026-05-21 16:00 | Al-Najma Manama vs Al Ittihad | odds_api_io_Bet365_ML | 2.0/3.2/3.5
- 2026-05-21 16:00 | Atlantis FC/2 vs Toolon Taisto | odds_api_io_Bet365_ML | 1.75/4.5/3.1

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Qatar | target=Qatar vs Sudan | candidate=Qatar vs Sudan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FF Jaro Akademia | target=FF Jaro Akademia vs VPS Akatemia | candidate=FF Jaro Akademia vs VPS Akatemia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Barracas Central Reserve | target=CA Barracas Central Reserve vs CA Union Santa Fe Reserve | candidate=CA Barracas Central Reserve vs CA Union Santa Fe Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Riyadh SC | target=Al-Riyadh SC vs Al-Okhdood Club | candidate=Al-Riyadh SC vs Al-Okhdood Club | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Boca Juniors | target=Boca Juniors vs CA River Plate (ARG) | candidate=Boca Juniors vs CA River Plate (ARG) | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Kholood | target=Al-Kholood vs Al-Fateh SC | candidate=Al-Kholood vs Al-Fateh SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Ittihad Club | target=Al-Ittihad Club vs Al Qadsiah | candidate=Al-Ittihad Club vs Al Qadsiah | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Paranaense PR | target=CA Paranaense PR vs Botafogo FR RJ | candidate=CA Paranaense PR vs Botafogo FR RJ | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Nassr Club | target=Al Nassr Club vs Damac FC | candidate=Al Nassr Club vs Damac FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=EC Bahia BA | target=EC Bahia BA vs Fortaleza EC CE | candidate=EC Bahia BA vs Fortaleza EC CE | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tarup-Paarup IF | target=Tarup-Paarup IF vs Vorup FB | candidate=Tarup-Paarup IF vs Vorup FB | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IA Akranes | target=IA Akranes vs IBV Vestmannaeyjar | candidate=IA Akranes vs IBV Vestmannaeyjar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Killas | target=FC Killas vs FC Melgar | candidate=FC Killas vs FC Melgar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Fahaheel | target=Al-Fahaheel vs Kuwait SC | candidate=Al-Fahaheel vs Kuwait SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Grei Kvinner Elite FK | target=Grei Kvinner Elite FK vs Lyn | candidate=Grei Kvinner Elite FK vs Lyn | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gimnasia de Mendoza Reserve | target=Gimnasia de Mendoza Reserve vs Atletico Tucuman Reserve | candidate=Gimnasia de Mendoza Reserve vs Atletico Tucuman Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=KF Ferizaj | target=KF Ferizaj vs KF Dukagjini | candidate=KF Ferizaj vs KF Dukagjini | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Instituto AC Cordoba Reserves | target=Instituto AC Cordoba Reserves vs CD Godoy Cruz | candidate=Instituto AC Cordoba Reserves vs CD Godoy Cruz | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Wadi Degla SC | target=Wadi Degla SC vs Zed FC | candidate=Wadi Degla SC vs Zed FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AE Kifisia FC | target=AE Kifisia FC vs AE Larissa FC | candidate=AE Kifisia FC vs AE Larissa FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Atromitos'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Kifisia'; best=0.505
- event_selection: No event above confidence 0.72 for query 'Panetolikos'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Anderlecht'; best=0.54
- event_selection: No event above confidence 0.72 for query 'Gent'; best=0.5723
- event_selection: No event above confidence 0.72 for query 'Mechelen'; best=0.0
- multi_odds_match: No multi-odds payload matched event 70232106
- multi_odds_match: No multi-odds payload matched event 68492534
- multi_odds_match: No multi-odds payload matched event 70224452
- multi_odds_match: No multi-odds payload matched event 71575764