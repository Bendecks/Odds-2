# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-06-03T02:59:14.974747+00:00`
GitHub run: `389` attempt `1`
GitHub SHA: `d9da6d2610e65eb2c61b75a5c82e0c083c6a0f51`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 41 |  |  |
| odds-api.io forward fixtures | True | 138 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 123 |  |  |
| Forward price coverage report | True | 282 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 282 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 126
- Positive EV proxy rows: 56
- Proxy observation rows: 25
- Valid forward/proxy log rows: 952
- Deduped forward/proxy log rows: 764
- Duplicate forward/proxy log rows identified: 188
- Fresh API match coverage rate: 0.14
- Matches with fresh API price: 42
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
Current: 126 value snapshots; fresh API coverage rate 0.14.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 764 deduped forward/proxy rows; 188 duplicate raw rows identified.
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
Upcoming fixture rows: 319
Fixture team rows unmatched: 637
Ready for model-fixture join: False
Automatic forward price rows: 42
odds-api.io price rows: 42
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. Wiener Neustadter SC | suggestion=nan | type=unmatched
- UFC Sankt Peter Au | suggestion=nan | type=unmatched
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
- AS Far Rabat | suggestion=nan | type=unmatched
- Difaa Hassani d'el-Jadida | suggestion=nan | type=unmatched
- Avai FC SC | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 42
Value snapshot rows: 126
Matches with any automatic price: 42
Matches with fresh API price: 42
Matches with odds-api.io price: 42
Fresh API match coverage rate: 0.14
odds-api.io match coverage rate: 0.14
Real-money ready: False
## Match coverage
- 2026-06-04 | Indonesia vs Kuwait | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | Japan vs Mongolia | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | DH van Hien vs K. Khanh Hoa | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Dornbirner SV vs FC Rotenberg | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | FC Lustenau vs VfB Hohenems | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Myanmar vs Vietnam | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | FC Raika Volders vs SC Mils | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Maldives vs Pakistan | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Modbury Jets SC Reserve vs Fulham United FC Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | Cambodia vs Bhutan | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | FC Lauterach vs SV Kuchl | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | FC Kattaqorgon vs Fardu Ferghana | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | FC Kitzbuhel vs TSV St. Johann | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | 1. Wiener Neustadter SC vs UFC Sankt Peter Au | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Lesotho vs Kenya | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-04 | Respublika Football Academy vs PFC Terdu | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-04 | Timor-Leste vs Indonesia | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 42
Matched prediction rows: 42
Value snapshot rows: 126
odds-api.io snapshot rows: 126
Baseline snapshot rows: 126
Full model snapshot rows: 0
Positive EV rows: 56
Source counts: {'odds_api_io_Bet365_ML': 126}
- 2026-06-04 | Spain vs Iraq | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3488 | EV=9.1152 | match=1.0
- 2026-06-04 | Cambodia vs Bhutan | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-06-04 | DH van Hien vs K. Khanh Hoa | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-06-04 | Spain vs Iraq | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-06-04 | FC Lasten vs Fish United | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-06-04 | Slovenia vs Cyprus | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-06-04 | France vs Ivory Coast | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-06-04 | Andorra vs Liechtenstein | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-06-04 | FC Lasten vs Fish United | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.274 | EV=1.329 | match=1.0
- 2026-06-04 | Afghanistan vs Bangladesh | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-06-04 | FC Juan Aurich de Alcatuyo vs CD Rio San Juan Humi | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-06-04 | FC Lauterach vs SV Kuchl | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3772 | EV=0.886 | match=1.0
- 2026-06-04 | US Goree vs Stade de Mbour | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-06-04 | IFK Stocksund vs FC Stockholm Internazionale | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3772 | EV=0.7917 | match=1.0
- 2026-06-04 | Fortune vs Bst Galaxy | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0
- 2026-06-04 | Cambodia vs Bhutan | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.274 | EV=0.7125 | match=1.0
- 2026-06-04 | Laholms FK vs Hassleholms IF | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 126
Pre-dedupe proxy candidate observation rows: 40
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 7
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-06-04 | Tmt vs Bombada | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-06-04 | Sundby BK vs Holbaek B&I | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-06-04 | Hassania Union Sport Agadir vs FUS Rabat | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-06-04 | Laholms FK vs Hassleholms IF | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-06-04 | Lesotho vs Kenya | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145
- 2026-06-04 | 1. Wiener Neustadter SC vs UFC Sankt Peter Au | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-06-04 | FC Wolfurt vs SV Ludesch | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3488 | EV=0.36032 | edge=0.09239 | penalty=0.3603213603213602 | tier=suppressed_proxy_watchlist | score=0.1216
- 2026-06-04 | Real de Banjul vs Falcons FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3488 | EV=0.36032 | edge=0.09239 | penalty=0.3603213603213602 | tier=suppressed_proxy_watchlist | score=0.1216
- 2026-06-04 | Lebanon vs Yemen | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3488 | EV=0.32544 | edge=0.085642 | penalty=0.325439469824212 | tier=suppressed_proxy_watchlist | score=0.1201
- 2026-06-04 | LTU vs Jyty Turku | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3488 | EV=0.32544 | edge=0.085642 | penalty=0.325439469824212 | tier=suppressed_proxy_watchlist | score=0.1201
- 2026-06-04 | Stenungsunds IF vs Vanersborgs IF | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3488 | EV=0.32544 | edge=0.085642 | penalty=0.325439469824212 | tier=suppressed_proxy_watchlist | score=0.1201
- 2026-06-04 | FC Lauterach vs SV Kuchl | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.083524 | penalty=0.4385014385014385 | tier=suppressed_proxy_watchlist | score=0.1196

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
- ev_above_real_candidate_cap_possible_overconfidence: 10
- market_alignment_penalty_too_high_for_real_candidate: 10
- probability_or_league_rule_suppressed: 7
- low_probability_band_under_0_35: 7
- watchlist_only_pending_forward_settlement: 2
## Row explanations
- 2026-06-04 | Tmt vs Bombada | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Sundby BK vs Holbaek B&I | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-04 | Hassania Union Sport Agadir vs FUS Rabat | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-04 | Laholms FK vs Hassleholms IF | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Lesotho vs Kenya | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | 1. Wiener Neustadter SC vs UFC Sankt Peter Au | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | FC Wolfurt vs SV Ludesch | sel=AWAY | score=0.1216 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Real de Banjul vs Falcons FC | sel=AWAY | score=0.1216 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Lebanon vs Yemen | sel=AWAY | score=0.1201 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | LTU vs Jyty Turku | sel=AWAY | score=0.1201 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | Stenungsunds IF vs Vanersborgs IF | sel=AWAY | score=0.1201 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-04 | FC Lauterach vs SV Kuchl | sel=DRAW | score=0.1196 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 126
Paper proxy observation rows: 25
Positive EV value rows: 56
Suppressed-band observation rows: 0
Distinct matches: 24
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.404257
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=13, avg_ev=0.3764, max_ev=0.744
- draw: rows=7, avg_ev=0.4091, max_ev=0.7125
- home: rows=5, avg_ev=0.4698, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 319
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-06-04 06:00 | Indonesia vs Kuwait | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 06:00 | Japan vs Mongolia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 09:00 | DH van Hien vs K. Khanh Hoa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 09:00 | Dornbirner SV vs FC Rotenberg | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 09:00 | FC Lustenau vs VfB Hohenems | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 09:00 | Myanmar vs Vietnam | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 09:00 | FC Raika Volders vs SC Mils | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 11:00 | Maldives vs Pakistan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 11:00 | Modbury Jets SC Reserve vs Fulham United FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 12:00 | Cambodia vs Bhutan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 12:00 | FC Lauterach vs SV Kuchl | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 12:30 | FC Kattaqorgon vs Fardu Ferghana | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 12:30 | FC Kitzbuhel vs TSV St. Johann | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 13:00 | 1. Wiener Neustadter SC vs UFC Sankt Peter Au | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 13:00 | Lesotho vs Kenya | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 13:00 | Respublika Football Academy vs PFC Terdu | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 13:00 | Timor-Leste vs Indonesia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 15:00 | Bulgaria vs Albania | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 15:00 | Sweden vs Finland | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 15:00 | FC Wolfurt vs SV Ludesch | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-04 15:30 | Slovenia vs Bosnia and Herzegovina | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 5555
Log type: probability_only_no_market_prices
- 2026-06-06 2026-06-04 18:00:00 | La Luz FC vs Paysandu FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | Argentino de Merlo vs Deportivo Camioneros | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | Argentino de Rosario vs CA Lugano | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | ASD Justo Jose de Urquiza vs CA Puerto Nuevo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | CA Atlas vs CA Fenix Pilar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | CA Excursionistas vs CSD San Martin | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | CD Armenio vs CA Defensores Unidos | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | Club Estrella Del Sur (Alejandro Korn) vs Sacachispas FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | CSD Flandria vs Argentino de Quilmes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | CSDC Espanol vs CA Claypole | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | Leones de Rosario FC vs CS Barracas | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | Villa Dalmine vs CA Villa San Carlos | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 18:30:00 | Yupanqui vs CA Central Cordoba Rosario | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 19:00:00 | Club Mercedes vs Deportivo Paraguayo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 19:00:00 | Panama vs Bosnia and Herzegovina | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 19:30:00 | SSA Swarm FC vs Birmingham Legion FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 22:00:00 | Venezuela vs Turkiye | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 23:00:00 | Cavalry FC vs HFX Wanderers FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 23:00:00 | FC Supra Du Quebec vs Pacific FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-06 2026-06-04 23:30:00 | SSA Swarm FC vs Birmingham Legion FC 2 | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 319
Manual template rows: 319
Rows with complete manual odds: 0
Rows missing manual odds: 319
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-06-04 13:00 | 1. Wiener Neustadter SC vs UFC Sankt Peter Au
- 2026-06-04 17:30 | AFC Eskilstuna vs Karlbergs BK
- 2026-06-04 16:00 | Afghanistan vs Bangladesh
- 2026-06-04 19:15 | Alafoss vs KFR
- 2026-06-04 18:00 | America FC SP vs CA Juventus SP
- 2026-06-04 23:00 | Anapolis FC GO vs Paysandu SC PA
- 2026-06-04 17:00 | Andorra vs Liechtenstein
- 2026-06-04 20:00 | AS Far Rabat vs Difaa Hassani d'el-Jadida
- 2026-06-04 18:00 | Avai FC SC vs Nacao
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger
- 2026-06-04 15:00 | Bulgaria vs Albania
- 2026-06-04 18:00 | CA Barracas Central Reserve vs CA Aldosivi Reserve
- 2026-06-04 22:00 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve
- 2026-06-04 18:00 | CA Platense vs CA Belgrano
- 2026-06-04 22:00 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 319
Source counts: {'odds_api_io_events_bookmaker_filtered': 284, 'odds_api_io_events_search': 35}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-06-04 13:00 | 1. Wiener Neustadter SC vs UFC Sankt Peter Au | austria-amateur-niederosterreich-1-landesliga | odds_api_io_events_bookmaker_filtered
- 2026-06-04 17:30 | AFC Eskilstuna vs Karlbergs BK | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:00 | Afghanistan vs Bangladesh | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 19:15 | Alafoss vs KFR | iceland-4-deild | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | America FC SP vs CA Juventus SP | brazil-u20-paulista | odds_api_io_events_bookmaker_filtered
- 2026-06-04 23:00 | Anapolis FC GO vs Paysandu SC PA | brazil-copa-verde | odds_api_io_events_bookmaker_filtered
- 2026-06-04 17:00 | Andorra vs Liechtenstein | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 20:00 | AS Far Rabat vs Difaa Hassani d'el-Jadida | morocco-botola-pro-d1 | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | Avai FC SC vs Nacao | brazil-u20-catarinense-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger | algeria-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-06-04 15:00 | Bulgaria vs Albania | international-youth-u19-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | CA Barracas Central Reserve vs CA Aldosivi Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 22:00 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | CA Platense vs CA Belgrano | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 22:00 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 12:00 | Cambodia vs Bhutan | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-04 18:00 | CD Godoy Cruz vs CA Union Santa Fe Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-04 23:30 | Club Deportivo Cuenca Juniors vs CSD Macara | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-06-04 21:30 | Deportivo Santani vs Resistencia SC | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-06-04 09:00 | DH van Hien vs K. Khanh Hoa | vietnam-v-league-2 | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:00 | FC Dornbirn vs SVG Reichenau | austria-amateur-regionalliga-west | odds_api_io_events_bookmaker_filtered
- 2026-06-04 09:00 | Dornbirner SV vs FC Rotenberg | austria-amateur-vorarlberg-eliteliga | odds_api_io_events_bookmaker_filtered
- 2026-06-04 16:30 | Fortune vs Bst Galaxy | gambia-division-one | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 319
Rows with complete odds: 0
- 2026-06-04 13:00 | 1. Wiener Neustadter SC vs UFC Sankt Peter Au | bookmaker=bet365_manual
- 2026-06-04 17:30 | AFC Eskilstuna vs Karlbergs BK | bookmaker=bet365_manual
- 2026-06-04 16:00 | Afghanistan vs Bangladesh | bookmaker=bet365_manual
- 2026-06-04 19:15 | Alafoss vs KFR | bookmaker=bet365_manual
- 2026-06-04 18:00 | America FC SP vs CA Juventus SP | bookmaker=bet365_manual
- 2026-06-04 23:00 | Anapolis FC GO vs Paysandu SC PA | bookmaker=bet365_manual
- 2026-06-04 17:00 | Andorra vs Liechtenstein | bookmaker=bet365_manual
- 2026-06-04 20:00 | AS Far Rabat vs Difaa Hassani d'el-Jadida | bookmaker=bet365_manual
- 2026-06-04 18:00 | Avai FC SC vs Nacao | bookmaker=bet365_manual
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger | bookmaker=bet365_manual
- 2026-06-04 15:00 | Bulgaria vs Albania | bookmaker=bet365_manual
- 2026-06-04 18:00 | CA Barracas Central Reserve vs CA Aldosivi Reserve | bookmaker=bet365_manual
- 2026-06-04 22:00 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve | bookmaker=bet365_manual
- 2026-06-04 18:00 | CA Platense vs CA Belgrano | bookmaker=bet365_manual
- 2026-06-04 22:00 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve | bookmaker=bet365_manual
- 2026-06-04 12:00 | Cambodia vs Bhutan | bookmaker=bet365_manual
- 2026-06-04 18:00 | CD Godoy Cruz vs CA Union Santa Fe Reserve | bookmaker=bet365_manual
- 2026-06-04 23:30 | Club Deportivo Cuenca Juniors vs CSD Macara | bookmaker=bet365_manual
- 2026-06-04 21:30 | Deportivo Santani vs Resistencia SC | bookmaker=bet365_manual
- 2026-06-04 09:00 | DH van Hien vs K. Khanh Hoa | bookmaker=bet365_manual
- 2026-06-04 16:00 | FC Dornbirn vs SVG Reichenau | bookmaker=bet365_manual
- 2026-06-04 09:00 | Dornbirner SV vs FC Rotenberg | bookmaker=bet365_manual
- 2026-06-04 16:30 | Fortune vs Bst Galaxy | bookmaker=bet365_manual
- 2026-06-04 19:10 | France vs Ivory Coast | bookmaker=bet365_manual

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
- 2026-06-04 13:00 | 1. Wiener Neustadter SC vs UFC Sankt Peter Au
- 2026-06-04 17:30 | AFC Eskilstuna vs Karlbergs BK
- 2026-06-04 16:00 | Afghanistan vs Bangladesh
- 2026-06-04 19:15 | Alafoss vs KFR
- 2026-06-04 18:00 | America FC SP vs CA Juventus SP
- 2026-06-04 23:00 | Anapolis FC GO vs Paysandu SC PA
- 2026-06-04 17:00 | Andorra vs Liechtenstein
- 2026-06-04 20:00 | AS Far Rabat vs Difaa Hassani d'el-Jadida
- 2026-06-04 18:00 | Avai FC SC vs Nacao
- 2026-06-04 16:00 | Ben Aknoun vs USM Alger
- 2026-06-04 15:00 | Bulgaria vs Albania
- 2026-06-04 18:00 | CA Barracas Central Reserve vs CA Aldosivi Reserve
- 2026-06-04 22:00 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve
- 2026-06-04 18:00 | CA Platense vs CA Belgrano
- 2026-06-04 22:00 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve
- 2026-06-04 12:00 | Cambodia vs Bhutan
- 2026-06-04 18:00 | CD Godoy Cruz vs CA Union Santa Fe Reserve
- 2026-06-04 23:30 | Club Deportivo Cuenca Juniors vs CSD Macara
- 2026-06-04 21:30 | Deportivo Santani vs Resistencia SC

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 955
Valid forward/proxy log rows: 952
Deduped forward/proxy observation rows: 764
Duplicate forward/proxy log rows: 188
Valid automatic proxy observation rows: 952
Deduped automatic proxy observation rows: 764
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
### IFK Stocksund vs FC Stockholm Internazionale
- Date/time: 2026-06-04 17:30
- League/phase: sweden-svenska-cup / automatic_forward_price_proxy
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
- Prediction ID: 183428ccdd359e8d591d
### Fortune vs Bst Galaxy
- Date/time: 2026-06-04 16:30
- League/phase: gambia-division-one / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 5.0
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
Total logged paper-test rows: 955
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 126, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 52, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 955, 'source_used': 'automatic_forward_value_snapshots'}
- IFK Stocksund vs FC Stockholm Internazionale | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Fortune vs Bst Galaxy | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Laholms FK vs Hassleholms IF | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ben Aknoun vs USM Alger | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Cambodia vs Bhutan | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Lesotho vs Kenya | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Dornbirn vs SVG Reichenau | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- 1. Wiener Neustadter SC vs UFC Sankt Peter Au | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- DH van Hien vs K. Khanh Hoa | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Wolfurt vs SV Ludesch | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real de Banjul vs Falcons FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Lauterach vs SV Kuchl | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Lebanon vs Yemen | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Stenungsunds IF vs Vanersborgs IF | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- LTU vs Jyty Turku | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Tmt vs Bombada | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.4 | prob=0.3772 | EV=0.2825 | edge=0.0831 | penalty=0.2825 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Solvesborgs GIF vs Torns IF | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.7 | prob=0.3488 | EV=0.2906 | edge=0.0785 | penalty=0.2906 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Kattaqorgon vs Fardu Ferghana | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.7 | prob=0.3488 | EV=0.2906 | edge=0.0785 | penalty=0.2906 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
