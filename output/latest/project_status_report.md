# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-12T07:30:24.992330+00:00`
GitHub run: `321` attempt `1`
GitHub SHA: `ab11592b75009650b2d15ffc9db60a455d429abf`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 19 |  |  |
| odds-api.io forward fixtures | True | 162 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 57 |  |  |
| Forward price coverage report | True | 160 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 5 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 160 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 160
- Automatic value snapshots: 441
- Positive EV proxy rows: 204
- Proxy observation rows: 7
- Valid forward/proxy log rows: 54
- Deduped forward/proxy log rows: 30
- Duplicate forward/proxy log rows identified: 24
- Fresh API match coverage rate: 0.1437
- Matches with fresh API price: 23
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
Current: 441 value snapshots; fresh API coverage rate 0.1437.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 30 deduped forward/proxy rows; 24 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 26
Upcoming fixture rows: 26
Proxy price rows: 78
Sources attempted: 1
Errors: 0
- 2026-05-13 20:00 | Man City vs Crystal Palace | football_data_bet365_proxy | 1.2/7.5/12.0
- 2026-05-13 20:00 | Man City vs Crystal Palace | football_data_max_market_proxy | 1.22/7.5/15.0
- 2026-05-13 20:00 | Man City vs Crystal Palace | football_data_average_market_proxy | 1.19/7.03/12.75
- 2026-05-13 18:00 | Brest vs Strasbourg | football_data_bet365_proxy | 2.63/3.6/2.5
- 2026-05-13 18:00 | Brest vs Strasbourg | football_data_max_market_proxy | 2.8/3.6/2.5
- 2026-05-13 18:00 | Brest vs Strasbourg | football_data_average_market_proxy | 2.68/3.47/2.42
- 2026-05-13 20:00 | Lens vs Paris SG | football_data_bet365_proxy | 3.4/4.0/1.95
- 2026-05-13 20:00 | Lens vs Paris SG | football_data_max_market_proxy | 3.5/4.0/2.05
- 2026-05-13 20:00 | Lens vs Paris SG | football_data_average_market_proxy | 3.3/3.91/1.95
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos | football_data_bet365_proxy | 1.76/3.3/5.0
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos | football_data_max_market_proxy | 1.86/3.5/5.0
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos | football_data_average_market_proxy | 1.78/3.31/4.36
- 2026-05-12 17:00 | Kifisia vs Atromitos | football_data_bet365_proxy | 2.3/3.25/3.1
- 2026-05-12 17:00 | Kifisia vs Atromitos | football_data_max_market_proxy | 2.3/3.4/3.1
- 2026-05-12 17:00 | Kifisia vs Atromitos | football_data_average_market_proxy | 2.24/3.23/2.95
- 2026-05-12 17:00 | Panetolikos vs Larisa | football_data_bet365_proxy | 2.1/3.1/3.1
- 2026-05-12 17:00 | Panetolikos vs Larisa | football_data_max_market_proxy | 2.28/3.2/3.33
- 2026-05-12 17:00 | Panetolikos vs Larisa | football_data_average_market_proxy | 2.21/3.08/3.13
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_bet365_proxy | 1.57/4.2/5.0
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_max_market_proxy | 1.68/4.2/5.0
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_average_market_proxy | 1.6/3.89/4.66
- 2026-05-13 15:00 | Volos NFC vs Aris | football_data_bet365_proxy | 4.33/3.2/1.91
- 2026-05-13 15:00 | Volos NFC vs Aris | football_data_max_market_proxy | 4.33/3.6/2.05

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 173
Fixture team rows unmatched: 315
Ready for model-fixture join: False
Automatic forward price rows: 101
odds-api.io price rows: 23
Football-Data price rows: 78
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. FC Slovacko Uherske Hradiste | suggestion=nan | type=unmatched
- FC Banik Ostrava | suggestion=nan | type=unmatched
- Aberdeen | suggestion=nan | type=unmatched
- St Mirren | suggestion=nan | type=unmatched
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
Forward prediction rows: 160
Automatic price rows: 101
Value snapshot rows: 441
Matches with any automatic price: 46
Matches with fresh API price: 23
Matches with odds-api.io price: 23
Fresh API match coverage rate: 0.1437
odds-api.io match coverage rate: 0.1437
Real-money ready: False
## Match coverage
- 2026-05-12 | Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | Singida Black Stars SC vs Namungo FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Murdoch University Melville FC Reserves vs Joondalup City FC Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | Fardu Ferghana vs Xorazm Fk Urganch | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Deportivo Maldonado Reserve vs Racing Club Montevideo | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | Namdhari FC vs Gokulam Kerala FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | TRA United vs Jkt Tanzania | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Sur SC vs Al-Khaboora | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | El Gouna FC vs Kahrabaa Ismailia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | FC Inter Turku vs JS Hercules | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Mohun Bagan Super Giant vs Inter Kashi FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Pharco FC vs Modern Sport FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | URA FC vs Calvary | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | AL Ittihad Kalba vs AL Nasr | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | AL Wasl vs AL Jazira | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-12 | PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 160
Proxy price rows: 101
Matched prediction rows: 63
Value snapshot rows: 441
odds-api.io snapshot rows: 72
Baseline snapshot rows: 441
Full model snapshot rows: 0
Positive EV rows: 204
Source counts: {'football_data_bet365_proxy': 123, 'football_data_max_market_proxy': 123, 'football_data_average_market_proxy': 123, 'odds_api_io_Bet365_ML': 72}
- 2026-05-12 | FC Elva vs Paide Linnameeskond | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=1.0
- 2026-05-12 | FC Inter Turku vs JS Hercules | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3488 | EV=10.8592 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-05-12 | FC Inter Turku vs JS Hercules | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.274 | EV=4.206 | match=1.0
- 2026-05-12 | Mohun Bagan Super Giant vs Inter Kashi FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=0.96
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-12 | FC Elva vs Paide Linnameeskond | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.7814
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 441
Pre-dedupe proxy candidate observation rows: 145
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-12 | Pharco FC vs Modern Sport FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-13 | Volos NPS vs Aris Thessaloniki | selection=HOME | source=football_data_average_market_proxy | odds=3.57 | prob=0.3772 | EV=0.346604 | edge=0.097088 | penalty=0.3466042154566742 | tier=proxy_watchlist | score=0.2205
- 2026-05-13 | Volos NFC vs Aris | selection=HOME | source=football_data_average_market_proxy | odds=3.57 | prob=0.3772 | EV=0.346604 | edge=0.097088 | penalty=0.3466042154566742 | tier=proxy_watchlist | score=0.2205
- 2026-05-13 | Racing Club De Lens vs Paris Saint-Germain | selection=HOME | source=football_data_max_market_proxy | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2184
- 2026-05-13 | Lens vs Paris SG | selection=HOME | source=football_data_max_market_proxy | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2184
- 2026-05-13 | Deportivo Alaves vs FC Barcelona | selection=HOME | source=football_data_max_market_proxy | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2091
- 2026-05-13 | Alaves vs Barcelona | selection=HOME | source=football_data_max_market_proxy | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2091
- 2026-05-13 | Stade Brest 29 vs Strasbourg Alsace | selection=HOME | source=football_data_max_market_proxy | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.195
- 2026-05-13 | Brest vs Strasbourg | selection=HOME | source=football_data_max_market_proxy | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.195
- 2026-05-13 | Espanyol Barcelona vs Athletic Bilbao | selection=HOME | source=football_data_max_market_proxy | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.1911
- 2026-05-13 | Espanol vs Ath Bilbao | selection=HOME | source=football_data_max_market_proxy | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.1911
- 2026-05-13 | Motherwell FC vs Celtic Glasgow | selection=HOME | source=football_data_bet365_proxy | odds=4.33 | prob=0.3772 | EV=0.633276 | edge=0.146253 | penalty=0.6332751670296646 | tier=proxy_watchlist | score=0.1905

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 4
Top blocker: delayed_football_data_proxy_not_fresh_api_price
Real-money ready: False
## Blocker summary
- delayed_football_data_proxy_not_fresh_api_price: 11
- ev_above_real_candidate_cap_possible_overconfidence: 8
- market_alignment_penalty_too_high_for_real_candidate: 8
- edge_below_candidate_threshold: 2
## Row explanations
- 2026-05-12 | Pharco FC vs Modern Sport FC | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-13 | Volos NPS vs Aris Thessaloniki | sel=HOME | score=0.2205 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Volos NFC vs Aris | sel=HOME | score=0.2205 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Racing Club De Lens vs Paris Saint-Germain | sel=HOME | score=0.2184 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Lens vs Paris SG | sel=HOME | score=0.2184 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Deportivo Alaves vs FC Barcelona | sel=HOME | score=0.2091 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Alaves vs Barcelona | sel=HOME | score=0.2091 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Stade Brest 29 vs Strasbourg Alsace | sel=HOME | score=0.195 | blockers=delayed_football_data_proxy_not_fresh_api_price | improve=prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Brest vs Strasbourg | sel=HOME | score=0.195 | blockers=delayed_football_data_proxy_not_fresh_api_price | improve=prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Espanyol Barcelona vs Athletic Bilbao | sel=HOME | score=0.1911 | blockers=edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Espanol vs Ath Bilbao | sel=HOME | score=0.1911 | blockers=edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Motherwell FC vs Celtic Glasgow | sel=HOME | score=0.1905 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 441
Paper proxy observation rows: 7
Positive EV value rows: 204
Suppressed-band observation rows: 7
Distinct matches: 4
Distinct sources: 0
Max EV: 0.524256
Average EV: 0.492864
Max probability edge: 0.119967
Average match confidence: None
## By selection
- away: rows=7, avg_ev=0.4929, max_ev=0.5243

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 173
Forward fixture prediction rows: 160
Full model prediction rows: 0
Baseline prediction rows: 160
Max forward predictions: 160
Ready for price join: True
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
- 2026-05-12 14:00 | FC Inter Turku vs JS Hercules | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 14:00 | Mohun Bagan Super Giant vs Inter Kashi FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 14:00 | Pharco FC vs Modern Sport FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 14:00 | URA FC vs Calvary | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 14:10 | AL Wasl vs AL Jazira | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 14:45 | PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 15:00 | FK Liepaja vs Ogre United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 15:00 | JS Omrane vs Avenir S Marsa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 15:00 | FC Metalist 1925 Kharkiv vs Karpaty Lviv | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 160
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 224
Log type: probability_only_no_market_prices
- 2026-05-12 2026-05-12 18:00:00 | Celta vs Levante | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 19:00:00 | Betis vs Elche | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 19:45:00 | Aberdeen vs St Mirren | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 19:45:00 | Dundee United vs Livingston | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 19:45:00 | Kilmarnock vs Dundee | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-12 20:30:00 | Osasuna vs Ath Madrid | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 15:00:00 | Levadeiakos vs OFI Crete | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 15:00:00 | Volos NFC vs Aris | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 17:30:00 | Olympiakos vs Panathinaikos | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 17:30:00 | PAOK vs AEK | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 18:00:00 | Brest vs Strasbourg | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 18:00:00 | Espanol vs Ath Bilbao | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 18:00:00 | Villarreal vs Sevilla | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 20:00:00 | Hearts vs Falkirk | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 20:00:00 | Lens vs Paris SG | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 20:00:00 | Man City vs Crystal Palace | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 20:00:00 | Motherwell vs Celtic | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 20:00:00 | Rangers vs Hibernian | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 20:30:00 | Alaves vs Barcelona | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 20:30:00 | Getafe vs Mallorca | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 173
Manual template rows: 173
Rows with complete manual odds: 0
Rows missing manual odds: 173
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava
- 2026-05-12 19:45 | Aberdeen vs St Mirren
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr
- 2026-05-12 18:00 | Al Nassr Club vs Al Hilal SFC
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan
- 2026-05-12 14:10 | AL Wasl vs AL Jazira
- 2026-05-12 16:20 | Al-Kholood vs Al-Okhdood Club
- 2026-05-12 16:20 | Al-Rustaq vs Ibri
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota.
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC
- 2026-05-12 17:30 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 173
Source counts: {'odds_api_io_events_bookmaker_filtered': 144, 'football_data_fixtures_proxy': 26, 'odds_api_io_events_search': 2, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | czechia-1-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-12 19:45 | Aberdeen vs St Mirren | SC0 | football_data_fixtures_proxy
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon | greece-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC | jordan-jordan-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat | jordan-jordan-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 18:00 | Al Nassr Club vs Al Hilal SFC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 14:10 | AL Wasl vs AL Jazira | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 16:20 | Al-Kholood vs Al-Okhdood Club | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 16:20 | Al-Rustaq vs Ibri | oman-omani-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos | G1 | football_data_fixtures_proxy
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota. | colombia-primera-a-apertura | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:30 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC | israel-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 19:00 | Betis vs Elche | la_liga | football_data_fixtures_proxy
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride | usa-national-womens-soccer-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:15 | Botev Plovdiv vs FC Arda Kardzhali | bulgaria-parva-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe | argentina-liga-profesional | odds_api_io_events_bookmaker_filtered
- 2026-05-12 19:30 | CA Osasuna vs Atletico Madrid | spain-laliga | odds_api_io_events_bookmaker_filtered
- 2026-05-12 20:00 | CD Real Santander vs Boca Juniors de Cali | colombia-copa-colombia | odds_api_io_events_bookmaker_filtered
- 2026-05-12 18:00 | Celta vs Levante | la_liga | football_data_fixtures_proxy
- 2026-05-12 17:00 | Central Espanol Reserve vs Defensor Sporting | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 173
Rows with complete odds: 0
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | bookmaker=bet365_manual
- 2026-05-12 19:45 | Aberdeen vs St Mirren | bookmaker=bet365_manual
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon | bookmaker=bet365_manual
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC | bookmaker=bet365_manual
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat | bookmaker=bet365_manual
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr | bookmaker=bet365_manual
- 2026-05-12 18:00 | Al Nassr Club vs Al Hilal SFC | bookmaker=bet365_manual
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan | bookmaker=bet365_manual
- 2026-05-12 14:10 | AL Wasl vs AL Jazira | bookmaker=bet365_manual
- 2026-05-12 16:20 | Al-Kholood vs Al-Okhdood Club | bookmaker=bet365_manual
- 2026-05-12 16:20 | Al-Rustaq vs Ibri | bookmaker=bet365_manual
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos | bookmaker=bet365_manual
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota. | bookmaker=bet365_manual
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC | bookmaker=bet365_manual
- 2026-05-12 17:30 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC | bookmaker=bet365_manual
- 2026-05-12 19:00 | Betis vs Elche | bookmaker=bet365_manual
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride | bookmaker=bet365_manual
- 2026-05-12 17:15 | Botev Plovdiv vs FC Arda Kardzhali | bookmaker=bet365_manual
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe | bookmaker=bet365_manual
- 2026-05-12 19:30 | CA Osasuna vs Atletico Madrid | bookmaker=bet365_manual
- 2026-05-12 20:00 | CD Real Santander vs Boca Juniors de Cali | bookmaker=bet365_manual
- 2026-05-12 18:00 | Celta vs Levante | bookmaker=bet365_manual
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
- 2026-05-12 19:45 | Aberdeen vs St Mirren
- 2026-05-12 16:00 | AE Kifisia FC vs Atromitos Athinon
- 2026-05-12 15:00 | AL Faisaly (Jor) vs Ramtha SC
- 2026-05-12 17:30 | Al Hussein Irbid vs Al Wehdat
- 2026-05-12 14:10 | AL Ittihad Kalba vs AL Nasr
- 2026-05-12 18:00 | Al Nassr Club vs Al Hilal SFC
- 2026-05-12 15:30 | AL Wahda FC vs Khorfakkan
- 2026-05-12 14:10 | AL Wasl vs AL Jazira
- 2026-05-12 16:20 | Al-Kholood vs Al-Okhdood Club
- 2026-05-12 16:20 | Al-Rustaq vs Ibri
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota.
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC
- 2026-05-12 17:30 | Beitar Jerusalem FC vs Hapoel Be`er Sheva FC
- 2026-05-12 19:00 | Betis vs Elche
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride
- 2026-05-12 17:15 | Botev Plovdiv vs FC Arda Kardzhali
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 57
Valid forward/proxy log rows: 54
Deduped forward/proxy observation rows: 30
Duplicate forward/proxy log rows: 24
Valid automatic proxy observation rows: 54
Deduped automatic proxy observation rows: 30
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-11 | Napoli vs Bologna | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.12610000000000002
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1247
- 2026-05-11 | Vallecano vs Girona | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1245
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1216
- 2026-05-12 | Dundee United vs Livingston | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0748
- 2026-05-12 | Asteras Tripolis vs Panserraikos | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0747
- 2026-05-12 | Sur SC vs Al-Khaboora | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0746
- 2026-05-12 | Celta vs Levante | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0746
- 2026-05-12 | RC Celta de Vigo vs Levante UD | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0746
- 2026-05-12 | PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0742
- 2026-05-12 | TRA United vs Jkt Tanzania | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0716
- 2026-05-12 | AL Wasl vs AL Jazira | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0711
- 2026-05-12 | Sportivo Ameliano vs Deportivo Recoleta Reserve | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0711
- 2026-05-12 | AL Ittihad Kalba vs AL Nasr | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.07060000000000001
- 2026-05-12 | El Gouna FC vs Kahrabaa Ismailia | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.07060000000000001
- 2026-05-12 | URA FC vs Calvary | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0693
- 2026-05-12 | Gwangju FC vs FC Seoul | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0684
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.06810000000000001
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.067
- 2026-05-12 | AL Faisaly (Jor) vs Ramtha SC | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.067

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
### Dundee United vs Livingston
- Date/time: 2026-05-12 19:45
- League/phase: SC0 / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.37
- Fair odds: 2.87
- Model probability: 0.3488
- Probability band: 0.00-0.35
- EV: 0.5243
- Probability edge: 0.12
- Alignment penalty: 0.5243
- Suppression action: proxy_suppressed_band_observe_only
- Paper tier: suppressed_band_proxy_observation
- Paper score: 0.0748
- Prediction ID: 2601f0b6cbd752ed0544
### Asteras Tripolis vs Panserraikos
- Date/time: 2026-05-12 17:00
- League/phase: G1 / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.36
- Fair odds: 2.87
- Model probability: 0.3488
- Probability band: 0.00-0.35

## paper_test_picks

# Paper Test Picks
Observation-only picks. These are not real-money recommendations.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Baseline coverage observations are not model signals. They exist only to test the pipeline and collect settlement evidence.
Suppressed historical bands may be tracked only as proxy observation and remain excluded from real-money readiness.
Source used: automatic_forward_value_snapshots
Current paper-test picks: 7
Newly logged paper-test picks: 7
Total logged paper-test rows: 57
- Dundee United vs Livingston | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.37 | prob=0.3488 | EV=0.5243 | edge=0.12 | penalty=0.5243 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Asteras Tripolis vs Panserraikos | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.36 | prob=0.3488 | EV=0.5208 | edge=0.1194 | penalty=0.5208 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Celta vs Levante | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5103 | edge=0.1179 | penalty=0.5103 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- RC Celta de Vigo vs Levante UD | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5103 | edge=0.1179 | penalty=0.5103 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Celta vs Levante | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- RC Celta de Vigo vs Levante UD | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- RC Celta de Vigo vs Levante UD | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.17 | prob=0.3488 | EV=0.4545 | edge=0.109 | penalty=0.4545 | band=0.00-0.35 | risk=baseline_coverage_only | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation

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
