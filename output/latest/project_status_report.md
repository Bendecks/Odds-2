# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-14T13:52:53.021616+00:00`
GitHub run: `347` attempt `1`
GitHub SHA: `aaf28b36139e663f474d0a591d17d01c12b19a08`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 3 |  |  |
| Football-Data upcoming odds proxy | True | 9 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 55 |  |  |
| odds-api.io forward fixtures | True | 328 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 228 |  |  |
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
- Forward fixture predictions: 255
- Automatic value snapshots: 201
- Positive EV proxy rows: 100
- Proxy observation rows: 25
- Valid forward/proxy log rows: 180
- Deduped forward/proxy log rows: 116
- Duplicate forward/proxy log rows identified: 64
- Fresh API match coverage rate: 0.1961
- Matches with fresh API price: 50
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
Current: 201 value snapshots; fresh API coverage rate 0.1961.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 116 deduped forward/proxy rows; 64 duplicate raw rows identified.
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
Upcoming fixture rows: 255
Fixture team rows unmatched: 500
Ready for model-fixture join: False
Automatic forward price rows: 59
odds-api.io price rows: 50
Football-Data price rows: 9
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AC Goianiense GO | suggestion=nan | type=unmatched
- CA Paranaense PR | suggestion=nan | type=unmatched
- AD Confianca SE | suggestion=nan | type=unmatched
- Gremio FB Porto Alegrense RS | suggestion=nan | type=unmatched
- Astillero FC (Ecu) | suggestion=nan | type=unmatched
- Guayaquil City FC | suggestion=nan | type=unmatched
- Chapecoense SC | suggestion=nan | type=unmatched
- Botafogo FR RJ | suggestion=nan | type=unmatched
- Club 3 De Noviembre | suggestion=nan | type=unmatched
- Deportivo Capiata | suggestion=nan | type=unmatched
- Club Fernando de La Mora | suggestion=nan | type=unmatched
- Independiente Campo Grande | suggestion=nan | type=unmatched
- CR Brasil AL | suggestion=nan | type=unmatched
- Fortaleza EC CE | suggestion=nan | type=unmatched
- Libertad Asuncion | suggestion=nan | type=unmatched
- CS 2 de Mayo | suggestion=nan | type=unmatched
- Oviedo | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 255
Automatic price rows: 59
Value snapshot rows: 201
Matches with any automatic price: 53
Matches with fresh API price: 50
Matches with odds-api.io price: 50
Fresh API match coverage rate: 0.1961
odds-api.io match coverage rate: 0.1961
Real-money ready: False
## Match coverage
- 2026-05-14 | Valencia vs Vallecano | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-14 | Girona vs Sociedad | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-14 | Real Madrid vs Real Oviedo | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Astillero FC (Ecu) vs Guayaquil City FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Club 3 De Noviembre vs Deportivo Capiata | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Libertad Asuncion vs CS 2 de Mayo | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Real Madrid vs Oviedo | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-14 | Red Bull Bragantino SP vs SC Corinthians SP | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Chapecoense SC vs Botafogo FR RJ | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | AC Goianiense GO vs CA Paranaense PR | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | AD Confianca SE vs Gremio FB Porto Alegrense RS | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Tigres FC vs Envigado FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Club Fernando de La Mora vs Independiente Campo Grande | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | Santos FC SP vs SE Palmeiras SP | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | SC Corinthians SP vs Barra FC SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-14 | CR Brasil AL vs Fortaleza EC CE | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 255
Proxy price rows: 59
Matched prediction rows: 55
Value snapshot rows: 201
odds-api.io snapshot rows: 165
Baseline snapshot rows: 183
Full model snapshot rows: 18
Positive EV rows: 100
Source counts: {'odds_api_io_Bet365_ML': 165, 'football_data_bet365_proxy': 12, 'football_data_max_market_proxy': 12, 'football_data_average_market_proxy': 12}
- 2026-05-15 | Bentleigh Greens SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=1.0
- 2026-05-15 | Bentleigh Greens vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=0.96
- 2026-05-15 | Bentleigh Greens vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.274 | EV=4.754 | match=0.96
- 2026-05-15 | Bentleigh Greens SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.274 | EV=4.754 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=0.96
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3488 | EV=2.3136 | match=0.96
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-14 | SC Corinthians SP vs Barra FC SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-15 | Semen Padang FC vs Persebaya Surabaya | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-15 | Brisbane Roar FC vs Lions FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-15 | Shenzhen 2028 FC vs Shaanxi Union FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3772 | EV=1.2632 | match=1.0
- 2026-05-14 | Red Bull Bragantino SP vs SC Corinthians SP | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3772 | EV=1.1689 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 201
Pre-dedupe proxy candidate observation rows: 69
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-15 | Myj-Gmsc vs FC Bengaluru United | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-15 | Werribee City FC vs Malvern City FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-15 | CF Monterrey vs Club America | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-15 | Hangzhou Linping Wuyue vs Foshan Nanshi FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-14 | AC Goianiense GO vs CA Paranaense PR | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-14 | Chapecoense SC vs Botafogo FR RJ | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-15 | Municipal Limeno vs CD FAS Santa Ana | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-15 | Wynnum Wolves FC vs Eastern Suburbs FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-15 | Central Coast United FC vs Inner West Hawks FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-15 | Kingston City FC vs Eastern Lions SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-14 | Astillero FC (Ecu) vs Guayaquil City FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-05-15 | Mekelle 70 Enderta FC vs Ethiopian Medhin | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 3
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 9
- ev_above_real_candidate_cap_possible_overconfidence: 8
- watchlist_only_pending_forward_settlement: 3
## Row explanations
- 2026-05-15 | Myj-Gmsc vs FC Bengaluru United | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Werribee City FC vs Malvern City FC | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | CF Monterrey vs Club America | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Hangzhou Linping Wuyue vs Foshan Nanshi FC | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | AC Goianiense GO vs CA Paranaense PR | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-14 | Chapecoense SC vs Botafogo FR RJ | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Municipal Limeno vs CD FAS Santa Ana | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-15 | Wynnum Wolves FC vs Eastern Suburbs FC | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-15 | Central Coast United FC vs Inner West Hawks FC | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-15 | Kingston City FC vs Eastern Lions SC | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-14 | Astillero FC (Ecu) vs Guayaquil City FC | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-15 | Mekelle 70 Enderta FC vs Ethiopian Medhin | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 201
Paper proxy observation rows: 25
Positive EV value rows: 100
Suppressed-band observation rows: 0
Distinct matches: 21
Distinct sources: 0
Max EV: 0.72072
Average EV: 0.452871
Max probability edge: 0.154978
Average match confidence: None
## By selection
- away: rows=8, avg_ev=0.2343, max_ev=0.5113
- draw: rows=5, avg_ev=0.6747, max_ev=0.7207
- home: rows=12, avg_ev=0.5062, max_ev=0.6974

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 255
Forward fixture prediction rows: 255
Full model prediction rows: 3
Baseline prediction rows: 252
Max forward predictions: 300
Ready for price join: True
- 2026-05-14 18:00 | Valencia vs Vallecano | coverage=full_team_strength_match | H=0.3922 D=0.2863 A=0.3215 | fair=2.55/3.49/3.11
- 2026-05-14 19:00 | Girona vs Sociedad | coverage=full_team_strength_match | H=0.3982 D=0.2712 A=0.3305 | fair=2.51/3.69/3.03
- 2026-05-14 19:30 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 20:00 | Astillero FC (Ecu) vs Guayaquil City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 20:00 | Club 3 De Noviembre vs Deportivo Capiata | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 20:00 | Libertad Asuncion vs CS 2 de Mayo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 20:30 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 20:30 | Red Bull Bragantino SP vs SC Corinthians SP | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 20:30 | Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 21:00 | Chapecoense SC vs Botafogo FR RJ | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 22:00 | AC Goianiense GO vs CA Paranaense PR | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 22:00 | AD Confianca SE vs Gremio FB Porto Alegrense RS | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 22:00 | Tigres FC vs Envigado FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 22:30 | Club Fernando de La Mora vs Independiente Campo Grande | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 22:30 | Santos FC SP vs SE Palmeiras SP | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 22:30 | SC Corinthians SP vs Barra FC SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-14 23:00 | CR Brasil AL vs Fortaleza EC CE | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 00:00 | Oriente Petrolero vs Guabira Montero | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 00:30 | EC Vitoria BA vs CR Flamengo RJ | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 00:45 | Deportes Quindio vs Internacional FC De Palmira | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-15 01:00 | CF Pachuca vs Pumas UNAM | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 255
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 829
Log type: probability_only_no_market_prices
- 2026-05-15 2026-05-14 14:30:00 | FC Bishkek City vs FC Kyrgyzaltyn | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 16:00:00 | AL Budaiya vs Al-Ahli SC Manama | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 16:00:00 | Al Hidd vs Al-Shabab | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 16:00:00 | Al Riffa vs AL Bahrain | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 16:45:00 | Al Wasl FC vs Ittihad Kalba FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 18:00:00 | Carlos Renaux SC vs Figueirense FC SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:00:00 | Crusaders Strikers FC vs Cliftonville LFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:00:00 | SE Palmeiras SP vs EC Vitoria BA | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 19:00:00 | Aston Villa vs Liverpool | H=0.36910000000000004 D=0.26680000000000004 A=0.364
- 2026-05-15 2026-05-14 20:00:00 | CA Bucaramanga Sa vs International FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 20:00:00 | Deportivo Santani vs Tacuary Asuncion | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 20:00:00 | Fortaleza FC vs Millonarios FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 20:30:00 | Llaneros FC vs Asociacion Deportivo Cali | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 21:45:00 | CD Genesis PN vs Olancho FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 22:30:00 | 12 de Junio de Villa Hayes vs Club Dr Benjamin Aceval | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 23:00:00 | Club Comunicaciones vs Argentino de Quilmes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-14 23:00:00 | G3X FC vs Fluxo FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-14 13:00:00 | Jitex Molndal BK vs Trelleborgs FF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-14 13:00:00 | NSI Runavik II vs HB Torshavn II | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-14 13:30:00 | FC St. Pauli vs VFL Wolfsburg | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 255
Manual template rows: 255
Rows with complete manual odds: 0
Rows missing manual odds: 255
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
- 2026-05-14 20:00 | Astillero FC (Ecu) vs Guayaquil City FC
- 2026-05-14 21:00 | Chapecoense SC vs Botafogo FR RJ
- 2026-05-14 20:00 | Club 3 De Noviembre vs Deportivo Capiata
- 2026-05-14 22:30 | Club Fernando de La Mora vs Independiente Campo Grande
- 2026-05-14 23:00 | CR Brasil AL vs Fortaleza EC CE
- 2026-05-14 19:00 | Girona vs Sociedad
- 2026-05-14 20:00 | Libertad Asuncion vs CS 2 de Mayo
- 2026-05-14 20:30 | Real Madrid vs Oviedo
- 2026-05-14 19:30 | Real Madrid vs Real Oviedo
- 2026-05-14 20:30 | Red Bull Bragantino SP vs SC Corinthians SP
- 2026-05-14 22:30 | Santos FC SP vs SE Palmeiras SP
- 2026-05-14 22:30 | SC Corinthians SP vs Barra FC SC
- 2026-05-14 22:00 | Tigres FC vs Envigado FC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 255
Source counts: {'odds_api_io_events_bookmaker_filtered': 248, 'football_data_fixtures_proxy': 3, 'odds_api_io_events_search': 3, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-14 22:00 | AC Goianiense GO vs CA Paranaense PR | brazil-copa-do-brasil | odds_api_io_events_bookmaker_filtered
- 2026-05-14 22:00 | AD Confianca SE vs Gremio FB Porto Alegrense RS | brazil-copa-do-brasil | odds_api_io_events_bookmaker_filtered
- 2026-05-14 20:00 | Astillero FC (Ecu) vs Guayaquil City FC | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-05-14 21:00 | Chapecoense SC vs Botafogo FR RJ | brazil-copa-do-brasil | odds_api_io_events_bookmaker_filtered
- 2026-05-14 20:00 | Club 3 De Noviembre vs Deportivo Capiata | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-14 22:30 | Club Fernando de La Mora vs Independiente Campo Grande | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-14 23:00 | CR Brasil AL vs Fortaleza EC CE | brazil-copa-do-brasil | odds_api_io_events_bookmaker_filtered
- 2026-05-14 19:00 | Girona vs Sociedad | la_liga | football_data_fixtures_proxy
- 2026-05-14 20:00 | Libertad Asuncion vs CS 2 de Mayo | paraguay-division-de-honor-apertura | odds_api_io_events_bookmaker_filtered
- 2026-05-14 20:30 | Real Madrid vs Oviedo | la_liga | football_data_fixtures_proxy
- 2026-05-14 19:30 | Real Madrid vs Real Oviedo | spain-laliga | odds_api_io_events_bookmaker_filtered
- 2026-05-14 20:30 | Red Bull Bragantino SP vs SC Corinthians SP | brazil-paulista-women | odds_api_io_events_bookmaker_filtered
- 2026-05-14 22:30 | Santos FC SP vs SE Palmeiras SP | brazil-paulista-women | odds_api_io_events_bookmaker_filtered
- 2026-05-14 22:30 | SC Corinthians SP vs Barra FC SC | brazil-copa-do-brasil | odds_api_io_events_bookmaker_filtered
- 2026-05-14 22:00 | Tigres FC vs Envigado FC | colombia-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-14 18:00 | Valencia vs Vallecano | la_liga | football_data_fixtures_proxy
- 2026-05-14 20:30 | Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | ecuador-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-15 22:30 | 12 de Junio de Villa Hayes vs Club Dr Benjamin Aceval | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-15 16:00 | Aalesunds FK vs Hoenefoss BK | norway-toppserien-women | odds_api_io_events_bookmaker_filtered
- 2026-05-15 18:15 | FC Aarau vs Yverdon-Sport | switzerland-challenge-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 17:30 | ACS Champions FC Arges vs Rapid Bucuresti 1923 | romania-superliga | odds_api_io_events_bookmaker_filtered
- 2026-05-15 09:35 | Adelaide United FC vs Auckland FC | australia-a-league | odds_api_io_events_bookmaker_filtered
- 2026-05-15 14:10 | Ajman Club vs Al-Nasr Dubai CSC | united-arab-emirates-arabian-gulf-league | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 255
Rows with complete odds: 0
- 2026-05-14 22:00 | AC Goianiense GO vs CA Paranaense PR | bookmaker=bet365_manual
- 2026-05-14 22:00 | AD Confianca SE vs Gremio FB Porto Alegrense RS | bookmaker=bet365_manual
- 2026-05-14 20:00 | Astillero FC (Ecu) vs Guayaquil City FC | bookmaker=bet365_manual
- 2026-05-14 21:00 | Chapecoense SC vs Botafogo FR RJ | bookmaker=bet365_manual
- 2026-05-14 20:00 | Club 3 De Noviembre vs Deportivo Capiata | bookmaker=bet365_manual
- 2026-05-14 22:30 | Club Fernando de La Mora vs Independiente Campo Grande | bookmaker=bet365_manual
- 2026-05-14 23:00 | CR Brasil AL vs Fortaleza EC CE | bookmaker=bet365_manual
- 2026-05-14 19:00 | Girona vs Sociedad | bookmaker=bet365_manual
- 2026-05-14 20:00 | Libertad Asuncion vs CS 2 de Mayo | bookmaker=bet365_manual
- 2026-05-14 20:30 | Real Madrid vs Oviedo | bookmaker=bet365_manual
- 2026-05-14 19:30 | Real Madrid vs Real Oviedo | bookmaker=bet365_manual
- 2026-05-14 20:30 | Red Bull Bragantino SP vs SC Corinthians SP | bookmaker=bet365_manual
- 2026-05-14 22:30 | Santos FC SP vs SE Palmeiras SP | bookmaker=bet365_manual
- 2026-05-14 22:30 | SC Corinthians SP vs Barra FC SC | bookmaker=bet365_manual
- 2026-05-14 22:00 | Tigres FC vs Envigado FC | bookmaker=bet365_manual
- 2026-05-14 18:00 | Valencia vs Vallecano | bookmaker=bet365_manual
- 2026-05-14 20:30 | Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | bookmaker=bet365_manual
- 2026-05-15 22:30 | 12 de Junio de Villa Hayes vs Club Dr Benjamin Aceval | bookmaker=bet365_manual
- 2026-05-15 16:00 | Aalesunds FK vs Hoenefoss BK | bookmaker=bet365_manual
- 2026-05-15 18:15 | FC Aarau vs Yverdon-Sport | bookmaker=bet365_manual
- 2026-05-15 17:30 | ACS Champions FC Arges vs Rapid Bucuresti 1923 | bookmaker=bet365_manual
- 2026-05-15 09:35 | Adelaide United FC vs Auckland FC | bookmaker=bet365_manual
- 2026-05-15 14:10 | Ajman Club vs Al-Nasr Dubai CSC | bookmaker=bet365_manual
- 2026-05-15 16:00 | Akritas Chlorakas vs AEL Limassol | bookmaker=bet365_manual

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
- 2026-05-14 20:00 | Astillero FC (Ecu) vs Guayaquil City FC
- 2026-05-14 21:00 | Chapecoense SC vs Botafogo FR RJ
- 2026-05-14 20:00 | Club 3 De Noviembre vs Deportivo Capiata
- 2026-05-14 22:30 | Club Fernando de La Mora vs Independiente Campo Grande
- 2026-05-14 23:00 | CR Brasil AL vs Fortaleza EC CE
- 2026-05-14 19:00 | Girona vs Sociedad
- 2026-05-14 20:00 | Libertad Asuncion vs CS 2 de Mayo
- 2026-05-14 20:30 | Real Madrid vs Oviedo
- 2026-05-14 19:30 | Real Madrid vs Real Oviedo
- 2026-05-14 20:30 | Red Bull Bragantino SP vs SC Corinthians SP
- 2026-05-14 22:30 | Santos FC SP vs SE Palmeiras SP
- 2026-05-14 22:30 | SC Corinthians SP vs Barra FC SC
- 2026-05-14 22:00 | Tigres FC vs Envigado FC
- 2026-05-14 18:00 | Valencia vs Vallecano
- 2026-05-14 20:30 | Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors
- 2026-05-15 22:30 | 12 de Junio de Villa Hayes vs Club Dr Benjamin Aceval
- 2026-05-15 16:00 | Aalesunds FK vs Hoenefoss BK

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 183
Valid forward/proxy log rows: 180
Deduped forward/proxy observation rows: 116
Duplicate forward/proxy log rows: 64
Valid automatic proxy observation rows: 180
Deduped automatic proxy observation rows: 116
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-14 | FC Salzburg Frauen vs FK Austria Wien | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0631
- 2026-05-14 | SV Wildon vs SC Stadtwerke Bruck/Mur | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0631
- 2026-05-14 | SC Corinthians SP vs Barra FC SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0631
- 2026-05-14 | Neroca FC vs Sudeva Delhi FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0623
- 2026-05-14 | Raelingen vs Brumunddal Fotball | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0623
- 2026-05-14 | First Vienna FC 1894 vs Schwarz-Weiss Bregenz | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0623
- 2026-05-14 | IF Karlstad Fotbol vs IFK Stocksund | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0616
- 2026-05-14 | FC Sion vs FC Lugano | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0614
- 2026-05-14 | Libertad Asuncion vs CS 2 de Mayo | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0614
- 2026-05-14 | Shire Endaselassie FC vs Ethiopian Coffee SC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-14 | Sanat Mes Kerman FC vs Mes Shahr-e Babak | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-14 | Mjallby AIF vs Hammarby IF | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-15 | CF Monterrey vs Club America | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-15 | Hangzhou Linping Wuyue vs Foshan Nanshi FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061200000000000004
- 2026-05-14 | Viking FK 2 vs Akra | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-14 | Herentals FC vs Dynamos Harare FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Trelleborgs FF vs Jonkopings Sodra IF | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Vinotinto FC Ecuador vs Club Deportivo Cuenca Juniors | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
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
Newly logged paper-test picks: 19
Total logged paper-test rows: 183
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 201, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 85, 'current_paper_picks': 25, 'newly_logged_picks': 19, 'total_logged_paper_rows': 183, 'source_used': 'automatic_forward_value_snapshots'}
- Girona vs Sociedad | coverage=full_team_strength_match | selection=AWAY | odds=3.35 | prob=0.3305 | EV=0.1072 | edge=0.032 | penalty=0.1072 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Girona vs Sociedad | coverage=full_team_strength_match | selection=AWAY | odds=3.3 | prob=0.3305 | EV=0.0906 | edge=0.0275 | penalty=0.0907 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Valencia vs Vallecano | coverage=full_team_strength_match | selection=AWAY | odds=3.4 | prob=0.3215 | EV=0.0931 | edge=0.0274 | penalty=0.0931 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Valencia vs Vallecano | coverage=full_team_strength_match | selection=AWAY | odds=3.3 | prob=0.3215 | EV=0.0609 | edge=0.0185 | penalty=0.061 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Santos FC SP vs SE Palmeiras SP | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mekelle 70 Enderta FC vs Ethiopian Medhin | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Astillero FC (Ecu) vs Guayaquil City FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Tigres FC vs Envigado FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.2 | prob=0.3772 | EV=0.5842 | edge=0.1391 | penalty=0.5842 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AD Confianca SE vs Gremio FB Porto Alegrense RS | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.1 | prob=0.3772 | EV=0.5465 | edge=0.1333 | penalty=0.5465 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PVF Cand B vs Ho Chi Minh City FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.1 | prob=0.3772 | EV=0.5465 | edge=0.1333 | penalty=0.5465 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.28 | prob=0.274 | EV=0.7207 | edge=0.1148 | penalty=0.7207 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.28 | prob=0.274 | EV=0.7207 | edge=0.1148 | penalty=0.7207 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Curtin University SC vs Murdoch University Melville FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- EC Vitoria BA vs CR Flamengo RJ | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Essendon Royals SC vs Moreland City FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Myj-Gmsc vs FC Bengaluru United | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.8 | prob=0.3772 | EV=0.4334 | edge=0.114 | penalty=0.4334 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
