# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-14T19:04:02.632654+00:00`
GitHub run: `348` attempt `1`
GitHub SHA: `91ff457b043b3ca13eeb134429aa6e608a96acf8`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 3 |  |  |
| Football-Data upcoming odds proxy | True | 9 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 50 |  |  |
| odds-api.io forward fixtures | True | 647 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 201 |  |  |
| Forward price coverage report | True | 255 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 3 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 255 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 171
- Positive EV proxy rows: 90
- Proxy observation rows: 25
- Valid forward/proxy log rows: 200
- Deduped forward/proxy log rows: 135
- Duplicate forward/proxy log rows identified: 65
- Fresh API match coverage rate: 0.1633
- Matches with fresh API price: 49
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
Current: 171 value snapshots; fresh API coverage rate 0.1633.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 135 deduped forward/proxy rows; 65 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 26
Upcoming fixture rows: 0
Proxy price rows: 0
Sources attempted: 1
Errors: 0
No usable proxy odds rows were available from Football-Data fixtures source.

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 649
Fixture team rows unmatched: 1283
Ready for model-fixture join: False
Automatic forward price rows: 49
odds-api.io price rows: 49
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 12 de Junio de Villa Hayes | suggestion=nan | type=unmatched
- Club Dr Benjamin Aceval | suggestion=nan | type=unmatched
- Aalesunds FK | suggestion=nan | type=unmatched
- Hoenefoss BK | suggestion=nan | type=unmatched
- FC Aarau | suggestion=nan | type=unmatched
- Yverdon-Sport | suggestion=nan | type=unmatched
- ACS Champions FC Arges | suggestion=nan | type=unmatched
- Rapid Bucuresti 1923 | suggestion=nan | type=unmatched
- Adelaide United FC | suggestion=nan | type=unmatched
- Auckland FC | suggestion=nan | type=unmatched
- Ajman Club | suggestion=nan | type=unmatched
- Al-Nasr Dubai CSC | suggestion=nan | type=unmatched
- Akritas Chlorakas | suggestion=nan | type=unmatched
- AEL Limassol | suggestion=nan | type=unmatched
- AL Arabi (UAE) | suggestion=nan | type=unmatched
- Gulf United | suggestion=nan | type=unmatched
- AL Budaiya | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 49
Value snapshot rows: 171
Matches with any automatic price: 49
Matches with fresh API price: 49
Matches with odds-api.io price: 49
Fresh API match coverage rate: 0.1633
odds-api.io match coverage rate: 0.1633
Real-money ready: False
## Match coverage
- 2026-05-15 | CF Monterrey vs Club America | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Auckland FC Reserves vs Auckland City FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-15 | Kyrgyzstan vs Turkmenistan | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-15 | Hurstville FC vs Prospect United | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-15 | Shenzhen 2028 FC vs Shaanxi Union FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Bentleigh Greens SC vs Heidelberg United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Melbourne Knights FC vs Eltham Redbacks FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Northcote City FC vs FC Bulleen Lions | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Caboolture Sports FC vs North Star | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-15 | Dalian Kewei vs Nantong Zhiyun | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Semen Padang FC vs Persebaya Surabaya | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Bunga Raya FC vs Malaysia University | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Penang FA vs Brunei DPMM FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Slovakia vs San Marino | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-15 | Brisbane Roar FC vs Lions FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-15 | Nunawading City vs Whittlesea United SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 49
Matched prediction rows: 55
Value snapshot rows: 171
odds-api.io snapshot rows: 171
Baseline snapshot rows: 171
Full model snapshot rows: 0
Positive EV rows: 90
Source counts: {'odds_api_io_Bet365_ML': 171}
- 2026-05-15 | Bentleigh Greens SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3772 | EV=9.9388 | match=1.0
- 2026-05-15 | Bentleigh Greens vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3772 | EV=9.9388 | match=0.96
- 2026-05-15 | ETO FC Gyor vs Pecsi MFC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=26.0 | prob=0.3488 | EV=8.0688 | match=1.0
- 2026-05-15 | Al Ittihad Ahli of Aleppo vs Al-Shorta SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-15 | Bentleigh Greens vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=0.96
- 2026-05-15 | Bentleigh Greens SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-05-15 | ETO FC Gyor vs Pecsi MFC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.274 | EV=2.288 | match=1.0
- 2026-05-15 | Beijing Guoan vs Qingdao Hainiu FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-15 | Brisbane Roar FC vs Lions FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-15 | Semen Padang FC vs Persebaya Surabaya | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-15 | Shenzhen 2028 FC vs Shaanxi Union FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3772 | EV=1.2632 | match=1.0
- 2026-05-15 | Dalian Kewei vs Nantong Zhiyun | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3772 | EV=1.2632 | match=1.0
- 2026-05-15 | Club Olimpia vs Recoleta FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-15 | SC Villa vs URA FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-15 | Bentleigh Greens SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=0.96
- 2026-05-15 | Bentleigh Greens vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-05-16 | Dandenong City SC vs Oakleigh Cannons FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3772 | EV=0.9803 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 171
Pre-dedupe proxy candidate observation rows: 67
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 2
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-15 | Myj-Gmsc vs FC Bengaluru United | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-15 | Werribee City FC vs Malvern City FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-15 | Dire Dawa Kenema vs Bahir Dar Kenema FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-15 | Qingdao Red Lions vs Nanjing City | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-15 | Kingston City FC vs Eastern Lions SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-15 | Hangzhou Linping Wuyue vs Foshan Nanshi FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-15 | CF Monterrey vs Club America | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-05-15 | Mekelle 70 Enderta FC vs Ethiopian Medhin | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-05-15 | Curtin University SC vs Murdoch University Melville FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145
- 2026-05-16 | Curtin University SC Reserves vs Murdoch University Melville FC Reserves | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145
- 2026-05-15 | Northcote City FC vs FC Bulleen Lions | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-05-15 | Bnei Yehuda Tel Aviv FC vs MS Football Hapoel Kiryat Yam | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: ev_above_real_candidate_cap_possible_overconfidence
Real-money ready: False
## Blocker summary
- ev_above_real_candidate_cap_possible_overconfidence: 9
- market_alignment_penalty_too_high_for_real_candidate: 9
- watchlist_only_pending_forward_settlement: 2
- probability_or_league_rule_suppressed: 2
- low_probability_band_under_0_35: 2
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-15 | Myj-Gmsc vs FC Bengaluru United | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Werribee City FC vs Malvern City FC | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Dire Dawa Kenema vs Bahir Dar Kenema FC | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Qingdao Red Lions vs Nanjing City | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-15 | Kingston City FC vs Eastern Lions SC | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-15 | Hangzhou Linping Wuyue vs Foshan Nanshi FC | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-15 | CF Monterrey vs Club America | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Mekelle 70 Enderta FC vs Ethiopian Medhin | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Curtin University SC vs Murdoch University Melville FC | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Curtin University SC Reserves vs Murdoch University Melville FC Reserves | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Northcote City FC vs FC Bulleen Lions | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Bnei Yehuda Tel Aviv FC vs MS Football Hapoel Kiryat Yam | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 171
Paper proxy observation rows: 25
Positive EV value rows: 90
Suppressed-band observation rows: 0
Distinct matches: 25
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.413689
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=11, avg_ev=0.3265, max_ev=0.5696
- draw: rows=5, avg_ev=0.3426, max_ev=0.4385
- home: rows=9, avg_ev=0.5598, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 649
Forward fixture prediction rows: 300
Full model prediction rows: 1
Baseline prediction rows: 299
Max forward predictions: 300
Ready for price join: True
- 2026-05-15 03:10 | CF Monterrey vs Club America | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 07:00 | Auckland FC Reserves vs Auckland City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 07:30 | Kyrgyzstan vs Turkmenistan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:00 | Hurstville FC vs Prospect United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:00 | Maitland FC Reserve vs Cooks Hill United FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:00 | Shenzhen 2028 FC vs Shaanxi Union FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:15 | Bentleigh Greens SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:15 | Melbourne Knights FC vs Eltham Redbacks FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:15 | Northcote City FC vs FC Bulleen Lions | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:30 | Caboolture Sports FC vs North Star | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:30 | Dalian Kewei vs Nantong Zhiyun | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:30 | Semen Padang FC vs Persebaya Surabaya | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 08:45 | Bunga Raya FC vs Malaysia University | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 09:00 | Penang FA vs Brunei DPMM FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 09:00 | Slovakia vs San Marino | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 09:15 | Brisbane Roar FC vs Lions FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 09:30 | Nunawading City vs Whittlesea United SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 09:30 | Peninsula Power FC vs Gold Coast Knights | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 09:35 | Adelaide United FC vs Auckland FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 09:45 | Dandenong City SC vs Oakleigh Cannons | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 09:45 | Kingston City FC vs Eastern Lions SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 903
Log type: probability_only_no_market_prices
- 2026-05-16 2026-05-15 05:30:00 | Adelaide Atletico VSC vs Eastern United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 05:30:00 | Adelaide Blue Eagles vs Fulham United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 05:30:00 | FC Bulleen Lions U20 vs Alamein FC U20 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 05:30:00 | Para Hills Knights SC vs Adelaide United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 05:30:00 | Playford City vs Adelaide City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 05:30:00 | South Adelaide FC vs Salisbury United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 05:30:00 | Sturt Lions vs Croydon FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 05:30:00 | Tigers FC vs Canberra Olympic FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 05:30:00 | West Adelaide SC vs West Torrens Birkalla | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:00:00 | Altona Magic SC vs Preston Lions FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:00:00 | Charlestown Azzurri FC vs Adamstown Rosebud JFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:00:00 | Peninsula Power vs Gold Coast Knights FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:00:00 | Sunshine Coast Wanderers vs St George Willawong | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:00:00 | Wynnum Wolves FC vs Eastern Suburbs | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:15:00 | Melbourne City FC vs Wellington Phoenix | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:30:00 | Hakoah vs Inter Lions FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:30:00 | Macarthur Rams vs Canterbury Bankstown FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:30:00 | Northern Tigers vs Western City Rangers FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 06:30:00 | St George FC vs Sydney United 58 FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-15 07:00:00 | Bankstown United FC vs Hawkesbury City SC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 649
Manual template rows: 649
Rows with complete manual odds: 0
Rows missing manual odds: 649
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-15 22:30 | 12 de Junio de Villa Hayes vs Club Dr Benjamin Aceval
- 2026-05-15 16:00 | Aalesunds FK vs Hoenefoss BK
- 2026-05-15 18:15 | FC Aarau vs Yverdon-Sport
- 2026-05-15 17:30 | ACS Champions FC Arges vs Rapid Bucuresti 1923
- 2026-05-15 09:35 | Adelaide United FC vs Auckland FC
- 2026-05-15 14:10 | Ajman Club vs Al-Nasr Dubai CSC
- 2026-05-15 16:00 | Akritas Chlorakas vs AEL Limassol
- 2026-05-15 14:05 | AL Arabi (UAE) vs Gulf United
- 2026-05-15 16:00 | AL Budaiya vs Al-Ahli SC Manama
- 2026-05-15 16:00 | Al Hidd vs Al-Shabab
- 2026-05-15 14:05 | AL Ittifaq vs Emirates Club
- 2026-05-15 13:00 | Al Ittihad Ahli of Aleppo vs Al-Shorta SC
- 2026-05-15 14:30 | AL Mosul SC vs Duhok FC
- 2026-05-15 17:00 | Al Quwa Al Jawiya vs AL Talaba
- 2026-05-15 16:00 | Al Riffa vs AL Bahrain

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 649
Source counts: {'odds_api_io_events_bookmaker_filtered': 648, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-15 22:30 | 12 de Junio de Villa Hayes vs Club Dr Benjamin Aceval | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-15 16:00 | Aalesunds FK vs Hoenefoss BK | norway-toppserien-women | odds_api_io_events_bookmaker_filtered
- 2026-05-15 18:15 | FC Aarau vs Yverdon-Sport | switzerland-challenge-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 17:30 | ACS Champions FC Arges vs Rapid Bucuresti 1923 | romania-superliga | odds_api_io_events_bookmaker_filtered
- 2026-05-15 09:35 | Adelaide United FC vs Auckland FC | australia-a-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:10 | Ajman Club vs Al-Nasr Dubai CSC | united-arab-emirates-arabian-gulf-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 16:00 | Akritas Chlorakas vs AEL Limassol | cyprus-1st-division | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:05 | AL Arabi (UAE) vs Gulf United | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-15 16:00 | AL Budaiya vs Al-Ahli SC Manama | bahrain-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 16:00 | Al Hidd vs Al-Shabab | bahrain-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:05 | AL Ittifaq vs Emirates Club | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-15 13:00 | Al Ittihad Ahli of Aleppo vs Al-Shorta SC | syria-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:30 | AL Mosul SC vs Duhok FC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 17:00 | Al Quwa Al Jawiya vs AL Talaba | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 16:00 | Al Riffa vs AL Bahrain | bahrain-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:40 | Al Shabab Kuwait vs Kazma SC | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:05 | Al Urooba UAE vs Dubai United FC | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-15 16:45 | Al Wasl FC vs Ittihad Kalba FC | united-arab-emirates-arabian-gulf-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:05 | Al-Dhaid vs Hatta SC | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:30 | Al-Gharraf SC vs AL Karkh | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:05 | Al-Hamriyah vs Dibba Al-Hisn SC | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-15 18:00 | Al-Taawoun FC vs Al-Riyadh SC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 16:30 | Alingsas FC United vs IF Elfsborg | sweden-amateur-elitettan-women | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 649
Rows with complete odds: 0
- 2026-05-15 22:30 | 12 de Junio de Villa Hayes vs Club Dr Benjamin Aceval | bookmaker=bet365_manual
- 2026-05-15 16:00 | Aalesunds FK vs Hoenefoss BK | bookmaker=bet365_manual
- 2026-05-15 18:15 | FC Aarau vs Yverdon-Sport | bookmaker=bet365_manual
- 2026-05-15 17:30 | ACS Champions FC Arges vs Rapid Bucuresti 1923 | bookmaker=bet365_manual
- 2026-05-15 09:35 | Adelaide United FC vs Auckland FC | bookmaker=bet365_manual
- 2026-05-15 14:10 | Ajman Club vs Al-Nasr Dubai CSC | bookmaker=bet365_manual
- 2026-05-15 16:00 | Akritas Chlorakas vs AEL Limassol | bookmaker=bet365_manual
- 2026-05-15 14:05 | AL Arabi (UAE) vs Gulf United | bookmaker=bet365_manual
- 2026-05-15 16:00 | AL Budaiya vs Al-Ahli SC Manama | bookmaker=bet365_manual
- 2026-05-15 16:00 | Al Hidd vs Al-Shabab | bookmaker=bet365_manual
- 2026-05-15 14:05 | AL Ittifaq vs Emirates Club | bookmaker=bet365_manual
- 2026-05-15 13:00 | Al Ittihad Ahli of Aleppo vs Al-Shorta SC | bookmaker=bet365_manual
- 2026-05-15 14:30 | AL Mosul SC vs Duhok FC | bookmaker=bet365_manual
- 2026-05-15 17:00 | Al Quwa Al Jawiya vs AL Talaba | bookmaker=bet365_manual
- 2026-05-15 16:00 | Al Riffa vs AL Bahrain | bookmaker=bet365_manual
- 2026-05-15 14:40 | Al Shabab Kuwait vs Kazma SC | bookmaker=bet365_manual
- 2026-05-15 14:05 | Al Urooba UAE vs Dubai United FC | bookmaker=bet365_manual
- 2026-05-15 16:45 | Al Wasl FC vs Ittihad Kalba FC | bookmaker=bet365_manual
- 2026-05-15 14:05 | Al-Dhaid vs Hatta SC | bookmaker=bet365_manual
- 2026-05-15 14:30 | Al-Gharraf SC vs AL Karkh | bookmaker=bet365_manual
- 2026-05-15 14:05 | Al-Hamriyah vs Dibba Al-Hisn SC | bookmaker=bet365_manual
- 2026-05-15 18:00 | Al-Taawoun FC vs Al-Riyadh SC | bookmaker=bet365_manual
- 2026-05-15 16:30 | Alingsas FC United vs IF Elfsborg | bookmaker=bet365_manual
- 2026-05-15 14:30 | Amanat Baghdad SC vs Al Kahrabaa SC | bookmaker=bet365_manual

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
- 2026-05-15 22:30 | 12 de Junio de Villa Hayes vs Club Dr Benjamin Aceval
- 2026-05-15 16:00 | Aalesunds FK vs Hoenefoss BK
- 2026-05-15 18:15 | FC Aarau vs Yverdon-Sport
- 2026-05-15 17:30 | ACS Champions FC Arges vs Rapid Bucuresti 1923
- 2026-05-15 09:35 | Adelaide United FC vs Auckland FC
- 2026-05-15 14:10 | Ajman Club vs Al-Nasr Dubai CSC
- 2026-05-15 16:00 | Akritas Chlorakas vs AEL Limassol
- 2026-05-15 14:05 | AL Arabi (UAE) vs Gulf United
- 2026-05-15 16:00 | AL Budaiya vs Al-Ahli SC Manama
- 2026-05-15 16:00 | Al Hidd vs Al-Shabab
- 2026-05-15 14:05 | AL Ittifaq vs Emirates Club
- 2026-05-15 13:00 | Al Ittihad Ahli of Aleppo vs Al-Shorta SC
- 2026-05-15 14:30 | AL Mosul SC vs Duhok FC
- 2026-05-15 17:00 | Al Quwa Al Jawiya vs AL Talaba
- 2026-05-15 16:00 | Al Riffa vs AL Bahrain
- 2026-05-15 14:40 | Al Shabab Kuwait vs Kazma SC
- 2026-05-15 14:05 | Al Urooba UAE vs Dubai United FC
- 2026-05-15 16:45 | Al Wasl FC vs Ittihad Kalba FC
- 2026-05-15 14:05 | Al-Dhaid vs Hatta SC

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 203
Valid forward/proxy log rows: 200
Deduped forward/proxy observation rows: 135
Duplicate forward/proxy log rows: 65
Valid automatic proxy observation rows: 200
Deduped automatic proxy observation rows: 135
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-14 | Sanat Mes Kerman FC vs Mes Shahr-e Babak | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-14 | Mjallby AIF vs Hammarby IF | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-15 | Hangzhou Linping Wuyue vs Foshan Nanshi FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-15 | Caboolture Sports FC vs North Star | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061
- 2026-05-15 | Caboolture FC vs North Star FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061
- 2026-05-14 | Viking FK 2 vs Akra | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-15 | Al Ittihad Ahli of Aleppo vs Al-Shorta SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
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
### Tianjin Jinmen Tiger vs Chengdu Rongcheng
- Date/time: 2026-05-15 11:35
- League/phase: china-chinese-super-league / automatic_forward_price_proxy
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
- Prediction ID: 29ef1e33635218db26d0
### FK Karvan Yevlakh vs Gabala FK
- Date/time: 2026-05-15 13:00
- League/phase: azerbaijan-premier-league / automatic_forward_price_proxy
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
Newly logged paper-test picks: 20
Total logged paper-test rows: 203
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 171, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 77, 'current_paper_picks': 25, 'newly_logged_picks': 20, 'total_logged_paper_rows': 203, 'source_used': 'automatic_forward_value_snapshots'}
- Tianjin Jinmen Tiger vs Chengdu Rongcheng | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Karvan Yevlakh vs Gabala FK | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mekelle 70 Enderta FC vs Ethiopian Medhin | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CF Monterrey vs Club America | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Penang FA vs Brunei DPMM FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Curtin University SC vs Murdoch University Melville FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Curtin University SC Reserves vs Murdoch University Melville FC Reserves | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Essendon Royals SC vs Moreland City FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Myj-Gmsc vs FC Bengaluru United | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.8 | prob=0.3772 | EV=0.4334 | edge=0.114 | penalty=0.4334 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Dire Dawa Kenema vs Bahir Dar Kenema FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.1105 | penalty=0.4145 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Werribee City FC vs Malvern City FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.1105 | penalty=0.4145 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Northcote City FC vs FC Bulleen Lions | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Bnei Yehuda Tel Aviv FC vs MS Football Hapoel Kiryat Yam | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Beijing Guoan vs Qingdao Hainiu FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Caboolture Sports FC vs North Star | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.0821 | penalty=0.308 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Caboolture FC vs North Star FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.0821 | penalty=0.308 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al Ittihad Ahli of Aleppo vs Al-Shorta SC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PVF Cand B vs Ho Chi Minh City FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.6 | prob=0.3488 | EV=0.2557 | edge=0.071 | penalty=0.2557 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
