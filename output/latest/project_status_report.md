# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-20T02:36:39.255077+00:00`
GitHub run: `361` attempt `1`
GitHub SHA: `a333293b3be318f31e60095c796bc09eb7be5ca7`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 6 |  |  |
| Football-Data upcoming odds proxy | True | 15 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 58 |  |  |
| odds-api.io forward fixtures | True | 223 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 246 |  |  |
| Forward price coverage report | True | 234 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 4 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 234 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 7
- Automatic value snapshots: 45
- Positive EV proxy rows: 24
- Proxy observation rows: 12
- Valid forward/proxy log rows: 415
- Deduped forward/proxy log rows: 287
- Duplicate forward/proxy log rows identified: 128
- Fresh API match coverage rate: 0.0
- Matches with fresh API price: 0
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
Current: 45 value snapshots; fresh API coverage rate 0.0.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 287 deduped forward/proxy rows; 128 duplicate raw rows identified.
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
Upcoming fixture rows: 7
Fixture team rows unmatched: 14
Ready for model-fixture join: False
Automatic forward price rows: 15
odds-api.io price rows: 0
Football-Data price rows: 15
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- Anderlecht | suggestion=nan | type=unmatched
- St Truiden | suggestion=nan | type=unmatched
- Atromitos | suggestion=nan | type=unmatched
- Panserraikos | suggestion=nan | type=unmatched
- Gent | suggestion=nan | type=unmatched
- St. Gilloise | suggestion=nan | type=unmatched
- Kifisia | suggestion=nan | type=unmatched
- Larisa | suggestion=nan | type=unmatched
- Mechelen | suggestion=nan | type=unmatched
- Club Brugge | suggestion=nan | type=unmatched
- Panetolikos | suggestion=nan | type=unmatched
- Asteras Tripolis | suggestion=nan | type=unmatched
- Brighton and Hove Albion | suggestion=nan | type=unmatched
- Manchester United | suggestion=nan | type=unmatched
## Interpretation
Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 7
Automatic price rows: 15
Value snapshot rows: 45
Matches with any automatic price: 6
Matches with fresh API price: 0
Matches with odds-api.io price: 0
Fresh API match coverage rate: 0.0
odds-api.io match coverage rate: 0.0
Real-money ready: False
## Match coverage
- 2026-05-21 | Atromitos vs Panserraikos | any=True | fresh_api=False | odds_api_io=False | rows=2 | sources=football_data_average_market_proxy, football_data_max_market_proxy
- 2026-05-21 | Kifisia vs Larisa | any=True | fresh_api=False | odds_api_io=False | rows=2 | sources=football_data_average_market_proxy, football_data_max_market_proxy
- 2026-05-21 | Panetolikos vs Asteras Tripolis | any=True | fresh_api=False | odds_api_io=False | rows=2 | sources=football_data_average_market_proxy, football_data_max_market_proxy
- 2026-05-21 | Anderlecht vs St Truiden | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-21 | Gent vs St. Gilloise | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-21 | Mechelen vs Club Brugge | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-24 | Brighton and Hove Albion vs Manchester United | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
## Source summary
- football_data_average_market_proxy | delayed_market_proxy | rows=6
- football_data_bet365_proxy | delayed_market_proxy | rows=3
- football_data_max_market_proxy | delayed_market_proxy | rows=6

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 7
Proxy price rows: 15
Matched prediction rows: 6
Value snapshot rows: 45
odds-api.io snapshot rows: 0
Baseline snapshot rows: 45
Full model snapshot rows: 0
Positive EV rows: 24
Source counts: {'football_data_max_market_proxy': 18, 'football_data_average_market_proxy': 18, 'football_data_bet365_proxy': 9}
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=6.57 | prob=0.3772 | EV=1.478204 | match=1.0
- 2026-05-21 | Atromitos vs Panserraikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-21 | Atromitos vs Panserraikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=5.28 | prob=0.3488 | EV=0.841664 | match=1.0
- 2026-05-21 | Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=4.6 | prob=0.3772 | EV=0.73512 | match=1.0
- 2026-05-21 | Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=4.5 | prob=0.3772 | EV=0.6974 | match=1.0
- 2026-05-21 | Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=4.32 | prob=0.3772 | EV=0.629504 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=5.25 | prob=0.274 | EV=0.4385 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_average_market_proxy | odds=5.0 | prob=0.274 | EV=0.37 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=4.75 | prob=0.274 | EV=0.3015 | match=1.0
- 2026-05-21 | Kifisia vs Larisa | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=3.2 | prob=0.3488 | EV=0.11616 | match=1.0
- 2026-05-21 | Atromitos vs Panserraikos | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=4.0 | prob=0.274 | EV=0.096 | match=1.0
- 2026-05-21 | Anderlecht vs St Truiden | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=3.1 | prob=0.3488 | EV=0.08128 | match=1.0
- 2026-05-21 | Panetolikos vs Asteras Tripolis | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=3.05 | prob=0.3488 | EV=0.06384 | match=1.0
- 2026-05-21 | Anderlecht vs St Truiden | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=3.0 | prob=0.3488 | EV=0.0464 | match=1.0
- 2026-05-21 | Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=3.8 | prob=0.274 | EV=0.0412 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 45
Pre-dedupe proxy candidate observation rows: 17
Proxy candidate observation rows: 8
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 7
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-21 | Gent vs St. Gilloise | selection=HOME | source=football_data_average_market_proxy | odds=4.32 | prob=0.3772 | EV=0.629504 | edge=0.145719 | penalty=0.6295073893753698 | tier=proxy_watchlist | score=0.1903
- 2026-05-21 | Mechelen vs Club Brugge | selection=DRAW | source=football_data_max_market_proxy | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.083524 | penalty=0.4385014385014385 | tier=suppressed_proxy_watchlist | score=0.1025
- 2026-05-21 | Kifisia vs Larisa | selection=AWAY | source=football_data_max_market_proxy | odds=3.2 | prob=0.3488 | EV=0.11616 | edge=0.0363 | penalty=0.11616000000000004 | tier=suppressed_proxy_watchlist | score=0.0947
- 2026-05-21 | Anderlecht vs St Truiden | selection=AWAY | source=football_data_max_market_proxy | odds=3.1 | prob=0.3488 | EV=0.08128 | edge=0.026219 | penalty=0.08127881059330822 | tier=suppressed_proxy_watchlist | score=0.0932
- 2026-05-21 | Panetolikos vs Asteras Tripolis | selection=AWAY | source=football_data_max_market_proxy | odds=3.05 | prob=0.3488 | EV=0.06384 | edge=0.020931 | penalty=0.06383952127221537 | tier=suppressed_proxy_watchlist | score=0.0924
- 2026-05-21 | Atromitos vs Panserraikos | selection=DRAW | source=football_data_max_market_proxy | odds=4.0 | prob=0.274 | EV=0.096 | edge=0.024 | penalty=0.09600000000000009 | tier=suppressed_proxy_watchlist | score=0.0908
- 2026-05-21 | Gent vs St. Gilloise | selection=DRAW | source=football_data_max_market_proxy | odds=3.8 | prob=0.274 | EV=0.0412 | edge=0.010842 | penalty=0.041199583520166616 | tier=suppressed_proxy_watchlist | score=0.0886
- 2026-05-21 | Anderlecht vs St Truiden | selection=DRAW | source=football_data_bet365_proxy | odds=3.75 | prob=0.274 | EV=0.0275 | edge=0.007333 | penalty=0.027498715626605552 | tier=suppressed_proxy_watchlist | score=0.0881

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 8
Explained rows: 8
Distinct blockers: 6
Top blocker: delayed_football_data_proxy_not_fresh_api_price
Real-money ready: False
## Blocker summary
- delayed_football_data_proxy_not_fresh_api_price: 8
- probability_or_league_rule_suppressed: 7
- low_probability_band_under_0_35: 7
- ev_above_real_candidate_cap_possible_overconfidence: 2
- market_alignment_penalty_too_high_for_real_candidate: 2
- edge_below_candidate_threshold: 2
## Row explanations
- 2026-05-21 | Gent vs St. Gilloise | sel=HOME | score=0.1903 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Mechelen vs Club Brugge | sel=DRAW | score=0.1025 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Kifisia vs Larisa | sel=AWAY | score=0.0947 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Anderlecht vs St Truiden | sel=AWAY | score=0.0932 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Panetolikos vs Asteras Tripolis | sel=AWAY | score=0.0924 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Atromitos vs Panserraikos | sel=DRAW | score=0.0908 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Gent vs St. Gilloise | sel=DRAW | score=0.0886 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Anderlecht vs St Truiden | sel=DRAW | score=0.0881 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 45
Paper proxy observation rows: 12
Positive EV value rows: 24
Suppressed-band observation rows: 0
Distinct matches: 6
Distinct sources: 0
Max EV: 0.73512
Average EV: 0.226015
Max probability edge: 0.159809
Average match confidence: None
## By selection
- away: rows=6, avg_ev=0.0598, max_ev=0.1162
- draw: rows=4, avg_ev=0.2303, max_ev=0.4385
- home: rows=2, avg_ev=0.7163, max_ev=0.7351

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 7
Forward fixture prediction rows: 7
Full model prediction rows: 0
Baseline prediction rows: 7
Max forward predictions: 300
Ready for price join: True
- 2026-05-21 16:00 | Atromitos vs Panserraikos | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 17:00 | Kifisia vs Larisa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 19:30 | Anderlecht vs St Truiden | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 19:30 | Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 19:30 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 15:00:00 | Brighton and Hove Albion vs Manchester United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 7
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
Upcoming fixtures: 7
Manual template rows: 7
Rows with complete manual odds: 0
Rows missing manual odds: 7
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-21 19:30 | Anderlecht vs St Truiden
- 2026-05-21 16:00 | Atromitos vs Panserraikos
- 2026-05-21 19:30 | Gent vs St. Gilloise
- 2026-05-21 17:00 | Kifisia vs Larisa
- 2026-05-21 19:30 | Mechelen vs Club Brugge
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis
- 2026-05-24 15:00:00 | Brighton and Hove Albion vs Manchester United

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 7
Source counts: {'football_data_fixtures_proxy': 6, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-21 19:30 | Anderlecht vs St Truiden | B1 | football_data_fixtures_proxy
- 2026-05-21 16:00 | Atromitos vs Panserraikos | G1 | football_data_fixtures_proxy
- 2026-05-21 19:30 | Gent vs St. Gilloise | B1 | football_data_fixtures_proxy
- 2026-05-21 17:00 | Kifisia vs Larisa | G1 | football_data_fixtures_proxy
- 2026-05-21 19:30 | Mechelen vs Club Brugge | B1 | football_data_fixtures_proxy
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis | G1 | football_data_fixtures_proxy
- 2026-05-24 15:00:00 | Brighton and Hove Albion vs Manchester United | premier_league | thesportsdb_eventsnextleague

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 7
Rows with complete odds: 0
- 2026-05-21 19:30 | Anderlecht vs St Truiden | bookmaker=bet365_manual
- 2026-05-21 16:00 | Atromitos vs Panserraikos | bookmaker=bet365_manual
- 2026-05-21 19:30 | Gent vs St. Gilloise | bookmaker=bet365_manual
- 2026-05-21 17:00 | Kifisia vs Larisa | bookmaker=bet365_manual
- 2026-05-21 19:30 | Mechelen vs Club Brugge | bookmaker=bet365_manual
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis | bookmaker=bet365_manual
- 2026-05-24 15:00:00 | Brighton and Hove Albion vs Manchester United | bookmaker=bet365_manual

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
- 2026-05-21 19:30 | Anderlecht vs St Truiden
- 2026-05-21 16:00 | Atromitos vs Panserraikos
- 2026-05-21 19:30 | Gent vs St. Gilloise
- 2026-05-21 17:00 | Kifisia vs Larisa
- 2026-05-21 19:30 | Mechelen vs Club Brugge
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis
- 2026-05-24 15:00:00 | Brighton and Hove Albion vs Manchester United
## After filling odds
Run the workflow again. Expected result:
- `manual_forward_snapshots` becomes greater than 0
- `paper_test_picks` may become greater than 0
- `candidate_bets` may still remain 0, which is acceptable

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 418
Valid forward/proxy log rows: 415
Deduped forward/proxy observation rows: 287
Duplicate forward/proxy log rows: 128
Valid automatic proxy observation rows: 415
Deduped automatic proxy observation rows: 287
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
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
- 2026-05-21 | Kifisia vs Larisa | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553
- 2026-05-21 | Anderlecht vs St Truiden | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0546
- 2026-05-21 | Panetolikos vs Asteras Tripolis | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054
- 2026-05-21 | Atromitos vs Panserraikos | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0533

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
### Gent vs St. Gilloise
- Date/time: 2026-05-21 19:30
- League/phase: B1 / automatic_forward_price_proxy
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
- Prediction ID: 0feb27e53c2d790d6c02
### Gent vs St. Gilloise
- Date/time: 2026-05-21 19:30
- League/phase: B1 / automatic_forward_price_proxy
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
Current paper-test picks: 12
Newly logged paper-test picks: 8
Total logged paper-test rows: 418
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 45, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 21, 'current_paper_picks': 12, 'newly_logged_picks': 8, 'total_logged_paper_rows': 418, 'source_used': 'automatic_forward_value_snapshots'}
- Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kifisia vs Larisa | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.2 | prob=0.3488 | EV=0.1162 | edge=0.0363 | penalty=0.1162 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Anderlecht vs St Truiden | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.1 | prob=0.3488 | EV=0.0813 | edge=0.0262 | penalty=0.0813 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Panetolikos vs Asteras Tripolis | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.05 | prob=0.3488 | EV=0.0638 | edge=0.0209 | penalty=0.0638 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Anderlecht vs St Truiden | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.0 | prob=0.3488 | EV=0.0464 | edge=0.0155 | penalty=0.0464 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Atromitos vs Panserraikos | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.0 | prob=0.274 | EV=0.096 | edge=0.024 | penalty=0.096 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kifisia vs Larisa | coverage=baseline_unmatched_fixture | selection=AWAY | odds=2.98 | prob=0.3488 | EV=0.0394 | edge=0.0132 | penalty=0.0394 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Panetolikos vs Asteras Tripolis | coverage=baseline_unmatched_fixture | selection=AWAY | odds=2.9 | prob=0.3488 | EV=0.0115 | edge=0.004 | penalty=0.0115 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Atromitos vs Panserraikos | coverage=baseline_unmatched_fixture | selection=DRAW | odds=3.71 | prob=0.274 | EV=0.0165 | edge=0.0045 | penalty=0.0165 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
