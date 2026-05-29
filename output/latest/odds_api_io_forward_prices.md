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
Events discovery rows: 461
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Piratas de Campeche
Selected event IDs: 69460628, 69455902, 69460630, 67693568, 68686936, 68051000, 68160578, 68160192, 68161722, 68161724, 68051624, 67807834, 68049818, 70926710, 68161734, 67692262, 68686542, 68162402, 68048882, 68049816, 71127916, 69455900, 69115230, 69455904, 68995188, 70314466, 70926712, 68902054, 70926714, 69880358, 69688816, 69880350, 62067484, 62067480, 62067474, 62067476, 62067482, 62067478, 62067486, 69254676, 67912710, 69670734, 68492550, 67604830, 67845768, 67845774, 69109020, 70683984, 69924692, 68538272, 67604832, 71732830, 69972748, 69972742, 71732828, 68538274, 62036316, 71482568, 71288188, 69670736, 71737510, 68954852, 61911566, 68959610, 67017092, 67604834, 65653558, 70684212, 71727738, 61911562, 71284974, 62274248, 61911556, 69108842, 70730328, 68538276, 69920658, 71530436, 69670738
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 465
Event selection diagnostic rows: 33802
Selected event rows: 79
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 58
Latest x-ratelimit-reset: 2026-05-29T03:04:59Z
Latest retry-after: None

- 2026-05-29 07:00 | Manukau United FC vs Fencibles United FC | odds_api_io_Bet365_ML | 15.0/9.0/1.111
- 2026-05-29 07:00 | Shaanxi Union FC vs Nanjing City | odds_api_io_Bet365_ML | 1.8/3.3/4.0
- 2026-05-29 07:00 | Western Springs AFC vs Bay Olympic | odds_api_io_Bet365_ML | 1.333/5.0/7.0
- 2026-05-29 08:00 | Blacktown Spartans FC vs Western City Rangers FC | odds_api_io_Bet365_ML | 1.727/4.0/3.5
- 2026-05-29 08:30 | Taroona vs South Hobart FC | odds_api_io_Bet365_ML | 23.0/11.0/1.062
- 2026-05-29 08:45 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves | odds_api_io_Bet365_ML | 8.0/6.0/1.25
- 2026-05-29 09:30 | Brunswick City SC vs Manningham United Blues | odds_api_io_Bet365_ML | 2.6/3.75/2.2
- 2026-05-29 09:30 | Heidelberg United FC vs Dandenong Thunder | odds_api_io_Bet365_ML | 1.533/4.2/4.75
- 2026-05-29 09:30 | Nunawading City vs Altona City SC | odds_api_io_Bet365_ML | 2.4/3.5/2.5
- 2026-05-29 09:45 | Keilor Park SC vs Kingston City FC | odds_api_io_Bet365_ML | 1.42/4.333/5.5

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Fardu Ferghana | target=Fardu Ferghana vs Olimpik Mobiuz | candidate=Fardu Ferghana vs Olimpik Mobiuz | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Keilor Park SC | target=Keilor Park SC vs Kingston City FC | candidate=Keilor Park SC vs Kingston City FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Liaoning Tieren FC | target=Liaoning Tieren FC vs Shanghai Port FC | candidate=Liaoning Tieren FC vs Shanghai Port FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Apollon Limassol | target=Apollon Limassol vs Pafos FC | candidate=Apollon Limassol vs Pafos FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Andorra | target=Andorra vs Iraq | candidate=Andorra vs Iraq | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Taroona | target=Taroona vs South Hobart FC | candidate=Taroona vs South Hobart FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Shire Endaselassie FC | target=Shire Endaselassie FC vs Hadiya Hossana FC | candidate=Shire Endaselassie FC vs Hadiya Hossana FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Guandong GZ-Power FC | target=Guandong GZ-Power FC vs Shenzhen Juniors FC | candidate=Guandong GZ-Power FC vs Shenzhen Juniors FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=West Torrens Birkalla | target=West Torrens Birkalla vs Adelaide Comets FC | candidate=West Torrens Birkalla vs Adelaide Comets FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Dfk Dainava Alytus | target=Dfk Dainava Alytus vs FK Ekranas | candidate=Dfk Dainava Alytus vs FK Ekranas | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Blacktown Spartans FC | target=Blacktown Spartans FC vs Western City Rangers FC | candidate=Blacktown Spartans vs Western City Rangers FC | confidence=1.0 | selected=False | reason=
- src=events_bookmaker_filtered | query=Blacktown Spartans FC | target=Blacktown Spartans FC vs Western City Rangers FC | candidate=Blacktown Spartans FC vs Western City Rangers FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Thisted FC | target=Thisted FC vs FC Roskilde | candidate=Thisted FC vs FC Roskilde | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Itabirito FC MG | target=Itabirito FC MG vs AE Uberabinha MG | candidate=Itabirito FC MG vs AE Uberabinha MG | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Pogon Sokol Lubaczow | target=Pogon Sokol Lubaczow vs Star Starachowice | candidate=Pogon Sokol Lubaczow vs Star Starachowice | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Olympic Kingsway SC | target=Olympic Kingsway SC vs Dianella White Eagles SC | candidate=Olympic Kingsway SC vs Dianella White Eagles SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Wolaita Dicha SC | target=Wolaita Dicha SC vs Negelle Arsi | candidate=Wolaita Dicha SC vs Negelle Arsi | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Jezero Plav | target=FK Jezero Plav vs FK Iskra Danilovgrad | candidate=FK Jezero Plav vs FK Iskra Danilovgrad | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=TPV Tampere | target=TPV Tampere vs Tampere United | candidate=TPV Tampere vs Tampere United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PK Keski-Uusimaa | target=PK Keski-Uusimaa vs KuPS Akatemia | candidate=PK Keski-Uusimaa vs KuPS Akatemia | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Piratas de Campeche'; best=0.6251
- multi_odds_match: No multi-odds payload matched event 68051624
- multi_odds_match: No multi-odds payload matched event 67807834
- multi_odds_match: No multi-odds payload matched event 68049818
- multi_odds_match: No multi-odds payload matched event 70926710
- multi_odds_match: No multi-odds payload matched event 68161734
- multi_odds_match: No multi-odds payload matched event 67692262
- multi_odds_match: No multi-odds payload matched event 68686542
- multi_odds_match: No multi-odds payload matched event 68162402
- multi_odds_match: No multi-odds payload matched event 68048882