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
Events discovery rows: 346
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: True
Search queries used: Levadeiakos, Volos NFC
Selected event IDs: 70905772, 67953290, 68492518, 69254638, 69254642, 68685980, 62038090, 62036872, 62037486, 71325698, 71218074, 62036256, 62038092, 62038104, 62038096, 70142040, 71218114, 71326004, 62037484, 62037482, 61651658, 71325688, 62037488, 62036266, 62038102, 71325694, 71467782, 62037478, 67953292, 71085530, 71325692, 69924658, 62038098, 62036258, 71325700, 62036268, 70730310, 71403924, 71403926, 70852954, 70670028, 62036880, 71403922, 71344704, 71133098, 61062283, 71055074, 71213320, 71133102, 62036874, 62036876, 62038106, 67953284, 67953280, 71336694, 71344700, 70730364, 71325674, 71462986, 70231844, 70231854, 61898614, 71467778, 68531856, 68320168, 71463050, 69880316, 70812660, 61466365, 61624648, 67126096, 68311580, 67126086, 71463060, 67126088, 67126098, 70812664, 70730368
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 346
Event selection diagnostic rows: 24635
Selected event rows: 78
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 5
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 86
Latest x-ratelimit-reset: 2026-05-13T15:11:23Z
Latest retry-after: None

- 2026-05-13 14:45 | PFC CSKA Sofia vs FC CSKA 1948 | odds_api_io_Bet365_ML | 2.15/3.25/3.5
- 2026-05-13 14:50 | Al-Raed Club vs Abha Club | odds_api_io_Bet365_ML | 1.65/4.0/3.8
- 2026-05-13 15:00 | BFC Daugavpils vs FC RFS | odds_api_io_Bet365_ML | 6.5/5.25/1.3
- 2026-05-13 15:00 | Coquimbo Unido vs Deportes Iquique | odds_api_io_Bet365_ML | 1.5/3.8/5.25
- 2026-05-13 15:00 | Deportes Recoleta vs Universidad Catolica | odds_api_io_Bet365_ML | 34.0/15.0/1.045
- 2026-05-13 15:00 | Forge FC Hamilton vs FC Supra Du Quebec | odds_api_io_Bet365_ML | 1.55/4.75/4.2
- 2026-05-13 15:00 | GKS Belchatow vs Widzew Lodz II | odds_api_io_Bet365_ML | 2.1/3.8/2.6
- 2026-05-13 15:00 | GKS Pniowek Pawlowice vs KS Gornik Polkowice | odds_api_io_Bet365_ML | 8.0/5.25/1.27
- 2026-05-13 15:00 | Gzs Tluchovia Tluchowo vs Lech II Poznan | odds_api_io_Bet365_ML | 3.6/4.2/1.65
- 2026-05-13 15:00 | HIFK vs JaPS | odds_api_io_Bet365_ML | 3.0/4.1/1.9

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Al Ittihad Al Sakandary | target=Al Ittihad Al Sakandary vs Talaea El Gaish | candidate=Al Ittihad Al Sakandary vs Talaea El Gaish | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=GKS Pniowek Pawlowice | target=GKS Pniowek Pawlowice vs KS Gornik Polkowice | candidate=GKS Pniowek Pawlowice vs KS Gornik Polkowice | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ajel de Rufisque | target=Ajel de Rufisque vs Guediawaye FC | candidate=Ajel de Rufisque vs Guediawaye FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Legia Warszawa II | target=Legia Warszawa II vs GKS Wikielec | candidate=Legia Warszawa II vs GKS Wikielec | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Busaiteen | target=Busaiteen vs AL Hala | candidate=Busaiteen vs AL Hala | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=KuPS Akatemia | target=KuPS Akatemia vs FC Honka | candidate=KuPS Akatemia vs FC Honka | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Helsingoer | target=FC Helsingoer vs BK Fremad Amager | candidate=FC Helsingoer vs BK Fremad Amager | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Velez Mostar | target=FK Velez Mostar vs HSK Zrinjski Mostar | candidate=FK Velez Mostar vs HSK Zrinjski Mostar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Ittihad | target=Al Ittihad vs Um Alhassam | candidate=Al Ittihad vs Um Alhassam | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=VJS | target=VJS vs FF Jaro | candidate=VJS vs FF Jaro | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Sokol Kolbuszowa Dolna | target=Sokol Kolbuszowa Dolna vs MKS Czarni Polaniec | candidate=Sokol Kolbuszowa Dolna vs MKS Czarni Polaniec | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ishoej IF | target=Ishoej IF vs Brabrand IF | candidate=Ishoej IF vs Brabrand IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=KS Ck Troszyn | target=KS Ck Troszyn vs Lechia Tomaszow Mazowiecki | candidate=KS Ck Troszyn vs Lechia Tomaszow Mazowiecki | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SJK Akatemia | target=SJK Akatemia vs KPV Kokkola | candidate=SJK Akatemia vs KPV Kokkola | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Manama Club | target=Manama Club vs Etehad Alreef | candidate=Manama Club vs Etehad Alreef | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Ahlafors IF | target=Ahlafors IF vs Herrestads AIF | candidate=Ahlafors IF vs Herrestads AIF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=HNK Rijeka | target=HNK Rijeka vs GNK Dinamo Zagreb | candidate=HNK Rijeka vs GNK Dinamo Zagreb | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=AB Gladsaxe | target=AB Gladsaxe vs FC Roskilde | candidate=AB Gladsaxe vs FC Roskilde | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Coquimbo Unido | target=Coquimbo Unido vs Deportes Iquique | candidate=Coquimbo Unido vs Deportes Iquique | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bnei Sakhnin FC | target=Bnei Sakhnin FC vs Hapoel Ironi Kiryat Shmona FC | candidate=Bnei Sakhnin FC vs Hapoel Ironi Kiryat Shmona FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- event_selection: No event above confidence 0.72 for query 'Levadeiakos'; best=0.0
- event_selection: No event above confidence 0.72 for query 'Volos NFC'; best=0.0
- multi_odds_match: No multi-odds payload matched event 71218074
- multi_odds_match: No multi-odds payload matched event 62036256
- multi_odds_match: No multi-odds payload matched event 62038092
- multi_odds_match: No multi-odds payload matched event 62038104
- multi_odds_match: No multi-odds payload matched event 62038096
- multi_odds_match: No multi-odds payload matched event 70142040
- multi_odds_match: No multi-odds payload matched event 71218114
- multi_odds_match: No multi-odds payload matched event 71326004