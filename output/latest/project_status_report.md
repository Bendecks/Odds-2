# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-19T02:36:32.326078+00:00`
GitHub run: `359` attempt `1`
GitHub SHA: `a34812d0de3b051503c9dd7667336d6c232dd079`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 42 |  |  |
| odds-api.io forward fixtures | True | 137 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 129 |  |  |
| Forward price coverage report | True | 176 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 176 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 210
- Automatic value snapshots: 294
- Positive EV proxy rows: 145
- Proxy observation rows: 25
- Valid forward/proxy log rows: 385
- Deduped forward/proxy log rows: 262
- Duplicate forward/proxy log rows identified: 123
- Fresh API match coverage rate: 0.2238
- Matches with fresh API price: 47
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
Current: 294 value snapshots; fresh API coverage rate 0.2238.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 262 deduped forward/proxy rows; 123 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 11
Upcoming fixture rows: 11
Proxy price rows: 30
Sources attempted: 1
Errors: 0
- 2026-05-19 19:30 | Charleroi vs Oud-Heverlee Leuven | football_data_bet365_proxy | 1.85/4.0/3.7
- 2026-05-19 19:30 | Charleroi vs Oud-Heverlee Leuven | football_data_max_market_proxy | 1.85/4.0/4.2
- 2026-05-19 19:30 | Charleroi vs Oud-Heverlee Leuven | football_data_average_market_proxy | 1.77/3.84/3.91
- 2026-05-19 19:30 | Genk vs Antwerp | football_data_bet365_proxy | 1.55/4.2/5.5
- 2026-05-19 19:30 | Genk vs Antwerp | football_data_max_market_proxy | 1.58/4.33/5.8
- 2026-05-19 19:30 | Genk vs Antwerp | football_data_average_market_proxy | 1.53/4.15/5.36
- 2026-05-19 19:30 | Westerlo vs Standard | football_data_bet365_proxy | 2.1/3.5/3.3
- 2026-05-19 19:30 | Westerlo vs Standard | football_data_max_market_proxy | 2.1/3.6/3.5
- 2026-05-19 19:30 | Westerlo vs Standard | football_data_average_market_proxy | 2.01/3.51/3.3
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_bet365_proxy | 2.2/3.75/3.0
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_max_market_proxy | 2.2/3.75/3.1
- 2026-05-21 19:30 | Anderlecht vs St Truiden | football_data_average_market_proxy | 2.14/3.61/2.92
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_bet365_proxy | 4.5/3.7/1.75
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_max_market_proxy | 4.6/3.8/1.8
- 2026-05-21 19:30 | Gent vs St. Gilloise | football_data_average_market_proxy | 4.32/3.61/1.73
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_bet365_proxy | 7.0/4.75/1.38
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_max_market_proxy | 7.0/5.25/1.41
- 2026-05-21 19:30 | Mechelen vs Club Brugge | football_data_average_market_proxy | 6.57/5.0/1.37
- 2026-05-19 19:30 | Bournemouth vs Man City | football_data_bet365_proxy | 4.5/4.33/1.67
- 2026-05-19 19:30 | Bournemouth vs Man City | football_data_max_market_proxy | 4.6/4.5/1.7
- 2026-05-19 19:30 | Bournemouth vs Man City | football_data_average_market_proxy | 4.42/4.27/1.66
- 2026-05-19 20:15 | Chelsea vs Tottenham | football_data_bet365_proxy | 1.91/3.7/3.9
- 2026-05-19 20:15 | Chelsea vs Tottenham | football_data_max_market_proxy | 1.95/3.75/4.0

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 210
Fixture team rows unmatched: 412
Ready for model-fixture join: False
Automatic forward price rows: 77
odds-api.io price rows: 47
Football-Data price rows: 30
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
- AL Naft | suggestion=nan | type=unmatched
- Duhok FC | suggestion=nan | type=unmatched
- AL Talaba | suggestion=nan | type=unmatched
- AL Karma | suggestion=nan | type=unmatched
- AS Korofina | suggestion=nan | type=unmatched
- Binga FC | suggestion=nan | type=unmatched
- Audax Italiano | suggestion=nan | type=unmatched
- CA Barracas Central | suggestion=nan | type=unmatched
- Bagatelle | suggestion=nan | type=unmatched
- Pride of Gall Hill | suggestion=nan | type=unmatched
- Barra FC SC | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 210
Automatic price rows: 77
Value snapshot rows: 294
Matches with any automatic price: 57
Matches with fresh API price: 47
Matches with odds-api.io price: 47
Fresh API match coverage rate: 0.2238
odds-api.io match coverage rate: 0.2238
Real-money ready: False
## Match coverage
- 2026-05-19 | Ben Aknoun vs ES Mostaganem | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Klaipedos Fsm vs Dfk Dainava Alytus | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | MB Rouissat vs Paradou AC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | FC Noah Yerevan vs Ararat Yerevan FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Velez Nevesinje vs FK Vlasenica | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | FC Haka J vs Saaksjaerven Loiske | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Hapoel Acre FC vs Hapoel Hadera FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Hapoel Ra`anana FC vs FC Kafr Qasim | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | FC Kiisto vs Vpv | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | LSK Kvinner FK vs Hoenefoss BK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Maccabi Kabilio Jaffa vs Hapoel Afula FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | SK Brann 2 vs Sogndal 2 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | AS Korofina vs Binga FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | Derby Academie vs Onze Createurs | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | SV Ried vs Wolfsberger AC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-19 | CS Constantine vs USM Khenchela | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 210
Proxy price rows: 77
Matched prediction rows: 58
Value snapshot rows: 294
odds-api.io snapshot rows: 159
Baseline snapshot rows: 294
Full model snapshot rows: 0
Positive EV rows: 145
Source counts: {'odds_api_io_Bet365_ML': 159, 'football_data_max_market_proxy': 48, 'football_data_average_market_proxy': 48, 'football_data_bet365_proxy': 39}
- 2026-05-19 | FK Pempininkai vs FK Minija 2017 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3772 | EV=11.8248 | match=1.0
- 2026-05-19 | FC Haka J vs Saaksjaerven Loiske | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.3488 | EV=5.6272 | match=1.0
- 2026-05-19 | CA Rosario Central vs UCV FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-19 | Fluminense FC RJ vs Club Bolivar | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-19 | FK Pempininkai vs FK Minija 2017 | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.274 | EV=3.658 | match=1.0
- 2026-05-19 | FK Riteriai vs FK Kauno Zalgiris | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3772 | EV=3.5264 | match=1.0
- 2026-05-19 | FC Noah Yerevan vs Ararat Yerevan FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-19 | FC Haka J vs Saaksjaerven Loiske | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-05-19 | Ben Aknoun vs ES Mostaganem | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-19 | FC Kiisto vs Vpv | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=6.57 | prob=0.3772 | EV=1.478204 | match=1.0
- 2026-05-19 | FC Noah Yerevan vs Ararat Yerevan FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.274 | EV=1.466 | match=1.0
- 2026-05-19 | Hapoel Petah Tikva FC vs Beitar Jerusalem FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3772 | EV=1.3575 | match=1.0
- 2026-05-19 | Velez Nevesinje vs FK Vlasenica | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-19 | KRC Genk vs Royal Antwerp FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 294
Pre-dedupe proxy candidate observation rows: 94
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 6
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-19 | Hapoel Ra`anana FC vs FC Kafr Qasim | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-19 | Helsingborgs IF vs Varbergs BoIS | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-19 | AL Talaba vs AL Karma | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-19 | USM Alger vs Olympique Akbou | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-19 | AS Korofina vs Binga FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-21 | Gent vs St. Gilloise | selection=HOME | source=football_data_average_market_proxy | odds=4.32 | prob=0.3772 | EV=0.629504 | edge=0.145719 | penalty=0.6295073893753698 | tier=proxy_watchlist | score=0.1903
- 2026-05-19 | Hapoel Be`er Sheva FC vs Maccabi Tel Aviv FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244
- 2026-05-19 | LVU Rush vs Delaware FC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.123
- 2026-05-19 | Ben Aknoun vs ES Mostaganem | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171
- 2026-05-19 | Hapoel Petah Tikva FC vs Beitar Jerusalem FC | selection=DRAW | source=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.3700000000000001 | tier=suppressed_proxy_watchlist | score=0.1171
- 2026-05-19 | MB Rouissat vs Paradou AC | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3488 | EV=0.25568 | edge=0.071022 | penalty=0.2556789954568035 | tier=suppressed_proxy_watchlist | score=0.1171
- 2026-05-19 | Union Sportive Bougouba vs FC Mali Coura | selection=AWAY | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3488 | EV=0.2208 | edge=0.063086 | penalty=0.22080122080122067 | tier=suppressed_proxy_watchlist | score=0.1155

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
- market_alignment_penalty_too_high_for_real_candidate: 10
- ev_above_real_candidate_cap_possible_overconfidence: 9
- probability_or_league_rule_suppressed: 6
- low_probability_band_under_0_35: 6
- watchlist_only_pending_forward_settlement: 2
- delayed_football_data_proxy_not_fresh_api_price: 1
## Row explanations
- 2026-05-19 | Hapoel Ra`anana FC vs FC Kafr Qasim | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Helsingborgs IF vs Varbergs BoIS | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | AL Talaba vs AL Karma | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-19 | USM Alger vs Olympique Akbou | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | AS Korofina vs Binga FC | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-21 | Gent vs St. Gilloise | sel=HOME | score=0.1903 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-19 | Hapoel Be`er Sheva FC vs Maccabi Tel Aviv FC | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | LVU Rush vs Delaware FC | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Ben Aknoun vs ES Mostaganem | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Hapoel Petah Tikva FC vs Beitar Jerusalem FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | MB Rouissat vs Paradou AC | sel=AWAY | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Union Sportive Bougouba vs FC Mali Coura | sel=AWAY | score=0.1155 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 294
Paper proxy observation rows: 25
Positive EV value rows: 145
Suppressed-band observation rows: 0
Distinct matches: 17
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.585404
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=11, avg_ev=0.5374, max_ev=0.744
- draw: rows=5, avg_ev=0.4933, max_ev=0.7125
- home: rows=9, avg_ev=0.6953, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 210
Forward fixture prediction rows: 210
Full model prediction rows: 0
Baseline prediction rows: 210
Max forward predictions: 300
Ready for price join: True
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 15:00 | Klaipedos Fsm vs Dfk Dainava Alytus | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 15:00 | MB Rouissat vs Paradou AC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 15:00 | FC Noah Yerevan vs Ararat Yerevan FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 15:00 | Velez Nevesinje vs FK Vlasenica | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:00 | FC Haka J vs Saaksjaerven Loiske | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:00 | Hapoel Acre FC vs Hapoel Hadera FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:00 | Hapoel Nof Hagalil FC vs Ironi Modiin | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:00 | Hapoel Ra`anana FC vs FC Kafr Qasim | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:00 | FC Kiisto vs Vpv | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:00 | LSK Kvinner FK vs Hoenefoss BK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:00 | Maccabi Kabilio Jaffa vs Hapoel Afula FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:00 | SK Brann 2 vs Sogndal 2 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:30 | AS Korofina vs Binga FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:30 | Derby Academie vs Onze Createurs | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:30 | SV Ried vs Wolfsberger AC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 16:45 | CS Constantine vs USM Khenchela | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 17:00 | AL Naft vs Duhok FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 17:00 | AL Talaba vs AL Karma | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-19 17:00 | CA River Plate (URU) vs Deportivo Maldonado Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 210
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 2427
Log type: probability_only_no_market_prices
- 2026-05-20 2026-05-19 23:00:00 | Seacoast United Phantoms vs Western Mass Pioneers | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-19 23:30:00 | East Atlanta FC vs Columbus United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-19 23:30:00 | Fort Wayne FC vs Corpus Christi FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-19 23:30:00 | Morris Elite SC vs Ironbound SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-19 23:30:00 | New Jersey Copa FC vs Paisley Athletic FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-20 2026-05-19 23:30:00 | Northern Virginia FC vs Lancaster Inferno | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 08:00:00 | Hapoel Ironi Kiryat Shmona vs Hapoel Ako | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 16:00:00 | Atromitos vs Panserraikos | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 17:00:00 | Kifisia vs Larisa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 17:00:00 | Panetolikos vs Asteras Tripolis | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 19:30:00 | Anderlecht vs St Truiden | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 19:30:00 | Gent vs St. Gilloise | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-21 2026-05-19 19:30:00 | Mechelen vs Club Brugge | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-22 2026-05-19 11:30:00 | Hubei Istar vs Chengdu Rongcheng B | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-22 2026-05-19 16:15:00 | HNK Hajduk Split vs HNK Vukovar 1991 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-19 05:00:00 | Uwa Nedlands FC Reserves vs Murdoch University Melville FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-19 07:00:00 | UWA Nedlands FC vs Murdoch University Melville FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-19 08:00:00 | HNK Hajduk Split vs NK Osijek | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-19 11:00:00 | Shanghai Port FC vs Tianjin Jinmen Tiger | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-19 12:00:00 | Dalian Yingbo FC vs Chengdu Rongcheng | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 210
Manual template rows: 210
Rows with complete manual odds: 0
Rows missing manual odds: 210
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
- 2026-05-19 17:00 | AL Naft vs Duhok FC
- 2026-05-19 17:00 | AL Talaba vs AL Karma
- 2026-05-19 16:30 | AS Korofina vs Binga FC
- 2026-05-19 22:00 | Audax Italiano vs CA Barracas Central
- 2026-05-19 23:00 | Bagatelle vs Pride of Gall Hill
- 2026-05-19 18:00 | Barra FC SC vs Concordia SC
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem
- 2026-05-19 18:00 | Boston Bolts vs Vermont Green FC
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve
- 2026-05-19 19:30 | Bournemouth vs Man City
- 2026-05-19 18:30:00 | Bournemouth vs Manchester City
- 2026-05-19 18:00 | CA Banfield vs CA Aldosivi Reserve

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 210
Source counts: {'odds_api_io_events_bookmaker_filtered': 189, 'football_data_fixtures_proxy': 11, 'odds_api_io_events_search': 9, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-19 18:30 | AFC Bournemouth vs Manchester City | england-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | AC Monza vs Juve Stabia | italy-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:30 | Afrique Football Elite vs AS Bakaridjan | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-19 17:00 | AL Naft vs Duhok FC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 17:00 | AL Talaba vs AL Karma | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 16:30 | AS Korofina vs Binga FC | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-19 22:00 | Audax Italiano vs CA Barracas Central | international-clubs-copa-sudamericana | odds_api_io_events_bookmaker_filtered
- 2026-05-19 23:00 | Bagatelle vs Pride of Gall Hill | barbados-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | Barra FC SC vs Concordia SC | brazil-u20-catarinense-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem | algeria-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | Boston Bolts vs Vermont Green FC | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 19:30 | Bournemouth vs Man City | premier_league | football_data_fixtures_proxy
- 2026-05-19 18:30:00 | Bournemouth vs Manchester City | premier_league | thesportsdb_eventsnextleague
- 2026-05-19 18:00 | CA Banfield vs CA Aldosivi Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 18:00 | CA Quilmes Reserve vs CA Lanus | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 17:00 | CA River Plate (URU) vs Deportivo Maldonado Reserve | uruguay-tercera-division-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 22:00 | CA Rosario Central vs UCV FC | international-clubs-copa-libertadores | odds_api_io_events_bookmaker_filtered
- 2026-05-19 19:30 | Charleroi vs Oud-Heverlee Leuven | B1 | football_data_fixtures_proxy
- 2026-05-19 20:15 | Chelsea vs Tottenham | premier_league | football_data_fixtures_proxy
- 2026-05-19 18:00 | Colon de Santa Fe Reserve vs Ferro Carril Oeste | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-19 22:00 | Coquimbo Unido vs CD Tolima | international-clubs-copa-libertadores | odds_api_io_events_bookmaker_filtered
- 2026-05-19 16:45 | CS Constantine vs USM Khenchela | algeria-ligue-1 | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 210
Rows with complete odds: 0
- 2026-05-19 18:30 | AFC Bournemouth vs Manchester City | bookmaker=bet365_manual
- 2026-05-19 18:00 | AC Monza vs Juve Stabia | bookmaker=bet365_manual
- 2026-05-19 18:30 | Afrique Football Elite vs AS Bakaridjan | bookmaker=bet365_manual
- 2026-05-19 17:00 | AL Naft vs Duhok FC | bookmaker=bet365_manual
- 2026-05-19 17:00 | AL Talaba vs AL Karma | bookmaker=bet365_manual
- 2026-05-19 16:30 | AS Korofina vs Binga FC | bookmaker=bet365_manual
- 2026-05-19 22:00 | Audax Italiano vs CA Barracas Central | bookmaker=bet365_manual
- 2026-05-19 23:00 | Bagatelle vs Pride of Gall Hill | bookmaker=bet365_manual
- 2026-05-19 18:00 | Barra FC SC vs Concordia SC | bookmaker=bet365_manual
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem | bookmaker=bet365_manual
- 2026-05-19 18:00 | Boston Bolts vs Vermont Green FC | bookmaker=bet365_manual
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve | bookmaker=bet365_manual
- 2026-05-19 19:30 | Bournemouth vs Man City | bookmaker=bet365_manual
- 2026-05-19 18:30:00 | Bournemouth vs Manchester City | bookmaker=bet365_manual
- 2026-05-19 18:00 | CA Banfield vs CA Aldosivi Reserve | bookmaker=bet365_manual
- 2026-05-19 18:00 | CA Quilmes Reserve vs CA Lanus | bookmaker=bet365_manual
- 2026-05-19 17:00 | CA River Plate (URU) vs Deportivo Maldonado Reserve | bookmaker=bet365_manual
- 2026-05-19 22:00 | CA Rosario Central vs UCV FC | bookmaker=bet365_manual
- 2026-05-19 19:30 | Charleroi vs Oud-Heverlee Leuven | bookmaker=bet365_manual
- 2026-05-19 20:15 | Chelsea vs Tottenham | bookmaker=bet365_manual
- 2026-05-19 18:00 | Colon de Santa Fe Reserve vs Ferro Carril Oeste | bookmaker=bet365_manual
- 2026-05-19 22:00 | Coquimbo Unido vs CD Tolima | bookmaker=bet365_manual
- 2026-05-19 16:45 | CS Constantine vs USM Khenchela | bookmaker=bet365_manual
- 2026-05-19 16:30 | Derby Academie vs Onze Createurs | bookmaker=bet365_manual

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
- 2026-05-19 17:00 | AL Naft vs Duhok FC
- 2026-05-19 17:00 | AL Talaba vs AL Karma
- 2026-05-19 16:30 | AS Korofina vs Binga FC
- 2026-05-19 22:00 | Audax Italiano vs CA Barracas Central
- 2026-05-19 23:00 | Bagatelle vs Pride of Gall Hill
- 2026-05-19 18:00 | Barra FC SC vs Concordia SC
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem
- 2026-05-19 18:00 | Boston Bolts vs Vermont Green FC
- 2026-05-19 17:00 | Boston River vs Central Espanol Reserve
- 2026-05-19 19:30 | Bournemouth vs Man City
- 2026-05-19 18:30:00 | Bournemouth vs Manchester City
- 2026-05-19 18:00 | CA Banfield vs CA Aldosivi Reserve
- 2026-05-19 18:00 | CA Quilmes Reserve vs CA Lanus
- 2026-05-19 17:00 | CA River Plate (URU) vs Deportivo Maldonado Reserve
- 2026-05-19 22:00 | CA Rosario Central vs UCV FC
- 2026-05-19 19:30 | Charleroi vs Oud-Heverlee Leuven

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 388
Valid forward/proxy log rows: 385
Deduped forward/proxy observation rows: 262
Duplicate forward/proxy log rows: 123
Valid automatic proxy observation rows: 385
Deduped automatic proxy observation rows: 262
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-15 | Shanghai Port FC vs Zhejiang FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-19 | MB Rouissat vs Paradou AC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
- 2026-05-14 | Kjp Kouvola vs Lautp | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0596
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
### Bournemouth vs Man City
- Date/time: 2026-05-19 19:30
- League/phase: premier_league / automatic_forward_price_proxy
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
- Prediction ID: 57cd14c3b3765ccf72bb
### Bournemouth vs Manchester City
- Date/time: 2026-05-19 18:30:00
- League/phase: premier_league / automatic_forward_price_proxy
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
Newly logged paper-test picks: 24
Total logged paper-test rows: 388
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 294, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 132, 'current_paper_picks': 25, 'newly_logged_picks': 24, 'total_logged_paper_rows': 388, 'source_used': 'automatic_forward_value_snapshots'}
- Bournemouth vs Man City | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Bournemouth vs Manchester City | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AFC Bournemouth vs Manchester City | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AFC Bournemouth vs Manchester City | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Bournemouth vs Manchester City | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Bournemouth vs Man City | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.6 | prob=0.3772 | EV=0.7351 | edge=0.1598 | penalty=0.7351 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gent vs St. Gilloise | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Royal Charleroi SC vs Oud-Heverlee Leuven | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Charleroi vs Oud-Heverlee Leuven | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CS Constantine vs USM Khenchela | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- IF Sao Joseense PR vs Azuriz FC PR | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Fluminense FC RJ vs Club Bolivar | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.25 | prob=0.274 | EV=0.7125 | edge=0.114 | penalty=0.7125 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hapoel Acre FC vs Hapoel Hadera FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Royal Charleroi SC vs Oud-Heverlee Leuven | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Charleroi vs Oud-Heverlee Leuven | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Kiisto vs Vpv | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.75 | prob=0.274 | EV=0.5755 | edge=0.1001 | penalty=0.5755 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Hapoel Be`er Sheva FC vs Maccabi Tel Aviv FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
