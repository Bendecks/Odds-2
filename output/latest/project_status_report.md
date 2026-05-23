# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-22T14:25:01.393754+00:00`
GitHub run: `366` attempt `1`
GitHub SHA: `b69cf766e19ff87da34e50579e5ec7b0d95f45d0`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 47 |  |  |
| Football-Data upcoming odds proxy | True | 138 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 57 |  |  |
| odds-api.io forward fixtures | True | 746 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 189 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
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
- Automatic value snapshots: 99
- Positive EV proxy rows: 52
- Proxy observation rows: 25
- Valid forward/proxy log rows: 524
- Deduped forward/proxy log rows: 388
- Duplicate forward/proxy log rows identified: 136
- Fresh API match coverage rate: 0.0967
- Matches with fresh API price: 29
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
Current: 99 value snapshots; fresh API coverage rate 0.0967.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 388 deduped forward/proxy rows; 136 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 47
Upcoming fixture rows: 46
Proxy price rows: 135
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
Upcoming fixture rows: 909
Fixture team rows unmatched: 1741
Ready for model-fixture join: False
Automatic forward price rows: 164
odds-api.io price rows: 29
Football-Data price rows: 135
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 12 de Junio de Villa Hayes | suggestion=nan | type=unmatched
- Tacuary Asuncion | suggestion=nan | type=unmatched
- 1.SK Prostejov | suggestion=nan | type=unmatched
- FC Silon Taborsko | suggestion=nan | type=unmatched
- 3B Sport AM | suggestion=nan | type=unmatched
- Vila Nova FC GO | suggestion=nan | type=unmatched
- AFC Ann Arbor | suggestion=nan | type=unmatched
- Lansing City Football | suggestion=nan | type=unmatched
- AFC Chindia Targoviste | suggestion=nan | type=unmatched
- FC Farul Constanta | suggestion=nan | type=unmatched
- Abecat Ouvidorense GO | suggestion=nan | type=unmatched
- Operario FC MS | suggestion=nan | type=unmatched
- AC Goianiense GO | suggestion=nan | type=unmatched
- Royal GO | suggestion=nan | type=unmatched
- AC Malveira | suggestion=nan | type=unmatched
- GD Vitoria Sernache | suggestion=nan | type=unmatched
- AC Nagano Parceiro | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 164
Value snapshot rows: 99
Matches with any automatic price: 29
Matches with fresh API price: 29
Matches with odds-api.io price: 29
Fresh API match coverage rate: 0.0967
odds-api.io match coverage rate: 0.0967
Real-money ready: False
## Match coverage
- 2026-05-23 | Clarence Zebras FC 2 vs Olympia Warriors Hobart | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Launceston United vs South Hobart FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Taroona vs University of Tasmania | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Davis Legacy vs Almaden FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-23 | Eastern United Reserve vs Adelaide Blue Eagles Reserves | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Green Gully SC vs Heidelberg United FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Waterside Karori vs Wellington Olympic | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-23 | Adelaide Atletico Victory Reserves vs South Adelaide Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Canberra White Eagles FC vs O'Connor Knights SC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Croydon Kings FC Reserve vs North Eastern Metrostars SC Reserves | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Gold Coast United FC vs Rochedale Rovers | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Port Melbourne Sharks SC vs Brunswick Juventus FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Queanbeyan City FC vs Canberra Juventus FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | Auckland United FC vs East Coast Bays | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-23 | Auckland City FC vs Melville United AFC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-23 | Bentleigh Greens SC vs Caroline Springs George Cross FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-23 | FC Fujizakura vs Jfa Academy Fukushima | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 164
Matched prediction rows: 33
Value snapshot rows: 99
odds-api.io snapshot rows: 99
Baseline snapshot rows: 99
Full model snapshot rows: 0
Positive EV rows: 52
Source counts: {'odds_api_io_Bet365_ML': 99}
- 2026-05-23 | Taroona vs Devonport City SC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3772 | EV=18.2372 | match=1.0
- 2026-05-23 | South Melbourne FC vs Bentleigh Greens SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3488 | EV=16.7888 | match=1.0
- 2026-05-23 | South Melbourne FC vs Bentleigh Greens SC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.274 | EV=8.316 | match=1.0
- 2026-05-23 | Birkenhead United AFC vs Bay Olympic | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=23.0 | prob=0.3488 | EV=7.0224 | match=1.0
- 2026-05-23 | Taroona vs Devonport City SC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.274 | EV=6.946 | match=1.0
- 2026-05-23 | Vonds Ichihara FC vs Shizuoka SSU Bonita | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-05-23 | Waterside Karori vs Wellington Olympic | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-05-23 | Riverside Olympic FC vs South Hobart FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3772 | EV=3.9036 | match=1.0
- 2026-05-23 | Birkenhead United AFC vs Bay Olympic | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.274 | EV=2.288 | match=1.0
- 2026-05-23 | Auckland City FC vs Melville United AFC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-23 | Riverside Olympic FC vs South Hobart FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.274 | EV=1.329 | match=1.0
- 2026-05-23 | Nittaidai FC vs Iga FC Kunoichi | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-05-23 | Waterside Karori vs Wellington Olympic | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.274 | EV=1.055 | match=1.0
- 2026-05-23 | NGU Loveledge Nagoya vs Okayama Yunogo Belle | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-23 | Manukau United FC vs Tauranga City AFC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3772 | EV=0.7917 | match=1.0
- 2026-05-23 | Avispa Fukuoka vs Vissel Kobe | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.5 | prob=0.3772 | EV=0.6974 | match=1.0
- 2026-05-23 | Clarence Zebras FC vs Kingborough Lions United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 99
Pre-dedupe proxy candidate observation rows: 36
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 5
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-23 | Croydon Kings FC Reserve vs North Eastern Metrostars SC Reserves | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-23 | Croydon FC vs North Eastern Metrostars SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-23 | Davis Legacy vs Almaden FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-23 | Canberra White Eagles FC vs O'Connor Knights SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-23 | Canberra White Eagles FC vs O'Connor Knights FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-23 | University of Nsw vs Sydney United 58 FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-23 | Clarence Zebras FC vs Kingborough Lions United FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-05-23 | Canberra Olympic vs Belconnen United | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-05-23 | Changwon FC vs Ulsan Citizen FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3488 | EV=0.32544 | edge=0.085642 | penalty=0.325439469824212 | tier=suppressed_proxy_watchlist | score=0.1201
- 2026-05-23 | Auckland City FC vs Melville United AFC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.083524 | penalty=0.4385014385014385 | tier=suppressed_proxy_watchlist | score=0.1196
- 2026-05-23 | Manukau United FC vs Tauranga City AFC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.083524 | penalty=0.4385014385014385 | tier=suppressed_proxy_watchlist | score=0.1196
- 2026-05-23 | South East United FC vs Ulverstone SC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.082133 | penalty=0.3079983650020437 | tier=suppressed_proxy_watchlist | score=0.1194

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
- ev_above_real_candidate_cap_possible_overconfidence: 12
- market_alignment_penalty_too_high_for_real_candidate: 12
- probability_or_league_rule_suppressed: 5
- low_probability_band_under_0_35: 5
## Row explanations
- 2026-05-23 | Croydon Kings FC Reserve vs North Eastern Metrostars SC Reserves | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Croydon FC vs North Eastern Metrostars SC | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Davis Legacy vs Almaden FC | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Canberra White Eagles FC vs O'Connor Knights SC | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Canberra White Eagles FC vs O'Connor Knights FC | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | University of Nsw vs Sydney United 58 FC | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Clarence Zebras FC vs Kingborough Lions United FC | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Canberra Olympic vs Belconnen United | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Changwon FC vs Ulsan Citizen FC | sel=AWAY | score=0.1201 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Auckland City FC vs Melville United AFC | sel=DRAW | score=0.1196 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | Manukau United FC vs Tauranga City AFC | sel=DRAW | score=0.1196 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-23 | South East United FC vs Ulverstone SC | sel=AWAY | score=0.1194 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 99
Paper proxy observation rows: 25
Positive EV value rows: 52
Suppressed-band observation rows: 0
Distinct matches: 19
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.353208
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=8, avg_ev=0.2579, max_ev=0.3952
- draw: rows=8, avg_ev=0.3215, max_ev=0.4385
- home: rows=9, avg_ev=0.4662, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 909
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-23 02:15 | Clarence Zebras FC 2 vs Olympia Warriors Hobart | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:15 | Launceston United vs South Hobart FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:15 | Taroona vs University of Tasmania | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:30 | Davis Legacy vs Almaden FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:30 | Eastern United Reserve vs Adelaide Blue Eagles Reserves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:30 | Green Gully SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:30 | Waterside Karori vs Wellington Olympic | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:45 | Adelaide Atletico Victory Reserves vs South Adelaide Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:45 | Canberra White Eagles FC vs O'Connor Knights SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:45 | Croydon Kings FC Reserve vs North Eastern Metrostars SC Reserves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:45 | Gold Coast United FC vs Rochedale Rovers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:45 | Port Melbourne Sharks SC vs Brunswick Juventus FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 02:45 | Queanbeyan City FC vs Canberra Juventus FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 03:00 | Auckland United FC vs East Coast Bays | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 03:00 | Auckland City FC vs Melville United AFC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 03:00 | Bentleigh Greens SC vs Caroline Springs George Cross FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 03:00 | FC Fujizakura vs Jfa Academy Fukushima | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 03:00 | Holland Park Hawks vs Sunshine Coast Wanderers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 03:00 | Manukau United FC vs Tauranga City AFC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 03:00 | Perth Redstar FC vs Perth SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-23 03:00 | Upper Hutt City FC vs Wellington Phoenix FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 3123
Log type: probability_only_no_market_prices
- 2026-05-23 2026-05-23 13:00:00 | Diamond Harbour FC vs Shillong Lajong FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Durban City FC 2024 vs AmaZulu FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Dynamic Herb Cebu FC vs Davao Aguilas | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Eskilstuna United DFF vs FC Rosengaard Malmo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | FK Partizan Belgrade vs FK Radnik Surdulica | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Flekkeroy IL vs Vindbjart FK | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Halmstads BK vs Orgryte IS | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Herentals FC vs Simba Bhora FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | IK Oddevold vs Ostersunds FK | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | JIPPO vs PK-35 Helsinki | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Johor Darul Ta'zim vs Kuching City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | FC Kairat Almaty vs Kaisar Kyzylorda | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Kaizer Chiefs vs Chippa United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Kalmar FF vs Degerfors IF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Kristianstads DFF vs Hammarby IF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Lamontville Golden Arrows vs TS Galaxy FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Linz AG Blau-Weiss / Kleinmunchen vs SCR Altach | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Magesi FC vs Richards Bay FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Marumo Gallants FC vs Stellenbosch FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-23 13:00:00 | Minas Boca Futebol MG vs Betim Futebol MG | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 909
Manual template rows: 909
Rows with complete manual odds: 0
Rows missing manual odds: 909
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-23 22:00 | 12 de Junio de Villa Hayes vs Tacuary Asuncion
- 2026-05-23 12:00 | 1.SK Prostejov vs FC Silon Taborsko
- 2026-05-23 19:30 | 3B Sport AM vs Vila Nova FC GO
- 2026-05-23 23:00 | AFC Ann Arbor vs Lansing City Football
- 2026-05-23 14:30 | AFC Chindia Targoviste vs FC Farul Constanta
- 2026-05-23 19:00 | Abecat Ouvidorense GO vs Operario FC MS
- 2026-05-23 18:30 | AC Goianiense GO vs Royal GO
- 2026-05-23 16:00 | AC Malveira vs GD Vitoria Sernache
- 2026-05-23 07:00 | AC Nagano Parceiro vs Ventforet Kofu
- 2026-05-23 22:00 | Academia Puerto Cabello vs UCV FC
- 2026-05-23 05:30 | Adelaide United FC vs West Torrens Birkalla
- 2026-05-23 02:45 | Adelaide Atletico Victory Reserves vs South Adelaide Reserve
- 2026-05-23 05:30 | Adelaide Atletico VSC vs South Adelaide FC
- 2026-05-23 05:00 | Adelaide City FC vs FK Beograd
- 2026-05-23 05:30 | Adelaide Comets FC vs Para Hills Knights SC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 909
Source counts: {'odds_api_io_events_bookmaker_filtered': 862, 'football_data_fixtures_proxy': 46, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-23 22:00 | 12 de Junio de Villa Hayes vs Tacuary Asuncion | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-23 12:00 | 1.SK Prostejov vs FC Silon Taborsko | czechia-fnl | odds_api_io_events_bookmaker_filtered
- 2026-05-23 19:30 | 3B Sport AM vs Vila Nova FC GO | brazil-brasileiro-serie-a2-women | odds_api_io_events_bookmaker_filtered
- 2026-05-23 23:00 | AFC Ann Arbor vs Lansing City Football | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-23 14:30 | AFC Chindia Targoviste vs FC Farul Constanta | romania-superliga | odds_api_io_events_bookmaker_filtered
- 2026-05-23 19:00 | Abecat Ouvidorense GO vs Operario FC MS | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-23 18:30 | AC Goianiense GO vs Royal GO | brazil-u20-goiano-1-divisao | odds_api_io_events_bookmaker_filtered
- 2026-05-23 16:00 | AC Malveira vs GD Vitoria Sernache | portugal-campeonato-de-portugal | odds_api_io_events_bookmaker_filtered
- 2026-05-23 07:00 | AC Nagano Parceiro vs Ventforet Kofu | japan-jleague-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-23 22:00 | Academia Puerto Cabello vs UCV FC | venezuela-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-23 05:30 | Adelaide United FC vs West Torrens Birkalla | australia-south-australia-npl | odds_api_io_events_bookmaker_filtered
- 2026-05-23 02:45 | Adelaide Atletico Victory Reserves vs South Adelaide Reserve | australia-south-australia-state-league-1-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-23 05:30 | Adelaide Atletico VSC vs South Adelaide FC | australia-south-australia-state-league-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-23 05:00 | Adelaide City FC vs FK Beograd | australia-south-australia-npl | odds_api_io_events_bookmaker_filtered
- 2026-05-23 05:30 | Adelaide Comets FC vs Para Hills Knights SC | australia-south-australia-npl | odds_api_io_events_bookmaker_filtered
- 2026-05-23 03:15 | Adelaide Comets Reserves vs Para Hills Knights SC Reserve | australia-south-australia-npl-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-23 05:30 | Adelaide Croatia Raiders SC vs Adelaide Olympic FC | australia-south-australia-state-league-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-23 03:15 | Adelaide Croatia Raiders SC Reserve vs Adelaide Olympic FC Reserve | australia-south-australia-state-league-1-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-23 14:00 | FC Aktobe vs FC Kyzylzhar SK | kazakhstan-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-23 16:10 | AL Draih vs AL Ula | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-23 17:45 | AL Fateh vs AL Hazem U21 | saudi-arabia-u21-elite-league | odds_api_io_events_bookmaker_filtered
- 2026-05-23 17:00 | Al Ittihad Al Sakandary vs Ismaily SC | egypt-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-23 15:25 | Al Nahda vs Al Shabab | oman-omani-league | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 909
Rows with complete odds: 0
- 2026-05-23 22:00 | 12 de Junio de Villa Hayes vs Tacuary Asuncion | bookmaker=bet365_manual
- 2026-05-23 12:00 | 1.SK Prostejov vs FC Silon Taborsko | bookmaker=bet365_manual
- 2026-05-23 19:30 | 3B Sport AM vs Vila Nova FC GO | bookmaker=bet365_manual
- 2026-05-23 23:00 | AFC Ann Arbor vs Lansing City Football | bookmaker=bet365_manual
- 2026-05-23 14:30 | AFC Chindia Targoviste vs FC Farul Constanta | bookmaker=bet365_manual
- 2026-05-23 19:00 | Abecat Ouvidorense GO vs Operario FC MS | bookmaker=bet365_manual
- 2026-05-23 18:30 | AC Goianiense GO vs Royal GO | bookmaker=bet365_manual
- 2026-05-23 16:00 | AC Malveira vs GD Vitoria Sernache | bookmaker=bet365_manual
- 2026-05-23 07:00 | AC Nagano Parceiro vs Ventforet Kofu | bookmaker=bet365_manual
- 2026-05-23 22:00 | Academia Puerto Cabello vs UCV FC | bookmaker=bet365_manual
- 2026-05-23 05:30 | Adelaide United FC vs West Torrens Birkalla | bookmaker=bet365_manual
- 2026-05-23 02:45 | Adelaide Atletico Victory Reserves vs South Adelaide Reserve | bookmaker=bet365_manual
- 2026-05-23 05:30 | Adelaide Atletico VSC vs South Adelaide FC | bookmaker=bet365_manual
- 2026-05-23 05:00 | Adelaide City FC vs FK Beograd | bookmaker=bet365_manual
- 2026-05-23 05:30 | Adelaide Comets FC vs Para Hills Knights SC | bookmaker=bet365_manual
- 2026-05-23 03:15 | Adelaide Comets Reserves vs Para Hills Knights SC Reserve | bookmaker=bet365_manual
- 2026-05-23 05:30 | Adelaide Croatia Raiders SC vs Adelaide Olympic FC | bookmaker=bet365_manual
- 2026-05-23 03:15 | Adelaide Croatia Raiders SC Reserve vs Adelaide Olympic FC Reserve | bookmaker=bet365_manual
- 2026-05-23 14:00 | FC Aktobe vs FC Kyzylzhar SK | bookmaker=bet365_manual
- 2026-05-23 16:10 | AL Draih vs AL Ula | bookmaker=bet365_manual
- 2026-05-23 17:45 | AL Fateh vs AL Hazem U21 | bookmaker=bet365_manual
- 2026-05-23 17:00 | Al Ittihad Al Sakandary vs Ismaily SC | bookmaker=bet365_manual
- 2026-05-23 15:25 | Al Nahda vs Al Shabab | bookmaker=bet365_manual
- 2026-05-23 16:15 | Al-Salmiya SC vs Al Shabab Kuwait | bookmaker=bet365_manual

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
- 2026-05-23 22:00 | 12 de Junio de Villa Hayes vs Tacuary Asuncion
- 2026-05-23 12:00 | 1.SK Prostejov vs FC Silon Taborsko
- 2026-05-23 19:30 | 3B Sport AM vs Vila Nova FC GO
- 2026-05-23 23:00 | AFC Ann Arbor vs Lansing City Football
- 2026-05-23 14:30 | AFC Chindia Targoviste vs FC Farul Constanta
- 2026-05-23 19:00 | Abecat Ouvidorense GO vs Operario FC MS
- 2026-05-23 18:30 | AC Goianiense GO vs Royal GO
- 2026-05-23 16:00 | AC Malveira vs GD Vitoria Sernache
- 2026-05-23 07:00 | AC Nagano Parceiro vs Ventforet Kofu
- 2026-05-23 22:00 | Academia Puerto Cabello vs UCV FC
- 2026-05-23 05:30 | Adelaide United FC vs West Torrens Birkalla
- 2026-05-23 02:45 | Adelaide Atletico Victory Reserves vs South Adelaide Reserve
- 2026-05-23 05:30 | Adelaide Atletico VSC vs South Adelaide FC
- 2026-05-23 05:00 | Adelaide City FC vs FK Beograd
- 2026-05-23 05:30 | Adelaide Comets FC vs Para Hills Knights SC
- 2026-05-23 03:15 | Adelaide Comets Reserves vs Para Hills Knights SC Reserve
- 2026-05-23 05:30 | Adelaide Croatia Raiders SC vs Adelaide Olympic FC
- 2026-05-23 03:15 | Adelaide Croatia Raiders SC Reserve vs Adelaide Olympic FC Reserve
- 2026-05-23 14:00 | FC Aktobe vs FC Kyzylzhar SK

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 527
Valid forward/proxy log rows: 524
Deduped forward/proxy observation rows: 388
Duplicate forward/proxy log rows: 136
Valid automatic proxy observation rows: 524
Deduped automatic proxy observation rows: 388
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-23 | Vonds Ichihara FC vs Shizuoka SSU Bonita | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-15 | Cong An TP Ho Chi Minh City FC vs SHB Da Nang | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-21 | BFC Daugavpils vs Ogre United | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-23 | Canberra Olympic vs Belconnen United | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-19 | Derby Academie vs Onze Createurs | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Al Kahrabaa SC vs Al-Gharraf SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Diyala FC vs Amanat Baghdad SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Deportivo Capiata vs Club Fernando de La Mora | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.056100000000000004
- 2026-05-23 | Clarence Zebras FC vs Kingborough Lions United FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0557
- 2026-05-19 | SV Ried vs Wolfsberger AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-21 | Kifisia vs Larisa | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-23 | Auckland United FC vs East Coast Bays | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-23 | Avondale FC vs Alamein FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
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
### Manukau United FC vs Tauranga City AFC
- Date/time: 2026-05-23 03:00
- League/phase: new-zealand-national-league / automatic_forward_price_proxy
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
- Prediction ID: e3a6bc6f1a50bdc4011c
### Avispa Fukuoka vs Vissel Kobe
- Date/time: 2026-05-23 05:00
- League/phase: japan-jleague / automatic_forward_price_proxy
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
Newly logged paper-test picks: 25
Total logged paper-test rows: 527
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 99, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 42, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 527, 'source_used': 'automatic_forward_value_snapshots'}
- Manukau United FC vs Tauranga City AFC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Avispa Fukuoka vs Vissel Kobe | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Clarence Zebras FC vs Kingborough Lions United FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Croydon FC vs North Eastern Metrostars SC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.1105 | penalty=0.4145 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Croydon Kings FC Reserve vs North Eastern Metrostars SC Reserves | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.1105 | penalty=0.4145 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Canberra Olympic vs Belconnen United | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Davis Legacy vs Almaden FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Canberra White Eagles FC vs O'Connor Knights SC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Canberra White Eagles FC vs O'Connor Knights FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Manukau United FC vs Tauranga City AFC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Auckland City FC vs Melville United AFC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Changwon FC vs Ulsan Citizen FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- South East United FC vs Ulverstone SC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.0821 | penalty=0.308 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Busan Transportation Corporation FC vs Chuncheon FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.7 | prob=0.3488 | EV=0.2906 | edge=0.0785 | penalty=0.2906 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- University of Nsw vs Sydney United 58 FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.3 | prob=0.3772 | EV=0.2448 | edge=0.0742 | penalty=0.2448 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- South East United FC vs Ulverstone SC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Adelaide Atletico Victory Reserves vs South Adelaide Reserve | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.6 | prob=0.3488 | EV=0.2557 | edge=0.071 | penalty=0.2557 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Adelaide Atletico VSC vs South Adelaide FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.6 | prob=0.3488 | EV=0.2557 | edge=0.071 | penalty=0.2557 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
