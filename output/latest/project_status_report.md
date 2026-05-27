# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-27T02:42:29.656100+00:00`
GitHub run: `375` attempt `1`
GitHub SHA: `be8c6dca9aec50f4e798a3fe29ea026a5969f965`
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
| odds-api.io forward fixtures | True | 182 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 147 |  |  |
| Forward price coverage report | True | 187 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 187 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 169
- Automatic value snapshots: 90
- Positive EV proxy rows: 40
- Proxy observation rows: 25
- Valid forward/proxy log rows: 670
- Deduped forward/proxy log rows: 503
- Duplicate forward/proxy log rows identified: 167
- Fresh API match coverage rate: 0.1775
- Matches with fresh API price: 30
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
Current: 90 value snapshots; fresh API coverage rate 0.1775.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 503 deduped forward/proxy rows; 167 duplicate raw rows identified.
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
Upcoming fixture rows: 169
Fixture team rows unmatched: 336
Ready for model-fixture join: False
Automatic forward price rows: 30
odds-api.io price rows: 30
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 3B Sport AM | suggestion=nan | type=unmatched
- Acao Futebol MT | suggestion=nan | type=unmatched
- AC Connecticut | suggestion=nan | type=unmatched
- Albany Rush | suggestion=nan | type=unmatched
- AC Goianiense GO | suggestion=nan | type=unmatched
- Operario Ferroviario EC PR | suggestion=nan | type=unmatched
- ADO 20 Heemskerk | suggestion=nan | type=unmatched
- FC Lisse | suggestion=nan | type=unmatched
- AIK DFF | suggestion=nan | type=unmatched
- Hacken Gothenburg | suggestion=nan | type=unmatched
- Al Zawraa | suggestion=nan | type=unmatched
- AL Naft | suggestion=nan | type=unmatched
- Al-Merrikh SC (SDN) | suggestion=nan | type=unmatched
- Apr FC | suggestion=nan | type=unmatched
- America FC MG | suggestion=nan | type=unmatched
- CR Flamengo RJ | suggestion=nan | type=unmatched
- Argentino de Quilmes | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 169
Automatic price rows: 30
Value snapshot rows: 90
Matches with any automatic price: 30
Matches with fresh API price: 30
Matches with odds-api.io price: 30
Fresh API match coverage rate: 0.1775
odds-api.io match coverage rate: 0.1775
Real-money ready: False
## Match coverage
- 2026-05-27 | Coton Sport de Garoua vs Panthere Sportive | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-27 | Duhok FC vs Al Kahrabaa SC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-27 | FK Famos Vojkovici vs FK Zvijezda 09 | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-27 | FC KTP vs FC Honka | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-27 | Velez Nevesinje vs FK Sutjeska Foca | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-27 | ETO FC Gyor vs MTK Hungaria Budapest | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Jypk vs Ons Oulu | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | SJK Akatemia/2 vs JS Hercules | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Tampereen Ilves vs Turun Palloseura | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Al-Merrikh SC (SDN) vs Apr FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | HJK Klubi 04 vs PK-35 Helsinki | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | JJK Jyvaskyla/2 vs Komeetat | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | JK Tallinna Kalev vs Viimsi JK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Primorje Ajdovscina vs Nafta 1903 Lendava | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Deportivo Riestra Afbc Reserve vs Estudiantes de LP Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-27 | Sparta Prague B vs FC Hradec Kralove | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 169
Proxy price rows: 30
Matched prediction rows: 30
Value snapshot rows: 90
odds-api.io snapshot rows: 90
Baseline snapshot rows: 90
Full model snapshot rows: 0
Positive EV rows: 40
Source counts: {'odds_api_io_Bet365_ML': 90}
- 2026-05-27 | Sao Jose EC vs Red Bull Bragantino SP | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=1.0
- 2026-05-27 | Vitoria FC ES vs SC Brasil Capixaba ES | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3488 | EV=9.1152 | match=1.0
- 2026-05-27 | FC Barcelona vs Real Sociedad San Sebastian | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-05-27 | Sao Jose EC vs Red Bull Bragantino SP | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.274 | EV=4.206 | match=1.0
- 2026-05-27 | Heips RJ vs Coritiba FC PR | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3772 | EV=2.5834 | match=1.0
- 2026-05-27 | Vitoria FC ES vs SC Brasil Capixaba ES | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-05-27 | Eskilstuna United DFF vs Hammarby IF | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3772 | EV=1.829 | match=1.0
- 2026-05-27 | HK Kopavogur vs Volsungur | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-27 | FC Barcelona vs Real Sociedad San Sebastian | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.274 | EV=1.466 | match=1.0
- 2026-05-27 | JJK Jyvaskyla/2 vs Komeetat | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-27 | AIK DFF vs Hacken Gothenburg | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3772 | EV=0.9803 | match=1.0
- 2026-05-27 | VfB Hohenems vs FC Lauterach | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-27 | JJK Jyvaskyla/2 vs Komeetat | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.274 | EV=0.781 | match=1.0
- 2026-05-27 | Al Zawraa vs AL Naft | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0
- 2026-05-27 | Tampereen Ilves vs Turun Palloseura | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3488 | EV=0.6568 | match=1.0
- 2026-05-27 | Eskilstuna United DFF vs Hammarby IF | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.274 | EV=0.644 | match=1.0
- 2026-05-27 | HK Kopavogur vs Volsungur | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.274 | EV=0.507 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 90
Pre-dedupe proxy candidate observation rows: 25
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 4
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-27 | JK Tallinna Kalev vs Viimsi JK | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-27 | CA Defensores Unidos vs Villa Dalmine | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-27 | HJK Klubi 04 vs PK-35 Helsinki | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-27 | Al-Merrikh SC (SDN) vs Apr FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-27 | SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-27 | VVSB Noordwijkerhout vs Excelsior Maassluis | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-27 | IF Vestri vs UMF Njardvik | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-27 | ADO 20 Heemskerk vs FC Lisse | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-27 | VfB Hohenems vs FC Lauterach | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171
- 2026-05-27 | Heips RJ vs Coritiba FC PR | selection=DRAW | source=odds_api_io_Bet365_ML | odds=4.75 | prob=0.274 | EV=0.3015 | edge=0.063474 | penalty=0.30150195225292853 | tier=suppressed_proxy_watchlist | score=0.1145
- 2026-05-27 | Newroz SC vs AL Mosul SC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3488 | EV=0.18592 | edge=0.054682 | penalty=0.18591857689770785 | tier=suppressed_proxy_watchlist | score=0.1139
- 2026-05-27 | Tampereen Ilves vs Turun Palloseura | selection=DRAW | source=odds_api_io_Bet365_ML | odds=4.5 | prob=0.274 | EV=0.233 | edge=0.051778 | penalty=0.233001233001233 | tier=suppressed_proxy_watchlist | score=0.1118

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
- ev_above_real_candidate_cap_possible_overconfidence: 7
- market_alignment_penalty_too_high_for_real_candidate: 7
- watchlist_only_pending_forward_settlement: 4
- probability_or_league_rule_suppressed: 4
- low_probability_band_under_0_35: 4
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-27 | JK Tallinna Kalev vs Viimsi JK | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | CA Defensores Unidos vs Villa Dalmine | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | HJK Klubi 04 vs PK-35 Helsinki | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Al-Merrikh SC (SDN) vs Apr FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | VVSB Noordwijkerhout vs Excelsior Maassluis | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | IF Vestri vs UMF Njardvik | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | ADO 20 Heemskerk vs FC Lisse | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-27 | VfB Hohenems vs FC Lauterach | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Heips RJ vs Coritiba FC PR | sel=DRAW | score=0.1145 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Newroz SC vs AL Mosul SC | sel=AWAY | score=0.1139 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Tampereen Ilves vs Turun Palloseura | sel=DRAW | score=0.1118 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 90
Paper proxy observation rows: 25
Positive EV value rows: 40
Suppressed-band observation rows: 0
Distinct matches: 21
Distinct sources: 0
Max EV: 0.781
Average EV: 0.257927
Max probability edge: 0.1488
Average match confidence: None
## By selection
- away: rows=6, avg_ev=0.2804, max_ev=0.744
- draw: rows=11, avg_ev=0.2998, max_ev=0.781
- home: rows=8, avg_ev=0.1835, max_ev=0.4145

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 169
Forward fixture prediction rows: 169
Full model prediction rows: 0
Baseline prediction rows: 169
Max forward predictions: 300
Ready for price join: True
- 2026-05-27 15:00 | Coton Sport de Garoua vs Panthere Sportive | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 15:00 | Duhok FC vs Al Kahrabaa SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 15:00 | FK Famos Vojkovici vs FK Zvijezda 09 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 15:00 | FC KTP vs FC Honka | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 15:00 | Velez Nevesinje vs FK Sutjeska Foca | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 15:30 | ETO FC Gyor vs MTK Hungaria Budapest | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 15:30 | Jypk vs Ons Oulu | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 15:30 | SJK Akatemia/2 vs JS Hercules | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 15:30 | Tampereen Ilves vs Turun Palloseura | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:00 | HJK Klubi 04 vs PK-35 Helsinki | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:00 | JJK Jyvaskyla/2 vs Komeetat | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:00 | JK Tallinna Kalev vs Viimsi JK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:00 | Primorje Ajdovscina vs Nafta 1903 Lendava | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:00 | SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:30 | Deportivo Riestra Afbc Reserve vs Estudiantes de LP Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:30 | Sparta Prague B vs FC Hradec Kralove | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 16:45 | Kings SC Kuopio vs KuPS Akatemia II | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 17:00 | AIK DFF vs Hacken Gothenburg | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 17:00 | Eskilstuna United DFF vs Hammarby IF | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 169
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 3983
Log type: probability_only_no_market_prices
- 2026-05-30 2026-05-27 18:00:00 | Sertaozinho FC SP vs Santos FC SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-27 18:15:00 | FC Killas vs Universitario de Deportes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-27 21:30:00 | Rochester FC vs Edgewater Castle | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-27 2026-05-27 18:30:00 | CF Esperanca D Andorra vs Sporting Club DE Escaldes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 00:30:00 | Atlantico Deportivo vs SV Deportivo Nacional | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 00:30:00 | Ds Edusoccer vs Academia Quintana | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 01:00:00 | Brittons Hill United vs Ellerton FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 16:00:00 | Deportivo Maldonado Reserve vs Liverpool Montevideo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 16:00:00 | Puskas Akademia Felcsut vs Ferencvarosi Budapest | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 16:00:00 | FC Torpedo Kutaisi vs FC Gagra | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 17:00:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 17:30:00 | Assyriska FF vs Vasalunds IF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 18:00:00 | Nacional de Montevideo vs La Luz FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 19:00:00 | Atletico Mineiro MG vs EC Vitoria BA | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 20:00:00 | CD Real Santander vs Once Caldas Sa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 20:30:00 | Llaneros FC vs Independiente Santa Fe | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 21:00:00 | CR Vasco da Gama RJ vs America FC MG | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 21:30:00 | Cruzeiro EC MG vs Doce Mel EC BA | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 23:30:00 | Patuxent Football Athletics vs Annapolis Blues FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-27 07:30:00 | Stallion Laguna FC vs Davao Aguilas | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 169
Manual template rows: 169
Rows with complete manual odds: 0
Rows missing manual odds: 169
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-27 19:30 | 3B Sport AM vs Acao Futebol MT
- 2026-05-27 23:00 | AC Connecticut vs Albany Rush
- 2026-05-27 18:00 | AC Goianiense GO vs Operario Ferroviario EC PR
- 2026-05-27 18:00 | ADO 20 Heemskerk vs FC Lisse
- 2026-05-27 17:00 | AIK DFF vs Hacken Gothenburg
- 2026-05-27 17:30 | Al Zawraa vs AL Naft
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ
- 2026-05-27 18:30 | Argentino de Quilmes vs CA Excursionistas
- 2026-05-27 22:00 | Atletico Mineiro MG vs Academia Puerto Cabello
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC
- 2026-05-27 18:00 | Atletico Tucuman Reserve vs CD Godoy Cruz
- 2026-05-27 22:00 | Avai FC SC vs Volta Redonda FC RJ
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian
- 2026-05-27 22:00 | Black Rock FC vs Vermont Green FC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 169
Source counts: {'odds_api_io_events_bookmaker_filtered': 168, 'odds_api_io_events_search': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-27 19:30 | 3B Sport AM vs Acao Futebol MT | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-27 23:00 | AC Connecticut vs Albany Rush | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | AC Goianiense GO vs Operario Ferroviario EC PR | brazil-u20-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | ADO 20 Heemskerk vs FC Lisse | netherlands-tweede-divisie | odds_api_io_events_bookmaker_filtered
- 2026-05-27 17:00 | AIK DFF vs Hacken Gothenburg | sweden-damallsvenskan | odds_api_io_events_bookmaker_filtered
- 2026-05-27 17:30 | Al Zawraa vs AL Naft | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC | rwanda-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ | brazil-u20-campeonato-brasileiro | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:30 | Argentino de Quilmes vs CA Excursionistas | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-27 22:00 | Atletico Mineiro MG vs Academia Puerto Cabello | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC | brazil-u20-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | Atletico Tucuman Reserve vs CD Godoy Cruz | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-27 22:00 | Avai FC SC vs Volta Redonda FC RJ | brazil-copa-sul-sudeste | odds_api_io_events_bookmaker_filtered
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian | spain-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-27 22:00 | Black Rock FC vs Vermont Green FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-27 23:00 | Boston Bolts vs New England FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:30 | Botafogo Fr RJ vs EC Juventude RS | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-27 21:00 | Boyaca Chico FC vs Llaneros FC | colombia-copa-colombia | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | CA Belgrano vs CA Quilmes Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:30 | CA Defensores Unidos vs Villa Dalmine | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | CA Paranaense PR vs EC Juventude RS | brazil-u20-campeonato-brasileiro | odds_api_io_events_bookmaker_filtered
- 2026-05-27 19:00 | Calcio Catania vs Ascoli Calcio 1898 | italy-serie-c-promotion-playoffs | odds_api_io_events_bookmaker_filtered
- 2026-05-27 22:00 | Caracas FC vs Botafogo FR RJ | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 169
Rows with complete odds: 0
- 2026-05-27 19:30 | 3B Sport AM vs Acao Futebol MT | bookmaker=bet365_manual
- 2026-05-27 23:00 | AC Connecticut vs Albany Rush | bookmaker=bet365_manual
- 2026-05-27 18:00 | AC Goianiense GO vs Operario Ferroviario EC PR | bookmaker=bet365_manual
- 2026-05-27 18:00 | ADO 20 Heemskerk vs FC Lisse | bookmaker=bet365_manual
- 2026-05-27 17:00 | AIK DFF vs Hacken Gothenburg | bookmaker=bet365_manual
- 2026-05-27 17:30 | Al Zawraa vs AL Naft | bookmaker=bet365_manual
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC | bookmaker=bet365_manual
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ | bookmaker=bet365_manual
- 2026-05-27 18:30 | Argentino de Quilmes vs CA Excursionistas | bookmaker=bet365_manual
- 2026-05-27 22:00 | Atletico Mineiro MG vs Academia Puerto Cabello | bookmaker=bet365_manual
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC | bookmaker=bet365_manual
- 2026-05-27 18:00 | Atletico Tucuman Reserve vs CD Godoy Cruz | bookmaker=bet365_manual
- 2026-05-27 22:00 | Avai FC SC vs Volta Redonda FC RJ | bookmaker=bet365_manual
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian | bookmaker=bet365_manual
- 2026-05-27 22:00 | Black Rock FC vs Vermont Green FC | bookmaker=bet365_manual
- 2026-05-27 23:00 | Boston Bolts vs New England FC | bookmaker=bet365_manual
- 2026-05-27 18:30 | Botafogo Fr RJ vs EC Juventude RS | bookmaker=bet365_manual
- 2026-05-27 21:00 | Boyaca Chico FC vs Llaneros FC | bookmaker=bet365_manual
- 2026-05-27 18:00 | CA Belgrano vs CA Quilmes Reserve | bookmaker=bet365_manual
- 2026-05-27 18:30 | CA Defensores Unidos vs Villa Dalmine | bookmaker=bet365_manual
- 2026-05-27 18:00 | CA Paranaense PR vs EC Juventude RS | bookmaker=bet365_manual
- 2026-05-27 19:00 | Calcio Catania vs Ascoli Calcio 1898 | bookmaker=bet365_manual
- 2026-05-27 22:00 | Caracas FC vs Botafogo FR RJ | bookmaker=bet365_manual
- 2026-05-27 18:00 | Ceara SC CE vs Brusque SC | bookmaker=bet365_manual

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
- 2026-05-27 19:30 | 3B Sport AM vs Acao Futebol MT
- 2026-05-27 23:00 | AC Connecticut vs Albany Rush
- 2026-05-27 18:00 | AC Goianiense GO vs Operario Ferroviario EC PR
- 2026-05-27 18:00 | ADO 20 Heemskerk vs FC Lisse
- 2026-05-27 17:00 | AIK DFF vs Hacken Gothenburg
- 2026-05-27 17:30 | Al Zawraa vs AL Naft
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ
- 2026-05-27 18:30 | Argentino de Quilmes vs CA Excursionistas
- 2026-05-27 22:00 | Atletico Mineiro MG vs Academia Puerto Cabello
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC
- 2026-05-27 18:00 | Atletico Tucuman Reserve vs CD Godoy Cruz
- 2026-05-27 22:00 | Avai FC SC vs Volta Redonda FC RJ
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian
- 2026-05-27 22:00 | Black Rock FC vs Vermont Green FC
- 2026-05-27 23:00 | Boston Bolts vs New England FC
- 2026-05-27 18:30 | Botafogo Fr RJ vs EC Juventude RS
- 2026-05-27 21:00 | Boyaca Chico FC vs Llaneros FC
- 2026-05-27 18:00 | CA Belgrano vs CA Quilmes Reserve

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 673
Valid forward/proxy log rows: 670
Deduped forward/proxy observation rows: 503
Duplicate forward/proxy log rows: 167
Valid automatic proxy observation rows: 670
Deduped automatic proxy observation rows: 503
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
### Al Zawraa vs AL Naft
- Date/time: 2026-05-27 17:30
- League/phase: iraq-iraqi-league / automatic_forward_price_proxy
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
- Prediction ID: ac34c178313a42e05fbe
### Tampereen Ilves vs Turun Palloseura
- Date/time: 2026-05-27 15:30
- League/phase: finland-suomen-cup / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.75
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
Newly logged paper-test picks: 24
Total logged paper-test rows: 673
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 90, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 35, 'current_paper_picks': 25, 'newly_logged_picks': 24, 'total_logged_paper_rows': 673, 'source_used': 'automatic_forward_value_snapshots'}
- Al Zawraa vs AL Naft | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Tampereen Ilves vs Turun Palloseura | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- JJK Jyvaskyla/2 vs Komeetat | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Eskilstuna United DFF vs Hammarby IF | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- JK Tallinna Kalev vs Viimsi JK | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.1105 | penalty=0.4145 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CA Defensores Unidos vs Villa Dalmine | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.7 | prob=0.3772 | EV=0.3956 | edge=0.1069 | penalty=0.3956 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- HK Kopavogur vs Volsungur | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- VfB Hohenems vs FC Lauterach | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- HJK Klubi 04 vs PK-35 Helsinki | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.0695 | penalty=0.2259 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Heips RJ vs Coritiba FC PR | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.75 | prob=0.274 | EV=0.3015 | edge=0.0635 | penalty=0.3015 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Newroz SC vs AL Mosul SC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.4 | prob=0.3488 | EV=0.1859 | edge=0.0547 | penalty=0.1859 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.0439 | penalty=0.1316 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al-Merrikh SC (SDN) vs Apr FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.0439 | penalty=0.1316 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Tampereen Ilves vs Turun Palloseura | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.5 | prob=0.274 | EV=0.233 | edge=0.0518 | penalty=0.233 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SJK Akatemia/2 vs JS Hercules | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.33 | prob=0.274 | EV=0.1872 | edge=0.0432 | penalty=0.1872 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- VVSB Noordwijkerhout vs Excelsior Maassluis | coverage=baseline_unmatched_fixture | selection=HOME | odds=2.9 | prob=0.3772 | EV=0.0939 | edge=0.0324 | penalty=0.0939 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- IF Vestri vs UMF Njardvik | coverage=baseline_unmatched_fixture | selection=HOME | odds=2.8 | prob=0.3772 | EV=0.0562 | edge=0.0201 | penalty=0.0562 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- JK Tallinna Kalev vs Viimsi JK | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.1 | prob=0.274 | EV=0.1234 | edge=0.0301 | penalty=0.1234 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
