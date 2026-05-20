# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-19T14:43:30.664824+00:00`
GitHub run: `360` attempt `1`
GitHub SHA: `c1835732e28371890d7d0299ea657699f26ec25c`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 11 |  |  |
| Football-Data upcoming odds proxy | True | 30 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 47 |  |  |
| odds-api.io forward fixtures | True | 242 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 294 |  |  |
| Forward price coverage report | True | 210 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 210 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 234
- Automatic value snapshots: 246
- Positive EV proxy rows: 123
- Proxy observation rows: 25
- Valid forward/proxy log rows: 407
- Deduped forward/proxy log rows: 283
- Duplicate forward/proxy log rows identified: 124
- Fresh API match coverage rate: 0.2479
- Matches with fresh API price: 58
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
Current: 246 value snapshots; fresh API coverage rate 0.2479.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 283 deduped forward/proxy rows; 124 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 11
Upcoming fixture rows: 6
Proxy price rows: 15
Sources attempted: 1
Errors: 0
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_bet365_proxy | 2.2/3.75/3.0
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_max_market_proxy | 2.2/3.75/3.1
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_average_market_proxy | 2.14/3.61/2.92
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_bet365_proxy | 4.5/3.7/1.75
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_max_market_proxy | 4.6/3.8/1.8
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_average_market_proxy | 4.32/3.61/1.73
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_bet365_proxy | 7.0/4.75/1.38
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_max_market_proxy | 7.0/5.25/1.41
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_average_market_proxy | 6.57/5.0/1.37
- 2026-05-21 16:00 | Atromitos vs Panserraikos | football_data_max_market_proxy | 1.67/4.0/6.0
- 2026-05-21 16:00 | Atromitos vs Panserraikos | football_data_average_market_proxy | 1.57/3.71/5.28
- 2026-05-21 17:00 | Kifisia vs Larisa | football_data_max_market_proxy | 2.3/3.25/3.2
- 2026-05-21 17:00 | Kifisia vs Larisa | football_data_average_market_proxy | 2.22/3.13/2.98
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis | football_data_max_market_proxy | 2.4/3.3/3.05
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis | football_data_average_market_proxy | 2.29/3.13/2.9

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 234
Fixture team rows unmatched: 465
Ready for model-fixture join: False
Automatic forward price rows: 73
odds-api.io price rows: 58
Football-Data price rows: 15
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 3B Sport AM | suggestion=nan | type=unmatched
- CR Vasco da Gama RJ | suggestion=nan | type=unmatched
- Aalesunds FK | suggestion=nan | type=unmatched
- SK Brann | suggestion=nan | type=unmatched
- Aasane Fotball | suggestion=nan | type=unmatched
- Sandnes Ulf | suggestion=nan | type=unmatched
- AC Connecticut | suggestion=nan | type=unmatched
- Connecticut Rush | suggestion=nan | type=unmatched
- Academia Puerto Cabello B | suggestion=nan | type=unmatched
- Deportivo Lara | suggestion=nan | type=unmatched
- Al Masry Club | suggestion=nan | type=unmatched
- AL Ahly SC (EGY) | suggestion=nan | type=unmatched
- AL Minaa | suggestion=nan | type=unmatched
- AL Mosul SC | suggestion=nan | type=unmatched
- AL Najaf | suggestion=nan | type=unmatched
- AL Karkh | suggestion=nan | type=unmatched
- Al Quwa Al Jawiya | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 234
Automatic price rows: 73
Value snapshot rows: 246
Matches with any automatic price: 64
Matches with fresh API price: 58
Matches with odds-api.io price: 58
Fresh API match coverage rate: 0.2479
odds-api.io match coverage rate: 0.2479
Real-money ready: False
## Match coverage
- 2026-05-20 | Melbourne City FC vs Tokyo Verdy Beleza | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Taichung Blue Whale vs New Taipei Hang Yuen | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Sydney Olympic FC vs University of NSW | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-20 | Canberra Olympic vs Canberra Croatia FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Tuggeranong United FC vs Belconnen United | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | West Canberra Wanderers FC vs Majura FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Hunters FC vs FC Ulaanbaatar | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Naegohyang Womens FC vs Suwon WFC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Liaoning Tieren FC vs Qingdao Hainiu FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Preah Khan Reach Svay Rieng FC vs Boeung Ket Angkor FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Bashundhara Kings vs Mohammedan SC Dhaka | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Shanghai Shenhua FC vs Wuhan Three Towns FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Chongqing Tonglianglong FC vs Yunnan Yukun | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Ethiopian Coffee SC vs Fasil Kenema SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | FC Gareji Sagarejo vs FC Merani Martvili | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | FC Meshakhte Tkibuli vs FC Torpedo Kutaisi | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-20 | Zhejiang FC vs Shandong Taishan FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 234
Proxy price rows: 73
Matched prediction rows: 67
Value snapshot rows: 246
odds-api.io snapshot rows: 174
Baseline snapshot rows: 246
Full model snapshot rows: 0
Positive EV rows: 123
Source counts: {'odds_api_io_Bet365_ML': 174, 'football_data_max_market_proxy': 27, 'football_data_average_market_proxy': 27, 'football_data_bet365_proxy': 18}
- 2026-05-20 | Tuggeranong United FC vs Belconnen United | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=1.0
- 2026-05-20 | West Canberra Wanderers FC vs Majura FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=26.0 | prob=0.3488 | EV=8.0688 | match=1.0
- 2026-05-20 | Hacken Gothenburg vs Vaxjo DFF | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.3488 | EV=5.6272 | match=1.0
- 2026-05-20 | FC Chernigiv vs FC Dynamo Kyiv | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-05-20 | FK Atmosfera vs FK Panevezys | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-05-20 | Tuggeranong United FC vs Belconnen United | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.274 | EV=4.206 | match=1.0
- 2026-05-20 | Flint City Bucks vs Lansing City Football | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-20 | IK Start vs Bodoe/Glimt | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3772 | EV=2.772 | match=1.0
- 2026-05-20 | El Bayadh vs JS Saoura | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-20 | Hunters FC vs FC Ulaanbaatar | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-20 | FK Tukums 2000/TSS vs Riga FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-20 | CS Sfaxien vs Stade Gabesien | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-20 | West Canberra Wanderers FC vs Majura FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.274 | EV=1.74 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-21 | Yellow-Red KV Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=0.96
- 2026-05-21 | Yellow-Red KV Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=0.96
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 246
Pre-dedupe proxy candidate observation rows: 80
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-20 | Canberra Olympic vs Canberra Croatia FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-20 | Selangor FC vs Buriram United | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-20 | Taichung Blue Whale vs New Taipei Hang Yuen | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-20 | SK Sparta Kolin vs FK Varnsdorf | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-20 | Tampereen Ilves vs FC Inter Turku | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-20 | Zhejiang FC vs Shandong Taishan FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-20 | FC Kuressaare vs FC Nomme United | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-20 | Melbourne City FC vs Tokyo Verdy Beleza | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-20 | Peimari Utd vs Eupa | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-20 | Chongqing Tonglianglong FC vs Yunnan Yukun | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-20 | AL Najaf vs AL Karkh | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145
- 2026-05-20 | FC Meshakhte Tkibuli vs FC Torpedo Kutaisi | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3772 | EV=0.47108 | edge=0.12079 | penalty=0.4710814710814708 | tier=proxy_watchlist | score=0.212

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 4
Top blocker: ev_above_real_candidate_cap_possible_overconfidence
Real-money ready: False
## Blocker summary
- ev_above_real_candidate_cap_possible_overconfidence: 7
- market_alignment_penalty_too_high_for_real_candidate: 7
- edge_below_candidate_threshold: 3
- watchlist_only_pending_forward_settlement: 2
## Row explanations
- 2026-05-20 | Canberra Olympic vs Canberra Croatia FC | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-20 | Selangor FC vs Buriram United | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-20 | Taichung Blue Whale vs New Taipei Hang Yuen | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-20 | SK Sparta Kolin vs FK Varnsdorf | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-20 | Tampereen Ilves vs FC Inter Turku | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-20 | Zhejiang FC vs Shandong Taishan FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-20 | FC Kuressaare vs FC Nomme United | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-20 | Melbourne City FC vs Tokyo Verdy Beleza | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-20 | Peimari Utd vs Eupa | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-20 | Chongqing Tonglianglong FC vs Yunnan Yukun | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-20 | AL Najaf vs AL Karkh | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-20 | FC Meshakhte Tkibuli vs FC Torpedo Kutaisi | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 246
Paper proxy observation rows: 25
Positive EV value rows: 123
Suppressed-band observation rows: 0
Distinct matches: 23
Distinct sources: 0
Max EV: 0.781
Average EV: 0.520504
Max probability edge: 0.159809
Average match confidence: None
## By selection
- away: rows=7, avg_ev=0.4849, max_ev=0.6568
- draw: rows=7, avg_ev=0.5853, max_ev=0.781
- home: rows=11, avg_ev=0.5019, max_ev=0.7351

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 234
Forward fixture prediction rows: 234
Full model prediction rows: 1
Baseline prediction rows: 233
Max forward predictions: 300
Ready for price join: True
- 2026-05-20 05:00 | Melbourne City FC vs Tokyo Verdy Beleza | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 07:30 | Taichung Blue Whale vs New Taipei Hang Yuen | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 09:00 | Sydney Olympic FC vs University of NSW | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 09:30 | Canberra Olympic vs Canberra Croatia FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 09:30 | Tuggeranong United FC vs Belconnen United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 09:30 | West Canberra Wanderers FC vs Majura FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 10:00 | Hunters FC vs FC Ulaanbaatar | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 10:00 | Naegohyang Womens FC vs Suwon WFC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 11:00 | Liaoning Tieren FC vs Qingdao Hainiu FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 11:00 | Preah Khan Reach Svay Rieng FC vs Boeung Ket Angkor FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 11:35 | Shanghai Shenhua FC vs Wuhan Three Towns FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 12:00 | Chongqing Tonglianglong FC vs Yunnan Yukun | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 12:00 | Ethiopian Coffee SC vs Fasil Kenema SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 12:00 | FC Gareji Sagarejo vs FC Merani Martvili | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 12:00 | FC Meshakhte Tkibuli vs FC Torpedo Kutaisi | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 12:00 | Zhejiang FC vs Shandong Taishan FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 13:00 | CA Tembetary Ypane vs 12 de Junio de Villa Hayes | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 13:00 | de Graafschap vs ADO Den Haag | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 13:00 | Guairena FC vs Paraguari AC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-20 13:00 | Kks Lech Poznan vs GKS Katowice | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 234
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 2504
Log type: probability_only_no_market_prices
- 2026-05-21 2026-05-20 02:00:00 | Montego Bay United vs Cavalier FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 02:00:00 | Portland Thorns FC vs Bay FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 02:30:00 | Washington Spirit vs CF Pachuca | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 12:00:00 | Adama City FC vs Welwalo Adigrat | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 12:00:00 | Arba Minch Ketema vs Sidama Bunna SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 14:00:00 | Inter Kashi FC vs SC East Bengal | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 14:00:00 | Punjab FC vs Mumbai City | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 15:00:00 | BFC Daugavpils vs Ogre United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 15:00:00 | Negelle Arsi vs Shire Endaselassie FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 15:00:00 | FC Spaeri vs FC Dinamo Batumi | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 17:00:00 | FC RFS vs FS Jelgava | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 17:00:00 | FC Rustavi vs FC Samgurali Tskaltubo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 18:00:00 | Boca Juniors vs CA River Plate (ARG) | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 18:30:00 | FK Velez Mostar vs FK Sarajevo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 18:30:00 | FK Zeljeznicar Sarajevo vs NK Siroki Brijeg | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-20 22:00:00 | Fort Lauderdale United FC II vs Brevard SC Riptide | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-22 2026-05-20 00:00:00 | Sao Paulo FC SP vs Red Bull Bragantino SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-22 2026-05-20 23:00:00 | Union de Santa Fe vs CA Independiente Avellaneda | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-20 01:30:00 | Midlakes United vs Tacoma Stars | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-20 15:00:00 | Brighton and Hove Albion vs Manchester United | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 234
Manual template rows: 234
Rows with complete manual odds: 0
Rows missing manual odds: 234
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-20 19:30 | 3B Sport AM vs CR Vasco da Gama RJ
- 2026-05-20 18:00 | Aalesunds FK vs SK Brann
- 2026-05-20 17:00 | Aasane Fotball vs Sandnes Ulf
- 2026-05-20 23:00 | AC Connecticut vs Connecticut Rush
- 2026-05-20 19:30 | Academia Puerto Cabello B vs Deportivo Lara
- 2026-05-20 17:00 | Al Masry Club vs AL Ahly SC (EGY)
- 2026-05-20 14:30 | AL Minaa vs AL Mosul SC
- 2026-05-20 14:30 | AL Najaf vs AL Karkh
- 2026-05-20 17:00 | Al Quwa Al Jawiya vs Al Zawraa
- 2026-05-20 17:00 | Al Shorta SC vs Erbil SC
- 2026-05-20 18:00 | Al-Khaleej Club vs Al Ahli Saudi FC
- 2026-05-20 18:00 | Al-Najma vs Al-Shabab FC (SA)
- 2026-05-20 18:00 | America FC RJ vs Marica FC RJ
- 2026-05-20 17:00 | Aragvi Dusheti vs FC Kolkheti-1913 Poti
- 2026-05-20 18:00 | Ascoli Calcio 1898 vs Potenza Calcio

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 234
Source counts: {'odds_api_io_events_bookmaker_filtered': 223, 'football_data_fixtures_proxy': 6, 'odds_api_io_events_search': 4, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-20 19:30 | 3B Sport AM vs CR Vasco da Gama RJ | brazil-brasileiro-serie-a2-women | odds_api_io_events_bookmaker_filtered
- 2026-05-20 18:00 | Aalesunds FK vs SK Brann | norway-eliteserien | odds_api_io_events_bookmaker_filtered
- 2026-05-20 17:00 | Aasane Fotball vs Sandnes Ulf | norway-1st-division | odds_api_io_events_bookmaker_filtered
- 2026-05-20 23:00 | AC Connecticut vs Connecticut Rush | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-20 19:30 | Academia Puerto Cabello B vs Deportivo Lara | venezuela-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-20 17:00 | Al Masry Club vs AL Ahly SC (EGY) | egypt-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-20 14:30 | AL Minaa vs AL Mosul SC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-20 14:30 | AL Najaf vs AL Karkh | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-20 17:00 | Al Quwa Al Jawiya vs Al Zawraa | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-20 17:00 | Al Shorta SC vs Erbil SC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-20 18:00 | Al-Khaleej Club vs Al Ahli Saudi FC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-20 18:00 | Al-Najma vs Al-Shabab FC (SA) | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-20 18:00 | America FC RJ vs Marica FC RJ | brazil-carioca-serie-a2 | odds_api_io_events_bookmaker_filtered
- 2026-05-20 17:00 | Aragvi Dusheti vs FC Kolkheti-1913 Poti | georgia-erovnuli-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-20 18:00 | Ascoli Calcio 1898 vs Potenza Calcio | italy-serie-c-promotion-playoffs | odds_api_io_events_bookmaker_filtered
- 2026-05-20 16:45 | ASO Chlef vs JS Kabylie | algeria-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-20 17:45 | Atletico Andahuaylas vs Club Alianza Lima | peru-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-20 18:00 | Avai FC SC vs Cuiaba EC MT | brazil-u20-campeonato-brasileiro | odds_api_io_events_bookmaker_filtered
- 2026-05-20 21:30 | Barquisimeto SC vs Atletico El Vigia | venezuela-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-20 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka | bangladesh-federation-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-20 22:00 | Boca Juniors vs CA Huracan | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-20 18:00 | Botafogo FC SP vs SC Recife PE | brazil-u20-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-20 22:00 | CA Boston River vs CD O´Higgins | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 234
Rows with complete odds: 0
- 2026-05-20 19:30 | 3B Sport AM vs CR Vasco da Gama RJ | bookmaker=bet365_manual
- 2026-05-20 18:00 | Aalesunds FK vs SK Brann | bookmaker=bet365_manual
- 2026-05-20 17:00 | Aasane Fotball vs Sandnes Ulf | bookmaker=bet365_manual
- 2026-05-20 23:00 | AC Connecticut vs Connecticut Rush | bookmaker=bet365_manual
- 2026-05-20 19:30 | Academia Puerto Cabello B vs Deportivo Lara | bookmaker=bet365_manual
- 2026-05-20 17:00 | Al Masry Club vs AL Ahly SC (EGY) | bookmaker=bet365_manual
- 2026-05-20 14:30 | AL Minaa vs AL Mosul SC | bookmaker=bet365_manual
- 2026-05-20 14:30 | AL Najaf vs AL Karkh | bookmaker=bet365_manual
- 2026-05-20 17:00 | Al Quwa Al Jawiya vs Al Zawraa | bookmaker=bet365_manual
- 2026-05-20 17:00 | Al Shorta SC vs Erbil SC | bookmaker=bet365_manual
- 2026-05-20 18:00 | Al-Khaleej Club vs Al Ahli Saudi FC | bookmaker=bet365_manual
- 2026-05-20 18:00 | Al-Najma vs Al-Shabab FC (SA) | bookmaker=bet365_manual
- 2026-05-20 18:00 | America FC RJ vs Marica FC RJ | bookmaker=bet365_manual
- 2026-05-20 17:00 | Aragvi Dusheti vs FC Kolkheti-1913 Poti | bookmaker=bet365_manual
- 2026-05-20 18:00 | Ascoli Calcio 1898 vs Potenza Calcio | bookmaker=bet365_manual
- 2026-05-20 16:45 | ASO Chlef vs JS Kabylie | bookmaker=bet365_manual
- 2026-05-20 17:45 | Atletico Andahuaylas vs Club Alianza Lima | bookmaker=bet365_manual
- 2026-05-20 18:00 | Avai FC SC vs Cuiaba EC MT | bookmaker=bet365_manual
- 2026-05-20 21:30 | Barquisimeto SC vs Atletico El Vigia | bookmaker=bet365_manual
- 2026-05-20 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka | bookmaker=bet365_manual
- 2026-05-20 22:00 | Boca Juniors vs CA Huracan | bookmaker=bet365_manual
- 2026-05-20 18:00 | Botafogo FC SP vs SC Recife PE | bookmaker=bet365_manual
- 2026-05-20 22:00 | CA Boston River vs CD O´Higgins | bookmaker=bet365_manual
- 2026-05-20 21:00 | CA Bucaramanga Sa vs Asociacion Deportivo Cali | bookmaker=bet365_manual

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
- 2026-05-20 19:30 | 3B Sport AM vs CR Vasco da Gama RJ
- 2026-05-20 18:00 | Aalesunds FK vs SK Brann
- 2026-05-20 17:00 | Aasane Fotball vs Sandnes Ulf
- 2026-05-20 23:00 | AC Connecticut vs Connecticut Rush
- 2026-05-20 19:30 | Academia Puerto Cabello B vs Deportivo Lara
- 2026-05-20 17:00 | Al Masry Club vs AL Ahly SC (EGY)
- 2026-05-20 14:30 | AL Minaa vs AL Mosul SC
- 2026-05-20 14:30 | AL Najaf vs AL Karkh
- 2026-05-20 17:00 | Al Quwa Al Jawiya vs Al Zawraa
- 2026-05-20 17:00 | Al Shorta SC vs Erbil SC
- 2026-05-20 18:00 | Al-Khaleej Club vs Al Ahli Saudi FC
- 2026-05-20 18:00 | Al-Najma vs Al-Shabab FC (SA)
- 2026-05-20 18:00 | America FC RJ vs Marica FC RJ
- 2026-05-20 17:00 | Aragvi Dusheti vs FC Kolkheti-1913 Poti
- 2026-05-20 18:00 | Ascoli Calcio 1898 vs Potenza Calcio
- 2026-05-20 16:45 | ASO Chlef vs JS Kabylie
- 2026-05-20 17:45 | Atletico Andahuaylas vs Club Alianza Lima
- 2026-05-20 18:00 | Avai FC SC vs Cuiaba EC MT
- 2026-05-20 21:30 | Barquisimeto SC vs Atletico El Vigia

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 410
Valid forward/proxy log rows: 407
Deduped forward/proxy observation rows: 283
Duplicate forward/proxy log rows: 124
Valid automatic proxy observation rows: 407
Deduped automatic proxy observation rows: 283
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-15 | Shanghai Port FC vs Zhejiang FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-19 | MB Rouissat vs Paradou AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Kjp Kouvola vs Lautp | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Ntnui vs Orkla | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.058600000000000006
- 2026-05-15 | Melbourne Knights FC vs Eltham Redbacks FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.058600000000000006
- 2026-05-15 | Brisbane Roar FC vs Lions FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Broadmeadow Magic FC vs Newcastle Olympic FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Semen Padang FC vs Persebaya Surabaya | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-19 | Northeast United FC vs Mohammedan SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-15 | Cong An TP Ho Chi Minh City FC vs SHB Da Nang | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-19 | Derby Academie vs Onze Createurs | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Al Kahrabaa SC vs Al-Gharraf SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Diyala FC vs Amanat Baghdad SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Deportivo Capiata vs Club Fernando de La Mora | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.056100000000000004
- 2026-05-19 | SV Ried vs Wolfsberger AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553

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
### KAA Gent vs Union Saint-Gilloise
- Date/time: 2026-05-21 18:30
- League/phase: belgium-pro-league / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.6
- Fair odds: 2.65
- Model probability: 0.3772
- Probability band: 0.35-0.45
- EV: 0.7351
- Probability edge: 0.1598
- Alignment penalty: 0.7351
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0721
- Prediction ID: d115e59493cade2be7e8
### Gent vs St. Gilloise
- Date/time: 2026-05-21 19:30
- League/phase: B1 / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.6
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
Newly logged paper-test picks: 22
Total logged paper-test rows: 410
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 246, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 106, 'current_paper_picks': 25, 'newly_logged_picks': 22, 'total_logged_paper_rows': 410, 'source_used': 'automatic_forward_value_snapshots'}
- KAA Gent vs Union Saint-Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- KAA Gent vs Union Saint-Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- ES Zarzis vs CA Bizertin | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Drina Zvornik vs FK Slavija Sarajevo | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Flint City Bucks vs Lansing City Football | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Chernigiv vs FC Dynamo Kyiv | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SFC Shturmi Sartichala vs FC Gori | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AL Najaf vs AL Karkh | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hunters FC vs FC Ulaanbaatar | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Meshakhte Tkibuli vs FC Torpedo Kutaisi | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.9 | prob=0.3772 | EV=0.4711 | edge=0.1208 | penalty=0.4711 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Tukums 2000/TSS vs Riga FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Canberra Olympic vs Canberra Croatia FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.8 | prob=0.3772 | EV=0.4334 | edge=0.114 | penalty=0.4334 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Bashundhara Kings vs Mohammedan SC Dhaka | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Selangor FC vs Buriram United | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.7 | prob=0.3772 | EV=0.3956 | edge=0.1069 | penalty=0.3956 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Jablonec vs MFK Karvina | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Taichung Blue Whale vs New Taipei Hang Yuen | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
