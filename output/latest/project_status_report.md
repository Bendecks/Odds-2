# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-22T02:39:47.948022+00:00`
GitHub run: `365` attempt `1`
GitHub SHA: `8be58f0eae35110d2e44b4cf2676441cda45e94a`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 53 |  |  |
| odds-api.io forward fixtures | True | 560 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 192 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 4 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 300 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 189
- Positive EV proxy rows: 86
- Proxy observation rows: 25
- Valid forward/proxy log rows: 499
- Deduped forward/proxy log rows: 363
- Duplicate forward/proxy log rows identified: 136
- Fresh API match coverage rate: 0.19
- Matches with fresh API price: 57
- Settled forward rows: 0
- Real-money ready: False
## Stage checklist
### historical_proxy_research
Status: `complete_but_negative_clv`
Target: Historical pipeline runs and exposes calibration/CLV weaknesses.
Current: Historical outputs exist; CLV trend remains negative.
Done when: Use only for model diagnostics, not betting decisions.
### automatic_proxy_odds_ingestion
Status: `working`
Target: Free automatic odds proxy exists and validates.
Current: 189 value snapshots; fresh API coverage rate 0.19.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 363 deduped forward/proxy rows; 136 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 47
Upcoming fixture rows: 47
Proxy price rows: 138
Sources attempted: 1
Errors: 0
- 2026-05-23 19:45 | Antwerp vs Westerlo | football_data_bet365_proxy | 1.91/3.7/3.5
- 2026-05-23 19:45 | Antwerp vs Westerlo | football_data_max_market_proxy | 1.92/4.0/3.65
- 2026-05-23 19:45 | Antwerp vs Westerlo | football_data_average_market_proxy | 1.88/3.77/3.42
- 2026-05-23 19:45 | Oud-Heverlee Leuven vs Genk | football_data_bet365_proxy | 3.7/3.75/1.85
- 2026-05-23 19:45 | Oud-Heverlee Leuven vs Genk | football_data_max_market_proxy | 3.7/4.0/1.91
- 2026-05-23 19:45 | Oud-Heverlee Leuven vs Genk | football_data_average_market_proxy | 3.54/3.73/1.87
- 2026-05-23 19:45 | Standard vs Charleroi | football_data_bet365_proxy | 2.1/3.4/3.2
- 2026-05-23 19:45 | Standard vs Charleroi | football_data_max_market_proxy | 2.1/3.45/3.6
- 2026-05-23 19:45 | Standard vs Charleroi | football_data_average_market_proxy | 2.03/3.35/3.4
- 2026-05-24 17:30 | Club Brugge vs Gent | football_data_max_market_proxy | 1.78/4.33/3.8
- 2026-05-24 17:30 | Club Brugge vs Gent | football_data_average_market_proxy | 1.72/4.15/3.67
- 2026-05-24 17:30 | St Truiden vs Mechelen | football_data_max_market_proxy | 1.88/4.1/3.65
- 2026-05-24 17:30 | St Truiden vs Mechelen | football_data_average_market_proxy | 1.82/3.85/3.53
- 2026-05-24 17:30 | St. Gilloise vs Anderlecht | football_data_max_market_proxy | 1.5/4.33/6.66
- 2026-05-24 17:30 | St. Gilloise vs Anderlecht | football_data_average_market_proxy | 1.44/4.2/6.26
- 2026-05-24 16:00 | Brighton vs Man United | football_data_bet365_proxy | 1.85/4.2/3.6
- 2026-05-24 16:00 | Brighton vs Man United | football_data_max_market_proxy | 1.92/4.2/3.75
- 2026-05-24 16:00 | Brighton vs Man United | football_data_average_market_proxy | 1.86/3.98/3.58
- 2026-05-24 16:00 | Burnley vs Wolves | football_data_bet365_proxy | 2.35/3.5/2.9
- 2026-05-24 16:00 | Burnley vs Wolves | football_data_max_market_proxy | 2.48/3.6/2.9
- 2026-05-24 16:00 | Burnley vs Wolves | football_data_average_market_proxy | 2.36/3.5/2.77
- 2026-05-24 16:00 | Crystal Palace vs Arsenal | football_data_bet365_proxy | 4.2/4.0/1.75
- 2026-05-24 16:00 | Crystal Palace vs Arsenal | football_data_max_market_proxy | 4.33/4.2/1.82

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 778
Fixture team rows unmatched: 1489
Ready for model-fixture join: False
Automatic forward price rows: 195
odds-api.io price rows: 57
Football-Data price rows: 138
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 9 de Octubre FC | suggestion=nan | type=unmatched
- Manta FC | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Atalanta BC | suggestion=Atalanta | type=suggested_alias_needed
- Aarhus Fremad | suggestion=nan | type=unmatched
- Aalborg BK | suggestion=nan | type=unmatched
- AB Gladsaxe | suggestion=nan | type=unmatched
- HIK Hellerup | suggestion=nan | type=unmatched
- AC Omonia Nicosia | suggestion=nan | type=unmatched
- Apollon Limassol | suggestion=nan | type=unmatched
- ADO Den Haag | suggestion=nan | type=unmatched
- PEC Zwolle | suggestion=nan | type=unmatched
- Afturelding | suggestion=nan | type=unmatched
- Throttur Reykjavik | suggestion=nan | type=unmatched
- Ajel de Rufisque | suggestion=nan | type=unmatched
- ASC Linguere | suggestion=nan | type=unmatched
- Al Jazira (UAE) | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 195
Value snapshot rows: 189
Matches with any automatic price: 58
Matches with fresh API price: 57
Matches with odds-api.io price: 57
Fresh API match coverage rate: 0.19
odds-api.io match coverage rate: 0.19
Real-money ready: False
## Match coverage
- 2026-05-22 | AC Omonia Nicosia vs Apollon Limassol | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Aris Limassol FC vs AEK Larnaca | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Pafos FC vs APOEL Nikosia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | AS Armee vs FC Brakna | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | FK Auda Riga vs FK Liepaja | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | FK Septemvri Sofia vs PFC Dobrudzha Dobrich | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | FK Spartak 1918 Varna vs FC Lokomotiv 1929 Sofia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | FK Zeleznicar Pancevo vs FK Cukaricki Belgrade | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Korona II Kielce SA vs MKS Czarni Polaniec | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-22 | POFC Botev Vratsa vs PFK Beroe Stara Zagora | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Rekord Bielsko-Biala vs AZS UJ Krakow | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Sexypoxyt vs PPJ/Ruoholahti | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Azam FC vs Tanzania Prisons | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Gzs Tluchovia Tluchowo vs Blekitni Stargard | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | HJK Akatemia vs FC Lahti | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Kjp Kouvola vs Kopa | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Kuopion Palloseura vs IF Gnistan | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 195
Matched prediction rows: 59
Value snapshot rows: 189
odds-api.io snapshot rows: 171
Baseline snapshot rows: 189
Full model snapshot rows: 0
Positive EV rows: 86
Source counts: {'odds_api_io_Bet365_ML': 171, 'football_data_bet365_proxy': 6, 'football_data_max_market_proxy': 6, 'football_data_average_market_proxy': 6}
- 2026-05-22 | Kuopion Palloseura vs IF Gnistan | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3488 | EV=9.1152 | match=1.0
- 2026-05-22 | Azam FC vs Tanzania Prisons | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-22 | HNK Hajduk Split vs HNK Vukovar 1991 | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-22 | AB Gladsaxe vs HIK Hellerup | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-22 | Kuopion Palloseura vs IF Gnistan | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-05-22 | Broendby IF vs Kolding IF | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-22 | HJK Akatemia vs FC Lahti | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-22 | FC Chomutov vs FK Seko Louny | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-22 | Hegelmann Litauen B vs FC Neptunas Klaipeda | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-22 | Vg-62 vs Jyty Turku | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-22 | Djurgardens IF vs IF Brommapojkarna | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-22 | Sumqayit FK vs Qarabag FK | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3772 | EV=1.1689 | match=1.0
- 2026-05-22 | FK Septemvri Sofia vs PFC Dobrudzha Dobrich | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-22 | Djoliba AC vs Usfas Bamako | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-22 | FK Spartak 1918 Varna vs FC Lokomotiv 1929 Sofia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-22 | Azam FC vs Tanzania Prisons | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-22 | HJK Akatemia vs FC Lahti | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.274 | EV=0.781 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 189
Pre-dedupe proxy candidate observation rows: 66
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-22 | Tampereen Ilves vs HPS | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-22 | Mps vs Leppavaaran Pallo | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-22 | FK Radnik Bijeljina vs FK Borac Banja Luka | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-22 | FK Jonava vs FK Babrungas Plunge | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-22 | SV Spittal/Drau vs FC Lendorf | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-22 | Dakar Sacre Coeur vs Teungueth FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-22 | Gzs Tluchovia Tluchowo vs Blekitni Stargard | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-22 | Hestrafors IF vs Jonsereds IF | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-22 | Dfk Dainava Alytus vs Be1 Nfa | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-22 | SJK Akatemia vs FC Haka Valkeakoski | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3772 | EV=0.54652 | edge=0.133298 | penalty=0.5465227837410107 | tier=proxy_watchlist | score=0.2169
- 2026-05-22 | Al Jazira (UAE) vs Al Ain FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145
- 2026-05-22 | ACF Fiorentina vs Atalanta BC | selection=HOME | source=football_data_max_market_proxy | odds=2.72 | prob=0.3772 | EV=0.025984 | edge=0.009553 | penalty=0.025984164157466294 | tier=proxy_watchlist | score=0.1919

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 5
Top blocker: ev_above_real_candidate_cap_possible_overconfidence
Real-money ready: False
## Blocker summary
- ev_above_real_candidate_cap_possible_overconfidence: 8
- market_alignment_penalty_too_high_for_real_candidate: 8
- watchlist_only_pending_forward_settlement: 2
- edge_below_candidate_threshold: 2
- delayed_football_data_proxy_not_fresh_api_price: 1
## Row explanations
- 2026-05-22 | Tampereen Ilves vs HPS | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Mps vs Leppavaaran Pallo | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | FK Radnik Bijeljina vs FK Borac Banja Luka | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | FK Jonava vs FK Babrungas Plunge | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | SV Spittal/Drau vs FC Lendorf | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Dakar Sacre Coeur vs Teungueth FC | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Gzs Tluchovia Tluchowo vs Blekitni Stargard | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Hestrafors IF vs Jonsereds IF | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Dfk Dainava Alytus vs Be1 Nfa | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-22 | SJK Akatemia vs FC Haka Valkeakoski | sel=HOME | score=0.2169 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Al Jazira (UAE) vs Al Ain FC | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | ACF Fiorentina vs Atalanta BC | sel=HOME | score=0.1919 | blockers=edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 189
Paper proxy observation rows: 25
Positive EV value rows: 86
Suppressed-band observation rows: 0
Distinct matches: 23
Distinct sources: 0
Max EV: 0.781
Average EV: 0.477578
Max probability edge: 0.1488
Average match confidence: None
## By selection
- away: rows=11, avg_ev=0.4607, max_ev=0.744
- draw: rows=8, avg_ev=0.5669, max_ev=0.781
- home: rows=6, avg_ev=0.3894, max_ev=0.5465

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 778
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 14:30 | Pafos FC vs APOEL Nikosia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:00 | AS Armee vs FC Brakna | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:00 | FK Auda Riga vs FK Liepaja | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:00 | FK Septemvri Sofia vs PFC Dobrudzha Dobrich | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:00 | FK Spartak 1918 Varna vs FC Lokomotiv 1929 Sofia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:00 | FK Zeleznicar Pancevo vs FK Cukaricki Belgrade | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:00 | Korona II Kielce SA vs MKS Czarni Polaniec | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:00 | POFC Botev Vratsa vs PFK Beroe Stara Zagora | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:00 | Rekord Bielsko-Biala vs AZS UJ Krakow | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:15 | Sexypoxyt vs PPJ/Ruoholahti | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | Azam FC vs Tanzania Prisons | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | Gzs Tluchovia Tluchowo vs Blekitni Stargard | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | HJK Akatemia vs FC Lahti | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | Kjp Kouvola vs Kopa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | Kuopion Palloseura vs IF Gnistan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | NK Kustosija Zagreb vs NK Uljanik | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | SJK Akatemia vs FC Haka Valkeakoski | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | Sokol Kolbuszowa Dolna vs Wislanie Skawina | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 15:30 | Sumqayit FK vs Qarabag FK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 2952
Log type: probability_only_no_market_prices
- 2026-05-23 2026-05-22 05:00:00 | Pocheon Citizen FC vs Jeonbuk FC II | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Renofa Yamaguchi vs Roasso Kumamoto | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Sagan Tosu vs FC Ryukyu | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Siheung Citizen FC vs Dangjin Citizen | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Sorrento FC vs Olympic Kingsway SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Stirling Macedonia FC vs Bayswater City SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Tokyo Verdy Beleza vs Naegohyang Womens FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Vegalta Sendai vs Yokohama FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Western Springs AFC vs Fencibles United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:30:00 | Adelaide Atletico VSC vs South Adelaide FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:30:00 | Adelaide Croatia Raiders SC vs Adelaide Olympic FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:30:00 | Fulham United FC vs The Cove FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:30:00 | Modbury Jets SC vs Cumberland United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:30:00 | Salisbury United vs Adelaide Cobras | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:30:00 | Tigers FC vs Brindabella Blues FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 06:30:00 | New Lambton FC vs Broadmeadow Magic FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 07:00:00 | AC Nagano Parceiro vs Ventforet Kofu | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 07:00:00 | Cockburn City vs Floreat Athena | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 07:00:00 | Gwelup Croatia SC vs Kingsley Westside FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 07:00:00 | Joondalup City vs Inglewood United | H=0.37720000000000004 D=0.274 A=0.3488

## forward_fixture_results

# Forward Fixture Results
Results for probability-only forward fixture predictions. Used for future calibration checks, not betting settlement.
Fixture rows checked: 1
Result rows: 1
Settled result rows: 0
Errors: 0
- 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United | score=not available | status=not_started_or_result_unavailable

## forward_probability_calibration

# Forward Probability Calibration Report
Probability-only forward calibration. No odds, no stakes, no real-money signal.
Forward probability rows: 1
Settled rows: 0
Unsettled rows: 1
Accuracy: None
Average Brier score: None
- 2026-05-11 | Tottenham Hotspur vs Leeds United | pred=home (0.4257) | actual=None | status=unsettled

## forward_input_status

# Forward Input Status
Manual Bet365 odds input is parked as an optional fallback. It is not an active development blocker.
Current priority: automatic/free-data forward-testing sources and robust fixture/model matching.
Upcoming fixtures: 778
Manual template rows: 778
Rows with complete manual odds: 0
Rows missing manual odds: 778
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-22 20:00 | 9 de Octubre FC vs Manta FC
- 2026-05-22 18:45 | ACF Fiorentina vs Atalanta BC
- 2026-05-22 16:00 | Aarhus Fremad vs Aalborg BK
- 2026-05-22 17:00 | AB Gladsaxe vs HIK Hellerup
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol
- 2026-05-22 18:00 | ADO Den Haag vs PEC Zwolle
- 2026-05-22 19:15 | Afturelding vs Throttur Reykjavik
- 2026-05-22 17:00 | Ajel de Rufisque vs ASC Linguere
- 2026-05-22 15:40 | Al Jazira (UAE) vs Al Ain FC
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca
- 2026-05-22 18:30 | Arsenal de Sarandi vs CA Villa San Carlos
- 2026-05-22 15:00 | AS Armee vs FC Brakna
- 2026-05-22 16:30 | AS Real Bamako vs FC Diarra
- 2026-05-22 16:45 | ASAC Concorde vs Garde
- 2026-05-22 18:45 | Athlone Town AFC vs Cork City FC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 778
Source counts: {'odds_api_io_events_bookmaker_filtered': 726, 'football_data_fixtures_proxy': 47, 'odds_api_io_events_search': 4, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-22 20:00 | 9 de Octubre FC vs Manta FC | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:45 | ACF Fiorentina vs Atalanta BC | italy-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-05-22 16:00 | Aarhus Fremad vs Aalborg BK | denmark-1-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 17:00 | AB Gladsaxe vs HIK Hellerup | denmark-2nd-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol | cyprus-1st-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:00 | ADO Den Haag vs PEC Zwolle | netherlands-eredivisie-women | odds_api_io_events_bookmaker_filtered
- 2026-05-22 19:15 | Afturelding vs Throttur Reykjavik | iceland-1-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-22 17:00 | Ajel de Rufisque vs ASC Linguere | senegal-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 15:40 | Al Jazira (UAE) vs Al Ain FC | united-arab-emirates-presidents-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca | cyprus-1st-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:30 | Arsenal de Sarandi vs CA Villa San Carlos | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-22 15:00 | AS Armee vs FC Brakna | mauritania-super-d2 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 16:30 | AS Real Bamako vs FC Diarra | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 16:45 | ASAC Concorde vs Garde | mauritania-super-d2 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:45 | Athlone Town AFC vs Cork City FC | ireland-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:00 | Ayacucho FC vs AD Comerciantes FC | peru-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:00 | AZ Alkmaar vs Excelsior Rotterdam | netherlands-eredivisie-women | odds_api_io_events_bookmaker_filtered
- 2026-05-22 15:30 | Azam FC vs Tanzania Prisons | tanzania-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-22 17:00 | Brabrand IF vs Skive IK | denmark-2nd-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 19:15 | Breidablik Kopavogur vs KR Reykjavik | iceland-besta-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-22 17:00 | Broendby IF vs Kolding IF | denmark-kvindeligaen-women | odds_api_io_events_bookmaker_filtered
- 2026-05-22 17:00 | Byaasen vs Fk Kvik Trondheim | norway-3rd-division-group-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 22:00 | CA Brown de Adrogue vs Deportivo Merlo | argentina-primera-b | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 778
Rows with complete odds: 0
- 2026-05-22 20:00 | 9 de Octubre FC vs Manta FC | bookmaker=bet365_manual
- 2026-05-22 18:45 | ACF Fiorentina vs Atalanta BC | bookmaker=bet365_manual
- 2026-05-22 16:00 | Aarhus Fremad vs Aalborg BK | bookmaker=bet365_manual
- 2026-05-22 17:00 | AB Gladsaxe vs HIK Hellerup | bookmaker=bet365_manual
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol | bookmaker=bet365_manual
- 2026-05-22 18:00 | ADO Den Haag vs PEC Zwolle | bookmaker=bet365_manual
- 2026-05-22 19:15 | Afturelding vs Throttur Reykjavik | bookmaker=bet365_manual
- 2026-05-22 17:00 | Ajel de Rufisque vs ASC Linguere | bookmaker=bet365_manual
- 2026-05-22 15:40 | Al Jazira (UAE) vs Al Ain FC | bookmaker=bet365_manual
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca | bookmaker=bet365_manual
- 2026-05-22 18:30 | Arsenal de Sarandi vs CA Villa San Carlos | bookmaker=bet365_manual
- 2026-05-22 15:00 | AS Armee vs FC Brakna | bookmaker=bet365_manual
- 2026-05-22 16:30 | AS Real Bamako vs FC Diarra | bookmaker=bet365_manual
- 2026-05-22 16:45 | ASAC Concorde vs Garde | bookmaker=bet365_manual
- 2026-05-22 18:45 | Athlone Town AFC vs Cork City FC | bookmaker=bet365_manual
- 2026-05-22 18:00 | Ayacucho FC vs AD Comerciantes FC | bookmaker=bet365_manual
- 2026-05-22 18:00 | AZ Alkmaar vs Excelsior Rotterdam | bookmaker=bet365_manual
- 2026-05-22 15:30 | Azam FC vs Tanzania Prisons | bookmaker=bet365_manual
- 2026-05-22 17:00 | Brabrand IF vs Skive IK | bookmaker=bet365_manual
- 2026-05-22 19:15 | Breidablik Kopavogur vs KR Reykjavik | bookmaker=bet365_manual
- 2026-05-22 17:00 | Broendby IF vs Kolding IF | bookmaker=bet365_manual
- 2026-05-22 17:00 | Byaasen vs Fk Kvik Trondheim | bookmaker=bet365_manual
- 2026-05-22 22:00 | CA Brown de Adrogue vs Deportivo Merlo | bookmaker=bet365_manual
- 2026-05-22 23:00 | CA Excursionistas vs CSD Liniers | bookmaker=bet365_manual

## manual_odds_instructions

# Manual Odds Entry Instructions
Purpose: create real forward paper-test snapshots from Bet365 pre-match 1X2 odds.
Do not stake real money from this system.
## What to fill
Open `data/manual/manual_odds_template.csv` and fill these columns only:
- `market_home_odds`
- `market_draw_odds`
- `market_away_odds`
- `odds_captured_at_utc`
Use decimal odds from Bet365 1X2 / Full Time Result before kickoff.
## Current rows needing odds
- 2026-05-22 20:00 | 9 de Octubre FC vs Manta FC
- 2026-05-22 18:45 | ACF Fiorentina vs Atalanta BC
- 2026-05-22 16:00 | Aarhus Fremad vs Aalborg BK
- 2026-05-22 17:00 | AB Gladsaxe vs HIK Hellerup
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol
- 2026-05-22 18:00 | ADO Den Haag vs PEC Zwolle
- 2026-05-22 19:15 | Afturelding vs Throttur Reykjavik
- 2026-05-22 17:00 | Ajel de Rufisque vs ASC Linguere
- 2026-05-22 15:40 | Al Jazira (UAE) vs Al Ain FC
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca
- 2026-05-22 18:30 | Arsenal de Sarandi vs CA Villa San Carlos
- 2026-05-22 15:00 | AS Armee vs FC Brakna
- 2026-05-22 16:30 | AS Real Bamako vs FC Diarra
- 2026-05-22 16:45 | ASAC Concorde vs Garde
- 2026-05-22 18:45 | Athlone Town AFC vs Cork City FC
- 2026-05-22 18:00 | Ayacucho FC vs AD Comerciantes FC
- 2026-05-22 18:00 | AZ Alkmaar vs Excelsior Rotterdam
- 2026-05-22 15:30 | Azam FC vs Tanzania Prisons
- 2026-05-22 17:00 | Brabrand IF vs Skive IK

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 502
Valid forward/proxy log rows: 499
Deduped forward/proxy observation rows: 363
Duplicate forward/proxy log rows: 136
Valid automatic proxy observation rows: 499
Deduped automatic proxy observation rows: 363
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-15 | Brisbane Roar FC vs Lions FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Broadmeadow Magic FC vs Newcastle Olympic FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Semen Padang FC vs Persebaya Surabaya | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-19 | Northeast United FC vs Mohammedan SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-22 | Fraser Park FC vs Camden Tigers FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-15 | Cong An TP Ho Chi Minh City FC vs SHB Da Nang | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-21 | BFC Daugavpils vs Ogre United | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-19 | Derby Academie vs Onze Createurs | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Al Kahrabaa SC vs Al-Gharraf SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Diyala FC vs Amanat Baghdad SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Deportivo Capiata vs Club Fernando de La Mora | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.056100000000000004
- 2026-05-19 | SV Ried vs Wolfsberger AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-21 | Kifisia vs Larisa | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553
- 2026-05-21 | Anderlecht vs St Truiden | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0546
- 2026-05-21 | Panetolikos vs Asteras Tripolis | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054

## betting_performance

# Betting Performance Report
Readiness: research-only
Recommendation: NO REAL MONEY - continue research
Total predictions: 210
Historical candidate predictions: 91
Current candidate bets: 0
Settled predictions: 210
Wins: 70
Total ROI units: -3.45
Average ROI per bet: -0.0164
Beat closing line rate: 0.419
Average CLV delta: -0.8542
## Interpretation
The model is not ready for real-money betting. Focus remains on CLV improvement, calibration and realistic market snapshots.

## model_health

# Model Health Report
Model state: not_beating_market
Largest problem: negative_clv
Recommended focus: improve calibration and snapshots
Tracked CLV rows: 210
Settled predictions: 210

## daily_betting_card

# Daily Betting Card
Status: research/paper-test only. No real-money recommendation yet.
Candidate bets remain the stricter real-money-gated list.
Paper-test picks are observation-only and must not be staked.
## Candidate Bets
No qualifying candidate bets today.
## Paper-Test Picks
### Sexypoxyt vs PPJ/Ruoholahti
- Date/time: 2026-05-22 15:15
- League/phase: finland-kolmonen / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 5.0
- Fair odds: 2.87
- Model probability: 0.3488
- Probability band: 0.25-0.35
- EV: 0.744
- Probability edge: 0.1488
- Alignment penalty: 0.744
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0711
- Prediction ID: 0791f9fbd59d3a0e4e41
### Kjp Kouvola vs Kopa
- Date/time: 2026-05-22 15:30
- League/phase: finland-kolmonen / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.75
- Fair odds: 2.87
- Model probability: 0.3488
- Probability band: 0.25-0.35

## paper_test_picks

# Paper Test Picks
Observation-only picks. These are not real-money recommendations.
This run uses expanded volume filters to collect more settlement evidence before tightening rules again.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Baseline coverage observations are not model signals. They exist only to test the pipeline and collect settlement evidence.
Suppressed historical bands and negative-EV controls may be tracked as observations only.
Source used: automatic_forward_value_snapshots
Current paper-test picks: 25
Newly logged paper-test picks: 25
Total logged paper-test rows: 502
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 189, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 87, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 502, 'source_used': 'automatic_forward_value_snapshots'}
- Sexypoxyt vs PPJ/Ruoholahti | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kjp Kouvola vs Kopa | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- HJK Akatemia vs FC Lahti | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Chomutov vs FK Seko Louny | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SJK Akatemia vs FC Haka Valkeakoski | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.1 | prob=0.3772 | EV=0.5465 | edge=0.1333 | penalty=0.5465 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al Jazira (UAE) vs Al Ain FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- HNK Hajduk Split vs HNK Vukovar 1991 | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ajel de Rufisque vs ASC Linguere | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- ASAC Concorde vs Garde | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SC Red Star Penzing vs SK Slovan HAC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Vg-62 vs Jyty Turku | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.75 | prob=0.274 | EV=0.5755 | edge=0.1001 | penalty=0.5755 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AB Gladsaxe vs HIK Hellerup | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.75 | prob=0.274 | EV=0.5755 | edge=0.1001 | penalty=0.5755 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Tampereen Ilves vs HPS | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.7 | prob=0.3772 | EV=0.3956 | edge=0.1069 | penalty=0.3956 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- NK Kustosija Zagreb vs NK Uljanik | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Pafos FC vs APOEL Nikosia | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mps vs Leppavaaran Pallo | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Zeleznicar Pancevo vs FK Cukaricki Belgrade | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Broendby IF vs Kolding IF | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

## probability_calibration_layer

# Probability Calibration Layer
Prediction rows: 7
Band rules available: 4
- 0.00-0.35 | very_strong_shrink | adjustments=13
- 0.35-0.45 | monitor_hold | adjustments=6
- 0.45-0.50 | none | adjustments=1
- 0.50-0.55 | small_sample_shrink | adjustments=1

## probability_calibration_impact

# Probability Calibration Impact Report
- 0.00-0.35 | action=very_strong_shrink | rows=13 | avg_raw_prob=0.2798 | avg_multiplier=0.82
- 0.35-0.45 | action=monitor_hold | rows=6 | avg_raw_prob=0.4002 | avg_multiplier=1.01
- 0.45-0.50 | action=none | rows=1 | avg_raw_prob=0.4554 | avg_multiplier=1.0
- 0.50-0.55 | action=small_sample_shrink | rows=1 | avg_raw_prob=0.5062 | avg_multiplier=0.96

## clv_trend

# CLV Trend Report
Rows: 210
Average CLV delta: -0.8542
Beat closing line rate: 0.419
Positive CLV rows: 88
Negative CLV rows: 122
CLV interpretation: negative_clv_signal

## clv_probability_bands

# CLV Probability Band Report
- 0.00-0.35 | rows=39 | avg_clv=-1.5456 | beat_rate=0.2564 | avg_ev=-0.007
- 0.35-0.45 | rows=18 | avg_clv=-0.0739 | beat_rate=0.6111 | avg_ev=0.774
- 0.45-0.50 | rows=3 | avg_clv=0.1533 | beat_rate=1.0 | avg_ev=-0.2455
- 0.50-0.55 | rows=3 | avg_clv=-0.33 | beat_rate=0.3333 | avg_ev=0.4087

## signal_suppression_rules

# Signal Suppression Rules
Research-only guardrails generated from settled proxy/paper diagnostics.
- probability_band=0.00-0.35 | action=suppress | avg_clv_delta=-1.5456 with rows=39
- probability_band=0.35-0.45 | action=monitor | healthier watchlist band: avg_clv_delta=-0.0739, beat_rate=0.6111, rows=18

## rule_action_summary

# Rule Action Summary
- monitor: 1 rule(s) | targets=0.35-0.45
- suppress: 1 rule(s) | targets=0.00-0.35

## phase_performance

# Sample Phase Performance Report
Separates historical proxy research from paper forward-testing diagnostics.
- historical_proxy_research | settled=21 | avg_roi=-0.0786 | clv_rows=21 | avg_clv=-1.3638 | beat_rate=0.3333 | usage=diagnostics_only_not_forward_validation
- unknown | settled=189 | avg_roi=-0.0095 | clv_rows=189 | avg_clv=-0.7976 | beat_rate=0.4286 | usage=diagnostics_only

## model_adjustment

# Model Adjustment Recommendation
## Flags
- High probability bands are currently negative ROI.
- Lower probability bands are currently performing better.
- Probability calibration gap is material.
- Toxic CLV probability band detected: 0.00-0.35 clv=-1.5456, beat_rate=0.2564
- Toxic CLV probability band detected: 0.50-0.55 clv=-0.33, beat_rate=0.3333
- Best league so far: premier_league avg_roi=-0.0786
- Worst league so far: premier_league avg_roi=-0.0786
- CLV beat rate below 50%: 0.419
- CLV trend materially negative: -0.8542
## Recommended model changes
- Reduce confidence in favorites and add extra shrinkage above 0.50 probability.
- Investigate underdog/moderate-price markets before expanding favorite exposure.
- Prioritize probability calibration before adding complex model features.
- Suppress or heavily downweight toxic probability bands during candidate selection.
- Treat all recommendations as paper-tracking until CLV improves above neutral.
- Reduce EV aggressiveness and tighten market-alignment filters.
## Suggested suppression targets
- probability_above_0.50
- 0.00-0.35
- 0.50-0.55

## market_alignment

# Market Alignment Report
Total usable rows: 21
Average alignment gap: 0.1107
Median alignment gap: 0.0964
Market alignment status: moderate_alignment

## market_proxy_quality

# Market Proxy Quality Report
Rows: 30
Average overround: 1.0294
Median overround: 1.0291
Min overround: 1.0266
Max overround: 1.0375
Market proxy quality: reasonable_market_proxy

## probability_distribution

# Probability Distribution Report
Count: 21
Mean probability: 0.3333
Max probability: 0.5455
Min probability: 0.2191
Std probability: 0.1099
Probability distribution is within conservative guardrails.

## historical_coverage

# Historical Coverage Report
Total matches: 5330
Total leagues: 5
Total seasons: 3
## Coverage
- 2223 | bundesliga | matches=306
- 2223 | la_liga | matches=380
- 2223 | ligue_1 | matches=380
- 2223 | premier_league | matches=380
- 2223 | serie_a | matches=380
- 2324 | bundesliga | matches=306
- 2324 | la_liga | matches=380
- 2324 | ligue_1 | matches=306
- 2324 | premier_league | matches=380
- 2324 | serie_a | matches=380
- 2425 | bundesliga | matches=306
- 2425 | la_liga | matches=380
- 2425 | ligue_1 | matches=306
- 2425 | premier_league | matches=380
- 2425 | serie_a | matches=380
