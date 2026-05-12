# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-12T21:22:17.923057+00:00`
GitHub run: `335` attempt `1`
GitHub SHA: `220fbe16313a677b9e4dce84338019061c9b7ed8`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 26 |  |  |
| Football-Data upcoming odds proxy | True | 78 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 60 |  |  |
| odds-api.io forward fixtures | True | 117 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 597 |  |  |
| Forward price coverage report | True | 212 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 6 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 4 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 212 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 142
- Automatic value snapshots: 408
- Positive EV proxy rows: 205
- Proxy observation rows: 25
- Valid forward/proxy log rows: 96
- Deduped forward/proxy log rows: 49
- Duplicate forward/proxy log rows identified: 47
- Fresh API match coverage rate: 0.0704
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
Current: 408 value snapshots; fresh API coverage rate 0.0704.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 49 deduped forward/proxy rows; 47 duplicate raw rows identified.
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
Upcoming fixture rows: 142
Fixture team rows unmatched: 253
Ready for model-fixture join: False
Automatic forward price rows: 88
odds-api.io price rows: 10
Football-Data price rows: 78
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- Aberdeen | suggestion=nan | type=unmatched
- St Mirren | suggestion=nan | type=unmatched
- Asteras Tripolis | suggestion=nan | type=unmatched
- Panserraikos | suggestion=nan | type=unmatched
- Atletico Nacional Medellin | suggestion=nan | type=unmatched
- Internacional de Bogota. | suggestion=nan | type=unmatched
- Banos Ciudad de Fuego | suggestion=nan | type=unmatched
- Delfin SC | suggestion=nan | type=unmatched
- Boston Legacy FC | suggestion=nan | type=unmatched
- Orlando Pride | suggestion=nan | type=unmatched
- CA Belgrano de Cordoba | suggestion=nan | type=unmatched
- Union de Santa Fe | suggestion=nan | type=unmatched
- Levante | suggestion=nan | type=unmatched
- Deportivo Tachira | suggestion=nan | type=unmatched
- Metropolitanos FC | suggestion=nan | type=unmatched
- Dundee United | suggestion=nan | type=unmatched
- Livingston | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 142
Automatic price rows: 88
Value snapshot rows: 408
Matches with any automatic price: 36
Matches with fresh API price: 10
Matches with odds-api.io price: 10
Fresh API match coverage rate: 0.0704
odds-api.io match coverage rate: 0.0704
Real-money ready: False
## Match coverage
- 2026-05-12 | Asteras Tripolis vs Panserraikos | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | Kifisia vs Atromitos | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | Panetolikos vs Larisa | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | Celta vs Levante | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | Betis vs Elche | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | Aberdeen vs St Mirren | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | Dundee United vs Livingston | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | Kilmarnock vs Dundee | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | Osasuna vs Ath Madrid | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-12 | CA Belgrano de Cordoba vs Union de Santa Fe | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Deportivo Tachira vs Metropolitanos FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_European Handicap
- 2026-05-12 | Londrina EC PR vs Sao Bernardo FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | SC Internacional RS vs Athletic Club Sjdr MG | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Banos Ciudad de Fuego vs Delfin SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | Boston Legacy FC vs Orlando Pride | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-12 | LVU Rush vs West Chester United SC USL2 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 142
Proxy price rows: 88
Matched prediction rows: 52
Value snapshot rows: 408
odds-api.io snapshot rows: 30
Baseline snapshot rows: 309
Full model snapshot rows: 99
Positive EV rows: 205
Source counts: {'football_data_bet365_proxy': 126, 'football_data_max_market_proxy': 126, 'football_data_average_market_proxy': 126, 'odds_api_io_Bet365_ML': 27, 'odds_api_io_Bet365_European Handicap': 3}
- 2026-05-12 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_European Handicap | odds=41.0 | prob=0.3488 | EV=13.3008 | match=1.0
- 2026-05-12 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_European Handicap | odds=21.0 | prob=0.274 | EV=4.754 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.96
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.2857 | EV=3.2855 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.2857 | EV=2.642675 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=0.96
- 2026-05-12 | SC Internacional RS vs Athletic Club Sjdr MG | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.2857 | EV=2.4284 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 408
Pre-dedupe proxy candidate observation rows: 143
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-12 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | selection=HOME | source=odds_api_io_Bet365_European Handicap | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-12 | Boston Legacy FC vs Orlando Pride | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-13 | Volos NPS vs Aris Thessaloniki | selection=HOME | source=football_data_average_market_proxy | odds=3.57 | prob=0.3772 | EV=0.346604 | edge=0.097088 | penalty=0.3466042154566742 | tier=proxy_watchlist | score=0.2205
- 2026-05-13 | Volos NFC vs Aris | selection=HOME | source=football_data_average_market_proxy | odds=3.57 | prob=0.3772 | EV=0.346604 | edge=0.097088 | penalty=0.3466042154566742 | tier=proxy_watchlist | score=0.2205
- 2026-05-13 | Racing Club De Lens vs Paris Saint-Germain | selection=HOME | source=football_data_max_market_proxy | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2184
- 2026-05-13 | Deportivo Alaves vs FC Barcelona | selection=HOME | source=football_data_max_market_proxy | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2091
- 2026-05-12 | Osasuna vs Ath Madrid | selection=AWAY | source=football_data_max_market_proxy | odds=2.65 | prob=0.3969 | EV=0.051785 | edge=0.019542 | penalty=0.05178636732227737 | tier=proxy_watchlist | score=0.1961
- 2026-05-13 | Stade Brest 29 vs Strasbourg Alsace | selection=HOME | source=football_data_max_market_proxy | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.195
- 2026-05-13 | Espanyol Barcelona vs Athletic Bilbao | selection=HOME | source=football_data_max_market_proxy | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.1911
- 2026-05-13 | Motherwell FC vs Celtic Glasgow | selection=HOME | source=football_data_bet365_proxy | odds=4.33 | prob=0.3772 | EV=0.633276 | edge=0.146253 | penalty=0.6332751670296646 | tier=proxy_watchlist | score=0.1905
- 2026-05-13 | Motherwell vs Celtic | selection=HOME | source=football_data_bet365_proxy | odds=4.33 | prob=0.3772 | EV=0.633276 | edge=0.146253 | penalty=0.6332751670296646 | tier=proxy_watchlist | score=0.1905
- 2026-05-13 | Brest vs Strasbourg | selection=HOME | source=football_data_max_market_proxy | odds=2.8 | prob=0.3618 | EV=0.01304 | edge=0.004657 | penalty=0.013039594784162167 | tier=proxy_watchlist | score=0.1895

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 5
Top blocker: delayed_football_data_proxy_not_fresh_api_price
Real-money ready: False
## Blocker summary
- delayed_football_data_proxy_not_fresh_api_price: 10
- ev_above_real_candidate_cap_possible_overconfidence: 7
- market_alignment_penalty_too_high_for_real_candidate: 7
- edge_below_candidate_threshold: 3
- watchlist_only_pending_forward_settlement: 1
## Row explanations
- 2026-05-12 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Boston Legacy FC vs Orlando Pride | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-13 | Volos NPS vs Aris Thessaloniki | sel=HOME | score=0.2205 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Volos NFC vs Aris | sel=HOME | score=0.2205 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Racing Club De Lens vs Paris Saint-Germain | sel=HOME | score=0.2184 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Deportivo Alaves vs FC Barcelona | sel=HOME | score=0.2091 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-12 | Osasuna vs Ath Madrid | sel=AWAY | score=0.1961 | blockers=edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Stade Brest 29 vs Strasbourg Alsace | sel=HOME | score=0.195 | blockers=delayed_football_data_proxy_not_fresh_api_price | improve=prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Espanyol Barcelona vs Athletic Bilbao | sel=HOME | score=0.1911 | blockers=edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Motherwell FC vs Celtic Glasgow | sel=HOME | score=0.1905 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Motherwell vs Celtic | sel=HOME | score=0.1905 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Brest vs Strasbourg | sel=HOME | score=0.1895 | blockers=edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 408
Paper proxy observation rows: 25
Positive EV value rows: 205
Suppressed-band observation rows: 0
Distinct matches: 14
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.245282
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=15, avg_ev=0.3445, max_ev=0.744
- draw: rows=8, avg_ev=0.0144, max_ev=0.0752
- home: rows=2, avg_ev=0.4247, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 142
Forward fixture prediction rows: 142
Full model prediction rows: 11
Baseline prediction rows: 131
Max forward predictions: 300
Ready for price join: True
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 17:00 | Kifisia vs Atromitos | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 17:00 | Panetolikos vs Larisa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 18:00 | Celta vs Levante | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 19:00 | Betis vs Elche | coverage=full_team_strength_match | H=0.4457 D=0.2703 A=0.2839 | fair=2.24/3.7/3.52
- 2026-05-12 19:45 | Aberdeen vs St Mirren | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 19:45 | Dundee United vs Livingston | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 19:45 | Kilmarnock vs Dundee | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 20:30 | Osasuna vs Ath Madrid | coverage=full_team_strength_match | H=0.3224 D=0.2807 A=0.3969 | fair=3.1/3.56/2.52
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 22:00 | Deportivo Tachira vs Metropolitanos FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 22:00 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 22:30 | Londrina EC PR vs Sao Bernardo FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 22:30 | SC Internacional RS vs Athletic Club Sjdr MG | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 23:00 | LVU Rush vs West Chester United SC USL2 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 23:00 | Mahaut Soca Strikers vs Middleham United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 23:00 | St Andrew Lions vs Ellerton FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota. | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-12 23:30 | UCV FC vs Deportivo La Guaira | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 142
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 361
Log type: probability_only_no_market_prices
- 2026-05-15 2026-05-12 18:45:00 | Oud-Heverlee Leuven vs Royal Antwerp FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 18:45:00 | Saint Patrick´s Athletic FC vs Shelbourne FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 18:45:00 | Treaty United vs Finn Harps FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 18:45:00 | Waterford FC vs Derry City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 19:00:00 | Aston Villa vs Liverpool FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 19:00:00 | Cordoba CF vs Albacete Balompie | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 19:00:00 | Dundalk FC vs Shamrock Rovers | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 19:00:00 | Notts County vs Chesterfield FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 20:00:00 | FC Cajamarca vs Sporting Cristal | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-12 21:30:00 | LDU Quito vs CD Tecnico Universitario | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-12 05:00:00 | Mandurah City FC Reserves vs Uwa Nedlands FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-12 06:30:00 | Port Darwin FC vs Darwin Hearts FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-12 07:00:00 | Fremantle City vs Olympic Kingsway SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-12 07:00:00 | Mandurah City vs UWA Nedlands FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-12 07:00:00 | Olympic Kingsway SC vs Fremantle City | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-12 08:30:00 | Darwin Hearts FC Reserves vs Garuda FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-12 08:45:00 | Kedah Darul Aman vs Manjung City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-12 09:30:00 | Sydney City Comets vs Manly Warringah Sea Eagles | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 14:00:00 | BC Olympiakos Piraeus vs BC Kolossos Rhodes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-12 18:30:00 | AN Brescia vs Olympiakos | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 142
Manual template rows: 142
Rows with complete manual odds: 0
Rows missing manual odds: 142
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-12 19:45 | Aberdeen vs St Mirren
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota.
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC
- 2026-05-12 19:00 | Betis vs Elche
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe
- 2026-05-12 18:00 | Celta vs Levante
- 2026-05-12 22:00 | Deportivo Tachira vs Metropolitanos FC
- 2026-05-12 19:45 | Dundee United vs Livingston
- 2026-05-12 22:00 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo
- 2026-05-12 17:00 | Kifisia vs Atromitos
- 2026-05-12 19:45 | Kilmarnock vs Dundee
- 2026-05-12 22:30 | Londrina EC PR vs Sao Bernardo FC
- 2026-05-12 23:00 | LVU Rush vs West Chester United SC USL2

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 142
Source counts: {'odds_api_io_events_bookmaker_filtered': 111, 'football_data_fixtures_proxy': 26, 'odds_api_io_events_search': 4, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-12 19:45 | Aberdeen vs St Mirren | SC0 | football_data_fixtures_proxy
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos | G1 | football_data_fixtures_proxy
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota. | colombia-primera-a-apertura | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-05-12 19:00 | Betis vs Elche | la_liga | football_data_fixtures_proxy
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride | usa-national-womens-soccer-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe | argentina-liga-profesional | odds_api_io_events_bookmaker_filtered
- 2026-05-12 18:00 | Celta vs Levante | la_liga | football_data_fixtures_proxy
- 2026-05-12 22:00 | Deportivo Tachira vs Metropolitanos FC | venezuela-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-12 19:45 | Dundee United vs Livingston | SC0 | football_data_fixtures_proxy
- 2026-05-12 22:00 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | bolivia-division-profesional | odds_api_io_events_bookmaker_filtered
- 2026-05-12 17:00 | Kifisia vs Atromitos | G1 | football_data_fixtures_proxy
- 2026-05-12 19:45 | Kilmarnock vs Dundee | SC0 | football_data_fixtures_proxy
- 2026-05-12 22:30 | Londrina EC PR vs Sao Bernardo FC | brazil-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:00 | LVU Rush vs West Chester United SC USL2 | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:00 | Mahaut Soca Strikers vs Middleham United FC | dominica-dfa-premier | odds_api_io_events_bookmaker_filtered
- 2026-05-12 20:30 | Osasuna vs Ath Madrid | la_liga | football_data_fixtures_proxy
- 2026-05-12 17:00 | Panetolikos vs Larisa | G1 | football_data_fixtures_proxy
- 2026-05-12 22:30 | SC Internacional RS vs Athletic Club Sjdr MG | brazil-copa-do-brasil | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:00 | St Andrew Lions vs Ellerton FC | barbados-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-12 23:30 | UCV FC vs Deportivo La Guaira | venezuela-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-13 23:30 | Academia Puerto Cabello vs Portuguesa FC | venezuela-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-13 23:00 | AD Pasto vs CD Tolima | colombia-primera-a-apertura | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 142
Rows with complete odds: 0
- 2026-05-12 19:45 | Aberdeen vs St Mirren | bookmaker=bet365_manual
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos | bookmaker=bet365_manual
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota. | bookmaker=bet365_manual
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC | bookmaker=bet365_manual
- 2026-05-12 19:00 | Betis vs Elche | bookmaker=bet365_manual
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride | bookmaker=bet365_manual
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe | bookmaker=bet365_manual
- 2026-05-12 18:00 | Celta vs Levante | bookmaker=bet365_manual
- 2026-05-12 22:00 | Deportivo Tachira vs Metropolitanos FC | bookmaker=bet365_manual
- 2026-05-12 19:45 | Dundee United vs Livingston | bookmaker=bet365_manual
- 2026-05-12 22:00 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo | bookmaker=bet365_manual
- 2026-05-12 17:00 | Kifisia vs Atromitos | bookmaker=bet365_manual
- 2026-05-12 19:45 | Kilmarnock vs Dundee | bookmaker=bet365_manual
- 2026-05-12 22:30 | Londrina EC PR vs Sao Bernardo FC | bookmaker=bet365_manual
- 2026-05-12 23:00 | LVU Rush vs West Chester United SC USL2 | bookmaker=bet365_manual
- 2026-05-12 23:00 | Mahaut Soca Strikers vs Middleham United FC | bookmaker=bet365_manual
- 2026-05-12 20:30 | Osasuna vs Ath Madrid | bookmaker=bet365_manual
- 2026-05-12 17:00 | Panetolikos vs Larisa | bookmaker=bet365_manual
- 2026-05-12 22:30 | SC Internacional RS vs Athletic Club Sjdr MG | bookmaker=bet365_manual
- 2026-05-12 23:00 | St Andrew Lions vs Ellerton FC | bookmaker=bet365_manual
- 2026-05-12 23:30 | UCV FC vs Deportivo La Guaira | bookmaker=bet365_manual
- 2026-05-13 23:30 | Academia Puerto Cabello vs Portuguesa FC | bookmaker=bet365_manual
- 2026-05-13 23:00 | AD Pasto vs CD Tolima | bookmaker=bet365_manual
- 2026-05-13 20:30 | Alaves vs Barcelona | bookmaker=bet365_manual

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
- 2026-05-12 19:45 | Aberdeen vs St Mirren
- 2026-05-12 17:00 | Asteras Tripolis vs Panserraikos
- 2026-05-12 23:20 | Atletico Nacional Medellin vs Internacional de Bogota.
- 2026-05-12 23:00 | Banos Ciudad de Fuego vs Delfin SC
- 2026-05-12 19:00 | Betis vs Elche
- 2026-05-12 23:00 | Boston Legacy FC vs Orlando Pride
- 2026-05-12 22:00 | CA Belgrano de Cordoba vs Union de Santa Fe
- 2026-05-12 18:00 | Celta vs Levante
- 2026-05-12 22:00 | Deportivo Tachira vs Metropolitanos FC
- 2026-05-12 19:45 | Dundee United vs Livingston
- 2026-05-12 22:00 | GV Club Deportivo San Jose de Oruro vs CD Real Tomayapo
- 2026-05-12 17:00 | Kifisia vs Atromitos
- 2026-05-12 19:45 | Kilmarnock vs Dundee
- 2026-05-12 22:30 | Londrina EC PR vs Sao Bernardo FC
- 2026-05-12 23:00 | LVU Rush vs West Chester United SC USL2
- 2026-05-12 23:00 | Mahaut Soca Strikers vs Middleham United FC
- 2026-05-12 20:30 | Osasuna vs Ath Madrid
- 2026-05-12 17:00 | Panetolikos vs Larisa
- 2026-05-12 22:30 | SC Internacional RS vs Athletic Club Sjdr MG

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 99
Valid forward/proxy log rows: 96
Deduped forward/proxy observation rows: 49
Duplicate forward/proxy log rows: 47
Valid automatic proxy observation rows: 96
Deduped automatic proxy observation rows: 49
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-12 | Sur SC vs Al-Khaboora | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0746
- 2026-05-12 | Celta vs Levante | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0746
- 2026-05-12 | RC Celta de Vigo vs Levante UD | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0746
- 2026-05-12 | PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0742
- 2026-05-12 | St Andrew Lions vs Ellerton FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0733
- 2026-05-12 | TRA United vs Jkt Tanzania | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0716
- 2026-05-13 | Motherwell vs Celtic | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0712
- 2026-05-13 | Motherwell FC vs Celtic Glasgow | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0712
- 2026-05-13 | PAOK vs AEK | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | Levadeiakos vs OFI Crete | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | PAOK Thessaloniki vs AEK Athens | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
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
### Betis vs Elche
- Date/time: 2026-05-12 19:00
- League/phase: la_liga / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 5.5
- Fair odds: 3.52
- Model probability: 0.2839
- Probability band: 0.25-0.35
- EV: 0.5615
- Probability edge: 0.1021
- Alignment penalty: 0.5615
- Suppression action: none
- Paper tier: volume_observation
- Paper score: 0.2872
- Prediction ID: 06c0b8a8cfd48f2f470a
### Betis vs Elche
- Date/time: 2026-05-12 19:00
- League/phase: la_liga / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 5.25
- Fair odds: 3.52
- Model probability: 0.2839
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
Newly logged paper-test picks: 4
Total logged paper-test rows: 99
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 408, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 193, 'current_paper_picks': 25, 'newly_logged_picks': 4, 'total_logged_paper_rows': 99, 'source_used': 'automatic_forward_value_snapshots'}
- Betis vs Elche | coverage=full_team_strength_match | selection=AWAY | odds=5.5 | prob=0.2839 | EV=0.5615 | edge=0.1021 | penalty=0.5615 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Betis vs Elche | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.2839 | EV=0.4905 | edge=0.0934 | penalty=0.4905 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Getafe vs Mallorca | coverage=full_team_strength_match | selection=AWAY | odds=3.7 | prob=0.3268 | EV=0.2092 | edge=0.0565 | penalty=0.2092 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Villarreal vs Sevilla | coverage=full_team_strength_match | selection=AWAY | odds=3.7 | prob=0.326 | EV=0.2062 | edge=0.0557 | penalty=0.2062 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Villarreal vs Sevilla | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.326 | EV=0.1736 | edge=0.0482 | penalty=0.1736 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Getafe vs Mallorca | coverage=full_team_strength_match | selection=AWAY | odds=3.51 | prob=0.3268 | EV=0.1471 | edge=0.0419 | penalty=0.1471 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Girona vs Sociedad | coverage=full_team_strength_match | selection=AWAY | odds=3.35 | prob=0.3305 | EV=0.1072 | edge=0.032 | penalty=0.1072 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Girona vs Sociedad | coverage=full_team_strength_match | selection=AWAY | odds=3.3 | prob=0.3305 | EV=0.0906 | edge=0.0275 | penalty=0.0907 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Valencia vs Vallecano | coverage=full_team_strength_match | selection=AWAY | odds=3.4 | prob=0.3215 | EV=0.0931 | edge=0.0274 | penalty=0.0931 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Valencia vs Vallecano | coverage=full_team_strength_match | selection=AWAY | odds=3.3 | prob=0.3215 | EV=0.0609 | edge=0.0185 | penalty=0.061 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Lens vs Paris SG | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3022 | EV=0.0577 | edge=0.0165 | penalty=0.0577 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Alaves vs Barcelona | coverage=full_team_strength_match | selection=DRAW | odds=3.9 | prob=0.2757 | EV=0.0752 | edge=0.0193 | penalty=0.0752 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Lens vs Paris SG | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2638 | EV=0.0552 | edge=0.0138 | penalty=0.0552 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Alaves vs Barcelona | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2757 | EV=0.0339 | edge=0.009 | penalty=0.0339 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Osasuna vs Ath Madrid | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2807 | EV=0.0105 | edge=0.0029 | penalty=0.0105 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brest vs Strasbourg | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2794 | EV=0.0058 | edge=0.0016 | penalty=0.0058 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brest vs Strasbourg | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2794 | EV=0.0058 | edge=0.0016 | penalty=0.0058 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Osasuna vs Ath Madrid | coverage=full_team_strength_match | selection=AWAY | odds=2.65 | prob=0.3969 | EV=0.0518 | edge=0.0195 | penalty=0.0518 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation

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
