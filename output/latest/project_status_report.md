# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-13T02:30:01.265169+00:00`
GitHub run: `338` attempt `1`
GitHub SHA: `990efc96ea3665de7f114ead91bd02bece12ccf6`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 17 |  |  |
| Football-Data upcoming odds proxy | True | 51 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 59 |  |  |
| odds-api.io forward fixtures | True | 194 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 513 |  |  |
| Forward price coverage report | True | 183 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 3 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 183 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 18
- Automatic value snapshots: 162
- Positive EV proxy rows: 81
- Proxy observation rows: 25
- Valid forward/proxy log rows: 106
- Deduped forward/proxy log rows: 54
- Duplicate forward/proxy log rows identified: 52
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
Current: 162 value snapshots; fresh API coverage rate 0.0.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 54 deduped forward/proxy rows; 52 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 26
Upcoming fixture rows: 17
Proxy price rows: 51
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
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_bet365_proxy | 1.57/4.2/5.0
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_max_market_proxy | 1.68/4.2/5.0
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_average_market_proxy | 1.6/3.89/4.66
- 2026-05-13 15:00 | Volos NFC vs Aris | football_data_bet365_proxy | 4.33/3.2/1.91
- 2026-05-13 15:00 | Volos NFC vs Aris | football_data_max_market_proxy | 4.33/3.6/2.05
- 2026-05-13 15:00 | Volos NFC vs Aris | football_data_average_market_proxy | 3.57/3.29/1.96
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | football_data_bet365_proxy | 1.41/4.2/8.0
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | football_data_max_market_proxy | 1.42/4.5/8.5
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | football_data_average_market_proxy | 1.38/4.21/7.59
- 2026-05-13 17:30 | PAOK vs AEK | football_data_bet365_proxy | 1.68/3.7/5.0
- 2026-05-13 17:30 | PAOK vs AEK | football_data_max_market_proxy | 1.74/3.8/5.0
- 2026-05-13 17:30 | PAOK vs AEK | football_data_average_market_proxy | 1.69/3.53/4.56
- 2026-05-13 20:00 | Hearts vs Falkirk | football_data_bet365_proxy | 1.41/4.75/6.5
- 2026-05-13 20:00 | Hearts vs Falkirk | football_data_max_market_proxy | 1.44/4.9/7.5

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 18
Fixture team rows unmatched: 16
Ready for model-fixture join: False
Automatic forward price rows: 51
odds-api.io price rows: 0
Football-Data price rows: 51
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- Hearts | suggestion=nan | type=unmatched
- Falkirk | suggestion=nan | type=unmatched
- Levadeiakos | suggestion=nan | type=unmatched
- OFI Crete | suggestion=nan | type=unmatched
- Manchester City | suggestion=nan | type=unmatched
- Motherwell | suggestion=nan | type=unmatched
- Celtic | suggestion=nan | type=unmatched
- Olympiakos | suggestion=nan | type=unmatched
- Panathinaikos | suggestion=nan | type=unmatched
- PAOK | suggestion=nan | type=unmatched
- AEK | suggestion=nan | type=unmatched
- Rangers | suggestion=Angers | type=suggested_alias_needed
- Hibernian | suggestion=nan | type=unmatched
- Volos NFC | suggestion=nan | type=unmatched
- Aris | suggestion=nan | type=unmatched
- Oviedo | suggestion=nan | type=unmatched
## Interpretation

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 18
Automatic price rows: 51
Value snapshot rows: 162
Matches with any automatic price: 17
Matches with fresh API price: 0
Matches with odds-api.io price: 0
Fresh API match coverage rate: 0.0
odds-api.io match coverage rate: 0.0
Real-money ready: False
## Match coverage
- 2026-05-13 | Levadeiakos vs OFI Crete | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Volos NFC vs Aris | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Olympiakos vs Panathinaikos | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | PAOK vs AEK | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Brest vs Strasbourg | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Espanol vs Ath Bilbao | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Villarreal vs Sevilla | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Manchester City vs Crystal Palace | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-13 | Hearts vs Falkirk | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Lens vs Paris SG | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Man City vs Crystal Palace | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Motherwell vs Celtic | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Rangers vs Hibernian | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Alaves vs Barcelona | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | Getafe vs Mallorca | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-14 | Valencia vs Vallecano | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-14 | Girona vs Sociedad | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 18
Proxy price rows: 51
Matched prediction rows: 18
Value snapshot rows: 162
odds-api.io snapshot rows: 0
Baseline snapshot rows: 81
Full model snapshot rows: 81
Positive EV rows: 81
Source counts: {'football_data_bet365_proxy': 54, 'football_data_max_market_proxy': 54, 'football_data_average_market_proxy': 54}
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.96
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.2857 | EV=3.2855 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.2857 | EV=2.642675 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.2857 | EV=2.4284 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.82 | prob=0.3488 | EV=1.378816 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-13 | Rangers vs Hibernian | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.5 | prob=0.274 | EV=1.055 | match=0.96

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 162
Pre-dedupe proxy candidate observation rows: 49
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 9
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-13 | Volos NFC vs Aris | selection=HOME | source=football_data_average_market_proxy | odds=3.57 | prob=0.3772 | EV=0.346604 | edge=0.097088 | penalty=0.3466042154566742 | tier=proxy_watchlist | score=0.2205
- 2026-05-13 | Motherwell vs Celtic | selection=HOME | source=football_data_bet365_proxy | odds=4.33 | prob=0.3772 | EV=0.633276 | edge=0.146253 | penalty=0.6332751670296646 | tier=proxy_watchlist | score=0.1905
- 2026-05-13 | Brest vs Strasbourg | selection=HOME | source=football_data_max_market_proxy | odds=2.8 | prob=0.3618 | EV=0.01304 | edge=0.004657 | penalty=0.013039594784162167 | tier=proxy_watchlist | score=0.1895
- 2026-05-13 | Hearts vs Falkirk | selection=DRAW | source=football_data_max_market_proxy | odds=4.9 | prob=0.274 | EV=0.3426 | edge=0.069918 | penalty=0.34259758332435 | tier=suppressed_proxy_watchlist | score=0.0995
- 2026-05-13 | Rangers vs Hibernian | selection=DRAW | source=football_data_bet365_proxy | odds=4.75 | prob=0.274 | EV=0.3015 | edge=0.063474 | penalty=0.30150195225292853 | tier=suppressed_proxy_watchlist | score=0.0982
- 2026-05-13 | Getafe vs Mallorca | selection=AWAY | source=football_data_max_market_proxy | odds=3.7 | prob=0.3268 | EV=0.20916 | edge=0.05653 | penalty=0.20916120916120895 | tier=suppressed_proxy_watchlist | score=0.0975
- 2026-05-13 | Villarreal vs Sevilla | selection=AWAY | source=football_data_max_market_proxy | odds=3.7 | prob=0.326 | EV=0.2062 | edge=0.05573 | penalty=0.2062012062012062 | tier=suppressed_proxy_watchlist | score=0.0973
- 2026-05-13 | Olympiakos vs Panathinaikos | selection=DRAW | source=football_data_max_market_proxy | odds=4.5 | prob=0.274 | EV=0.233 | edge=0.051778 | penalty=0.233001233001233 | tier=suppressed_proxy_watchlist | score=0.0958
- 2026-05-14 | Girona vs Sociedad | selection=AWAY | source=football_data_max_market_proxy | odds=3.35 | prob=0.3305 | EV=0.107175 | edge=0.031993 | penalty=0.10717671612390989 | tier=suppressed_proxy_watchlist | score=0.0936
- 2026-05-13 | Levadeiakos vs OFI Crete | selection=DRAW | source=football_data_bet365_proxy | odds=4.2 | prob=0.274 | EV=0.1508 | edge=0.035905 | penalty=0.15080115080115086 | tier=suppressed_proxy_watchlist | score=0.0929
- 2026-05-13 | Motherwell vs Celtic | selection=DRAW | source=football_data_max_market_proxy | odds=4.2 | prob=0.274 | EV=0.1508 | edge=0.035905 | penalty=0.15080115080115086 | tier=suppressed_proxy_watchlist | score=0.0929
- 2026-05-14 | Valencia vs Vallecano | selection=AWAY | source=football_data_max_market_proxy | odds=3.4 | prob=0.3215 | EV=0.0931 | edge=0.027382 | penalty=0.09309868828157408 | tier=suppressed_proxy_watchlist | score=0.0926

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: delayed_football_data_proxy_not_fresh_api_price
Real-money ready: False
## Blocker summary
- delayed_football_data_proxy_not_fresh_api_price: 12
- market_alignment_penalty_too_high_for_real_candidate: 9
- probability_or_league_rule_suppressed: 9
- low_probability_band_under_0_35: 9
- ev_above_real_candidate_cap_possible_overconfidence: 7
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-13 | Volos NFC vs Aris | sel=HOME | score=0.2205 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Motherwell vs Celtic | sel=HOME | score=0.1905 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Brest vs Strasbourg | sel=HOME | score=0.1895 | blockers=edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Hearts vs Falkirk | sel=DRAW | score=0.0995 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Rangers vs Hibernian | sel=DRAW | score=0.0982 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Getafe vs Mallorca | sel=AWAY | score=0.0975 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Villarreal vs Sevilla | sel=AWAY | score=0.0973 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Olympiakos vs Panathinaikos | sel=DRAW | score=0.0958 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-14 | Girona vs Sociedad | sel=AWAY | score=0.0936 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Levadeiakos vs OFI Crete | sel=DRAW | score=0.0929 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Motherwell vs Celtic | sel=DRAW | score=0.0929 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-14 | Valencia vs Vallecano | sel=AWAY | score=0.0926 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 162
Paper proxy observation rows: 25
Positive EV value rows: 81
Suppressed-band observation rows: 0
Distinct matches: 13
Distinct sources: 0
Max EV: 0.744
Average EV: 0.300253
Max probability edge: 0.149927
Average match confidence: None
## By selection
- away: rows=12, avg_ev=0.3387, max_ev=0.744
- draw: rows=8, avg_ev=0.1032, max_ev=0.7207
- home: rows=5, avg_ev=0.5234, max_ev=0.6597

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 18
Forward fixture prediction rows: 18
Full model prediction rows: 9
Baseline prediction rows: 9
Max forward predictions: 300
Ready for price join: True
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Volos NFC vs Aris | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 17:30 | PAOK vs AEK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 18:00 | Brest vs Strasbourg | coverage=full_team_strength_match | H=0.3618 D=0.2794 A=0.3588 | fair=2.76/3.58/2.79
- 2026-05-13 18:00 | Espanol vs Ath Bilbao | coverage=full_team_strength_match | H=0.349 D=0.2922 A=0.3588 | fair=2.87/3.42/2.79
- 2026-05-13 18:00 | Villarreal vs Sevilla | coverage=full_team_strength_match | H=0.4041 D=0.2699 A=0.326 | fair=2.47/3.71/3.07
- 2026-05-13 19:00:00 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 20:00 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 20:00 | Lens vs Paris SG | coverage=full_team_strength_match | H=0.3022 D=0.2638 A=0.4339 | fair=3.31/3.79/2.3
- 2026-05-13 20:00 | Man City vs Crystal Palace | coverage=full_team_strength_match | H=0.4509 D=0.2635 A=0.2857 | fair=2.22/3.8/3.5
- 2026-05-13 20:00 | Motherwell vs Celtic | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 20:00 | Rangers vs Hibernian | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 20:30 | Alaves vs Barcelona | coverage=full_team_strength_match | H=0.2965 D=0.2757 A=0.4277 | fair=3.37/3.63/2.34
- 2026-05-13 20:30 | Getafe vs Mallorca | coverage=full_team_strength_match | H=0.3792 D=0.2939 A=0.3268 | fair=2.64/3.4/3.06
- 2026-05-14 18:00 | Valencia vs Vallecano | coverage=full_team_strength_match | H=0.3922 D=0.2863 A=0.3215 | fair=2.55/3.49/3.11
- 2026-05-14 19:00 | Girona vs Sociedad | coverage=full_team_strength_match | H=0.3982 D=0.2712 A=0.3305 | fair=2.51/3.69/3.03
- 2026-05-14 20:30 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 18
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 362
Log type: probability_only_no_market_prices
- 2026-05-15 2026-05-13 18:45:00 | Saint Patrick´s Athletic FC vs Shelbourne FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-13 18:45:00 | Treaty United vs Finn Harps FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-13 18:45:00 | Waterford FC vs Derry City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-13 19:00:00 | Aston Villa vs Liverpool FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-13 19:00:00 | Cordoba CF vs Albacete Balompie | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-13 19:00:00 | Dundalk FC vs Shamrock Rovers | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-13 19:00:00 | Notts County vs Chesterfield FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-13 20:00:00 | FC Cajamarca vs Sporting Cristal | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-15 2026-05-13 21:30:00 | LDU Quito vs CD Tecnico Universitario | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 05:00:00 | Mandurah City FC Reserves vs Uwa Nedlands FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 06:30:00 | Port Darwin FC vs Darwin Hearts FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 07:00:00 | Fremantle City vs Olympic Kingsway SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 07:00:00 | Mandurah City vs UWA Nedlands FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 07:00:00 | Olympic Kingsway SC vs Fremantle City | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 08:30:00 | Darwin Hearts FC Reserves vs Garuda FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 08:45:00 | Kedah Darul Aman vs Manjung City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 09:30:00 | Sydney City Comets vs Manly Warringah Sea Eagles | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-13 14:00:00 | BC Olympiakos Piraeus vs BC Kolossos Rhodes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-13 2026-05-13 18:30:00 | AN Brescia vs Olympiakos | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-13 12:00:00 | West Ham United FC vs Manchester City WFC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 18
Manual template rows: 18
Rows with complete manual odds: 0
Rows missing manual odds: 18
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-13 20:30 | Alaves vs Barcelona
- 2026-05-13 18:00 | Brest vs Strasbourg
- 2026-05-13 18:00 | Espanol vs Ath Bilbao
- 2026-05-13 20:30 | Getafe vs Mallorca
- 2026-05-13 20:00 | Hearts vs Falkirk
- 2026-05-13 20:00 | Lens vs Paris SG
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete
- 2026-05-13 20:00 | Man City vs Crystal Palace
- 2026-05-13 19:00:00 | Manchester City vs Crystal Palace
- 2026-05-13 20:00 | Motherwell vs Celtic
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos
- 2026-05-13 17:30 | PAOK vs AEK
- 2026-05-13 20:00 | Rangers vs Hibernian
- 2026-05-13 18:00 | Villarreal vs Sevilla
- 2026-05-13 15:00 | Volos NFC vs Aris

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 18
Source counts: {'football_data_fixtures_proxy': 17, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-13 20:30 | Alaves vs Barcelona | la_liga | football_data_fixtures_proxy
- 2026-05-13 18:00 | Brest vs Strasbourg | ligue_1 | football_data_fixtures_proxy
- 2026-05-13 18:00 | Espanol vs Ath Bilbao | la_liga | football_data_fixtures_proxy
- 2026-05-13 20:30 | Getafe vs Mallorca | la_liga | football_data_fixtures_proxy
- 2026-05-13 20:00 | Hearts vs Falkirk | SC0 | football_data_fixtures_proxy
- 2026-05-13 20:00 | Lens vs Paris SG | ligue_1 | football_data_fixtures_proxy
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | G1 | football_data_fixtures_proxy
- 2026-05-13 20:00 | Man City vs Crystal Palace | premier_league | football_data_fixtures_proxy
- 2026-05-13 19:00:00 | Manchester City vs Crystal Palace | premier_league | thesportsdb_eventsnextleague
- 2026-05-13 20:00 | Motherwell vs Celtic | SC0 | football_data_fixtures_proxy
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | G1 | football_data_fixtures_proxy
- 2026-05-13 17:30 | PAOK vs AEK | G1 | football_data_fixtures_proxy
- 2026-05-13 20:00 | Rangers vs Hibernian | SC0 | football_data_fixtures_proxy
- 2026-05-13 18:00 | Villarreal vs Sevilla | la_liga | football_data_fixtures_proxy
- 2026-05-13 15:00 | Volos NFC vs Aris | G1 | football_data_fixtures_proxy
- 2026-05-14 19:00 | Girona vs Sociedad | la_liga | football_data_fixtures_proxy
- 2026-05-14 20:30 | Real Madrid vs Oviedo | la_liga | football_data_fixtures_proxy
- 2026-05-14 18:00 | Valencia vs Vallecano | la_liga | football_data_fixtures_proxy

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 18
Rows with complete odds: 0
- 2026-05-13 20:30 | Alaves vs Barcelona | bookmaker=bet365_manual
- 2026-05-13 18:00 | Brest vs Strasbourg | bookmaker=bet365_manual
- 2026-05-13 18:00 | Espanol vs Ath Bilbao | bookmaker=bet365_manual
- 2026-05-13 20:30 | Getafe vs Mallorca | bookmaker=bet365_manual
- 2026-05-13 20:00 | Hearts vs Falkirk | bookmaker=bet365_manual
- 2026-05-13 20:00 | Lens vs Paris SG | bookmaker=bet365_manual
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | bookmaker=bet365_manual
- 2026-05-13 20:00 | Man City vs Crystal Palace | bookmaker=bet365_manual
- 2026-05-13 19:00:00 | Manchester City vs Crystal Palace | bookmaker=bet365_manual
- 2026-05-13 20:00 | Motherwell vs Celtic | bookmaker=bet365_manual
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | bookmaker=bet365_manual
- 2026-05-13 17:30 | PAOK vs AEK | bookmaker=bet365_manual
- 2026-05-13 20:00 | Rangers vs Hibernian | bookmaker=bet365_manual
- 2026-05-13 18:00 | Villarreal vs Sevilla | bookmaker=bet365_manual
- 2026-05-13 15:00 | Volos NFC vs Aris | bookmaker=bet365_manual
- 2026-05-14 19:00 | Girona vs Sociedad | bookmaker=bet365_manual
- 2026-05-14 20:30 | Real Madrid vs Oviedo | bookmaker=bet365_manual
- 2026-05-14 18:00 | Valencia vs Vallecano | bookmaker=bet365_manual

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
- 2026-05-13 20:30 | Alaves vs Barcelona
- 2026-05-13 18:00 | Brest vs Strasbourg
- 2026-05-13 18:00 | Espanol vs Ath Bilbao
- 2026-05-13 20:30 | Getafe vs Mallorca
- 2026-05-13 20:00 | Hearts vs Falkirk
- 2026-05-13 20:00 | Lens vs Paris SG
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete
- 2026-05-13 20:00 | Man City vs Crystal Palace
- 2026-05-13 19:00:00 | Manchester City vs Crystal Palace
- 2026-05-13 20:00 | Motherwell vs Celtic
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos
- 2026-05-13 17:30 | PAOK vs AEK
- 2026-05-13 20:00 | Rangers vs Hibernian
- 2026-05-13 18:00 | Villarreal vs Sevilla
- 2026-05-13 15:00 | Volos NFC vs Aris
- 2026-05-14 19:00 | Girona vs Sociedad
- 2026-05-14 20:30 | Real Madrid vs Oviedo
- 2026-05-14 18:00 | Valencia vs Vallecano
## After filling odds

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 109
Valid forward/proxy log rows: 106
Deduped forward/proxy observation rows: 54
Duplicate forward/proxy log rows: 52
Valid automatic proxy observation rows: 106
Deduped automatic proxy observation rows: 54
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-12 | TRA United vs Jkt Tanzania | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0716
- 2026-05-13 | Motherwell vs Celtic | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0712
- 2026-05-13 | Motherwell FC vs Celtic Glasgow | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0712
- 2026-05-13 | PAOK vs AEK | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | Levadeiakos vs OFI Crete | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | PAOK Thessaloniki vs AEK Athens | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | APO Levadiakos FC vs OFI Crete | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | Machida Zelvia vs Tokyo Verdy | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | Vissel Kobe vs Kyoto Sanga FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-12 | AL Wasl vs AL Jazira | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0711
- 2026-05-12 | Sportivo Ameliano vs Deportivo Recoleta Reserve | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0711
- 2026-05-12 | AL Ittihad Kalba vs AL Nasr | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.07060000000000001
- 2026-05-12 | El Gouna FC vs Kahrabaa Ismailia | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.07060000000000001
- 2026-05-13 | Volos NFC vs Aris | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0698
- 2026-05-12 | URA FC vs Calvary | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0693
- 2026-05-12 | Gwangju FC vs FC Seoul | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0684
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.06810000000000001
- 2026-05-14 | Real Madrid vs Oviedo | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0675
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
### Getafe vs Mallorca
- Date/time: 2026-05-13 20:30
- League/phase: la_liga / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 3.7
- Fair odds: 3.06
- Model probability: 0.3268
- Probability band: 0.25-0.35
- EV: 0.2092
- Probability edge: 0.0565
- Alignment penalty: 0.2092
- Suppression action: none
- Paper tier: priority_proxy_observation
- Paper score: 0.2564
- Prediction ID: 512b2aaa4dc6a4610a3d
### Villarreal vs Sevilla
- Date/time: 2026-05-13 18:00
- League/phase: la_liga / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 3.7
- Fair odds: 3.07
- Model probability: 0.326
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
Newly logged paper-test picks: 6
Total logged paper-test rows: 109
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 162, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 71, 'current_paper_picks': 25, 'newly_logged_picks': 6, 'total_logged_paper_rows': 109, 'source_used': 'automatic_forward_value_snapshots'}
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
- Brest vs Strasbourg | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2794 | EV=0.0058 | edge=0.0016 | penalty=0.0058 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brest vs Strasbourg | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2794 | EV=0.0058 | edge=0.0016 | penalty=0.0058 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Espanol vs Ath Bilbao | coverage=full_team_strength_match | selection=DRAW | odds=3.3 | prob=0.2922 | EV=-0.0357 | edge=-0.0108 | penalty=0.0357 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=negative_ev_control_observation
- Espanol vs Ath Bilbao | coverage=full_team_strength_match | selection=DRAW | odds=3.3 | prob=0.2922 | EV=-0.0357 | edge=-0.0108 | penalty=0.0357 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=negative_ev_control_observation
- PAOK vs AEK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Levadeiakos vs OFI Crete | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
