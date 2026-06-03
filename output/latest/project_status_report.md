# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-06-01T17:26:05.364583+00:00`
GitHub run: `386` attempt `1`
GitHub SHA: `1be6e125ceb56f8c40b51cdbb69450eb5e7eb8eb`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 45 |  |  |
| odds-api.io forward fixtures | True | 106 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 135 |  |  |
| Forward price coverage report | True | 150 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 150 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 282
- Automatic value snapshots: 123
- Positive EV proxy rows: 63
- Proxy observation rows: 25
- Valid forward/proxy log rows: 927
- Deduped forward/proxy log rows: 739
- Duplicate forward/proxy log rows identified: 188
- Fresh API match coverage rate: 0.1454
- Matches with fresh API price: 41
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
Current: 123 value snapshots; fresh API coverage rate 0.1454.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 739 deduped forward/proxy rows; 188 duplicate raw rows identified.
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
Upcoming fixture rows: 282
Fixture team rows unmatched: 564
Ready for model-fixture join: False
Automatic forward price rows: 41
odds-api.io price rows: 41
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- ADO 20 Heemskerk | suggestion=nan | type=unmatched
- IJsselmeervogels | suggestion=nan | type=unmatched
- Albania | suggestion=nan | type=unmatched
- Israel | suggestion=nan | type=unmatched
- America FC RJ | suggestion=nan | type=unmatched
- Sao Goncalo EC RJ | suggestion=nan | type=unmatched
- Annapolis Blues FC | suggestion=nan | type=unmatched
- Lionsbridge FC | suggestion=nan | type=unmatched
- Araruama FC RJ | suggestion=nan | type=unmatched
- Marica FC RJ | suggestion=nan | type=unmatched
- Atus Velden | suggestion=nan | type=unmatched
- FC Gleisdorf 09 | suggestion=nan | type=unmatched
- Avai FC SC | suggestion=nan | type=unmatched
- Chapecoense SC | suggestion=nan | type=unmatched
- Belconnen United FC | suggestion=nan | type=unmatched
- Tuggeranong United FC | suggestion=nan | type=unmatched
- BK Olympic | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 282
Automatic price rows: 41
Value snapshot rows: 123
Matches with any automatic price: 41
Matches with fresh API price: 41
Matches with odds-api.io price: 41
Fresh API match coverage rate: 0.1454
odds-api.io match coverage rate: 0.1454
Real-money ready: False
## Match coverage
- 2026-06-03 | Hoo P R / Lai P J vs Faza M / Pranata A S P | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-03 | Pakistan Panthers vs Asian Stars | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-03 | Belconnen United FC vs Tuggeranong United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Broadmeadow Magic FC vs Maitland FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Hawkesbury City SC vs Gladesville Ryde Magic | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Portugal vs Kazakhstan | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-03 | Sydney Olympic FC vs University of NSW | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-03 | Rochedale Rovers vs Magic United Tfa | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Sunshine Coast Wanderers vs St George Willawong FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Nepal vs Bangladesh | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Philippines vs Guam | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Indonesia vs Singapore | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-03 | Japan vs Portugal | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-03 | Milford FC vs Magesi FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Philippines vs Australia | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-06-03 | FK Gazalkent vs FC Jayxun | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-06-03 | Greece vs Serbia | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 282
Proxy price rows: 41
Matched prediction rows: 41
Value snapshot rows: 123
odds-api.io snapshot rows: 123
Baseline snapshot rows: 123
Full model snapshot rows: 0
Positive EV rows: 63
Source counts: {'odds_api_io_Bet365_ML': 123}
- 2026-06-03 | Broadmeadow Magic FC vs Maitland FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=1.0
- 2026-06-03 | Philippines vs Guam | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3488 | EV=10.8592 | match=1.0
- 2026-06-03 | India vs Bhutan | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-06-03 | Broadmeadow Magic FC vs Maitland FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.274 | EV=3.658 | match=1.0
- 2026-06-03 | Philippines vs Guam | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-06-03 | Netherlands vs Algeria | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-06-03 | Viggbyholms IK FF vs Sollentuna FK | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-06-03 | FK Gazalkent vs FC Jayxun | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-06-03 | IFK Umea vs Taftea IK | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-06-03 | Gibraltar vs Virgin Islands, British | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-06-03 | India vs Bhutan | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.274 | EV=1.603 | match=1.0
- 2026-06-03 | Luxembourg vs Italy | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3772 | EV=1.2632 | match=1.0
- 2026-06-03 | Denmark vs Congo DR | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-06-03 | SV Donau vs SC/ESV Parndorf 1919 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.2 | prob=0.3772 | EV=0.58424 | match=1.0
- 2026-06-03 | Presidente Hayes vs Deportivo Pinoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3488 | EV=0.51135 | match=1.0
- 2026-06-03 | Vilavelhense FC ES vs Vitoria FC ES | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3488 | EV=0.51135 | match=1.0
- 2026-06-03 | SK Bischofshofen vs SC Schwaz | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3488 | EV=0.51135 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 123
Pre-dedupe proxy candidate observation rows: 50
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 2
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-06-03 | SV Anthering vs SV Burmoos | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-06-03 | Araruama FC RJ vs Marica FC RJ | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-06-03 | Ntnui vs Fk Kvik Trondheim | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-06-03 | SC Neusiedl am See 1919 vs SC Wiener Viktoria | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-06-03 | Sacachispas FC vs AD Berazategui | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-06-03 | FC Rijnvogels vs Excelsior Maassluis | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-06-03 | Milford FC vs Magesi FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-06-03 | FC Hard vs SC Rothis | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-06-03 | ADO 20 Heemskerk vs IJsselmeervogels | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-06-03 | SV Donau vs SC/ESV Parndorf 1919 | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.2 | prob=0.3772 | EV=0.58424 | edge=0.139105 | penalty=0.5842415842415842 | tier=proxy_watchlist | score=0.2192
- 2026-06-03 | America FC RJ vs Sao Goncalo EC RJ | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244
- 2026-06-03 | Nepal vs Bangladesh | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123

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
- market_alignment_penalty_too_high_for_real_candidate: 10
- ev_above_real_candidate_cap_possible_overconfidence: 9
- probability_or_league_rule_suppressed: 2
- low_probability_band_under_0_35: 2
- watchlist_only_pending_forward_settlement: 1
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-06-03 | SV Anthering vs SV Burmoos | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-03 | Araruama FC RJ vs Marica FC RJ | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-03 | Ntnui vs Fk Kvik Trondheim | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-03 | SC Neusiedl am See 1919 vs SC Wiener Viktoria | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-03 | Sacachispas FC vs AD Berazategui | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-03 | FC Rijnvogels vs Excelsior Maassluis | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-03 | Milford FC vs Magesi FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-06-03 | FC Hard vs SC Rothis | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-06-03 | ADO 20 Heemskerk vs IJsselmeervogels | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-06-03 | SV Donau vs SC/ESV Parndorf 1919 | sel=HOME | score=0.2192 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-03 | America FC RJ vs Sao Goncalo EC RJ | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-06-03 | Nepal vs Bangladesh | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 123
Paper proxy observation rows: 25
Positive EV value rows: 63
Suppressed-band observation rows: 0
Distinct matches: 24
Distinct sources: 0
Max EV: 0.58424
Average EV: 0.351665
Max probability edge: 0.139105
Average match confidence: None
## By selection
- away: rows=11, avg_ev=0.4105, max_ev=0.5113
- draw: rows=6, avg_ev=0.3015, max_ev=0.37
- home: rows=8, avg_ev=0.3084, max_ev=0.5842

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 282
Forward fixture prediction rows: 282
Full model prediction rows: 0
Baseline prediction rows: 282
Max forward predictions: 300
Ready for price join: True
- 2026-06-03 02:50 | Hoo P R / Lai P J vs Faza M / Pranata A S P | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 07:00 | Pakistan Panthers vs Asian Stars | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 07:30 | Belconnen United FC vs Tuggeranong United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 08:15 | Broadmeadow Magic FC vs Maitland FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 09:00 | Hawkesbury City SC vs Gladesville Ryde Magic | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 09:00 | Portugal vs Kazakhstan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 09:00 | Sydney Olympic FC vs University of NSW | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 09:30 | Rochedale Rovers vs Magic United Tfa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 09:30 | Sunshine Coast Wanderers vs St George Willawong FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 11:00 | Nepal vs Bangladesh | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 11:30 | Philippines vs Guam | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 12:00 | Indonesia vs Singapore | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 13:00 | Japan vs Portugal | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 13:00 | Milford FC vs Magesi FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 13:00 | Philippines vs Australia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 14:30 | FK Gazalkent vs FC Jayxun | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 15:00 | Greece vs Serbia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 15:00 | India vs Bhutan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 15:00 | Montenegro vs Georgia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 15:00 | Pakistan vs West Indies | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-06-03 15:30 | Croatia vs Qatar | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 282
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 5392
Log type: probability_only_no_market_prices
- 2026-06-07 2026-06-03 14:00:00 | FC Arlanda vs Assyriska FF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 14:15:00 | RC Celta Fortuna vs CE Europa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 15:00:00 | Ranheim vs Stroemmen IF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 16:30:00 | Denmark vs Ukraine | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 16:30:00 | Deportes La Serena vs Deportes Union La Calera | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 16:30:00 | Universidad de Chile vs Audax Italiano | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 16:30:00 | Zamora CF vs Villarreal CF B | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 19:00:00 | CR Brasil AL vs Sao Bernardo FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 19:00:00 | Greece vs Italy | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 19:00:00 | Huachipato vs Colo-Colo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 19:00:00 | Morocco vs Norway | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 19:00:00 | UD Las Palmas vs Malaga CF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 20:00:00 | Ecuador vs Guatemala | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 22:00:00 | CD O´Higgins vs CD Palestino | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-07 2026-06-03 22:00:00 | Deportes Limache vs CD Everton Vina del Mar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-08 2026-06-03 17:00:00 | FC Stockholm Internazionale vs Vasalunds IF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-08 2026-06-03 17:30:00 | FC Jarfalla vs IFK Stocksund | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-08 2026-06-03 22:00:00 | Liverpool Montevideo vs Cerro Largo FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-08 2026-06-03 23:00:00 | America FC MG vs AC Goianiense GO | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-08 2026-06-03 23:00:00 | Vila Nova FC GO vs Botafogo FC SP | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 282
Manual template rows: 282
Rows with complete manual odds: 0
Rows missing manual odds: 282
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-06-03 18:00 | ADO 20 Heemskerk vs IJsselmeervogels
- 2026-06-03 18:00 | Albania vs Israel
- 2026-06-03 17:45 | America FC RJ vs Sao Goncalo EC RJ
- 2026-06-03 23:00 | Annapolis Blues FC vs Lionsbridge FC
- 2026-06-03 17:45 | Araruama FC RJ vs Marica FC RJ
- 2026-06-03 17:00 | Atus Velden vs FC Gleisdorf 09
- 2026-06-03 23:00 | Avai FC SC vs Chapecoense SC
- 2026-06-03 07:30 | Belconnen United FC vs Tuggeranong United FC
- 2026-06-03 17:00 | BK Olympic vs Lunds BK
- 2026-06-03 22:00 | Boca Juniors vs Defensa Y Justicia Reserve
- 2026-06-03 23:00 | Brevard SC vs Fort Lauderdale United FC
- 2026-06-03 08:15 | Broadmeadow Magic FC vs Maitland FC
- 2026-06-03 21:00 | Capo FC vs Socal Reds FC
- 2026-06-03 23:00 | Charlotte Eagles vs Tobacco Road FC
- 2026-06-03 23:00 | Christos FC vs Charlottesville Blues

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 282
Source counts: {'odds_api_io_events_bookmaker_filtered': 241, 'odds_api_io_events_search': 41}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-06-03 18:00 | ADO 20 Heemskerk vs IJsselmeervogels | netherlands-tweede-divisie | odds_api_io_events_bookmaker_filtered
- 2026-06-03 18:00 | Albania vs Israel | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-03 17:45 | America FC RJ vs Sao Goncalo EC RJ | brazil-carioca-serie-a2 | odds_api_io_events_bookmaker_filtered
- 2026-06-03 23:00 | Annapolis Blues FC vs Lionsbridge FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-06-03 17:45 | Araruama FC RJ vs Marica FC RJ | brazil-carioca-serie-a2 | odds_api_io_events_bookmaker_filtered
- 2026-06-03 17:00 | Atus Velden vs FC Gleisdorf 09 | austria-amateur-regionalliga-centre | odds_api_io_events_bookmaker_filtered
- 2026-06-03 23:00 | Avai FC SC vs Chapecoense SC | brazil-copa-sul-sudeste | odds_api_io_events_bookmaker_filtered
- 2026-06-03 07:30 | Belconnen United FC vs Tuggeranong United FC | australia-u23-capital-npl | odds_api_io_events_bookmaker_filtered
- 2026-06-03 17:00 | BK Olympic vs Lunds BK | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-06-03 22:00 | Boca Juniors vs Defensa Y Justicia Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-03 23:00 | Brevard SC vs Fort Lauderdale United FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-06-03 08:15 | Broadmeadow Magic FC vs Maitland FC | australia-northern-nsw-premier-league-women | odds_api_io_events_bookmaker_filtered
- 2026-06-03 21:00 | Capo FC vs Socal Reds FC | usa-usl-w-league | odds_api_io_events_bookmaker_filtered
- 2026-06-03 23:00 | Charlotte Eagles vs Tobacco Road FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-06-03 23:00 | Christos FC vs Charlottesville Blues | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-06-03 23:00 | Cleveland SC vs Ambassadors FC Ohio | usa-national-premier-soccer-league | odds_api_io_events_bookmaker_filtered
- 2026-06-03 15:30 | Croatia vs Qatar | international-youth-u21-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-03 23:00 | Davis Legacy vs San Francisco Glens SC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-06-03 18:00 | Denmark vs Congo DR | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-06-03 18:00 | Estudiantes de LP Reserve vs Independiente Rivadavia de Mendoza Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-06-03 14:30 | FK Gazalkent vs FC Jayxun | uzbekistan-pro-liga | odds_api_io_events_bookmaker_filtered
- 2026-06-03 20:30 | France vs Japan | international-nations-league-women | odds_api_io_events_search
- 2026-06-03 17:00 | Gibraltar vs Virgin Islands, British | international-int-friendly-games | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 282
Rows with complete odds: 0
- 2026-06-03 18:00 | ADO 20 Heemskerk vs IJsselmeervogels | bookmaker=bet365_manual
- 2026-06-03 18:00 | Albania vs Israel | bookmaker=bet365_manual
- 2026-06-03 17:45 | America FC RJ vs Sao Goncalo EC RJ | bookmaker=bet365_manual
- 2026-06-03 23:00 | Annapolis Blues FC vs Lionsbridge FC | bookmaker=bet365_manual
- 2026-06-03 17:45 | Araruama FC RJ vs Marica FC RJ | bookmaker=bet365_manual
- 2026-06-03 17:00 | Atus Velden vs FC Gleisdorf 09 | bookmaker=bet365_manual
- 2026-06-03 23:00 | Avai FC SC vs Chapecoense SC | bookmaker=bet365_manual
- 2026-06-03 07:30 | Belconnen United FC vs Tuggeranong United FC | bookmaker=bet365_manual
- 2026-06-03 17:00 | BK Olympic vs Lunds BK | bookmaker=bet365_manual
- 2026-06-03 22:00 | Boca Juniors vs Defensa Y Justicia Reserve | bookmaker=bet365_manual
- 2026-06-03 23:00 | Brevard SC vs Fort Lauderdale United FC | bookmaker=bet365_manual
- 2026-06-03 08:15 | Broadmeadow Magic FC vs Maitland FC | bookmaker=bet365_manual
- 2026-06-03 21:00 | Capo FC vs Socal Reds FC | bookmaker=bet365_manual
- 2026-06-03 23:00 | Charlotte Eagles vs Tobacco Road FC | bookmaker=bet365_manual
- 2026-06-03 23:00 | Christos FC vs Charlottesville Blues | bookmaker=bet365_manual
- 2026-06-03 23:00 | Cleveland SC vs Ambassadors FC Ohio | bookmaker=bet365_manual
- 2026-06-03 15:30 | Croatia vs Qatar | bookmaker=bet365_manual
- 2026-06-03 23:00 | Davis Legacy vs San Francisco Glens SC | bookmaker=bet365_manual
- 2026-06-03 18:00 | Denmark vs Congo DR | bookmaker=bet365_manual
- 2026-06-03 18:00 | Estudiantes de LP Reserve vs Independiente Rivadavia de Mendoza Reserve | bookmaker=bet365_manual
- 2026-06-03 14:30 | FK Gazalkent vs FC Jayxun | bookmaker=bet365_manual
- 2026-06-03 20:30 | France vs Japan | bookmaker=bet365_manual
- 2026-06-03 17:00 | Gibraltar vs Virgin Islands, British | bookmaker=bet365_manual
- 2026-06-03 15:00 | Greece vs Serbia | bookmaker=bet365_manual

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
- 2026-06-03 18:00 | ADO 20 Heemskerk vs IJsselmeervogels
- 2026-06-03 18:00 | Albania vs Israel
- 2026-06-03 17:45 | America FC RJ vs Sao Goncalo EC RJ
- 2026-06-03 23:00 | Annapolis Blues FC vs Lionsbridge FC
- 2026-06-03 17:45 | Araruama FC RJ vs Marica FC RJ
- 2026-06-03 17:00 | Atus Velden vs FC Gleisdorf 09
- 2026-06-03 23:00 | Avai FC SC vs Chapecoense SC
- 2026-06-03 07:30 | Belconnen United FC vs Tuggeranong United FC
- 2026-06-03 17:00 | BK Olympic vs Lunds BK
- 2026-06-03 22:00 | Boca Juniors vs Defensa Y Justicia Reserve
- 2026-06-03 23:00 | Brevard SC vs Fort Lauderdale United FC
- 2026-06-03 08:15 | Broadmeadow Magic FC vs Maitland FC
- 2026-06-03 21:00 | Capo FC vs Socal Reds FC
- 2026-06-03 23:00 | Charlotte Eagles vs Tobacco Road FC
- 2026-06-03 23:00 | Christos FC vs Charlottesville Blues
- 2026-06-03 23:00 | Cleveland SC vs Ambassadors FC Ohio
- 2026-06-03 15:30 | Croatia vs Qatar
- 2026-06-03 23:00 | Davis Legacy vs San Francisco Glens SC
- 2026-06-03 18:00 | Denmark vs Congo DR

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 930
Valid forward/proxy log rows: 927
Deduped forward/proxy observation rows: 739
Duplicate forward/proxy log rows: 188
Valid automatic proxy observation rows: 927
Deduped automatic proxy observation rows: 739
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
### SV Donau vs SC/ESV Parndorf 1919
- Date/time: 2026-06-03 17:30
- League/phase: austria-amateur-regionalliga-ost / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.2
- Fair odds: 2.65
- Model probability: 0.3772
- Probability band: 0.35-0.45
- EV: 0.5842
- Probability edge: 0.1391
- Alignment penalty: 0.5842
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0687
- Prediction ID: a73ca48ce1f6c1fc8c80
### Sunshine Coast Wanderers vs St George Willawong FC
- Date/time: 2026-06-03 09:30
- League/phase: australia-queensland-premier-league-1 / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.33
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
Total logged paper-test rows: 930
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 123, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 56, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 930, 'source_used': 'automatic_forward_value_snapshots'}
- SV Donau vs SC/ESV Parndorf 1919 | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.2 | prob=0.3772 | EV=0.5842 | edge=0.1391 | penalty=0.5842 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Sunshine Coast Wanderers vs St George Willawong FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SK Bischofshofen vs SC Schwaz | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Vilavelhense FC ES vs Vitoria FC ES | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Presidente Hayes vs Deportivo Pinoza | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Vasalunds IF vs FC Jarfalla | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SV Anthering vs SV Burmoos | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.1105 | penalty=0.4145 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Araruama FC RJ vs Marica FC RJ | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.7 | prob=0.3772 | EV=0.3956 | edge=0.1069 | penalty=0.3956 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- America FC RJ vs Sao Goncalo EC RJ | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Nepal vs Bangladesh | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Atus Velden vs FC Gleisdorf 09 | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Rochedale Rovers vs Magic United Tfa | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.0821 | penalty=0.308 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ntnui vs Fk Kvik Trondheim | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.3 | prob=0.3772 | EV=0.2448 | edge=0.0742 | penalty=0.2448 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Gazalkent vs FC Jayxun | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Rochedale Rovers vs Magic United Tfa | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SC Neusiedl am See 1919 vs SC Wiener Viktoria | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.0695 | penalty=0.2259 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SC Kalsdorf vs SPG Wallern/ASV St. Marienkirchen | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.6 | prob=0.3488 | EV=0.2557 | edge=0.071 | penalty=0.2557 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Poland vs Nigeria | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.6 | prob=0.3488 | EV=0.2557 | edge=0.071 | penalty=0.2557 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
