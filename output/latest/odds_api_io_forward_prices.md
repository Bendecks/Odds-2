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
Events discovery rows: 682
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 69195836, 68050998, 69195838, 67905212, 67693086, 68050318, 68050322, 68050320, 68050046, 68050316, 68051002, 69195840, 71686416, 67807404, 67807406, 68160196, 68161728, 71684772, 69195842, 67808484, 68050050, 68162406, 71715884, 68160200, 68160952, 69768192, 69115756, 68916322, 69768196, 69768194, 68916320, 71715878, 69768198, 68160954, 69768202, 71717478, 71715874, 67692626, 69194944, 69115766, 71715870, 71717646, 71715876, 71715868, 69115760, 69115758, 69768200, 68050326, 71715872, 71715882, 71715480, 71716610, 69115764, 71715880, 68161346, 68048888, 68051628, 68051632, 68051630, 69195844, 68048884, 68051626, 68162404, 68048886, 68161348, 68162408, 67905696, 71717650, 67692264, 68162410, 67691630, 67691628, 67807408, 67693080, 68680078, 68686942, 68680076, 67904454, 69115226, 71717756
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 676
Event selection diagnostic rows: 51400
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 50
Latest x-ratelimit-reset: 2026-05-30T02:59:49Z
Latest retry-after: None

- 2026-05-30 02:30 | Canberra Juventus FC vs Tuggeranong United FC | odds_api_io_Bet365_ML | 2.2/4.1/2.5
- 2026-05-30 02:30 | Metrostars Reserve vs West Adelaide Reserve | odds_api_io_Bet365_ML | 1.5/4.5/4.2
- 2026-05-30 02:30 | O'Connor Knights SC vs Queanbeyan City FC | odds_api_io_Bet365_ML | 2.6/4.1/2.05
- 2026-05-30 02:45 | Gold Coast United FC vs Peninsula Power | odds_api_io_Bet365_ML | 2.25/4.0/2.375
- 2026-05-30 03:00 | University of NSW vs Wollongong Wolves FC | odds_api_io_Bet365_ML | 2.8/3.7/2.05
- 2026-05-30 03:15 | Adelaide Cobras Reserves vs Adelaide Atletico Victory Reserves | odds_api_io_Bet365_ML | 2.1/4.0/2.6
- 2026-05-30 03:15 | Adelaide Croatia Raiders SC Reserve vs Modbury Jets SC Reserve | odds_api_io_Bet365_ML | 5.0/5.0/1.4
- 2026-05-30 03:15 | Cumberland United Reserve vs Salisbury United Reserve | odds_api_io_Bet365_ML | 1.142/8.5/15.0
- 2026-05-30 03:15 | Para Hills Knights SC Reserve vs Croydon Kings FC Reserve | odds_api_io_Bet365_ML | 1.615/5.0/3.4
- 2026-05-30 03:15 | South Adelaide Reserve vs Eastern United Reserve | odds_api_io_Bet365_ML | 2.3/4.0/2.3

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Canberra Juventus FC | target=Canberra Juventus FC vs Tuggeranong United FC | candidate=Canberra Juventus FC vs Tuggeranong United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra Juventus FC | target=Canberra Juventus FC vs Tuggeranong United FC | candidate=Canberra Juventus FC vs Tuggeranong Utd | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Gold Coast United FC | target=Gold Coast United FC vs Peninsula Power | candidate=Gold Coast United FC vs Peninsula Power FC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Gwelup Croatia SC Reserves | target=Gwelup Croatia SC Reserves vs Quinns FC Reserve | candidate=Gwelup Croatia SC Reserves vs Quinns FC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Launceston United | target=Launceston United vs Kingborough Lions United FC | candidate=Launceston United vs Kingborough Lions United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Nara Club | target=Nara Club vs Oita Trinita | candidate=Nara Club vs Oita Trinita | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Moreland City FC | target=Moreland City FC vs Eastern Lions SC | candidate=Moreland City FC vs Eastern Lions SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Melbourne Srbija | target=FC Melbourne Srbija vs Langwarrin SC | candidate=FC Melbourne Srbija vs Langwarrin SC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Cooks Hill United | target=Cooks Hill United vs Valentine FC | candidate=Cooks Hill United vs Valentine FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Avondale FC | target=Avondale FC vs Bentleigh Greens | candidate=Avondale FC vs Bentleigh Greens | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Cerezo Osaka | target=Cerezo Osaka vs FC Tokyo | candidate=Cerezo Osaka vs FC Tokyo | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Subiaco AFC Reserve | target=Subiaco AFC Reserve vs Uwa Nedlands FC Reserves | candidate=Subiaco AFC Reserve vs Uwa Nedlands FC Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Riverside Olympic FC | target=Riverside Olympic FC vs Kingborough Lions United FC | candidate=Riverside Olympic FC vs Kingborough Lions United FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Altona Magic SC | target=Altona Magic SC vs Oakleigh Cannons FC | candidate=Altona Magic SC vs Oakleigh Cannons | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Maitland FC Reserve | target=Maitland FC Reserve vs Belmont Swansea United FC Reserves | candidate=Maitland FC Reserve vs Belmont Swansea United FC Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sturt Lions | target=Sturt Lions vs FK Beograd | candidate=Sturt Lions vs FK Beograd | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=O'Connor Knights FC | target=O'Connor Knights FC vs Queanbeyan City FC | candidate=O'Connor Knights FC vs Queanbeyan City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Osaka | target=FC Osaka vs Reilac Shiga FC | candidate=FC Osaka vs Reilac Shiga FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Olympic Kingsway SC | target=Olympic Kingsway SC vs Dianella White Eagles SC | candidate=Olympic Kingsway SC vs Dianella White Eagles SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Vissel Kobe | target=Vissel Kobe vs Kashima Antlers | candidate=Vissel Kobe vs Kashima Antlers | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 68051002
- multi_odds_match: No multi-odds payload matched event 69195840
- multi_odds_match: No multi-odds payload matched event 71686416
- multi_odds_match: No multi-odds payload matched event 67807404
- multi_odds_match: No multi-odds payload matched event 67807406
- multi_odds_match: No multi-odds payload matched event 68160196
- multi_odds_match: No multi-odds payload matched event 68161728
- multi_odds_match: No multi-odds payload matched event 71684772
- multi_odds_match: No multi-odds payload matched event 69195842
- multi_odds_match: No multi-odds payload matched event 67808484