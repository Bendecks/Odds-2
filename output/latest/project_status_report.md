# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-18T14:58:54.096168+00:00`
GitHub run: `358` attempt `1`
GitHub SHA: `2fdaca15fb28097f2a1d728cd5cdd48f28c71512`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 2 |  |  |
| Football-Data upcoming odds proxy | True | 6 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 51 |  |  |
| odds-api.io forward fixtures | True | 187 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 189 |  |  |
| Forward price coverage report | True | 198 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 198 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 176
- Automatic value snapshots: 129
- Positive EV proxy rows: 54
- Proxy observation rows: 25
- Valid forward/proxy log rows: 361
- Deduped forward/proxy log rows: 250
- Duplicate forward/proxy log rows identified: 111
- Fresh API match coverage rate: 0.2386
- Matches with fresh API price: 42
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
Current: 129 value snapshots; fresh API coverage rate 0.2386.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 250 deduped forward/proxy rows; 111 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 112
Upcoming fixture rows: 0
Proxy price rows: 0
Sources attempted: 1
Errors: 0
No usable proxy odds rows were available from Football-Data fixtures source.

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 176
Fixture team rows unmatched: 348
Ready for model-fixture join: False
Automatic forward price rows: 42
odds-api.io price rows: 42
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AFC Bournemouth | suggestion=Bournemouth | type=suggested_alias_needed
- Manchester City | suggestion=nan | type=unmatched
- AC Monza | suggestion=nan | type=unmatched
- Juve Stabia | suggestion=nan | type=unmatched
- Afrique Football Elite | suggestion=nan | type=unmatched
- AS Bakaridjan | suggestion=nan | type=unmatched
- Al Kahrabaa SC | suggestion=nan | type=unmatched
- Al-Gharraf SC | suggestion=nan | type=unmatched
- AL Naft | suggestion=nan | type=unmatched
- Duhok FC | suggestion=nan | type=unmatched
- AL Talaba | suggestion=nan | type=unmatched
- AL Karma | suggestion=nan | type=unmatched
- Al-Horiyah | suggestion=nan | type=unmatched
- Al-Jaish SC (Syr) | suggestion=nan | type=unmatched
- AS Korofina | suggestion=nan | type=unmatched
- Binga FC | suggestion=nan | type=unmatched
- Audax Italiano | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 176
Automatic price rows: 42
Value snapshot rows: 129
Matches with any automatic price: 42
Matches with fresh API price: 42
Matches with odds-api.io price: 42
Fresh API match coverage rate: 0.2386
odds-api.io match coverage rate: 0.2386
Real-money ready: False
## Match coverage
- 2026-05-19 | Turkmenistan vs Uzbekistan | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-19 | Ethiopian Medhin vs Wolaita Dicha SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Rtc FC vs Paro FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | HNK Hajduk Split vs NK Mladost Zdralovi | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-19 | Murdoch University Melville FC vs Joondalup City | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Bashundhara Kings vs Mohammedan SC Dhaka | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Northeast United FC vs Mohammedan SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Tianjin Jinmen Tiger vs Henan | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Hapoel Ironi Kiryat Shmona vs Maccabi Herzliya | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-19 | Juventud de Las Piedras vs Colon FC Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-19 | Qingdao West Coast FC vs Beijing Guoan | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Quinns FC Reserve vs Floreat Athena FC Reserves | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-19 | Tajikistan vs Kyrgyzstan | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-19 | Uwa Nedlands FC Reserves vs Inglewood United Reserves | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-19 | Al-Horiyah vs Al-Jaish SC (Syr) | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Deportivo Capiata vs Club Fernando de La Mora | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 176
Proxy price rows: 42
Matched prediction rows: 42
Value snapshot rows: 129
odds-api.io snapshot rows: 129
Baseline snapshot rows: 129
Full model snapshot rows: 0
Positive EV rows: 54
Source counts: {'odds_api_io_Bet365_ML': 129}
- 2026-05-19 | FK Pempininkai vs FK Minija 2017 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3772 | EV=9.9388 | match=1.0
- 2026-05-19 | FC Noah Yerevan vs Ararat Yerevan FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-19 | FK Riteriai vs FK Kauno Zalgiris | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-19 | FK Pempininkai vs FK Minija 2017 | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.274 | EV=2.014 | match=1.0
- 2026-05-19 | Northeast United FC vs Mohammedan SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-19 | Ben Aknoun vs ES Mostaganem | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-19 | FC Noah Yerevan vs Ararat Yerevan FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.274 | EV=1.603 | match=1.0
- 2026-05-19 | Hapoel Petah Tikva FC vs Beitar Jerusalem FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-19 | FC Kiisto vs Vpv | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-19 | Velez Nevesinje vs FK Vlasenica | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-19 | FC Haka J vs Saaksjaerven Loiske | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-19 | LSK Kvinner FK vs Hoenefoss BK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-19 | CS Constantine vs USM Khenchela | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-19 | FK Riteriai vs FK Kauno Zalgiris | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-19 | Hapoel Acre FC vs Hapoel Hadera FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0
- 2026-05-19 | Klaipedos Fsm vs Dfk Dainava Alytus | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.5 | prob=0.3772 | EV=0.6974 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 129
Pre-dedupe proxy candidate observation rows: 36
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 3
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-19 | Qingdao West Coast FC vs Beijing Guoan | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-19 | Hapoel Ra`anana FC vs FC Kafr Qasim | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-19 | AS Korofina vs Binga FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-19 | Rtc FC vs Paro FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-19 | Tianjin Jinmen Tiger vs Henan | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-19 | Helsingborgs IF vs Varbergs BoIS | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-19 | Murdoch University Melville FC vs Joondalup City | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-19 | Boston Bolts vs Vermont Green FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | edge=0.146413 | penalty=0.6344074839570686 | tier=proxy_watchlist | score=0.2223
- 2026-05-19 | Rajasthan United vs Chanmari FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3488 | EV=0.32544 | edge=0.085642 | penalty=0.325439469824212 | tier=suppressed_proxy_watchlist | score=0.1201
- 2026-05-19 | Hapoel Petah Tikva FC vs Beitar Jerusalem FC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171
- 2026-05-19 | Boston Bolts vs Vermont Green FC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171

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
- ev_above_real_candidate_cap_possible_overconfidence: 6
- market_alignment_penalty_too_high_for_real_candidate: 6
- watchlist_only_pending_forward_settlement: 5
- probability_or_league_rule_suppressed: 3
- low_probability_band_under_0_35: 3
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-19 | Qingdao West Coast FC vs Beijing Guoan | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Hapoel Ra`anana FC vs FC Kafr Qasim | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | AS Korofina vs Binga FC | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | Rtc FC vs Paro FC | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | Tianjin Jinmen Tiger vs Henan | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | Helsingborgs IF vs Varbergs BoIS | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | Murdoch University Melville FC vs Joondalup City | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-19 | Boston Bolts vs Vermont Green FC | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Rajasthan United vs Chanmari FC | sel=AWAY | score=0.1201 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Hapoel Petah Tikva FC vs Beitar Jerusalem FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Boston Bolts vs Vermont Green FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 129
Paper proxy observation rows: 25
Positive EV value rows: 54
Suppressed-band observation rows: 0
Distinct matches: 24
Distinct sources: 0
Max EV: 0.744
Average EV: 0.333118
Max probability edge: 0.154978
Average match confidence: None
## By selection
- away: rows=11, avg_ev=0.3286, max_ev=0.744
- draw: rows=7, avg_ev=0.3635, max_ev=0.5755
- home: rows=7, avg_ev=0.3099, max_ev=0.6974

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 176
Forward fixture prediction rows: 176
Full model prediction rows: 1
Baseline prediction rows: 175
Max forward predictions: 300
Ready for price join: True
- 2026-05-19 07:30 | Turkmenistan vs Uzbekistan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 10:00 | Ethiopian Medhin vs Wolaita Dicha SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 10:00 | Rtc FC vs Paro FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 11:00 | HNK Hajduk Split vs NK Mladost Zdralovi | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 11:15 | Murdoch University Melville FC vs Joondalup City | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 11:30 | Northeast United FC vs Mohammedan SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 11:35 | Tianjin Jinmen Tiger vs Henan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 12:00 | Chengdu Rongcheng vs Shanghai Port FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 12:00 | Hapoel Ironi Kiryat Shmona vs Maccabi Herzliya | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 12:00 | Juventud de Las Piedras vs Colon FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 12:00 | Qingdao West Coast FC vs Beijing Guoan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 12:00 | Quinns FC Reserve vs Floreat Athena FC Reserves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 12:00 | Tajikistan vs Kyrgyzstan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 12:00 | Uwa Nedlands FC Reserves vs Inglewood United Reserves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 13:00 | Al-Horiyah vs Al-Jaish SC (Syr) | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 13:00 | Deportivo Capiata vs Club Fernando de La Mora | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 13:00 | Rajasthan United vs Chanmari FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 13:00 | Tacuary Asuncion vs Encarnacion FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 14:30 | Al Kahrabaa SC vs Al-Gharraf SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 14:30 | Diyala FC vs Amanat Baghdad SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 176
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 2332
Log type: probability_only_no_market_prices
- 2026-05-21 2026-05-19 18:00:00 | Al-Fayha FC vs Al Hilal SFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:00:00 | Al-Hazm vs Al-Taawoun FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:00:00 | Al-Ittihad Club vs Al Qadsiah | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:00:00 | Al-Kholood vs Al-Fateh SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:00:00 | Al-Riyadh SC vs Al-Okhdood Club | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:00:00 | IA Akranes vs IBV Vestmannaeyjar | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:00:00 | Neom SC vs Al-Ittifaq FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:30:00 | KAA Gent vs Union Saint-Gilloise | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:30:00 | RSC Anderlecht vs St. Truidense VV | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:30:00 | VFL Wolfsburg vs SC Paderborn 07 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 18:30:00 | Yellow-Red KV Mechelen vs Club Brugge | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 19:00:00 | Partick Thistle FC vs St Mirren FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 19:00:00 | FC Utrecht vs SC Heerenveen | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 21:00:00 | Ferroviaria SP vs SE Palmeiras SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 22:00:00 | Academia Puerto Cabello vs CA Juventud de Las Piedras | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 22:00:00 | Atletico Mineiro MG vs CS Cienciano | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 22:00:00 | Deportivo La Guaira vs Independiente Rivadavia | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-22 2026-05-19 00:30:00 | CA Penarol Montevideo vs SC Corinthians SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-19 05:00:00 | Quinns FC Reserve vs Mandurah City FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-19 13:00:00 | Cruzeiro EC MG vs Boston City FC MG | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 176
Manual template rows: 176
Rows with complete manual odds: 0
Rows missing manual odds: 176
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-19 18:30 | AFC Bournemouth vs Manchester City
- 2026-05-19 18:00 | AC Monza vs Juve Stabia
- 2026-05-19 18:30 | Afrique Football Elite vs AS Bakaridjan
- 2026-05-19 14:30 | Al Kahrabaa SC vs Al-Gharraf SC
- 2026-05-19 17:00 | AL Naft vs Duhok FC
- 2026-05-19 17:00 | AL Talaba vs AL Karma
- 2026-05-19 13:00 | Al-Horiyah vs Al-Jaish SC (Syr)
- 2026-05-19 16:30 | AS Korofina vs Binga FC
- 2026-05-19 22:00 | Audax Italiano vs CA Barracas Central
- 2026-05-19 18:00 | Barra FC SC vs Concordia SC
- 2026-05-19 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem
- 2026-05-19 18:00 | Boston Bolts vs Vermont Green FC
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve
- 2026-05-19 18:30:00 | Bournemouth vs Manchester City

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 176
Source counts: {'odds_api_io_events_bookmaker_filtered': 167, 'odds_api_io_events_search': 8, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-19 18:30 | AFC Bournemouth vs Manchester City | england-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | AC Monza vs Juve Stabia | italy-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:30 | Afrique Football Elite vs AS Bakaridjan | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-19 14:30 | Al Kahrabaa SC vs Al-Gharraf SC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 17:00 | AL Naft vs Duhok FC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 17:00 | AL Talaba vs AL Karma | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 13:00 | Al-Horiyah vs Al-Jaish SC (Syr) | syria-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 16:30 | AS Korofina vs Binga FC | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-19 22:00 | Audax Italiano vs CA Barracas Central | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | Barra FC SC vs Concordia SC | brazil-u20-catarinense-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-05-19 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka | bangladesh-federation-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem | algeria-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | Boston Bolts vs Vermont Green FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:30:00 | Bournemouth vs Manchester City | premier_league | thesportsdb_eventsnextleague
- 2026-05-19 18:00 | CA Banfield vs CA Aldosivi Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | CA Quilmes Reserve vs CA Lanus | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 17:00 | CA River Plate (URU) vs Deportivo Maldonado Reserve | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 22:00 | CA Rosario Central vs UCV FC | international-clubs-copa-libertadores | odds_api_io_events_bookmaker_filtered
- 2026-05-19 19:15 | Chelsea FC vs Tottenham Hotspur | england-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 12:00 | Chengdu Rongcheng vs Shanghai Port FC | china-chinese-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | Colon de Santa Fe Reserve vs Ferro Carril Oeste | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 22:00 | Coquimbo Unido vs CD Tolima | international-clubs-copa-libertadores | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 176
Rows with complete odds: 0
- 2026-05-19 18:30 | AFC Bournemouth vs Manchester City | bookmaker=bet365_manual
- 2026-05-19 18:00 | AC Monza vs Juve Stabia | bookmaker=bet365_manual
- 2026-05-19 18:30 | Afrique Football Elite vs AS Bakaridjan | bookmaker=bet365_manual
- 2026-05-19 14:30 | Al Kahrabaa SC vs Al-Gharraf SC | bookmaker=bet365_manual
- 2026-05-19 17:00 | AL Naft vs Duhok FC | bookmaker=bet365_manual
- 2026-05-19 17:00 | AL Talaba vs AL Karma | bookmaker=bet365_manual
- 2026-05-19 13:00 | Al-Horiyah vs Al-Jaish SC (Syr) | bookmaker=bet365_manual
- 2026-05-19 16:30 | AS Korofina vs Binga FC | bookmaker=bet365_manual
- 2026-05-19 22:00 | Audax Italiano vs CA Barracas Central | bookmaker=bet365_manual
- 2026-05-19 18:00 | Barra FC SC vs Concordia SC | bookmaker=bet365_manual
- 2026-05-19 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka | bookmaker=bet365_manual
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem | bookmaker=bet365_manual
- 2026-05-19 18:00 | Boston Bolts vs Vermont Green FC | bookmaker=bet365_manual
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve | bookmaker=bet365_manual
- 2026-05-19 18:30:00 | Bournemouth vs Manchester City | bookmaker=bet365_manual
- 2026-05-19 18:00 | CA Banfield vs CA Aldosivi Reserve | bookmaker=bet365_manual
- 2026-05-19 18:00 | CA Quilmes Reserve vs CA Lanus | bookmaker=bet365_manual
- 2026-05-19 17:00 | CA River Plate (URU) vs Deportivo Maldonado Reserve | bookmaker=bet365_manual
- 2026-05-19 22:00 | CA Rosario Central vs UCV FC | bookmaker=bet365_manual
- 2026-05-19 19:15 | Chelsea FC vs Tottenham Hotspur | bookmaker=bet365_manual
- 2026-05-19 12:00 | Chengdu Rongcheng vs Shanghai Port FC | bookmaker=bet365_manual
- 2026-05-19 18:00 | Colon de Santa Fe Reserve vs Ferro Carril Oeste | bookmaker=bet365_manual
- 2026-05-19 22:00 | Coquimbo Unido vs CD Tolima | bookmaker=bet365_manual
- 2026-05-19 16:45 | CS Constantine vs USM Khenchela | bookmaker=bet365_manual

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
- 2026-05-19 18:30 | AFC Bournemouth vs Manchester City
- 2026-05-19 18:00 | AC Monza vs Juve Stabia
- 2026-05-19 18:30 | Afrique Football Elite vs AS Bakaridjan
- 2026-05-19 14:30 | Al Kahrabaa SC vs Al-Gharraf SC
- 2026-05-19 17:00 | AL Naft vs Duhok FC
- 2026-05-19 17:00 | AL Talaba vs AL Karma
- 2026-05-19 13:00 | Al-Horiyah vs Al-Jaish SC (Syr)
- 2026-05-19 16:30 | AS Korofina vs Binga FC
- 2026-05-19 22:00 | Audax Italiano vs CA Barracas Central
- 2026-05-19 18:00 | Barra FC SC vs Concordia SC
- 2026-05-19 11:30 | Bashundhara Kings vs Mohammedan SC Dhaka
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem
- 2026-05-19 18:00 | Boston Bolts vs Vermont Green FC
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve
- 2026-05-19 18:30:00 | Bournemouth vs Manchester City
- 2026-05-19 18:00 | CA Banfield vs CA Aldosivi Reserve
- 2026-05-19 18:00 | CA Quilmes Reserve vs CA Lanus
- 2026-05-19 17:00 | CA River Plate (URU) vs Deportivo Maldonado Reserve
- 2026-05-19 22:00 | CA Rosario Central vs UCV FC

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 364
Valid forward/proxy log rows: 361
Deduped forward/proxy observation rows: 250
Duplicate forward/proxy log rows: 111
Valid automatic proxy observation rows: 361
Deduped automatic proxy observation rows: 250
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-14 | Kjp Kouvola vs Lautp | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-19 | Hapoel Ra`anana FC vs FC Kafr Qasim | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.059000000000000004
- 2026-05-14 | Ntnui vs Orkla | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.058600000000000006
- 2026-05-15 | Melbourne Knights FC vs Eltham Redbacks FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.058600000000000006
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
- 2026-05-19 | Ben Aknoun vs ES Mostaganem | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0557
- 2026-05-19 | SV Ried vs Wolfsberger AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | AS Korofina vs Binga FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.055600000000000004
- 2026-05-19 | Rtc FC vs Paro FC | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0553

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
### Klaipedos Fsm vs Dfk Dainava Alytus
- Date/time: 2026-05-19 15:00
- League/phase: lithuania-lff-cup / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.5
- Fair odds: 2.65
- Model probability: 0.3772
- Probability band: 0.35-0.45
- EV: 0.6974
- Probability edge: 0.155
- Alignment penalty: 0.6974
- Suppression action: baseline_coverage_observe_only
- Paper tier: baseline_coverage_observation
- Paper score: 0.0712
- Prediction ID: a5be16867b84026f9f38
### Hapoel Acre FC vs Hapoel Hadera FC
- Date/time: 2026-05-19 16:00
- League/phase: israel-national-league / automatic_forward_price_proxy
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
Total logged paper-test rows: 364
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 129, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 50, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 364, 'source_used': 'automatic_forward_value_snapshots'}
- Klaipedos Fsm vs Dfk Dainava Alytus | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hapoel Acre FC vs Hapoel Hadera FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Boston Bolts vs Vermont Green FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6344 | edge=0.1464 | penalty=0.6344 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AC Monza vs Juve Stabia | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Bashundhara Kings vs Mohammedan SC Dhaka | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hapoel Be`er Sheva FC vs Maccabi Tel Aviv FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Kiisto vs Vpv | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.75 | prob=0.274 | EV=0.5755 | edge=0.1001 | penalty=0.5755 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Qingdao West Coast FC vs Beijing Guoan | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Haka J vs Saaksjaerven Loiske | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Rajasthan United vs Chanmari FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hapoel Petah Tikva FC vs Beitar Jerusalem FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Boston Bolts vs Vermont Green FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- MB Rouissat vs Paradou AC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.6 | prob=0.3488 | EV=0.2557 | edge=0.071 | penalty=0.2557 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hapoel Ra`anana FC vs FC Kafr Qasim | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.2 | prob=0.3772 | EV=0.207 | edge=0.0647 | penalty=0.207 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Northeast United FC vs Mohammedan SC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.75 | prob=0.274 | EV=0.3015 | edge=0.0635 | penalty=0.3015 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Chengdu Rongcheng vs Shanghai Port FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=4.5 | prob=0.274 | EV=0.233 | edge=0.0518 | penalty=0.233 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Derby Academie vs Onze Createurs | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.3 | prob=0.3488 | EV=0.151 | edge=0.0458 | penalty=0.151 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Al Kahrabaa SC vs Al-Gharraf SC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.3 | prob=0.3488 | EV=0.151 | edge=0.0458 | penalty=0.151 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
