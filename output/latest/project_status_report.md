# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-31T13:22:43.828168+00:00`
GitHub run: `384` attempt `1`
GitHub SHA: `470c560a365bb85c805dc8e8c2a0488e58682632`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 9 |  |  |
| Football-Data upcoming odds proxy | True | 27 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 58 |  |  |
| odds-api.io forward fixtures | True | 255 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 327 |  |  |
| Forward price coverage report | True | 274 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 3 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 274 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 113
- Automatic value snapshots: 135
- Positive EV proxy rows: 61
- Proxy observation rows: 25
- Valid forward/proxy log rows: 881
- Deduped forward/proxy log rows: 700
- Duplicate forward/proxy log rows identified: 181
- Fresh API match coverage rate: 0.3894
- Matches with fresh API price: 44
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
Current: 135 value snapshots; fresh API coverage rate 0.3894.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 700 deduped forward/proxy rows; 181 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 12
Upcoming fixture rows: 0
Proxy price rows: 0
Sources attempted: 1
Errors: 0
No usable proxy odds rows were available from Football-Data fixtures source.

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 113
Fixture team rows unmatched: 226
Ready for model-fixture join: False
Automatic forward price rows: 44
odds-api.io price rows: 44
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AA Ponte Preta SP | suggestion=nan | type=unmatched
- Botafogo FC SP | suggestion=nan | type=unmatched
- Al Masry Club | suggestion=nan | type=unmatched
- Zed FC | suggestion=nan | type=unmatched
- AL Naft | suggestion=nan | type=unmatched
- Newroz SC | suggestion=nan | type=unmatched
- AL Najaf | suggestion=nan | type=unmatched
- Al Zawraa | suggestion=nan | type=unmatched
- AL Talaba | suggestion=nan | type=unmatched
- AL Karkh | suggestion=nan | type=unmatched
- Argentino de Quilmes | suggestion=nan | type=unmatched
- CA Ituzaingo | suggestion=nan | type=unmatched
- FC Arlanda | suggestion=nan | type=unmatched
- Gefle IF | suggestion=nan | type=unmatched
- Athletic Club MG | suggestion=nan | type=unmatched
- Atletico Mineiro MG | suggestion=nan | type=unmatched
- FC Atletico CE | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 113
Automatic price rows: 44
Value snapshot rows: 135
Matches with any automatic price: 44
Matches with fresh API price: 44
Matches with odds-api.io price: 44
Fresh API match coverage rate: 0.3894
odds-api.io match coverage rate: 0.3894
Real-money ready: False
## Match coverage
- 2026-06-01 | FC Bulleen Lions vs Port Melbourne Sharks SC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-01 | Vietnam vs Timor-Leste | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-01 | Vanraure Hachinohe FC vs Fukushima United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | FC Bulleen Lions vs Port Melbourne Sharks | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | Melbourne Victory vs Melbourne Knights | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | Pakistan vs Bangladesh | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | Juventud de Las Piedras vs Montevideo Wanderers | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-01 | Bulawayo Chiefs FC vs Manica Diamonds FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | Indonesia vs Myanmar | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-01 | Japan vs Ivory Coast | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-01 | Nacional de Montevideo vs Albion FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-01 | Barra FC SC vs Nacao | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-01 | Al Masry Club vs Zed FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | AL Naft vs Newroz SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | Diyala FC vs Duhok FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | Bulgaria vs Montenegro | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-01 | FC Elva vs Tartu JK Welco | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 113
Proxy price rows: 44
Matched prediction rows: 45
Value snapshot rows: 135
odds-api.io snapshot rows: 135
Baseline snapshot rows: 135
Full model snapshot rows: 0
Positive EV rows: 61
Source counts: {'odds_api_io_Bet365_ML': 135}
- 2026-06-01 | Colombia vs Costa Rica | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.3488 | EV=5.6272 | match=1.0
- 2026-06-01 | Jrfpc Upesciema Warriors vs JFK Ventspils | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-06-01 | Slovakia vs Malta | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-06-01 | Turkiye vs North Macedonia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-06-01 | SC Recife PE vs Paysandu SC PA | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-06-01 | AL Najaf vs Al Zawraa | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3772 | EV=1.3575 | match=1.0
- 2026-06-01 | FC Bulleen Lions vs Port Melbourne Sharks SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=0.96
- 2026-06-01 | FC Bulleen Lions vs Port Melbourne Sharks | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-06-01 | Chapaquito Nacional Senac vs Club Deportivo San Martin | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3772 | EV=1.1689 | match=1.0
- 2026-06-01 | Austria vs Tunisia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-06-01 | Vard Haugesund vs Aasane Fotball 2 | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-06-01 | CA Penarol Montevideo vs Central Espanol FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-06-01 | Al Masry Club vs Zed FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-06-01 | Jrfpc Upesciema Warriors vs JFK Ventspils | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-06-01 | Colombia vs Costa Rica | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-06-01 | KFG Gardabaer vs Fjolnir | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3772 | EV=0.7917 | match=1.0
- 2026-06-01 | Skovde AIK vs Jonkopings Sodra IF | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3772 | EV=0.7917 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 135
Pre-dedupe proxy candidate observation rows: 42
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 2
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-06-01 | FC Elva vs Tartu JK Welco | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-06-01 | Leones Futbol Club vs CSD Macara | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-06-01 | CA Boston River vs Liverpool Montevideo | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-06-01 | CA Fenix Pilar vs Canuelas FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-06-01 | Diyala FC vs Duhok FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-06-01 | Bulgaria vs Montenegro | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-06-01 | Pirata FC vs CSC Deportivo Llacuabamba | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-06-01 | Melbourne Victory vs Melbourne Knights | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-06-01 | AA Ponte Preta SP vs Botafogo FC SP | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-06-01 | FC Atletico CE vs Piaui PI | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145
- 2026-06-01 | Norway vs Sweden | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-06-01 | Barra FC SC vs Brusque FC SC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 7
- ev_above_real_candidate_cap_possible_overconfidence: 5
- watchlist_only_pending_forward_settlement: 3
- edge_below_candidate_threshold: 2
- probability_or_league_rule_suppressed: 2
- low_probability_band_under_0_35: 2
## Row explanations
- 2026-06-01 | FC Elva vs Tartu JK Welco | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-01 | Leones Futbol Club vs CSD Macara | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-01 | CA Boston River vs Liverpool Montevideo | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-06-01 | CA Fenix Pilar vs Canuelas FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-06-01 | Diyala FC vs Duhok FC | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-01 | Bulgaria vs Montenegro | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-01 | Pirata FC vs CSC Deportivo Llacuabamba | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-01 | Melbourne Victory vs Melbourne Knights | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-06-01 | AA Ponte Preta SP vs Botafogo FC SP | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-06-01 | FC Atletico CE vs Piaui PI | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-01 | Norway vs Sweden | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-01 | Barra FC SC vs Brusque FC SC | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 135
Paper proxy observation rows: 25
Positive EV value rows: 61
Suppressed-band observation rows: 0
Distinct matches: 24
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.417217
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=12, avg_ev=0.4141, max_ev=0.744
- draw: rows=8, avg_ev=0.3529, max_ev=0.37
- home: rows=5, avg_ev=0.5277, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 113
Forward fixture prediction rows: 113
Full model prediction rows: 0
Baseline prediction rows: 113
Max forward predictions: 300
Ready for price join: True
- 2026-06-01 08:15 | FC Bulleen Lions vs Port Melbourne Sharks SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 09:00 | Vietnam vs Timor-Leste | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 10:00 | Vanraure Hachinohe FC vs Fukushima United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 10:30 | FC Bulleen Lions vs Port Melbourne Sharks | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 10:30 | Melbourne Victory vs Melbourne Knights | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 11:00 | Pakistan vs Bangladesh | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 12:30 | Juventud de Las Piedras vs Montevideo Wanderers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 13:00 | Bulawayo Chiefs FC vs Manica Diamonds FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 13:00 | Indonesia vs Myanmar | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 13:00 | Japan vs Ivory Coast | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 13:00 | Nacional de Montevideo vs Albion FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 13:30 | Barra FC SC vs Nacao | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 14:00 | Al Masry Club vs Zed FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 15:00 | AL Naft vs Newroz SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 15:00 | Diyala FC vs Duhok FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 16:00 | Bulgaria vs Montenegro | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 16:00 | FC Elva vs Tartu JK Welco | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 16:00 | Jrfpc Upesciema Warriors vs JFK Ventspils | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 16:00 | Maldives vs Afghanistan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 16:00 | Pirata FC vs CSC Deportivo Llacuabamba | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-01 16:00 | Slovakia vs Malta | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 113
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 5067
Log type: probability_only_no_market_prices
- 2026-06-03 2026-06-01 17:30:00 | Vasalunds IF vs FC Jarfalla | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-03 2026-06-01 18:45:00 | Luxembourg vs Italy | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-03 2026-06-01 18:45:00 | Netherlands vs Algeria | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-03 2026-06-01 22:00:00 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-04 2026-06-01 00:00:00 | Birmingham Legion FC vs Louisville City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-04 2026-06-01 19:00:00 | Spain vs Iraq | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-05 2026-06-01 10:00:00 | Hills United FC Brumbies vs Bull FC Academy | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-05 2026-06-01 22:00:00 | Montevideo Wanderers vs Danubio FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-01 00:00:00 | Nomads United AFC vs Northern AFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-01 03:00:00 | Bentleigh Greens SC vs Hume City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-01 09:00:00 | Rochedale Rovers vs Peninsula Power FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-01 13:00:00 | Central Espanol FC vs Racing Club Montevideo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-01 18:00:00 | Montevideo City Torque vs Deportivo Maldonado | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-01 21:30:00 | Club Nacional de Football vs CA Juventud de Las Piedras | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-01 04:40:00 | Bulls FC Academy vs Hills United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-01 07:00:00 | Bulls FC Academy U23 vs Hills United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-01 07:00:00 | Western Sydney Wanderers Youth vs Illawarra Stingrays | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-01 13:00:00 | CA Progreso vs Albion FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-01 18:00:00 | CA Cerro vs CA Penarol Montevideo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-01 21:30:00 | Defensor Sporting vs CA Boston River | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 113
Manual template rows: 113
Rows with complete manual odds: 0
Rows missing manual odds: 113
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-06-01 22:00 | AA Ponte Preta SP vs Botafogo FC SP
- 2026-06-01 14:00 | Al Masry Club vs Zed FC
- 2026-06-01 15:00 | AL Naft vs Newroz SC
- 2026-06-01 17:30 | AL Najaf vs Al Zawraa
- 2026-06-01 17:30 | AL Talaba vs AL Karkh
- 2026-06-01 18:30 | Argentino de Quilmes vs CA Ituzaingo
- 2026-06-01 17:30 | FC Arlanda vs Gefle IF
- 2026-06-01 18:00 | Athletic Club MG vs Atletico Mineiro MG
- 2026-06-01 19:00 | FC Atletico CE vs Piaui PI
- 2026-06-01 18:45 | Austria vs Tunisia
- 2026-06-01 23:00 | Barra FC SC vs Brusque FC SC
- 2026-06-01 13:30 | Barra FC SC vs Nacao
- 2026-06-01 13:00 | Bulawayo Chiefs FC vs Manica Diamonds FC
- 2026-06-01 16:00 | Bulgaria vs Montenegro
- 2026-06-01 10:30 | FC Bulleen Lions vs Port Melbourne Sharks

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 113
Source counts: {'odds_api_io_events_bookmaker_filtered': 95, 'odds_api_io_events_search': 18}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-06-01 22:00 | AA Ponte Preta SP vs Botafogo FC SP | brazil-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-06-01 14:00 | Al Masry Club vs Zed FC | egypt-league-cup | odds_api_io_events_bookmaker_filtered
- 2026-06-01 15:00 | AL Naft vs Newroz SC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-06-01 17:30 | AL Najaf vs Al Zawraa | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-06-01 17:30 | AL Talaba vs AL Karkh | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-06-01 18:30 | Argentino de Quilmes vs CA Ituzaingo | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-06-01 17:30 | FC Arlanda vs Gefle IF | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-06-01 18:00 | Athletic Club MG vs Atletico Mineiro MG | brazil-u20-mineiro-1-divisao | odds_api_io_events_bookmaker_filtered
- 2026-06-01 19:00 | FC Atletico CE vs Piaui PI | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-06-01 18:45 | Austria vs Tunisia | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-01 23:00 | Barra FC SC vs Brusque FC SC | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-06-01 13:30 | Barra FC SC vs Nacao | brazil-u20-catarinense-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-06-01 13:00 | Bulawayo Chiefs FC vs Manica Diamonds FC | zimbabwe-premier-soccer-league | odds_api_io_events_bookmaker_filtered
- 2026-06-01 16:00 | Bulgaria vs Montenegro | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-01 10:30 | FC Bulleen Lions vs Port Melbourne Sharks | australia-victoria-premier-league-1 | odds_api_io_events_bookmaker_filtered
- 2026-06-01 08:15 | FC Bulleen Lions vs Port Melbourne Sharks SC | australia-u23-victoria-premier-league-1 | odds_api_io_events_bookmaker_filtered
- 2026-06-01 18:00 | CA Boston River vs Liverpool Montevideo | uruguay-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-06-01 18:30 | CA Fenix Pilar vs Canuelas FC | argentina-primera-c | odds_api_io_events_bookmaker_filtered
- 2026-06-01 23:00 | CA Penarol Montevideo vs Central Espanol FC | uruguay-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-06-01 18:00 | CA River Plate (URU) vs Colon FC Reserve | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-01 23:00 | CD Santa Cruz vs Deportes Copiapo | chile-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-06-01 19:30 | Chapaquito Nacional Senac vs Club Deportivo San Martin | bolivia-copa-simon-bolivar | odds_api_io_events_bookmaker_filtered
- 2026-06-01 23:15 | CN Marcilio Dias SC vs Azuriz FC PR | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 113
Rows with complete odds: 0
- 2026-06-01 22:00 | AA Ponte Preta SP vs Botafogo FC SP | bookmaker=bet365_manual
- 2026-06-01 14:00 | Al Masry Club vs Zed FC | bookmaker=bet365_manual
- 2026-06-01 15:00 | AL Naft vs Newroz SC | bookmaker=bet365_manual
- 2026-06-01 17:30 | AL Najaf vs Al Zawraa | bookmaker=bet365_manual
- 2026-06-01 17:30 | AL Talaba vs AL Karkh | bookmaker=bet365_manual
- 2026-06-01 18:30 | Argentino de Quilmes vs CA Ituzaingo | bookmaker=bet365_manual
- 2026-06-01 17:30 | FC Arlanda vs Gefle IF | bookmaker=bet365_manual
- 2026-06-01 18:00 | Athletic Club MG vs Atletico Mineiro MG | bookmaker=bet365_manual
- 2026-06-01 19:00 | FC Atletico CE vs Piaui PI | bookmaker=bet365_manual
- 2026-06-01 18:45 | Austria vs Tunisia | bookmaker=bet365_manual
- 2026-06-01 23:00 | Barra FC SC vs Brusque FC SC | bookmaker=bet365_manual
- 2026-06-01 13:30 | Barra FC SC vs Nacao | bookmaker=bet365_manual
- 2026-06-01 13:00 | Bulawayo Chiefs FC vs Manica Diamonds FC | bookmaker=bet365_manual
- 2026-06-01 16:00 | Bulgaria vs Montenegro | bookmaker=bet365_manual
- 2026-06-01 10:30 | FC Bulleen Lions vs Port Melbourne Sharks | bookmaker=bet365_manual
- 2026-06-01 08:15 | FC Bulleen Lions vs Port Melbourne Sharks SC | bookmaker=bet365_manual
- 2026-06-01 18:00 | CA Boston River vs Liverpool Montevideo | bookmaker=bet365_manual
- 2026-06-01 18:30 | CA Fenix Pilar vs Canuelas FC | bookmaker=bet365_manual
- 2026-06-01 23:00 | CA Penarol Montevideo vs Central Espanol FC | bookmaker=bet365_manual
- 2026-06-01 18:00 | CA River Plate (URU) vs Colon FC Reserve | bookmaker=bet365_manual
- 2026-06-01 23:00 | CD Santa Cruz vs Deportes Copiapo | bookmaker=bet365_manual
- 2026-06-01 19:30 | Chapaquito Nacional Senac vs Club Deportivo San Martin | bookmaker=bet365_manual
- 2026-06-01 23:15 | CN Marcilio Dias SC vs Azuriz FC PR | bookmaker=bet365_manual
- 2026-06-01 20:00 | CODM Meknes vs Olympique Dcheira | bookmaker=bet365_manual

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
- 2026-06-01 22:00 | AA Ponte Preta SP vs Botafogo FC SP
- 2026-06-01 14:00 | Al Masry Club vs Zed FC
- 2026-06-01 15:00 | AL Naft vs Newroz SC
- 2026-06-01 17:30 | AL Najaf vs Al Zawraa
- 2026-06-01 17:30 | AL Talaba vs AL Karkh
- 2026-06-01 18:30 | Argentino de Quilmes vs CA Ituzaingo
- 2026-06-01 17:30 | FC Arlanda vs Gefle IF
- 2026-06-01 18:00 | Athletic Club MG vs Atletico Mineiro MG
- 2026-06-01 19:00 | FC Atletico CE vs Piaui PI
- 2026-06-01 18:45 | Austria vs Tunisia
- 2026-06-01 23:00 | Barra FC SC vs Brusque FC SC
- 2026-06-01 13:30 | Barra FC SC vs Nacao
- 2026-06-01 13:00 | Bulawayo Chiefs FC vs Manica Diamonds FC
- 2026-06-01 16:00 | Bulgaria vs Montenegro
- 2026-06-01 10:30 | FC Bulleen Lions vs Port Melbourne Sharks
- 2026-06-01 08:15 | FC Bulleen Lions vs Port Melbourne Sharks SC
- 2026-06-01 18:00 | CA Boston River vs Liverpool Montevideo
- 2026-06-01 18:30 | CA Fenix Pilar vs Canuelas FC
- 2026-06-01 23:00 | CA Penarol Montevideo vs Central Espanol FC

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 884
Valid forward/proxy log rows: 881
Deduped forward/proxy observation rows: 700
Duplicate forward/proxy log rows: 181
Valid automatic proxy observation rows: 881
Deduped automatic proxy observation rows: 700
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-23 | Avondale FC vs Alamein FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-27 | VVSB Noordwijkerhout vs Excelsior Maassluis | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553
- 2026-05-30 | Gold Coast United FC vs Peninsula Power | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054700000000000006
- 2026-05-30 | Canberra Juventus FC vs Tuggeranong United FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054700000000000006
- 2026-05-30 | Cooks Hill United vs Valentine FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054700000000000006
- 2026-05-30 | Alamein FC vs Keilor Park SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054700000000000006
- 2026-05-21 | Anderlecht vs St Truiden | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0546
- 2026-05-27 | IF Vestri vs UMF Njardvik | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054400000000000004
- 2026-05-27 | JK Tallinna Kalev vs Viimsi JK | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054
- 2026-05-21 | Panetolikos vs Asteras Tripolis | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054
- 2026-05-27 | ETO FC Gyor vs MTK Hungaria Budapest | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.053500000000000006
- 2026-05-27 | SJK Akatemia/2 vs JS Hercules | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.053500000000000006
- 2026-05-27 | ADO 20 Heemskerk vs FC Lisse | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0531
- 2026-05-27 | AIK DFF vs Hacken Gothenburg | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.052500000000000005
- 2026-05-27 | Jypk vs Ons Oulu | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.052000000000000005
- 2026-05-27 | Sparta Prague B vs FC Hradec Kralove | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0517
- 2026-05-27 | Jypk vs Ons Oulu | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0517

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
### Skovde AIK vs Jonkopings Sodra IF
- Date/time: 2026-06-01 17:00
- League/phase: sweden-ettan-relegation/promotion / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.75
- Fair odds: 2.65
- Model probability: 0.3772
- Probability band: 0.35-0.45
- EV: 0.7917
- Probability edge: 0.1667
- Alignment penalty: 0.7917
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0733
- Prediction ID: fea14f3d64741c6536d3
### KFG Gardabaer vs Fjolnir
- Date/time: 2026-06-01 19:15
- League/phase: iceland-2-deild / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.75
- Fair odds: 2.65
- Model probability: 0.3772
- Probability band: 0.35-0.45

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
Total logged paper-test rows: 884
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 135, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 53, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 884, 'source_used': 'automatic_forward_value_snapshots'}
- Skovde AIK vs Jonkopings Sodra IF | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- KFG Gardabaer vs Fjolnir | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Throttur Reykjavik vs UMF Grindavik | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Vanraure Hachinohe FC vs Fukushima United FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Argentino de Quilmes vs CA Ituzaingo | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Atletico CE vs Piaui PI | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Norway vs Sweden | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Barra FC SC vs Brusque FC SC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CS Barracas vs CA Atlas | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- KH Hlidarendi vs Arbaer | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Elva vs Tartu JK Welco | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Arlanda vs Gefle IF | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Guairena FC vs Club 3 De Noviembre | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Pakistan vs Bangladesh | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Slovakia vs Malta | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Bulleen Lions vs Port Melbourne Sharks | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Bulleen Lions vs Port Melbourne Sharks SC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Turkiye vs North Macedonia | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
