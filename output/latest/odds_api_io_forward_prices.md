# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 2 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 142
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 68046538, 68160188, 71234486, 70663798, 70317958, 67921082, 67239144, 67915858, 67919646, 67919278, 67915592, 67015206, 71668802, 71668804, 67915862, 67563298, 67921086, 70317954, 67915594, 67919280, 67915866, 68307876, 67850002, 71580016, 68307870, 68307868, 67850000, 67915596, 71532956, 67920620, 67850006, 70906734, 70906736, 67017968, 70774882, 71630496, 67017954, 67015196, 67017956, 67015198, 67017958, 67017960, 68492542, 67912696, 67017962, 67015204, 71612042, 67017964, 71630498, 67017966, 61911612, 67015208, 71620936, 68954850, 71575768, 67919282, 70929734, 71631808, 67919284, 68194428, 70929792, 70929732, 70929786, 70929788, 70929730, 71622030, 70317956, 70929790, 67920370, 71575770, 70929736, 61737350, 68852084, 68492544, 71631810, 69612876, 71530426, 71680540, 67849998, 71668806
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 142
Event selection diagnostic rows: 8200
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 2
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 73
Latest x-ratelimit-reset: 2026-05-25T03:15:11Z
Latest retry-after: None

- 2026-05-25 07:30 | Suwon Bluewings vs Cheonan City FC | odds_api_io_Bet365_ML | 1.533/3.9/5.5
- 2026-05-25 09:30 | South Melbourne FC vs Avondale FC | odds_api_io_Bet365_ML | 15.0/8.5/1.125
- 2026-05-25 11:00 | Bhutan vs Nepal | odds_api_io_Bet365_ML | 6.0/5.0/1.333
- 2026-05-25 11:00 | Esbjerg FB 2 vs Hobro IK 2 | odds_api_io_Bet365_ML | 2.875/3.75/2.0
- 2026-05-25 11:00 | Kolding IF vs Hillerod Fodbold | odds_api_io_Bet365_ML | 3.3/4.0/1.9
- 2026-05-25 12:00 | FK Gjoevik-Lyn vs Elverum | odds_api_io_Bet365_ML | 2.2/4.0/2.4
- 2026-05-25 12:00 | Naestved HG vs Esbjerg FB | odds_api_io_Bet365_ML | 1.363/4.75/5.75
- 2026-05-25 12:00 | Sotra SK vs Bjarg | odds_api_io_Bet365_ML | 1.533/4.0/4.75
- 2026-05-25 12:00 | Strindheim TF vs Nardo FK | odds_api_io_Bet365_ML | 1.666/4.333/3.5
- 2026-05-25 12:00 | Valerenga IF 2 vs Heming | odds_api_io_Bet365_ML | 3.1/4.333/1.8

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Suwon Bluewings | target=Suwon Bluewings vs Cheonan City FC | candidate=Suwon Bluewings vs Cheonan City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Esbjerg FB 2 | target=Esbjerg FB 2 vs Hobro IK 2 | candidate=Esbjerg FB 2 vs Hobro IK 2 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Naestved HG | target=Naestved HG vs Esbjerg FB | candidate=Naestved HG vs Esbjerg FB | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sotra SK | target=Sotra SK vs Bjarg | candidate=Sotra SK vs Bjarg | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Strindheim TF | target=Strindheim TF vs Nardo FK | candidate=Strindheim TF vs Nardo FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IBV Vestmannaeyjar | target=IBV Vestmannaeyjar vs Grindavik/Njarovik | candidate=IBV Vestmannaeyjar vs Grindavik/Njarovik | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lyngby BK | target=Lyngby BK vs AC Horsens | candidate=Lyngby BK vs AC Horsens | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Maccabi Kabilio Jaffa | target=Maccabi Kabilio Jaffa vs Hapoel Hadera FC | candidate=Maccabi Kabilio Jaffa vs Hapoel Hadera FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Madla | target=Madla vs Hinna | candidate=Madla vs Hinna | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Manama Club | target=Manama Club vs Al Ittihad | candidate=Manama Club vs Al Ittihad | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=MS Football Hapoel Kiryat Yam | target=MS Football Hapoel Kiryat Yam vs Maccabi Petah Tikva FC | candidate=MS Football Hapoel Kiryat Yam vs Maccabi Petah Tikva FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=NK Siroki Brijeg | target=NK Siroki Brijeg vs FK Radnik Bijeljina | candidate=NK Siroki Brijeg vs FK Radnik Bijeljina | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Phoenix Johvi | target=FC Phoenix Johvi vs Parnu JK Vaprus II | candidate=FC Phoenix Johvi vs Parnu JK Vaprus II | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC RFS | target=FC RFS vs FK Tukums 2000/TSS | candidate=FC RFS vs FK Tukums 2000/TSS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Valerenga IF 2 | target=Valerenga IF 2 vs Heming | candidate=Valerenga IF 2 vs Heming | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bhutan | target=Bhutan vs Nepal | candidate=Bhutan vs Nepal | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Eidsvold TF | target=Eidsvold TF vs Rana FK | candidate=Eidsvold TF vs Rana FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IK Start | target=IK Start vs Vaalerenga IF | candidate=IK Start vs Vaalerenga IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Montevideo Wanderers | target=Montevideo Wanderers vs Liverpool Montevideo | candidate=Montevideo Wanderers vs Liverpool Montevideo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Nof Hagalil FC | target=Hapoel Nof Hagalil FC vs Hapoel Acre FC | candidate=Hapoel Nof Hagalil FC vs Hapoel Acre FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 67915592
- multi_odds_match: No multi-odds payload matched event 67015206
- multi_odds_match: No multi-odds payload matched event 71668802
- multi_odds_match: No multi-odds payload matched event 71668804
- multi_odds_match: No multi-odds payload matched event 67915862
- multi_odds_match: No multi-odds payload matched event 67563298
- multi_odds_match: No multi-odds payload matched event 67921086
- multi_odds_match: No multi-odds payload matched event 70317954
- multi_odds_match: No multi-odds payload matched event 67915594
- multi_odds_match: No multi-odds payload matched event 67919280