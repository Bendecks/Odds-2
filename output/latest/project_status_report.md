# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-24T02:35:03.078575+00:00`
GitHub run: `369` attempt `1`
GitHub SHA: `87509e0862d86a3cc6eaef930952994fa76c3953`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 32 |  |  |
| Football-Data upcoming odds proxy | True | 93 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 53 |  |  |
| odds-api.io forward fixtures | True | 467 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 552 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 3 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 300 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 228
- Automatic value snapshots: 174
- Positive EV proxy rows: 82
- Proxy observation rows: 25
- Valid forward/proxy log rows: 574
- Deduped forward/proxy log rows: 426
- Duplicate forward/proxy log rows identified: 148
- Fresh API match coverage rate: 0.2544
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
Current: 174 value snapshots; fresh API coverage rate 0.2544.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 426 deduped forward/proxy rows; 148 duplicate raw rows identified.
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
Upcoming fixture rows: 228
Fixture team rows unmatched: 454
Ready for model-fixture join: False
Automatic forward price rows: 58
odds-api.io price rows: 58
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- Aasane Fotball | suggestion=nan | type=unmatched
- Raufoss IL | suggestion=nan | type=unmatched
- AL Budaiya | suggestion=nan | type=unmatched
- Al-Najma Manama | suggestion=nan | type=unmatched
- Al Jahra | suggestion=nan | type=unmatched
- Al Arabi | suggestion=nan | type=unmatched
- AL Tadhamon | suggestion=nan | type=unmatched
- Qadsia SC | suggestion=nan | type=unmatched
- Albion FC | suggestion=nan | type=unmatched
- Boston River | suggestion=nan | type=unmatched
- AS Bakaridjan | suggestion=nan | type=unmatched
- Djoliba AC | suggestion=nan | type=unmatched
- AS Fortuna | suggestion=nan | type=unmatched
- Colombe Sportive Du Dja Et Lobo | suggestion=nan | type=unmatched
- Asker Fotball | suggestion=nan | type=unmatched
- Gamle Oslo FK | suggestion=nan | type=unmatched
- B36 Torshavn | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 228
Automatic price rows: 58
Value snapshot rows: 174
Matches with any automatic price: 58
Matches with fresh API price: 58
Matches with odds-api.io price: 58
Fresh API match coverage rate: 0.2544
odds-api.io match coverage rate: 0.2544
Real-money ready: False
## Match coverage
- 2026-05-25 | Suwon Bluewings vs Cheonan City FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | South Melbourne FC vs Avondale FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Bhutan vs Nepal | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Esbjerg FB 2 vs Hobro IK 2 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Kolding IF vs Hillerod Fodbold | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | FK Gjoevik-Lyn vs Elverum | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Naestved HG vs Esbjerg FB | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Sotra SK vs Bjarg | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Strindheim TF vs Nardo FK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Valerenga IF 2 vs Heming | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Eidsvold TF vs Rana FK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | IK Start vs Vaalerenga IF | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Montevideo Wanderers vs Liverpool Montevideo | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-25 | Albion FC vs Boston River | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-25 | Brattvaag vs Notodden FK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Caps United FC vs FC Platinum | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-25 | Fram IF vs Raelingen | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 228
Proxy price rows: 58
Matched prediction rows: 58
Value snapshot rows: 174
odds-api.io snapshot rows: 174
Baseline snapshot rows: 174
Full model snapshot rows: 0
Positive EV rows: 82
Source counts: {'odds_api_io_Bet365_ML': 174}
- 2026-05-25 | South Melbourne FC vs Avondale FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-05-25 | KI Klaksvik vs AB Argir | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-25 | Eb/Streymur vs NSI Runavik | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-25 | FA Siauliai vs FK Riteriai | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-25 | South Melbourne FC vs Avondale FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.274 | EV=1.329 | match=1.0
- 2026-05-25 | Tromsoe IL vs Aalesunds FK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-25 | SV Dinamo Helfort 15 vs SV Schwechat | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-25 | Bhutan vs Nepal | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3772 | EV=1.2632 | match=1.0
- 2026-05-25 | Stroemsgodset IF vs Bryne FK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-25 | Club S Hammam-Lif vs AS Kasserine | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-25 | Eidsvold TF vs Rana FK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-25 | KI Klaksvik vs AB Argir | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.274 | EV=1.055 | match=1.0
- 2026-05-25 | Naestved HG vs Esbjerg FB | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-25 | Vikingur Gota vs Skala IF | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-25 | Suwon Bluewings vs Cheonan City FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-25 | Brattvaag vs Notodden FK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-25 | Asker Fotball vs Gamle Oslo FK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 174
Pre-dedupe proxy candidate observation rows: 61
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-25 | Fram vs Thor/KA | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-25 | Bnei Yehuda Tel Aviv FC vs Maccabi Herzliya | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-25 | Kolding IF vs Hillerod Fodbold | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-25 | PFC Lokomotiv Plovdiv vs Botev Plovdiv | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-25 | Hoedd IL vs Egersunds IK | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-25 | Ogre United vs Grobinas SC/LFS | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-25 | Valerenga IF 2 vs Heming | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-25 | HamKam vs Lillestroem SK | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-25 | IK Start vs Vaalerenga IF | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-25 | Esbjerg FB 2 vs Hobro IK 2 | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-25 | Notts County vs Salford City | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-25 | USM Khenchela vs USM Alger | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 4
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 8
- ev_above_real_candidate_cap_possible_overconfidence: 6
- watchlist_only_pending_forward_settlement: 2
- edge_below_candidate_threshold: 2
## Row explanations
- 2026-05-25 | Fram vs Thor/KA | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-25 | Bnei Yehuda Tel Aviv FC vs Maccabi Herzliya | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-25 | Kolding IF vs Hillerod Fodbold | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-25 | PFC Lokomotiv Plovdiv vs Botev Plovdiv | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-25 | Hoedd IL vs Egersunds IK | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-25 | Ogre United vs Grobinas SC/LFS | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-25 | Valerenga IF 2 vs Heming | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-25 | HamKam vs Lillestroem SK | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-25 | IK Start vs Vaalerenga IF | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-25 | Esbjerg FB 2 vs Hobro IK 2 | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-25 | Notts County vs Salford City | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-25 | USM Khenchela vs USM Alger | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 174
Paper proxy observation rows: 25
Positive EV value rows: 82
Suppressed-band observation rows: 0
Distinct matches: 25
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.381366
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=7, avg_ev=0.445, max_ev=0.744
- draw: rows=7, avg_ev=0.3896, max_ev=0.644
- home: rows=11, avg_ev=0.3356, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 228
Forward fixture prediction rows: 228
Full model prediction rows: 0
Baseline prediction rows: 228
Max forward predictions: 300
Ready for price join: True
- 2026-05-25 07:30 | Suwon Bluewings vs Cheonan City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 09:30 | South Melbourne FC vs Avondale FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 11:00 | Bhutan vs Nepal | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 11:00 | Esbjerg FB 2 vs Hobro IK 2 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 11:00 | Kolding IF vs Hillerod Fodbold | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 12:00 | FK Gjoevik-Lyn vs Elverum | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 12:00 | Naestved HG vs Esbjerg FB | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 12:00 | Sotra SK vs Bjarg | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 12:00 | Strindheim TF vs Nardo FK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 12:00 | Valerenga IF 2 vs Heming | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 12:30 | Eidsvold TF vs Rana FK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 12:30 | IK Start vs Vaalerenga IF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 12:30 | Montevideo Wanderers vs Liverpool Montevideo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 13:00 | Albion FC vs Boston River | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 13:00 | Brattvaag vs Notodden FK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 13:00 | Caps United FC vs FC Platinum | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 13:00 | Fram IF vs Raelingen | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 13:00 | Hvidovre IF vs Esbjerg FB | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 13:00 | IK Junkeren vs Ullensaker/Kisa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 13:00 | Konnerud vs Lokomotiv Oslo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-25 13:00 | Lysekloster vs Arendal FK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 228
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 3650
Log type: probability_only_no_market_prices
- 2026-05-31 2026-05-25 03:00:00 | Racing Club Avellaneda vs Defensa y Justicia | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 13:00:00 | AC Oulu vs FF Jaro | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 14:00:00 | Red Bull Bragantino SP vs SC Internacional RS | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 16:00:00 | FBC Melgar vs Alianza Atletico | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 16:30:00 | Deportes Limache vs Coquimbo Unido | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 18:00:00 | Mushuc Runa SC vs SD Aucas | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 18:15:00 | FC Cajamarca vs Alianza Lima | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 19:00:00 | CR Vasco da Gama RJ vs Atletico Mineiro MG | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 19:00:00 | Huachipato vs CD Universidad Catolica | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 19:00:00 | SE Palmeiras SP vs Chapecoense SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 20:00:00 | Los Chankas CYC vs UTC de Cajamarca | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 20:30:00 | Guayaquil City FC vs CSD Independiente del Valle | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 21:30:00 | CD O´Higgins vs CD Everton Vina del Mar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 22:00:00 | Cienciano vs Sporting Cristal | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 23:10:00 | CS Emelec vs CD Universidad Catolica del Ecuador | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 23:30:00 | Clube do Remo PA vs Sao Paulo FC SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-25 23:30:00 | Cruzeiro EC MG vs Fluminense FC RJ | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-01 2026-05-25 00:00:00 | CD Palestino vs Audax Italiano | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-01 2026-05-25 22:00:00 | Leones Futbol Club vs CSD Macara | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-02 2026-05-25 00:30:00 | CD Tecnico Universitario vs Barcelona SC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 228
Manual template rows: 228
Rows with complete manual odds: 0
Rows missing manual odds: 228
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-25 15:00 | Aasane Fotball vs Raufoss IL
- 2026-05-25 16:00 | AL Budaiya vs Al-Najma Manama
- 2026-05-25 16:15 | Al Jahra vs Al Arabi
- 2026-05-25 17:25 | AL Tadhamon vs Qadsia SC
- 2026-05-25 13:00 | Albion FC vs Boston River
- 2026-05-25 16:30 | AS Bakaridjan vs Djoliba AC
- 2026-05-25 15:00 | AS Fortuna vs Colombe Sportive Du Dja Et Lobo
- 2026-05-25 16:00 | Asker Fotball vs Gamle Oslo FK
- 2026-05-25 17:00 | B36 Torshavn vs 07 Vestur Sorvagur
- 2026-05-25 11:00 | Bhutan vs Nepal
- 2026-05-25 16:00 | Bnei Yehuda Tel Aviv FC vs Maccabi Herzliya
- 2026-05-25 18:00 | Boca Juniors vs CA Huracan
- 2026-05-25 19:00 | Bohemians Dublin FC vs Shamrock Rovers
- 2026-05-25 22:00 | Botafogo FC SP vs Athletic Club Sjdr MG
- 2026-05-25 13:00 | Brattvaag vs Notodden FK

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 228
Source counts: {'odds_api_io_events_bookmaker_filtered': 228}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-25 15:00 | Aasane Fotball vs Raufoss IL | norway-1st-division | odds_api_io_events_bookmaker_filtered
- 2026-05-25 16:00 | AL Budaiya vs Al-Najma Manama | bahrain-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-25 16:15 | Al Jahra vs Al Arabi | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-25 17:25 | AL Tadhamon vs Qadsia SC | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-25 13:00 | Albion FC vs Boston River | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-25 16:30 | AS Bakaridjan vs Djoliba AC | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-25 15:00 | AS Fortuna vs Colombe Sportive Du Dja Et Lobo | cameroon-elite-one | odds_api_io_events_bookmaker_filtered
- 2026-05-25 16:00 | Asker Fotball vs Gamle Oslo FK | norway-3rd-division-group-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-25 17:00 | B36 Torshavn vs 07 Vestur Sorvagur | faroe-islands-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-25 11:00 | Bhutan vs Nepal | international-saff-championship-women | odds_api_io_events_bookmaker_filtered
- 2026-05-25 16:00 | Bnei Yehuda Tel Aviv FC vs Maccabi Herzliya | israel-national-league | odds_api_io_events_bookmaker_filtered
- 2026-05-25 18:00 | Boca Juniors vs CA Huracan | argentina-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-25 19:00 | Bohemians Dublin FC vs Shamrock Rovers | ireland-premier-division | odds_api_io_events_bookmaker_filtered
- 2026-05-25 22:00 | Botafogo FC SP vs Athletic Club Sjdr MG | brazil-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-25 13:00 | Brattvaag vs Notodden FK | norway-2nd-division-group-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-25 19:15 | Breidablik Kopavogur vs FH Hafnarfjordur | iceland-besta-deild-women | odds_api_io_events_bookmaker_filtered
- 2026-05-25 16:00 | Brikama United vs Fortune | gambia-division-one | odds_api_io_events_bookmaker_filtered
- 2026-05-25 20:30 | CA Talleres de Cordoba vs CA River Plate (ARG) | argentina-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-25 18:30 | CA Victoriano Arenas vs Sacachispas FC | argentina-primera-c | odds_api_io_events_bookmaker_filtered
- 2026-05-25 13:00 | Caps United FC vs FC Platinum | zimbabwe-premier-soccer-league | odds_api_io_events_bookmaker_filtered
- 2026-05-25 20:00 | Carapegua vs CA Tembetary Ypane | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-25 20:00 | CD Independiente Juniors vs 9 de Octubre FC | ecuador-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-25 19:00 | CD Provincial Ovalle FC vs Brujas de Salamanca | chile-segunda-division | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 228
Rows with complete odds: 0
- 2026-05-25 15:00 | Aasane Fotball vs Raufoss IL | bookmaker=bet365_manual
- 2026-05-25 16:00 | AL Budaiya vs Al-Najma Manama | bookmaker=bet365_manual
- 2026-05-25 16:15 | Al Jahra vs Al Arabi | bookmaker=bet365_manual
- 2026-05-25 17:25 | AL Tadhamon vs Qadsia SC | bookmaker=bet365_manual
- 2026-05-25 13:00 | Albion FC vs Boston River | bookmaker=bet365_manual
- 2026-05-25 16:30 | AS Bakaridjan vs Djoliba AC | bookmaker=bet365_manual
- 2026-05-25 15:00 | AS Fortuna vs Colombe Sportive Du Dja Et Lobo | bookmaker=bet365_manual
- 2026-05-25 16:00 | Asker Fotball vs Gamle Oslo FK | bookmaker=bet365_manual
- 2026-05-25 17:00 | B36 Torshavn vs 07 Vestur Sorvagur | bookmaker=bet365_manual
- 2026-05-25 11:00 | Bhutan vs Nepal | bookmaker=bet365_manual
- 2026-05-25 16:00 | Bnei Yehuda Tel Aviv FC vs Maccabi Herzliya | bookmaker=bet365_manual
- 2026-05-25 18:00 | Boca Juniors vs CA Huracan | bookmaker=bet365_manual
- 2026-05-25 19:00 | Bohemians Dublin FC vs Shamrock Rovers | bookmaker=bet365_manual
- 2026-05-25 22:00 | Botafogo FC SP vs Athletic Club Sjdr MG | bookmaker=bet365_manual
- 2026-05-25 13:00 | Brattvaag vs Notodden FK | bookmaker=bet365_manual
- 2026-05-25 19:15 | Breidablik Kopavogur vs FH Hafnarfjordur | bookmaker=bet365_manual
- 2026-05-25 16:00 | Brikama United vs Fortune | bookmaker=bet365_manual
- 2026-05-25 20:30 | CA Talleres de Cordoba vs CA River Plate (ARG) | bookmaker=bet365_manual
- 2026-05-25 18:30 | CA Victoriano Arenas vs Sacachispas FC | bookmaker=bet365_manual
- 2026-05-25 13:00 | Caps United FC vs FC Platinum | bookmaker=bet365_manual
- 2026-05-25 20:00 | Carapegua vs CA Tembetary Ypane | bookmaker=bet365_manual
- 2026-05-25 20:00 | CD Independiente Juniors vs 9 de Octubre FC | bookmaker=bet365_manual
- 2026-05-25 19:00 | CD Provincial Ovalle FC vs Brujas de Salamanca | bookmaker=bet365_manual
- 2026-05-25 17:00 | Central Espanol Reserve vs Nacional de Montevideo | bookmaker=bet365_manual

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
- 2026-05-25 15:00 | Aasane Fotball vs Raufoss IL
- 2026-05-25 16:00 | AL Budaiya vs Al-Najma Manama
- 2026-05-25 16:15 | Al Jahra vs Al Arabi
- 2026-05-25 17:25 | AL Tadhamon vs Qadsia SC
- 2026-05-25 13:00 | Albion FC vs Boston River
- 2026-05-25 16:30 | AS Bakaridjan vs Djoliba AC
- 2026-05-25 15:00 | AS Fortuna vs Colombe Sportive Du Dja Et Lobo
- 2026-05-25 16:00 | Asker Fotball vs Gamle Oslo FK
- 2026-05-25 17:00 | B36 Torshavn vs 07 Vestur Sorvagur
- 2026-05-25 11:00 | Bhutan vs Nepal
- 2026-05-25 16:00 | Bnei Yehuda Tel Aviv FC vs Maccabi Herzliya
- 2026-05-25 18:00 | Boca Juniors vs CA Huracan
- 2026-05-25 19:00 | Bohemians Dublin FC vs Shamrock Rovers
- 2026-05-25 22:00 | Botafogo FC SP vs Athletic Club Sjdr MG
- 2026-05-25 13:00 | Brattvaag vs Notodden FK
- 2026-05-25 19:15 | Breidablik Kopavogur vs FH Hafnarfjordur
- 2026-05-25 16:00 | Brikama United vs Fortune
- 2026-05-25 20:30 | CA Talleres de Cordoba vs CA River Plate (ARG)
- 2026-05-25 18:30 | CA Victoriano Arenas vs Sacachispas FC

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 577
Valid forward/proxy log rows: 574
Deduped forward/proxy observation rows: 426
Duplicate forward/proxy log rows: 148
Valid automatic proxy observation rows: 574
Deduped automatic proxy observation rows: 426
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-25 | HamKam vs Lillestroem SK | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0579
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
### AS Fortuna vs Colombe Sportive Du Dja Et Lobo
- Date/time: 2026-05-25 15:00
- League/phase: cameroon-elite-one / automatic_forward_price_proxy
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
- Prediction ID: d5af9519ccc18184555a
### Haukar Hafnarfjordur vs UMF Selfoss
- Date/time: 2026-05-25 14:00
- League/phase: iceland-1-deild-women / automatic_forward_price_proxy
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
Total logged paper-test rows: 577
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 174, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 82, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 577, 'source_used': 'automatic_forward_value_snapshots'}
- AS Fortuna vs Colombe Sportive Du Dja Et Lobo | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Haukar Hafnarfjordur vs UMF Selfoss | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Sotra SK vs Bjarg | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Stade Gabesien vs US Tataouine | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Samgurali Tskaltubo vs FC Iberia 1999 | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Eb/Streymur vs NSI Runavik | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Volsungur vs Keflavik IF | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.9 | prob=0.3772 | EV=0.4711 | edge=0.1208 | penalty=0.4711 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Fram vs Thor/KA | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FA Siauliai vs FK Riteriai | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Haugesund vs Moss FK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Bnei Yehuda Tel Aviv FC vs Maccabi Herzliya | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.4 | prob=0.3772 | EV=0.2825 | edge=0.0831 | penalty=0.2825 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Lyn 1896 FK vs Stroemmen IF | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.7 | prob=0.3488 | EV=0.2906 | edge=0.0785 | penalty=0.2906 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ogre United vs Grobinas SC/LFS | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.3 | prob=0.3772 | EV=0.2448 | edge=0.0742 | penalty=0.2448 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hoedd IL vs Egersunds IK | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.3 | prob=0.3772 | EV=0.2448 | edge=0.0742 | penalty=0.2448 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PFC Lokomotiv Plovdiv vs Botev Plovdiv | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.3 | prob=0.3772 | EV=0.2448 | edge=0.0742 | penalty=0.2448 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kolding IF vs Hillerod Fodbold | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.3 | prob=0.3772 | EV=0.2448 | edge=0.0742 | penalty=0.2448 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Bhutan vs Nepal | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Asker Fotball vs Gamle Oslo FK | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
