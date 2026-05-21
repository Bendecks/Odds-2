# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-20T14:43:42.111213+00:00`
GitHub run: `362` attempt `1`
GitHub SHA: `96df83d4c1940399b1efbb86e1b5657185cf5a12`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 6 |  |  |
| Football-Data upcoming odds proxy | True | 15 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 0 |  |  |
| odds-api.io forward fixtures | True | 0 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 45 |  |  |
| Forward price coverage report | True | 7 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 3 |  |  |
| Proxy candidate observations | True | 8 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 8 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 7 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 264
- Positive EV proxy rows: 134
- Proxy observation rows: 25
- Valid forward/proxy log rows: 433
- Deduped forward/proxy log rows: 304
- Duplicate forward/proxy log rows identified: 129
- Fresh API match coverage rate: 0.1833
- Matches with fresh API price: 55
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
Current: 264 value snapshots; fresh API coverage rate 0.1833.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 304 deduped forward/proxy rows; 129 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 11
Upcoming fixture rows: 6
Proxy price rows: 15
Sources attempted: 1
Errors: 0
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_bet365_proxy | 2.2/3.75/3.0
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_max_market_proxy | 2.2/3.75/3.1
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_average_market_proxy | 2.14/3.61/2.92
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_bet365_proxy | 4.5/3.7/1.75
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_max_market_proxy | 4.6/3.8/1.8
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_average_market_proxy | 4.32/3.61/1.73
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_bet365_proxy | 7.0/4.75/1.38
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_max_market_proxy | 7.0/5.25/1.41
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_average_market_proxy | 6.57/5.0/1.37
- 2026-05-21 16:00 | Atromitos vs Panserraikos | football_data_max_market_proxy | 1.67/4.0/6.0
- 2026-05-21 16:00 | Atromitos vs Panserraikos | football_data_average_market_proxy | 1.57/3.71/5.28
- 2026-05-21 17:00 | Kifisia vs Larisa | football_data_max_market_proxy | 2.3/3.25/3.2
- 2026-05-21 17:00 | Kifisia vs Larisa | football_data_average_market_proxy | 2.22/3.13/2.98
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis | football_data_max_market_proxy | 2.4/3.3/3.05
- 2026-05-21 17:00 | Panetolikos vs Asteras Tripolis | football_data_average_market_proxy | 2.29/3.13/2.9

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 611
Fixture team rows unmatched: 1199
Ready for model-fixture join: False
Automatic forward price rows: 70
odds-api.io price rows: 55
Football-Data price rows: 15
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- A Sakiet Edayer | suggestion=nan | type=unmatched
- JS Omrane | suggestion=nan | type=unmatched
- Academia Puerto Cabello | suggestion=nan | type=unmatched
- CA Juventud de Las Piedras | suggestion=nan | type=unmatched
- Acao Futebol MT | suggestion=nan | type=unmatched
- SC Recife PE | suggestion=nan | type=unmatched
- Adama City FC | suggestion=nan | type=unmatched
- Welwalo Adigrat | suggestion=nan | type=unmatched
- AE Kifisia FC | suggestion=nan | type=unmatched
- AE Larissa FC | suggestion=nan | type=unmatched
- Aguilas Doradas Rionegro | suggestion=nan | type=unmatched
- Deportivo Pereira FC SA | suggestion=nan | type=unmatched
- Ajax Amsterdam | suggestion=nan | type=unmatched
- FC Groningen | suggestion=nan | type=unmatched
- Al Arabi | suggestion=nan | type=unmatched
- AL Tadhamon | suggestion=nan | type=unmatched
- AL Budaiya | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 70
Value snapshot rows: 264
Matches with any automatic price: 61
Matches with fresh API price: 55
Matches with odds-api.io price: 55
Fresh API match coverage rate: 0.1833
odds-api.io match coverage rate: 0.1833
Real-money ready: False
## Match coverage
- 2026-05-21 | Khangarid vs Central Stallions FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Maccabi Petah Tikva vs Beitar Jerusalem | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-21 | Libertad Asuncion vs Sportivo Trinidense | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-21 | Adama City FC vs Welwalo Adigrat | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Arba Minch Ketema vs Sidama Bunna SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | FC Shakhtar Donetsk vs Kolos Kovalivka | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Cabrayil vs Simal | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | FC Fard Alborz vs FC Pars Jonoubi Jam | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Jkt Tanzania vs Fountain Gate FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Moik Baku vs Difai Agsu | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Resistencia SC vs Club General Caballero JLM | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Mes Shahr-e Babak vs Shahrdari Nowshahr | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Nassaji Mazandaran FC vs Navad Urmia FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Inter Kashi FC vs SC East Bengal | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Jamshedpur FC vs Odisha FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Mohun Bagan Super Giant vs Sporting Club Delhi | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-21 | Punjab FC vs Mumbai City | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 70
Matched prediction rows: 64
Value snapshot rows: 264
odds-api.io snapshot rows: 174
Baseline snapshot rows: 264
Full model snapshot rows: 0
Positive EV rows: 134
Source counts: {'odds_api_io_Bet365_ML': 174, 'football_data_max_market_proxy': 36, 'football_data_average_market_proxy': 36, 'football_data_bet365_proxy': 18}
- 2026-05-21 | Grei Kvinner Elite FK vs Lyn | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3772 | EV=5.4124 | match=1.0
- 2026-05-21 | VIFK vs Aaland United | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-05-21 | Al Nassr Club vs Damac FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-05-21 | Mohun Bagan Super Giant vs Sporting Club Delhi | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-21 | FC RFS vs FS Jelgava | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-21 | Al Arabi vs AL Tadhamon | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-21 | Al-Fahaheel vs Kuwait SC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3772 | EV=2.5834 | match=1.0
- 2026-05-21 | Coastal Union FC vs Simba SC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3772 | EV=2.5834 | match=1.0
- 2026-05-21 | Qatar vs Sudan | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-05-21 | Al-Fayha FC vs Al Hilal SFC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-21 | Stade Malien de Bamako vs US Bougouni | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-21 | FC Shakhtar Donetsk vs Kolos Kovalivka | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-21 | Inter Kashi FC vs SC East Bengal | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-21 | Nassaji Mazandaran FC vs Navad Urmia FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-21 | Yellow-Red KV Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=0.96
- 2026-05-21 | Yellow-Red KV Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=0.96
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 264
Pre-dedupe proxy candidate observation rows: 90
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 1
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-21 | Al-Hazm vs Al-Taawoun FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-21 | A Sakiet Edayer vs JS Omrane | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-21 | IK Tord vs Skara FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-21 | SK Treibach vs FC Gleisdorf 09 | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-21 | Khangarid vs Central Stallions FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-21 | Broendby IF vs FC Copenhagen | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-21 | Cabrayil vs Simal | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-21 | IF Elfsborg vs Mjallby AIF | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-21 | Adama City FC vs Welwalo Adigrat | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-21 | KAA Gent vs Union Saint-Gilloise | selection=HOME | source=football_data_average_market_proxy | odds=4.32 | prob=0.3772 | EV=0.629504 | edge=0.145719 | penalty=0.6295073893753698 | tier=proxy_watchlist | score=0.1903
- 2026-05-21 | Gent vs St. Gilloise | selection=HOME | source=football_data_average_market_proxy | odds=4.32 | prob=0.3772 | EV=0.629504 | edge=0.145719 | penalty=0.6295073893753698 | tier=proxy_watchlist | score=0.1903
- 2026-05-21 | Ajax Amsterdam vs FC Groningen | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244

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
- ev_above_real_candidate_cap_possible_overconfidence: 9
- market_alignment_penalty_too_high_for_real_candidate: 9
- edge_below_candidate_threshold: 3
- delayed_football_data_proxy_not_fresh_api_price: 2
- probability_or_league_rule_suppressed: 1
- low_probability_band_under_0_35: 1
## Row explanations
- 2026-05-21 | Al-Hazm vs Al-Taawoun FC | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-21 | A Sakiet Edayer vs JS Omrane | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-21 | IK Tord vs Skara FC | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-21 | SK Treibach vs FC Gleisdorf 09 | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-21 | Khangarid vs Central Stallions FC | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-21 | Broendby IF vs FC Copenhagen | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-21 | Cabrayil vs Simal | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-21 | IF Elfsborg vs Mjallby AIF | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-21 | Adama City FC vs Welwalo Adigrat | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-21 | KAA Gent vs Union Saint-Gilloise | sel=HOME | score=0.1903 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Gent vs St. Gilloise | sel=HOME | score=0.1903 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Ajax Amsterdam vs FC Groningen | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 264
Paper proxy observation rows: 25
Positive EV value rows: 134
Suppressed-band observation rows: 0
Distinct matches: 21
Distinct sources: 0
Max EV: 0.744
Average EV: 0.461647
Max probability edge: 0.159809
Average match confidence: None
## By selection
- away: rows=6, avg_ev=0.4843, max_ev=0.744
- draw: rows=8, avg_ev=0.4128, max_ev=0.507
- home: rows=11, avg_ev=0.4848, max_ev=0.7351

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 611
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-21 07:00 | Khangarid vs Central Stallions FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 08:00 | Maccabi Petah Tikva vs Beitar Jerusalem | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 11:30 | Libertad Asuncion vs Sportivo Trinidense | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 12:00 | Adama City FC vs Welwalo Adigrat | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 12:00 | Arba Minch Ketema vs Sidama Bunna SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 12:30 | FC Shakhtar Donetsk vs Kolos Kovalivka | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 13:00 | Cabrayil vs Simal | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 13:00 | FC Fard Alborz vs FC Pars Jonoubi Jam | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 13:00 | Jkt Tanzania vs Fountain Gate FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 13:00 | Moik Baku vs Difai Agsu | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 13:00 | Resistencia SC vs Club General Caballero JLM | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 13:15 | Mes Shahr-e Babak vs Shahrdari Nowshahr | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 13:15 | Nassaji Mazandaran FC vs Navad Urmia FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 14:00 | Inter Kashi FC vs SC East Bengal | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 14:00 | Jamshedpur FC vs Odisha FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 14:00 | Mohun Bagan Super Giant vs Sporting Club Delhi | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 14:00 | Punjab FC vs Mumbai City | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 14:00 | VIFK vs Aaland United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 14:30 | A Sakiet Edayer vs JS Omrane | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 14:30 | FC Talant vs FC Asia Talas | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-21 15:00 | Atromitos Athinon vs Panserraikos FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 2758
Log type: probability_only_no_market_prices
- 2026-05-23 2026-05-21 07:00:00 | Canterbury Bankstown FC vs Northern Tigers | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Central Coast United FC vs Bonnyrigg W. E. | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Fremantle City vs Perth Glory FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Hawkesbury City SC vs Dunbar Rovers FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Hills United FC Brumbies vs Blacktown Spartans | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Holland Park Hawks vs Sunshine Coast Wanderers | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Inner West Hawks FC vs Bankstown United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Inter Lions FC vs Bull FC Academy | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | North Star FC vs Logan Lightning | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Peninsula Power FC vs Magic United Tfa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Sorrento FC vs Olympic Kingsway SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:00:00 | Stirling Macedonia FC vs Bayswater City | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:30:00 | Gyeongnam FC vs Suwon FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 07:30:00 | Jeonnam Dragons vs Gimhae FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 08:00:00 | Brisbane Strikers FC vs Capalaba Bulldogs | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 08:00:00 | Broadbeach United vs Redlands United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 08:00:00 | CSC 1599 Selimbar vs CS Dinamo Bucuresti | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 08:00:00 | Mitchelton FC vs Moreton City Excelsior FC 2 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 08:00:00 | Taringa Rovers SFC vs Souths United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-21 08:00:00 | Tigers FC vs Brindabella Blues FC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 611
Manual template rows: 611
Rows with complete manual odds: 0
Rows missing manual odds: 611
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-21 14:30 | A Sakiet Edayer vs JS Omrane
- 2026-05-21 22:00 | Academia Puerto Cabello vs CA Juventud de Las Piedras
- 2026-05-21 19:00 | Acao Futebol MT vs SC Recife PE
- 2026-05-21 12:00 | Adama City FC vs Welwalo Adigrat
- 2026-05-21 16:00 | AE Kifisia FC vs AE Larissa FC
- 2026-05-21 20:30 | Aguilas Doradas Rionegro vs Deportivo Pereira FC SA
- 2026-05-21 16:45 | Ajax Amsterdam vs FC Groningen
- 2026-05-21 16:15 | Al Arabi vs AL Tadhamon
- 2026-05-21 16:00 | AL Budaiya vs Manama Club
- 2026-05-21 18:00 | Al Nassr Club vs Damac FC
- 2026-05-21 17:20 | Al-Fahaheel vs Kuwait SC
- 2026-05-21 18:00 | Al-Fayha FC vs Al Hilal SFC
- 2026-05-21 18:00 | Al-Hazm vs Al-Taawoun FC
- 2026-05-21 18:00 | Al-Ittihad Club vs Al Qadsiah
- 2026-05-21 18:00 | Al-Kholood vs Al-Fateh SC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 611
Source counts: {'odds_api_io_events_bookmaker_filtered': 604, 'football_data_fixtures_proxy': 6, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-21 14:30 | A Sakiet Edayer vs JS Omrane | tunisia-tunisian-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-21 22:00 | Academia Puerto Cabello vs CA Juventud de Las Piedras | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered
- 2026-05-21 19:00 | Acao Futebol MT vs SC Recife PE | brazil-brasileiro-serie-a2-women | odds_api_io_events_bookmaker_filtered
- 2026-05-21 12:00 | Adama City FC vs Welwalo Adigrat | ethiopia-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 16:00 | AE Kifisia FC vs AE Larissa FC | greece-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 20:30 | Aguilas Doradas Rionegro vs Deportivo Pereira FC SA | colombia-copa-colombia | odds_api_io_events_bookmaker_filtered
- 2026-05-21 16:45 | Ajax Amsterdam vs FC Groningen | netherlands-eredivisie | odds_api_io_events_bookmaker_filtered
- 2026-05-21 16:15 | Al Arabi vs AL Tadhamon | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 16:00 | AL Budaiya vs Manama Club | bahrain-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 18:00 | Al Nassr Club vs Damac FC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 17:20 | Al-Fahaheel vs Kuwait SC | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 18:00 | Al-Fayha FC vs Al Hilal SFC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 18:00 | Al-Hazm vs Al-Taawoun FC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 18:00 | Al-Ittihad Club vs Al Qadsiah | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 18:00 | Al-Kholood vs Al-Fateh SC | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 16:00 | Al-Najma Manama vs Al Ittihad | bahrain-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 18:00 | Al-Riyadh SC vs Al-Okhdood Club | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 20:00 | Alafoss vs Ellidi | iceland-4-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-21 23:00 | Anapolis FC GO vs Rio Branco AC ES | brazil-copa-verde | odds_api_io_events_bookmaker_filtered
- 2026-05-21 19:30 | Anderlecht vs St Truiden | B1 | football_data_fixtures_proxy
- 2026-05-21 12:00 | Arba Minch Ketema vs Sidama Bunna SC | ethiopia-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-21 16:00 | Atlantis FC/2 vs Toolon Taisto | finland-kolmonen | odds_api_io_events_bookmaker_filtered
- 2026-05-21 22:00 | Atletico Mineiro MG vs CS Cienciano | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 611
Rows with complete odds: 0
- 2026-05-21 14:30 | A Sakiet Edayer vs JS Omrane | bookmaker=bet365_manual
- 2026-05-21 22:00 | Academia Puerto Cabello vs CA Juventud de Las Piedras | bookmaker=bet365_manual
- 2026-05-21 19:00 | Acao Futebol MT vs SC Recife PE | bookmaker=bet365_manual
- 2026-05-21 12:00 | Adama City FC vs Welwalo Adigrat | bookmaker=bet365_manual
- 2026-05-21 16:00 | AE Kifisia FC vs AE Larissa FC | bookmaker=bet365_manual
- 2026-05-21 20:30 | Aguilas Doradas Rionegro vs Deportivo Pereira FC SA | bookmaker=bet365_manual
- 2026-05-21 16:45 | Ajax Amsterdam vs FC Groningen | bookmaker=bet365_manual
- 2026-05-21 16:15 | Al Arabi vs AL Tadhamon | bookmaker=bet365_manual
- 2026-05-21 16:00 | AL Budaiya vs Manama Club | bookmaker=bet365_manual
- 2026-05-21 18:00 | Al Nassr Club vs Damac FC | bookmaker=bet365_manual
- 2026-05-21 17:20 | Al-Fahaheel vs Kuwait SC | bookmaker=bet365_manual
- 2026-05-21 18:00 | Al-Fayha FC vs Al Hilal SFC | bookmaker=bet365_manual
- 2026-05-21 18:00 | Al-Hazm vs Al-Taawoun FC | bookmaker=bet365_manual
- 2026-05-21 18:00 | Al-Ittihad Club vs Al Qadsiah | bookmaker=bet365_manual
- 2026-05-21 18:00 | Al-Kholood vs Al-Fateh SC | bookmaker=bet365_manual
- 2026-05-21 16:00 | Al-Najma Manama vs Al Ittihad | bookmaker=bet365_manual
- 2026-05-21 18:00 | Al-Riyadh SC vs Al-Okhdood Club | bookmaker=bet365_manual
- 2026-05-21 20:00 | Alafoss vs Ellidi | bookmaker=bet365_manual
- 2026-05-21 23:00 | Anapolis FC GO vs Rio Branco AC ES | bookmaker=bet365_manual
- 2026-05-21 19:30 | Anderlecht vs St Truiden | bookmaker=bet365_manual
- 2026-05-21 12:00 | Arba Minch Ketema vs Sidama Bunna SC | bookmaker=bet365_manual
- 2026-05-21 16:00 | Atlantis FC/2 vs Toolon Taisto | bookmaker=bet365_manual
- 2026-05-21 22:00 | Atletico Mineiro MG vs CS Cienciano | bookmaker=bet365_manual
- 2026-05-21 16:00 | Atromitos vs Panserraikos | bookmaker=bet365_manual

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
- 2026-05-21 14:30 | A Sakiet Edayer vs JS Omrane
- 2026-05-21 22:00 | Academia Puerto Cabello vs CA Juventud de Las Piedras
- 2026-05-21 19:00 | Acao Futebol MT vs SC Recife PE
- 2026-05-21 12:00 | Adama City FC vs Welwalo Adigrat
- 2026-05-21 16:00 | AE Kifisia FC vs AE Larissa FC
- 2026-05-21 20:30 | Aguilas Doradas Rionegro vs Deportivo Pereira FC SA
- 2026-05-21 16:45 | Ajax Amsterdam vs FC Groningen
- 2026-05-21 16:15 | Al Arabi vs AL Tadhamon
- 2026-05-21 16:00 | AL Budaiya vs Manama Club
- 2026-05-21 18:00 | Al Nassr Club vs Damac FC
- 2026-05-21 17:20 | Al-Fahaheel vs Kuwait SC
- 2026-05-21 18:00 | Al-Fayha FC vs Al Hilal SFC
- 2026-05-21 18:00 | Al-Hazm vs Al-Taawoun FC
- 2026-05-21 18:00 | Al-Ittihad Club vs Al Qadsiah
- 2026-05-21 18:00 | Al-Kholood vs Al-Fateh SC
- 2026-05-21 16:00 | Al-Najma Manama vs Al Ittihad
- 2026-05-21 18:00 | Al-Riyadh SC vs Al-Okhdood Club
- 2026-05-21 20:00 | Alafoss vs Ellidi
- 2026-05-21 23:00 | Anapolis FC GO vs Rio Branco AC ES

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 436
Valid forward/proxy log rows: 433
Deduped forward/proxy observation rows: 304
Duplicate forward/proxy log rows: 129
Valid automatic proxy observation rows: 433
Deduped automatic proxy observation rows: 304
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-21 | AL Budaiya vs Manama Club | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.058600000000000006
- 2026-05-15 | Brisbane Roar FC vs Lions FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Broadmeadow Magic FC vs Newcastle Olympic FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Semen Padang FC vs Persebaya Surabaya | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-19 | Northeast United FC vs Mohammedan SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-15 | Cong An TP Ho Chi Minh City FC vs SHB Da Nang | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-19 | Derby Academie vs Onze Createurs | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Al Kahrabaa SC vs Al-Gharraf SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Diyala FC vs Amanat Baghdad SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Deportivo Capiata vs Club Fernando de La Mora | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.056100000000000004
- 2026-05-19 | SV Ried vs Wolfsberger AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-21 | Kifisia vs Larisa | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553
- 2026-05-21 | Anderlecht vs St Truiden | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0546
- 2026-05-21 | Panetolikos vs Asteras Tripolis | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054
- 2026-05-21 | Atromitos vs Panserraikos | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0533

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
### Gent vs St. Gilloise
- Date/time: 2026-05-21 19:30
- League/phase: B1 / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.6
- Fair odds: 2.65
- Model probability: 0.3772
- Probability band: 0.35-0.45
- EV: 0.7351
- Probability edge: 0.1598
- Alignment penalty: 0.7351
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0721
- Prediction ID: 0feb27e53c2d790d6c02
### KAA Gent vs Union Saint-Gilloise
- Date/time: 2026-05-21 18:30
- League/phase: belgium-pro-league / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.6
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
Newly logged paper-test picks: 18
Total logged paper-test rows: 436
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 264, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 105, 'current_paper_picks': 25, 'newly_logged_picks': 18, 'total_logged_paper_rows': 436, 'source_used': 'automatic_forward_value_snapshots'}
- Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- KAA Gent vs Union Saint-Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- KAA Gent vs Union Saint-Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Arba Minch Ketema vs Sidama Bunna SC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Jkt Tanzania vs Fountain Gate FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Negelle Arsi vs Shire Endaselassie FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Lasten vs Ylojarvi United FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al-Hazm vs Al-Taawoun FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.1105 | penalty=0.4145 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ajax Amsterdam vs FC Groningen | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mohun Bagan Super Giant vs Sporting Club Delhi | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- IK Tord vs Skara FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- A Sakiet Edayer vs JS Omrane | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Yellow-Red KV Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al Arabi vs AL Tadhamon | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SK Treibach vs FC Gleisdorf 09 | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.4 | prob=0.3772 | EV=0.2825 | edge=0.0831 | penalty=0.2825 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al-Riyadh SC vs Al-Okhdood Club | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
