# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 3 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 335
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 69091194, 69460634, 70343232, 69460626, 69342886, 69342884, 71234490, 69342878, 71505358, 71704136, 69880354, 69342882, 69880352, 69880348, 69342890, 71709420, 71704158, 71685284, 71685282, 71685286, 69342888, 70684208, 71704428, 68538268, 69924684, 69924686, 71737390, 71577916, 68774164, 67912706, 69924124, 71530440, 71544082, 67149486, 62274242, 70655020, 69923700, 71401844, 70663592, 71685288, 68158840, 68158856, 68158836, 68158844, 68158842, 71668632, 71729572, 68751826, 71769326, 71602082, 71585136, 71704432, 69829492, 71615192, 71615270, 71562582, 71705028, 71705030, 71615688, 71615454, 68158832, 70075878, 70075876, 71355212, 71762788, 69091202, 69091204, 69091206, 71517962, 70075106, 70075754, 70075108, 70075756, 71705032, 69091222, 68989156, 67693568, 67905690, 68160578, 68160192
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 332
Event selection diagnostic rows: 23640
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 57
Latest x-ratelimit-reset: 2026-05-28T02:57:51Z
Latest retry-after: None

- 2026-05-28 02:30 | Stars FC vs AMSG FC | odds_api_io_Bet365_ML | 3.0/4.333/1.8
- 2026-05-28 07:00 | Auckland FC Reserves vs Auckland United FC | odds_api_io_Bet365_ML | 3.8/4.75/1.571
- 2026-05-28 07:00 | Birkenhead United AFC vs East Coast Bays | odds_api_io_Bet365_ML | 1.38/5.0/5.5
- 2026-05-28 07:00 | Melville United AFC vs Tauranga City AFC | odds_api_io_Bet365_ML | 2.4/3.9/2.25
- 2026-05-28 10:00 | FC Okzhetpes vs FC Aktobe | odds_api_io_Bet365_ML | 2.45/3.1/2.7
- 2026-05-28 11:00 | FC Kyzylzhar SK vs Zhetysu Taldykorgan | odds_api_io_Bet365_ML | 1.9/3.2/3.75
- 2026-05-28 11:00 | Sri Lanka vs Bhutan | odds_api_io_Bet365_ML | 13.0/10.0/1.111
- 2026-05-28 13:00 | FK Atyrau vs Tobol Kostanay | odds_api_io_Bet365_ML | 3.3/3.0/2.05
- 2026-05-28 13:00 | FK Kukesi vs Butrinti Sarande | odds_api_io_Bet365_ML | 1.3/4.333/8.0
- 2026-05-28 14:00 | FK Septemvri Sofia vs FC Yantra Gabrovo | odds_api_io_Bet365_ML | 1.533/3.6/6.0

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Stars FC | target=Stars FC vs AMSG FC | candidate=Stars FC vs AMSG FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Torpedo Kutaisi | target=FC Torpedo Kutaisi vs FC Gagra | candidate=FC Torpedo Kutaisi vs FC Gagra | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA River Plate (Arg) | target=CA River Plate (Arg) vs San Lorenzo de Almagro Res. | candidate=CA River Plate (Arg) vs San Lorenzo de Almagro Res. | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CD El Nacional | target=CD El Nacional vs CD Universidad Catolica del Ecuador | candidate=CD El Nacional vs CD Universidad Catolica del Ecuador | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Ylivieska | target=FC Ylivieska vs Lapuan Virkia | candidate=FC Ylivieska vs Lapuan Virkia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Heidelberg United FC | target=Heidelberg United FC vs Dandenong Thunder | candidate=Heidelberg United FC vs Dandenong Thunder | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cruzeiro EC MG | target=Cruzeiro EC MG vs Doce Mel EC BA | candidate=Cruzeiro EC MG vs Doce Mel EC BA | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Llaneros FC | target=Llaneros FC vs Independiente Santa Fe | candidate=Llaneros FC vs Independiente Santa Fe | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FCM Traiskirchen | target=FCM Traiskirchen vs SC Neusiedl am See 1919 | candidate=FCM Traiskirchen vs SC Neusiedl am See 1919 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Deportivo Maldonado Reserve | target=Deportivo Maldonado Reserve vs Liverpool Montevideo | candidate=Deportivo Maldonado Reserve vs Liverpool Montevideo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kolding IF | target=Kolding IF vs Dbk Fortuna Hjoerring | candidate=Kolding IF vs Dbk Fortuna Hjoerring | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=1. FC Lokomotive Leipzig | target=1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | candidate=1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Fahaheel | target=Al-Fahaheel vs Al-Salmiya SC | candidate=Al-Fahaheel vs Al-Salmiya SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Petrojet FC | target=Petrojet FC vs El Gouna FC | candidate=Petrojet FC vs El Gouna FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cruzeiro EC MG | target=Cruzeiro EC MG vs Barcelona SC | candidate=Cruzeiro EC MG vs Barcelona SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tacoma Stars | target=Tacoma Stars vs FC Olympia | candidate=Tacoma Stars vs FC Olympia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Jazz | target=FC Jazz vs SalPa | candidate=FC Jazz vs SalPa | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Assyriska FF | target=Assyriska FF vs Vasalunds IF | candidate=Assyriska FF vs Vasalunds IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Patuxent Football Athletics | target=Patuxent Football Athletics vs Annapolis Blues FC | candidate=Patuxent Football Athletics vs Annapolis Blues FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Casa Pia Lisbon | target=Casa Pia Lisbon vs SCU Torreense | candidate=Casa Pia Lisbon vs SCU Torreense | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 69880354
- multi_odds_match: No multi-odds payload matched event 69342882
- multi_odds_match: No multi-odds payload matched event 69880352
- multi_odds_match: No multi-odds payload matched event 69880348
- multi_odds_match: No multi-odds payload matched event 69342890
- multi_odds_match: No multi-odds payload matched event 71709420
- multi_odds_match: No multi-odds payload matched event 71704158
- multi_odds_match: No multi-odds payload matched event 71685284
- multi_odds_match: No multi-odds payload matched event 71685282
- multi_odds_match: No multi-odds payload matched event 71685286