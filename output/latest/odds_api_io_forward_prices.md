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
Events discovery rows: 650
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Celtic, Falkirk, Hibernian, Sociedad B, Bayern Munich, Ein Frankfurt, Freiburg, Heidenheim, Leverkusen
Selected event IDs: 70232102, 66886788, 71459880, 67681864, 68687652, 71478624, 68097900, 68822896, 71220890, 66886790, 70320270, 68156614, 68156616, 67119316, 66886778, 67844000, 67844006, 71495712, 69255022, 69255026, 67912070, 71501266, 70319970, 71422912, 70881726, 71307978, 62509066, 71507330, 67844002, 69090836, 70322106, 71307980, 69090842, 67844004, 69090876, 66299176, 68822902, 66299178, 67844008, 66299182, 66299184, 66299186, 66299188, 70893864, 68687644
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 659
Event selection diagnostic rows: 51013
Selected event rows: 45
Priced event rows: 9
Price rows: 9
Errors/status rows: 45

## Provider rate-limit headers

Header rows captured: 14
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 36
Latest x-ratelimit-reset: 2026-05-16T21:38:06Z
Latest retry-after: None

- 2026-05-16 21:30 | Atletico Mineiro MG vs Mirassol FC SP | odds_api_io_Bet365_ML | 1.95/3.3/4.1
- 2026-05-16 21:30 | CA Penarol Montevideo vs Liverpool Montevideo | odds_api_io_Bet365_ML | 1.85/3.3/4.1
- 2026-05-16 21:30 | CD O´Higgins vs Universidad de Concepcion | odds_api_io_Bet365_ML | 1.533/4.2/5.5
- 2026-05-16 21:30 | CD Universidad Catolica del Ecuador vs Delfin SC | odds_api_io_Bet365_ML | 1.42/4.333/6.5
- 2026-05-16 21:30 | Cerro Porteno vs Recoleta FC | odds_api_io_Bet365_ML | 1.015/23.0/51.0
- 2026-05-16 21:30 | Curico Unido vs Santiago Wanderers | odds_api_io_Bet365_ML | 1.85/3.5/3.4
- 2026-05-16 21:30 | Goias EC GO vs Botafogo FC SP | odds_api_io_Bet365_ML | 1.95/2.9/3.75
- 2026-05-16 21:30 | New Jersey United AC vs Jackson Lions FC | odds_api_io_Bet365_ML | 2.05/3.8/2.75
- 2026-05-16 21:30 | SC Internacional RS vs CR Vasco da Gama RJ | odds_api_io_Bet365_ML | 1.909/3.4/4.333

## Event selection diagnostics

- src=events_bookmaker_filtered | query=CD O´Higgins | target=CD O´Higgins vs Universidad de Concepcion | candidate=CD O´Higgins vs Universidad de Concepcion | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lagarto FC SE | target=Lagarto FC SE vs CS Sergipe SE | candidate=Lagarto FC SE vs CS Sergipe SE | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Brooklyn FC | target=Brooklyn FC vs Hartford Athletic | candidate=Brooklyn FC vs Hartford Athletic | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Universidad Catolica del Ecuador | target=CD Universidad Catolica del Ecuador vs Delfin SC | candidate=CD Universidad Catolica del Ecuador vs Delfin SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=One Knoxville SC | target=One Knoxville SC vs San Antonio FC | candidate=One Knoxville SC vs San Antonio FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Atletico Mineiro MG | target=Atletico Mineiro MG vs Mirassol FC SP | candidate=Atletico Mineiro MG vs Mirassol FC SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Point Michel | target=Point Michel vs Middleham United FC | candidate=Point Michel vs Middleham United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CT United FC | target=CT United FC vs Toronto FC II | candidate=CT United FC vs Toronto FC II | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cerro Porteno | target=Cerro Porteno vs Recoleta FC | candidate=Cerro Porteno vs Recoleta FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Barcelona SC | target=Barcelona SC vs SD Aucas | candidate=Barcelona SC vs SD Aucas | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA River Plate (ARG) | target=CA River Plate (ARG) vs CA Rosario Central | candidate=CA River Plate (ARG) vs CA Rosario Central | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Richmond Kickers | target=Richmond Kickers vs Charleston Battery | candidate=Richmond Kickers vs Charleston Battery | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cuiaba EC MT | target=Cuiaba EC MT vs Gremio Novorizontino SP | candidate=Cuiaba EC MT vs Gremio Novorizontino SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Weston FC | target=Weston FC vs Fort Lauderdale United FC | candidate=Weston FC vs Fort Lauderdale United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Chattanooga Red Wolves SC | target=Chattanooga Red Wolves SC vs Birmingham Legion FC | candidate=Chattanooga Red Wolves SC vs Birmingham Legion FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Curico Unido | target=Curico Unido vs Santiago Wanderers | candidate=Curico Unido vs Santiago Wanderers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Floresta EC CE | target=Floresta EC CE vs Amazonas FC AM | candidate=Floresta EC CE vs Amazonas FC AM | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Forward Madison FC | target=Forward Madison FC vs Detroit City FC | candidate=Forward Madison FC vs Detroit City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fort Wayne FC | target=Fort Wayne FC vs Indy Eleven | candidate=Fort Wayne FC vs Indy Eleven | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=DC United | target=DC United vs Saint Louis City SC | candidate=DC United vs Saint Louis City SC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Celtic'; best=0.58
- event_selection: No event above confidence 0.72 for query 'Falkirk'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Hibernian'; best=0.5281
- event_selection: No event above confidence 0.72 for query 'Sociedad B'; best=0.3153
- event_selection: No event above confidence 0.72 for query 'Bayern Munich'; best=0.4976
- event_selection: No event above confidence 0.72 for query 'Ein Frankfurt'; best=0.4596
- event_selection: No event above confidence 0.72 for query 'Freiburg'; best=0.5012
- event_selection: No event above confidence 0.72 for query 'Heidenheim'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Leverkusen'; best=0.6432
- odds_parse: No 1X2 odds found in multi-odds payload for event 70232102