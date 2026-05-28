# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-28T02:29:24.777886+00:00`
GitHub run: `377` attempt `1`
GitHub SHA: `362761c2d9d65f16de150cc4228a45c1b015b8f0`
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
| odds-api.io forward fixtures | True | 332 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 147 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
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
- Forward fixture predictions: 300
- Automatic value snapshots: 132
- Positive EV proxy rows: 64
- Proxy observation rows: 25
- Valid forward/proxy log rows: 717
- Deduped forward/proxy log rows: 546
- Duplicate forward/proxy log rows identified: 171
- Fresh API match coverage rate: 0.1467
- Matches with fresh API price: 44
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
Current: 132 value snapshots; fresh API coverage rate 0.1467.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 546 deduped forward/proxy rows; 171 duplicate raw rows identified.
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
Upcoming fixture rows: 474
Fixture team rows unmatched: 944
Ready for model-fixture join: False
Automatic forward price rows: 44
odds-api.io price rows: 44
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. FC Lokomotive Leipzig | suggestion=nan | type=unmatched
- FC Wurzburger Kickers | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Parma Calcio 1913 U20 | suggestion=nan | type=unmatched
- Al-Fahaheel | suggestion=nan | type=unmatched
- Al-Salmiya SC | suggestion=nan | type=unmatched
- Assyriska FF | suggestion=nan | type=unmatched
- Vasalunds IF | suggestion=nan | type=unmatched
- Atletico Mineiro MG | suggestion=nan | type=unmatched
- EC Vitoria BA | suggestion=nan | type=unmatched
- CA Aldosivi Reserve | suggestion=nan | type=unmatched
- CA Talleres de Cordoba Reserve | suggestion=nan | type=unmatched
- CA Lanus | suggestion=nan | type=unmatched
- CA Platense | suggestion=nan | type=unmatched
- CA Piauiense PI | suggestion=nan | type=unmatched
- Santos FC SP | suggestion=nan | type=unmatched
- CA River Plate (Arg) | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 44
Value snapshot rows: 132
Matches with any automatic price: 44
Matches with fresh API price: 44
Matches with odds-api.io price: 44
Fresh API match coverage rate: 0.1467
odds-api.io match coverage rate: 0.1467
Real-money ready: False
## Match coverage
- 2026-05-28 | Mikkelin Pallo-Kissat vs HaPK Edustus | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Deportivo Maldonado Reserve vs Liverpool Montevideo | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-28 | Puskas Akademia Felcsut vs Ferencvarosi Budapest | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FC Tallinn vs Maardu Linnameeskond | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FC Torpedo Kutaisi vs FC Gagra | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FC Ylivieska vs Lapuan Virkia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Al-Fahaheel vs Al-Salmiya SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Kolding IF vs Dbk Fortuna Hjoerring | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FCM Traiskirchen vs SC Neusiedl am See 1919 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | PPJ/Ruoholahti vs Mps | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Ylojarvi United FC vs FC Haka J | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Assyriska FF vs Vasalunds IF | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Hedensted IF vs Fuglebakken KFUM | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Zakho FC vs Erbil SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-28 | CA Lanus vs CA Platense | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 44
Matched prediction rows: 44
Value snapshot rows: 132
odds-api.io snapshot rows: 132
Baseline snapshot rows: 132
Full model snapshot rows: 0
Positive EV rows: 64
Source counts: {'odds_api_io_Bet365_ML': 132}
- 2026-05-28 | Cruzeiro EC MG vs Doce Mel EC BA | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3488 | EV=13.3008 | match=1.0
- 2026-05-28 | Cruzeiro EC MG vs Doce Mel EC BA | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.274 | EV=3.658 | match=1.0
- 2026-05-28 | SE Palmeiras SP vs CD Junior FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-29 | CA Tigre vs Alianza Atletico | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-29 | Cruzeiro EC MG vs Barcelona SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-05-29 | Edgewater Castle vs Sueno FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-29 | Manukau United FC vs Fencibles United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-28 | CD El Nacional vs CD Universidad Catolica del Ecuador | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-28 | Patuxent Football Athletics vs Annapolis Blues FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-28 | Atletico Mineiro MG vs EC Vitoria BA | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-28 | Llaneros FC vs Independiente Santa Fe | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3772 | EV=1.829 | match=1.0
- 2026-05-29 | Western Springs AFC vs Bay Olympic | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-28 | FC Torpedo Kutaisi vs FC Gagra | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-29 | Boca Juniors vs CD Universidad Catolica | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-28 | Ireland vs Qatar | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-29 | Edgewater Castle vs Sueno FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.274 | EV=1.055 | match=1.0
- 2026-05-28 | Cerro Porteno vs Sporting Cristal | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 132
Pre-dedupe proxy candidate observation rows: 42
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 6
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-28 | CA Piauiense PI vs Santos FC SP | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-28 | FC Tallinn vs Maardu Linnameeskond | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-28 | FK Decic Tuzi vs FK Mornar Bar | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-28 | Al-Fahaheel vs Al-Salmiya SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-29 | Houston FC vs Laredo Heat SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145
- 2026-05-28 | Kolding IF vs Dbk Fortuna Hjoerring | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3772 | EV=0.47108 | edge=0.12079 | penalty=0.4710814710814708 | tier=proxy_watchlist | score=0.212
- 2026-05-29 | Shaanxi Union FC vs Nanjing City | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244
- 2026-05-28 | CR Vasco da Gama RJ vs America FC MG | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-05-29 | CA Tigre vs Alianza Atletico | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.083524 | penalty=0.4385014385014385 | tier=suppressed_proxy_watchlist | score=0.1196
- 2026-05-29 | Cruzeiro EC MG vs Barcelona SC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.083524 | penalty=0.4385014385014385 | tier=suppressed_proxy_watchlist | score=0.1196
- 2026-05-29 | Utah United vs Real Colorado | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.083524 | penalty=0.4385014385014385 | tier=suppressed_proxy_watchlist | score=0.1196
- 2026-05-29 | Western Springs AFC vs Bay Olympic | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 5
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 11
- ev_above_real_candidate_cap_possible_overconfidence: 10
- probability_or_league_rule_suppressed: 6
- low_probability_band_under_0_35: 6
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-28 | CA Piauiense PI vs Santos FC SP | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | FC Tallinn vs Maardu Linnameeskond | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | FK Decic Tuzi vs FK Mornar Bar | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-28 | Al-Fahaheel vs Al-Salmiya SC | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | Houston FC vs Laredo Heat SC | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | Kolding IF vs Dbk Fortuna Hjoerring | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Shaanxi Union FC vs Nanjing City | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | CR Vasco da Gama RJ vs America FC MG | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | CA Tigre vs Alianza Atletico | sel=DRAW | score=0.1196 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Cruzeiro EC MG vs Barcelona SC | sel=DRAW | score=0.1196 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Utah United vs Real Colorado | sel=DRAW | score=0.1196 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Western Springs AFC vs Bay Olympic | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 132
Paper proxy observation rows: 25
Positive EV value rows: 64
Suppressed-band observation rows: 0
Distinct matches: 22
Distinct sources: 0
Max EV: 0.781
Average EV: 0.414284
Max probability edge: 0.138274
Average match confidence: None
## By selection
- away: rows=6, avg_ev=0.4039, max_ev=0.6568
- draw: rows=14, avg_ev=0.4483, max_ev=0.781
- home: rows=5, avg_ev=0.3315, max_ev=0.5088

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 474
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-28 15:45 | Mikkelin Pallo-Kissat vs HaPK Edustus | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 16:00 | Deportivo Maldonado Reserve vs Liverpool Montevideo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 16:00 | Puskas Akademia Felcsut vs Ferencvarosi Budapest | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 16:00 | FC Tallinn vs Maardu Linnameeskond | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 16:00 | FC Torpedo Kutaisi vs FC Gagra | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 16:00 | FC Ylivieska vs Lapuan Virkia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 17:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 17:00 | Kolding IF vs Dbk Fortuna Hjoerring | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 17:00 | FCM Traiskirchen vs SC Neusiedl am See 1919 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 17:00 | PPJ/Ruoholahti vs Mps | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 17:20 | Ylojarvi United FC vs FC Haka J | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 17:30 | Hedensted IF vs Fuglebakken KFUM | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 17:30 | Zakho FC vs Erbil SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 18:00 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 18:00 | CA Lanus vs CA Platense | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 18:00 | CA Sarmiento de Junin vs Rosario Central Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 18:00 | CA Union Santa Fe Reserve vs Gimnasia de Mendoza Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 18:00 | Gimnasia de la Plata Reserve vs CA Barracas Central Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 18:00 | Nacional de Montevideo vs La Luz FC Reserves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 4293
Log type: probability_only_no_market_prices
- 2026-05-30 2026-05-28 05:00:00 | Inglewood United Reserves vs Cockburn City SC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 05:00:00 | Mandurah City FC Reserves vs Floreat Athena FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 05:00:00 | Olympic Kingsway SC vs Dianella White Eagles SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 05:00:00 | Sorrento FC vs Bayswater City SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 05:00:00 | Stirling Macedonia FC vs Balcatta Etna FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 05:00:00 | Subiaco AFC Reserve vs Uwa Nedlands FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 05:00:00 | Western Knights SC vs Perth SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 06:00:00 | Caboolture Sports FC vs Capalaba FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 06:00:00 | Rochedale Rovers vs Moreton City Excelsior U23 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 06:00:00 | South Coast Flame FC vs Sydney University SFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 06:30:00 | Hakoah vs Bankstown City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 06:30:00 | Macarthur Rams vs Central Coast Mariners Academy | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 06:30:00 | St George FC vs St George City FA | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 07:00:00 | AC Carina vs Logan Roos FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 07:00:00 | Bankstown United FC vs Fraser Park FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 07:00:00 | Canterbury Bankstown FC vs Inter Lions FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 07:00:00 | Curtin University SC vs Joondalup City | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 07:00:00 | Dulwich Hill vs Hills United FC Brumbies | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 07:00:00 | Grange Thistle vs Souths United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 07:00:00 | Gwelup Croatia SC vs Quinns FC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 474
Manual template rows: 474
Rows with complete manual odds: 0
Rows missing manual odds: 474
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-28 17:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers
- 2026-05-28 18:30 | ACF Fiorentina vs Parma Calcio 1913 U20
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA
- 2026-05-28 18:00 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve
- 2026-05-28 18:00 | CA Lanus vs CA Platense
- 2026-05-28 19:00 | CA Piauiense PI vs Santos FC SP
- 2026-05-28 22:00 | CA River Plate (Arg) vs San Lorenzo de Almagro Res.
- 2026-05-28 18:00 | CA Sarmiento de Junin vs Rosario Central Reserve
- 2026-05-28 18:00 | CA Union Santa Fe Reserve vs Gimnasia de Mendoza Reserve
- 2026-05-28 19:00 | Casa Pia Lisbon vs SCU Torreense
- 2026-05-28 23:00 | CD El Nacional vs CD Universidad Catolica del Ecuador
- 2026-05-28 20:00 | CD Real Santander vs Once Caldas Sa
- 2026-05-28 22:00 | Cerro Porteno vs Sporting Cristal

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 474
Source counts: {'odds_api_io_events_bookmaker_filtered': 465, 'odds_api_io_events_search': 9}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-28 17:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | germany-amateur-regionalliga-playoffs | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:30 | ACF Fiorentina vs Parma Calcio 1913 U20 | italy-primavera-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF | sweden-svenska-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:00 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:00 | CA Lanus vs CA Platense | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-28 19:00 | CA Piauiense PI vs Santos FC SP | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-28 22:00 | CA River Plate (Arg) vs San Lorenzo de Almagro Res. | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:00 | CA Sarmiento de Junin vs Rosario Central Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:00 | CA Union Santa Fe Reserve vs Gimnasia de Mendoza Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-28 19:00 | Casa Pia Lisbon vs SCU Torreense | portugal-liga-portugal | odds_api_io_events_bookmaker_filtered
- 2026-05-28 23:00 | CD El Nacional vs CD Universidad Catolica del Ecuador | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-05-28 20:00 | CD Real Santander vs Once Caldas Sa | colombia-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-28 22:00 | Cerro Porteno vs Sporting Cristal | international-clubs-copa-libertadores | odds_api_io_events_bookmaker_filtered
- 2026-05-28 21:00 | CR Vasco da Gama RJ vs America FC MG | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-28 21:30 | Cruzeiro EC MG vs Doce Mel EC BA | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-28 16:00 | Deportivo Maldonado Reserve vs Liverpool Montevideo | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:30 | East Fife Lfc vs Falkirk FC | scotland-premier-league-2-women | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:30 | FK Decic Tuzi vs FK Mornar Bar | montenegro-cup-crne-gore | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:00 | Gimnasia de la Plata Reserve vs CA Barracas Central Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-28 17:30 | Hedensted IF vs Fuglebakken KFUM | denmark-amateur-danmarksserien | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:45 | Ireland vs Qatar | international-int-friendly-games | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 474
Rows with complete odds: 0
- 2026-05-28 17:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | bookmaker=bet365_manual
- 2026-05-28 18:30 | ACF Fiorentina vs Parma Calcio 1913 U20 | bookmaker=bet365_manual
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC | bookmaker=bet365_manual
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF | bookmaker=bet365_manual
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA | bookmaker=bet365_manual
- 2026-05-28 18:00 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve | bookmaker=bet365_manual
- 2026-05-28 18:00 | CA Lanus vs CA Platense | bookmaker=bet365_manual
- 2026-05-28 19:00 | CA Piauiense PI vs Santos FC SP | bookmaker=bet365_manual
- 2026-05-28 22:00 | CA River Plate (Arg) vs San Lorenzo de Almagro Res. | bookmaker=bet365_manual
- 2026-05-28 18:00 | CA Sarmiento de Junin vs Rosario Central Reserve | bookmaker=bet365_manual
- 2026-05-28 18:00 | CA Union Santa Fe Reserve vs Gimnasia de Mendoza Reserve | bookmaker=bet365_manual
- 2026-05-28 19:00 | Casa Pia Lisbon vs SCU Torreense | bookmaker=bet365_manual
- 2026-05-28 23:00 | CD El Nacional vs CD Universidad Catolica del Ecuador | bookmaker=bet365_manual
- 2026-05-28 20:00 | CD Real Santander vs Once Caldas Sa | bookmaker=bet365_manual
- 2026-05-28 22:00 | Cerro Porteno vs Sporting Cristal | bookmaker=bet365_manual
- 2026-05-28 21:00 | CR Vasco da Gama RJ vs America FC MG | bookmaker=bet365_manual
- 2026-05-28 21:30 | Cruzeiro EC MG vs Doce Mel EC BA | bookmaker=bet365_manual
- 2026-05-28 16:00 | Deportivo Maldonado Reserve vs Liverpool Montevideo | bookmaker=bet365_manual
- 2026-05-28 18:30 | East Fife Lfc vs Falkirk FC | bookmaker=bet365_manual
- 2026-05-28 18:30 | FK Decic Tuzi vs FK Mornar Bar | bookmaker=bet365_manual
- 2026-05-28 18:00 | Gimnasia de la Plata Reserve vs CA Barracas Central Reserve | bookmaker=bet365_manual
- 2026-05-28 17:30 | Hedensted IF vs Fuglebakken KFUM | bookmaker=bet365_manual
- 2026-05-28 18:45 | Ireland vs Qatar | bookmaker=bet365_manual
- 2026-05-28 17:00 | Kolding IF vs Dbk Fortuna Hjoerring | bookmaker=bet365_manual

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
- 2026-05-28 17:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers
- 2026-05-28 18:30 | ACF Fiorentina vs Parma Calcio 1913 U20
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA
- 2026-05-28 18:00 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve
- 2026-05-28 18:00 | CA Lanus vs CA Platense
- 2026-05-28 19:00 | CA Piauiense PI vs Santos FC SP
- 2026-05-28 22:00 | CA River Plate (Arg) vs San Lorenzo de Almagro Res.
- 2026-05-28 18:00 | CA Sarmiento de Junin vs Rosario Central Reserve
- 2026-05-28 18:00 | CA Union Santa Fe Reserve vs Gimnasia de Mendoza Reserve
- 2026-05-28 19:00 | Casa Pia Lisbon vs SCU Torreense
- 2026-05-28 23:00 | CD El Nacional vs CD Universidad Catolica del Ecuador
- 2026-05-28 20:00 | CD Real Santander vs Once Caldas Sa
- 2026-05-28 22:00 | Cerro Porteno vs Sporting Cristal
- 2026-05-28 21:00 | CR Vasco da Gama RJ vs America FC MG
- 2026-05-28 21:30 | Cruzeiro EC MG vs Doce Mel EC BA
- 2026-05-28 16:00 | Deportivo Maldonado Reserve vs Liverpool Montevideo
- 2026-05-28 18:30 | East Fife Lfc vs Falkirk FC

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 720
Valid forward/proxy log rows: 717
Deduped forward/proxy observation rows: 546
Duplicate forward/proxy log rows: 171
Valid automatic proxy observation rows: 717
Deduped automatic proxy observation rows: 546
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-27 | SJK Akatemia/2 vs JS Hercules | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0557
- 2026-05-19 | SV Ried vs Wolfsberger AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-21 | Kifisia vs Larisa | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-23 | Auckland United FC vs East Coast Bays | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-23 | Avondale FC vs Alamein FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-27 | VVSB Noordwijkerhout vs Excelsior Maassluis | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553
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
### Orsomarso SC vs CDP Junior FC
- Date/time: 2026-05-29 00:30
- League/phase: colombia-liga-femenina / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.75
- Fair odds: 2.87
- Model probability: 0.3488
- Probability band: 0.25-0.35
- EV: 0.6568
- Probability edge: 0.1383
- Alignment penalty: 0.6568
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0692
- Prediction ID: b9f4db1352a1ac69a21a
### Patuxent Football Athletics vs Annapolis Blues FC
- Date/time: 2026-05-28 23:30
- League/phase: usa-usl-league-two / automatic_forward_price_proxy
- Selection: DRAW
- Market odds: 6.5
- Fair odds: 3.65
- Model probability: 0.274
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
Newly logged paper-test picks: 22
Total logged paper-test rows: 720
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 132, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 52, 'current_paper_picks': 25, 'newly_logged_picks': 22, 'total_logged_paper_rows': 720, 'source_used': 'automatic_forward_value_snapshots'}
- Orsomarso SC vs CDP Junior FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Patuxent Football Athletics vs Annapolis Blues FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Utah United vs Real Colorado | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Manukau United FC vs Fencibles United FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Houston FC vs Laredo Heat SC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kolding IF vs Dbk Fortuna Hjoerring | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.9 | prob=0.3772 | EV=0.4711 | edge=0.1208 | penalty=0.4711 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SE Palmeiras SP vs CD Junior FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FCM Traiskirchen vs SC Neusiedl am See 1919 | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.75 | prob=0.274 | EV=0.5755 | edge=0.1001 | penalty=0.5755 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Shaanxi Union FC vs Nanjing City | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CR Vasco da Gama RJ vs America FC MG | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Ylivieska vs Lapuan Virkia | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Cruzeiro EC MG vs Barcelona SC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CA Tigre vs Alianza Atletico | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Utah United vs Real Colorado | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CA Piauiense PI vs Santos FC SP | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.4 | prob=0.3772 | EV=0.2825 | edge=0.0831 | penalty=0.2825 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Western Springs AFC vs Bay Olympic | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Tallinn vs Maardu Linnameeskond | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.0695 | penalty=0.2259 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mikkelin Pallo-Kissat vs HaPK Edustus | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.75 | prob=0.274 | EV=0.3015 | edge=0.0635 | penalty=0.3015 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
