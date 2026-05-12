# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 3 / 8
Max discovery calls: 7
Events bookmaker: Bet365
Events discovery rows: 162
Events max pages: 4
Events lookahead days: 14
Max events per page/search: 100
Max priced events: 10
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 69195816, 71325526, 71111302, 61651664, 71372286, 67817690, 71348330, 67817692, 71240286, 67817694
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365,1xbet
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 162
Event selection diagnostic rows: 1575
Selected event rows: 10
Priced event rows: 10
Price rows: 10
Errors/status rows: 0

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 94
Latest x-ratelimit-reset: 2026-05-12T04:42:36Z
Latest retry-after: None

- 2026-05-12 07:30 | Canberra White Eagles FC vs Queanbeyan City FC | odds_api_io_Bet365_ML | 7.0/5.0/1.3
- 2026-05-12 08:45 | Brothers Union vs Mohammedan SC Dhaka | odds_api_io_Bet365_ML | 3.6/3.5/1.8
- 2026-05-12 09:45 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | odds_api_io_Bet365_ML | 8.0/5.0/1.27
- 2026-05-12 10:00 | FC Oleksandriya vs FC Zorya Luhansk | odds_api_io_Bet365_ML | 3.5/3.2/1.95
- 2026-05-12 10:30 | Cerro Porteno Asuncion vs Guarani Asuncion | odds_api_io_Bet365_ML | 2.1/3.8/2.7
- 2026-05-12 10:30 | Gangwon FC vs Daejeon Citizen FC | odds_api_io_Bet365_ML | 2.2/3.1/3.1
- 2026-05-12 10:30 | Gold Coast Knights vs Gold Coast United FC | odds_api_io_Bet365_ML | 1.083/9.5/21.0
- 2026-05-12 10:30 | Gwangju FC vs FC Seoul | odds_api_io_Bet365_ML | 8.0/4.2/1.38
- 2026-05-12 10:30 | Hellenic Athletic Club vs Darwin Hearts FC | odds_api_io_Bet365_ML | 3.3/4.2/1.75
- 2026-05-12 10:30 | Incheon United FC vs FC Pohang Steelers | odds_api_io_Bet365_ML | 2.45/3.0/2.875

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Incheon United FC | target=Incheon United FC vs FC Pohang Steelers | candidate=Incheon United FC vs FC Pohang Steelers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hellenic Athletic Club | target=Hellenic Athletic Club vs Darwin Hearts FC | candidate=Hellenic Athletic Club vs Darwin Hearts FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gwangju FC | target=Gwangju FC vs FC Seoul | candidate=Gwangju FC vs FC Seoul | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gold Coast Knights | target=Gold Coast Knights vs Gold Coast United FC | candidate=Gold Coast Knights vs Gold Coast United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gangwon FC | target=Gangwon FC vs Daejeon Citizen FC | candidate=Gangwon FC vs Daejeon Citizen FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Oleksandriya | target=FC Oleksandriya vs FC Zorya Luhansk | candidate=FC Oleksandriya vs FC Zorya Luhansk | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cerro Porteno Asuncion | target=Cerro Porteno Asuncion vs Guarani Asuncion | candidate=Cerro Porteno Asuncion vs Guarani Asuncion | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sunshine Coast Wanderers FC | target=Sunshine Coast Wanderers FC vs Eastern Suburbs FC | candidate=Sunshine Coast Wanderers FC vs Eastern Suburbs FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra White Eagles FC | target=Canberra White Eagles FC vs Queanbeyan City FC | candidate=Canberra White Eagles FC vs Queanbeyan City FC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Canberra White Eagles FC | target=Canberra White Eagles FC vs Queanbeyan City FC | candidate=Canberra White Eagles FC vs Queanbeyan City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Brothers Union | target=Brothers Union vs Mohammedan SC Dhaka | candidate=Brothers Union vs Mohammedan SC Dhaka | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hellenic Athletic Club | target=Hellenic Athletic Club vs Darwin Hearts FC | candidate=SC Internacional RS vs Athletic Club Sjdr MG | confidence=0.4586 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Brothers Union | target=Brothers Union vs Mohammedan SC Dhaka | candidate=Cerro Porteno Asuncion vs Guarani Asuncion | confidence=0.4492 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Hellenic Athletic Club | target=Hellenic Athletic Club vs Darwin Hearts FC | candidate=Al Nassr Club vs Al Hilal SFC | confidence=0.446 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Brothers Union | target=Brothers Union vs Mohammedan SC Dhaka | candidate=Mohun Bagan Super Giant vs Inter Kashi FC | confidence=0.4381 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=FC Oleksandriya | target=FC Oleksandriya vs FC Zorya Luhansk | candidate=Panaitolikos Agrinio vs AE Larissa FC | confidence=0.4361 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=FC Oleksandriya | target=FC Oleksandriya vs FC Zorya Luhansk | candidate=Boston Legacy FC vs Orlando Pride | confidence=0.4338 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Incheon United FC | target=Incheon United FC vs FC Pohang Steelers | candidate=Real Betis Seville vs Elche CF | confidence=0.4318 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Hellenic Athletic Club | target=Hellenic Athletic Club vs Darwin Hearts FC | candidate=Dunfermline Athletic FC vs Partick Thistle FC | confidence=0.4286 | selected=False | reason=below_min_event_match_confidence
- src=events_bookmaker_filtered | query=Incheon United FC | target=Incheon United FC vs FC Pohang Steelers | candidate=Canberra White Eagles FC vs Queanbeyan City FC | confidence=0.4265 | selected=False | reason=below_min_event_match_confidence