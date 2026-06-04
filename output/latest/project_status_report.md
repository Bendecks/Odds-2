# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-06-04T02:54:14.934003+00:00`
GitHub run: `391` attempt `1`
GitHub SHA: `186e6d33b44422a36f47214b088dd5f471347951`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 42 |  |  |
| odds-api.io forward fixtures | True | 307 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 126 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 5 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 300 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 138
- Positive EV proxy rows: 64
- Proxy observation rows: 25
- Valid forward/proxy log rows: 973
- Deduped forward/proxy log rows: 776
- Duplicate forward/proxy log rows identified: 197
- Fresh API match coverage rate: 0.15
- Matches with fresh API price: 45
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
Current: 138 value snapshots; fresh API coverage rate 0.15.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 776 deduped forward/proxy rows; 197 duplicate raw rows identified.
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
Upcoming fixture rows: 408
Fixture team rows unmatched: 814
Ready for model-fixture join: False
Automatic forward price rows: 45
odds-api.io price rows: 45
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AFC Eskilstuna | suggestion=nan | type=unmatched
- Karlbergs BK | suggestion=nan | type=unmatched
- Afghanistan | suggestion=nan | type=unmatched
- Bangladesh | suggestion=nan | type=unmatched
- Alafoss | suggestion=nan | type=unmatched
- KFR | suggestion=nan | type=unmatched
- America FC SP | suggestion=nan | type=unmatched
- CA Juventus SP | suggestion=nan | type=unmatched
- Anapolis FC GO | suggestion=nan | type=unmatched
- Paysandu SC PA | suggestion=nan | type=unmatched
- Andorra | suggestion=nan | type=unmatched
- Liechtenstein | suggestion=nan | type=unmatched
- Araucaria ECR PR | suggestion=nan | type=unmatched
- FC Cascavel PR | suggestion=nan | type=unmatched
- AS Far Rabat | suggestion=nan | type=unmatched
- Difaa Hassani d'el-Jadida | suggestion=nan | type=unmatched
- Avai FC SC | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 45
Value snapshot rows: 138
Matches with any automatic price: 45
Matches with fresh API price: 45
Matches with odds-api.io price: 45
Fresh API match coverage rate: 0.15
odds-api.io match coverage rate: 0.15
Real-money ready: False
## Match coverage
- 2026-06-04 | Bulgaria vs Albania | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | Sweden vs Finland | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | FC Wolfurt vs SV Ludesch | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Slovenia vs Bosnia and Herzegovina | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | Afghanistan vs Bangladesh | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Ben Aknoun vs USM Alger | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Burundi vs Equatorial Guinea | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | FC Dornbirn vs SVG Reichenau | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Germany vs Denmark | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | Lebanon vs Yemen | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | LTU vs Jyty Turku | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Moldova vs Malta | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | Northern Ireland vs Guinea | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Slovenia vs Cyprus | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | FC Ylivieska vs SIF | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Fortune vs Bst Galaxy | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Gambia Ports Authority vs Gambian Dutch Lions | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 45
Matched prediction rows: 46
Value snapshot rows: 138
odds-api.io snapshot rows: 138
Baseline snapshot rows: 138
Full model snapshot rows: 0
Positive EV rows: 64
Source counts: {'odds_api_io_Bet365_ML': 138}
- 2026-06-04 | Spain vs Iraq | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=26.0 | prob=0.3488 | EV=8.0688 | match=1.0
- 2026-06-05 | Czechia vs Albania | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.6875
- 2026-06-05 | Czechia vs Guatemala | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-06-04 | Spain vs Iraq | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-06-04 | France vs Ivory Coast | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-06-05 | Mexico vs Serbia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-06-04 | AS Far Rabat vs Difaa Hassani d'el-Jadida | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-06-04 | FC Lasten vs Fish United | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-06-04 | Afghanistan vs Bangladesh | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-06-04 | Manhattan SC vs New Jersey Copa FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-06-04 | Andorra vs Liechtenstein | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-06-04 | IH Hafnarfjordur vs Arborg | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-06-04 | Slovenia vs Cyprus | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-06-04 | FC Lasten vs Fish United | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.274 | EV=1.329 | match=1.0
- 2026-06-04 | Millonarios FC vs Independiente Medellin | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-06-04 | FC Wolfurt vs SV Ludesch | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-06-04 | Hafnir vs Ellidi | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3772 | EV=0.9803 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 138
Pre-dedupe proxy candidate observation rows: 42
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 4
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-06-04 | Laholms FK vs Hassleholms IF | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-06-04 | Tmt vs Bombada | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-06-04 | Club Deportivo Cuenca Juniors vs CSD Macara | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-06-04 | Hassania Union Sport Agadir vs FUS Rabat | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-06-05 | San Antonio FC vs CD Independiente Juniors | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-06-04 | Sundby BK vs Holbaek B&I | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-06-04 | FC Ylivieska vs SIF | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-06-04 | FC Juan Aurich de Alcatuyo vs CD Rio San Juan Humi | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3772 | EV=0.47108 | edge=0.12079 | penalty=0.4710814710814708 | tier=proxy_watchlist | score=0.212
- 2026-06-04 | Solvesborgs GIF vs Torns IF | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244
- 2026-06-04 | Fortune vs Bst Galaxy | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-06-04 | Real de Banjul vs Falcons FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3488 | EV=0.36032 | edge=0.09239 | penalty=0.3603213603213602 | tier=suppressed_proxy_watchlist | score=0.1216
- 2026-06-04 | FC Wolfurt vs SV Ludesch | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.083524 | penalty=0.4385014385014385 | tier=suppressed_proxy_watchlist | score=0.1196

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
- market_alignment_penalty_too_high_for_real_candidate: 8
- ev_above_real_candidate_cap_possible_overconfidence: 7
- probability_or_league_rule_suppressed: 4
- low_probability_band_under_0_35: 4
- watchlist_only_pending_forward_settlement: 3
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-06-04 | Laholms FK vs Hassleholms IF | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Tmt vs Bombada | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Club Deportivo Cuenca Juniors vs CSD Macara | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-06-04 | Hassania Union Sport Agadir vs FUS Rabat | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-05 | San Antonio FC vs CD Independiente Juniors | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-04 | Sundby BK vs Holbaek B&I | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-04 | FC Ylivieska vs SIF | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-06-04 | FC Juan Aurich de Alcatuyo vs CD Rio San Juan Humi | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Solvesborgs GIF vs Torns IF | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Fortune vs Bst Galaxy | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Real de Banjul vs Falcons FC | sel=AWAY | score=0.1216 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | FC Wolfurt vs SV Ludesch | sel=DRAW | score=0.1196 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 138
Paper proxy observation rows: 25
Positive EV value rows: 64
Suppressed-band observation rows: 0
Distinct matches: 25
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.481678
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=12, avg_ev=0.4291, max_ev=0.6568
- draw: rows=8, avg_ev=0.5413, max_ev=0.7125
- home: rows=5, avg_ev=0.5126, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 408
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-06-04 15:00 | Bulgaria vs Albania | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 15:00 | Sweden vs Finland | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 15:00 | FC Wolfurt vs SV Ludesch | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 15:30 | Slovenia vs Bosnia and Herzegovina | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | Afghanistan vs Bangladesh | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | Burundi vs Equatorial Guinea | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | FC Dornbirn vs SVG Reichenau | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | Germany vs Denmark | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | Lebanon vs Yemen | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | LTU vs Jyty Turku | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | Moldova vs Malta | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | Northern Ireland vs Guinea | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | Slovenia vs Cyprus | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:00 | FC Ylivieska vs SIF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:30 | Fortune vs Bst Galaxy | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:30 | Gambia Ports Authority vs Gambian Dutch Lions | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:30 | Real de Banjul vs Falcons FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:30 | Tmt vs Bombada | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 16:45 | Lautp vs Peka | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 17:00 | Andorra vs Liechtenstein | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 5656
Log type: probability_only_no_market_prices
- 2026-06-06 2026-06-04 01:00:00 | Snohomish United vs Midlakes United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 01:00:00 | Whitecaps FC 2 vs Portland Timbers II | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 03:00:00 | Floreat Athena FC Reserves vs Gwelup Croatia SC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 04:00:00 | Bayswater City SC vs Dianella White Eagles SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 04:45:00 | Brisbane Strikers vs Robina City | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 04:45:00 | Unsw FC vs Western City Rangers FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:00:00 | Armadale SC vs Fremantle City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:00:00 | Balcatta Etna FC vs Sorrento FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:00:00 | Cockburn City SC Reserves vs Subiaco AFC Reserve | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:00:00 | Inglewood United Reserves vs Curtin University SC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:00:00 | Murdoch University Melville FC Reserves vs Mandurah City FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:00:00 | Perth Redstar FC vs Western Knights SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:00:00 | Perth SC vs Stirling Macedonia FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:00:00 | Uwa Nedlands FC Reserves vs Joondalup City FC Reserve | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:45:00 | Broadbeach United vs Holland Park Hawks | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 05:45:00 | Sunshine Coast Wanderers vs North Star | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 06:00:00 | Caboolture Sports FC vs Ipswich FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 06:15:00 | Port Melbourne Sharks SC vs Brunswick City SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 06:30:00 | Rydalmere Lions FC vs Macarthur Rams FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 06:50:00 | Japan vs South Africa | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 408
Manual template rows: 408
Rows with complete manual odds: 0
Rows missing manual odds: 408
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-06-04 17:30 | AFC Eskilstuna vs Karlbergs BK
- 2026-06-04 16:00 | Afghanistan vs Bangladesh
- 2026-06-04 19:15 | Alafoss vs KFR
- 2026-06-04 18:00 | America FC SP vs CA Juventus SP
- 2026-06-04 23:00 | Anapolis FC GO vs Paysandu SC PA
- 2026-06-04 17:00 | Andorra vs Liechtenstein
- 2026-06-04 18:00 | Araucaria ECR PR vs FC Cascavel PR
- 2026-06-04 20:00 | AS Far Rabat vs Difaa Hassani d'el-Jadida
- 2026-06-04 18:00 | Avai FC SC vs Nacao
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger
- 2026-06-04 15:00 | Bulgaria vs Albania
- 2026-06-04 16:00 | Burundi vs Equatorial Guinea
- 2026-06-04 18:00 | CA Barracas Central Reserve vs CA Aldosivi Reserve
- 2026-06-04 22:00 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve
- 2026-06-04 22:00 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 408
Source counts: {'odds_api_io_events_bookmaker_filtered': 376, 'odds_api_io_events_search': 32}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-06-04 17:30 | AFC Eskilstuna vs Karlbergs BK | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:00 | Afghanistan vs Bangladesh | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 19:15 | Alafoss vs KFR | iceland-4-deild | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | America FC SP vs CA Juventus SP | brazil-u20-paulista | odds_api_io_events_bookmaker_filtered
- 2026-06-04 23:00 | Anapolis FC GO vs Paysandu SC PA | brazil-copa-verde | odds_api_io_events_bookmaker_filtered
- 2026-06-04 17:00 | Andorra vs Liechtenstein | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | Araucaria ECR PR vs FC Cascavel PR | brazil-u20-paranaense-1-divisao | odds_api_io_events_bookmaker_filtered
- 2026-06-04 20:00 | AS Far Rabat vs Difaa Hassani d'el-Jadida | morocco-botola-pro-d1 | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | Avai FC SC vs Nacao | brazil-u20-catarinense-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger | algeria-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-06-04 15:00 | Bulgaria vs Albania | international-youth-u19-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:00 | Burundi vs Equatorial Guinea | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | CA Barracas Central Reserve vs CA Aldosivi Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 22:00 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 22:00 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | CD Godoy Cruz vs CA Union Santa Fe Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 23:30 | Club Deportivo Cuenca Juniors vs CSD Macara | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-06-04 21:30 | Deportivo Santani vs Resistencia SC | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:00 | FC Dornbirn vs SVG Reichenau | austria-amateur-regionalliga-west | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:30 | Fortune vs Bst Galaxy | gambia-division-one | odds_api_io_events_bookmaker_filtered
- 2026-06-04 19:10 | France vs Ivory Coast | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:30 | Gambia Ports Authority vs Gambian Dutch Lions | gambia-division-one | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | GD Prudente SP vs SE Palmeiras SP | brazil-u20-paulista | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 408
Rows with complete odds: 0
- 2026-06-04 17:30 | AFC Eskilstuna vs Karlbergs BK | bookmaker=bet365_manual
- 2026-06-04 16:00 | Afghanistan vs Bangladesh | bookmaker=bet365_manual
- 2026-06-04 19:15 | Alafoss vs KFR | bookmaker=bet365_manual
- 2026-06-04 18:00 | America FC SP vs CA Juventus SP | bookmaker=bet365_manual
- 2026-06-04 23:00 | Anapolis FC GO vs Paysandu SC PA | bookmaker=bet365_manual
- 2026-06-04 17:00 | Andorra vs Liechtenstein | bookmaker=bet365_manual
- 2026-06-04 18:00 | Araucaria ECR PR vs FC Cascavel PR | bookmaker=bet365_manual
- 2026-06-04 20:00 | AS Far Rabat vs Difaa Hassani d'el-Jadida | bookmaker=bet365_manual
- 2026-06-04 18:00 | Avai FC SC vs Nacao | bookmaker=bet365_manual
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger | bookmaker=bet365_manual
- 2026-06-04 15:00 | Bulgaria vs Albania | bookmaker=bet365_manual
- 2026-06-04 16:00 | Burundi vs Equatorial Guinea | bookmaker=bet365_manual
- 2026-06-04 18:00 | CA Barracas Central Reserve vs CA Aldosivi Reserve | bookmaker=bet365_manual
- 2026-06-04 22:00 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve | bookmaker=bet365_manual
- 2026-06-04 22:00 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve | bookmaker=bet365_manual
- 2026-06-04 18:00 | CD Godoy Cruz vs CA Union Santa Fe Reserve | bookmaker=bet365_manual
- 2026-06-04 23:30 | Club Deportivo Cuenca Juniors vs CSD Macara | bookmaker=bet365_manual
- 2026-06-04 21:30 | Deportivo Santani vs Resistencia SC | bookmaker=bet365_manual
- 2026-06-04 16:00 | FC Dornbirn vs SVG Reichenau | bookmaker=bet365_manual
- 2026-06-04 16:30 | Fortune vs Bst Galaxy | bookmaker=bet365_manual
- 2026-06-04 19:10 | France vs Ivory Coast | bookmaker=bet365_manual
- 2026-06-04 16:30 | Gambia Ports Authority vs Gambian Dutch Lions | bookmaker=bet365_manual
- 2026-06-04 18:00 | GD Prudente SP vs SE Palmeiras SP | bookmaker=bet365_manual
- 2026-06-04 17:00 | Generation Foot vs Ajel de Rufisque | bookmaker=bet365_manual

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
- 2026-06-04 17:30 | AFC Eskilstuna vs Karlbergs BK
- 2026-06-04 16:00 | Afghanistan vs Bangladesh
- 2026-06-04 19:15 | Alafoss vs KFR
- 2026-06-04 18:00 | America FC SP vs CA Juventus SP
- 2026-06-04 23:00 | Anapolis FC GO vs Paysandu SC PA
- 2026-06-04 17:00 | Andorra vs Liechtenstein
- 2026-06-04 18:00 | Araucaria ECR PR vs FC Cascavel PR
- 2026-06-04 20:00 | AS Far Rabat vs Difaa Hassani d'el-Jadida
- 2026-06-04 18:00 | Avai FC SC vs Nacao
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger
- 2026-06-04 15:00 | Bulgaria vs Albania
- 2026-06-04 16:00 | Burundi vs Equatorial Guinea
- 2026-06-04 18:00 | CA Barracas Central Reserve vs CA Aldosivi Reserve
- 2026-06-04 22:00 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve
- 2026-06-04 22:00 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve
- 2026-06-04 18:00 | CD Godoy Cruz vs CA Union Santa Fe Reserve
- 2026-06-04 23:30 | Club Deportivo Cuenca Juniors vs CSD Macara
- 2026-06-04 21:30 | Deportivo Santani vs Resistencia SC
- 2026-06-04 16:00 | FC Dornbirn vs SVG Reichenau

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 976
Valid forward/proxy log rows: 973
Deduped forward/proxy observation rows: 776
Duplicate forward/proxy log rows: 197
Valid automatic proxy observation rows: 973
Deduped automatic proxy observation rows: 776
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
### Burundi vs Equatorial Guinea
- Date/time: 2026-06-04 16:00
- League/phase: international-int-friendly-games / automatic_forward_price_proxy
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
- Prediction ID: 5c7d77f141cdc0938cf2
### IFK Stocksund vs FC Stockholm Internazionale
- Date/time: 2026-06-04 17:30
- League/phase: sweden-svenska-cup / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.5
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
Newly logged paper-test picks: 21
Total logged paper-test rows: 976
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 138, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 53, 'current_paper_picks': 25, 'newly_logged_picks': 21, 'total_logged_paper_rows': 976, 'source_used': 'automatic_forward_value_snapshots'}
- Burundi vs Equatorial Guinea | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- IFK Stocksund vs FC Stockholm Internazionale | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Vinotinto FC Ecuador vs Cumbaya FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Stenungsunds IF vs Vanersborgs IF | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Czechia vs Albania | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Czechia vs Guatemala | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- IH Hafnarfjordur vs Arborg | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Juan Aurich de Alcatuyo vs CD Rio San Juan Humi | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.9 | prob=0.3772 | EV=0.4711 | edge=0.1208 | penalty=0.4711 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ben Aknoun vs USM Alger | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Lebanon vs Yemen | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- US Goree vs Stade de Mbour | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Dornbirn vs SVG Reichenau | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Solvesborgs GIF vs Torns IF | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Fortune vs Bst Galaxy | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- France vs Ivory Coast | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hafnir vs Ellidi | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real de Banjul vs Falcons FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Laholms FK vs Hassleholms IF | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
