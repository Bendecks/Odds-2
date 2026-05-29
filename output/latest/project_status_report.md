# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-28T15:34:47.066148+00:00`
GitHub run: `378` attempt `1`
GitHub SHA: `5131790578b1662223c948fda9c9b2223a21abf3`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 44 |  |  |
| odds-api.io forward fixtures | True | 478 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 132 |  |  |
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
- Automatic value snapshots: 171
- Positive EV proxy rows: 84
- Proxy observation rows: 25
- Valid forward/proxy log rows: 741
- Deduped forward/proxy log rows: 569
- Duplicate forward/proxy log rows identified: 172
- Fresh API match coverage rate: 0.18
- Matches with fresh API price: 54
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
Current: 171 value snapshots; fresh API coverage rate 0.18.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 569 deduped forward/proxy rows; 172 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 47
Upcoming fixture rows: 0
Proxy price rows: 0
Sources attempted: 1
Errors: 0
No usable proxy odds rows were available from Football-Data fixtures source.

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 459
Fixture team rows unmatched: 914
Ready for model-fixture join: False
Automatic forward price rows: 54
odds-api.io price rows: 54
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AFC Ann Arbor | suggestion=nan | type=unmatched
- Union FC Macomb | suggestion=nan | type=unmatched
- AA Flamengo SP | suggestion=nan | type=unmatched
- Referencia FC SP | suggestion=nan | type=unmatched
- Aalesunds FK | suggestion=nan | type=unmatched
- HamKam | suggestion=nan | type=unmatched
- Aberdeen LFC | suggestion=nan | type=unmatched
- Queen's Park LFC | suggestion=nan | type=unmatched
- AC Monza | suggestion=nan | type=unmatched
- US Catanzaro | suggestion=nan | type=unmatched
- Adelaide Olympic FC | suggestion=nan | type=unmatched
- Fulham United FC | suggestion=nan | type=unmatched
- Adelaide University | suggestion=nan | type=unmatched
- Adelaide Comets FC | suggestion=nan | type=unmatched
- Adelaide University FC Reserve | suggestion=nan | type=unmatched
- Adelaide Comets FC Reserves | suggestion=nan | type=unmatched
- AE Velo Clube SP | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 54
Value snapshot rows: 171
Matches with any automatic price: 54
Matches with fresh API price: 54
Matches with odds-api.io price: 54
Fresh API match coverage rate: 0.18
odds-api.io match coverage rate: 0.18
Real-money ready: False
## Match coverage
- 2026-05-29 | Piratas de Campeche vs Tigres de Quintana Roo | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-29 | Manukau United FC vs Fencibles United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Shaanxi Union FC vs Nanjing City | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Western Springs AFC vs Bay Olympic | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Blacktown Spartans FC vs Western City Rangers FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Taroona vs South Hobart FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-29 | Brunswick City SC vs Manningham United Blues | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Heidelberg United FC vs Dandenong Thunder | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Nunawading City vs Altona City SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Keilor Park SC vs Kingston City FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Adelaide Olympic FC vs Fulham United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Broadmeadow Magic FC vs Maitland FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Campbelltown City SC vs Salisbury Inter | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Ethiopia Nigd Bank vs Ethio Electric | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Malvern City FC vs Box Hill United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Nepean FC vs Inner West Hawks FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 54
Matched prediction rows: 57
Value snapshot rows: 171
odds-api.io snapshot rows: 171
Baseline snapshot rows: 171
Full model snapshot rows: 0
Positive EV rows: 84
Source counts: {'odds_api_io_Bet365_ML': 171}
- 2026-05-29 | HJK Helsinki vs VIFK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=101.0 | prob=0.3488 | EV=34.2288 | match=1.0
- 2026-05-29 | Broadmeadow Magic FC vs Maitland FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3772 | EV=11.8248 | match=1.0
- 2026-05-29 | Taroona vs South Hobart FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=23.0 | prob=0.3772 | EV=7.6756 | match=1.0
- 2026-05-29 | Riga FC vs Grobinas SC/LFS | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-29 | HJK Helsinki vs VIFK | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.274 | EV=4.754 | match=1.0
- 2026-05-29 | Manukau United FC vs Fencibles United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-05-29 | Broadmeadow Magic FC vs Maitland FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-05-29 | Glenorchy Knights FC 2 vs Taroona | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3772 | EV=2.5834 | match=1.0
- 2026-05-29 | Andorra vs Iraq | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-29 | Majd FC vs Hatta SC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-29 | Kopa vs Lautp | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-29 | KPV Kokkola vs FC Inter Turku 2 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-29 | Taroona vs South Hobart FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.274 | EV=2.014 | match=1.0
- 2026-05-29 | Manukau United FC vs Fencibles United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.274 | EV=1.466 | match=1.0
- 2026-05-29 | Riga FC vs Grobinas SC/LFS | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.274 | EV=1.466 | match=1.0
- 2026-05-29 | Dubai City Football Club vs Dibba Al-Hisn SC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-29 | Western Springs AFC vs Bay Olympic | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 171
Pre-dedupe proxy candidate observation rows: 59
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 4
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-29 | Al-Hamriyah vs Dubai United FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-29 | FK Babrungas Plunge vs FK Minija 2017 | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-29 | Campbelltown City SC vs Salisbury Inter | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-29 | Ningbo Professional FC vs Nantong Zhiyun | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-29 | HPS vs Kuopion Palloseura | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-29 | Adelaide Olympic FC vs Fulham United FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-29 | Shire Endaselassie FC vs Hadiya Hossana FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-29 | Deportes Temuco vs Santiago Wanderers | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3772 | EV=0.47108 | edge=0.12079 | penalty=0.4710814710814708 | tier=proxy_watchlist | score=0.212
- 2026-05-29 | NK Opatija vs NK Karlovac 1919 | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244
- 2026-05-29 | PK Keski-Uusimaa vs KuPS Akatemia | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244
- 2026-05-29 | Shaanxi Union FC vs Nanjing City | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-05-29 | Guandong GZ-Power FC vs Shenzhen Juniors FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123

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
- ev_above_real_candidate_cap_possible_overconfidence: 7
- market_alignment_penalty_too_high_for_real_candidate: 7
- probability_or_league_rule_suppressed: 4
- low_probability_band_under_0_35: 4
- watchlist_only_pending_forward_settlement: 3
- edge_below_candidate_threshold: 2
## Row explanations
- 2026-05-29 | Al-Hamriyah vs Dubai United FC | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | FK Babrungas Plunge vs FK Minija 2017 | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Campbelltown City SC vs Salisbury Inter | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | Ningbo Professional FC vs Nantong Zhiyun | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | HPS vs Kuopion Palloseura | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | Adelaide Olympic FC vs Fulham United FC | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | Shire Endaselassie FC vs Hadiya Hossana FC | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | Deportes Temuco vs Santiago Wanderers | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | NK Opatija vs NK Karlovac 1919 | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | PK Keski-Uusimaa vs KuPS Akatemia | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Shaanxi Union FC vs Nanjing City | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Guandong GZ-Power FC vs Shenzhen Juniors FC | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 171
Paper proxy observation rows: 25
Positive EV value rows: 84
Suppressed-band observation rows: 0
Distinct matches: 24
Distinct sources: 0
Max EV: 0.744
Average EV: 0.412264
Max probability edge: 0.1488
Average match confidence: None
## By selection
- away: rows=16, avg_ev=0.4134, max_ev=0.744
- draw: rows=6, avg_ev=0.4271, max_ev=0.644
- home: rows=3, avg_ev=0.3768, max_ev=0.4711

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 459
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-29 02:30 | Piratas de Campeche vs Tigres de Quintana Roo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 07:00 | Manukau United FC vs Fencibles United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 07:00 | Shaanxi Union FC vs Nanjing City | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 07:00 | Western Springs AFC vs Bay Olympic | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 08:00 | Blacktown Spartans FC vs Western City Rangers FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 08:30 | Taroona vs South Hobart FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 08:45 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 09:30 | Brunswick City SC vs Manningham United Blues | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 09:30 | Heidelberg United FC vs Dandenong Thunder | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 09:30 | Nunawading City vs Altona City SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 09:45 | Keilor Park SC vs Kingston City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:00 | Adelaide Olympic FC vs Fulham United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:00 | Broadmeadow Magic FC vs Maitland FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:00 | Campbelltown City SC vs Salisbury Inter | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:00 | Ethiopia Nigd Bank vs Ethio Electric | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:00 | Malvern City FC vs Box Hill United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:00 | Nepean FC vs Inner West Hawks FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:15 | Glenorchy Knights FC 2 vs Taroona | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:30 | Spring Hills FC vs Melbourne City Youth | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:30 | West Torrens Birkalla vs Adelaide Comets FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 10:45 | Adelaide University vs Adelaide Comets FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 4327
Log type: probability_only_no_market_prices
- 2026-05-30 2026-05-29 06:00:00 | Altona Magic SC vs Oakleigh Cannons FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Bayside Argonauts FC vs Werribee City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Brunswick Juventus FC vs Eltham Redbacks FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Goulburn Valley Suns vs Essendon Royals SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Hawkesbury City SC vs Gladesville Ryde Magic | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Hurstville FC vs Rydalmere Lions FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Inglewood United vs Cockburn City | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Mandurah City vs Floreat Athena | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Marconi Stallions FC vs Rockdale Ilinden FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Metrostars vs West Adelaide | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Moreton City Excelsior FC 2 vs Pine Hills | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Murdoch University Melville FC vs Kingsley Westside FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | North Geelong Warriors FC vs North Sunshine Eagles FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Subiaco AFC vs UWA Nedlands FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Tai Po FC vs Eastern District | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 08:00:00 | Ferencvarosi TC vs MTK Budapest | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 08:15:00 | Modbury Vista vs Flinders United Wfc | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 09:00:00 | Puskas Akademia vs Illes Akademia | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 09:00:00 | Whittlesea United SC vs Springvale White Eagles | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 10:00:00 | Budapest Honved vs Diosgyori VTK | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 459
Manual template rows: 459
Rows with complete manual odds: 0
Rows missing manual odds: 459
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-29 23:00 | AFC Ann Arbor vs Union FC Macomb
- 2026-05-29 18:00 | AA Flamengo SP vs Referencia FC SP
- 2026-05-29 17:00 | Aalesunds FK vs HamKam
- 2026-05-29 18:35 | Aberdeen LFC vs Queen's Park LFC
- 2026-05-29 18:00 | AC Monza vs US Catanzaro
- 2026-05-29 10:00 | Adelaide Olympic FC vs Fulham United FC
- 2026-05-29 10:45 | Adelaide University vs Adelaide Comets FC
- 2026-05-29 08:45 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves
- 2026-05-29 18:00 | AE Velo Clube SP vs CA Bandeirante SP
- 2026-05-29 14:15 | AL Ittifaq vs Gulf United
- 2026-05-29 14:15 | AL Jazira AL Hamra vs Fujairah FC
- 2026-05-29 14:00 | Al Mokawloon Al Arab vs Modern Sport FC
- 2026-05-29 16:20 | Al Shabab Kuwait vs AL Tadhamon
- 2026-05-29 14:15 | Al Urooba UAE vs Masfoot Sports Club
- 2026-05-29 14:15 | Al-Dhaid vs Emirates Club

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 459
Source counts: {'odds_api_io_events_bookmaker_filtered': 446, 'odds_api_io_events_search': 13}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-29 23:00 | AFC Ann Arbor vs Union FC Macomb | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:00 | AA Flamengo SP vs Referencia FC SP | brazil-u20-paulista | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:00 | Aalesunds FK vs HamKam | norway-eliteserien | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:35 | Aberdeen LFC vs Queen's Park LFC | scotland-premier-league-women | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:00 | AC Monza vs US Catanzaro | italy-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-29 10:00 | Adelaide Olympic FC vs Fulham United FC | australia-south-australia-state-league-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-29 10:45 | Adelaide University vs Adelaide Comets FC | australia-south-australia-npl-women | odds_api_io_events_bookmaker_filtered
- 2026-05-29 08:45 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves | australia-south-australia-npl-reserves-women | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:00 | AE Velo Clube SP vs CA Bandeirante SP | brazil-u20-paulista | odds_api_io_events_bookmaker_filtered
- 2026-05-29 14:15 | AL Ittifaq vs Gulf United | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-29 14:15 | AL Jazira AL Hamra vs Fujairah FC | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-29 14:00 | Al Mokawloon Al Arab vs Modern Sport FC | egypt-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-29 16:20 | Al Shabab Kuwait vs AL Tadhamon | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-29 14:15 | Al Urooba UAE vs Masfoot Sports Club | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-29 14:15 | Al-Dhaid vs Emirates Club | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-29 14:15 | Al-Hamriyah vs Dubai United FC | united-arab-emirates-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-29 21:00 | America de Cali Sa vs International FC | colombia-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-29 22:30 | America FC RN vs Central SC PE | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-29 16:00 | Andorra vs Iraq | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-05-29 16:00 | Apollon Limassol vs Pafos FC | cyprus-cyprus-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:00 | Aragvi Dusheti vs FC Merani Martvili | georgia-erovnuli-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-29 20:00 | Asociacion Deportivo Cali vs Asociacion Deportivo Pasto | colombia-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:30 | ASV Siegendorf vs ASK Horitschon/U | austria-amateur-burgenland-burgenlandliga | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 459
Rows with complete odds: 0
- 2026-05-29 23:00 | AFC Ann Arbor vs Union FC Macomb | bookmaker=bet365_manual
- 2026-05-29 18:00 | AA Flamengo SP vs Referencia FC SP | bookmaker=bet365_manual
- 2026-05-29 17:00 | Aalesunds FK vs HamKam | bookmaker=bet365_manual
- 2026-05-29 18:35 | Aberdeen LFC vs Queen's Park LFC | bookmaker=bet365_manual
- 2026-05-29 18:00 | AC Monza vs US Catanzaro | bookmaker=bet365_manual
- 2026-05-29 10:00 | Adelaide Olympic FC vs Fulham United FC | bookmaker=bet365_manual
- 2026-05-29 10:45 | Adelaide University vs Adelaide Comets FC | bookmaker=bet365_manual
- 2026-05-29 08:45 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves | bookmaker=bet365_manual
- 2026-05-29 18:00 | AE Velo Clube SP vs CA Bandeirante SP | bookmaker=bet365_manual
- 2026-05-29 14:15 | AL Ittifaq vs Gulf United | bookmaker=bet365_manual
- 2026-05-29 14:15 | AL Jazira AL Hamra vs Fujairah FC | bookmaker=bet365_manual
- 2026-05-29 14:00 | Al Mokawloon Al Arab vs Modern Sport FC | bookmaker=bet365_manual
- 2026-05-29 16:20 | Al Shabab Kuwait vs AL Tadhamon | bookmaker=bet365_manual
- 2026-05-29 14:15 | Al Urooba UAE vs Masfoot Sports Club | bookmaker=bet365_manual
- 2026-05-29 14:15 | Al-Dhaid vs Emirates Club | bookmaker=bet365_manual
- 2026-05-29 14:15 | Al-Hamriyah vs Dubai United FC | bookmaker=bet365_manual
- 2026-05-29 21:00 | America de Cali Sa vs International FC | bookmaker=bet365_manual
- 2026-05-29 22:30 | America FC RN vs Central SC PE | bookmaker=bet365_manual
- 2026-05-29 16:00 | Andorra vs Iraq | bookmaker=bet365_manual
- 2026-05-29 16:00 | Apollon Limassol vs Pafos FC | bookmaker=bet365_manual
- 2026-05-29 17:00 | Aragvi Dusheti vs FC Merani Martvili | bookmaker=bet365_manual
- 2026-05-29 20:00 | Asociacion Deportivo Cali vs Asociacion Deportivo Pasto | bookmaker=bet365_manual
- 2026-05-29 17:30 | ASV Siegendorf vs ASK Horitschon/U | bookmaker=bet365_manual
- 2026-05-29 17:45 | Atletico Andahuaylas vs Club Yanapuma | bookmaker=bet365_manual

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
- 2026-05-29 23:00 | AFC Ann Arbor vs Union FC Macomb
- 2026-05-29 18:00 | AA Flamengo SP vs Referencia FC SP
- 2026-05-29 17:00 | Aalesunds FK vs HamKam
- 2026-05-29 18:35 | Aberdeen LFC vs Queen's Park LFC
- 2026-05-29 18:00 | AC Monza vs US Catanzaro
- 2026-05-29 10:00 | Adelaide Olympic FC vs Fulham United FC
- 2026-05-29 10:45 | Adelaide University vs Adelaide Comets FC
- 2026-05-29 08:45 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves
- 2026-05-29 18:00 | AE Velo Clube SP vs CA Bandeirante SP
- 2026-05-29 14:15 | AL Ittifaq vs Gulf United
- 2026-05-29 14:15 | AL Jazira AL Hamra vs Fujairah FC
- 2026-05-29 14:00 | Al Mokawloon Al Arab vs Modern Sport FC
- 2026-05-29 16:20 | Al Shabab Kuwait vs AL Tadhamon
- 2026-05-29 14:15 | Al Urooba UAE vs Masfoot Sports Club
- 2026-05-29 14:15 | Al-Dhaid vs Emirates Club
- 2026-05-29 14:15 | Al-Hamriyah vs Dubai United FC
- 2026-05-29 21:00 | America de Cali Sa vs International FC
- 2026-05-29 22:30 | America FC RN vs Central SC PE
- 2026-05-29 16:00 | Andorra vs Iraq

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 744
Valid forward/proxy log rows: 741
Deduped forward/proxy observation rows: 569
Duplicate forward/proxy log rows: 172
Valid automatic proxy observation rows: 741
Deduped automatic proxy observation rows: 569
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-27 | SJK Akatemia/2 vs JS Hercules | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0557
- 2026-05-19 | SV Ried vs Wolfsberger AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-21 | Kifisia vs Larisa | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-23 | Auckland United FC vs East Coast Bays | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-23 | Avondale FC vs Alamein FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-27 | VVSB Noordwijkerhout vs Excelsior Maassluis | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553
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
### Blacktown Spartans FC vs Western City Rangers FC
- Date/time: 2026-05-29 08:00
- League/phase: australia-u20-nsw-premier-league-2 / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 5.0
- Fair odds: 2.87
- Model probability: 0.3488
- Probability band: 0.25-0.35
- EV: 0.744
- Probability edge: 0.1488
- Alignment penalty: 0.744
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0711
- Prediction ID: 8aea38dab23077c5e8a9
### Heidelberg United FC vs Dandenong Thunder
- Date/time: 2026-05-29 09:30
- League/phase: australia-victoria-npl / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.75
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
Newly logged paper-test picks: 24
Total logged paper-test rows: 744
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 171, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 77, 'current_paper_picks': 25, 'newly_logged_picks': 24, 'total_logged_paper_rows': 744, 'source_used': 'automatic_forward_value_snapshots'}
- Blacktown Spartans FC vs Western City Rangers FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Heidelberg United FC vs Dandenong Thunder | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- NK Rudes Zagreb vs NK Sesvete | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Deportes Temuco vs Santiago Wanderers | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.9 | prob=0.3772 | EV=0.4711 | edge=0.1208 | penalty=0.4711 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kopa vs Lautp | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- West Torrens Birkalla vs Adelaide Comets FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al-Hamriyah vs Dubai United FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.8 | prob=0.3772 | EV=0.4334 | edge=0.114 | penalty=0.4334 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Dila Gori vs FC Samgurali Tskaltubo | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- NK Opatija vs NK Karlovac 1919 | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PK Keski-Uusimaa vs KuPS Akatemia | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Shaanxi Union FC vs Nanjing City | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Huima/Urho vs GBK Kokkola | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Fardu Ferghana vs Olimpik Mobiuz | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Guandong GZ-Power FC vs Shenzhen Juniors FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Majd FC vs Hatta SC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Malvern City FC vs Box Hill United FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.0821 | penalty=0.308 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AL Ittifaq vs Gulf United | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.7 | prob=0.3488 | EV=0.2906 | edge=0.0785 | penalty=0.2906 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al Urooba UAE vs Masfoot Sports Club | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
