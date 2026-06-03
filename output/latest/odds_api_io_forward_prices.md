# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 7 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 112
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Hoo P R / Lai P J, Pakistan Panthers, Indonesia, Pakistan, France
Selected event IDs: 70867478, 71802536, 71814042, 69165652, 71621900, 71576338, 71576342, 71845998, 71601846, 70771306, 71719762, 71562038, 70314470, 69165654, 71846000, 69165770, 71859968, 71585576, 61906402, 61927922, 70771308, 61898678, 61466419, 68311642, 71600568, 71898554, 69921796, 69539704, 62274254, 67919706, 61466413, 61541458, 61898670, 71401950, 62274252, 62274262, 62274264, 68310938, 71463818, 71463918, 71829500, 71421934, 71304240, 68158898, 68158866, 71829502, 68158878, 71535110, 71797626, 71598620, 71550288, 67122996, 71399484, 69621688, 70993382, 71585580, 71355738, 71437544, 69091360, 68158888, 71546946, 69091366, 69091380, 71796106, 69091388, 69091390, 69091358, 69072358, 69091374, 69091400, 69091408, 68989248, 69091410, 67171968, 69091416, 71863252, 71792798, 71792536, 70673122, 68883304
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 138
Event selection diagnostic rows: 6134
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 7
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 57
Latest x-ratelimit-reset: 2026-06-03T03:42:26Z
Latest retry-after: None

- 2026-06-03 07:30 | Belconnen United FC vs Tuggeranong United FC | odds_api_io_Bet365_ML | 6.5/5.75/1.285
- 2026-06-03 08:15 | Broadmeadow Magic FC vs Maitland FC | odds_api_io_Bet365_ML | 41.0/17.0/1.03
- 2026-06-03 09:00 | Hawkesbury City SC vs Gladesville Ryde Magic | odds_api_io_Bet365_ML | 2.0/3.9/2.75
- 2026-06-03 09:00 | Portugal vs Kazakhstan | odds_api_io_Bet365_ML | 1.111/8.5/17.0
- 2026-06-03 09:00 | Sydney Olympic FC vs University of NSW | odds_api_io_Bet365_ML | 4.5/4.5/1.5
- 2026-06-03 09:30 | Rochedale Rovers vs Magic United Tfa | odds_api_io_Bet365_ML | 1.55/5.0/3.75
- 2026-06-03 09:30 | Sunshine Coast Wanderers vs St George Willawong FC | odds_api_io_Bet365_ML | 1.55/4.333/4.333
- 2026-06-03 11:00 | Nepal vs Bangladesh | odds_api_io_Bet365_ML | 1.7/3.6/4.0
- 2026-06-03 11:30 | Philippines vs Guam | odds_api_io_Bet365_ML | 1.045/13.0/34.0
- 2026-06-03 13:00 | Japan vs Portugal | odds_api_io_Bet365_ML | 4.5/3.6/1.615

## Event selection diagnostics

- src=events_search_fallback | query=Pakistan | target=Pakistan vs West Indies | candidate=Pakistan vs West Indies | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gibraltar | target=Gibraltar vs Virgin Islands, British | candidate=Gibraltar vs Virgin Islands, British | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=BK Olympic | target=BK Olympic vs Lunds BK | candidate=BK Olympic vs Lunds BK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SV Anthering | target=SV Anthering vs SV Burmoos | candidate=SV Anthering vs SV Burmoos | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Greenville Triumph SC | target=Greenville Triumph SC vs Forward Madison FC | candidate=Greenville Triumph SC vs Forward Madison FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Miami AC | target=Miami AC vs Weston FC | candidate=Miami AC vs Weston FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=GV Club Deportivo San Jose de Oruro | target=GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | candidate=GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hawkesbury City SC | target=Hawkesbury City SC vs Gladesville Ryde Magic | candidate=Hawkesbury City SC vs Gladesville Ryde Magic | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Boca Juniors | target=Boca Juniors vs Defensa Y Justicia Reserve | candidate=Boca Juniors vs Defensa Y Justicia Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Union FC Macomb | target=Union FC Macomb vs Midwest United FC | candidate=Union FC Macomb vs Midwest United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Annapolis Blues FC | target=Annapolis Blues FC vs Lionsbridge FC | candidate=Annapolis Blues FC vs Lionsbridge FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Capo FC | target=Capo FC vs Socal Reds FC | candidate=Capo FC vs Socal Reds FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gualaceo SC | target=Gualaceo SC vs Mushuc Runa SC | candidate=Gualaceo SC vs Mushuc Runa SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Broadmeadow Magic FC | target=Broadmeadow Magic FC vs Maitland FC | candidate=Broadmeadow Magic FC vs Maitland FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Portugal | target=Portugal vs Kazakhstan | candidate=Portugal vs Kazakhstan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Raja Casablanca Athletic | target=Raja Casablanca Athletic vs Rs Berkane | candidate=Raja Casablanca Athletic vs Rs Berkane | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Avai FC SC | target=Avai FC SC vs Chapecoense SC | candidate=Avai FC SC vs Chapecoense SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Groningen | target=FC Groningen vs de Graafschap | candidate=FC Groningen vs de Graafschap | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Wake FC | target=Wake FC vs South Carolina United Bantams | candidate=Wake FC vs South Carolina United Bantams | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Renaissance Zemamra | target=Renaissance Zemamra vs US Yacoub Mansour | candidate=Renaissance Zemamra vs US Yacoub Mansour | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71719762
- multi_odds_match: No multi-odds payload matched event 71562038
- multi_odds_match: No multi-odds payload matched event 70314470
- multi_odds_match: No multi-odds payload matched event 69165654
- multi_odds_match: No multi-odds payload matched event 71846000
- multi_odds_match: No multi-odds payload matched event 69165770
- multi_odds_match: No multi-odds payload matched event 71859968
- multi_odds_match: No multi-odds payload matched event 71585576
- multi_odds_match: No multi-odds payload matched event 61906402
- multi_odds_match: No multi-odds payload matched event 61927922