# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 4 / 8
Max discovery calls: 7
Events bookmaker: Bet365
Events discovery rows: 136
Events max pages: 4
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 30
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Sur SC
Selected event IDs: 71338854, 71338856, 70906728, 71228890, 68492514, 71372082, 61651662, 71231390, 61651650, 62036882, 71085582, 71338858, 71085578, 71085580, 70232094, 71328286, 70232096, 71421816, 68492516, 71216798, 71338146, 64055855, 71336690, 71344696, 71401082, 70430016, 71378882, 70812400, 67126090, 71336688
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: 
Selected markets: 
Fixture rows: 136
Event selection diagnostic rows: 3675
Selected event rows: 30
Priced event rows: 0
Price rows: 0
Errors/status rows: 1

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 88
Latest x-ratelimit-reset: 2026-05-12T15:01:13Z
Latest retry-after: None


## Event selection diagnostics

- src=events_bookmaker_filtered | query=Modena FC | target=Modena FC vs Juve Stabia | candidate=Modena FC vs Juve Stabia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=JS Omrane | target=JS Omrane vs Avenir S Marsa | candidate=JS Omrane vs Avenir S Marsa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Metalist 1925 Kharkiv | target=FC Metalist 1925 Kharkiv vs Karpaty Lviv | candidate=FC Metalist 1925 Kharkiv vs Karpaty Lviv | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Kholood | target=Al-Kholood vs Al-Okhdood Club | candidate=Al-Kholood vs Al-Okhdood Club | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Asteras Tripolis | target=Asteras Tripolis vs Panserraikos | candidate=Asteras Tripolis vs Panserraikos FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Veres Rivne | target=Veres Rivne vs FC Kryvbas Kriviy Rih | candidate=Veres Rivne vs FC Kryvbas Kriviy Rih | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=MFK Chrudim | target=MFK Chrudim vs FK Pribram | candidate=MFK Chrudim vs FK Pribram | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Rustaq | target=Al-Rustaq vs Ibri | candidate=Al-Rustaq vs Ibri | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Liepaja | target=FK Liepaja vs Ogre United | candidate=FK Liepaja vs Ogre United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Samger FC | target=Samger FC vs Real de Banjul | candidate=Samger FC vs Real de Banjul | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Zlin | target=FC Zlin vs FK Teplice | candidate=FC Zlin vs FK Teplice | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Ittihad Kalba | target=AL Ittihad Kalba vs AL Nasr | candidate=AL Ittihad Kalba vs AL Nasr | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Wasl | target=AL Wasl vs AL Jazira | candidate=AL Wasl vs AL Jazira | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Tel Aviv FC | target=Hapoel Tel Aviv FC vs Hapoel Petah Tikva FC | candidate=Hapoel Tel Aviv FC vs Hapoel Petah Tikva FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Mlada Boleslav | target=FK Mlada Boleslav vs Dukla Prague | candidate=FK Mlada Boleslav vs Dukla Prague | confidence=1.0 | selected=True | reason=
- src=events_search_fallback | query=Sur SC | target=Sur SC vs Al-Khaboora | candidate=Sur SC vs Al-Khaboora | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Varnamo | target=IFK Varnamo vs Orebro SK | candidate=IFK Varnamo vs Orebro SK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Central Espanol Reserve | target=Central Espanol Reserve vs Defensor Sporting | candidate=Central Espanol Reserve vs Defensor Sporting | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Elva | target=FC Elva vs Paide Linnameeskond | candidate=FC Elva vs Paide Linnameeskond | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AE Kifisia FC | target=AE Kifisia FC vs Atromitos Athinon | candidate=AE Kifisia FC vs Atromitos Athinon | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_request_or_parse: RuntimeError('HTTP 500: {"error":"Failed to check event existence"}')