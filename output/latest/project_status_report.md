# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-30T13:09:31.341440+00:00`
GitHub run: `382` attempt `1`
GitHub SHA: `dc1dc98d2ceea70173945a9d5fedf47c0580abad`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 12 |  |  |
| Football-Data upcoming odds proxy | True | 36 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 57 |  |  |
| odds-api.io forward fixtures | True | 523 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 231 |  |  |
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
- Automatic value snapshots: 315
- Positive EV proxy rows: 159
- Proxy observation rows: 25
- Valid forward/proxy log rows: 841
- Deduped forward/proxy log rows: 660
- Duplicate forward/proxy log rows identified: 181
- Fresh API match coverage rate: 0.1733
- Matches with fresh API price: 52
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
Current: 315 value snapshots; fresh API coverage rate 0.1733.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 660 deduped forward/proxy rows; 181 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 12
Upcoming fixture rows: 9
Proxy price rows: 27
Sources attempted: 1
Errors: 0
- 2026-05-31 17:30 | Gent vs Genk | football_data_bet365_proxy | 2.9/3.75/2.2
- 2026-05-31 17:30 | Gent vs Genk | football_data_max_market_proxy | 3.0/3.75/2.25
- 2026-05-31 17:30 | Gent vs Genk | football_data_average_market_proxy | 2.89/3.55/2.19
- 2026-05-31 17:30 | Almeria vs Valladolid | football_data_bet365_proxy | 1.39/5.25/5.75
- 2026-05-31 17:30 | Almeria vs Valladolid | football_data_max_market_proxy | 1.42/5.25/7.8
- 2026-05-31 17:30 | Almeria vs Valladolid | football_data_average_market_proxy | 1.38/4.6/6.54
- 2026-05-31 17:30 | Burgos vs Andorra | football_data_bet365_proxy | 1.49/4.2/5.75
- 2026-05-31 17:30 | Burgos vs Andorra | football_data_max_market_proxy | 1.52/4.2/6.33
- 2026-05-31 17:30 | Burgos vs Andorra | football_data_average_market_proxy | 1.48/3.91/5.98
- 2026-05-31 17:30 | Castellon vs Eibar | football_data_bet365_proxy | 1.51/4.33/5.25
- 2026-05-31 17:30 | Castellon vs Eibar | football_data_max_market_proxy | 1.55/4.5/5.5
- 2026-05-31 17:30 | Castellon vs Eibar | football_data_average_market_proxy | 1.51/4.17/5.08
- 2026-05-31 17:30 | La Coruna vs Las Palmas | football_data_bet365_proxy | 3.25/3.4/2.1
- 2026-05-31 17:30 | La Coruna vs Las Palmas | football_data_max_market_proxy | 3.5/3.4/2.15
- 2026-05-31 17:30 | La Coruna vs Las Palmas | football_data_average_market_proxy | 3.2/3.26/2.08
- 2026-05-31 17:30 | Santander vs Cadiz | football_data_bet365_proxy | 1.3/4.75/9.0
- 2026-05-31 17:30 | Santander vs Cadiz | football_data_max_market_proxy | 1.35/5.0/9.0
- 2026-05-31 17:30 | Santander vs Cadiz | football_data_average_market_proxy | 1.33/4.65/7.9
- 2026-05-31 17:30 | Zaragoza vs Malaga | football_data_bet365_proxy | 4.75/3.6/1.71
- 2026-05-31 17:30 | Zaragoza vs Malaga | football_data_max_market_proxy | 5.0/3.6/1.85
- 2026-05-31 17:30 | Zaragoza vs Malaga | football_data_average_market_proxy | 4.34/3.34/1.77
- 2026-05-31 20:00 | Cordoba vs Huesca | football_data_bet365_proxy | 1.71/3.2/5.5
- 2026-05-31 20:00 | Cordoba vs Huesca | football_data_max_market_proxy | 1.8/3.65/5.5

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 363
Fixture team rows unmatched: 716
Ready for model-fixture join: False
Automatic forward price rows: 79
odds-api.io price rows: 52
Football-Data price rows: 27
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. FC Slovacko Uherske Hradiste | suggestion=nan | type=unmatched
- SK Artis Brno | suggestion=nan | type=unmatched
- AA Internacional Limeira SP | suggestion=nan | type=unmatched
- Ypiranga FC RS | suggestion=nan | type=unmatched
- Aalesund FK 2 | suggestion=nan | type=unmatched
- Strindheim TF | suggestion=nan | type=unmatched
- AC Horsens | suggestion=nan | type=unmatched
- Kolding IF | suggestion=nan | type=unmatched
- AC Oulu | suggestion=nan | type=unmatched
- FF Jaro | suggestion=nan | type=unmatched
- AD Cantolao | suggestion=nan | type=unmatched
- CDU San Martin | suggestion=nan | type=unmatched
- AD Sao Caetano SP | suggestion=nan | type=unmatched
- Botafogo FC SP | suggestion=nan | type=unmatched
- AE Realidade Jovem SP | suggestion=nan | type=unmatched
- Criciuma EC SC | suggestion=nan | type=unmatched
- Afturelding | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 79
Value snapshot rows: 315
Matches with any automatic price: 61
Matches with fresh API price: 52
Matches with odds-api.io price: 52
Fresh API match coverage rate: 0.1733
odds-api.io match coverage rate: 0.1733
Real-money ready: False
## Match coverage
- 2026-05-31 | Broadmeadow Magic FC vs Lambton Jaffas FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | South Hobart FC 2 vs Hobart United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Veertien Mie FC vs FC Fujizakura | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Canberra Olympic vs West Canberra Wanderers FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Clarence Zebras FC vs South East United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Magic United Tfa vs Lions FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Sydney United 58 FC vs Sutherland Sharks | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Bulls FC Academy vs Western City Rangers FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-31 | Blaublitz Akita vs Hokkaido Consadole Sapporo | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Boroondara Eagles vs Essendon Royals SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Broadmeadow Magic FC Reserve vs Lambton Jaffas FC Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-31 | Canberra Croatia FC vs Belconnen United | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Fagiano Okayama vs Urawa Red Diamonds | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Gold Coast United FC vs Sunshine Coast Wanderers FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | FC Imabari vs FC Ryukyu | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Kamatamare Sanuki vs Giravanz Kitakyushu | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-31 | Macarthur Rams vs Illawarra Stingrays | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 79
Matched prediction rows: 71
Value snapshot rows: 315
odds-api.io snapshot rows: 162
Baseline snapshot rows: 303
Full model snapshot rows: 12
Positive EV rows: 159
Source counts: {'odds_api_io_Bet365_ML': 159, 'football_data_bet365_proxy': 51, 'football_data_max_market_proxy': 51, 'football_data_average_market_proxy': 51, 'odds_api_io_Bet365 (no latency)_ML': 3}
- 2026-05-31 | Uwa Nedlands FC vs Balcatta FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3772 | EV=11.8248 | match=1.0
- 2026-05-31 | Canberra Olympic vs West Canberra Wanderers FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3488 | EV=10.8592 | match=1.0
- 2026-05-31 | Perth Azzurri vs Sorrento FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3488 | EV=9.1152 | match=1.0
- 2026-05-31 | South Hobart FC 2 vs Hobart United FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-31 | Tuggeranong United FC vs Majura FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-31 | Japan vs Iceland | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-31 | Magic United Tfa vs Lions FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3772 | EV=3.1492 | match=1.0
- 2026-05-31 | Canberra Olympic vs West Canberra Wanderers FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-05-31 | Perth Azzurri vs Sorrento FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-05-31 | Uwa Nedlands FC vs Balcatta FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.274 | EV=2.288 | match=1.0
- 2026-05-31 | Santander vs Cadiz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-31 | Racing Santander vs Cadiz CF | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-31 | Santander vs Cadiz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-31 | Racing Santander vs Cadiz CF | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-31 | SK Slovan HAC vs SV Wienerberg 1921 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-31 | Canberra Croatia FC vs Belconnen United | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-31 | Real Madrid vs Granada CF | coverage=full_team_strength_match | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.2345 | EV=1.814 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 315
Pre-dedupe proxy candidate observation rows: 97
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-31 | Yeoju FC vs Daejeon Korail FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-31 | Boroondara Eagles vs Essendon Royals SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-31 | Ansan Greeners FC vs Cheonan City FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-31 | Jeonnam Dragons vs Seoul E-Land FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-31 | Fagiano Okayama vs Urawa Red Diamonds | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-31 | Moggill FC vs Yeronga Eagles FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-31 | Gil Vicente FC vs Rio Ave FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.2 | prob=0.3772 | EV=0.58424 | edge=0.139105 | penalty=0.5842415842415842 | tier=proxy_watchlist | score=0.2192
- 2026-05-31 | RC Deportivo De La Coruna vs UD Las Palmas | selection=HOME | source=football_data_max_market_proxy | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2184
- 2026-05-31 | La Coruna vs Las Palmas | selection=HOME | source=football_data_max_market_proxy | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2184
- 2026-05-31 | West Adelaide SC Reserve vs Adelaide City FC Reserve | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3772 | EV=0.54652 | edge=0.133298 | penalty=0.5465227837410107 | tier=proxy_watchlist | score=0.2169
- 2026-05-31 | West Adelaide SC vs Adelaide City FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3772 | EV=0.54652 | edge=0.133298 | penalty=0.5465227837410107 | tier=proxy_watchlist | score=0.2169
- 2026-05-31 | Moreton City Excelsior vs The Gap FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3772 | EV=0.47108 | edge=0.12079 | penalty=0.4710814710814708 | tier=proxy_watchlist | score=0.212

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 5
Top blocker: ev_above_real_candidate_cap_possible_overconfidence
Real-money ready: False
## Blocker summary
- ev_above_real_candidate_cap_possible_overconfidence: 10
- market_alignment_penalty_too_high_for_real_candidate: 10
- delayed_football_data_proxy_not_fresh_api_price: 2
- watchlist_only_pending_forward_settlement: 1
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-31 | Yeoju FC vs Daejeon Korail FC | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-31 | Boroondara Eagles vs Essendon Royals SC | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-31 | Ansan Greeners FC vs Cheonan City FC | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-31 | Jeonnam Dragons vs Seoul E-Land FC | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-31 | Fagiano Okayama vs Urawa Red Diamonds | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-31 | Moggill FC vs Yeronga Eagles FC | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-31 | Gil Vicente FC vs Rio Ave FC | sel=HOME | score=0.2192 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-31 | RC Deportivo De La Coruna vs UD Las Palmas | sel=HOME | score=0.2184 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-31 | La Coruna vs Las Palmas | sel=HOME | score=0.2184 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-31 | West Adelaide SC Reserve vs Adelaide City FC Reserve | sel=HOME | score=0.2169 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-31 | West Adelaide SC vs Adelaide City FC | sel=HOME | score=0.2169 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-31 | Moreton City Excelsior vs The Gap FC | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 315
Paper proxy observation rows: 25
Positive EV value rows: 159
Suppressed-band observation rows: 0
Distinct matches: 22
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.607713
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=7, avg_ev=0.6626, max_ev=0.7719
- draw: rows=5, avg_ev=0.6085, max_ev=0.781
- home: rows=13, avg_ev=0.5779, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 363
Forward fixture prediction rows: 300
Full model prediction rows: 2
Baseline prediction rows: 298
Max forward predictions: 300
Ready for price join: True
- 2026-05-31 03:00 | Broadmeadow Magic FC vs Lambton Jaffas FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 04:00 | South Hobart FC 2 vs Hobart United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 04:00 | Veertien Mie FC vs FC Fujizakura | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 04:30 | Canberra Olympic vs West Canberra Wanderers FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 04:30 | Clarence Zebras FC vs South East United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 04:30 | Magic United Tfa vs Lions FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 04:30 | Sydney United 58 FC vs Sutherland Sharks | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 04:40 | Bulls FC Academy vs Western City Rangers FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Blaublitz Akita vs Hokkaido Consadole Sapporo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Boroondara Eagles vs Essendon Royals SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Broadmeadow Magic FC Reserve vs Lambton Jaffas FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Canberra Croatia FC vs Belconnen United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Fagiano Okayama vs Urawa Red Diamonds | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Gold Coast United FC vs Sunshine Coast Wanderers FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | FC Imabari vs FC Ryukyu | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Kamatamare Sanuki vs Giravanz Kitakyushu | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Macarthur Rams vs Illawarra Stingrays | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Montedio Yamagata vs Matsumoto Yamaga FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Palm Beach SC vs Virginia United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Shimizu S-Pulse vs Yokohama F Marinos | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-31 05:00 | Siheung Citizen FC vs FC Mokpo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 4924
Log type: probability_only_no_market_prices
- 2026-05-31 2026-05-31 19:30:00 | Club Atletico Barinas vs Atletico El Vigia | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 19:30:00 | Deportes Colina vs CD Trasandino de Los Andes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 19:30:00 | Monagas SC B vs Deportivo Miranda | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 19:30:00 | Serra Branca EC PB vs Retro FC PE | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 19:30:00 | Urena SC vs Yaracuyanos FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 19:30:00 | USA vs Senegal | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Atletico Avila FC vs Bolivar SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Atletico Balboa vs CD Inca | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Brazil Juniors vs SV River Plate Aruba | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Cordoba vs Huesca | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Dynamo Puerto FC vs Aragua FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | EC Democrata MG vs Rio Branco AC ES | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Inhumas EC GO vs SE Gama DF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Ivinhema MS vs Uberlandia EC MG | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Leganes vs Mirandes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Mahaut Soca Strikers vs We United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Oriente Petrolero vs Blooming Santa Cruz | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | Portland Timbers II vs Tacoma Defiance | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | RKC Third Coast vs Rockford Raptors | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-31 20:00:00 | St. Croix SC vs River Light FC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 363
Manual template rows: 363
Rows with complete manual odds: 0
Rows missing manual odds: 363
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-31 11:00 | 1. FC Slovacko Uherske Hradiste vs SK Artis Brno
- 2026-05-31 19:00 | AA Internacional Limeira SP vs Ypiranga FC RS
- 2026-05-31 14:00 | Aalesund FK 2 vs Strindheim TF
- 2026-05-31 13:00 | AC Horsens vs Kolding IF
- 2026-05-31 13:00 | AC Oulu vs FF Jaro
- 2026-05-31 16:00 | AD Cantolao vs CDU San Martin
- 2026-05-31 18:00 | AD Sao Caetano SP vs Botafogo FC SP
- 2026-05-31 18:00 | AE Realidade Jovem SP vs Criciuma EC SC
- 2026-05-31 19:15 | Afturelding vs Fylkir Reykjavik
- 2026-05-31 10:00 | AGF Aarhus vs HB Koege
- 2026-05-31 13:00 | Albion FC vs Montevideo City Torque
- 2026-05-31 17:30 | Almeria vs Valladolid
- 2026-05-31 21:30 | Anapolis FC GO vs Maranhao AC MA
- 2026-05-31 23:00 | Angel City FC vs North Carolina Courage
- 2026-05-31 10:00 | Ansan Greeners FC vs Cheonan City FC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 363
Source counts: {'odds_api_io_events_bookmaker_filtered': 345, 'football_data_fixtures_proxy': 9, 'odds_api_io_events_search': 9}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-31 11:00 | 1. FC Slovacko Uherske Hradiste vs SK Artis Brno | czechia-1-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-31 19:00 | AA Internacional Limeira SP vs Ypiranga FC RS | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-31 14:00 | Aalesund FK 2 vs Strindheim TF | norway-3rd-division-group-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-31 13:00 | AC Horsens vs Kolding IF | denmark-1-division | odds_api_io_events_bookmaker_filtered
- 2026-05-31 13:00 | AC Oulu vs FF Jaro | finland-veikkausliiga | odds_api_io_events_bookmaker_filtered
- 2026-05-31 16:00 | AD Cantolao vs CDU San Martin | peru-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-31 18:00 | AD Sao Caetano SP vs Botafogo FC SP | brazil-u20-paulista | odds_api_io_events_bookmaker_filtered
- 2026-05-31 18:00 | AE Realidade Jovem SP vs Criciuma EC SC | brazil-brasileiro-a3-women | odds_api_io_events_bookmaker_filtered
- 2026-05-31 19:15 | Afturelding vs Fylkir Reykjavik | iceland-1-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-31 10:00 | AGF Aarhus vs HB Koege | denmark-kvindeligaen-women | odds_api_io_events_bookmaker_filtered
- 2026-05-31 13:00 | Albion FC vs Montevideo City Torque | uruguay-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-31 17:30 | Almeria vs Valladolid | SP2 | football_data_fixtures_proxy
- 2026-05-31 21:30 | Anapolis FC GO vs Maranhao AC MA | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-31 23:00 | Angel City FC vs North Carolina Courage | usa-national-womens-soccer-league | odds_api_io_events_bookmaker_filtered
- 2026-05-31 10:00 | Ansan Greeners FC vs Cheonan City FC | republic-of-korea-k-league-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-31 17:00 | Arborg vs Hafnir | iceland-4-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-31 17:00 | Arenas Armilla CD vs CF Motril | spain-amateur-tercera-federacion-group-9 | odds_api_io_events_bookmaker_filtered
- 2026-05-31 14:00 | Arendal FK vs Sotra SK | norway-2nd-division-group-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-31 20:00 | Atletico Avila FC vs Bolivar SC | venezuela-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-31 20:00 | Atletico Balboa vs CD Inca | el-salvador-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-31 14:00 | Augnablik Kopavogur vs Hottur/Huginn | iceland-3-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-31 13:00 | Avai FC SC vs Figueirense FC SC | brazil-u20-catarinense-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-05-31 12:30 | Big Bullets vs Moyale Barracks | malawi-super-league | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 363
Rows with complete odds: 0
- 2026-05-31 11:00 | 1. FC Slovacko Uherske Hradiste vs SK Artis Brno | bookmaker=bet365_manual
- 2026-05-31 19:00 | AA Internacional Limeira SP vs Ypiranga FC RS | bookmaker=bet365_manual
- 2026-05-31 14:00 | Aalesund FK 2 vs Strindheim TF | bookmaker=bet365_manual
- 2026-05-31 13:00 | AC Horsens vs Kolding IF | bookmaker=bet365_manual
- 2026-05-31 13:00 | AC Oulu vs FF Jaro | bookmaker=bet365_manual
- 2026-05-31 16:00 | AD Cantolao vs CDU San Martin | bookmaker=bet365_manual
- 2026-05-31 18:00 | AD Sao Caetano SP vs Botafogo FC SP | bookmaker=bet365_manual
- 2026-05-31 18:00 | AE Realidade Jovem SP vs Criciuma EC SC | bookmaker=bet365_manual
- 2026-05-31 19:15 | Afturelding vs Fylkir Reykjavik | bookmaker=bet365_manual
- 2026-05-31 10:00 | AGF Aarhus vs HB Koege | bookmaker=bet365_manual
- 2026-05-31 13:00 | Albion FC vs Montevideo City Torque | bookmaker=bet365_manual
- 2026-05-31 17:30 | Almeria vs Valladolid | bookmaker=bet365_manual
- 2026-05-31 21:30 | Anapolis FC GO vs Maranhao AC MA | bookmaker=bet365_manual
- 2026-05-31 23:00 | Angel City FC vs North Carolina Courage | bookmaker=bet365_manual
- 2026-05-31 10:00 | Ansan Greeners FC vs Cheonan City FC | bookmaker=bet365_manual
- 2026-05-31 17:00 | Arborg vs Hafnir | bookmaker=bet365_manual
- 2026-05-31 17:00 | Arenas Armilla CD vs CF Motril | bookmaker=bet365_manual
- 2026-05-31 14:00 | Arendal FK vs Sotra SK | bookmaker=bet365_manual
- 2026-05-31 20:00 | Atletico Avila FC vs Bolivar SC | bookmaker=bet365_manual
- 2026-05-31 20:00 | Atletico Balboa vs CD Inca | bookmaker=bet365_manual
- 2026-05-31 14:00 | Augnablik Kopavogur vs Hottur/Huginn | bookmaker=bet365_manual
- 2026-05-31 13:00 | Avai FC SC vs Figueirense FC SC | bookmaker=bet365_manual
- 2026-05-31 12:30 | Big Bullets vs Moyale Barracks | bookmaker=bet365_manual
- 2026-05-31 12:00 | BK Hacken vs Hammarby IF | bookmaker=bet365_manual

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
- 2026-05-31 11:00 | 1. FC Slovacko Uherske Hradiste vs SK Artis Brno
- 2026-05-31 19:00 | AA Internacional Limeira SP vs Ypiranga FC RS
- 2026-05-31 14:00 | Aalesund FK 2 vs Strindheim TF
- 2026-05-31 13:00 | AC Horsens vs Kolding IF
- 2026-05-31 13:00 | AC Oulu vs FF Jaro
- 2026-05-31 16:00 | AD Cantolao vs CDU San Martin
- 2026-05-31 18:00 | AD Sao Caetano SP vs Botafogo FC SP
- 2026-05-31 18:00 | AE Realidade Jovem SP vs Criciuma EC SC
- 2026-05-31 19:15 | Afturelding vs Fylkir Reykjavik
- 2026-05-31 10:00 | AGF Aarhus vs HB Koege
- 2026-05-31 13:00 | Albion FC vs Montevideo City Torque
- 2026-05-31 17:30 | Almeria vs Valladolid
- 2026-05-31 21:30 | Anapolis FC GO vs Maranhao AC MA
- 2026-05-31 23:00 | Angel City FC vs North Carolina Courage
- 2026-05-31 10:00 | Ansan Greeners FC vs Cheonan City FC
- 2026-05-31 17:00 | Arborg vs Hafnir
- 2026-05-31 17:00 | Arenas Armilla CD vs CF Motril
- 2026-05-31 14:00 | Arendal FK vs Sotra SK
- 2026-05-31 20:00 | Atletico Avila FC vs Bolivar SC

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 844
Valid forward/proxy log rows: 841
Deduped forward/proxy observation rows: 660
Duplicate forward/proxy log rows: 181
Valid automatic proxy observation rows: 841
Deduped automatic proxy observation rows: 660
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-23 | Avondale FC vs Alamein FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-27 | VVSB Noordwijkerhout vs Excelsior Maassluis | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553
- 2026-05-30 | Gold Coast United FC vs Peninsula Power | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054700000000000006
- 2026-05-30 | Canberra Juventus FC vs Tuggeranong United FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054700000000000006
- 2026-05-30 | Cooks Hill United vs Valentine FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054700000000000006
- 2026-05-30 | Alamein FC vs Keilor Park SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054700000000000006
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
### Almeria vs Valladolid
- Date/time: 2026-05-31 17:30
- League/phase: SP2 / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 5.75
- Fair odds: 3.64
- Model probability: 0.2746
- Probability band: 0.25-0.35
- EV: 0.5789
- Probability edge: 0.1007
- Alignment penalty: 0.579
- Suppression action: none
- Paper tier: volume_observation
- Paper score: 0.2873
- Prediction ID: d5fb5db5924b06af4072
### Almeria vs Valladolid
- Date/time: 2026-05-31 17:30
- League/phase: SP2 / automatic_forward_price_proxy
- Selection: DRAW
- Market odds: 5.25
- Fair odds: 3.89
- Model probability: 0.2572
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
Total logged paper-test rows: 844
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 315, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 128, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 844, 'source_used': 'automatic_forward_value_snapshots'}
- Almeria vs Valladolid | coverage=full_team_strength_match | selection=AWAY | odds=5.75 | prob=0.2746 | EV=0.5789 | edge=0.1007 | penalty=0.579 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Almeria vs Valladolid | coverage=full_team_strength_match | selection=DRAW | odds=5.25 | prob=0.2572 | EV=0.3503 | edge=0.0667 | penalty=0.3503 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Real Madrid vs Granada CF | coverage=full_team_strength_match | selection=DRAW | odds=6.5 | prob=0.2497 | EV=0.623 | edge=0.0959 | penalty=0.6231 | band=0.00-0.25 | risk=market_misalignment | rule=none | tier=volume_observation
- Real Zaragoza vs Malaga CF | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Zaragoza vs Malaga | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CD Castellon vs SD Eibar | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.08 | prob=0.3488 | EV=0.7719 | edge=0.152 | penalty=0.7719 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Castellon vs Eibar | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.08 | prob=0.3488 | EV=0.7719 | edge=0.152 | penalty=0.7719 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mitchelton FC vs SWQ Thunder FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Veertien Mie FC vs FC Fujizakura | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Imabari vs FC Ryukyu | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Zaragoza vs Malaga | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.34 | prob=0.3772 | EV=0.637 | edge=0.1468 | penalty=0.637 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Real Zaragoza vs Malaga CF | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.34 | prob=0.3772 | EV=0.637 | edge=0.1468 | penalty=0.637 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Cordoba CF vs SD Huesca | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.74 | prob=0.3488 | EV=0.6533 | edge=0.1378 | penalty=0.6533 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Cordoba vs Huesca | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.74 | prob=0.3488 | EV=0.6533 | edge=0.1378 | penalty=0.6533 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gil Vicente FC vs Rio Ave FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.2 | prob=0.3772 | EV=0.5842 | edge=0.1391 | penalty=0.5842 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Tuggeranong United FC vs Majura FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- West Adelaide SC Reserve vs Adelaide City FC Reserve | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.1 | prob=0.3772 | EV=0.5465 | edge=0.1333 | penalty=0.5465 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- West Adelaide SC vs Adelaide City FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.1 | prob=0.3772 | EV=0.5465 | edge=0.1333 | penalty=0.5465 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
