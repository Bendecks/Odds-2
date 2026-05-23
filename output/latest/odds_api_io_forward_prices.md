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
Events discovery rows: 906
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 68686532, 68686928, 68686534, 69091022, 68050304, 68161328, 69462634, 68050306, 69195828, 68050032, 67905200, 68160942, 69195830, 69460620, 69460616, 68161330, 71549044, 67905678, 69460614, 69115744, 69462636, 68050042, 68050308, 68050038, 68050312, 68050310, 68050036, 68050314, 67905202, 67807392, 68728650, 68728648, 68728656, 67690874, 69194930, 68680064, 71549046, 67808472, 68680066, 68680068, 68162388, 68686930, 67905680, 68048872, 67648310, 67645078, 68162390, 69115750, 69460622, 68916306, 69194932, 68916318, 69463280, 69768186, 68048870, 68161332, 69115746, 68162392, 67648154, 67648156, 69768184, 68916310, 67648152, 69768182, 68162394, 68162396, 67648312, 68160568, 68916316, 68160570, 69768188, 67648470, 67648472, 67645076, 68916308, 69115748, 69115754, 69768180, 68532512, 69768190
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 891
Event selection diagnostic rows: 69320
Selected event rows: 80
Priced event rows: 7
Price rows: 7
Errors/status rows: 73

## Provider rate-limit headers

Header rows captured: 7
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 47
Latest x-ratelimit-reset: 2026-05-23T02:58:20Z
Latest retry-after: None

- 2026-05-23 02:30 | Davis Legacy vs Almaden FC | odds_api_io_Bet365_ML | 3.6/3.8/1.75
- 2026-05-23 02:30 | Eastern United Reserve vs Adelaide Blue Eagles Reserves | odds_api_io_Bet365_ML | 5.0/5.0/1.4
- 2026-05-23 02:30 | Green Gully SC vs Heidelberg United FC | odds_api_io_Bet365_ML | 2.9/4.333/1.8
- 2026-05-23 02:30 | Waterside Karori vs Wellington Olympic | odds_api_io_Bet365_ML | 15.0/7.5/1.166
- 2026-05-23 02:45 | Adelaide Atletico Victory Reserves vs South Adelaide Reserve | odds_api_io_Bet365_ML | 1.666/4.5/3.4
- 2026-05-23 02:45 | Canberra White Eagles FC vs O'Connor Knights SC | odds_api_io_Bet365_ML | 15.0/8.5/1.142
- 2026-05-23 02:45 | Croydon Kings FC Reserve vs North Eastern Metrostars SC Reserves | odds_api_io_Bet365_ML | 10.0/6.5/1.166

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Clarence Zebras FC 2 | target=Clarence Zebras FC 2 vs Olympia Warriors Hobart | candidate=Clarence Zebras FC 2 vs Olympia Warriors Hobart | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Playford City Reserve | target=Playford City Reserve vs West Adelaide SC Reserve | candidate=Playford City Reserve vs West Adelaide SC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tokyo Verdy Beleza | target=Tokyo Verdy Beleza vs Naegohyang Womens FC | candidate=Tokyo Verdy Beleza vs Naegohyang Womens FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dandenong City SC | target=Dandenong City SC vs ST Albans Saints Dinamo SC | candidate=Dandenong City SC vs ST Albans Saints Dinamo SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra Olympic | target=Canberra Olympic vs Belconnen United | candidate=Canberra Olympic vs Belconnen United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sanfrecce Hiroshima | target=Sanfrecce Hiroshima vs Nagoya Grampus | candidate=Sanfrecce Hiroshima vs Nagoya Grampus | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Changwon FC | target=Changwon FC vs Ulsan Citizen FC | candidate=Changwon FC vs Ulsan Citizen FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=North Sunshine Eagles FC | target=North Sunshine Eagles FC vs Langwarrin SC | candidate=North Sunshine Eagles FC vs Langwarrin SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=South Melbourne FC | target=South Melbourne FC vs Bentleigh Greens SC | candidate=South Melbourne FC vs Bentleigh Greens SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Manukau United FC | target=Manukau United FC vs Tauranga City AFC | candidate=Manukau United FC vs Tauranga City AFC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Edgeworth FC Reserve | target=Edgeworth FC Reserve vs Lambton Jaffas FC Reserve | candidate=Edgeworth FC Reserve vs Lambton Jaffas FC Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dianella White Eagles SC | target=Dianella White Eagles SC vs Armadale SC | candidate=Dianella White Eagles SC vs Armadale SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dianella White Eagles SC | target=Dianella White Eagles SC vs Armadale SC | candidate=Dianella White Eagles SC vs Armadale SC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Launceston United | target=Launceston United vs South Hobart FC | candidate=Launceston United vs South Hobart FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra White Eagles FC | target=Canberra White Eagles FC vs O'Connor Knights FC | candidate=Canberra White Eagles FC vs O'Connor Knights FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Modbury Jets SC Reserve | target=Modbury Jets SC Reserve vs Cumberland United Reserve | candidate=Modbury Jets SC Reserve vs Cumberland United Reserve | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Salisbury United Reserve | target=Salisbury United Reserve vs Adelaide Cobras Reserves | candidate=Salisbury United Reserve vs Adelaide Cobras Reserves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gold Coast United FC | target=Gold Coast United FC vs Rochedale Rovers | candidate=Gold Coast United FC vs Rochedale Rovers | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Christchurch United FC | target=Christchurch United FC vs Coastal Spirit FC | candidate=Christchurch United FC vs Coastal Spirit FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=University of Nsw | target=University of Nsw vs Sydney United 58 FC | candidate=University of NSW vs Sydney United 58 FC | confidence=1.0 | selected=False | reason=

## Errors / Status

- odds_parse: No 1X2 odds found in multi-odds payload for event 68686532
- odds_parse: No 1X2 odds found in multi-odds payload for event 68686928
- odds_parse: No 1X2 odds found in multi-odds payload for event 68686534
- multi_odds_match: No multi-odds payload matched event 67905200
- multi_odds_match: No multi-odds payload matched event 68160942
- multi_odds_match: No multi-odds payload matched event 69195830
- multi_odds_match: No multi-odds payload matched event 69460620
- multi_odds_match: No multi-odds payload matched event 69460616
- multi_odds_match: No multi-odds payload matched event 68161330
- multi_odds_match: No multi-odds payload matched event 71549044