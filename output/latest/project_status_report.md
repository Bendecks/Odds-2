# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-13T14:12:44.138180+00:00`
GitHub run: `342` attempt `1`
GitHub SHA: `9b4f4e26825ab16cb2a8fd3fd9fe62ad23e1e537`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 17 |  |  |
| Football-Data upcoming odds proxy | True | 51 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 52 |  |  |
| odds-api.io forward fixtures | True | 346 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 384 |  |  |
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
- Forward fixture predictions: 278
- Automatic value snapshots: 171
- Positive EV proxy rows: 81
- Proxy observation rows: 25
- Valid forward/proxy log rows: 129
- Deduped forward/proxy log rows: 75
- Duplicate forward/proxy log rows identified: 54
- Fresh API match coverage rate: 0.1403
- Matches with fresh API price: 39
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
Current: 171 value snapshots; fresh API coverage rate 0.1403.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 75 deduped forward/proxy rows; 54 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 26
Upcoming fixture rows: 3
Proxy price rows: 9
Sources attempted: 1
Errors: 0
- 2026-05-14 18:00 | Valencia vs Vallecano | football_data_bet365_proxy | 2.2/3.4/3.3
- 2026-05-14 18:00 | Valencia vs Vallecano | football_data_max_market_proxy | 2.25/3.4/3.4
- 2026-05-14 18:00 | Valencia vs Vallecano | football_data_average_market_proxy | 2.17/3.33/3.23
- 2026-05-14 19:00 | Girona vs Sociedad | football_data_bet365_proxy | 2.05/3.8/3.3
- 2026-05-14 19:00 | Girona vs Sociedad | football_data_max_market_proxy | 2.1/3.8/3.35
- 2026-05-14 19:00 | Girona vs Sociedad | football_data_average_market_proxy | 2.06/3.64/3.21
- 2026-05-14 20:30 | Real Madrid vs Oviedo | football_data_bet365_proxy | 1.22/7.0/11.0
- 2026-05-14 20:30 | Real Madrid vs Oviedo | football_data_max_market_proxy | 1.26/7.0/11.5
- 2026-05-14 20:30 | Real Madrid vs Oviedo | football_data_average_market_proxy | 1.23/6.28/10.42

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 278
Fixture team rows unmatched: 541
Ready for model-fixture join: False
Automatic forward price rows: 48
odds-api.io price rows: 39
Football-Data price rows: 9
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AC Goianiense GO | suggestion=nan | type=unmatched
- CA Paranaense PR | suggestion=nan | type=unmatched
- AD Confianca SE | suggestion=nan | type=unmatched
- Gremio FB Porto Alegrense RS | suggestion=nan | type=unmatched
- AL Draih | suggestion=nan | type=unmatched
- Al Bukiryah | suggestion=nan | type=unmatched
- Al Jahra | suggestion=nan | type=unmatched
- Al-Nasr SC | suggestion=nan | type=unmatched
- AL Naft | suggestion=nan | type=unmatched
- AL Minaa | suggestion=nan | type=unmatched
- AL Naft Maysan | suggestion=nan | type=unmatched
- AL Karma | suggestion=nan | type=unmatched
- Al Nahda | suggestion=nan | type=unmatched
- Al-Seeb | suggestion=nan | type=unmatched
- Al Qadsiah | suggestion=nan | type=unmatched
- Al-Hazm | suggestion=nan | type=unmatched
- AL Ula | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 278
Automatic price rows: 48
Value snapshot rows: 171
Matches with any automatic price: 42
Matches with fresh API price: 39
Matches with odds-api.io price: 39
Fresh API match coverage rate: 0.1403
odds-api.io match coverage rate: 0.1403
Real-money ready: False
## Match coverage
- 2026-05-14 | SJK-J vs FC Kiisto | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | SV Lochau vs FC Wolfurt | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Neroca FC vs Sudeva Delhi FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | FC Barcelona vs CD Tenerife | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-14 | JaPS vs FC KTP | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Sidama Bunna SC vs Hadiya Hossana FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Bjarg vs Brattvaag | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-14 | Hobro IK vs Aarhus Fremad | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365 (no latency)_ML
- 2026-05-14 | IFK Berga vs Rappe GOIF | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-14 | Mtibwa Sugar FC vs Kmc FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Nykopings BIS vs Lindo FF | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-14 | Piteaa IF vs FBK Karlstad | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-14 | Tanzania Prisons vs Fountain Gate FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Torslanda IK vs Qviding FIF | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365 (no latency)_ML
- 2026-05-14 | Tromsdalen UIL vs Grorud IL | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-14 | Tvaakers IF vs BK Olympic | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-14 | Vasalunds IF vs Gefle IF | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 278
Proxy price rows: 48
Matched prediction rows: 45
Value snapshot rows: 171
odds-api.io snapshot rows: 117
Baseline snapshot rows: 153
Full model snapshot rows: 18
Positive EV rows: 81
Source counts: {'odds_api_io_Bet365_ML': 111, 'football_data_bet365_proxy': 18, 'football_data_max_market_proxy': 18, 'football_data_average_market_proxy': 18, 'odds_api_io_Bet365 (no latency)_ML': 6}
- 2026-05-14 | FC Salzburg Frauen vs FK Austria Wien | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3772 | EV=3.1492 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=1.0
- 2026-05-14 | KA Akureyri vs KF Aegir | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=0.96
- 2026-05-14 | IF Karlstad Fotbol vs IFK Stocksund | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-14 | Union Saint-Gilloise vs RSC Anderlecht | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-14 | FK Vidar vs Sotra SK | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3772 | EV=0.886 | match=1.0
- 2026-05-14 | JaPS vs FC KTP | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3772 | EV=0.886 | match=1.0
- 2026-05-14 | Viking FK 2 vs Akra | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 171
Pre-dedupe proxy candidate observation rows: 59
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 5
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-14 | Shire Endaselassie FC vs Ethiopian Coffee SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-14 | Kjp Kouvola vs Lautp | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-14 | Fauve Azur de Yaounde vs Gazelle FA de Garoua | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-14 | Hobro IK vs Aarhus Fremad | selection=HOME | source=odds_api_io_Bet365 (no latency)_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-14 | Sanat Mes Kerman FC vs Mes Shahr-e Babak | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-14 | SJK-J vs FC Kiisto | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-05-14 | Oppsal IF vs Raade IL | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-05-14 | Mtibwa Sugar FC vs Kmc FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-05-14 | Neroca FC vs Sudeva Delhi FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3488 | EV=0.36032 | edge=0.09239 | penalty=0.3603213603213602 | tier=suppressed_proxy_watchlist | score=0.1216
- 2026-05-14 | Masku vs LTU | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3488 | EV=0.32544 | edge=0.085642 | penalty=0.325439469824212 | tier=suppressed_proxy_watchlist | score=0.1201
- 2026-05-14 | Viking FK 2 vs Akra | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171
- 2026-05-14 | IF Karlstad Fotbol vs IFK Stocksund | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 5
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 10
- ev_above_real_candidate_cap_possible_overconfidence: 9
- probability_or_league_rule_suppressed: 5
- low_probability_band_under_0_35: 5
- watchlist_only_pending_forward_settlement: 2
## Row explanations
- 2026-05-14 | Shire Endaselassie FC vs Ethiopian Coffee SC | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | Kjp Kouvola vs Lautp | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | Fauve Azur de Yaounde vs Gazelle FA de Garoua | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-14 | Hobro IK vs Aarhus Fremad | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-14 | Sanat Mes Kerman FC vs Mes Shahr-e Babak | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-14 | SJK-J vs FC Kiisto | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | Oppsal IF vs Raade IL | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | Mtibwa Sugar FC vs Kmc FC | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | Neroca FC vs Sudeva Delhi FC | sel=AWAY | score=0.1216 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | Masku vs LTU | sel=AWAY | score=0.1201 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | Viking FK 2 vs Akra | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | IF Karlstad Fotbol vs IFK Stocksund | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 171
Paper proxy observation rows: 25
Positive EV value rows: 81
Suppressed-band observation rows: 0
Distinct matches: 23
Distinct sources: 0
Max EV: 0.72072
Average EV: 0.40504
Max probability edge: 0.146413
Average match confidence: None
## By selection
- away: rows=14, avg_ev=0.3074, max_ev=0.6568
- draw: rows=7, avg_ev=0.5778, max_ev=0.7207
- home: rows=4, avg_ev=0.4443, max_ev=0.6344

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 278
Forward fixture prediction rows: 278
Full model prediction rows: 2
Baseline prediction rows: 276
Max forward predictions: 300
Ready for price join: True
- 2026-05-14 08:00 | SJK-J vs FC Kiisto | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 09:00 | SV Lochau vs FC Wolfurt | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 09:30 | Neroca FC vs Sudeva Delhi FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 10:00 | FC Barcelona vs CD Tenerife | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 10:00 | JaPS vs FC KTP | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 10:00 | Sidama Bunna SC vs Hadiya Hossana FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Bjarg vs Brattvaag | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Hobro IK vs Aarhus Fremad | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | IFK Berga vs Rappe GOIF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Mtibwa Sugar FC vs Kmc FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Nykopings BIS vs Lindo FF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Piteaa IF vs FBK Karlstad | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Tanzania Prisons vs Fountain Gate FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Torslanda IK vs Qviding FIF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Tromsdalen UIL vs Grorud IL | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Tvaakers IF vs BK Olympic | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Vasalunds IF vs Gefle IF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 11:00 | Vastra Frolunda IF vs IK Kongahalla | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 12:00 | Ellidi vs Vaengir Jupiters | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 12:00 | Hinna vs FK Haugesund 2 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 12:00 | HPS II vs FC Honka | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 278
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 712
Log type: probability_only_no_market_prices
- 2026-05-15 2026-05-14 18:00:00 | Jeugd Patro Eisden Maasmechelen vs RAAL La Louviere | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 18:00:00 | K Beerschot VA vs Jeugd RWDM Brussels | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 18:00:00 | Maritimo Madeira vs GD Chaves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 18:00:00 | Olympic Club De Charleroi vs Jeugd KV Kortrijk | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 18:00:00 | RFC Liege vs KVC Westerlo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 18:00:00 | Raagsveds IF vs FOC Farsta | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 18:45:00 | Partick Thistle FC vs Dunfermline Athletic FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 18:45:00 | University College Dublin vs Bray Wanderers AFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:00:00 | Leixoes SC vs Lusitania FC Lourosa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:00:00 | Aston Villa vs Liverpool | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:15:00 | Augnablik Kopavogur vs KA Asvellir | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:15:00 | Haukar Hafnarfjordur vs Fjolnir | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:15:00 | Kari vs Hviti Riddarinn | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:15:00 | KH Hlidarendi vs Ymir Kopavogur | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 20:00:00 | Rubio Nu vs Nacional Asuncion | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 20:00:00 | Sportivo Trinidense vs Cerro Porteno | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 23:00:00 | Montevideo City Torque vs Club Nacional de Football | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 23:30:00 | Deportivo La Guaira vs UCV FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-14 15:00:00 | Club America vs Guadalajara | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-14 18:00:00 | Ceara SC CE vs 3B Sport AM | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 278
Manual template rows: 278
Rows with complete manual odds: 0
Rows missing manual odds: 278
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-14 22:00 | AC Goianiense GO vs CA Paranaense PR
- 2026-05-14 22:00 | AD Confianca SE vs Gremio FB Porto Alegrense RS
- 2026-05-14 18:00 | AL Draih vs Al Bukiryah
- 2026-05-14 14:40 | Al Jahra vs Al-Nasr SC
- 2026-05-14 14:30 | AL Naft vs AL Minaa
- 2026-05-14 14:30 | AL Naft Maysan vs AL Karma
- 2026-05-14 16:35 | Al Nahda vs Al-Seeb
- 2026-05-14 18:00 | Al Qadsiah vs Al-Hazm
- 2026-05-14 18:00 | AL Ula vs Al-Zulfi FC
- 2026-05-14 18:00 | Al-Faisaly FC vs Al-Batin
- 2026-05-14 15:55 | Al-Fateh SC vs Al-Najma
- 2026-05-14 18:00 | Al-Ittifaq FC vs Al-Ittihad Club
- 2026-05-14 16:45 | Al-Orobah vs AL Anwar
- 2026-05-14 16:35 | Al-Wehda FC vs Al-Jabalain
- 2026-05-14 18:30 | Alftanes vs KFR

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 278
Source counts: {'odds_api_io_events_bookmaker_filtered': 271, 'football_data_fixtures_proxy': 3, 'odds_api_io_events_search': 3, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-14 22:00 | AC Goianiense GO vs CA Paranaense PR | brazil-copa-do-brasil | odds_api_io_events_bookmaker_filtered
- 2026-05-14 22:00 | AD Confianca SE vs Gremio FB Porto Alegrense RS | brazil-copa-do-brasil | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:00 | AL Draih vs Al Bukiryah | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-14 14:40 | Al Jahra vs Al-Nasr SC | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-14 14:30 | AL Naft vs AL Minaa | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-14 14:30 | AL Naft Maysan vs AL Karma | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-14 16:35 | Al Nahda vs Al-Seeb | oman-omani-league | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:00 | Al Qadsiah vs Al-Hazm | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:00 | AL Ula vs Al-Zulfi FC | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:00 | Al-Faisaly FC vs Al-Batin | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-14 15:55 | Al-Fateh SC vs Al-Najma | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:00 | Al-Ittifaq FC vs Al-Ittihad Club | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-14 16:45 | Al-Orobah vs AL Anwar | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-14 16:35 | Al-Wehda FC vs Al-Jabalain | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:30 | Alftanes vs KFR | iceland-4-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-14 19:00 | Always Ready vs The Strongest | bolivia-division-profesional | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:00 | America FC MG vs EC Bahia BA | brazil-u20-campeonato-brasileiro | odds_api_io_events_bookmaker_filtered
- 2026-05-14 14:00 | Angelholms FF vs Aatvidabergs FF | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-14 17:00 | Arborg vs Alafoss | iceland-4-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-14 15:00 | AS Fortuna vs Coton Sport de Garoua | cameroon-elite-one | odds_api_io_events_bookmaker_filtered
- 2026-05-14 13:00 | Assyriska FF vs Umea FC | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:00 | Atletico Mineiro MG vs Mirassol FC SP | brazil-u20-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-14 15:00 | Austria Lustenau vs SKU Amstetten | austria-2-liga | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 278
Rows with complete odds: 0
- 2026-05-14 22:00 | AC Goianiense GO vs CA Paranaense PR | bookmaker=bet365_manual
- 2026-05-14 22:00 | AD Confianca SE vs Gremio FB Porto Alegrense RS | bookmaker=bet365_manual
- 2026-05-14 18:00 | AL Draih vs Al Bukiryah | bookmaker=bet365_manual
- 2026-05-14 14:40 | Al Jahra vs Al-Nasr SC | bookmaker=bet365_manual
- 2026-05-14 14:30 | AL Naft vs AL Minaa | bookmaker=bet365_manual
- 2026-05-14 14:30 | AL Naft Maysan vs AL Karma | bookmaker=bet365_manual
- 2026-05-14 16:35 | Al Nahda vs Al-Seeb | bookmaker=bet365_manual
- 2026-05-14 18:00 | Al Qadsiah vs Al-Hazm | bookmaker=bet365_manual
- 2026-05-14 18:00 | AL Ula vs Al-Zulfi FC | bookmaker=bet365_manual
- 2026-05-14 18:00 | Al-Faisaly FC vs Al-Batin | bookmaker=bet365_manual
- 2026-05-14 15:55 | Al-Fateh SC vs Al-Najma | bookmaker=bet365_manual
- 2026-05-14 18:00 | Al-Ittifaq FC vs Al-Ittihad Club | bookmaker=bet365_manual
- 2026-05-14 16:45 | Al-Orobah vs AL Anwar | bookmaker=bet365_manual
- 2026-05-14 16:35 | Al-Wehda FC vs Al-Jabalain | bookmaker=bet365_manual
- 2026-05-14 18:30 | Alftanes vs KFR | bookmaker=bet365_manual
- 2026-05-14 19:00 | Always Ready vs The Strongest | bookmaker=bet365_manual
- 2026-05-14 18:00 | America FC MG vs EC Bahia BA | bookmaker=bet365_manual
- 2026-05-14 14:00 | Angelholms FF vs Aatvidabergs FF | bookmaker=bet365_manual
- 2026-05-14 17:00 | Arborg vs Alafoss | bookmaker=bet365_manual
- 2026-05-14 15:00 | AS Fortuna vs Coton Sport de Garoua | bookmaker=bet365_manual
- 2026-05-14 13:00 | Assyriska FF vs Umea FC | bookmaker=bet365_manual
- 2026-05-14 18:00 | Atletico Mineiro MG vs Mirassol FC SP | bookmaker=bet365_manual
- 2026-05-14 15:00 | Austria Lustenau vs SKU Amstetten | bookmaker=bet365_manual
- 2026-05-14 15:30 | Azam FC vs Pamba Jiji SC | bookmaker=bet365_manual

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
- 2026-05-14 22:00 | AC Goianiense GO vs CA Paranaense PR
- 2026-05-14 22:00 | AD Confianca SE vs Gremio FB Porto Alegrense RS
- 2026-05-14 18:00 | AL Draih vs Al Bukiryah
- 2026-05-14 14:40 | Al Jahra vs Al-Nasr SC
- 2026-05-14 14:30 | AL Naft vs AL Minaa
- 2026-05-14 14:30 | AL Naft Maysan vs AL Karma
- 2026-05-14 16:35 | Al Nahda vs Al-Seeb
- 2026-05-14 18:00 | Al Qadsiah vs Al-Hazm
- 2026-05-14 18:00 | AL Ula vs Al-Zulfi FC
- 2026-05-14 18:00 | Al-Faisaly FC vs Al-Batin
- 2026-05-14 15:55 | Al-Fateh SC vs Al-Najma
- 2026-05-14 18:00 | Al-Ittifaq FC vs Al-Ittihad Club
- 2026-05-14 16:45 | Al-Orobah vs AL Anwar
- 2026-05-14 16:35 | Al-Wehda FC vs Al-Jabalain
- 2026-05-14 18:30 | Alftanes vs KFR
- 2026-05-14 19:00 | Always Ready vs The Strongest
- 2026-05-14 18:00 | America FC MG vs EC Bahia BA
- 2026-05-14 14:00 | Angelholms FF vs Aatvidabergs FF
- 2026-05-14 17:00 | Arborg vs Alafoss

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 132
Valid forward/proxy log rows: 129
Deduped forward/proxy observation rows: 75
Duplicate forward/proxy log rows: 54
Valid automatic proxy observation rows: 129
Deduped automatic proxy observation rows: 75
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.06810000000000001
- 2026-05-14 | Real Madrid vs Oviedo | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0675
- 2026-05-14 | Real Madrid vs Real Oviedo | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0675
- 2026-05-14 | KA Akureyri vs KF Aegir | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0673
- 2026-05-14 | FK Septemvri Sofia vs FK Spartak 1918 Varna | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0673
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.067
- 2026-05-12 | AL Faisaly (Jor) vs Ramtha SC | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.067
- 2026-05-14 | JaPS vs FC KTP | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.066
- 2026-05-14 | Mtibwa Sugar FC vs Kmc FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0632
- 2026-05-14 | FC Salzburg Frauen vs FK Austria Wien | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0631
- 2026-05-14 | Neroca FC vs Sudeva Delhi FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0623
- 2026-05-14 | Masku vs LTU | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0614
- 2026-05-14 | Shire Endaselassie FC vs Ethiopian Coffee SC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-14 | IF Karlstad Fotbol vs IFK Stocksund | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-14 | Viking FK 2 vs Akra | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-14 | Herentals FC vs Dynamos Harare FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | IF Vestri vs Grotta | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Trelleborgs FF vs Jonkopings Sodra IF | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Kjp Kouvola vs Lautp | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Ntnui vs Orkla | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.058600000000000006

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
### Girona vs Sociedad
- Date/time: 2026-05-14 19:00
- League/phase: la_liga / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 3.35
- Fair odds: 3.03
- Model probability: 0.3305
- Probability band: 0.25-0.35
- EV: 0.1072
- Probability edge: 0.032
- Alignment penalty: 0.1072
- Suppression action: none
- Paper tier: priority_proxy_observation
- Paper score: 0.2441
- Prediction ID: 24bd77f085ea78e07dc9
### Girona vs Sociedad
- Date/time: 2026-05-14 19:00
- League/phase: la_liga / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 3.3
- Fair odds: 3.03
- Model probability: 0.3305
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
Newly logged paper-test picks: 20
Total logged paper-test rows: 132
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 171, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 73, 'current_paper_picks': 25, 'newly_logged_picks': 20, 'total_logged_paper_rows': 132, 'source_used': 'automatic_forward_value_snapshots'}
- Girona vs Sociedad | coverage=full_team_strength_match | selection=AWAY | odds=3.35 | prob=0.3305 | EV=0.1072 | edge=0.032 | penalty=0.1072 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Girona vs Sociedad | coverage=full_team_strength_match | selection=AWAY | odds=3.3 | prob=0.3305 | EV=0.0906 | edge=0.0275 | penalty=0.0907 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Valencia vs Vallecano | coverage=full_team_strength_match | selection=AWAY | odds=3.4 | prob=0.3215 | EV=0.0931 | edge=0.0274 | penalty=0.0931 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Valencia vs Vallecano | coverage=full_team_strength_match | selection=AWAY | odds=3.3 | prob=0.3215 | EV=0.0609 | edge=0.0185 | penalty=0.061 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- SJK-J vs FC Kiisto | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Oppsal IF vs Raade IL | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Red Arrows vs Green Eagles | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Sidama Bunna SC vs Hadiya Hossana FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.28 | prob=0.274 | EV=0.7207 | edge=0.1148 | penalty=0.7207 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.28 | prob=0.274 | EV=0.7207 | edge=0.1148 | penalty=0.7207 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Septemvri Sofia vs FK Spartak 1918 Varna | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- KA Akureyri vs KF Aegir | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- JaPS vs FC KTP | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mtibwa Sugar FC vs Kmc FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Salzburg Frauen vs FK Austria Wien | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Neroca FC vs Sudeva Delhi FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Masku vs LTU | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Shire Endaselassie FC vs Ethiopian Coffee SC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.4 | prob=0.3772 | EV=0.2825 | edge=0.0831 | penalty=0.2825 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
