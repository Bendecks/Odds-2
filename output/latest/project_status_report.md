# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-16T13:05:59.703526+00:00`
GitHub run: `353` attempt `1`
GitHub SHA: `4ba911ea45d87d2e44695f136f1f19b7cbf486a5`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 107 |  |  |
| Football-Data upcoming odds proxy | True | 316 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 41 |  |  |
| odds-api.io forward fixtures | True | 903 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 615 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
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
- Automatic value snapshots: 675
- Positive EV proxy rows: 348
- Proxy observation rows: 25
- Valid forward/proxy log rows: 260
- Deduped forward/proxy log rows: 173
- Duplicate forward/proxy log rows identified: 87
- Fresh API match coverage rate: 0.1867
- Matches with fresh API price: 56
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
Current: 675 value snapshots; fresh API coverage rate 0.1867.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 173 deduped forward/proxy rows; 87 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 112
Upcoming fixture rows: 107
Proxy price rows: 316
Sources attempted: 1
Errors: 0
- 2026-05-16 15:00 | Charleroi vs Westerlo | football_data_bet365_proxy | 1.95/3.5/3.25
- 2026-05-16 15:00 | Charleroi vs Westerlo | football_data_max_market_proxy | 2.05/3.8/3.35
- 2026-05-16 15:00 | Charleroi vs Westerlo | football_data_average_market_proxy | 2.0/3.6/3.23
- 2026-05-16 17:15 | Standard vs Genk | football_data_bet365_proxy | 3.1/3.4/2.1
- 2026-05-16 17:15 | Standard vs Genk | football_data_max_market_proxy | 3.2/3.6/2.2
- 2026-05-16 17:15 | Standard vs Genk | football_data_average_market_proxy | 3.08/3.43/2.12
- 2026-05-16 19:45 | St Truiden vs Gent | football_data_bet365_proxy | 1.91/3.6/3.5
- 2026-05-16 19:45 | St Truiden vs Gent | football_data_max_market_proxy | 1.95/4.0/3.6
- 2026-05-16 19:45 | St Truiden vs Gent | football_data_average_market_proxy | 1.92/3.67/3.4
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_bet365_proxy | 1.83/3.6/3.75
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_max_market_proxy | 1.87/4.0/4.0
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_average_market_proxy | 1.8/3.72/3.79
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_bet365_proxy | 2.05/3.5/3.1
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_max_market_proxy | 2.1/3.8/3.45
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_average_market_proxy | 2.02/3.51/3.23
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | football_data_bet365_proxy | 1.14/9.5/14.0
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | football_data_max_market_proxy | 1.18/9.5/16.0
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | football_data_average_market_proxy | 1.14/8.71/12.84
- 2026-05-16 14:30 | Ein Frankfurt vs Stuttgart | football_data_bet365_proxy | 3.4/4.33/1.85
- 2026-05-16 14:30 | Ein Frankfurt vs Stuttgart | football_data_max_market_proxy | 3.5/4.33/1.91
- 2026-05-16 14:30 | Ein Frankfurt vs Stuttgart | football_data_average_market_proxy | 3.35/4.22/1.86
- 2026-05-16 14:30 | Freiburg vs RB Leipzig | football_data_bet365_proxy | 2.7/4.0/2.3
- 2026-05-16 14:30 | Freiburg vs RB Leipzig | football_data_max_market_proxy | 2.75/4.0/2.37

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 707
Fixture team rows unmatched: 1296
Ready for model-fixture join: False
Automatic forward price rows: 372
odds-api.io price rows: 56
Football-Data price rows: 316
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- Arouca | suggestion=nan | type=unmatched
- Tondela | suggestion=nan | type=unmatched
- Asteras Tripolis | suggestion=nan | type=unmatched
- Kifisia | suggestion=nan | type=unmatched
- Atletico Mineiro MG | suggestion=nan | type=unmatched
- Mirassol FC SP | suggestion=nan | type=unmatched
- Brooklyn FC | suggestion=nan | type=unmatched
- Hartford Athletic | suggestion=nan | type=unmatched
- CA Penarol Montevideo | suggestion=nan | type=unmatched
- Liverpool Montevideo | suggestion=nan | type=unmatched
- CA River Plate (ARG) | suggestion=nan | type=unmatched
- CA Rosario Central | suggestion=nan | type=unmatched
- Capital CF DF | suggestion=nan | type=unmatched
- Ceilandia EC DF | suggestion=nan | type=unmatched
- Carolina Ascent | suggestion=nan | type=unmatched
- Sporting Jacksonville | suggestion=nan | type=unmatched
- Carolina Core FC | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 372
Value snapshot rows: 675
Matches with any automatic price: 99
Matches with fresh API price: 56
Matches with odds-api.io price: 56
Fresh API match coverage rate: 0.1867
odds-api.io match coverage rate: 0.1867
Real-money ready: False
## Match coverage
- 2026-05-16 | Celtic vs Hearts | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Falkirk vs Rangers | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Hibernian vs Motherwell | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Sociedad B vs Mirandes | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Bayern Munich vs FC Koln | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Ein Frankfurt vs Stuttgart | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Freiburg vs RB Leipzig | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Heidenheim vs Mainz | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Leverkusen vs Hamburg | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | M'gladbach vs Hoffenheim | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | St Pauli vs Wolfsburg | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Union Berlin vs Augsburg | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Werder Bremen vs Dortmund | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Charleroi vs Westerlo | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Karagumruk vs Alanyaspor | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Ceuta vs Malaga | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Cultural Leonesa vs Eibar | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 372
Matched prediction rows: 114
Value snapshot rows: 675
odds-api.io snapshot rows: 171
Baseline snapshot rows: 549
Full model snapshot rows: 126
Positive EV rows: 348
Source counts: {'football_data_max_market_proxy': 171, 'football_data_average_market_proxy': 171, 'odds_api_io_Bet365_ML': 171, 'football_data_bet365_proxy': 162}
- 2026-05-16 | Cerro Porteno vs Recoleta FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3488 | EV=16.7888 | match=1.0
- 2026-05-16 | Cerro Porteno vs Recoleta FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=23.0 | prob=0.274 | EV=5.302 | match=1.0
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=0.92
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.92
- 2026-05-16 | Sp Lisbon vs Gil Vicente | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3217 | EV=3.1821 | match=1.0
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3488 | EV=2.955392 | match=0.92
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3217 | EV=2.8604 | match=1.0
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=16.0 | prob=0.2402 | EV=2.8432 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3217 | EV=2.648078 | match=1.0
- 2026-05-16 | Porto vs Santa Clara | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=10.25 | prob=0.3488 | EV=2.5752 | match=1.0
- 2026-05-16 | Sp Lisbon vs Gil Vicente | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.07 | prob=0.3488 | EV=2.512416 | match=1.0
- 2026-05-16 | Sp Lisbon vs Gil Vicente | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-05-16 | Estoril vs Benfica | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Pisa SC vs SSC Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=0.92
- 2026-05-17 | Pisa SC vs SSC Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=0.92

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 675
Pre-dedupe proxy candidate observation rows: 248
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-17 | Houston Dynamo vs Vancouver Whitecaps FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-16 | Fort Wayne FC vs Indy Eleven | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-16 | Lagarto FC SE vs CS Sergipe SE | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-17 | Corpus Christi FC vs FC Tulsa | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-16 | Chattanooga Red Wolves SC vs Birmingham Legion FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-16 | Point Michel vs Middleham United FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-17 | Deportes Limache vs CD Universidad Catolica | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-16 | Falkirk vs Rangers | selection=HOME | source=football_data_average_market_proxy | odds=3.82 | prob=0.3772 | EV=0.440904 | edge=0.11542 | penalty=0.44090457636183045 | tier=proxy_watchlist | score=0.2276
- 2026-05-17 | Oakland Roots SC vs Sacramento Republic FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-16 | Ceuta vs Malaga | selection=HOME | source=football_data_bet365_proxy | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2257
- 2026-05-16 | Floresta EC CE vs Amazonas FC AM | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-17 | FC Western vs Upper Hutt City FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223

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
- watchlist_only_pending_forward_settlement: 3
- delayed_football_data_proxy_not_fresh_api_price: 2
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-17 | Houston Dynamo vs Vancouver Whitecaps FC | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Fort Wayne FC vs Indy Eleven | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Lagarto FC SE vs CS Sergipe SE | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Corpus Christi FC vs FC Tulsa | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Chattanooga Red Wolves SC vs Birmingham Legion FC | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Point Michel vs Middleham United FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-17 | Deportes Limache vs CD Universidad Catolica | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | Falkirk vs Rangers | sel=HOME | score=0.2276 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-17 | Oakland Roots SC vs Sacramento Republic FC | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | Ceuta vs Malaga | sel=HOME | score=0.2257 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-16 | Floresta EC CE vs Amazonas FC AM | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-17 | FC Western vs Upper Hutt City FC | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 675
Paper proxy observation rows: 25
Positive EV value rows: 348
Suppressed-band observation rows: 0
Distinct matches: 13
Distinct sources: 0
Max EV: 0.77765
Average EV: 0.318808
Max probability edge: 0.148124
Average match confidence: None
## By selection
- away: rows=6, avg_ev=0.4207, max_ev=0.7776
- draw: rows=13, avg_ev=0.2476, max_ev=0.5847
- home: rows=6, avg_ev=0.3713, max_ev=0.6718

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 707
Forward fixture prediction rows: 300
Full model prediction rows: 14
Baseline prediction rows: 286
Max forward predictions: 300
Ready for price join: True
- 2026-05-16 12:30 | Celtic vs Hearts | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 12:30 | Falkirk vs Rangers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 12:30 | Hibernian vs Motherwell | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:00 | Sociedad B vs Mirandes | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | H=0.5122 D=0.2477 A=0.2402 | fair=1.95/4.04/4.16
- 2026-05-16 14:30 | Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | H=0.3716 D=0.2659 A=0.3625 | fair=2.69/3.76/2.76
- 2026-05-16 14:30 | Freiburg vs RB Leipzig | coverage=full_team_strength_match | H=0.3796 D=0.2767 A=0.3437 | fair=2.63/3.61/2.91
- 2026-05-16 14:30 | Heidenheim vs Mainz | coverage=full_team_strength_match | H=0.3531 D=0.2725 A=0.3743 | fair=2.83/3.67/2.67
- 2026-05-16 14:30 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 14:30 | M'gladbach vs Hoffenheim | coverage=full_team_strength_match | H=0.4111 D=0.257 A=0.3318 | fair=2.43/3.89/3.01
- 2026-05-16 14:30 | St Pauli vs Wolfsburg | coverage=full_team_strength_match | H=0.3484 D=0.2858 A=0.3658 | fair=2.87/3.5/2.73
- 2026-05-16 14:30 | Union Berlin vs Augsburg | coverage=full_team_strength_match | H=0.3819 D=0.2746 A=0.3435 | fair=2.62/3.64/2.91
- 2026-05-16 14:30 | Werder Bremen vs Dortmund | coverage=full_team_strength_match | H=0.3487 D=0.2614 A=0.3899 | fair=2.87/3.82/2.56
- 2026-05-16 15:00 | Charleroi vs Westerlo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 15:00 | Karagumruk vs Alanyaspor | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 15:15 | Ceuta vs Malaga | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 15:15 | Cultural Leonesa vs Eibar | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 15:30 | Moreirense vs AVS | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 15:30 | Porto vs Santa Clara | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 17:00 | Asteras Tripolis vs Kifisia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 17:00 | Larisa vs Atromitos | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 1714
Log type: probability_only_no_market_prices
- 2026-05-17 2026-05-16 12:00:00 | TSG Hoffenheim vs RB Leipzig | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:00:00 | VfL Wolfsburg vs 1. FC Nuremberg | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:00:00 | Wisla Plock II vs ZKS Olimpia Elblag | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:00:00 | FC Zhenis vs FC Kairat Almaty | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:10:00 | Heart of Midlothian WFC vs Glasgow City LFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:15:00 | Cong An Ha Noi FC vs Dong A Thanh Hoa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:15:00 | Kuching City FC vs Kuala Lumpur City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | Anderlecht vs Mechelen | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | Dedza Dynamos FC vs Blue Eagles Malawi | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | FK Austria Wien vs LASK Linz | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | Heracles Almelo vs FC Groningen | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | Kolos Kovalivka vs FC Obolon Kyiv | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | Man United vs Nott'm Forest | H=0.39590000000000003 D=0.2656 A=0.3386
- 2026-05-17 2026-05-16 12:30:00 | Miedz Legnica vs Ruch Chorzow | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | NEC Nijmegen vs Go Ahead Eagles | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | PEC Zwolle vs Feyenoord Rotterdam | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | PSV Eindhoven vs FC Twente Enschede | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | FC Salzburg vs TSV Hartberg | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | SC Heerenveen vs Ajax Amsterdam | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-16 12:30:00 | Silver Strikers vs Masters FC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 707
Manual template rows: 707
Rows with complete manual odds: 0
Rows missing manual odds: 707
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-16 17:30 | Almeria vs Las Palmas
- 2026-05-16 18:00 | Arouca vs Tondela
- 2026-05-16 17:00 | Asteras Tripolis vs Kifisia
- 2026-05-16 21:30 | Atletico Mineiro MG vs Mirassol FC SP
- 2026-05-16 14:30 | Bayern Munich vs FC Koln
- 2026-05-16 23:00 | Brooklyn FC vs Hartford Athletic
- 2026-05-16 21:30 | CA Penarol Montevideo vs Liverpool Montevideo
- 2026-05-16 22:30 | CA River Plate (ARG) vs CA Rosario Central
- 2026-05-16 22:00 | Capital CF DF vs Ceilandia EC DF
- 2026-05-16 23:00 | Carolina Ascent vs Sporting Jacksonville
- 2026-05-16 22:00 | Carolina Core FC vs Chicago Fire FC II
- 2026-05-16 18:00 | Casa Pia vs Rio Ave
- 2026-05-16 21:30 | CD O´Higgins vs Universidad de Concepcion
- 2026-05-16 23:00 | CD Tolima vs Atletico Nacional Medellin
- 2026-05-16 21:30 | CD Universidad Catolica del Ecuador vs Delfin SC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 707
Source counts: {'odds_api_io_events_bookmaker_filtered': 595, 'football_data_fixtures_proxy': 107, 'odds_api_io_events_search': 5}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-16 17:30 | Almeria vs Las Palmas | SP2 | football_data_fixtures_proxy
- 2026-05-16 18:00 | Arouca vs Tondela | P1 | football_data_fixtures_proxy
- 2026-05-16 17:00 | Asteras Tripolis vs Kifisia | G1 | football_data_fixtures_proxy
- 2026-05-16 21:30 | Atletico Mineiro MG vs Mirassol FC SP | brazil-brasileiro-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | bundesliga | football_data_fixtures_proxy
- 2026-05-16 23:00 | Brooklyn FC vs Hartford Athletic | usa-usl-league-one-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-16 21:30 | CA Penarol Montevideo vs Liverpool Montevideo | uruguay-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-16 22:30 | CA River Plate (ARG) vs CA Rosario Central | argentina-liga-profesional | odds_api_io_events_bookmaker_filtered
- 2026-05-16 22:00 | Capital CF DF vs Ceilandia EC DF | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-16 23:00 | Carolina Ascent vs Sporting Jacksonville | usa-usl-super-league-women | odds_api_io_events_bookmaker_filtered
- 2026-05-16 22:00 | Carolina Core FC vs Chicago Fire FC II | usa-mls-next-pro | odds_api_io_events_bookmaker_filtered
- 2026-05-16 18:00 | Casa Pia vs Rio Ave | P1 | football_data_fixtures_proxy
- 2026-05-16 21:30 | CD O´Higgins vs Universidad de Concepcion | chile-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-16 23:00 | CD Tolima vs Atletico Nacional Medellin | colombia-primera-a-apertura | odds_api_io_events_bookmaker_filtered
- 2026-05-16 21:30 | CD Universidad Catolica del Ecuador vs Delfin SC | ecuador-ligapro-primera-a | odds_api_io_events_bookmaker_filtered
- 2026-05-16 12:30 | Celtic vs Hearts | SC0 | football_data_fixtures_proxy
- 2026-05-16 21:30 | Cerro Porteno vs Recoleta FC | paraguay-camopeonato-femenino-women | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:15 | Ceuta vs Malaga | SP2 | football_data_fixtures_proxy
- 2026-05-16 15:00 | Charleroi vs Westerlo | B1 | football_data_fixtures_proxy
- 2026-05-16 23:30 | Charlotte FC vs Toronto FC | usa-mls | odds_api_io_events_bookmaker_filtered
- 2026-05-16 23:00 | Chattanooga Red Wolves SC vs Birmingham Legion FC | usa-usl-league-one-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-16 23:00 | Christos FC vs Lionsbridge FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-16 22:45 | CS Cienciano vs Alianza Lima | peru-liga-1 | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 707
Rows with complete odds: 0
- 2026-05-16 17:30 | Almeria vs Las Palmas | bookmaker=bet365_manual
- 2026-05-16 18:00 | Arouca vs Tondela | bookmaker=bet365_manual
- 2026-05-16 17:00 | Asteras Tripolis vs Kifisia | bookmaker=bet365_manual
- 2026-05-16 21:30 | Atletico Mineiro MG vs Mirassol FC SP | bookmaker=bet365_manual
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | bookmaker=bet365_manual
- 2026-05-16 23:00 | Brooklyn FC vs Hartford Athletic | bookmaker=bet365_manual
- 2026-05-16 21:30 | CA Penarol Montevideo vs Liverpool Montevideo | bookmaker=bet365_manual
- 2026-05-16 22:30 | CA River Plate (ARG) vs CA Rosario Central | bookmaker=bet365_manual
- 2026-05-16 22:00 | Capital CF DF vs Ceilandia EC DF | bookmaker=bet365_manual
- 2026-05-16 23:00 | Carolina Ascent vs Sporting Jacksonville | bookmaker=bet365_manual
- 2026-05-16 22:00 | Carolina Core FC vs Chicago Fire FC II | bookmaker=bet365_manual
- 2026-05-16 18:00 | Casa Pia vs Rio Ave | bookmaker=bet365_manual
- 2026-05-16 21:30 | CD O´Higgins vs Universidad de Concepcion | bookmaker=bet365_manual
- 2026-05-16 23:00 | CD Tolima vs Atletico Nacional Medellin | bookmaker=bet365_manual
- 2026-05-16 21:30 | CD Universidad Catolica del Ecuador vs Delfin SC | bookmaker=bet365_manual
- 2026-05-16 12:30 | Celtic vs Hearts | bookmaker=bet365_manual
- 2026-05-16 21:30 | Cerro Porteno vs Recoleta FC | bookmaker=bet365_manual
- 2026-05-16 15:15 | Ceuta vs Malaga | bookmaker=bet365_manual
- 2026-05-16 15:00 | Charleroi vs Westerlo | bookmaker=bet365_manual
- 2026-05-16 23:30 | Charlotte FC vs Toronto FC | bookmaker=bet365_manual
- 2026-05-16 23:00 | Chattanooga Red Wolves SC vs Birmingham Legion FC | bookmaker=bet365_manual
- 2026-05-16 23:00 | Christos FC vs Lionsbridge FC | bookmaker=bet365_manual
- 2026-05-16 22:45 | CS Cienciano vs Alianza Lima | bookmaker=bet365_manual
- 2026-05-16 22:00 | CT United FC vs Toronto FC II | bookmaker=bet365_manual

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
- 2026-05-16 17:30 | Almeria vs Las Palmas
- 2026-05-16 18:00 | Arouca vs Tondela
- 2026-05-16 17:00 | Asteras Tripolis vs Kifisia
- 2026-05-16 21:30 | Atletico Mineiro MG vs Mirassol FC SP
- 2026-05-16 14:30 | Bayern Munich vs FC Koln
- 2026-05-16 23:00 | Brooklyn FC vs Hartford Athletic
- 2026-05-16 21:30 | CA Penarol Montevideo vs Liverpool Montevideo
- 2026-05-16 22:30 | CA River Plate (ARG) vs CA Rosario Central
- 2026-05-16 22:00 | Capital CF DF vs Ceilandia EC DF
- 2026-05-16 23:00 | Carolina Ascent vs Sporting Jacksonville
- 2026-05-16 22:00 | Carolina Core FC vs Chicago Fire FC II
- 2026-05-16 18:00 | Casa Pia vs Rio Ave
- 2026-05-16 21:30 | CD O´Higgins vs Universidad de Concepcion
- 2026-05-16 23:00 | CD Tolima vs Atletico Nacional Medellin
- 2026-05-16 21:30 | CD Universidad Catolica del Ecuador vs Delfin SC
- 2026-05-16 12:30 | Celtic vs Hearts
- 2026-05-16 21:30 | Cerro Porteno vs Recoleta FC
- 2026-05-16 15:15 | Ceuta vs Malaga
- 2026-05-16 15:00 | Charleroi vs Westerlo

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 263
Valid forward/proxy log rows: 260
Deduped forward/proxy observation rows: 173
Duplicate forward/proxy log rows: 87
Valid automatic proxy observation rows: 260
Deduped automatic proxy observation rows: 173
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-15 | Caboolture Sports FC vs North Star | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061
- 2026-05-15 | Caboolture FC vs North Star FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061
- 2026-05-16 | Real Sociedad San Sebastian B vs CD Mirandes | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0606
- 2026-05-14 | Viking FK 2 vs Akra | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-15 | Al Ittihad Ahli of Aleppo vs Al-Shorta SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-16 | Bay Olympic vs Auckland United FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-16 | Belmont Swansea United FC vs Valentine FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-14 | Herentals FC vs Dynamos Harare FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Trelleborgs FF vs Jonkopings Sodra IF | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-15 | PVF Cand B vs Ho Chi Minh City FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-15 | Shanghai Port FC vs Zhejiang FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Kjp Kouvola vs Lautp | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Ntnui vs Orkla | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.058600000000000006
- 2026-05-15 | Melbourne Knights FC vs Eltham Redbacks FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.058600000000000006
- 2026-05-15 | Brisbane Roar FC vs Lions FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Broadmeadow Magic FC vs Newcastle Olympic FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Semen Padang FC vs Persebaya Surabaya | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-15 | Cong An TP Ho Chi Minh City FC vs SHB Da Nang | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577

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
### Genoa vs Milan
- Date/time: 2026-05-17 11:00
- League/phase: serie_a / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.5
- Fair odds: 2.9
- Model probability: 0.3447
- Probability band: 0.25-0.35
- EV: 0.5512
- Probability edge: 0.1225
- Alignment penalty: 0.5512
- Suppression action: none
- Paper tier: volume_observation
- Paper score: 0.2964
- Prediction ID: d9610f99658e74875e25
### Como vs Parma
- Date/time: 2026-05-17 11:00
- League/phase: serie_a / automatic_forward_price_proxy
- Selection: DRAW
- Market odds: 5.69
- Fair odds: 3.59
- Model probability: 0.2785
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
Newly logged paper-test picks: 12
Total logged paper-test rows: 263
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 675, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 329, 'current_paper_picks': 25, 'newly_logged_picks': 12, 'total_logged_paper_rows': 263, 'source_used': 'automatic_forward_value_snapshots'}
- Genoa vs Milan | coverage=full_team_strength_match | selection=HOME | odds=4.5 | prob=0.3447 | EV=0.5512 | edge=0.1225 | penalty=0.5512 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.69 | prob=0.2785 | EV=0.5847 | edge=0.1028 | penalty=0.5847 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.28 | prob=0.2806 | EV=0.4816 | edge=0.0912 | penalty=0.4816 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.25 | prob=0.2785 | EV=0.4621 | edge=0.088 | penalty=0.4621 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.0 | prob=0.2806 | EV=0.403 | edge=0.0806 | penalty=0.403 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Werder Bremen vs Dortmund | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3487 | EV=0.2205 | edge=0.063 | penalty=0.2205 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Werder Bremen vs Dortmund | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3487 | EV=0.2205 | edge=0.063 | penalty=0.2205 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.5 | prob=0.2857 | EV=0.2857 | edge=0.0635 | penalty=0.2857 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Almeria vs Las Palmas | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3314 | EV=0.193 | edge=0.0536 | penalty=0.193 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Almeria vs Las Palmas | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3314 | EV=0.193 | edge=0.0536 | penalty=0.193 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Heidenheim vs Mainz | coverage=full_team_strength_match | selection=AWAY | odds=3.5 | prob=0.3743 | EV=0.31 | edge=0.0886 | penalty=0.3101 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3716 | EV=0.3006 | edge=0.0859 | penalty=0.3006 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- M'gladbach vs Hoffenheim | coverage=full_team_strength_match | selection=DRAW | odds=4.75 | prob=0.257 | EV=0.2208 | edge=0.0465 | penalty=0.2208 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Heidenheim vs Mainz | coverage=full_team_strength_match | selection=AWAY | odds=3.4 | prob=0.3743 | EV=0.2726 | edge=0.0802 | penalty=0.2726 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | selection=HOME | odds=3.4 | prob=0.3716 | EV=0.2634 | edge=0.0775 | penalty=0.2634 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.09 | prob=0.2857 | EV=0.1685 | edge=0.0412 | penalty=0.1685 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Man United vs Nott'm Forest | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.3386 | EV=0.7776 | edge=0.1481 | penalty=0.7777 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Man United vs Nott'm Forest | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.3386 | EV=0.7776 | edge=0.1481 | penalty=0.7777 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation

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
