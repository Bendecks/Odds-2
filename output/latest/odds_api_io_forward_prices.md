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
Events discovery rows: 675
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 71454736, 69460606, 71465054, 67693536, 67808456, 70968242, 68162372, 68160934, 68160922, 67905666, 70968246, 62083172, 62204956, 61974264, 69165688, 67878238, 68161886, 67878230, 71240192, 68160142, 68161694, 67807822, 67692234, 67807380, 70926670, 70090086, 70090088, 68161704, 67691594, 68160146, 67903672, 68161696, 67903674, 69767360, 68663472, 68664046, 70090090, 69767598, 70969284, 70968250, 71474752, 70968262, 61974266, 68995142, 68995140, 68995144, 68995146, 68995148, 67343112, 70995260, 70995264, 68042490, 71357268, 70929720, 70926672, 71056744, 63185777, 71492822, 70929774, 70929716, 70929718, 70929714, 70812408, 70929776, 63637923, 70962958, 69972728, 71453928, 70556720, 67018386, 62067454, 62067450, 62067446, 62067458, 62067452, 62067456, 62067448, 71468302, 71468304, 71339470
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 670
Event selection diagnostic rows: 50840
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 58
Latest x-ratelimit-reset: 2026-05-15T03:04:15Z
Latest retry-after: None

- 2026-05-15 03:10 | CF Monterrey vs Club America | odds_api_io_Bet365_ML | 4.333/3.7/1.6
- 2026-05-15 07:00 | Auckland FC Reserves vs Auckland City FC | odds_api_io_Bet365_ML | 4.5/4.5/1.48
- 2026-05-15 07:30 | Kyrgyzstan vs Turkmenistan | odds_api_io_Bet365_ML | 3.0/3.2/2.15
- 2026-05-15 08:00 | Hurstville FC vs Prospect United | odds_api_io_Bet365_ML | 4.333/4.333/1.533
- 2026-05-15 08:00 | Maitland FC Reserve vs Cooks Hill United FC Reserve | odds_api_io_Bet365_ML | 2.9/3.9/1.909
- 2026-05-15 08:00 | Shenzhen 2028 FC vs Shaanxi Union FC | odds_api_io_Bet365_ML | 6.0/4.0/1.533
- 2026-05-15 08:15 | Bentleigh Greens SC vs Heidelberg United FC | odds_api_io_Bet365_ML | 29.0/15.0/1.04
- 2026-05-15 08:15 | Melbourne Knights FC vs Eltham Redbacks FC | odds_api_io_Bet365_ML | 1.8/4.5/3.0
- 2026-05-15 08:15 | Northcote City FC vs FC Bulleen Lions | odds_api_io_Bet365_ML | 2.75/4.2/1.95
- 2026-05-15 08:30 | Caboolture Sports FC vs North Star | odds_api_io_Bet365_ML | 2.7/3.9/2.0

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Maitland FC Reserve | target=Maitland FC Reserve vs Cooks Hill United FC Reserve | candidate=Maitland FC Reserve vs Cooks Hill United FC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dandenong City SC | target=Dandenong City SC vs Oakleigh Cannons | candidate=Dandenong City SC vs Oakleigh Cannons | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CF Monterrey | target=CF Monterrey vs Club America | candidate=CF Monterrey vs Club America | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dalian Yingbo FC | target=Dalian Yingbo FC vs Qingdao West Coast FC | candidate=Dalian Yingbo FC vs Qingdao West Coast FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kingston City FC | target=Kingston City FC vs Eastern Lions SC | candidate=Kingston City FC vs Eastern Lions SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Nunawading City | target=Nunawading City vs Whittlesea United SC | candidate=Nunawading City vs Whittlesea United SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Caboolture Sports FC | target=Caboolture Sports FC vs North Star | candidate=Caboolture Sports FC vs North Star | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Kfar Saba FC | target=Hapoel Kfar Saba FC vs Maccabi Petah Tikva FC | candidate=Hapoel Kfar Saba FC vs Maccabi Petah Tikva FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bentleigh Greens SC | target=Bentleigh Greens SC vs Heidelberg United FC | candidate=Bentleigh Greens SC vs Heidelberg United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hurstville FC | target=Hurstville FC vs Prospect United | candidate=Hurstville FC vs Prospect United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Balcatta FC | target=Balcatta FC vs Fremantle City FC | candidate=Balcatta FC vs Fremantle City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bunga Raya FC | target=Bunga Raya FC vs Malaysia University | candidate=Bunga Raya FC vs Malaysia University | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Blacktown Spartans | target=Blacktown Spartans vs Bull FC Academy | candidate=Blacktown Spartans vs Bull FC Academy | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Slovakia | target=Slovakia vs San Marino | candidate=Slovakia vs San Marino | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Majd FC | target=Majd FC vs AL Jazira AL Hamra | candidate=Majd FC vs AL Jazira AL Hamra | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Arabi (UAE) | target=AL Arabi (UAE) vs Gulf United | candidate=AL Arabi (UAE) vs Gulf United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Henan | target=Henan vs Shenzhen Peng City | candidate=Henan vs Shenzhen Peng City | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Caboolture FC | target=Caboolture FC vs North Star FC | candidate=Caboolture FC vs North Star FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hangzhou Linping Wuyue | target=Hangzhou Linping Wuyue vs Foshan Nanshi FC | candidate=Hangzhou Linping Wuyue vs Foshan Nanshi FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bnei Yehuda Tel Aviv FC | target=Bnei Yehuda Tel Aviv FC vs MS Football Hapoel Kiryat Yam | candidate=Bnei Yehuda Tel Aviv FC vs MS Football Hapoel Kiryat Yam | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 70968246
- multi_odds_match: No multi-odds payload matched event 62083172
- multi_odds_match: No multi-odds payload matched event 62204956
- multi_odds_match: No multi-odds payload matched event 61974264
- multi_odds_match: No multi-odds payload matched event 69165688
- multi_odds_match: No multi-odds payload matched event 67878238
- multi_odds_match: No multi-odds payload matched event 68161886
- multi_odds_match: No multi-odds payload matched event 67878230
- multi_odds_match: No multi-odds payload matched event 71240192
- multi_odds_match: No multi-odds payload matched event 68160142