# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 14 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 394
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Como, Genoa, Juventus, Pisa, Roma, Anderlecht, Man United, La Coruna, AZ Alkmaar, Heerenveen
Selected event IDs: 61515244, 61515256, 61515258, 69279590, 61515248, 70966260, 61515246, 61515254, 61515242, 61515250, 71467818, 71471574, 70231956, 71467824, 71439998, 68311602, 71467784, 71482712, 61789404, 68310896, 68311600, 61301257, 69670716, 68492528, 70708878, 68310900, 67845758, 68310902, 68310904, 61788920, 69342848, 68306812, 71427438, 68214656, 61301259, 71411460, 71069098, 65382126, 62216468, 70502988, 69880318, 61286591, 70231958, 61788918, 63185781, 66886782, 61789408, 71467788, 71467790, 67849994, 68320796, 71467826, 61788930, 71467820, 68311604, 61788928, 71467812, 71467780, 70774886, 61895632
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 416
Event selection diagnostic rows: 29636
Selected event rows: 60
Priced event rows: 10
Price rows: 10
Errors/status rows: 59

## Provider rate-limit headers

Header rows captured: 14
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 28
Latest x-ratelimit-reset: 2026-05-17T13:54:52Z
Latest retry-after: None

- 2026-05-17 13:30 | 1. FC Magdeburg vs 1 FC Kaiserslautern | odds_api_io_Bet365_ML | 1.5/4.75/5.0
- 2026-05-17 13:30 | Arminia Bielefeld vs Hertha BSC | odds_api_io_Bet365_ML | 1.7/3.8/4.5
- 2026-05-17 13:30 | Dynamo Dresden vs Holstein Kiel | odds_api_io_Bet365_ML | 1.75/4.0/4.1
- 2026-05-17 13:30 | Hamilton Academical WFC vs Montrose FC | odds_api_io_Bet365_ML | 7.5/4.75/1.3
- 2026-05-17 13:30 | Hannover 96 vs 1 FC Nuremberg | odds_api_io_Bet365_ML | 1.5/4.5/5.75
- 2026-05-17 13:30 | FC Hradec Kralove vs FK Pardubice | odds_api_io_Bet365_ML | 1.363/5.0/5.5
- 2026-05-17 13:30 | Karlsruher SC vs VfL Bochum | odds_api_io_Bet365_ML | 2.45/3.75/2.45
- 2026-05-17 13:30 | Schalke 04 vs Eintracht Braunschweig | odds_api_io_Bet365_ML | 1.727/3.8/4.5
- 2026-05-17 13:30 | SV 07 Elversberg vs SC Preussen 06 Munster | odds_api_io_Bet365_ML | 1.25/6.5/9.0
- 2026-05-17 13:30 | SV Darmstadt 98 vs SC Paderborn 07 | odds_api_io_Bet365_ML | 3.5/3.9/1.9

## Event selection diagnostics

- src=events_bookmaker_filtered | query=KF Dukagjini | target=KF Dukagjini vs FC Drita | candidate=KF Dukagjini vs FC Drita | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AC Prato 1908 | target=AC Prato 1908 vs ASD Seravezza Pozzi Calcio | candidate=AC Prato 1908 vs ASD Seravezza Pozzi Calcio | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Skiljebo SK | target=Skiljebo SK vs Kungsangens IF | candidate=Skiljebo SK vs Kungsangens IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=National Bank of Egypt SC | target=National Bank of Egypt SC vs El Gouna FC | candidate=National Bank of Egypt SC vs El Gouna FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Meyrin | target=FC Meyrin vs FC Echallens Region | candidate=FC Meyrin vs FC Echallens Region | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Stocksund | target=IFK Stocksund vs Piteaa IF | candidate=IFK Stocksund vs Piteaa IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Cukaricki Belgrade | target=FK Cukaricki Belgrade vs FK Partizan Belgrade | candidate=FK Cukaricki Belgrade vs FK Partizan Belgrade | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Trelleborgs FF | target=Trelleborgs FF vs FC Trollhattan | candidate=Trelleborgs FF vs FC Trollhattan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Kuressaare | target=FC Kuressaare vs Nomme Kalju FC | candidate=FC Kuressaare vs Nomme Kalju FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Mohun Bagan Super Giant | target=Mohun Bagan Super Giant vs SC East Bengal | candidate=Mohun Bagan Super Giant vs SC East Bengal | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gefle IF | target=Gefle IF vs Assyriska FF | candidate=Gefle IF vs Assyriska FF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=ASD Martina Calcio 1947 | target=ASD Martina Calcio 1947 vs Paganese Calcio | candidate=ASD Martina Calcio 1947 vs Paganese Calcio | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Auda Riga | target=FK Auda Riga vs FC RFS | candidate=FK Auda Riga vs FC RFS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IF Karlstad Fotbol | target=IF Karlstad Fotbol vs Vasalunds IF | candidate=IF Karlstad Fotbol vs Vasalunds IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=US Mondorf-Les-Bains | target=US Mondorf-Les-Bains vs Union Titus Petange | candidate=US Mondorf-Les-Bains vs Union Titus Petange | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=HPS | target=HPS vs HJK Helsinki | candidate=HPS vs HJK Helsinki | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=NK Slaven Belupo | target=NK Slaven Belupo vs GNK Dinamo Zagreb | candidate=NK Slaven Belupo vs GNK Dinamo Zagreb | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Leeds United | target=Leeds United vs Brighton & Hove Albion | candidate=Leeds United vs Brighton & Hove Albion | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kaisar Kyzylorda | target=Kaisar Kyzylorda vs Tobol Kostanay | candidate=Kaisar Kyzylorda vs Tobol Kostanay | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dynamo Dresden | target=Dynamo Dresden vs Holstein Kiel | candidate=Dynamo Dresden vs Holstein Kiel | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Como'; best=0.547
- event_selection: No event above confidence 0.72 for query 'Genoa'; best=0.6267
- event_selection: No event above confidence 0.72 for query 'Juventus'; best=0.5509
- event_selection: No event above confidence 0.72 for query 'Pisa'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Roma'; best=0.6743
- event_selection: No event above confidence 0.72 for query 'Anderlecht'; best=0.5509
- event_selection: No event above confidence 0.72 for query 'Man United'; best=0.5979
- event_selection: No event above confidence 0.72 for query 'La Coruna'; best=0.0
- event_selection: No event above confidence 0.72 for query 'AZ Alkmaar'; best=0.6343
- multi_odds_match: No multi-odds payload matched event 71467818