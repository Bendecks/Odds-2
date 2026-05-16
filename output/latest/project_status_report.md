# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-16T02:12:57.625768+00:00`
GitHub run: `352` attempt `1`
GitHub SHA: `cdf485a2fb45638abdfcc2eae474fbad32c708e2`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 107 |  |  |
| Football-Data upcoming odds proxy | True | 316 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 35 |  |  |
| odds-api.io forward fixtures | True | 1069 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 198 |  |  |
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
- Forward fixture predictions: 300
- Automatic value snapshots: 615
- Positive EV proxy rows: 312
- Proxy observation rows: 25
- Valid forward/proxy log rows: 248
- Deduped forward/proxy log rows: 168
- Duplicate forward/proxy log rows identified: 80
- Fresh API match coverage rate: 0.1367
- Matches with fresh API price: 41
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
Current: 615 value snapshots; fresh API coverage rate 0.1367.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 168 deduped forward/proxy rows; 80 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 112
Upcoming fixture rows: 107
Proxy price rows: 316
Sources attempted: 1
Errors: 0
- 2026-05-16 15:00 | Charleroi vs Westerlo | football_data_bet365_proxy | 1.95/3.5/3.25
- 2026-05-16 15:00 | Charleroi vs Westerlo | football_data_max_market_proxy | 2.05/3.8/3.35
- 2026-05-16 15:00 | Charleroi vs Westerlo | football_data_average_market_proxy | 2.0/3.6/3.23
- 2026-05-16 17:15 | Standard vs Genk | football_data_bet365_proxy | 3.1/3.4/2.1
- 2026-05-16 17:15 | Standard vs Genk | football_data_max_market_proxy | 3.2/3.6/2.2
- 2026-05-16 17:15 | Standard vs Genk | football_data_average_market_proxy | 3.08/3.43/2.12
- 2026-05-16 19:45 | St Truiden vs Gent | football_data_bet365_proxy | 1.91/3.6/3.5
- 2026-05-16 19:45 | St Truiden vs Gent | football_data_max_market_proxy | 1.95/4.0/3.6
- 2026-05-16 19:45 | St Truiden vs Gent | football_data_average_market_proxy | 1.92/3.67/3.4
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_bet365_proxy | 1.83/3.6/3.75
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_max_market_proxy | 1.87/4.0/4.0
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_average_market_proxy | 1.8/3.72/3.79
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_bet365_proxy | 2.05/3.5/3.1
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_max_market_proxy | 2.1/3.8/3.45
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_average_market_proxy | 2.02/3.51/3.23
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | football_data_bet365_proxy | 1.14/9.5/14.0
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | football_data_max_market_proxy | 1.18/9.5/16.0
- 2026-05-16 14:30 | Bayern Munich vs FC Koln | football_data_average_market_proxy | 1.14/8.71/12.84
- 2026-05-16 14:30 | Ein Frankfurt vs Stuttgart | football_data_bet365_proxy | 3.4/4.33/1.85
- 2026-05-16 14:30 | Ein Frankfurt vs Stuttgart | football_data_max_market_proxy | 3.5/4.33/1.91
- 2026-05-16 14:30 | Ein Frankfurt vs Stuttgart | football_data_average_market_proxy | 3.35/4.22/1.86
- 2026-05-16 14:30 | Freiburg vs RB Leipzig | football_data_bet365_proxy | 2.7/4.0/2.3
- 2026-05-16 14:30 | Freiburg vs RB Leipzig | football_data_max_market_proxy | 2.75/4.0/2.37

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 991
Fixture team rows unmatched: 1862
Ready for model-fixture join: False
Automatic forward price rows: 357
odds-api.io price rows: 41
Football-Data price rows: 316
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. FC Heidenheim | suggestion=Heidenheim | type=suggested_alias_needed
- FSV Mainz | suggestion=nan | type=unmatched
- 1. FC Slovacko Uherske Hradiste | suggestion=nan | type=unmatched
- FK Mlada Boleslav | suggestion=nan | type=unmatched
- A-Xiii Auhof Center | suggestion=nan | type=unmatched
- WAF Vorwarts Brigittenau | suggestion=nan | type=unmatched
- ABC FC RN | suggestion=nan | type=unmatched
- Sousa EC PB | suggestion=nan | type=unmatched
- AC Goianiense GO | suggestion=nan | type=unmatched
- Cerrado EC GO | suggestion=nan | type=unmatched
- AC Oulu | suggestion=nan | type=unmatched
- Turun Palloseura | suggestion=nan | type=unmatched
- AC Virtus | suggestion=nan | type=unmatched
- SP La Fiorita | suggestion=nan | type=unmatched
- Academica de Coimbra | suggestion=nan | type=unmatched
- CD Trofense | suggestion=nan | type=unmatched
- ACV Assen | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 357
Value snapshot rows: 615
Matches with any automatic price: 69
Matches with fresh API price: 41
Matches with odds-api.io price: 41
Fresh API match coverage rate: 0.1367
odds-api.io match coverage rate: 0.1367
Real-money ready: False
## Match coverage
- 2026-05-16 | Celtic vs Hearts | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Falkirk vs Rangers | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Hibernian vs Motherwell | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | Sociedad B vs Mirandes | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-16 | 1. FC Heidenheim vs FSV Mainz | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | ACV Assen vs Koninklijke HFC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | ADO 20 Heemskerk vs VV Scherpenzeel | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Bayer Leverkusen vs Hamburger SV | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Borussia Monchengladbach vs TSG Hoffenheim | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | FC Chernomorets Odessa vs FC Livyi Bereh Kyiv | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Eintracht Frankfurt vs VfB Stuttgart | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Excelsior Maassluis vs Jong Almere City FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | HHC Hardenberg vs Kozakken Boys Werkendam | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Hoek vs Rijnsburgse Boys | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Jong Sparta Rotterdam vs De Treffers Groesbeek | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-16 | K.v.v. Quick Boys vs IJsselmeervogels | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 357
Matched prediction rows: 87
Value snapshot rows: 615
odds-api.io snapshot rows: 147
Baseline snapshot rows: 513
Full model snapshot rows: 102
Positive EV rows: 312
Source counts: {'football_data_max_market_proxy': 162, 'football_data_average_market_proxy': 162, 'odds_api_io_Bet365_ML': 147, 'football_data_bet365_proxy': 144}
- 2026-05-16 | CE Carroi vs Inter Club de Escaldes | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3772 | EV=5.4124 | match=1.0
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=16.0 | prob=0.3488 | EV=4.5808 | match=0.7308
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=14.0 | prob=0.3488 | EV=3.8832 | match=0.7308
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.84 | prob=0.3488 | EV=3.478592 | match=0.7308
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=16.0 | prob=0.2402 | EV=2.8432 | match=1.0
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-16 | Porto vs Santa Clara | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=10.25 | prob=0.3488 | EV=2.5752 | match=1.0
- 2026-05-16 | FC Porto vs Santa Clara Azores | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=10.25 | prob=0.3488 | EV=2.5752 | match=0.96
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=14.0 | prob=0.2402 | EV=2.3628 | match=1.0
- 2026-05-16 | Bayer Leverkusen vs Hamburger SV | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=0.92
- 2026-05-16 | Bayer Leverkusen vs Hamburger SV | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=0.92
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.84 | prob=0.2402 | EV=2.084168 | match=1.0
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.83 | prob=0.3488 | EV=2.079904 | match=1.0
- 2026-05-16 | Bayer Leverkusen vs Hamburger SV | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.83 | prob=0.3488 | EV=2.079904 | match=0.92
- 2026-05-16 | FC Porto vs Santa Clara Azores | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.82 | prob=0.3488 | EV=2.076416 | match=0.96

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 615
Pre-dedupe proxy candidate observation rows: 241
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-16 | SV Meerssen vs FC Rijnvogels | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-16 | Heidenheim vs Mainz | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3743 | EV=0.27262 | edge=0.080182 | penalty=0.2726184728578327 | tier=proxy_watchlist | score=0.25
- 2026-05-16 | Werder Bremen vs Borussia Dortmund | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-16 | Eintracht Frankfurt vs VfB Stuttgart | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-16 | Ein Frankfurt vs Stuttgart | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3716 | EV=0.18912 | edge=0.0591 | penalty=0.18911999999999995 | tier=proxy_watchlist | score=0.2415
- 2026-05-16 | KV Vesturbaer vs Hottur/Huginn | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-16 | FC Irtysh Pavlodar vs FC Yelimai | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-16 | Falkirk vs Rangers | selection=HOME | source=football_data_average_market_proxy | odds=3.82 | prob=0.3772 | EV=0.440904 | edge=0.11542 | penalty=0.44090457636183045 | tier=proxy_watchlist | score=0.2276
- 2026-05-16 | AD Ceuta vs Malaga CF | selection=HOME | source=football_data_bet365_proxy | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2257
- 2026-05-16 | Ceuta vs Malaga | selection=HOME | source=football_data_bet365_proxy | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2257
- 2026-05-16 | Sociedad B vs Mirandes | selection=HOME | source=football_data_max_market_proxy | odds=3.35 | prob=0.3772 | EV=0.26362 | edge=0.078693 | penalty=0.2636219586140356 | tier=proxy_watchlist | score=0.2139
- 2026-05-16 | Standard Liege vs KRC Genk | selection=HOME | source=football_data_max_market_proxy | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2091

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
- ev_above_real_candidate_cap_possible_overconfidence: 10
- market_alignment_penalty_too_high_for_real_candidate: 10
- delayed_football_data_proxy_not_fresh_api_price: 5
- watchlist_only_pending_forward_settlement: 2
## Row explanations
- 2026-05-16 | SV Meerssen vs FC Rijnvogels | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Heidenheim vs Mainz | sel=AWAY | score=0.25 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Werder Bremen vs Borussia Dortmund | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Eintracht Frankfurt vs VfB Stuttgart | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Ein Frankfurt vs Stuttgart | sel=HOME | score=0.2415 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | KV Vesturbaer vs Hottur/Huginn | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | FC Irtysh Pavlodar vs FC Yelimai | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | Falkirk vs Rangers | sel=HOME | score=0.2276 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-16 | AD Ceuta vs Malaga CF | sel=HOME | score=0.2257 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-16 | Ceuta vs Malaga | sel=HOME | score=0.2257 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-16 | Sociedad B vs Mirandes | sel=HOME | score=0.2139 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-16 | Standard Liege vs KRC Genk | sel=HOME | score=0.2091 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 615
Paper proxy observation rows: 25
Positive EV value rows: 312
Suppressed-band observation rows: 0
Distinct matches: 14
Distinct sources: 0
Max EV: 0.747488
Average EV: 0.379347
Max probability edge: 0.154978
Average match confidence: None
## By selection
- away: rows=11, avg_ev=0.5618, max_ev=0.7475
- draw: rows=8, avg_ev=0.113, max_ev=0.2208
- home: rows=6, avg_ev=0.4, max_ev=0.6974

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 991
Forward fixture prediction rows: 300
Full model prediction rows: 9
Baseline prediction rows: 291
Max forward predictions: 300
Ready for price join: True
- 2026-05-16 12:30 | Celtic vs Hearts | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 12:30 | Falkirk vs Rangers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 12:30 | Hibernian vs Motherwell | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:00 | Sociedad B vs Mirandes | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | ADO 20 Heemskerk vs VV Scherpenzeel | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | Bayer Leverkusen vs Hamburger SV | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | Borussia Monchengladbach vs TSG Hoffenheim | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | FC Chernomorets Odessa vs FC Livyi Bereh Kyiv | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | Eintracht Frankfurt vs VfB Stuttgart | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | Excelsior Maassluis vs Jong Almere City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | HHC Hardenberg vs Kozakken Boys Werkendam | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | Hoek vs Rijnsburgse Boys | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | Jong Sparta Rotterdam vs De Treffers Groesbeek | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | K.v.v. Quick Boys vs IJsselmeervogels | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | Rkav Volendam vs BVV Barendrecht | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | SC Freiburg vs RB Leipzig | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | FC St. Pauli vs VFL Wolfsburg | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 13:30 | SV Meerssen vs FC Rijnvogels | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 1442
Log type: probability_only_no_market_prices
- 2026-05-16 2026-05-16 18:00:00 | Belgrano de Cordoba vs Boca Juniors | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | Blumenau EC SC vs CN Marcilio Dias SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | Bonsucesso FC RJ vs Audax Rio EC RJ | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | Botafogo FR RJ vs Cruzeiro EC MG | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | CA Juventud de Las Piedras vs CA Progreso | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | Casa Pia vs Rio Ave | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | CR Vasco da Gama RJ vs Rio Negro RR | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | Criciuma EC SC vs Fluminense FC RJ | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | CSDC Alianza Universidad vs CD Estudiantil Cni | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | Defensor SC Montevideo vs CA Penarol Montevideo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | Deportivo Camioneros vs CA Brown de Adrogue | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | FC Dinamo Bucuresti 1948 vs FC CFR 1907 Cluj | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | Doce Mel EC BA vs Perolas Negras RJ | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | EC Juventude RS vs CR Flamengo RJ | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | FBC Melgar vs Sport Huancayo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | FK Bokelj Kotor vs FK Arsenal Tivat | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | FK Buducnost vs FK Mornar Bar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | FK Javor Ivanjica vs FK Mladost Lucani | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | FK Jezero Plav vs OFK Mladost DG | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 18:00:00 | FK Napredak Krusevac vs FK Radnicki 1923 Kragujevac | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 991
Manual template rows: 991
Rows with complete manual odds: 0
Rows missing manual odds: 991
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz
- 2026-05-16 15:00 | 1. FC Slovacko Uherske Hradiste vs FK Mlada Boleslav
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau
- 2026-05-16 19:00 | ABC FC RN vs Sousa EC PB
- 2026-05-16 18:30 | AC Goianiense GO vs Cerrado EC GO
- 2026-05-16 16:00 | AC Oulu vs Turun Palloseura
- 2026-05-16 15:00 | AC Virtus vs SP La Fiorita
- 2026-05-16 15:30 | Academica de Coimbra vs CD Trofense
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC
- 2026-05-16 19:00 | AD Alcorcon vs Marbella FC
- 2026-05-16 18:00 | AD Cabofriense RJ vs Serrano FC RJ
- 2026-05-16 14:15 | AD Ceuta vs Malaga CF
- 2026-05-16 20:00 | AD Comerciantes FC vs Deportivo Binacional FC
- 2026-05-16 13:30 | ADO 20 Heemskerk vs VV Scherpenzeel
- 2026-05-16 16:00 | AE Larissa FC vs Atromitos Athinon

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 991
Source counts: {'odds_api_io_events_bookmaker_filtered': 883, 'football_data_fixtures_proxy': 107, 'odds_api_io_events_search': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz | germany-bundesliga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:00 | 1. FC Slovacko Uherske Hradiste vs FK Mlada Boleslav | czechia-1-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau | austria-amateur-wien-wiener-stadtliga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 19:00 | ABC FC RN vs Sousa EC PB | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-16 18:30 | AC Goianiense GO vs Cerrado EC GO | brazil-u20-goiano-1-divisao | odds_api_io_events_bookmaker_filtered
- 2026-05-16 16:00 | AC Oulu vs Turun Palloseura | finland-veikkausliiga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:00 | AC Virtus vs SP La Fiorita | san-marino-campionato-sammarinese | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:30 | Academica de Coimbra vs CD Trofense | portugal-liga-portugal-3 | odds_api_io_events_bookmaker_filtered
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC | netherlands-tweede-divisie | odds_api_io_events_bookmaker_filtered
- 2026-05-16 19:00 | AD Alcorcon vs Marbella FC | spain-primera-federacion | odds_api_io_events_bookmaker_filtered
- 2026-05-16 18:00 | AD Cabofriense RJ vs Serrano FC RJ | brazil-carioca-serie-a2 | odds_api_io_events_bookmaker_filtered
- 2026-05-16 14:15 | AD Ceuta vs Malaga CF | spain-laliga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-16 20:00 | AD Comerciantes FC vs Deportivo Binacional FC | peru-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-16 13:30 | ADO 20 Heemskerk vs VV Scherpenzeel | netherlands-derde-divisie | odds_api_io_events_bookmaker_filtered
- 2026-05-16 16:00 | AE Larissa FC vs Atromitos Athinon | greece-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:00 | AEK Larnaca vs Pafos FC | cyprus-1st-division | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:30 | AFK Csikszereda Miercurea Ciuc vs FC Botosani | romania-superliga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 18:00 | Al Ahli Saudi FC vs Al-Kholood | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:30 | Al Ain FC vs Dibba Al Fujairah | united-arab-emirates-arabian-gulf-league | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:30 | Al Dhafra SSC vs Al Wahda FC (UAE) | united-arab-emirates-arabian-gulf-league | odds_api_io_events_bookmaker_filtered
- 2026-05-16 16:05 | Al Hilal SFC vs Neom SC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-16 14:10 | AL Ittihad Kalba vs AL Wasl | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:30 | Al Jazira (UAE) vs Baniyas Club | united-arab-emirates-arabian-gulf-league | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 991
Rows with complete odds: 0
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz | bookmaker=bet365_manual
- 2026-05-16 15:00 | 1. FC Slovacko Uherske Hradiste vs FK Mlada Boleslav | bookmaker=bet365_manual
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau | bookmaker=bet365_manual
- 2026-05-16 19:00 | ABC FC RN vs Sousa EC PB | bookmaker=bet365_manual
- 2026-05-16 18:30 | AC Goianiense GO vs Cerrado EC GO | bookmaker=bet365_manual
- 2026-05-16 16:00 | AC Oulu vs Turun Palloseura | bookmaker=bet365_manual
- 2026-05-16 15:00 | AC Virtus vs SP La Fiorita | bookmaker=bet365_manual
- 2026-05-16 15:30 | Academica de Coimbra vs CD Trofense | bookmaker=bet365_manual
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC | bookmaker=bet365_manual
- 2026-05-16 19:00 | AD Alcorcon vs Marbella FC | bookmaker=bet365_manual
- 2026-05-16 18:00 | AD Cabofriense RJ vs Serrano FC RJ | bookmaker=bet365_manual
- 2026-05-16 14:15 | AD Ceuta vs Malaga CF | bookmaker=bet365_manual
- 2026-05-16 20:00 | AD Comerciantes FC vs Deportivo Binacional FC | bookmaker=bet365_manual
- 2026-05-16 13:30 | ADO 20 Heemskerk vs VV Scherpenzeel | bookmaker=bet365_manual
- 2026-05-16 16:00 | AE Larissa FC vs Atromitos Athinon | bookmaker=bet365_manual
- 2026-05-16 15:00 | AEK Larnaca vs Pafos FC | bookmaker=bet365_manual
- 2026-05-16 15:30 | AFK Csikszereda Miercurea Ciuc vs FC Botosani | bookmaker=bet365_manual
- 2026-05-16 18:00 | Al Ahli Saudi FC vs Al-Kholood | bookmaker=bet365_manual
- 2026-05-16 15:30 | Al Ain FC vs Dibba Al Fujairah | bookmaker=bet365_manual
- 2026-05-16 15:30 | Al Dhafra SSC vs Al Wahda FC (UAE) | bookmaker=bet365_manual
- 2026-05-16 16:05 | Al Hilal SFC vs Neom SC | bookmaker=bet365_manual
- 2026-05-16 14:10 | AL Ittihad Kalba vs AL Wasl | bookmaker=bet365_manual
- 2026-05-16 15:30 | Al Jazira (UAE) vs Baniyas Club | bookmaker=bet365_manual
- 2026-05-16 17:45 | Al Nassr Club vs Gamba Osaka | bookmaker=bet365_manual

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
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz
- 2026-05-16 15:00 | 1. FC Slovacko Uherske Hradiste vs FK Mlada Boleslav
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau
- 2026-05-16 19:00 | ABC FC RN vs Sousa EC PB
- 2026-05-16 18:30 | AC Goianiense GO vs Cerrado EC GO
- 2026-05-16 16:00 | AC Oulu vs Turun Palloseura
- 2026-05-16 15:00 | AC Virtus vs SP La Fiorita
- 2026-05-16 15:30 | Academica de Coimbra vs CD Trofense
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC
- 2026-05-16 19:00 | AD Alcorcon vs Marbella FC
- 2026-05-16 18:00 | AD Cabofriense RJ vs Serrano FC RJ
- 2026-05-16 14:15 | AD Ceuta vs Malaga CF
- 2026-05-16 20:00 | AD Comerciantes FC vs Deportivo Binacional FC
- 2026-05-16 13:30 | ADO 20 Heemskerk vs VV Scherpenzeel
- 2026-05-16 16:00 | AE Larissa FC vs Atromitos Athinon
- 2026-05-16 15:00 | AEK Larnaca vs Pafos FC
- 2026-05-16 15:30 | AFK Csikszereda Miercurea Ciuc vs FC Botosani
- 2026-05-16 18:00 | Al Ahli Saudi FC vs Al-Kholood
- 2026-05-16 15:30 | Al Ain FC vs Dibba Al Fujairah

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 251
Valid forward/proxy log rows: 248
Deduped forward/proxy observation rows: 168
Duplicate forward/proxy log rows: 80
Valid automatic proxy observation rows: 248
Deduped automatic proxy observation rows: 168
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-15 | Caboolture Sports FC vs North Star | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061
- 2026-05-15 | Caboolture FC vs North Star FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.061
- 2026-05-16 | Real Sociedad San Sebastian B vs CD Mirandes | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0606
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
### Werder Bremen vs Dortmund
- Date/time: 2026-05-16 14:30
- League/phase: bundesliga / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 3.5
- Fair odds: 2.87
- Model probability: 0.3487
- Probability band: 0.25-0.35
- EV: 0.2205
- Probability edge: 0.063
- Alignment penalty: 0.2205
- Suppression action: none
- Paper tier: priority_proxy_observation
- Paper score: 0.2605
- Prediction ID: 2a7a0850586d4950c2d1
### Werder Bremen vs Dortmund
- Date/time: 2026-05-16 14:30
- League/phase: bundesliga / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 3.5
- Fair odds: 2.87
- Model probability: 0.3487
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
Newly logged paper-test picks: 23
Total logged paper-test rows: 251
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 615, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 301, 'current_paper_picks': 25, 'newly_logged_picks': 23, 'total_logged_paper_rows': 251, 'source_used': 'automatic_forward_value_snapshots'}
- Werder Bremen vs Dortmund | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3487 | EV=0.2205 | edge=0.063 | penalty=0.2205 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Werder Bremen vs Dortmund | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3487 | EV=0.2205 | edge=0.063 | penalty=0.2205 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Almeria vs Las Palmas | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3314 | EV=0.193 | edge=0.0536 | penalty=0.193 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Almeria vs Las Palmas | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3314 | EV=0.193 | edge=0.0536 | penalty=0.193 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Heidenheim vs Mainz | coverage=full_team_strength_match | selection=AWAY | odds=3.5 | prob=0.3743 | EV=0.31 | edge=0.0886 | penalty=0.3101 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3716 | EV=0.3006 | edge=0.0859 | penalty=0.3006 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- M'gladbach vs Hoffenheim | coverage=full_team_strength_match | selection=DRAW | odds=4.75 | prob=0.257 | EV=0.2208 | edge=0.0465 | penalty=0.2208 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Heidenheim vs Mainz | coverage=full_team_strength_match | selection=AWAY | odds=3.4 | prob=0.3743 | EV=0.2726 | edge=0.0802 | penalty=0.2726 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | selection=HOME | odds=3.4 | prob=0.3716 | EV=0.2634 | edge=0.0775 | penalty=0.2634 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- M'gladbach vs Hoffenheim | coverage=full_team_strength_match | selection=DRAW | odds=4.5 | prob=0.257 | EV=0.1565 | edge=0.0348 | penalty=0.1565 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Freiburg vs RB Leipzig | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2767 | EV=0.1068 | edge=0.0267 | penalty=0.1068 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Freiburg vs RB Leipzig | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2767 | EV=0.1068 | edge=0.0267 | penalty=0.1068 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Union Berlin vs Augsburg | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2746 | EV=0.0984 | edge=0.0246 | penalty=0.0984 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- St Pauli vs Wolfsburg | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2858 | EV=0.0717 | edge=0.0191 | penalty=0.0717 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- St Pauli vs Wolfsburg | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2858 | EV=0.0717 | edge=0.0191 | penalty=0.0717 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Union Berlin vs Augsburg | coverage=full_team_strength_match | selection=DRAW | odds=3.9 | prob=0.2746 | EV=0.0709 | edge=0.0182 | penalty=0.0709 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Chelsea FC vs Manchester City | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Celtic vs Hearts | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.01 | prob=0.3488 | EV=0.7475 | edge=0.1492 | penalty=0.7475 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
