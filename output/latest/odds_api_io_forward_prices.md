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
Events discovery rows: 322
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: TRA United
Selected event IDs: 68310888, 70774892, 67919620, 67563266, 67915572, 68320174, 67921064, 67919258, 70683964, 67921056, 71423498, 70945796, 63637929, 69491788, 70479356, 70945864, 67915824, 70267784, 68311590, 71218680, 68310890, 70820616, 70820618, 69924662, 68311592, 68311594, 70648002, 71336696, 71339462, 71339460, 70448376, 70448378, 70774888, 70448380, 71370014, 70906776, 70774898, 61591358, 69757834, 71372084, 61591362, 70820614, 64200529, 67126094, 61591360, 61591372, 61591366, 61541420, 61902044, 71203972, 71456920, 71336698, 61898610, 70479362, 64055871, 71403928, 68158790, 71403932, 70162024, 67919260, 70929770, 70929772, 71403930, 70683966, 71312158, 67921068, 61894062, 68774142, 68377548, 71336700, 67953278, 67953286, 70844430, 69923670, 67919890, 71312160, 61624652, 70906778, 67953282
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 323
Event selection diagnostic rows: 22667
Selected event rows: 79
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 82
Latest x-ratelimit-reset: 2026-05-14T13:40:05Z
Latest retry-after: None

- 2026-05-14 13:00 | Assyriska FF vs Umea FC | odds_api_io_Bet365_ML | 2.75/3.3/2.25
- 2026-05-14 13:00 | Fauve Azur de Yaounde vs Gazelle FA de Garoua | odds_api_io_Bet365_ML | 4.2/3.3/1.727
- 2026-05-14 13:00 | Fk Kvik Trondheim vs Strindheim TF | odds_api_io_Bet365_ML | 2.9/4.2/1.9
- 2026-05-14 13:00 | Herentals FC vs Dynamos Harare FC | odds_api_io_Bet365_ML | 2.1/2.75/3.6
- 2026-05-14 13:00 | Hoenefoss BK vs Stjordals-Blink | odds_api_io_Bet365_ML | 1.4/4.333/5.75
- 2026-05-14 13:00 | Lidkopings FK vs Grebbestads IF | odds_api_io_Bet365_ML | 2.0/3.75/2.9
- 2026-05-14 13:00 | Lillehammer FK vs FK Gjoevik-Lyn | odds_api_io_Bet365_ML | 2.0/4.0/2.7
- 2026-05-14 13:00 | Lokomotiv Oslo vs FK Union Carl Berner | odds_api_io_Bet365_ML | 2.35/4.1/2.25
- 2026-05-14 13:00 | Masku vs LTU | odds_api_io_Bet365_ML | 1.45/4.75/4.5
- 2026-05-14 13:00 | Raelingen vs Brumunddal Fotball | odds_api_io_Bet365_ML | 1.6/4.333/3.9

## Event selection diagnostics

- src=events_bookmaker_filtered | query=FC Urartu Yerevan | target=FC Urartu Yerevan vs FC Noah Yerevan | candidate=FC Urartu Yerevan vs FC Noah Yerevan | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Thun | target=FC Thun vs Young Boys Bern | candidate=FC Thun vs Young Boys Bern | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AL Draih | target=AL Draih vs Al Bukiryah | candidate=AL Draih vs Al Bukiryah | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kjp Kouvola | target=Kjp Kouvola vs Lautp | candidate=Kjp Kouvola vs Lautp | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Lokomotiv Oslo | target=Lokomotiv Oslo vs FK Union Carl Berner | candidate=Lokomotiv Oslo vs FK Union Carl Berner | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hapoel Nir Ramat Hasharon | target=Hapoel Nir Ramat Hasharon vs Maccabi Kishronot Hadera | candidate=Hapoel Nir Ramat Hasharon vs Maccabi Kishronot Hadera | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Herentals FC | target=Herentals FC vs Dynamos Harare FC | candidate=Herentals FC vs Dynamos Harare FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Trelleborgs FF | target=Trelleborgs FF vs Jonkopings Sodra IF | candidate=Trelleborgs FF vs Jonkopings Sodra IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Orobah | target=Al-Orobah vs AL Anwar | candidate=Al-Orobah vs AL Anwar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hoenefoss BK | target=Hoenefoss BK vs Stjordals-Blink | candidate=Hoenefoss BK vs Stjordals-Blink | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Arborg | target=Arborg vs Alafoss | candidate=Arborg vs Alafoss | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AS Fortuna | target=AS Fortuna vs Coton Sport de Garoua | candidate=AS Fortuna vs Coton Sport de Garoua | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=POFC Botev Vratsa | target=POFC Botev Vratsa vs PFC Montana 1921 | candidate=POFC Botev Vratsa vs PFC Montana 1921 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fish United | target=Fish United vs NOPS | candidate=Fish United vs NOPS | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Masku | target=Masku vs LTU | candidate=Masku vs LTU | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ironi Modiin | target=Ironi Modiin vs Hapoel Acre FC | candidate=Ironi Modiin vs Hapoel Acre FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Wehda FC | target=Al-Wehda FC vs Al-Jabalain | candidate=Al-Wehda FC vs Al-Jabalain | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Trollhattan | target=FC Trollhattan vs Ariana FC | candidate=FC Trollhattan vs Ariana FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=ASKO Kottmannsdorf | target=ASKO Kottmannsdorf vs SV Dellach/Gail | candidate=ASKO Kottmannsdorf vs SV Dellach/Gail | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Lokomotiv 1929 Sofia | target=FC Lokomotiv 1929 Sofia vs PFK Beroe Stara Zagora | candidate=FC Lokomotiv 1929 Sofia vs PFK Beroe Stara Zagora | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'TRA United'; best=0.4871
- multi_odds_match: No multi-odds payload matched event 71423498
- multi_odds_match: No multi-odds payload matched event 70945796
- multi_odds_match: No multi-odds payload matched event 63637929
- multi_odds_match: No multi-odds payload matched event 69491788
- multi_odds_match: No multi-odds payload matched event 70479356
- multi_odds_match: No multi-odds payload matched event 70945864
- multi_odds_match: No multi-odds payload matched event 67915824
- multi_odds_match: No multi-odds payload matched event 70267784
- multi_odds_match: No multi-odds payload matched event 68311590