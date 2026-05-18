# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-18T02:37:26.725165+00:00`
GitHub run: `357` attempt `1`
GitHub SHA: `d3c8545bcde4fd7a43e76db53e2d97a030b6423a`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 2 |  |  |
| Football-Data upcoming odds proxy | True | 6 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 51 |  |  |
| odds-api.io forward fixtures | True | 125 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 183 |  |  |
| Forward price coverage report | True | 101 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 3 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 101 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 198
- Automatic value snapshots: 189
- Positive EV proxy rows: 84
- Proxy observation rows: 25
- Valid forward/proxy log rows: 336
- Deduped forward/proxy log rows: 225
- Duplicate forward/proxy log rows identified: 111
- Fresh API match coverage rate: 0.2576
- Matches with fresh API price: 51
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
Current: 189 value snapshots; fresh API coverage rate 0.2576.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 225 deduped forward/proxy rows; 111 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 112
Upcoming fixture rows: 2
Proxy price rows: 6
Sources attempted: 1
Errors: 0
- 2026-05-18 20:00 | Arsenal vs Burnley | football_data_bet365_proxy | 1.09/11.0/23.0
- 2026-05-18 20:00 | Arsenal vs Burnley | football_data_max_market_proxy | 1.11/11.0/26.0
- 2026-05-18 20:00 | Arsenal vs Burnley | football_data_average_market_proxy | 1.08/10.12/22.13
- 2026-05-18 19:30 | Leganes vs Huesca | football_data_bet365_proxy | 2.01/3.5/3.5
- 2026-05-18 19:30 | Leganes vs Huesca | football_data_max_market_proxy | 2.05/3.5/4.0
- 2026-05-18 19:30 | Leganes vs Huesca | football_data_average_market_proxy | 1.95/3.29/3.57

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 198
Fixture team rows unmatched: 390
Ready for model-fixture join: False
Automatic forward price rows: 57
odds-api.io price rows: 51
Football-Data price rows: 6
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AFC Eskilstuna | suggestion=nan | type=unmatched
- FC Arlanda | suggestion=nan | type=unmatched
- AFC Hermannstadt | suggestion=nan | type=unmatched
- Fotbal Club FCSB | suggestion=nan | type=unmatched
- AA Ponte Preta SP | suggestion=nan | type=unmatched
- Londrina EC PR | suggestion=nan | type=unmatched
- FC Aarau | suggestion=nan | type=unmatched
- Grasshopper Club Zurich | suggestion=nan | type=unmatched
- AB Argir | suggestion=nan | type=unmatched
- Vikingur Gota | suggestion=nan | type=unmatched
- AD Confianca SE | suggestion=nan | type=unmatched
- Maranhao AC MA | suggestion=nan | type=unmatched
- AL Draih | suggestion=nan | type=unmatched
- Al-Jabalain | suggestion=nan | type=unmatched
- Al Mokawloon Al Arab | suggestion=nan | type=unmatched
- Wadi Degla SC | suggestion=nan | type=unmatched
- AL Nasr SC (OMA) | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 198
Automatic price rows: 57
Value snapshot rows: 189
Matches with any automatic price: 53
Matches with fresh API price: 51
Matches with odds-api.io price: 51
Fresh API match coverage rate: 0.2576
odds-api.io match coverage rate: 0.2576
Real-money ready: False
## Match coverage
- 2026-05-18 | Club Deportivo Magallanes vs Deportes Recoleta | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | AL Nasr SC (OMA) vs Samail SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Al Shabab vs Al-Seeb | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Al-Khaboora vs Al-Rustaq | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Bahla Club vs Al Nahda | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Ibri vs Dhofar SCSC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Oman Club vs Sur SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Sohar vs Saham | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | FC Haka Valkeakoski vs HJK Klubi 04 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | NK Samobor vs GNK Dinamo Zagreb | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-18 | SJK Akatemia/2 vs VPS Akatemia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Puszcza Niepolomice vs LKS Lodz | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Universidad de Concepcion vs Colo Colo | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | AL Draih vs Al-Jabalain | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Kuwait SC vs Al Arabi | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | Falcons FC vs Bst Galaxy | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-18 | FC Lokomotiv 1929 Sofia vs PFC Slavia Sofia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 198
Proxy price rows: 57
Matched prediction rows: 55
Value snapshot rows: 189
odds-api.io snapshot rows: 162
Baseline snapshot rows: 180
Full model snapshot rows: 9
Positive EV rows: 84
Source counts: {'odds_api_io_Bet365_ML': 162, 'football_data_bet365_proxy': 9, 'football_data_max_market_proxy': 9, 'football_data_average_market_proxy': 9}
- 2026-05-18 | Universidad de Concepcion vs Colo Colo | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=81.0 | prob=0.3772 | EV=29.5532 | match=1.0
- 2026-05-18 | Universidad de Concepcion vs Colo Colo | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=26.0 | prob=0.274 | EV=6.124 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=26.0 | prob=0.2712 | EV=6.0512 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=23.0 | prob=0.2712 | EV=5.2376 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=22.13 | prob=0.2712 | EV=5.001656 | match=1.0
- 2026-05-18 | PFC Montana 1921 vs FK Spartak 1918 Varna | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3772 | EV=2.5834 | match=1.0
- 2026-05-18 | FC Farul Constanta vs Metaloglobus Bucuresti | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=DRAW | src=football_data_max_market_proxy | odds=11.0 | prob=0.2596 | EV=1.8556 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=DRAW | src=football_data_bet365_proxy | odds=11.0 | prob=0.2596 | EV=1.8556 | match=1.0
- 2026-05-18 | HB Torshavn vs Eb/Streymur | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=DRAW | src=football_data_average_market_proxy | odds=10.12 | prob=0.2596 | EV=1.627152 | match=1.0
- 2026-05-18 | FC Petrolul Ploiesti vs ASC Otelul Galati | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-18 | FC Haka Valkeakoski vs HJK Klubi 04 | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-20 | PFC Lokomotiv Plovdiv vs PFC CSKA Sofia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=0.6923
- 2026-05-18 | Throttur Reykjavik vs Leiknir Reykjavik | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=0.7835
- 2026-05-18 | Fylkir Reykjavik vs IR Reykjavik | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-18 | FC Lokomotiv 1929 Sofia vs PFC Slavia Sofia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 189
Pre-dedupe proxy candidate observation rows: 59
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 1
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-18 | GIF Sundsvall vs Landskrona BoIS | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-18 | Bahla Club vs Al Nahda | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-18 | Ghazl El Mahallah vs Al Ittihad Al Sakandary | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-18 | Al Shabab vs Al-Seeb | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-18 | Ibri vs Dhofar SCSC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-18 | Puszcza Niepolomice vs LKS Lodz | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-18 | SJK Akatemia/2 vs VPS Akatemia | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-18 | Waterford FC vs Drogheda United FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-18 | AB Argir vs Vikingur Gota | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-05-18 | Laholms FK vs FC Rosengaard 1917 | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145
- 2026-05-18 | Orgryte IS vs IFK Goteborg | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3772 | EV=0.47108 | edge=0.12079 | penalty=0.4710814710814708 | tier=proxy_watchlist | score=0.212
- 2026-05-18 | CS Italiano vs CSCD Laferrere | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123

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
- ev_above_real_candidate_cap_possible_overconfidence: 7
- watchlist_only_pending_forward_settlement: 1
- edge_below_candidate_threshold: 1
- probability_or_league_rule_suppressed: 1
- low_probability_band_under_0_35: 1
## Row explanations
- 2026-05-18 | GIF Sundsvall vs Landskrona BoIS | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Bahla Club vs Al Nahda | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Ghazl El Mahallah vs Al Ittihad Al Sakandary | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Al Shabab vs Al-Seeb | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-18 | Ibri vs Dhofar SCSC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-18 | Puszcza Niepolomice vs LKS Lodz | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-18 | SJK Akatemia/2 vs VPS Akatemia | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-18 | Waterford FC vs Drogheda United FC | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-18 | AB Argir vs Vikingur Gota | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Laholms FK vs FC Rosengaard 1917 | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Orgryte IS vs IFK Goteborg | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | CS Italiano vs CSCD Laferrere | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 189
Paper proxy observation rows: 25
Positive EV value rows: 84
Suppressed-band observation rows: 0
Distinct matches: 23
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.537223
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=16, avg_ev=0.5242, max_ev=0.744
- draw: rows=3, avg_ev=0.5527, max_ev=0.644
- home: rows=6, avg_ev=0.5643, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 198
Forward fixture prediction rows: 198
Full model prediction rows: 2
Baseline prediction rows: 196
Max forward predictions: 300
Ready for price join: True
- 2026-05-18 15:00 | Club Deportivo Magallanes vs Deportes Recoleta | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:20 | AL Nasr SC (OMA) vs Samail SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:20 | Al Shabab vs Al-Seeb | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:20 | Al-Khaboora vs Al-Rustaq | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:20 | Bahla Club vs Al Nahda | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:20 | Ibri vs Dhofar SCSC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:20 | Oman Club vs Sur SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:20 | Sohar vs Saham | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:30 | FC Haka Valkeakoski vs HJK Klubi 04 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:30 | NK Samobor vs GNK Dinamo Zagreb | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 15:30 | SJK Akatemia/2 vs VPS Akatemia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:00 | Puszcza Niepolomice vs LKS Lodz | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:00 | Universidad de Concepcion vs Colo Colo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:05 | AL Draih vs Al-Jabalain | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:15 | Kuwait SC vs Al Arabi | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:30 | Falcons FC vs Bst Galaxy | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:30 | FC Lokomotiv 1929 Sofia vs PFC Slavia Sofia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:30 | PFC Dobrudzha Dobrich vs POFC Botev Vratsa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:30 | PFC Montana 1921 vs FK Spartak 1918 Varna | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 16:30 | PFK Beroe Stara Zagora vs FK Septemvri Sofia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-18 17:00 | Al Mokawloon Al Arab vs Wadi Degla SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 198
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 2264
Log type: probability_only_no_market_prices
- 2026-05-20 2026-05-18 18:00:00 | Aalesunds FK vs SK Brann | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 18:00:00 | Al-Khaleej Club vs Al Ahli Saudi FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 18:00:00 | Al-Najma vs Al-Shabab FC (SA) | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 18:00:00 | FH Hafnarfjordur vs IBV Vestmannaeyjar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 18:00:00 | Palermo FC vs US Catanzaro | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 19:00:00 | SC Freiburg vs Aston Villa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 22:00:00 | CA Boston River vs CD O´Higgins | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 22:00:00 | Club Nacional de Football vs Universitario de Deportes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 22:00:00 | Club Olimpia vs CR Vasco da Gama RJ | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 22:00:00 | Santos FC SP vs CA San Lorenzo de Almagro | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-18 23:30:00 | Detroit City FC vs Miami FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-18 14:00:00 | Noah Yerevan 2 vs FC Shirak Gyumri 2 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-18 22:30:00 | Urunday Universitario vs Defensor Sporting | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-22 2026-05-18 13:00:00 | FC Dynamo Kyiv vs FK Kudrivka U19 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-22 2026-05-18 14:00:00 | El Gouna FC vs Talaea El Gaish | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-22 2026-05-18 14:00:00 | Kahrabaa Ismailia vs Al Mokawloon Al Arab | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-18 00:15:00 | Defensor Sporting vs CA Penarol | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-18 02:00:00 | South Melbourne FC U20 vs Bentleigh Greens SC U20 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-18 04:30:00 | South Melbourne FC vs Bentleigh Greens SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-18 05:00:00 | South Melbourne FC vs Avondale FC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 198
Manual template rows: 198
Rows with complete manual odds: 0
Rows missing manual odds: 198
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-18 17:30 | AFC Eskilstuna vs FC Arlanda
- 2026-05-18 17:30 | AFC Hermannstadt vs Fotbal Club FCSB
- 2026-05-18 22:00 | AA Ponte Preta SP vs Londrina EC PR
- 2026-05-18 18:15 | FC Aarau vs Grasshopper Club Zurich
- 2026-05-18 17:30 | AB Argir vs Vikingur Gota
- 2026-05-18 23:00 | AD Confianca SE vs Maranhao AC MA
- 2026-05-18 16:05 | AL Draih vs Al-Jabalain
- 2026-05-18 17:00 | Al Mokawloon Al Arab vs Wadi Degla SC
- 2026-05-18 15:20 | AL Nasr SC (OMA) vs Samail SC
- 2026-05-18 17:15 | AL Qadisiya vs AL Fateh
- 2026-05-18 15:20 | Al Shabab vs Al-Seeb
- 2026-05-18 18:00 | AL Ula vs Al-Orobah
- 2026-05-18 15:20 | Al-Khaboora vs Al-Rustaq
- 2026-05-18 17:00 | Angelholms FF vs Kristianstad FC
- 2026-05-18 17:00 | Ariana FC vs Tvaakers IF

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 198
Source counts: {'odds_api_io_events_bookmaker_filtered': 186, 'odds_api_io_events_search': 10, 'football_data_fixtures_proxy': 2}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-18 17:30 | AFC Eskilstuna vs FC Arlanda | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-18 17:30 | AFC Hermannstadt vs Fotbal Club FCSB | romania-superliga | odds_api_io_events_bookmaker_filtered
- 2026-05-18 22:00 | AA Ponte Preta SP vs Londrina EC PR | brazil-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-18 18:15 | FC Aarau vs Grasshopper Club Zurich | switzerland-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-18 17:30 | AB Argir vs Vikingur Gota | faroe-islands-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-18 23:00 | AD Confianca SE vs Maranhao AC MA | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-18 16:05 | AL Draih vs Al-Jabalain | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-18 17:00 | Al Mokawloon Al Arab vs Wadi Degla SC | egypt-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-18 15:20 | AL Nasr SC (OMA) vs Samail SC | oman-omani-league | odds_api_io_events_bookmaker_filtered
- 2026-05-18 17:15 | AL Qadisiya vs AL Fateh | saudi-arabia-u21-elite-league | odds_api_io_events_bookmaker_filtered
- 2026-05-18 15:20 | Al Shabab vs Al-Seeb | oman-omani-league | odds_api_io_events_bookmaker_filtered
- 2026-05-18 18:00 | AL Ula vs Al-Orobah | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-18 15:20 | Al-Khaboora vs Al-Rustaq | oman-omani-league | odds_api_io_events_bookmaker_filtered
- 2026-05-18 17:00 | Angelholms FF vs Kristianstad FC | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-18 17:00 | Ariana FC vs Tvaakers IF | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-18 20:00 | Arsenal vs Burnley | premier_league | football_data_fixtures_proxy
- 2026-05-18 15:20 | Bahla Club vs Al Nahda | oman-omani-league | odds_api_io_events_bookmaker_filtered
- 2026-05-18 23:00 | Botafogo FC PB vs AA Internacional Limeira SP | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-18 18:30 | CD Leganes vs SD Huesca | spain-laliga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-18 23:00 | CD Santa Cruz vs Deportes Temuco | chile-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-18 15:00 | Club Deportivo Magallanes vs Deportes Recoleta | chile-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-18 21:00 | Criciuma EC SC vs AE Realidade Jovem SP | brazil-brasileiro-a3-women | odds_api_io_events_bookmaker_filtered
- 2026-05-18 18:30 | CS Barracas vs Defensores de Cambaceres | argentina-primera-c | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 198
Rows with complete odds: 0
- 2026-05-18 17:30 | AFC Eskilstuna vs FC Arlanda | bookmaker=bet365_manual
- 2026-05-18 17:30 | AFC Hermannstadt vs Fotbal Club FCSB | bookmaker=bet365_manual
- 2026-05-18 22:00 | AA Ponte Preta SP vs Londrina EC PR | bookmaker=bet365_manual
- 2026-05-18 18:15 | FC Aarau vs Grasshopper Club Zurich | bookmaker=bet365_manual
- 2026-05-18 17:30 | AB Argir vs Vikingur Gota | bookmaker=bet365_manual
- 2026-05-18 23:00 | AD Confianca SE vs Maranhao AC MA | bookmaker=bet365_manual
- 2026-05-18 16:05 | AL Draih vs Al-Jabalain | bookmaker=bet365_manual
- 2026-05-18 17:00 | Al Mokawloon Al Arab vs Wadi Degla SC | bookmaker=bet365_manual
- 2026-05-18 15:20 | AL Nasr SC (OMA) vs Samail SC | bookmaker=bet365_manual
- 2026-05-18 17:15 | AL Qadisiya vs AL Fateh | bookmaker=bet365_manual
- 2026-05-18 15:20 | Al Shabab vs Al-Seeb | bookmaker=bet365_manual
- 2026-05-18 18:00 | AL Ula vs Al-Orobah | bookmaker=bet365_manual
- 2026-05-18 15:20 | Al-Khaboora vs Al-Rustaq | bookmaker=bet365_manual
- 2026-05-18 17:00 | Angelholms FF vs Kristianstad FC | bookmaker=bet365_manual
- 2026-05-18 17:00 | Ariana FC vs Tvaakers IF | bookmaker=bet365_manual
- 2026-05-18 20:00 | Arsenal vs Burnley | bookmaker=bet365_manual
- 2026-05-18 15:20 | Bahla Club vs Al Nahda | bookmaker=bet365_manual
- 2026-05-18 23:00 | Botafogo FC PB vs AA Internacional Limeira SP | bookmaker=bet365_manual
- 2026-05-18 18:30 | CD Leganes vs SD Huesca | bookmaker=bet365_manual
- 2026-05-18 23:00 | CD Santa Cruz vs Deportes Temuco | bookmaker=bet365_manual
- 2026-05-18 15:00 | Club Deportivo Magallanes vs Deportes Recoleta | bookmaker=bet365_manual
- 2026-05-18 21:00 | Criciuma EC SC vs AE Realidade Jovem SP | bookmaker=bet365_manual
- 2026-05-18 18:30 | CS Barracas vs Defensores de Cambaceres | bookmaker=bet365_manual
- 2026-05-18 18:30 | CS Italiano vs CSCD Laferrere | bookmaker=bet365_manual

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
- 2026-05-18 17:30 | AFC Eskilstuna vs FC Arlanda
- 2026-05-18 17:30 | AFC Hermannstadt vs Fotbal Club FCSB
- 2026-05-18 22:00 | AA Ponte Preta SP vs Londrina EC PR
- 2026-05-18 18:15 | FC Aarau vs Grasshopper Club Zurich
- 2026-05-18 17:30 | AB Argir vs Vikingur Gota
- 2026-05-18 23:00 | AD Confianca SE vs Maranhao AC MA
- 2026-05-18 16:05 | AL Draih vs Al-Jabalain
- 2026-05-18 17:00 | Al Mokawloon Al Arab vs Wadi Degla SC
- 2026-05-18 15:20 | AL Nasr SC (OMA) vs Samail SC
- 2026-05-18 17:15 | AL Qadisiya vs AL Fateh
- 2026-05-18 15:20 | Al Shabab vs Al-Seeb
- 2026-05-18 18:00 | AL Ula vs Al-Orobah
- 2026-05-18 15:20 | Al-Khaboora vs Al-Rustaq
- 2026-05-18 17:00 | Angelholms FF vs Kristianstad FC
- 2026-05-18 17:00 | Ariana FC vs Tvaakers IF
- 2026-05-18 20:00 | Arsenal vs Burnley
- 2026-05-18 15:20 | Bahla Club vs Al Nahda
- 2026-05-18 23:00 | Botafogo FC PB vs AA Internacional Limeira SP
- 2026-05-18 18:30 | CD Leganes vs SD Huesca

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 339
Valid forward/proxy log rows: 336
Deduped forward/proxy observation rows: 225
Duplicate forward/proxy log rows: 111
Valid automatic proxy observation rows: 336
Deduped automatic proxy observation rows: 225
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-18 | Al Mokawloon Al Arab vs Wadi Degla SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.060500000000000005
- 2026-05-18 | Puszcza Niepolomice vs LKS Lodz | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0601
- 2026-05-18 | Kerala Blasters FC vs FC Goa | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0601
- 2026-05-14 | Viking FK 2 vs Akra | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-15 | Al Ittihad Ahli of Aleppo vs Al-Shorta SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-16 | Bay Olympic vs Auckland United FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
- 2026-05-16 | Belmont Swansea United FC vs Valentine FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.06
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
### Grotta vs Afturelding
- Date/time: 2026-05-18 19:15
- League/phase: iceland-1-deild / automatic_forward_price_proxy
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
- Prediction ID: b0c3badc84b6b8b241b0
### Maccabi Bney Reine vs Maccabi Netanya FC
- Date/time: 2026-05-18 17:00
- League/phase: israel-premier-league / automatic_forward_price_proxy
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
Total logged paper-test rows: 339
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 189, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 81, 'current_paper_picks': 25, 'newly_logged_picks': 21, 'total_logged_paper_rows': 339, 'source_used': 'automatic_forward_value_snapshots'}
- Grotta vs Afturelding | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Maccabi Bney Reine vs Maccabi Netanya FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AL Ula vs Al-Orobah | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AL Nasr SC (OMA) vs Samail SC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AB Argir vs Vikingur Gota | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AL Draih vs Al-Jabalain | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kuwait SC vs Al Arabi | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- MKS Arka Gdynia vs Bruk-Bet Termalica Nieciecza | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Club Deportivo Magallanes vs Deportes Recoleta | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PFC Dobrudzha Dobrich vs POFC Botev Vratsa | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hapoel Haifa FC vs Bnei Sakhnin FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Laholms FK vs FC Rosengaard 1917 | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Orgryte IS vs IFK Goteborg | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.9 | prob=0.3772 | EV=0.4711 | edge=0.1208 | penalty=0.4711 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Farul Constanta vs Metaloglobus Bucuresti | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CD Leganes vs SD Huesca | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Leganes vs Huesca | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- IK Oddevold vs Orebro SK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Leganes vs Huesca | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
