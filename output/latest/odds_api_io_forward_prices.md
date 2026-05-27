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
Events discovery rows: 178
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: America FC MG
Selected event IDs: 69910676, 69910678, 71267616, 69910680, 71734140, 69910944, 69976278, 71267618, 71633030, 69342876, 69910946, 69910682, 69910948, 71491228, 71574410, 70773706, 69342880, 71267620, 70946056, 70946082, 70946052, 68751828, 71736646, 71736642, 71650104, 71685274, 71685276, 70773710, 71685272, 71238562, 71679480, 71238560, 71577986, 71734956, 69109016, 71553484, 67782936, 67604828, 70711924, 68774162, 71679670, 71685812, 68158852, 71681884, 69924498, 70965792, 71299152, 71072680, 61541488, 71685278, 71685280, 69688872, 71732466, 69688816, 68158846, 68158854, 68751818, 69688820, 69688870, 69688818, 68751830, 68751812, 68751820, 69688814, 71615196, 68306836, 68306838, 68158850, 71732468, 68751824, 71615628, 69688876, 69688874, 71636144, 68158830, 70703500, 71732456, 71732476, 70531734, 68751822
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 182
Event selection diagnostic rows: 11110
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 62
Latest x-ratelimit-reset: 2026-05-27T03:14:01Z
Latest retry-after: None

- 2026-05-27 07:00 | Dalian Yingbo B vs Shandong Taishan B | odds_api_io_Bet365_ML | 3.9/2.875/1.95
- 2026-05-27 07:00 | Shanxi Chongde Ronghai vs Qingdao Red Lions | odds_api_io_Bet365_ML | 1.85/3.3/3.5
- 2026-05-27 07:30 | Stallion Laguna FC vs Dynamic Herb Cebu FC | odds_api_io_Bet365_ML | 2.4/3.6/2.45
- 2026-05-27 08:00 | Changchun Xidu vs Beijing Institute of Technology | odds_api_io_Bet365_ML | 1.833/3.2/4.0
- 2026-05-27 08:00 | Mombasa United FC vs 3K FC | odds_api_io_Bet365_ML | 2.55/3.1/2.5
- 2026-05-27 08:00 | Xiamen Feilu vs Jiangxi Lushan | odds_api_io_Bet365_ML | 2.5/3.2/2.5
- 2026-05-27 10:00 | Sejong Sportstoto WFC vs Gyeongju FC | odds_api_io_Bet365_ML | 1.5/3.6/5.75
- 2026-05-27 10:15 | Davao Aguilas vs Taguig FC | odds_api_io_Bet365_ML | 7.5/6.0/1.222
- 2026-05-27 10:30 | The Gap FC vs Virginia United | odds_api_io_Bet365_ML | 1.571/4.333/4.0
- 2026-05-27 11:00 | FC Altai Oskemen vs FC Astana | odds_api_io_Bet365_ML | 3.0/3.0/2.25

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Velez Nevesinje | target=Velez Nevesinje vs FK Sutjeska Foca | candidate=Velez Nevesinje vs FK Sutjeska Foca | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IF Vestri | target=IF Vestri vs UMF Njardvik | candidate=IF Vestri vs UMF Njardvik | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sejong Sportstoto WFC | target=Sejong Sportstoto WFC vs Gyeongju FC | candidate=Sejong Sportstoto WFC vs Gyeongju FC | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=America FC MG | target=America FC MG vs CR Flamengo RJ | candidate=America FC MG vs CR Flamengo RJ | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Avai FC SC | target=Avai FC SC vs CR Vasco da Gama RJ | candidate=Avai FC SC vs CR Vasco da Gama RJ | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Stallion Laguna FC | target=Stallion Laguna FC vs Dynamic Herb Cebu FC | candidate=Stallion Laguna FC vs Dynamic Herb Cebu FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Newroz SC | target=Newroz SC vs AL Mosul SC | candidate=Newroz SC vs AL Mosul SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Niroye Zamini Tehran | target=Niroye Zamini Tehran vs Havadar SC | candidate=Niroye Zamini Tehran vs Havadar SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tampereen Ilves | target=Tampereen Ilves vs Turun Palloseura | candidate=Tampereen Ilves vs Turun Palloseura | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Goias EC GO | target=Goias EC GO vs Mirassol FC SP | candidate=Goias EC GO vs Mirassol FC SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Davao Aguilas | target=Davao Aguilas vs Taguig FC | candidate=Davao Aguilas vs Taguig FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AC Goianiense GO | target=AC Goianiense GO vs Operario Ferroviario EC PR | candidate=AC Goianiense GO vs Operario Ferroviario EC PR | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Shahrdari Nowshahr | target=Shahrdari Nowshahr vs FC Pars Jonoubi Jam | candidate=Shahrdari Nowshahr vs FC Pars Jonoubi Jam | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=VV Sparta Nijkerk | target=VV Sparta Nijkerk vs IJsselmeervogels | candidate=VV Sparta Nijkerk vs IJsselmeervogels | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=ADO 20 Heemskerk | target=ADO 20 Heemskerk vs FC Lisse | candidate=ADO 20 Heemskerk vs FC Lisse | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Manila Digger FC | target=Manila Digger FC vs Kaya FC–Iloilo | candidate=Manila Digger FC vs Kaya FC–Iloilo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Changchun Xidu | target=Changchun Xidu vs Beijing Institute of Technology | candidate=Changchun Xidu vs Beijing Institute of Technology | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Velez Sarsfield Reserve | target=Velez Sarsfield Reserve vs Instituto AC Cordoba Reserves | candidate=Velez Sarsfield Reserve vs Instituto AC Cordoba Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Pakhtakor | target=Pakhtakor vs FC Kattaqorgon | candidate=Pakhtakor vs FC Kattaqorgon | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Eskilstuna United DFF | target=Eskilstuna United DFF vs Hammarby IF | candidate=Eskilstuna United DFF vs Hammarby IF | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 69910946
- multi_odds_match: No multi-odds payload matched event 69910682
- multi_odds_match: No multi-odds payload matched event 69910948
- multi_odds_match: No multi-odds payload matched event 71491228
- multi_odds_match: No multi-odds payload matched event 71574410
- multi_odds_match: No multi-odds payload matched event 70773706
- multi_odds_match: No multi-odds payload matched event 69342880
- multi_odds_match: No multi-odds payload matched event 71267620
- multi_odds_match: No multi-odds payload matched event 70946056
- multi_odds_match: No multi-odds payload matched event 70946082