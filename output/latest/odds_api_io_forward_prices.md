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
Events discovery rows: 135
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Quinns FC Reserve, Bournemouth
Selected event IDs: 71465134, 70926682, 71582646, 71009988, 71177274, 71491232, 68746508, 68995156, 68995162, 71579008, 71500638, 68995160, 71465136, 71164846, 71357284, 71426270, 71489072, 71426268, 71553494, 71553492, 71553138, 71344708, 71218292, 71344710, 71360374, 71238550, 69923680, 70929780, 70929778, 70929782, 69924108, 71523836, 70929784, 67919906, 71579002, 71579010, 71553430, 71344712, 71553498, 71553500, 71500640, 71500642, 71218290, 71218286, 67126100, 67921076, 70812414, 70812412, 70812416, 71477636, 71001772, 69090916, 68158802, 68158822, 68158812, 69688810, 68158816, 68158808, 68158828, 69688866, 61301247, 71579006, 70207506, 70207508, 71540168, 70207504, 71344714, 71173724, 71426272, 68751804, 70075272, 70076108, 70075680, 70075712, 71506796, 70075248, 71354860, 69090918, 71240280
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 137
Event selection diagnostic rows: 7721
Selected event rows: 79
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 52
Latest x-ratelimit-reset: 2026-05-19T03:09:53Z
Latest retry-after: None

- 2026-05-19 07:30 | Turkmenistan vs Uzbekistan | odds_api_io_Bet365_ML | 6.5/5.25/1.285
- 2026-05-19 10:00 | Ethiopian Medhin vs Wolaita Dicha SC | odds_api_io_Bet365_ML | 2.5/2.625/3.0
- 2026-05-19 10:00 | Rtc FC vs Paro FC | odds_api_io_Bet365_ML | 2.875/4.2/1.909
- 2026-05-19 11:00 | HNK Hajduk Split vs NK Mladost Zdralovi | odds_api_io_Bet365_ML | 1.222/5.25/9.0
- 2026-05-19 11:15 | Murdoch University Melville FC vs Joondalup City | odds_api_io_Bet365_ML | 2.7/3.75/2.1
- 2026-05-19 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka | odds_api_io_Bet365_ML | 1.666/3.6/4.2
- 2026-05-19 11:30 | Northeast United FC vs Mohammedan SC | odds_api_io_Bet365_ML | 1.25/4.75/8.5
- 2026-05-19 11:35 | Tianjin Jinmen Tiger vs Henan | odds_api_io_Bet365_ML | 2.8/3.2/2.55
- 2026-05-19 12:00 | Chengdu Rongcheng vs Shanghai Port FC | odds_api_io_Bet365_ML | 1.48/4.5/6.25
- 2026-05-19 12:00 | Hapoel Ironi Kiryat Shmona vs Maccabi Herzliya | odds_api_io_Bet365_ML | 3.1/3.6/1.909

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Chengdu Rongcheng | target=Chengdu Rongcheng vs Shanghai Port FC | candidate=Chengdu Rongcheng vs Shanghai Port FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Juventud de Las Piedras | target=Juventud de Las Piedras vs Colon FC Reserve | candidate=Juventud de Las Piedras vs Colon FC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fluminense FC RJ | target=Fluminense FC RJ vs Club Bolivar | candidate=Fluminense FC RJ vs Club Bolivar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IF Sao Joseense PR | target=IF Sao Joseense PR vs Azuriz FC PR | candidate=IF Sao Joseense PR vs Azuriz FC PR | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Qingdao West Coast FC | target=Qingdao West Coast FC vs Beijing Guoan | candidate=Qingdao West Coast FC vs Beijing Guoan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tianjin Jinmen Tiger | target=Tianjin Jinmen Tiger vs Henan | candidate=Tianjin Jinmen Tiger vs Henan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tajikistan | target=Tajikistan vs Kyrgyzstan | candidate=Tajikistan vs Kyrgyzstan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Uwa Nedlands FC Reserves | target=Uwa Nedlands FC Reserves vs Inglewood United Reserves | candidate=Uwa Nedlands FC Reserves vs Inglewood United Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Horiyah | target=Al-Horiyah vs Al-Jaish SC (Syr) | candidate=Al-Horiyah vs Al-Jaish SC (Syr) | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Deportivo Capiata | target=Deportivo Capiata vs Club Fernando de La Mora | candidate=Deportivo Capiata vs Club Fernando de La Mora | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Rajasthan United | target=Rajasthan United vs Chanmari FC | candidate=Rajasthan United vs Chanmari FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tacuary Asuncion | target=Tacuary Asuncion vs Encarnacion FC | candidate=Tacuary Asuncion vs Encarnacion FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Northeast United FC | target=Northeast United FC vs Mohammedan SC | candidate=Northeast United FC vs Mohammedan SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Kahrabaa SC | target=Al Kahrabaa SC vs Al-Gharraf SC | candidate=Al Kahrabaa SC vs Al-Gharraf SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Diyala FC | target=Diyala FC vs Amanat Baghdad SC | candidate=Diyala FC vs Amanat Baghdad SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=MFK Zvolen | target=MFK Zvolen vs KFC Komarno | candidate=MFK Zvolen vs KFC Komarno | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ben Aknoun | target=Ben Aknoun vs ES Mostaganem | candidate=Ben Aknoun vs ES Mostaganem | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Klaipedos Fsm | target=Klaipedos Fsm vs Dfk Dainava Alytus | candidate=Klaipedos Fsm vs Dfk Dainava Alytus | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Rosario Central | target=CA Rosario Central vs UCV FC | candidate=CA Rosario Central vs UCV FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Coquimbo Unido | target=Coquimbo Unido vs CD Tolima | candidate=Coquimbo Unido vs CD Tolima | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Bournemouth'; best=0.0
- multi_odds_match: No multi-odds payload matched event 71500638
- multi_odds_match: No multi-odds payload matched event 68995160
- multi_odds_match: No multi-odds payload matched event 71465136
- multi_odds_match: No multi-odds payload matched event 71164846
- multi_odds_match: No multi-odds payload matched event 71357284
- multi_odds_match: No multi-odds payload matched event 71426270
- multi_odds_match: No multi-odds payload matched event 71489072
- multi_odds_match: No multi-odds payload matched event 71426268
- multi_odds_match: No multi-odds payload matched event 71553494