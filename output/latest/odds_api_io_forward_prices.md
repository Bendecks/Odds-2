# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 8 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 240
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Bournemouth, Bournemouth, Charleroi, Genk, Westerlo
Selected event IDs: 71344708, 71218292, 71344710, 71360374, 71238550, 69923680, 70929780, 70929778, 70929782, 69924108, 71523836, 70929784, 67919906, 71579002, 71579010, 71553430, 71344712, 71553498, 71553500, 71500640, 71500642, 71218290, 71218286, 67126100, 67921076, 70812414, 70812412, 70812416, 71477636, 71001772, 69090916, 68158802, 68158822, 68158812, 69688810, 68158816, 68158808, 68158828, 69688866, 61301247, 71579006, 70207506, 70207508, 71540168, 70207504, 71579014, 71344714, 71426272, 71173724, 68751804, 70075272, 70076108, 70075680, 70075712, 71506796, 70075248, 71577480, 71354860, 69090918, 68971756, 71216944, 70076022, 70075784, 71216948, 70075750, 70075172, 71577482, 69090926, 70075102, 70075200, 70076106, 68532510, 71564480, 71550354, 69195330
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 242
Event selection diagnostic rows: 16193
Selected event rows: 75
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 8
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 50
Latest x-ratelimit-reset: 2026-05-19T15:34:23Z
Latest retry-after: None

- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem | odds_api_io_Bet365_ML | 1.285/5.0/8.5
- 2026-05-19 15:00 | Klaipedos Fsm vs Dfk Dainava Alytus | odds_api_io_Bet365_ML | 5.5/4.0/1.45
- 2026-05-19 15:00 | MB Rouissat vs Paradou AC | odds_api_io_Bet365_ML | 1.95/3.0/3.6
- 2026-05-19 15:00 | FC Noah Yerevan vs Ararat Yerevan FC | odds_api_io_Bet365_ML | 1.125/9.0/11.0
- 2026-05-19 15:00 | Velez Nevesinje vs FK Vlasenica | odds_api_io_Bet365_ML | 1.42/4.1/6.5
- 2026-05-19 16:00 | FC Haka J vs Saaksjaerven Loiske | odds_api_io_Bet365_ML | 1.071/13.0/19.0
- 2026-05-19 16:00 | Hapoel Acre FC vs Hapoel Hadera FC | odds_api_io_Bet365_ML | 1.666/3.4/4.333
- 2026-05-19 16:00 | Hapoel Nof Hagalil FC vs Ironi Modiin | odds_api_io_Bet365_ML | 2.625/3.0/2.45
- 2026-05-19 16:00 | Hapoel Ra`anana FC vs FC Kafr Qasim | odds_api_io_Bet365_ML | 3.3/3.3/1.95
- 2026-05-19 16:00 | FC Kiisto vs Vpv | odds_api_io_Bet365_ML | 1.27/5.75/7.5

## Event selection diagnostics

- src=events_bookmaker_filtered | query=FC Noah Yerevan | target=FC Noah Yerevan vs Ararat Yerevan FC | candidate=FC Noah Yerevan vs Ararat Yerevan FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CSD Independiente del Valle | target=CSD Independiente del Valle vs Libertad Asuncion | candidate=CSD Independiente del Valle vs Libertad Asuncion | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sydney Olympic FC | target=Sydney Olympic FC vs University of NSW | candidate=Sydney Olympic FC vs University of NSW | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Velez Nevesinje | target=Velez Nevesinje vs FK Vlasenica | candidate=Velez Nevesinje vs FK Vlasenica | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Banfield | target=CA Banfield vs CA Aldosivi Reserve | candidate=CA Banfield vs CA Aldosivi Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Boston Bolts | target=Boston Bolts vs Vermont Green FC | candidate=Boston Bolts vs Vermont Green FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Be`er Sheva FC | target=Hapoel Be`er Sheva FC vs Maccabi Tel Aviv FC | candidate=Hapoel Be`er Sheva FC vs Maccabi Tel Aviv FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Barra FC SC | target=Barra FC SC vs Concordia SC | candidate=Barra FC SC vs Concordia SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Cuenca | target=CD Cuenca vs Recoleta FC | candidate=CD Cuenca vs Recoleta FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Haka J | target=FC Haka J vs Saaksjaerven Loiske | candidate=FC Haka J vs Saaksjaerven Loiske | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=America de Cali | target=America de Cali vs CA Tigre | candidate=America de Cali vs CA Tigre | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Midlakes United | target=Midlakes United vs FC Olympia | candidate=Midlakes United vs FC Olympia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Acre FC | target=Hapoel Acre FC vs Hapoel Hadera FC | candidate=Hapoel Acre FC vs Hapoel Hadera FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ellerton FC | target=Ellerton FC vs Paradise SC | candidate=Ellerton FC vs Paradise SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Nof Hagalil FC | target=Hapoel Nof Hagalil FC vs Ironi Modiin | candidate=Hapoel Nof Hagalil FC vs Ironi Modiin | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sao Paulo FC SP | target=Sao Paulo FC SP vs Millonarios FC | candidate=Sao Paulo FC SP vs Millonarios FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Ra`anana FC | target=Hapoel Ra`anana FC vs FC Kafr Qasim | candidate=Hapoel Ra`anana FC vs FC Kafr Qasim | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Boca Juniors | target=Boca Juniors vs Cruzeiro EC MG | candidate=Boca Juniors vs Cruzeiro EC MG | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Kiisto | target=FC Kiisto vs Vpv | candidate=FC Kiisto vs Vpv | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Helsingborgs IF | target=Helsingborgs IF vs Varbergs BoIS | candidate=Helsingborgs IF vs Varbergs BoIS | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Bournemouth'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Bournemouth'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Charleroi'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Genk'; best=0.467
- event_selection: No event above confidence 0.72 for query 'Westerlo'; best=0.4425
- multi_odds_match: No multi-odds payload matched event 71523836
- multi_odds_match: No multi-odds payload matched event 70929784
- multi_odds_match: No multi-odds payload matched event 67919906
- multi_odds_match: No multi-odds payload matched event 71579002
- multi_odds_match: No multi-odds payload matched event 71579010