# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-15T02:30:48.887131+00:00`
GitHub run: `350` attempt `1`
GitHub SHA: `8605718400a11f4379bd20d5d0b52814854e5baf`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 49 |  |  |
| odds-api.io forward fixtures | True | 670 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 171 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 300 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 198
- Positive EV proxy rows: 94
- Proxy observation rows: 25
- Valid forward/proxy log rows: 225
- Deduped forward/proxy log rows: 155
- Duplicate forward/proxy log rows identified: 70
- Fresh API match coverage rate: 0.1167
- Matches with fresh API price: 35
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
Current: 198 value snapshots; fresh API coverage rate 0.1167.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 155 deduped forward/proxy rows; 70 duplicate raw rows identified.
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
Upcoming fixture rows: 1137
Fixture team rows unmatched: 2158
Ready for model-fixture join: False
Automatic forward price rows: 351
odds-api.io price rows: 35
Football-Data price rows: 316
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. FC Bocholt | suggestion=nan | type=unmatched
- RW Oberhausen | suggestion=nan | type=unmatched
- 1. FC Cologne II | suggestion=nan | type=unmatched
- FC Schalke 04 II | suggestion=Schalke 04 | type=suggested_alias_needed
- 1. FC Heidenheim | suggestion=Heidenheim | type=suggested_alias_needed
- FSV Mainz | suggestion=nan | type=unmatched
- 1. FC Lokomotive Leipzig | suggestion=nan | type=unmatched
- FC Magdeburg II | suggestion=nan | type=unmatched
- 1 FC Nuremberg II | suggestion=nan | type=unmatched
- SpVgg Hankofen-Hailing | suggestion=nan | type=unmatched
- 1. FC Saarbrucken | suggestion=nan | type=unmatched
- Hansa Rostock | suggestion=nan | type=unmatched
- 1. FC Schweinfurt 05 | suggestion=nan | type=unmatched
- Erzgebirge Aue | suggestion=nan | type=unmatched
- 1. FC Slovacko Uherske Hradiste | suggestion=nan | type=unmatched
- FK Mlada Boleslav | suggestion=nan | type=unmatched
- A-Xiii Auhof Center | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 351
Value snapshot rows: 198
Matches with any automatic price: 38
Matches with fresh API price: 35
Matches with odds-api.io price: 35
Fresh API match coverage rate: 0.1167
odds-api.io match coverage rate: 0.1167
Real-money ready: False
## Match coverage
- 2026-05-16 | CD Marathon San Pedro Sula vs CD Olimpia Tegucigalpa | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Ballard FC vs FC Olympia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Essendon Royals SC U20 vs South Melbourne FC U20 | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-16 | O'Connor Knights SC vs Canberra Croatia FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-16 | Waterside Karori vs Western Suburbs FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Adelaide Atletico Victory Reserves vs Eastern United Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-16 | Nomads United AFC vs Ferrymead Bays | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Bay Olympic vs Auckland United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Bentleigh Greens SC vs Heidelberg United FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-16 | Dandenong Thunder FC vs ST Albans Saints Dinamo SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Manningham United Blues FC vs Brunswick Juventus FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-16 | Melville United AFC vs Manukau United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Selwyn United FC vs Wanaka AFC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | Sturt Lions Reserve vs Croydon Kings FC Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-16 | Tauranga City AFC vs Western Springs AFC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-16 | University of NSW vs Rockdale Ilinden FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-16 | Wellington Phoenix FC Reserve vs Island Bay United | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 351
Matched prediction rows: 48
Value snapshot rows: 198
odds-api.io snapshot rows: 117
Baseline snapshot rows: 198
Full model snapshot rows: 0
Positive EV rows: 94
Source counts: {'odds_api_io_Bet365_ML': 117, 'football_data_bet365_proxy': 27, 'football_data_max_market_proxy': 27, 'football_data_average_market_proxy': 27}
- 2026-05-16 | Waterside Karori vs Western Suburbs FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3772 | EV=5.4124 | match=1.0
- 2026-05-16 | Ballard FC vs FC Olympia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-16 | Wellington Olympic vs Petone FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-16 | O'Connor Knights SC vs Canberra Croatia FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=0.96
- 2026-05-16 | O'Connor Knights FC vs Canberra Croatia FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-16 | Cerezo Osaka Sakai Ladies vs AC Nagano Parceiro | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-16 | JEF United Ichihara Chiba vs Urawa Red Diamonds | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-16 | Bay Olympic vs Auckland United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-16 | Waterside Karori vs Western Suburbs FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.274 | EV=1.192 | match=1.0
- 2026-05-16 | Avondale FC vs Spring Hills FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-16 | Ballard FC vs FC Olympia | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.274 | EV=1.055 | match=1.0
- 2026-05-16 | Wellington Olympic vs Petone FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.274 | EV=1.055 | match=1.0
- 2026-05-16 | Lambton Jaffas FC vs Kahibah FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-16 | Tokyo Verdy Beleza vs Albirex Niigata | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-16 | Celtic vs Hearts | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-16 | O'Connor Knights FC vs Canberra Croatia FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-16 | O'Connor Knights SC vs Canberra Croatia FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=0.96

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 198
Pre-dedupe proxy candidate observation rows: 70
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-16 | Dangjin Citizen vs Daejeon Korail FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-16 | Essendon Royals SC U20 vs South Melbourne FC U20 | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-16 | Essendon Royals SC vs South Melbourne FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-16 | Fukushima United FC vs Hokkaido Consadole Sapporo | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-16 | Keilor Park SC vs Boroondara Eagles | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-16 | AS Harima Albion vs Orca Kamogawa FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-16 | Mito Hollyhock vs Tokyo Verdy | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-16 | Adamstown Rosebud FC vs Charlestown Azzurri FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-16 | Falkirk FC vs Glasgow Rangers | selection=HOME | source=football_data_average_market_proxy | odds=3.82 | prob=0.3772 | EV=0.440904 | edge=0.11542 | penalty=0.44090457636183045 | tier=proxy_watchlist | score=0.2276
- 2026-05-16 | Falkirk vs Rangers | selection=HOME | source=football_data_average_market_proxy | odds=3.82 | prob=0.3772 | EV=0.440904 | edge=0.11542 | penalty=0.44090457636183045 | tier=proxy_watchlist | score=0.2276
- 2026-05-16 | Ehime FC Ladies vs NHK Spring Yokohama FC Seagulls | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-16 | SC Wiedenbruck vs Borussia Dortmund II | selection=HOME | source=football_data_bet365_proxy | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2184

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
- ev_above_real_candidate_cap_possible_overconfidence: 8
- market_alignment_penalty_too_high_for_real_candidate: 8
- watchlist_only_pending_forward_settlement: 4
- delayed_football_data_proxy_not_fresh_api_price: 3
## Row explanations
- 2026-05-16 | Dangjin Citizen vs Daejeon Korail FC | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Essendon Royals SC U20 vs South Melbourne FC U20 | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Essendon Royals SC vs South Melbourne FC | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Fukushima United FC vs Hokkaido Consadole Sapporo | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Keilor Park SC vs Boroondara Eagles | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | AS Harima Albion vs Orca Kamogawa FC | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | Mito Hollyhock vs Tokyo Verdy | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | Adamstown Rosebud FC vs Charlestown Azzurri FC | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | Falkirk FC vs Glasgow Rangers | sel=HOME | score=0.2276 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-16 | Falkirk vs Rangers | sel=HOME | score=0.2276 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-16 | Ehime FC Ladies vs NHK Spring Yokohama FC Seagulls | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | SC Wiedenbruck vs Borussia Dortmund II | sel=HOME | score=0.2184 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 198
Paper proxy observation rows: 25
Positive EV value rows: 94
Suppressed-band observation rows: 0
Distinct matches: 19
Distinct sources: 0
Max EV: 0.747488
Average EV: 0.470835
Max probability edge: 0.149199
Average match confidence: None
## By selection
- away: rows=9, avg_ev=0.6011, max_ev=0.7475
- draw: rows=4, avg_ev=0.4042, max_ev=0.4385
- home: rows=12, avg_ev=0.3953, max_ev=0.5465

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 1137
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-16 02:15 | CD Marathon San Pedro Sula vs CD Olimpia Tegucigalpa | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 02:30 | Ballard FC vs FC Olympia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 02:30 | Essendon Royals SC U20 vs South Melbourne FC U20 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 02:30 | O'Connor Knights SC vs Canberra Croatia FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 02:30 | Waterside Karori vs Western Suburbs FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 02:45 | Adelaide Atletico Victory Reserves vs Eastern United Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 02:45 | Nomads United AFC vs Ferrymead Bays | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Bay Olympic vs Auckland United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Bentleigh Greens SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Dandenong Thunder FC vs ST Albans Saints Dinamo SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Manningham United Blues FC vs Brunswick Juventus FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Melville United AFC vs Manukau United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Selwyn United FC vs Wanaka AFC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Sturt Lions Reserve vs Croydon Kings FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Tauranga City AFC vs Western Springs AFC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | University of NSW vs Rockdale Ilinden FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:00 | Wellington Phoenix FC Reserve vs Island Bay United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:15 | Adelaide Blue Eagles Reserves vs Fulham United FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:15 | South Adelaide Reserve vs Salisbury United Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:15 | West Adelaide SC Reserve vs West Torrens Birkalla Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-16 03:45 | Wellington Olympic vs Petone FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 1147
Log type: probability_only_no_market_prices
- 2026-05-16 2026-05-16 12:00:00 | VfL Bochum II vs Fortuna Dusseldorf II | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:00:00 | VfL Sportfreunde Lotte 1929 vs Fortuna Cologne | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:00:00 | Viktoria Aschaffenburg vs Bayern Munich II | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:00:00 | VSG Altglienicke vs BFC Preussen Berlin | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:00:00 | Wuppertaler SV vs Bonner SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:00:00 | Yunnan Yukun vs Shanghai Shenhua FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:00:00 | ZFC Meuselwitz vs FSV Luckenwalde | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:30:00 | Celtic vs Hearts | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:30:00 | Chitipa United vs Civil Service United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:30:00 | Creck SC vs Kamuzu Barracks FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:30:00 | Ekhaya FC vs Moyale Barracks | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:30:00 | Falkirk vs Rangers | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:30:00 | Hibernian vs Motherwell | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:30:00 | Social Atletico Television vs Union de Santa Fe | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 12:45:00 | LKP Motor Lublin vs MKS Cracovia Krakow | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 13:00:00 | AC Horsens vs Hvidovre IF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 13:00:00 | AmaZulu FC vs Kaizer Chiefs | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 13:00:00 | AS Monaco vs Valenciennes FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 13:00:00 | AS Roma vs Genoa CFC Women | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-16 2026-05-16 13:00:00 | BK Fremad Amager vs Ishoej IF | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 1137
Manual template rows: 1137
Rows with complete manual odds: 0
Rows missing manual odds: 1137
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-16 12:00 | 1. FC Bocholt vs RW Oberhausen
- 2026-05-16 12:00 | 1. FC Cologne II vs FC Schalke 04 II
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz
- 2026-05-16 12:00 | 1. FC Lokomotive Leipzig vs FC Magdeburg II
- 2026-05-16 12:00 | 1 FC Nuremberg II vs SpVgg Hankofen-Hailing
- 2026-05-16 11:30 | 1. FC Saarbrucken vs Hansa Rostock
- 2026-05-16 11:30 | 1. FC Schweinfurt 05 vs Erzgebirge Aue
- 2026-05-16 15:00 | 1. FC Slovacko Uherske Hradiste vs FK Mlada Boleslav
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau
- 2026-05-16 19:00 | ABC FC RN vs Sousa EC PB
- 2026-05-16 18:30 | AC Goianiense GO vs Cerrado EC GO
- 2026-05-16 13:00 | AC Horsens vs Hvidovre IF
- 2026-05-16 16:00 | AC Oulu vs Turun Palloseura
- 2026-05-16 15:00 | AC Virtus vs SP La Fiorita
- 2026-05-16 15:30 | Academica de Coimbra vs CD Trofense

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 1137
Source counts: {'odds_api_io_events_bookmaker_filtered': 1030, 'football_data_fixtures_proxy': 107}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-16 12:00 | 1. FC Bocholt vs RW Oberhausen | germany-amateur-regionalliga-west | odds_api_io_events_bookmaker_filtered
- 2026-05-16 12:00 | 1. FC Cologne II vs FC Schalke 04 II | germany-amateur-regionalliga-west | odds_api_io_events_bookmaker_filtered
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz | germany-bundesliga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 12:00 | 1. FC Lokomotive Leipzig vs FC Magdeburg II | germany-amateur-regionalliga-northeast | odds_api_io_events_bookmaker_filtered
- 2026-05-16 12:00 | 1 FC Nuremberg II vs SpVgg Hankofen-Hailing | germany-amateur-regionalliga-bavaria | odds_api_io_events_bookmaker_filtered
- 2026-05-16 11:30 | 1. FC Saarbrucken vs Hansa Rostock | germany-3-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 11:30 | 1. FC Schweinfurt 05 vs Erzgebirge Aue | germany-3-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:00 | 1. FC Slovacko Uherske Hradiste vs FK Mlada Boleslav | czechia-1-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau | austria-amateur-wien-wiener-stadtliga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 19:00 | ABC FC RN vs Sousa EC PB | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-16 18:30 | AC Goianiense GO vs Cerrado EC GO | brazil-u20-goiano-1-divisao | odds_api_io_events_bookmaker_filtered
- 2026-05-16 13:00 | AC Horsens vs Hvidovre IF | denmark-1-division | odds_api_io_events_bookmaker_filtered
- 2026-05-16 16:00 | AC Oulu vs Turun Palloseura | finland-veikkausliiga | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:00 | AC Virtus vs SP La Fiorita | san-marino-campionato-sammarinese | odds_api_io_events_bookmaker_filtered
- 2026-05-16 15:30 | Academica de Coimbra vs CD Trofense | portugal-liga-portugal-3 | odds_api_io_events_bookmaker_filtered
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC | netherlands-tweede-divisie | odds_api_io_events_bookmaker_filtered
- 2026-05-16 19:00 | AD Alcorcon vs Marbella FC | spain-primera-federacion | odds_api_io_events_bookmaker_filtered
- 2026-05-16 18:00 | AD Cabofriense RJ vs Serrano FC RJ | brazil-carioca-serie-a2 | odds_api_io_events_bookmaker_filtered
- 2026-05-16 14:15 | AD Ceuta vs Malaga CF | spain-laliga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-16 04:00 | Adamstown Rosebud FC vs Charlestown Azzurri FC | australia-northern-nsw-npl | odds_api_io_events_bookmaker_filtered
- 2026-05-16 02:45 | Adelaide Atletico Victory Reserves vs Eastern United Reserve | australia-south-australia-state-league-1-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-16 05:30 | Adelaide Atletico VSC vs Eastern United | australia-south-australia-state-league-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-16 05:30 | Adelaide Blue Eagles vs Fulham United FC | australia-south-australia-state-league-1 | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 1137
Rows with complete odds: 0
- 2026-05-16 12:00 | 1. FC Bocholt vs RW Oberhausen | bookmaker=bet365_manual
- 2026-05-16 12:00 | 1. FC Cologne II vs FC Schalke 04 II | bookmaker=bet365_manual
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz | bookmaker=bet365_manual
- 2026-05-16 12:00 | 1. FC Lokomotive Leipzig vs FC Magdeburg II | bookmaker=bet365_manual
- 2026-05-16 12:00 | 1 FC Nuremberg II vs SpVgg Hankofen-Hailing | bookmaker=bet365_manual
- 2026-05-16 11:30 | 1. FC Saarbrucken vs Hansa Rostock | bookmaker=bet365_manual
- 2026-05-16 11:30 | 1. FC Schweinfurt 05 vs Erzgebirge Aue | bookmaker=bet365_manual
- 2026-05-16 15:00 | 1. FC Slovacko Uherske Hradiste vs FK Mlada Boleslav | bookmaker=bet365_manual
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau | bookmaker=bet365_manual
- 2026-05-16 19:00 | ABC FC RN vs Sousa EC PB | bookmaker=bet365_manual
- 2026-05-16 18:30 | AC Goianiense GO vs Cerrado EC GO | bookmaker=bet365_manual
- 2026-05-16 13:00 | AC Horsens vs Hvidovre IF | bookmaker=bet365_manual
- 2026-05-16 16:00 | AC Oulu vs Turun Palloseura | bookmaker=bet365_manual
- 2026-05-16 15:00 | AC Virtus vs SP La Fiorita | bookmaker=bet365_manual
- 2026-05-16 15:30 | Academica de Coimbra vs CD Trofense | bookmaker=bet365_manual
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC | bookmaker=bet365_manual
- 2026-05-16 19:00 | AD Alcorcon vs Marbella FC | bookmaker=bet365_manual
- 2026-05-16 18:00 | AD Cabofriense RJ vs Serrano FC RJ | bookmaker=bet365_manual
- 2026-05-16 14:15 | AD Ceuta vs Malaga CF | bookmaker=bet365_manual
- 2026-05-16 04:00 | Adamstown Rosebud FC vs Charlestown Azzurri FC | bookmaker=bet365_manual
- 2026-05-16 02:45 | Adelaide Atletico Victory Reserves vs Eastern United Reserve | bookmaker=bet365_manual
- 2026-05-16 05:30 | Adelaide Atletico VSC vs Eastern United | bookmaker=bet365_manual
- 2026-05-16 05:30 | Adelaide Blue Eagles vs Fulham United FC | bookmaker=bet365_manual
- 2026-05-16 03:15 | Adelaide Blue Eagles Reserves vs Fulham United FC Reserve | bookmaker=bet365_manual

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
- 2026-05-16 12:00 | 1. FC Bocholt vs RW Oberhausen
- 2026-05-16 12:00 | 1. FC Cologne II vs FC Schalke 04 II
- 2026-05-16 13:30 | 1. FC Heidenheim vs FSV Mainz
- 2026-05-16 12:00 | 1. FC Lokomotive Leipzig vs FC Magdeburg II
- 2026-05-16 12:00 | 1 FC Nuremberg II vs SpVgg Hankofen-Hailing
- 2026-05-16 11:30 | 1. FC Saarbrucken vs Hansa Rostock
- 2026-05-16 11:30 | 1. FC Schweinfurt 05 vs Erzgebirge Aue
- 2026-05-16 15:00 | 1. FC Slovacko Uherske Hradiste vs FK Mlada Boleslav
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau
- 2026-05-16 19:00 | ABC FC RN vs Sousa EC PB
- 2026-05-16 18:30 | AC Goianiense GO vs Cerrado EC GO
- 2026-05-16 13:00 | AC Horsens vs Hvidovre IF
- 2026-05-16 16:00 | AC Oulu vs Turun Palloseura
- 2026-05-16 15:00 | AC Virtus vs SP La Fiorita
- 2026-05-16 15:30 | Academica de Coimbra vs CD Trofense
- 2026-05-16 13:30 | ACV Assen vs Koninklijke HFC
- 2026-05-16 19:00 | AD Alcorcon vs Marbella FC
- 2026-05-16 18:00 | AD Cabofriense RJ vs Serrano FC RJ
- 2026-05-16 14:15 | AD Ceuta vs Malaga CF

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 228
Valid forward/proxy log rows: 225
Deduped forward/proxy observation rows: 155
Duplicate forward/proxy log rows: 70
Valid automatic proxy observation rows: 225
Deduped automatic proxy observation rows: 155
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
### Celtic vs Hearts
- Date/time: 2026-05-16 12:30
- League/phase: SC0 / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 5.01
- Fair odds: 2.87
- Model probability: 0.3488
- Probability band: 0.25-0.35
- EV: 0.7475
- Probability edge: 0.1492
- Alignment penalty: 0.7475
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0712
- Prediction ID: 9c4925d313c86ca7fa71
### FC Famalicao vs SL Benfica
- Date/time: 2026-05-16 10:00
- League/phase: portugal-u19-campeonato-nacional / automatic_forward_price_proxy
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
Total logged paper-test rows: 228
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 198, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 88, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 228, 'source_used': 'automatic_forward_value_snapshots'}
- Celtic vs Hearts | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.01 | prob=0.3488 | EV=0.7475 | edge=0.1492 | penalty=0.7475 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Famalicao vs SL Benfica | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Celtic vs Hearts | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Famalicao vs SL Benfica | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.92 | prob=0.3488 | EV=0.7161 | edge=0.1455 | penalty=0.7161 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Belmont Swansea United FC vs Valentine FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Falkirk vs Rangers | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.1 | prob=0.3772 | EV=0.5465 | edge=0.1333 | penalty=0.5465 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Falkirk FC vs Glasgow Rangers | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.1 | prob=0.3772 | EV=0.5465 | edge=0.1333 | penalty=0.5465 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Tauranga City AFC vs Western Springs AFC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.9 | prob=0.3772 | EV=0.4711 | edge=0.1208 | penalty=0.4711 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Albirex Niigata vs Nara Club | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Falkirk FC vs Glasgow Rangers | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.82 | prob=0.3772 | EV=0.4409 | edge=0.1154 | penalty=0.4409 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Falkirk vs Rangers | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.82 | prob=0.3772 | EV=0.4409 | edge=0.1154 | penalty=0.4409 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Adelaide Atletico VSC vs Eastern United | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Adelaide Atletico Victory Reserves vs Eastern United Reserve | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Dangjin Citizen vs Daejeon Korail FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.7 | prob=0.3772 | EV=0.3956 | edge=0.1069 | penalty=0.3956 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Essendon Royals SC vs South Melbourne FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Essendon Royals SC U20 vs South Melbourne FC U20 | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mynavi Sendai Ladies vs Chifure AS Elfen Saitama | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SC Wiedenbruck vs Borussia Dortmund II | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
