# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-12T03:43:47.547968+00:00`
GitHub run: `308` attempt `1`
GitHub SHA: `d734be67f7ae449e246aab44ee90b995b9a63553`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 10 |  |  |
| odds-api.io forward fixtures | True | 162 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 30 |  |  |
| Forward price coverage report | True | 80 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 1 |  |  |
| Proxy candidate observations | True | 10 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 10 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 5 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 80 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 80
- Automatic value snapshots: 30
- Positive EV proxy rows: 15
- Proxy observation rows: 7
- Valid forward/proxy log rows: 30
- Deduped forward/proxy log rows: 17
- Duplicate forward/proxy log rows identified: 13
- Fresh API match coverage rate: 0.125
- Matches with fresh API price: 10
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
Current: 30 value snapshots; fresh API coverage rate 0.125.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 17 deduped forward/proxy rows; 13 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 135
Upcoming fixture rows: 0
Proxy price rows: 0
Sources attempted: 1
Errors: 0
No usable proxy odds rows were available from Football-Data fixtures source.

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 161
Fixture team rows unmatched: 313
Ready for model-fixture join: False
Automatic forward price rows: 10
odds-api.io price rows: 10
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. FC Slovacko Uherske Hradiste | suggestion=nan | type=unmatched
- FC Banik Ostrava | suggestion=nan | type=unmatched
- Aberdeen FC | suggestion=nan | type=unmatched
- St Mirren FC | suggestion=nan | type=unmatched
- AE Kifisia FC | suggestion=nan | type=unmatched
- Atromitos Athinon | suggestion=nan | type=unmatched
- AL Faisaly (Jor) | suggestion=nan | type=unmatched
- Ramtha SC | suggestion=nan | type=unmatched
- Al Hussein Irbid | suggestion=nan | type=unmatched
- Al Wehdat | suggestion=nan | type=unmatched
- AL Ittihad Kalba | suggestion=nan | type=unmatched
- AL Nasr | suggestion=nan | type=unmatched
- Al Nassr Club | suggestion=nan | type=unmatched
- Al Hilal SFC | suggestion=nan | type=unmatched
- AL Wahda FC | suggestion=nan | type=unmatched
- Khorfakkan | suggestion=nan | type=unmatched
- AL Wasl | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 80
Automatic price rows: 10
Value snapshot rows: 30
Matches with any automatic price: 10
Matches with fresh API price: 10
Matches with odds-api.io price: 10
Fresh API match coverage rate: 0.125
odds-api.io match coverage rate: 0.125
Real-money ready: False
## Match coverage
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Gold Coast Knights vs Gold Coast United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Gwangju FC vs FC Seoul | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Sportivo Ameliano vs Deportivo Recoleta Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | Singida Black Stars SC vs Namungo FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | Murdoch University Melville FC Reserves vs Joondalup City FC Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | Fardu Ferghana vs Xorazm Fk Urganch | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | Deportivo Maldonado Reserve vs Racing Club Montevideo | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 80
Proxy price rows: 10
Matched prediction rows: 10
Value snapshot rows: 30
odds-api.io snapshot rows: 30
Baseline snapshot rows: 30
Full model snapshot rows: 0
Positive EV rows: 15
Source counts: {'odds_api_io_Bet365_ML': 30}
- 2026-05-12 | Gold Coast Knights vs Gold Coast United FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.3488 | EV=6.3248 | match=1.0
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-12 | Gwangju FC vs FC Seoul | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-12 | Gold Coast Knights vs Gold Coast United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.274 | EV=1.603 | match=1.0
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | match=1.0
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | match=1.0
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | match=1.0
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | match=1.0
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | match=1.0
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=4.2 | prob=0.274 | EV=0.1508 | match=1.0
- 2026-05-12 | Gwangju FC vs FC Seoul | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=4.2 | prob=0.274 | EV=0.1508 | match=1.0
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3488 | EV=0.08128 | match=1.0
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=3.8 | prob=0.274 | EV=0.0412 | match=1.0
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3488 | EV=0.0028 | match=1.0
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=3.5 | prob=0.274 | EV=-0.041 | match=1.0
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3488 | EV=-0.05824 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 30
Pre-dedupe proxy candidate observation rows: 10
Proxy candidate observation rows: 10
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 7
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3488 | EV=0.08128 | edge=0.026219 | penalty=0.08127881059330822 | tier=suppressed_proxy_watchlist | score=0.1087
- 2026-05-12 | Gwangju FC vs FC Seoul | selection=DRAW | source=odds_api_io_Bet365_ML | odds=4.2 | prob=0.274 | EV=0.1508 | edge=0.035905 | penalty=0.15080115080115086 | tier=suppressed_proxy_watchlist | score=0.1084
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=4.2 | prob=0.274 | EV=0.1508 | edge=0.035905 | penalty=0.15080115080115086 | tier=suppressed_proxy_watchlist | score=0.1084
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | selection=AWAY | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3488 | EV=0.0028 | edge=0.000974 | penalty=0.002800250700062623 | tier=suppressed_proxy_watchlist | score=0.1044
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | selection=DRAW | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.274 | EV=0.0412 | edge=0.010842 | penalty=0.041199583520166616 | tier=suppressed_proxy_watchlist | score=0.1034

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 10
Explained rows: 10
Distinct blockers: 5
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 7
- probability_or_league_rule_suppressed: 7
- low_probability_band_under_0_35: 7
- ev_above_real_candidate_cap_possible_overconfidence: 5
- edge_below_candidate_threshold: 2
## Row explanations
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | sel=AWAY | score=0.1087 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35 | improve=collect settled forward results before trusting low-probability selections
- 2026-05-12 | Gwangju FC vs FC Seoul | sel=DRAW | score=0.1084 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; needs better market alignment or stricter probability calibration
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | sel=DRAW | score=0.1084 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; needs better market alignment or stricter probability calibration
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | sel=AWAY | score=0.1044 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | sel=DRAW | score=0.1034 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 30
Paper proxy observation rows: 7
Positive EV value rows: 15
Suppressed-band observation rows: 7
Distinct matches: 7
Distinct sources: 0
Max EV: 0.37
Average EV: 0.166697
Max probability edge: 0.074
Average match confidence: None
## By selection
- away: rows=2, avg_ev=0.042, max_ev=0.0813
- draw: rows=5, avg_ev=0.2166, max_ev=0.37

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 161
Forward fixture prediction rows: 80
Full model prediction rows: 0
Baseline prediction rows: 80
Max forward predictions: 80
Ready for price join: True
- 2026-05-12 07:30 | Canberra White Eagles FC vs Queanbeyan City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 08:45 | Brothers Union vs Mohammedan SC Dhaka | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 09:45 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 10:00 | FC Oleksandriya vs FC Zorya Luhansk | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 10:30 | Cerro Porteno Asuncion vs Guarani Asuncion | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 10:30 | Gangwon FC vs Daejeon Citizen FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 10:30 | Gold Coast Knights vs Gold Coast United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 10:30 | Gwangju FC vs FC Seoul | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 10:30 | Hellenic Athletic Club vs Darwin Hearts FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 10:30 | Incheon United FC vs FC Pohang Steelers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 10:30 | Sportivo Ameliano vs Deportivo Recoleta Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 11:00 | Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 11:00 | Singida Black Stars SC vs Namungo FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 11:15 | Murdoch University Melville FC Reserves vs Joondalup City FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 12:00 | Fardu Ferghana vs Xorazm Fk Urganch | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 12:30 | FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 13:00 | Deportivo Maldonado Reserve vs Racing Club Montevideo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 13:00 | Namdhari FC vs Gokulam Kerala FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 13:15 | TRA United vs Jkt Tanzania | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 13:50 | Sur SC vs Al-Khaboora | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 14:00 | El Gouna FC vs Kahrabaa Ismailia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 80
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 121
Log type: probability_only_no_market_prices
- 2026-05-12 2026-05-12 17:30:00 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 17:30:00 | TS Galaxy FC vs Mamelodi Sundowns | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:00:00 | Al Nassr Club vs Al Hilal SFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:00:00 | Colon FC Reserve vs Liverpool Montevideo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:00:00 | Defensa Y Justicia Reserve vs CA Platense | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:00:00 | Gimnasia de la Plata Reserve vs CA Banfield | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:00:00 | Newells Old Boys vs CA Quilmes Reserve | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:00:00 | Racing Club Avellaneda vs Velez Sarsfield Reserve | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:00:00 | Real Betis Seville vs Elche CF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:00:00 | Sparta Prague vs FC Viktoria Plzen | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:30:00 | Cerro Largo FC vs Boston River | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:30:00 | Grasshopper Club Zurich vs FC Winterthur | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:30:00 | FC Luzern vs FC Zurich | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:30:00 | Penarol Montevideo vs Nacional de Montevideo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:30:00 | Red Star FC vs Rodez Aveyron Football | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:30:00 | Servette Geneva vs Lausanne-Sport | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:45:00 | Aberdeen FC vs St Mirren FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:45:00 | Clyde FC vs Hamilton Academical FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:45:00 | FC Domagnano vs AC Virtus | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 18:45:00 | Dundee United vs Livingston FC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 161
Manual template rows: 161
Rows with complete manual odds: 0
Rows missing manual odds: 161
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava
- 2026-05-12 18:45 | Aberdeen FC vs St Mirren FC
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr
- 2026-05-12 18:00 | Al Nassr Club vs Al Hilal SFC
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan
- 2026-05-12 14:10 | AL Wasl vs AL Jazira
- 2026-05-12 16:20 | Al-Kholood vs Al-Okhdood Club
- 2026-05-12 16:20 | Al-Rustaq vs Ibri
- 2026-05-12 16:00 | Asteras Tripolis vs Panserraikos FC
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota.
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC
- 2026-05-12 17:30 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 161
Source counts: {'odds_api_io_events_bookmaker_filtered': 160, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | czechia-1-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-12 18:45 | Aberdeen FC vs St Mirren FC | scotland-premiership | odds_api_io_events_bookmaker_filtered
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon | greece-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC | jordan-jordan-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat | jordan-jordan-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 18:00 | Al Nassr Club vs Al Hilal SFC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 14:10 | AL Wasl vs AL Jazira | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 16:20 | Al-Kholood vs Al-Okhdood Club | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 16:20 | Al-Rustaq vs Ibri | oman-omani-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 16:00 | Asteras Tripolis vs Panserraikos FC | greece-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota. | colombia-primera-a-apertura | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:30 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC | israel-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride | usa-national-womens-soccer-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:15 | Botev Plovdiv vs FC Arda Kardzhali | bulgaria-parva-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-12 08:45 | Brothers Union vs Mohammedan SC Dhaka | bangladesh-federation-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe | argentina-liga-profesional | odds_api_io_events_bookmaker_filtered
- 2026-05-12 19:30 | CA Osasuna vs Atletico Madrid | spain-laliga | odds_api_io_events_bookmaker_filtered
- 2026-05-12 07:30 | Canberra White Eagles FC vs Queanbeyan City FC | australia-u23-capital-npl | odds_api_io_events_bookmaker_filtered
- 2026-05-12 20:00 | CD Real Santander vs Boca Juniors de Cali | colombia-copa-colombia | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:00 | Central Espanol Reserve vs Defensor Sporting | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 161
Rows with complete odds: 0
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | bookmaker=bet365_manual
- 2026-05-12 18:45 | Aberdeen FC vs St Mirren FC | bookmaker=bet365_manual
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon | bookmaker=bet365_manual
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC | bookmaker=bet365_manual
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat | bookmaker=bet365_manual
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr | bookmaker=bet365_manual
- 2026-05-12 18:00 | Al Nassr Club vs Al Hilal SFC | bookmaker=bet365_manual
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan | bookmaker=bet365_manual
- 2026-05-12 14:10 | AL Wasl vs AL Jazira | bookmaker=bet365_manual
- 2026-05-12 16:20 | Al-Kholood vs Al-Okhdood Club | bookmaker=bet365_manual
- 2026-05-12 16:20 | Al-Rustaq vs Ibri | bookmaker=bet365_manual
- 2026-05-12 16:00 | Asteras Tripolis vs Panserraikos FC | bookmaker=bet365_manual
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota. | bookmaker=bet365_manual
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC | bookmaker=bet365_manual
- 2026-05-12 17:30 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC | bookmaker=bet365_manual
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride | bookmaker=bet365_manual
- 2026-05-12 17:15 | Botev Plovdiv vs FC Arda Kardzhali | bookmaker=bet365_manual
- 2026-05-12 08:45 | Brothers Union vs Mohammedan SC Dhaka | bookmaker=bet365_manual
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe | bookmaker=bet365_manual
- 2026-05-12 19:30 | CA Osasuna vs Atletico Madrid | bookmaker=bet365_manual
- 2026-05-12 07:30 | Canberra White Eagles FC vs Queanbeyan City FC | bookmaker=bet365_manual
- 2026-05-12 20:00 | CD Real Santander vs Boca Juniors de Cali | bookmaker=bet365_manual
- 2026-05-12 17:00 | Central Espanol Reserve vs Defensor Sporting | bookmaker=bet365_manual
- 2026-05-12 18:30 | Cerro Largo FC vs Boston River | bookmaker=bet365_manual

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
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava
- 2026-05-12 18:45 | Aberdeen FC vs St Mirren FC
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr
- 2026-05-12 18:00 | Al Nassr Club vs Al Hilal SFC
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan
- 2026-05-12 14:10 | AL Wasl vs AL Jazira
- 2026-05-12 16:20 | Al-Kholood vs Al-Okhdood Club
- 2026-05-12 16:20 | Al-Rustaq vs Ibri
- 2026-05-12 16:00 | Asteras Tripolis vs Panserraikos FC
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota.
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC
- 2026-05-12 17:30 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride
- 2026-05-12 17:15 | Botev Plovdiv vs FC Arda Kardzhali
- 2026-05-12 08:45 | Brothers Union vs Mohammedan SC Dhaka
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 33
Valid forward/proxy log rows: 30
Deduped forward/proxy observation rows: 17
Duplicate forward/proxy log rows: 13
Valid automatic proxy observation rows: 30
Deduped automatic proxy observation rows: 17
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-11 | Estrela vs Famalicao | selection=home | phase=automatic_forward_price_proxy | tier=proxy_observation | score=0.2607
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | selection=home | phase=automatic_forward_price_proxy | tier=proxy_observation | score=0.2592
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | selection=home | phase=automatic_forward_price_proxy | tier=priority_proxy_observation | score=0.2576
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | selection=home | phase=automatic_forward_price_proxy | tier=priority_proxy_observation | score=0.25420000000000004
- 2026-05-11 | Tondela vs Moreirense | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.13470000000000001
- 2026-05-11 | Huesca vs Sociedad B | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.134
- 2026-05-11 | Tottenham vs Leeds | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1313
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.12860000000000002
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.12860000000000002
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.12660000000000002
- 2026-05-11 | Napoli vs Bologna | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.12610000000000002
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1247
- 2026-05-11 | Vallecano vs Girona | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1245
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1216
- 2026-05-12 | Gwangju FC vs FC Seoul | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0684
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.06810000000000001
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.067
## Raw valid rows
- 2026-05-11 | Napoli vs Bologna | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Vallecano vs Girona | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation

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
### Canberra White Eagles FC vs Queanbeyan City FC
- Date/time: 2026-05-12 07:30
- League/phase: australia-u23-capital-npl / automatic_forward_price_proxy
- Selection: DRAW
- Market odds: 5.0
- Fair odds: 3.65
- Model probability: 0.274
- Probability band: 0.00-0.35
- EV: 0.37
- Probability edge: 0.074
- Alignment penalty: 0.37
- Suppression action: proxy_suppressed_band_observe_only
- Paper tier: suppressed_band_proxy_observation
- Paper score: 0.0706
- Prediction ID: dabb233183cfe864c5d8
### Sunshine Coast Wanderers FC vs Eastern Suburbs FC
- Date/time: 2026-05-12 09:45
- League/phase: australia-queensland-npl-women / automatic_forward_price_proxy
- Selection: DRAW
- Market odds: 5.0
- Fair odds: 3.65
- Model probability: 0.274
- Probability band: 0.00-0.35

## paper_test_picks

# Paper Test Picks
Observation-only picks. These are not real-money recommendations.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Baseline coverage observations are not model signals. They exist only to test the pipeline and collect settlement evidence.
Suppressed historical bands may be tracked only as proxy observation and remain excluded from real-money readiness.
Source used: automatic_forward_value_snapshots
Current paper-test picks: 7
Newly logged paper-test picks: 3
Total logged paper-test rows: 33
- Canberra White Eagles FC vs Queanbeyan City FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Sunshine Coast Wanderers FC vs Eastern Suburbs FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Gangwon FC vs Daejeon Citizen FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.1 | prob=0.3488 | EV=0.0813 | edge=0.0262 | penalty=0.0813 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Hellenic Athletic Club vs Darwin Hearts FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.2 | prob=0.274 | EV=0.1508 | edge=0.0359 | penalty=0.1508 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Gwangju FC vs FC Seoul | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.2 | prob=0.274 | EV=0.1508 | edge=0.0359 | penalty=0.1508 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Incheon United FC vs FC Pohang Steelers | coverage=baseline_unmatched_fixture | selection=AWAY | odds=2.88 | prob=0.3488 | EV=0.0028 | edge=0.001 | penalty=0.0028 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Cerro Porteno Asuncion vs Guarani Asuncion | coverage=baseline_unmatched_fixture | selection=DRAW | odds=3.8 | prob=0.274 | EV=0.0412 | edge=0.0108 | penalty=0.0412 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation

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
