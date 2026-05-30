# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-30T02:28:33.782482+00:00`
GitHub run: `381` attempt `1`
GitHub SHA: `d7ed09c3ff148971965c3dfbbf90d22034e8ed32`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 30 |  |  |
| odds-api.io forward fixtures | True | 676 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 117 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 1 |  |  |
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
- Automatic value snapshots: 231
- Positive EV proxy rows: 94
- Proxy observation rows: 25
- Valid forward/proxy log rows: 816
- Deduped forward/proxy log rows: 637
- Duplicate forward/proxy log rows identified: 179
- Fresh API match coverage rate: 0.19
- Matches with fresh API price: 57
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
Current: 231 value snapshots; fresh API coverage rate 0.19.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 637 deduped forward/proxy rows; 179 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 12
Upcoming fixture rows: 12
Proxy price rows: 36
Sources attempted: 1
Errors: 0
- 2026-05-31 17:30 | Gent vs Genk | football_data_bet365_proxy | 2.9/3.75/2.2
- 2026-05-31 17:30 | Gent vs Genk | football_data_max_market_proxy | 3.0/3.75/2.25
- 2026-05-31 17:30 | Gent vs Genk | football_data_average_market_proxy | 2.89/3.55/2.19
- 2026-05-30 15:15 | Ceuta vs Albacete | football_data_bet365_proxy | 2.3/3.2/3.1
- 2026-05-30 15:15 | Ceuta vs Albacete | football_data_max_market_proxy | 2.38/3.4/3.14
- 2026-05-30 15:15 | Ceuta vs Albacete | football_data_average_market_proxy | 2.29/3.2/2.88
- 2026-05-30 15:15 | Sociedad B vs Cultural Leonesa | football_data_bet365_proxy | 2.25/3.25/3.1
- 2026-05-30 15:15 | Sociedad B vs Cultural Leonesa | football_data_max_market_proxy | 2.34/3.4/3.1
- 2026-05-30 15:15 | Sociedad B vs Cultural Leonesa | football_data_average_market_proxy | 2.25/3.24/2.91
- 2026-05-30 20:00 | Granada vs Sp Gijon | football_data_bet365_proxy | 2.32/3.4/2.75
- 2026-05-30 20:00 | Granada vs Sp Gijon | football_data_max_market_proxy | 2.46/3.4/2.95
- 2026-05-30 20:00 | Granada vs Sp Gijon | football_data_average_market_proxy | 2.34/3.24/2.76
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

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 532
Fixture team rows unmatched: 1049
Ready for model-fixture join: False
Automatic forward price rows: 93
odds-api.io price rows: 57
Football-Data price rows: 36
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- FC 1980 Wien | suggestion=nan | type=unmatched
- LAC Inter | suggestion=nan | type=unmatched
- 22 de Julio | suggestion=nan | type=unmatched
- San Antonio FC | suggestion=nan | type=unmatched
- 9 de Octubre FC | suggestion=nan | type=unmatched
- Club Deportivo Cuenca Juniors | suggestion=nan | type=unmatched
- AA Aparecidense GO | suggestion=nan | type=unmatched
- Primavera AC MT | suggestion=nan | type=unmatched
- AA Portuguesa RJ | suggestion=nan | type=unmatched
- America FC RJ | suggestion=nan | type=unmatched
- AB Argir | suggestion=nan | type=unmatched
- NSI Runavik | suggestion=nan | type=unmatched
- Abecat Ouvidorense GO | suggestion=nan | type=unmatched
- Betim Futebol MG | suggestion=nan | type=unmatched
- AC Connecticut | suggestion=nan | type=unmatched
- Boston City FC | suggestion=nan | type=unmatched
- AC Goianiense GO | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 93
Value snapshot rows: 231
Matches with any automatic price: 60
Matches with fresh API price: 57
Matches with odds-api.io price: 57
Fresh API match coverage rate: 0.19
odds-api.io match coverage rate: 0.19
Real-money ready: False
## Match coverage
- 2026-05-30 | Gamle Oslo FK vs Frigg Oslo FK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | Patriotas FC PR vs City London FC PR U20 | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-30 | SV Kuchl vs FC Lustenau | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | SV Seekirchen vs FC Dornbirn | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | Zimbabwe vs India | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | FC 1980 Wien vs LAC Inter | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | Ariana FC vs Laholms FK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | ASKO Kohfidisch vs SV Leithaprodersdorf | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | ASKO Kottmannsdorf vs SVG Bleiburg | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | FC Baden vs FC Collina D Oro | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | Bollstanas SK vs Sunnersta AIF | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | Ciudad Nueva Santa Cruz vs Virginia Usc | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | FC Concordia Basel vs Grasshopper Club Zurich II | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-30 | FC Deutschkreutz vs SV Eberau | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | FH Hafnarfjordur vs Fram | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | FK Auda Riga vs Ogre United | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-30 | FK Fyllingsdalen vs Viking FK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 93
Matched prediction rows: 61
Value snapshot rows: 231
odds-api.io snapshot rows: 177
Baseline snapshot rows: 231
Full model snapshot rows: 0
Positive EV rows: 94
Source counts: {'odds_api_io_Bet365_ML': 177, 'football_data_bet365_proxy': 18, 'football_data_max_market_proxy': 18, 'football_data_average_market_proxy': 18}
- 2026-05-30 | FH Hafnarfjordur vs Fram | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-30 | FK Auda Riga vs Ogre United | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-30 | FK Fyllingsdalen vs Viking FK | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-30 | NK Hrvatski Dragovoljac vs NK Bjelovar | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-30 | Grindavik/Njarovik vs Breidablik Kopavogur | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-30 | Zimbabwe vs India | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-30 | IF Elfsborg vs Enskede IK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-30 | Hammarby Talang FF vs AFC Eskilstuna | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-30 | Hassleholms IF vs Utsiktens BK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-30 | Gamle Oslo FK vs Frigg Oslo FK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-30 | Ariana FC vs Laholms FK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-30 | FH Hafnarfjordur vs Fram | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-30 | Molde FK vs Sandefjord Fotball | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-30 | IF Karlstad Fotbol vs Sollentuna FK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-30 | NK Trnje vs NK Dugo Selo | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3772 | EV=0.7917 | match=1.0
- 2026-05-30 | Ufc Jennersdorf vs ASK Royal Sped Klingenbach | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3772 | EV=0.7917 | match=1.0
- 2026-05-30 | VfB Hohenems vs Wacker Innsbruck | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3772 | EV=0.7917 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 231
Pre-dedupe proxy candidate observation rows: 75
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-30 | IK Kongahalla vs Astorps FF | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-30 | NK BSK Bijelo Brdo vs NK Croatia Zmijavci | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-30 | CS Minerul Lupeni vs CSM Unirea Alba Iulia | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-30 | FC Lausanne Sports vs FC Schaffhausen | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-30 | SC Cham vs FC Biel-Bienne | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-30 | Moss FK vs Stabaek IF | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-30 | NK Varteks vs NK Segesta | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-30 | ASKO Kottmannsdorf vs SVG Bleiburg | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-30 | ASKO Kohfidisch vs SV Leithaprodersdorf | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-30 | Bollstanas SK vs Sunnersta AIF | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-30 | AD Ceuta vs Albacete Balompie | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-30 | Ceuta vs Albacete | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 4
Top blocker: watchlist_only_pending_forward_settlement
Real-money ready: False
## Blocker summary
- watchlist_only_pending_forward_settlement: 6
- ev_above_real_candidate_cap_possible_overconfidence: 3
- market_alignment_penalty_too_high_for_real_candidate: 3
- edge_below_candidate_threshold: 3
## Row explanations
- 2026-05-30 | IK Kongahalla vs Astorps FF | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | NK BSK Bijelo Brdo vs NK Croatia Zmijavci | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | CS Minerul Lupeni vs CSM Unirea Alba Iulia | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | FC Lausanne Sports vs FC Schaffhausen | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | SC Cham vs FC Biel-Bienne | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | Moss FK vs Stabaek IF | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | NK Varteks vs NK Segesta | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | ASKO Kottmannsdorf vs SVG Bleiburg | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | ASKO Kohfidisch vs SV Leithaprodersdorf | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | Bollstanas SK vs Sunnersta AIF | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-30 | AD Ceuta vs Albacete Balompie | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-30 | Ceuta vs Albacete | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 231
Paper proxy observation rows: 25
Positive EV value rows: 94
Suppressed-band observation rows: 0
Distinct matches: 24
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.480552
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=6, avg_ev=0.5027, max_ev=0.744
- draw: rows=9, avg_ev=0.4309, max_ev=0.644
- home: rows=10, avg_ev=0.5119, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 532
Forward fixture prediction rows: 300
Full model prediction rows: 1
Baseline prediction rows: 299
Max forward predictions: 300
Ready for price join: True
- 2026-05-30 13:30 | Gamle Oslo FK vs Frigg Oslo FK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 13:30 | Patriotas FC PR vs City London FC PR U20 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 13:30 | SV Kuchl vs FC Lustenau | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 13:30 | SV Seekirchen vs FC Dornbirn | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 13:30 | Zimbabwe vs India | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | FC 1980 Wien vs LAC Inter | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | Ariana FC vs Laholms FK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | ASKO Kohfidisch vs SV Leithaprodersdorf | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | ASKO Kottmannsdorf vs SVG Bleiburg | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | FC Baden vs FC Collina D Oro | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | Bollstanas SK vs Sunnersta AIF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | Ciudad Nueva Santa Cruz vs Virginia Usc | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | FC Concordia Basel vs Grasshopper Club Zurich II | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | FC Deutschkreutz vs SV Eberau | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | FH Hafnarfjordur vs Fram | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | FK Auda Riga vs Ogre United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | FK Fyllingsdalen vs Viking FK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | Grindavik/Njarovik vs Breidablik Kopavogur | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | Hammarby Talang FF vs AFC Eskilstuna | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | Hassleholms IF vs Utsiktens BK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-30 14:00 | HB Torshavn vs Vikingur Gota | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 4690
Log type: probability_only_no_market_prices
- 2026-05-31 2026-05-30 05:00:00 | Macarthur Rams vs Illawarra Stingrays | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:00:00 | Montedio Yamagata vs Matsumoto Yamaga FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:00:00 | Palm Beach SC vs Virginia United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:00:00 | Shimizu S-Pulse vs Yokohama F Marinos | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:00:00 | Siheung Citizen FC vs FC Mokpo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:00:00 | ST Albans Saints Dinamo SC vs Preston Lions FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:00:00 | Tochigi SC vs AC Nagano Parceiro | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:00:00 | West Adelaide SC Reserve vs Adelaide City FC Reserve | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:00:00 | Zweigen Kanazawa vs Gainare Tottori | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 05:30:00 | Heidelberg United FC vs Dandenong Thunder FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 06:15:00 | Tuggeranong United FC vs Majura FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 06:30:00 | Darwin Hearts FC vs Palmerston Rovers | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 07:00:00 | Ipswich Knights vs North Pine | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 07:00:00 | Mitchelton FC vs SWQ Thunder FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 07:00:00 | Moreton City Excelsior vs The Gap FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 07:00:00 | North Lakes United vs MT Gravatt Hawks | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 07:00:00 | Perth Azzurri vs Sorrento FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 07:00:00 | Redcliffe Dolphins vs Springfield United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 07:00:00 | Sydney Olympic FC vs Western Sydney Wanderers Youth | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-31 2026-05-30 07:00:00 | Uwa Nedlands FC vs Balcatta FC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 532
Manual template rows: 532
Rows with complete manual odds: 0
Rows missing manual odds: 532
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-30 14:00 | FC 1980 Wien vs LAC Inter
- 2026-05-30 20:30 | 22 de Julio vs San Antonio FC
- 2026-05-30 20:30 | 9 de Octubre FC vs Club Deportivo Cuenca Juniors
- 2026-05-30 19:00 | AA Aparecidense GO vs Primavera AC MT
- 2026-05-30 22:00 | AA Portuguesa RJ vs America FC RJ
- 2026-05-30 18:00 | AB Argir vs NSI Runavik
- 2026-05-30 19:00 | Abecat Ouvidorense GO vs Betim Futebol MG
- 2026-05-30 22:00 | AC Connecticut vs Boston City FC
- 2026-05-30 19:00 | AC Goianiense GO vs Goias EC GO
- 2026-05-30 17:45 | AD Cabofriense RJ vs Audax Rio EC RJ
- 2026-05-30 14:15 | AD Ceuta vs Albacete Balompie
- 2026-05-30 20:00 | Aguia de Maraba FC PA vs Tocantinopolis EC TO
- 2026-05-30 16:00 | Al Ittihad vs AL Budaiya
- 2026-05-30 16:00 | Al-Najma Manama vs Manama Club
- 2026-05-30 21:00 | Ambassadors FC Ohio vs Flower City Union

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 532
Source counts: {'odds_api_io_events_bookmaker_filtered': 519, 'football_data_fixtures_proxy': 12, 'odds_api_io_events_search': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-30 14:00 | FC 1980 Wien vs LAC Inter | austria-amateur-wien-wiener-stadtliga | odds_api_io_events_bookmaker_filtered
- 2026-05-30 20:30 | 22 de Julio vs San Antonio FC | ecuador-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-30 20:30 | 9 de Octubre FC vs Club Deportivo Cuenca Juniors | ecuador-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-30 19:00 | AA Aparecidense GO vs Primavera AC MT | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-30 22:00 | AA Portuguesa RJ vs America FC RJ | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-30 18:00 | AB Argir vs NSI Runavik | faroe-islands-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-30 19:00 | Abecat Ouvidorense GO vs Betim Futebol MG | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-30 22:00 | AC Connecticut vs Boston City FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-30 19:00 | AC Goianiense GO vs Goias EC GO | brazil-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-30 17:45 | AD Cabofriense RJ vs Audax Rio EC RJ | brazil-carioca-serie-a2 | odds_api_io_events_bookmaker_filtered
- 2026-05-30 14:15 | AD Ceuta vs Albacete Balompie | spain-laliga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-30 20:00 | Aguia de Maraba FC PA vs Tocantinopolis EC TO | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-30 16:00 | Al Ittihad vs AL Budaiya | bahrain-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-30 16:00 | Al-Najma Manama vs Manama Club | bahrain-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-30 21:00 | Ambassadors FC Ohio vs Flower City Union | usa-national-premier-soccer-league | odds_api_io_events_bookmaker_filtered
- 2026-05-30 23:30 | Annapolis Blues FC vs Virginia Beach United | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-30 20:00 | AO Itabaiana SE vs Volta Redonda FC RJ | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-30 18:30 | Argentino de Rosario vs Club Estrella Del Sur (Alejandro Korn) | argentina-primera-c | odds_api_io_events_bookmaker_filtered
- 2026-05-30 14:00 | Ariana FC vs Laholms FK | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-30 14:00 | ASKO Kohfidisch vs SV Leithaprodersdorf | austria-amateur-burgenland-burgenlandliga | odds_api_io_events_bookmaker_filtered
- 2026-05-30 14:00 | ASKO Kottmannsdorf vs SVG Bleiburg | austria-amateur-karnten-karntner-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-30 16:00 | Asociacion Deportiva Tarma vs Cusco FC | peru-liga-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-30 21:00 | Athletic Club Sjdr MG vs Fortaleza EC CE | brazil-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 532
Rows with complete odds: 0
- 2026-05-30 14:00 | FC 1980 Wien vs LAC Inter | bookmaker=bet365_manual
- 2026-05-30 20:30 | 22 de Julio vs San Antonio FC | bookmaker=bet365_manual
- 2026-05-30 20:30 | 9 de Octubre FC vs Club Deportivo Cuenca Juniors | bookmaker=bet365_manual
- 2026-05-30 19:00 | AA Aparecidense GO vs Primavera AC MT | bookmaker=bet365_manual
- 2026-05-30 22:00 | AA Portuguesa RJ vs America FC RJ | bookmaker=bet365_manual
- 2026-05-30 18:00 | AB Argir vs NSI Runavik | bookmaker=bet365_manual
- 2026-05-30 19:00 | Abecat Ouvidorense GO vs Betim Futebol MG | bookmaker=bet365_manual
- 2026-05-30 22:00 | AC Connecticut vs Boston City FC | bookmaker=bet365_manual
- 2026-05-30 19:00 | AC Goianiense GO vs Goias EC GO | bookmaker=bet365_manual
- 2026-05-30 17:45 | AD Cabofriense RJ vs Audax Rio EC RJ | bookmaker=bet365_manual
- 2026-05-30 14:15 | AD Ceuta vs Albacete Balompie | bookmaker=bet365_manual
- 2026-05-30 20:00 | Aguia de Maraba FC PA vs Tocantinopolis EC TO | bookmaker=bet365_manual
- 2026-05-30 16:00 | Al Ittihad vs AL Budaiya | bookmaker=bet365_manual
- 2026-05-30 16:00 | Al-Najma Manama vs Manama Club | bookmaker=bet365_manual
- 2026-05-30 21:00 | Ambassadors FC Ohio vs Flower City Union | bookmaker=bet365_manual
- 2026-05-30 23:30 | Annapolis Blues FC vs Virginia Beach United | bookmaker=bet365_manual
- 2026-05-30 20:00 | AO Itabaiana SE vs Volta Redonda FC RJ | bookmaker=bet365_manual
- 2026-05-30 18:30 | Argentino de Rosario vs Club Estrella Del Sur (Alejandro Korn) | bookmaker=bet365_manual
- 2026-05-30 14:00 | Ariana FC vs Laholms FK | bookmaker=bet365_manual
- 2026-05-30 14:00 | ASKO Kohfidisch vs SV Leithaprodersdorf | bookmaker=bet365_manual
- 2026-05-30 14:00 | ASKO Kottmannsdorf vs SVG Bleiburg | bookmaker=bet365_manual
- 2026-05-30 16:00 | Asociacion Deportiva Tarma vs Cusco FC | bookmaker=bet365_manual
- 2026-05-30 21:00 | Athletic Club Sjdr MG vs Fortaleza EC CE | bookmaker=bet365_manual
- 2026-05-30 19:00 | Avai FC SC vs Criciuma EC SC | bookmaker=bet365_manual

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
- 2026-05-30 14:00 | FC 1980 Wien vs LAC Inter
- 2026-05-30 20:30 | 22 de Julio vs San Antonio FC
- 2026-05-30 20:30 | 9 de Octubre FC vs Club Deportivo Cuenca Juniors
- 2026-05-30 19:00 | AA Aparecidense GO vs Primavera AC MT
- 2026-05-30 22:00 | AA Portuguesa RJ vs America FC RJ
- 2026-05-30 18:00 | AB Argir vs NSI Runavik
- 2026-05-30 19:00 | Abecat Ouvidorense GO vs Betim Futebol MG
- 2026-05-30 22:00 | AC Connecticut vs Boston City FC
- 2026-05-30 19:00 | AC Goianiense GO vs Goias EC GO
- 2026-05-30 17:45 | AD Cabofriense RJ vs Audax Rio EC RJ
- 2026-05-30 14:15 | AD Ceuta vs Albacete Balompie
- 2026-05-30 20:00 | Aguia de Maraba FC PA vs Tocantinopolis EC TO
- 2026-05-30 16:00 | Al Ittihad vs AL Budaiya
- 2026-05-30 16:00 | Al-Najma Manama vs Manama Club
- 2026-05-30 21:00 | Ambassadors FC Ohio vs Flower City Union
- 2026-05-30 23:30 | Annapolis Blues FC vs Virginia Beach United
- 2026-05-30 20:00 | AO Itabaiana SE vs Volta Redonda FC RJ
- 2026-05-30 18:30 | Argentino de Rosario vs Club Estrella Del Sur (Alejandro Korn)
- 2026-05-30 14:00 | Ariana FC vs Laholms FK

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 819
Valid forward/proxy log rows: 816
Deduped forward/proxy observation rows: 637
Duplicate forward/proxy log rows: 179
Valid automatic proxy observation rows: 816
Deduped automatic proxy observation rows: 637
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
### NK Trnje vs NK Dugo Selo
- Date/time: 2026-05-30 14:00
- League/phase: croatia-druga-nl / automatic_forward_price_proxy
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
- Prediction ID: 74de2fa5b80706c2e2f7
### Ufc Jennersdorf vs ASK Royal Sped Klingenbach
- Date/time: 2026-05-30 14:00
- League/phase: austria-amateur-burgenland-burgenlandliga / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.75
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
Newly logged paper-test picks: 25
Total logged paper-test rows: 819
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 231, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 97, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 819, 'source_used': 'automatic_forward_value_snapshots'}
- NK Trnje vs NK Dugo Selo | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ufc Jennersdorf vs ASK Royal Sped Klingenbach | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- VfB Hohenems vs Wacker Innsbruck | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Stjarnan vs IBV Vestmannaeyjar | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Mendrisio vs AC Taverne | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Odds BK vs Lyn 1896 FK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Club Deportivo Libertad FC vs Club Deportivo Amanecer | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.1 | prob=0.3772 | EV=0.5465 | edge=0.1333 | penalty=0.5465 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SV Kuchl vs FC Lustenau | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Meyrin vs CS Chenois | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Auda Riga vs Ogre United | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Fyllingsdalen vs Viking FK | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.75 | prob=0.274 | EV=0.5755 | edge=0.1001 | penalty=0.5755 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Telavi vs FC Gori | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- IK Kongahalla vs Astorps FF | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- NK Hrvace vs NK Dubrava Zagreb | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- IF Elfsborg vs Enskede IK | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Grindavik/Njarovik vs Breidablik Kopavogur | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gamle Oslo FK vs Frigg Oslo FK | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- NK BSK Bijelo Brdo vs NK Croatia Zmijavci | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.4 | prob=0.3772 | EV=0.2825 | edge=0.0831 | penalty=0.2825 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
