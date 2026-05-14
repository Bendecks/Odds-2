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
Events discovery rows: 320
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Valencia
Selected event IDs: 68311590, 71218680, 68310890, 70820616, 70820618, 69924662, 68311592, 68311594, 70648002, 71336696, 71339462, 71339460, 70448376, 70448378, 70774888, 70448380, 71370014, 70906776, 70774898, 61591358, 69757834, 71372084, 61591362, 70820614, 64200529, 67126094, 61591360, 61591372, 61591366, 61541420, 61902044, 71203972, 71456920, 71336698, 61898610, 70479362, 64055871, 71403928, 68158790, 71403932, 70162024, 67919260, 70929770, 70929772, 71403930, 70683966, 71312158, 67921068, 61894062, 68774142, 68377548, 71336700, 67953278, 67953286, 70844430, 69923670, 67919890, 71312160, 61624652, 70906778, 67953282, 64055877, 67953288, 67953276, 64055869, 68751762, 69688798, 68158782, 68158758, 68158762, 68158770, 68158774, 71296260, 69688800, 68158778, 61624646, 70844432, 69279792, 70379160
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 328
Event selection diagnostic rows: 22451
Selected event rows: 79
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 82
Latest x-ratelimit-reset: 2026-05-14T14:51:16Z
Latest retry-after: None

- 2026-05-14 14:00 | Angelholms FF vs Aatvidabergs FF | odds_api_io_Bet365_ML | 2.4/3.2/2.625
- 2026-05-14 14:00 | HB Torshavn vs Vikingur Gota | odds_api_io_Bet365_ML | 2.2/3.6/2.7
- 2026-05-14 14:00 | IF Karlstad Fotbol vs IFK Stocksund | odds_api_io_Bet365_ML | 1.285/5.25/6.5
- 2026-05-14 14:00 | IF Vestri vs Grotta | odds_api_io_Bet365_ML | 1.75/4.5/3.1
- 2026-05-14 14:00 | KA Akureyri vs KF Aegir | odds_api_io_Bet365_ML | 1.125/8.0/15.0
- 2026-05-14 14:00 | Kjp Kouvola vs Lautp | odds_api_io_Bet365_ML | 3.4/4.5/1.7
- 2026-05-14 14:00 | Trelleborgs FF vs Jonkopings Sodra IF | odds_api_io_Bet365_ML | 2.0/3.3/3.2
- 2026-05-14 14:00 | FC Trollhattan vs Ariana FC | odds_api_io_Bet365_ML | 2.75/3.7/2.1
- 2026-05-14 14:00 | VfL Wolfsburg vs Bayern Munich | odds_api_io_Bet365_ML | 4.5/3.9/1.55
- 2026-05-14 14:05 | Dhofar SCSC vs Al Shabab | odds_api_io_Bet365_ML | 3.7/3.3/1.85

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Al Nahda | target=Al Nahda vs Al-Seeb | candidate=Al Nahda vs Al-Seeb | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Sarmiento de Junin | target=CA Sarmiento de Junin vs San Lorenzo de Almagro Res. | candidate=CA Sarmiento de Junin vs San Lorenzo de Almagro Res. | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Lanus | target=CA Lanus vs Estudiantes de LP Reserve | candidate=CA Lanus vs Estudiantes de LP Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Samail SC | target=Samail SC vs Sohar | candidate=Samail SC vs Sohar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=ASKO Kottmannsdorf | target=ASKO Kottmannsdorf vs SV Dellach/Gail | candidate=ASKO Kottmannsdorf vs SV Dellach/Gail | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA River Plate (Arg) | target=CA River Plate (Arg) vs Instituto AC Cordoba Reserves | candidate=CA River Plate (Arg) vs Instituto AC Cordoba Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CS Sfaxien | target=CS Sfaxien vs ES Sahel | candidate=CS Sfaxien vs ES Sahel | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=POFC Botev Vratsa | target=POFC Botev Vratsa vs PFC Montana 1921 | candidate=POFC Botev Vratsa vs PFC Montana 1921 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IF Vestri | target=IF Vestri vs Grotta | candidate=IF Vestri vs Grotta | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=First Vienna FC 1894 | target=First Vienna FC 1894 vs Schwarz-Weiss Bregenz | candidate=First Vienna FC 1894 vs Schwarz-Weiss Bregenz | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Nir Ramat Hasharon | target=Hapoel Nir Ramat Hasharon vs Maccabi Kishronot Hadera | candidate=Hapoel Nir Ramat Hasharon vs Maccabi Kishronot Hadera | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=KA Akureyri | target=KA Akureyri vs KF Aegir | candidate=KA Akureyri vs KF Aegir | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Ittifaq FC | target=Al-Ittifaq FC vs Al-Ittihad Club | candidate=Al-Ittifaq FC vs Al-Ittihad Club | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Thun | target=FC Thun vs Young Boys Bern | candidate=FC Thun vs Young Boys Bern | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Urartu Yerevan | target=FC Urartu Yerevan vs FC Noah Yerevan | candidate=FC Urartu Yerevan vs FC Noah Yerevan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CE Juventude de Estancia SE | target=CE Juventude de Estancia SE vs EC Vitoria BA | candidate=CE Juventude de Estancia SE vs EC Vitoria BA | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fylkir Reykjavik | target=Fylkir Reykjavik vs FH Hafnarfjordur | candidate=Fylkir Reykjavik vs FH Hafnarfjordur | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Always Ready | target=Always Ready vs The Strongest | candidate=Always Ready vs The Strongest | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD Godoy Cruz | target=CD Godoy Cruz vs Gimnasia de Mendoza Reserve | candidate=CD Godoy Cruz vs Gimnasia de Mendoza Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=America FC MG | target=America FC MG vs EC Bahia BA | candidate=America FC MG vs EC Bahia BA | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Valencia'; best=0.5979
- multi_odds_match: No multi-odds payload matched event 71339462
- multi_odds_match: No multi-odds payload matched event 71339460
- multi_odds_match: No multi-odds payload matched event 70448376
- multi_odds_match: No multi-odds payload matched event 70448378
- multi_odds_match: No multi-odds payload matched event 70774888
- multi_odds_match: No multi-odds payload matched event 70448380
- multi_odds_match: No multi-odds payload matched event 71370014
- multi_odds_match: No multi-odds payload matched event 70906776
- multi_odds_match: No multi-odds payload matched event 70774898