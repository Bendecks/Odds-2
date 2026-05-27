# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 2 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 168
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 70773710, 71685272, 71238562, 71679480, 71238560, 71577986, 71734956, 69109016, 71553484, 67782936, 67604828, 70711924, 68774162, 71679670, 71685812, 68158852, 71681884, 69924498, 70965792, 71299152, 71072680, 61541488, 71685278, 71685280, 69688872, 71732466, 68751822, 69688816, 68158846, 68158854, 68751818, 69688820, 69688870, 69688818, 68751830, 68751812, 68751820, 69688814, 71615196, 68306836, 68306838, 68158850, 71732468, 68751824, 71615628, 69688876, 69688874, 71636144, 68158830, 70703500, 71732456, 71732476, 70531734, 71615334, 70531736, 71738554, 71284950, 71636148, 69340066, 61688400, 68306842, 68306840, 68306846, 68306844, 71615568, 71445308, 69091140, 71355154, 71335392, 68989440, 71615692, 70075150, 71463786, 69091142, 70075228, 71463600, 70075152, 70075274, 70075276, 70076110
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 168
Event selection diagnostic rows: 10280
Selected event rows: 80
Priced event rows: 5
Price rows: 5
Errors/status rows: 75

## Provider rate-limit headers

Header rows captured: 2
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 47
Latest x-ratelimit-reset: 2026-05-27T15:24:03Z
Latest retry-after: None

- 2026-05-27 15:30 | ETO FC Gyor vs MTK Hungaria Budapest | odds_api_io_Bet365_ML | 1.95/3.7/3.0
- 2026-05-27 15:30 | Jypk vs Ons Oulu | odds_api_io_Bet365_ML | 2.0/3.8/2.875
- 2026-05-27 15:30 | SJK Akatemia/2 vs JS Hercules | odds_api_io_Bet365_ML | 1.8/4.333/3.0
- 2026-05-27 15:30 | Tampereen Ilves vs Turun Palloseura | odds_api_io_Bet365_ML | 1.5/4.5/4.75
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC | odds_api_io_Bet365_ML | 3.0/2.9/2.25

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Coton Sport de Garoua | target=Coton Sport de Garoua vs Panthere Sportive | candidate=Coton Sport de Garoua vs Panthere Sportive | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SJK Akatemia/2 | target=SJK Akatemia/2 vs JS Hercules | candidate=SJK Akatemia/2 vs JS Hercules | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=San Francisco Glens SC | target=San Francisco Glens SC vs Davis Legacy | candidate=San Francisco Glens SC vs Davis Legacy | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al-Merrikh SC (SDN) | target=Al-Merrikh SC (SDN) vs Apr FC | candidate=Al-Merrikh SC (SDN) vs Apr FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Throttur Reykjavik | target=Throttur Reykjavik vs Grotta | candidate=Throttur Reykjavik vs Grotta | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=UMF Grindavik | target=UMF Grindavik vs Afturelding | candidate=UMF Grindavik vs Afturelding | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tampereen Ilves | target=Tampereen Ilves vs Turun Palloseura | candidate=Tampereen Ilves vs Turun Palloseura | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=3B Sport AM | target=3B Sport AM vs Acao Futebol MT | candidate=3B Sport AM vs Acao Futebol MT | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CA Defensores Unidos | target=CA Defensores Unidos vs Villa Dalmine | candidate=CA Defensores Unidos vs Villa Dalmine | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Primorje Ajdovscina | target=Primorje Ajdovscina vs Nafta 1903 Lendava | candidate=Primorje Ajdovscina vs Nafta 1903 Lendava | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=JK Tallinna Kalev | target=JK Tallinna Kalev vs Viimsi JK | candidate=JK Tallinna Kalev vs Viimsi JK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CF Esperanca D Andorra | target=CF Esperanca D Andorra vs Sporting Club DE Escaldes | candidate=CF Esperanca D Andorra vs Sporting Club DE Escaldes | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Jamaica | target=Jamaica vs India | candidate=Jamaica vs India | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Fylkir Reykjavik | target=Fylkir Reykjavik vs Leiknir Reykjavik | candidate=Fylkir Reykjavik vs Leiknir Reykjavik | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=KF Aegir | target=KF Aegir vs IR Reykjavik | candidate=KF Aegir vs IR Reykjavik | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Vinotinto FC Ecuador | target=Vinotinto FC Ecuador vs Orense SC | candidate=Vinotinto FC Ecuador vs Orense SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=RC Deportivo De La Coruna | target=RC Deportivo De La Coruna vs RCD Espanyol Barcelona | candidate=RC Deportivo De La Coruna vs RCD Espanyol Barcelona | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=HJK Klubi 04 | target=HJK Klubi 04 vs PK-35 Helsinki | candidate=HJK Klubi 04 vs PK-35 Helsinki | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CR Brasil AL | target=CR Brasil AL vs Gremio Novorizontino SP | candidate=CR Brasil AL vs Gremio Novorizontino SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Boyaca Chico FC | target=Boyaca Chico FC vs Llaneros FC | candidate=Boyaca Chico FC vs Llaneros FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- odds_parse: No 1X2 odds found in multi-odds payload for event 70773710
- odds_parse: No 1X2 odds found in multi-odds payload for event 71685272
- odds_parse: No 1X2 odds found in multi-odds payload for event 71238562
- odds_parse: No 1X2 odds found in multi-odds payload for event 71679480
- odds_parse: No 1X2 odds found in multi-odds payload for event 71238560
- multi_odds_match: No multi-odds payload matched event 67604828
- multi_odds_match: No multi-odds payload matched event 70711924
- multi_odds_match: No multi-odds payload matched event 68774162
- multi_odds_match: No multi-odds payload matched event 71679670
- multi_odds_match: No multi-odds payload matched event 71685812