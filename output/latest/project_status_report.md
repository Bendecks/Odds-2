# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-25T02:43:32.605466+00:00`
GitHub run: `371` attempt `1`
GitHub SHA: `0bf19d20dd4179eebff9e93b378b866e3fc97058`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 58 |  |  |
| odds-api.io forward fixtures | True | 142 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 174 |  |  |
| Forward price coverage report | True | 228 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 4 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 228 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 262
- Automatic value snapshots: 150
- Positive EV proxy rows: 71
- Proxy observation rows: 25
- Valid forward/proxy log rows: 599
- Deduped forward/proxy log rows: 451
- Duplicate forward/proxy log rows identified: 148
- Fresh API match coverage rate: 0.1794
- Matches with fresh API price: 47
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
Current: 150 value snapshots; fresh API coverage rate 0.1794.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 451 deduped forward/proxy rows; 148 duplicate raw rows identified.
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
Upcoming fixture rows: 262
Fixture team rows unmatched: 517
Ready for model-fixture join: False
Automatic forward price rows: 47
odds-api.io price rows: 47
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- Aasane Fotball 2 | suggestion=nan | type=unmatched
- Gneist | suggestion=nan | type=unmatched
- FC Alashkert Yerevan | suggestion=nan | type=unmatched
- FC Shirak Gyumri | suggestion=nan | type=unmatched
- Alhama CF | suggestion=nan | type=unmatched
- Levante UD | suggestion=nan | type=unmatched
- Argentinos Juniors Reserve | suggestion=nan | type=unmatched
- CA Banfield | suggestion=nan | type=unmatched
- AS Saint-Etienne | suggestion=nan | type=unmatched
- OGC Nice | suggestion=nan | type=unmatched
- Atletico Madrid | suggestion=nan | type=unmatched
- CD Tenerife | suggestion=nan | type=unmatched
- BFC Daugavpils | suggestion=nan | type=unmatched
- FK Auda Riga | suggestion=nan | type=unmatched
- FC Badalona Women | suggestion=nan | type=unmatched
- FC Banik Ostrava | suggestion=nan | type=unmatched
- FC Silon Taborsko | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 262
Automatic price rows: 47
Value snapshot rows: 150
Matches with any automatic price: 47
Matches with fresh API price: 47
Matches with odds-api.io price: 47
Fresh API match coverage rate: 0.1794
odds-api.io match coverage rate: 0.1794
Real-money ready: False
## Match coverage
- 2026-05-26 | Taian Tiankuang vs Dalian Kewei | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | Shanghai Port B vs Lanzhou Longyuan Athletic | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | Shenzhen 2028 FC vs Wenzhou Professional FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | Logan Lightning vs Palm Beach SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | Hangzhou Linping Wuyue vs Hubei Istar | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | Chengdu Rongcheng B vs Guizhou Guiyang Athletic | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | Goztepe vs Arnavutkoy Belediyesi Futbol SK | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-26 | Trabzonspor vs Manisa Futbol Kulubu | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-26 | Cape Town City FC vs Milford FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | FC Alashkert Yerevan vs FC Shirak Gyumri | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | Club Yanapuma vs Club Alianza Lima | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | FS Jelgava vs FK Liepaja | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | IFK Mariehamn vs FC Lahti | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | JaPS vs Kuopion Palloseura | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | BFC Daugavpils vs FK Auda Riga | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | FC Banik Ostrava vs FC Silon Taborsko | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-26 | BK Olympic vs Ariana FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 262
Proxy price rows: 47
Matched prediction rows: 50
Value snapshot rows: 150
odds-api.io snapshot rows: 150
Baseline snapshot rows: 150
Full model snapshot rows: 0
Positive EV rows: 71
Source counts: {'odds_api_io_Bet365_ML': 150}
- 2026-05-26 | Vaalerenga Oslo vs Bodoe/Glimt | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3488 | EV=16.7888 | match=1.0
- 2026-05-26 | Vaalerenga Oslo vs Bodoe/Glimt | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.274 | EV=4.206 | match=1.0
- 2026-05-31 | FC Cajamarca vs Alianza Lima | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3772 | EV=3.5264 | match=0.6873
- 2026-05-26 | Club Yanapuma vs Club Alianza Lima | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3772 | EV=3.5264 | match=1.0
- 2026-05-26 | SK Brann vs Lyn | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-26 | Waterford FC vs Shamrock Rovers FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3772 | EV=3.1492 | match=1.0
- 2026-05-26 | KPV/Akatemia vs FC Kiisto | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3772 | EV=2.772 | match=1.0
- 2026-05-26 | JaPS vs Kuopion Palloseura | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-26 | FC Alashkert Yerevan vs FC Shirak Gyumri | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-26 | FC Banik Ostrava vs FC Silon Taborsko | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-26 | Molde FK vs Rosenborg BK Kvinner | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3772 | EV=1.3575 | match=1.0
- 2026-05-26 | Club Yanapuma vs Club Alianza Lima | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.274 | EV=1.329 | match=1.0
- 2026-05-31 | FC Cajamarca vs Alianza Lima | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.274 | EV=1.329 | match=0.6873
- 2026-05-26 | IFK Mariehamn vs FC Lahti | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3772 | EV=1.1689 | match=1.0
- 2026-05-26 | Nigeria vs Zimbabwe | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-26 | FC Badalona Women vs Real Madrid | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-05-26 | KPV/Akatemia vs FC Kiisto | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.274 | EV=1.055 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 150
Pre-dedupe proxy candidate observation rows: 48
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 1
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-26 | Chengdu Rongcheng B vs Guizhou Guiyang Athletic | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-26 | FS Jelgava vs FK Liepaja | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-26 | BFC Daugavpils vs FK Auda Riga | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-26 | CSD Flandria vs Arsenal de Sarandi | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-26 | CD Armenio vs Argentino de Merlo | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-26 | CS Dock Sud vs Real Pilar FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-26 | CA Brown de Adrogue vs CA Talleres de Remedios | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-26 | Hangzhou Linping Wuyue vs Hubei Istar | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-26 | Logan Lightning vs Palm Beach SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-26 | FC Honka vs VJS | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-26 | BK Olympic vs Ariana FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-26 | Greuther Furth vs Rot-Weiss Essen | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244

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
- market_alignment_penalty_too_high_for_real_candidate: 8
- ev_above_real_candidate_cap_possible_overconfidence: 5
- watchlist_only_pending_forward_settlement: 2
- edge_below_candidate_threshold: 2
- probability_or_league_rule_suppressed: 1
- low_probability_band_under_0_35: 1
## Row explanations
- 2026-05-26 | Chengdu Rongcheng B vs Guizhou Guiyang Athletic | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-26 | FS Jelgava vs FK Liepaja | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-26 | BFC Daugavpils vs FK Auda Riga | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-26 | CSD Flandria vs Arsenal de Sarandi | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-26 | CD Armenio vs Argentino de Merlo | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-26 | CS Dock Sud vs Real Pilar FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-26 | CA Brown de Adrogue vs CA Talleres de Remedios | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-26 | Hangzhou Linping Wuyue vs Hubei Istar | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-26 | Logan Lightning vs Palm Beach SC | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-26 | FC Honka vs VJS | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-26 | BK Olympic vs Ariana FC | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-26 | Greuther Furth vs Rot-Weiss Essen | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 150
Paper proxy observation rows: 25
Positive EV value rows: 71
Suppressed-band observation rows: 0
Distinct matches: 24
Distinct sources: 0
Max EV: 0.781
Average EV: 0.450633
Max probability edge: 0.1488
Average match confidence: None
## By selection
- away: rows=14, avg_ev=0.4641, max_ev=0.744
- draw: rows=7, avg_ev=0.4874, max_ev=0.781
- home: rows=4, avg_ev=0.3391, max_ev=0.3956

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 262
Forward fixture prediction rows: 262
Full model prediction rows: 0
Baseline prediction rows: 262
Max forward predictions: 300
Ready for price join: True
- 2026-05-26 07:30 | Taian Tiankuang vs Dalian Kewei | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 08:00 | Shanghai Port B vs Lanzhou Longyuan Athletic | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 08:00 | Shenzhen 2028 FC vs Wenzhou Professional FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 09:30 | Logan Lightning vs Palm Beach SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 11:30 | Hangzhou Linping Wuyue vs Hubei Istar | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 11:35 | Chengdu Rongcheng B vs Guizhou Guiyang Athletic | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 12:00 | Goztepe vs Arnavutkoy Belediyesi Futbol SK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 12:00 | Trabzonspor vs Manisa Futbol Kulubu | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 13:00 | Cape Town City FC vs Milford FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 15:00 | FC Alashkert Yerevan vs FC Shirak Gyumri | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 15:00 | Club Yanapuma vs Club Alianza Lima | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 15:00 | FS Jelgava vs FK Liepaja | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 15:00 | IFK Mariehamn vs FC Lahti | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 15:30 | JaPS vs Kuopion Palloseura | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 16:00 | BFC Daugavpils vs FK Auda Riga | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 16:00 | FC Banik Ostrava vs FC Silon Taborsko | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 16:00 | BK Olympic vs Ariana FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 16:00 | Brodd vs Odds BK 2 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 16:00 | FC Honka vs VJS | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 16:00 | KPV/Akatemia vs FC Kiisto | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-26 16:00 | LSK Kvinner FK vs Hoenefoss BK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 262
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 3816
Log type: probability_only_no_market_prices
- 2026-05-31 2026-05-26 12:00:00 | Degerfors IF vs IF Brommapojkarna | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 12:00:00 | Vasteraas SK vs IFK Goteborg | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 14:00:00 | Brighton and Hove Albion WFC vs Manchester City WFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 14:00:00 | Londrina EC PR vs Vila Nova FC GO | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 14:00:00 | Paide Linnameeskond vs FC Kuressaare | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 14:00:00 | Sao Bernardo FC vs Gremio Novorizontino SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | Burgos CF vs FC Andorra | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | CD Castellon vs SD Eibar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | CD Leganes vs CD Mirandes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | Cordoba CF vs SD Huesca | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | Racing Santander vs Cadiz CF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | RC Deportivo De La Coruna vs UD Las Palmas | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | Real Sociedad San Sebastian B vs Cultural Leonesa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | Real Zaragoza vs Malaga CF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 16:30:00 | UD Almeria vs Real Valladolid | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 18:00:00 | Sporting Jax vs Brooklyn FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 19:00:00 | Ceara SC CE vs Operario Ferroviario EC PR | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 20:00:00 | Forge FC Hamilton vs Cavalry FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-26 23:30:00 | Cuiaba EC MT vs CR Brasil AL | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-06-01 2026-05-26 22:00:00 | AA Ponte Preta SP vs Botafogo FC SP | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 262
Manual template rows: 262
Rows with complete manual odds: 0
Rows missing manual odds: 262
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-26 17:00 | Aasane Fotball 2 vs Gneist
- 2026-05-26 15:00 | FC Alashkert Yerevan vs FC Shirak Gyumri
- 2026-05-26 17:00 | Alhama CF vs Levante UD
- 2026-05-26 18:00 | Argentinos Juniors Reserve vs CA Banfield
- 2026-05-26 18:45 | AS Saint-Etienne vs OGC Nice
- 2026-05-26 19:00 | Atletico Madrid vs CD Tenerife
- 2026-05-26 16:00 | BFC Daugavpils vs FK Auda Riga
- 2026-05-26 17:00 | FC Badalona Women vs Real Madrid
- 2026-05-26 16:00 | FC Banik Ostrava vs FC Silon Taborsko
- 2026-05-26 16:00 | BK Olympic vs Ariana FC
- 2026-05-26 16:00 | Brodd vs Odds BK 2
- 2026-05-26 22:00 | CA Brown de Adrogue vs CA Talleres de Remedios
- 2026-05-26 18:00 | CA Huracan vs Ferro Carril Oeste
- 2026-05-26 22:30 | CA Ituzaingo vs CSCD Laferrere
- 2026-05-26 22:00 | CA Lanus vs Mirassol FC SP

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 262
Source counts: {'odds_api_io_events_bookmaker_filtered': 259, 'odds_api_io_events_search': 3}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-26 17:00 | Aasane Fotball 2 vs Gneist | norway-3rd-division-group-3 | odds_api_io_events_bookmaker_filtered
- 2026-05-26 15:00 | FC Alashkert Yerevan vs FC Shirak Gyumri | armenia-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-26 17:00 | Alhama CF vs Levante UD | spain-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-26 18:00 | Argentinos Juniors Reserve vs CA Banfield | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-26 18:45 | AS Saint-Etienne vs OGC Nice | france-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-26 19:00 | Atletico Madrid vs CD Tenerife | spain-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-26 16:00 | BFC Daugavpils vs FK Auda Riga | latvia-virsliga | odds_api_io_events_bookmaker_filtered
- 2026-05-26 17:00 | FC Badalona Women vs Real Madrid | spain-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-26 16:00 | FC Banik Ostrava vs FC Silon Taborsko | czechia-1-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-26 16:00 | BK Olympic vs Ariana FC | sweden-svenska-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-26 16:00 | Brodd vs Odds BK 2 | norway-3rd-division-group-4 | odds_api_io_events_bookmaker_filtered
- 2026-05-26 22:00 | CA Brown de Adrogue vs CA Talleres de Remedios | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-26 18:00 | CA Huracan vs Ferro Carril Oeste | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-26 22:30 | CA Ituzaingo vs CSCD Laferrere | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-26 22:00 | CA Lanus vs Mirassol FC SP | international-clubs-copa-libertadores | odds_api_io_events_bookmaker_filtered
- 2026-05-26 13:00 | Cape Town City FC vs Milford FC | south-africa-premiership | odds_api_io_events_bookmaker_filtered
- 2026-05-26 18:30 | CD Armenio vs Argentino de Merlo | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-26 22:00 | CD Palestino vs Deportivo Riestra AFBC | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered
- 2026-05-26 11:35 | Chengdu Rongcheng B vs Guizhou Guiyang Athletic | china-china-league-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-26 22:00 | Club Comunicaciones vs CD UAI Urquiza | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-26 15:00 | Club Yanapuma vs Club Alianza Lima | peru-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-26 18:30 | CS Dock Sud vs Real Pilar FC | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-26 18:30 | CSD Flandria vs Arsenal de Sarandi | argentina-primera-b | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 262
Rows with complete odds: 0
- 2026-05-26 17:00 | Aasane Fotball 2 vs Gneist | bookmaker=bet365_manual
- 2026-05-26 15:00 | FC Alashkert Yerevan vs FC Shirak Gyumri | bookmaker=bet365_manual
- 2026-05-26 17:00 | Alhama CF vs Levante UD | bookmaker=bet365_manual
- 2026-05-26 18:00 | Argentinos Juniors Reserve vs CA Banfield | bookmaker=bet365_manual
- 2026-05-26 18:45 | AS Saint-Etienne vs OGC Nice | bookmaker=bet365_manual
- 2026-05-26 19:00 | Atletico Madrid vs CD Tenerife | bookmaker=bet365_manual
- 2026-05-26 16:00 | BFC Daugavpils vs FK Auda Riga | bookmaker=bet365_manual
- 2026-05-26 17:00 | FC Badalona Women vs Real Madrid | bookmaker=bet365_manual
- 2026-05-26 16:00 | FC Banik Ostrava vs FC Silon Taborsko | bookmaker=bet365_manual
- 2026-05-26 16:00 | BK Olympic vs Ariana FC | bookmaker=bet365_manual
- 2026-05-26 16:00 | Brodd vs Odds BK 2 | bookmaker=bet365_manual
- 2026-05-26 22:00 | CA Brown de Adrogue vs CA Talleres de Remedios | bookmaker=bet365_manual
- 2026-05-26 18:00 | CA Huracan vs Ferro Carril Oeste | bookmaker=bet365_manual
- 2026-05-26 22:30 | CA Ituzaingo vs CSCD Laferrere | bookmaker=bet365_manual
- 2026-05-26 22:00 | CA Lanus vs Mirassol FC SP | bookmaker=bet365_manual
- 2026-05-26 13:00 | Cape Town City FC vs Milford FC | bookmaker=bet365_manual
- 2026-05-26 18:30 | CD Armenio vs Argentino de Merlo | bookmaker=bet365_manual
- 2026-05-26 22:00 | CD Palestino vs Deportivo Riestra AFBC | bookmaker=bet365_manual
- 2026-05-26 11:35 | Chengdu Rongcheng B vs Guizhou Guiyang Athletic | bookmaker=bet365_manual
- 2026-05-26 22:00 | Club Comunicaciones vs CD UAI Urquiza | bookmaker=bet365_manual
- 2026-05-26 15:00 | Club Yanapuma vs Club Alianza Lima | bookmaker=bet365_manual
- 2026-05-26 18:30 | CS Dock Sud vs Real Pilar FC | bookmaker=bet365_manual
- 2026-05-26 18:30 | CSD Flandria vs Arsenal de Sarandi | bookmaker=bet365_manual
- 2026-05-26 16:30 | Defensa Y Justicia Reserve vs Independiente Reserve | bookmaker=bet365_manual

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
- 2026-05-26 17:00 | Aasane Fotball 2 vs Gneist
- 2026-05-26 15:00 | FC Alashkert Yerevan vs FC Shirak Gyumri
- 2026-05-26 17:00 | Alhama CF vs Levante UD
- 2026-05-26 18:00 | Argentinos Juniors Reserve vs CA Banfield
- 2026-05-26 18:45 | AS Saint-Etienne vs OGC Nice
- 2026-05-26 19:00 | Atletico Madrid vs CD Tenerife
- 2026-05-26 16:00 | BFC Daugavpils vs FK Auda Riga
- 2026-05-26 17:00 | FC Badalona Women vs Real Madrid
- 2026-05-26 16:00 | FC Banik Ostrava vs FC Silon Taborsko
- 2026-05-26 16:00 | BK Olympic vs Ariana FC
- 2026-05-26 16:00 | Brodd vs Odds BK 2
- 2026-05-26 22:00 | CA Brown de Adrogue vs CA Talleres de Remedios
- 2026-05-26 18:00 | CA Huracan vs Ferro Carril Oeste
- 2026-05-26 22:30 | CA Ituzaingo vs CSCD Laferrere
- 2026-05-26 22:00 | CA Lanus vs Mirassol FC SP
- 2026-05-26 13:00 | Cape Town City FC vs Milford FC
- 2026-05-26 18:30 | CD Armenio vs Argentino de Merlo
- 2026-05-26 22:00 | CD Palestino vs Deportivo Riestra AFBC
- 2026-05-26 11:35 | Chengdu Rongcheng B vs Guizhou Guiyang Athletic

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 602
Valid forward/proxy log rows: 599
Deduped forward/proxy observation rows: 451
Duplicate forward/proxy log rows: 148
Valid automatic proxy observation rows: 599
Deduped automatic proxy observation rows: 451
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
### CA Paranaense PR vs Mirassol FC SP
- Date/time: 2026-05-30 19:00
- League/phase: brazil-brasileiro-serie-a / automatic_forward_price_proxy
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
- Prediction ID: 22718fc795bc90ca9770
### CA Lanus vs Mirassol FC SP
- Date/time: 2026-05-26 22:00
- League/phase: international-clubs-copa-libertadores / automatic_forward_price_proxy
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
Total logged paper-test rows: 602
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 150, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 57, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 602, 'source_used': 'automatic_forward_value_snapshots'}
- CA Paranaense PR vs Mirassol FC SP | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CA Lanus vs Mirassol FC SP | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Raade IL vs Sarpsborg 08 2 | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SK Brann vs Lyn | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Shanghai Port B vs Lanzhou Longyuan Athletic | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Banik Ostrava vs FC Silon Taborsko | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Atletico Madrid vs CD Tenerife | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- KR Reykjavik vs Valur Reykjavik | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Brodd vs Odds BK 2 | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Waterford FC vs Shamrock Rovers FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.75 | prob=0.274 | EV=0.5755 | edge=0.1001 | penalty=0.5755 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Chengdu Rongcheng B vs Guizhou Guiyang Athletic | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.7 | prob=0.3772 | EV=0.3956 | edge=0.1069 | penalty=0.3956 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Greuther Furth vs Rot-Weiss Essen | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Stabaek Fotball vs Haugesund | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FS Jelgava vs FK Liepaja | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- LSK Kvinner FK vs Hoenefoss BK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- BFC Daugavpils vs FK Auda Riga | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SK Herd vs Aalesund FK 2 | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Deportivo Camioneros vs CA Villa San Carlos | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
