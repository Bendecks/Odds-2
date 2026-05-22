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
Events discovery rows: 560
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 69460618, 69910660, 68160938, 62083190, 68050986, 68049806, 68664056, 68160172, 68161708, 68160164, 67878242, 68160168, 68161714, 68161710, 69342862, 67692248, 62036902, 67807828, 67692252, 67692250, 62036918, 68051612, 68160564, 68161712, 67645564, 68162386, 68049808, 68050990, 71127908, 69115208, 69910662, 68664058, 69910930, 69910928, 69910926, 69910664, 69910932, 63637935, 69342864, 62083200, 68663486, 70906798, 71594326, 63637939, 70571044, 63637937, 63185785, 70479406, 62161268, 69342866, 67920628, 61286609, 71186824, 71186826, 71186828, 68492538, 70906796, 70906794, 70708886, 62036296, 70906792, 67790442, 69920644, 70479408, 62037524, 71589682, 69924674, 67845760, 71183116, 67604820, 62036298, 63185791, 68538256, 70683976, 71037644, 70318296, 69670720, 69670722, 69670724, 61737344
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 560
Event selection diagnostic rows: 41640
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 59
Latest x-ratelimit-reset: 2026-05-22T03:10:33Z
Latest retry-after: None

- 2026-05-22 07:00 | Auckland FC Reserves vs Eastern Suburbs AFC | odds_api_io_Bet365_ML | 4.5/4.333/1.5
- 2026-05-22 07:00 | Dalian Yingbo B vs Taian Tiankuang | odds_api_io_Bet365_ML | 3.6/2.875/2.05
- 2026-05-22 08:15 | Northcote City FC vs Brunswick City SC | odds_api_io_Bet365_ML | 1.38/5.0/5.25
- 2026-05-22 08:30 | Arema FC vs Psim Yogyakarta | odds_api_io_Bet365_ML | 2.1/3.8/2.8
- 2026-05-22 08:30 | West Adelaide Reserve vs Flinders United Wfc Reserves | odds_api_io_Bet365_ML | 1.181/6.5/9.0
- 2026-05-22 08:45 | Salisbury Inter vs Adelaide Comets FC | odds_api_io_Bet365_ML | 2.0/3.6/3.0
- 2026-05-22 09:00 | Ho Chi Minh City FC vs Truong Tuoi Dong Nai FC | odds_api_io_Bet365_ML | 8.0/5.0/1.285
- 2026-05-22 09:30 | Bentleigh Greens vs Caroline Springs George Cross FC | odds_api_io_Bet365_ML | 2.55/3.4/2.4
- 2026-05-22 09:30 | Box Hill United FC vs Springvale White Eagles | odds_api_io_Bet365_ML | 2.0/3.7/2.9
- 2026-05-22 09:30 | Green Gully SC vs Heidelberg United FC | odds_api_io_Bet365_ML | 8.5/5.5/1.25

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Wenzhou Professional FC | target=Wenzhou Professional FC vs Guangdong Mingtu | candidate=Wenzhou Professional FC vs Guangdong Mingtu | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=West Adelaide Reserve | target=West Adelaide Reserve vs Flinders United Wfc Reserves | candidate=West Adelaide Reserve vs Flinders United Wfc Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Altai Oskemen | target=FC Altai Oskemen vs FC Okzhetpes | candidate=FC Altai Oskemen vs FC Okzhetpes | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Eastern United | target=Eastern United vs Adelaide Blue Eagles | candidate=Eastern United vs Adelaide Blue Eagles | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Mindil Aces | target=Mindil Aces vs Garuda FC | candidate=Mindil Aces vs Garuda FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Young Africans SC | target=Young Africans SC vs Singida Black Stars SC | candidate=Young Africans SC vs Singida Black Stars SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Aarhus Fremad | target=Aarhus Fremad vs Aalborg BK | candidate=Aarhus Fremad vs Aalborg BK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=West Torrens Birkalla | target=West Torrens Birkalla vs Modbury Vista | candidate=West Torrens Birkalla vs Modbury Vista | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sokol Kolbuszowa Dolna | target=Sokol Kolbuszowa Dolna vs Wislanie Skawina | candidate=Sokol Kolbuszowa Dolna vs Wislanie Skawina | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gornik Zabrze II | target=Gornik Zabrze II vs KS Gornik Polkowice | candidate=Gornik Zabrze II vs KS Gornik Polkowice | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Eltham Redbacks FC | target=Eltham Redbacks FC vs Melbourne Victory | candidate=Eltham Redbacks FC vs Melbourne Victory | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=NK Kustosija Zagreb | target=NK Kustosija Zagreb vs NK Uljanik | candidate=NK Kustosija Zagreb vs NK Uljanik | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lanzhou Longyuan Athletic | target=Lanzhou Longyuan Athletic vs Dalian Kewei | candidate=Lanzhou Longyuan Athletic vs Dalian Kewei | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Zaqatala FK | target=Zaqatala FK vs Safa | candidate=Zaqatala FK vs Safa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kongsvinger IL Toppfotball 2 | target=Kongsvinger IL Toppfotball 2 vs Tromsoe 2 | candidate=Kongsvinger IL Toppfotball 2 vs Tromsoe 2 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Maitland FC | target=Maitland FC vs Newcastle Olympic FC | candidate=Maitland FC vs Newcastle Olympic FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Shahdag Qusar FK | target=Shahdag Qusar FK vs Baku Sporting | candidate=Shahdag Qusar FK vs Baku Sporting | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Septemvri Sofia | target=FK Septemvri Sofia vs PFC Dobrudzha Dobrich | candidate=FK Septemvri Sofia vs PFC Dobrudzha Dobrich | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Moreton City Excelsior FC | target=Moreton City Excelsior FC vs Brisbane City FC | candidate=Moreton City Excelsior FC vs Brisbane City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Salisbury Inter | target=Salisbury Inter vs Adelaide Comets FC | candidate=Salisbury Inter vs Adelaide Comets FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 67878242
- multi_odds_match: No multi-odds payload matched event 68160168
- multi_odds_match: No multi-odds payload matched event 68161714
- multi_odds_match: No multi-odds payload matched event 68161710
- multi_odds_match: No multi-odds payload matched event 69342862
- multi_odds_match: No multi-odds payload matched event 67692248
- multi_odds_match: No multi-odds payload matched event 62036902
- multi_odds_match: No multi-odds payload matched event 67807828
- multi_odds_match: No multi-odds payload matched event 67692252
- multi_odds_match: No multi-odds payload matched event 67692250