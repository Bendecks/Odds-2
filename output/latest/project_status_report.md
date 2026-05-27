# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-26T14:51:42.111429+00:00`
GitHub run: `374` attempt `1`
GitHub SHA: `448dc5aac6670024184416a95aa1ba6a24228441`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 47 |  |  |
| odds-api.io forward fixtures | True | 193 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 144 |  |  |
| Forward price coverage report | True | 196 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 196 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 187
- Automatic value snapshots: 147
- Positive EV proxy rows: 56
- Proxy observation rows: 25
- Valid forward/proxy log rows: 646
- Deduped forward/proxy log rows: 486
- Duplicate forward/proxy log rows identified: 160
- Fresh API match coverage rate: 0.262
- Matches with fresh API price: 49
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
Current: 147 value snapshots; fresh API coverage rate 0.262.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 486 deduped forward/proxy rows; 160 duplicate raw rows identified.
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
Upcoming fixture rows: 187
Fixture team rows unmatched: 372
Ready for model-fixture join: False
Automatic forward price rows: 49
odds-api.io price rows: 49
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
- AL Karma | suggestion=nan | type=unmatched
- Diyala FC | suggestion=nan | type=unmatched
- Al Zawraa | suggestion=nan | type=unmatched
- AL Naft | suggestion=nan | type=unmatched
- Al-Merrikh SC (SDN) | suggestion=nan | type=unmatched
- Apr FC | suggestion=nan | type=unmatched
- FC Alga | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 187
Automatic price rows: 49
Value snapshot rows: 147
Matches with any automatic price: 49
Matches with fresh API price: 49
Matches with odds-api.io price: 49
Fresh API match coverage rate: 0.262
odds-api.io match coverage rate: 0.262
Real-money ready: False
## Match coverage
- 2026-05-27 | Dalian Yingbo B vs Shandong Taishan B | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Shanxi Chongde Ronghai vs Qingdao Red Lions | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Stallion Laguna FC vs Dynamic Herb Cebu FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Changchun Xidu vs Beijing Institute of Technology | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Mombasa United FC vs 3K FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Xiamen Feilu vs Jiangxi Lushan | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Sejong Sportstoto WFC vs Gyeongju FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Davao Aguilas vs Taguig FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | The Gap FC vs Virginia United | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | FC Altai Oskemen vs FC Astana | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Guangzhou Dandelion Alpha FC vs Ganzhou Ruishi FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Nantong Haimen Codion vs Shanghai Second | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Wuhan Three Towns B vs Guangdong Mingtu | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Buriram United vs Selangor FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Mighty Wanderers FC vs Karonga United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | Gazelle FA de Garoua vs Stade Renard | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-27 | FC Irtysh Pavlodar vs Ulytau FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 187
Proxy price rows: 49
Matched prediction rows: 49
Value snapshot rows: 147
odds-api.io snapshot rows: 147
Baseline snapshot rows: 147
Full model snapshot rows: 0
Positive EV rows: 56
Source counts: {'odds_api_io_Bet365_ML': 147}
- 2026-05-27 | Pakhtakor vs FC Kattaqorgon | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-27 | JJK Jyvaskyla/2 vs Komeetat | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-27 | FC Barcelona vs Real Sociedad San Sebastian | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-27 | Eskilstuna United DFF vs Hammarby IF | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-27 | Gazelle FA de Garoua vs Stade Renard | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-27 | Davao Aguilas vs Taguig FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3772 | EV=1.829 | match=1.0
- 2026-05-27 | FC KTP vs FC Honka | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-27 | JJK Jyvaskyla/2 vs Komeetat | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.274 | EV=1.603 | match=1.0
- 2026-05-27 | AIK DFF vs Hacken Gothenburg | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-27 | Pakhtakor vs FC Kattaqorgon | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.274 | EV=1.192 | match=1.0
- 2026-05-27 | Mighty Wanderers FC vs Karonga United FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-27 | Coton Sport de Garoua vs Panthere Sportive | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-27 | Sejong Sportstoto WFC vs Gyeongju FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-27 | VfB Hohenems vs FC Lauterach | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-27 | FC Barcelona vs Real Sociedad San Sebastian | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-27 | Manila Digger FC vs Kaya FC–Iloilo | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3772 | EV=0.886 | match=1.0
- 2026-05-27 | Buriram United vs Selangor FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 147
Pre-dedupe proxy candidate observation rows: 35
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 3
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-27 | Sanat Mes Kerman FC vs Nassaji Mazandaran FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-27 | JK Tallinna Kalev vs Viimsi JK | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-27 | HJK Klubi 04 vs PK-35 Helsinki | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-27 | SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-27 | FC Altai Oskemen vs FC Astana | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-27 | FC Yaypan Fergana vs FK Termez Surkhon | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-27 | Sparta Prague B vs FC Hradec Kralove | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-27 | Primorje Ajdovscina vs Nafta 1903 Lendava | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-27 | Dalian Yingbo B vs Shandong Taishan B | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.9 | prob=0.3772 | EV=0.47108 | edge=0.12079 | penalty=0.4710814710814708 | tier=proxy_watchlist | score=0.212
- 2026-05-27 | FC Alga vs FC Bishkek City | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244
- 2026-05-27 | Changchun Xidu vs Beijing Institute of Technology | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-05-27 | The Gap FC vs Virginia United | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 8
- ev_above_real_candidate_cap_possible_overconfidence: 6
- watchlist_only_pending_forward_settlement: 3
- probability_or_league_rule_suppressed: 3
- low_probability_band_under_0_35: 3
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-27 | Sanat Mes Kerman FC vs Nassaji Mazandaran FC | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | JK Tallinna Kalev vs Viimsi JK | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | HJK Klubi 04 vs PK-35 Helsinki | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-27 | SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-27 | FC Altai Oskemen vs FC Astana | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | FC Yaypan Fergana vs FK Termez Surkhon | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | Sparta Prague B vs FC Hradec Kralove | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | Primorje Ajdovscina vs Nafta 1903 Lendava | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-27 | Dalian Yingbo B vs Shandong Taishan B | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | FC Alga vs FC Bishkek City | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Changchun Xidu vs Beijing Institute of Technology | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | The Gap FC vs Virginia United | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 147
Paper proxy observation rows: 25
Positive EV value rows: 56
Suppressed-band observation rows: 0
Distinct matches: 25
Distinct sources: 0
Max EV: 0.781
Average EV: 0.403255
Max probability edge: 0.1488
Average match confidence: None
## By selection
- away: rows=12, avg_ev=0.4388, max_ev=0.744
- draw: rows=6, avg_ev=0.5108, max_ev=0.781
- home: rows=7, avg_ev=0.2501, max_ev=0.4711

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 187
Forward fixture prediction rows: 187
Full model prediction rows: 0
Baseline prediction rows: 187
Max forward predictions: 300
Ready for price join: True
- 2026-05-27 07:00 | Dalian Yingbo B vs Shandong Taishan B | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 07:00 | Shanxi Chongde Ronghai vs Qingdao Red Lions | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 07:30 | Stallion Laguna FC vs Dynamic Herb Cebu FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 08:00 | Changchun Xidu vs Beijing Institute of Technology | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 08:00 | Mombasa United FC vs 3K FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 08:00 | Xiamen Feilu vs Jiangxi Lushan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 10:00 | Sejong Sportstoto WFC vs Gyeongju FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 10:15 | Davao Aguilas vs Taguig FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 10:30 | The Gap FC vs Virginia United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 11:00 | FC Altai Oskemen vs FC Astana | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 11:00 | Guangzhou Dandelion Alpha FC vs Ganzhou Ruishi FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 11:30 | Nantong Haimen Codion vs Shanghai Second | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 11:30 | Wuhan Three Towns B vs Guangdong Mingtu | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 12:00 | Buriram United vs Selangor FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 12:30 | Mighty Wanderers FC vs Karonga United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 13:00 | Gazelle FA de Garoua vs Stade Renard | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 13:00 | FC Irtysh Pavlodar vs Ulytau FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 13:00 | Manila Digger FC vs Kaya FC–Iloilo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 13:00 | Shahrdari Nowshahr vs FC Pars Jonoubi Jam | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 13:15 | Niroye Zamini Tehran vs Havadar SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-27 13:30 | Sanat Mes Kerman FC vs Nassaji Mazandaran FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 187
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 3966
Log type: probability_only_no_market_prices
- 2026-05-28 2026-05-27 15:00:00 | AL Karkh vs Al Shorta SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 15:00:00 | AL Minaa vs AL Talaba | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 15:00:00 | AL Naft Maysan vs Al Quwa Al Jawiya | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 15:00:00 | Toolon Taisto vs FC Kontu | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 15:30:00 | Kultsu FC vs Kjp Kouvola | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 15:45:00 | Mikkelin Pallo-Kissat vs HaPK Edustus | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 16:00:00 | FC Ylivieska vs Lapuan Virkia | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 16:20:00 | Al-Fahaheel vs Al-Salmiya SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 17:00:00 | PPJ/Ruoholahti vs Mps | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 17:20:00 | Ylojarvi United FC vs FC Haka J | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 17:30:00 | Zakho FC vs Erbil SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 18:30:00 | East Fife Lfc vs Falkirk FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 18:30:00 | FK Decic Tuzi vs FK Mornar Bar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 18:45:00 | Ireland vs Qatar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 19:00:00 | CA Piauiense PI vs Santos FC SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-28 2026-05-27 22:00:00 | CA River Plate (Arg) vs San Lorenzo de Almagro Res. | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-29 2026-05-27 00:00:00 | Edgewater Castle vs Sueno FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-27 18:00:00 | Sertaozinho FC SP vs Santos FC SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-27 18:15:00 | FC Killas vs Universitario de Deportes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-27 21:30:00 | Rochester FC vs Edgewater Castle | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 187
Manual template rows: 187
Rows with complete manual odds: 0
Rows missing manual odds: 187
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
- 2026-05-27 15:00 | AL Karma vs Diyala FC
- 2026-05-27 17:30 | Al Zawraa vs AL Naft
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC
- 2026-05-27 14:30 | FC Alga vs FC Bishkek City
- 2026-05-27 11:00 | FC Altai Oskemen vs FC Astana
- 2026-05-27 15:00 | Amanat Baghdad SC vs Al-Gharraf SC
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ
- 2026-05-27 18:30 | Argentino de Quilmes vs CA Excursionistas
- 2026-05-27 22:00 | Atletico Mineiro MG vs Academia Puerto Cabello
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 187
Source counts: {'odds_api_io_events_bookmaker_filtered': 178, 'odds_api_io_events_search': 9}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-27 19:30 | 3B Sport AM vs Acao Futebol MT | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-27 23:00 | AC Connecticut vs Albany Rush | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | AC Goianiense GO vs Operario Ferroviario EC PR | brazil-u20-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | ADO 20 Heemskerk vs FC Lisse | netherlands-tweede-divisie | odds_api_io_events_bookmaker_filtered
- 2026-05-27 17:00 | AIK DFF vs Hacken Gothenburg | sweden-damallsvenskan | odds_api_io_events_bookmaker_filtered
- 2026-05-27 15:00 | AL Karma vs Diyala FC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-27 17:30 | Al Zawraa vs AL Naft | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC | rwanda-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-27 14:30 | FC Alga vs FC Bishkek City | kyrgyzstan-top-league | odds_api_io_events_bookmaker_filtered
- 2026-05-27 11:00 | FC Altai Oskemen vs FC Astana | kazakhstan-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-27 15:00 | Amanat Baghdad SC vs Al-Gharraf SC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ | brazil-u20-campeonato-brasileiro | odds_api_io_events_search
- 2026-05-27 18:30 | Argentino de Quilmes vs CA Excursionistas | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-27 22:00 | Atletico Mineiro MG vs Academia Puerto Cabello | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC | brazil-u20-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:00 | Atletico Tucuman Reserve vs CD Godoy Cruz | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-27 14:00 | Avai FC SC vs CR Vasco da Gama RJ | brazil-u20-campeonato-brasileiro | odds_api_io_events_bookmaker_filtered
- 2026-05-27 22:00 | Avai FC SC vs Volta Redonda FC RJ | brazil-copa-sul-sudeste | odds_api_io_events_bookmaker_filtered
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian | spain-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-27 22:00 | Black Rock FC vs Vermont Green FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-27 23:00 | Boston Bolts vs New England FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-27 18:30 | Botafogo Fr RJ vs EC Juventude RS | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-27 21:00 | Boyaca Chico FC vs Llaneros FC | colombia-copa-colombia | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 187
Rows with complete odds: 0
- 2026-05-27 19:30 | 3B Sport AM vs Acao Futebol MT | bookmaker=bet365_manual
- 2026-05-27 23:00 | AC Connecticut vs Albany Rush | bookmaker=bet365_manual
- 2026-05-27 18:00 | AC Goianiense GO vs Operario Ferroviario EC PR | bookmaker=bet365_manual
- 2026-05-27 18:00 | ADO 20 Heemskerk vs FC Lisse | bookmaker=bet365_manual
- 2026-05-27 17:00 | AIK DFF vs Hacken Gothenburg | bookmaker=bet365_manual
- 2026-05-27 15:00 | AL Karma vs Diyala FC | bookmaker=bet365_manual
- 2026-05-27 17:30 | Al Zawraa vs AL Naft | bookmaker=bet365_manual
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC | bookmaker=bet365_manual
- 2026-05-27 14:30 | FC Alga vs FC Bishkek City | bookmaker=bet365_manual
- 2026-05-27 11:00 | FC Altai Oskemen vs FC Astana | bookmaker=bet365_manual
- 2026-05-27 15:00 | Amanat Baghdad SC vs Al-Gharraf SC | bookmaker=bet365_manual
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ | bookmaker=bet365_manual
- 2026-05-27 18:30 | Argentino de Quilmes vs CA Excursionistas | bookmaker=bet365_manual
- 2026-05-27 22:00 | Atletico Mineiro MG vs Academia Puerto Cabello | bookmaker=bet365_manual
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC | bookmaker=bet365_manual
- 2026-05-27 18:00 | Atletico Tucuman Reserve vs CD Godoy Cruz | bookmaker=bet365_manual
- 2026-05-27 14:00 | Avai FC SC vs CR Vasco da Gama RJ | bookmaker=bet365_manual
- 2026-05-27 22:00 | Avai FC SC vs Volta Redonda FC RJ | bookmaker=bet365_manual
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian | bookmaker=bet365_manual
- 2026-05-27 22:00 | Black Rock FC vs Vermont Green FC | bookmaker=bet365_manual
- 2026-05-27 23:00 | Boston Bolts vs New England FC | bookmaker=bet365_manual
- 2026-05-27 18:30 | Botafogo Fr RJ vs EC Juventude RS | bookmaker=bet365_manual
- 2026-05-27 21:00 | Boyaca Chico FC vs Llaneros FC | bookmaker=bet365_manual
- 2026-05-27 12:00 | Buriram United vs Selangor FC | bookmaker=bet365_manual

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
- 2026-05-27 15:00 | AL Karma vs Diyala FC
- 2026-05-27 17:30 | Al Zawraa vs AL Naft
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC
- 2026-05-27 14:30 | FC Alga vs FC Bishkek City
- 2026-05-27 11:00 | FC Altai Oskemen vs FC Astana
- 2026-05-27 15:00 | Amanat Baghdad SC vs Al-Gharraf SC
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ
- 2026-05-27 18:30 | Argentino de Quilmes vs CA Excursionistas
- 2026-05-27 22:00 | Atletico Mineiro MG vs Academia Puerto Cabello
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC
- 2026-05-27 18:00 | Atletico Tucuman Reserve vs CD Godoy Cruz
- 2026-05-27 14:00 | Avai FC SC vs CR Vasco da Gama RJ
- 2026-05-27 22:00 | Avai FC SC vs Volta Redonda FC RJ
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 649
Valid forward/proxy log rows: 646
Deduped forward/proxy observation rows: 486
Duplicate forward/proxy log rows: 160
Valid automatic proxy observation rows: 646
Deduped automatic proxy observation rows: 486
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-21 | BFC Daugavpils vs Ogre United | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-23 | Canberra Olympic vs Belconnen United | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-27 | FC Altai Oskemen vs FC Astana | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-27 | FC Yaypan Fergana vs FK Termez Surkhon | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-19 | Derby Academie vs Onze Createurs | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Al Kahrabaa SC vs Al-Gharraf SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Diyala FC vs Amanat Baghdad SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Deportivo Capiata vs Club Fernando de La Mora | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.056100000000000004
- 2026-05-23 | Clarence Zebras FC vs Kingborough Lions United FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0557
- 2026-05-27 | Buriram United vs Selangor FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0557
- 2026-05-19 | SV Ried vs Wolfsberger AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-21 | Kifisia vs Larisa | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-23 | Auckland United FC vs East Coast Bays | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-23 | Avondale FC vs Alamein FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553
- 2026-05-21 | Anderlecht vs St Truiden | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0546
- 2026-05-21 | Panetolikos vs Asteras Tripolis | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.054

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
### Nantong Haimen Codion vs Shanghai Second
- Date/time: 2026-05-27 11:30
- League/phase: china-china-league-2 / automatic_forward_price_proxy
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
- Prediction ID: a5cd313593f0bdecf321
### Guangzhou Dandelion Alpha FC vs Ganzhou Ruishi FC
- Date/time: 2026-05-27 11:00
- League/phase: china-china-league-2 / automatic_forward_price_proxy
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
Newly logged paper-test picks: 25
Total logged paper-test rows: 649
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 147, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 51, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 649, 'source_used': 'automatic_forward_value_snapshots'}
- Nantong Haimen Codion vs Shanghai Second | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Guangzhou Dandelion Alpha FC vs Ganzhou Ruishi FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC KTP vs FC Honka | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Eskilstuna United DFF vs Hammarby IF | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Velez Nevesinje vs FK Sutjeska Foca | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Davao Aguilas vs Taguig FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.0 | prob=0.274 | EV=0.644 | edge=0.1073 | penalty=0.644 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Dalian Yingbo B vs Shandong Taishan B | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.9 | prob=0.3772 | EV=0.4711 | edge=0.1208 | penalty=0.4711 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AL Karma vs Diyala FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Alga vs FC Bishkek City | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Changchun Xidu vs Beijing Institute of Technology | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- The Gap FC vs Virginia United | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Sanat Mes Kerman FC vs Nassaji Mazandaran FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al Zawraa vs AL Naft | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Tampereen Ilves vs Turun Palloseura | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- JK Tallinna Kalev vs Viimsi JK | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Famos Vojkovici vs FK Zvijezda 09 | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Newroz SC vs AL Mosul SC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.0821 | penalty=0.308 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- VfB Hohenems vs FC Lauterach | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
