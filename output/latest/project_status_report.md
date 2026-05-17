# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-17T02:28:16.702612+00:00`
GitHub run: `355` attempt `1`
GitHub SHA: `9ec5541bffda471656ecbcc3913f9b695b78ef36`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 71 |  |  |
| Football-Data upcoming odds proxy | True | 211 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 51 |  |  |
| odds-api.io forward fixtures | True | 583 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 609 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 5 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 300 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 1014
- Positive EV proxy rows: 515
- Proxy observation rows: 25
- Valid forward/proxy log rows: 290
- Deduped forward/proxy log rows: 193
- Duplicate forward/proxy log rows identified: 97
- Fresh API match coverage rate: 0.2
- Matches with fresh API price: 60
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
Current: 1014 value snapshots; fresh API coverage rate 0.2.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 193 deduped forward/proxy rows; 97 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 112
Upcoming fixture rows: 71
Proxy price rows: 211
Sources attempted: 1
Errors: 0
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_bet365_proxy | 1.83/3.6/3.75
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_max_market_proxy | 1.87/4.0/4.0
- 2026-05-17 12:30 | Anderlecht vs Mechelen | football_data_average_market_proxy | 1.8/3.72/3.79
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_bet365_proxy | 2.05/3.5/3.1
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_max_market_proxy | 2.1/3.8/3.45
- 2026-05-17 17:30 | Club Brugge vs St. Gilloise | football_data_average_market_proxy | 2.02/3.51/3.23
- 2026-05-17 14:30 | Bielefeld vs Hertha | football_data_bet365_proxy | 1.73/3.9/4.33
- 2026-05-17 14:30 | Bielefeld vs Hertha | football_data_max_market_proxy | 1.75/4.4/4.33
- 2026-05-17 14:30 | Bielefeld vs Hertha | football_data_average_market_proxy | 1.7/4.08/3.93
- 2026-05-17 14:30 | Darmstadt vs Paderborn | football_data_bet365_proxy | 3.25/4.1/1.83
- 2026-05-17 14:30 | Darmstadt vs Paderborn | football_data_max_market_proxy | 3.5/4.33/1.93
- 2026-05-17 14:30 | Darmstadt vs Paderborn | football_data_average_market_proxy | 3.32/4.04/1.84
- 2026-05-17 14:30 | Dresden vs Holstein Kiel | football_data_bet365_proxy | 1.67/4.1/4.2
- 2026-05-17 14:30 | Dresden vs Holstein Kiel | football_data_max_market_proxy | 1.73/4.1/4.5
- 2026-05-17 14:30 | Dresden vs Holstein Kiel | football_data_average_market_proxy | 1.67/3.93/4.19
- 2026-05-17 14:30 | Elversberg vs Preußen Münster | football_data_bet365_proxy | 1.22/6.0/10.0
- 2026-05-17 14:30 | Elversberg vs Preußen Münster | football_data_max_market_proxy | 1.26/6.5/13.0
- 2026-05-17 14:30 | Elversberg vs Preußen Münster | football_data_average_market_proxy | 1.21/6.11/10.13
- 2026-05-17 14:30 | Greuther Furth vs Fortuna Dusseldorf | football_data_bet365_proxy | 2.5/3.6/2.5
- 2026-05-17 14:30 | Greuther Furth vs Fortuna Dusseldorf | football_data_max_market_proxy | 2.6/3.75/2.63
- 2026-05-17 14:30 | Greuther Furth vs Fortuna Dusseldorf | football_data_average_market_proxy | 2.45/3.59/2.48
- 2026-05-17 14:30 | Hannover vs Nurnberg | football_data_bet365_proxy | 1.44/4.75/5.75
- 2026-05-17 14:30 | Hannover vs Nurnberg | football_data_max_market_proxy | 1.45/5.0/6.6

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 465
Fixture team rows unmatched: 843
Ready for model-fixture join: False
Automatic forward price rows: 271
odds-api.io price rows: 60
Football-Data price rows: 211
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 07 Vestur Sorvagur | suggestion=nan | type=unmatched
- NSI Runavik | suggestion=nan | type=unmatched
- 1. FC Magdeburg | suggestion=nan | type=unmatched
- 1 FC Kaiserslautern | suggestion=nan | type=unmatched
- 9 de Octubre FC | suggestion=nan | type=unmatched
- CD El Nacional | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Lazio Rome | suggestion=nan | type=unmatched
- FC Abdysh-Ata | suggestion=nan | type=unmatched
- FC Alay | suggestion=nan | type=unmatched
- AC Prato 1908 | suggestion=nan | type=unmatched
- ASD Seravezza Pozzi Calcio | suggestion=nan | type=unmatched
- AC Vigasio | suggestion=nan | type=unmatched
- Obermais | suggestion=nan | type=unmatched
- AD Cantolao | suggestion=nan | type=unmatched
- Carlos Mannucci | suggestion=nan | type=unmatched
- AEK | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 271
Value snapshot rows: 1014
Matches with any automatic price: 115
Matches with fresh API price: 60
Matches with odds-api.io price: 60
Fresh API match coverage rate: 0.2
odds-api.io match coverage rate: 0.2
Real-money ready: False
## Match coverage
- 2026-05-17 | Como vs Parma | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | Genoa vs Milan | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | Juventus vs Fiorentina | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | Pisa vs Napoli | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | Roma vs Lazio | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | Anderlecht vs Mechelen | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | Man United vs Nott'm Forest | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | La Coruna vs Andorra | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | 1. FC Magdeburg vs 1 FC Kaiserslautern | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Arminia Bielefeld vs Hertha BSC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | AZ Alkmaar vs NAC Breda | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | Dynamo Dresden vs Holstein Kiel | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Hamilton Academical WFC vs Montrose FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Hannover 96 vs 1 FC Nuremberg | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Heerenveen vs Ajax | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | Heracles vs Groningen | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-17 | FC Hradec Kralove vs FK Pardubice | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 271
Matched prediction rows: 138
Value snapshot rows: 1014
odds-api.io snapshot rows: 225
Baseline snapshot rows: 846
Full model snapshot rows: 168
Positive EV rows: 515
Source counts: {'football_data_max_market_proxy': 267, 'football_data_average_market_proxy': 267, 'football_data_bet365_proxy': 255, 'odds_api_io_Bet365_ML': 225}
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=0.8114
- 2026-05-17 | Elversberg vs Preußen Münster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-17 | Inter vs Verona | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.292 | EV=3.38 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3217 | EV=3.1821 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3217 | EV=2.8604 | match=1.0
- 2026-05-17 | Fenerbahce vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-17 | Fenerbahce Istanbul vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=0.96
- 2026-05-17 | Inter vs Verona | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.88 | prob=0.292 | EV=2.76096 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3217 | EV=2.648078 | match=1.0
- 2026-05-17 | Elversberg vs Preußen Münster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.13 | prob=0.3488 | EV=2.533344 | match=1.0
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.13 | prob=0.3488 | EV=2.533344 | match=0.8114
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=10.0 | prob=0.3488 | EV=2.488 | match=0.8114
- 2026-05-17 | Elversberg vs Preußen Münster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Fenerbahce vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=9.53 | prob=0.3488 | EV=2.324064 | match=1.0
- 2026-05-17 | Fenerbahce Istanbul vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=9.53 | prob=0.3488 | EV=2.324064 | match=0.96

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 1014
Pre-dedupe proxy candidate observation rows: 413
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-17 | Wolverhampton Wanderers vs Fulham FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-17 | SV Darmstadt 98 vs SC Paderborn 07 | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-17 | KF Aegir vs IF Vestri | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-17 | Darmstadt vs Paderborn | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-17 | Wolves vs Fulham | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3554 | EV=0.35052 | edge=0.092242 | penalty=0.3505194597922161 | tier=proxy_watchlist | score=0.2547
- 2026-05-17 | Kaisar Kyzylorda vs Tobol Kostanay | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-17 | Leeds United vs Brighton & Hove Albion | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-17 | FA Siauliai B vs FK Ekranas | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-17 | Ayvalikgucu Belediyespor vs 52 Orduspor FK | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-17 | Victoria United Limbe vs Aigle Royal Du Moungo | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-17 | SSD Nissa FC vs Reggina 1914 | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-17 | Panathinaikos Athens vs PAOK Thessaloniki | selection=HOME | source=football_data_max_market_proxy | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2271

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
- delayed_football_data_proxy_not_fresh_api_price: 1
## Row explanations
- 2026-05-17 | Wolverhampton Wanderers vs Fulham FC | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | SV Darmstadt 98 vs SC Paderborn 07 | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | KF Aegir vs IF Vestri | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Darmstadt vs Paderborn | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Wolves vs Fulham | sel=HOME | score=0.2547 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Kaisar Kyzylorda vs Tobol Kostanay | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Leeds United vs Brighton & Hove Albion | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | FA Siauliai B vs FK Ekranas | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-17 | Ayvalikgucu Belediyespor vs 52 Orduspor FK | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-17 | Victoria United Limbe vs Aigle Royal Du Moungo | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-17 | SSD Nissa FC vs Reggina 1914 | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-17 | Panathinaikos Athens vs PAOK Thessaloniki | sel=HOME | score=0.2271 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 1014
Paper proxy observation rows: 25
Positive EV value rows: 515
Suppressed-band observation rows: 0
Distinct matches: 14
Distinct sources: 0
Max EV: 0.77765
Average EV: 0.399475
Max probability edge: 0.148124
Average match confidence: None
## By selection
- away: rows=14, avg_ev=0.3983, max_ev=0.7776
- draw: rows=7, avg_ev=0.3552, max_ev=0.5847
- home: rows=4, avg_ev=0.481, max_ev=0.6718

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 465
Forward fixture prediction rows: 300
Full model prediction rows: 18
Baseline prediction rows: 282
Max forward predictions: 300
Ready for price join: True
- 2026-05-17 11:00 | Como vs Parma | coverage=full_team_strength_match | H=0.3999 D=0.2785 A=0.3217 | fair=2.5/3.59/3.11
- 2026-05-17 11:00 | Genoa vs Milan | coverage=full_team_strength_match | H=0.3447 D=0.2762 A=0.3792 | fair=2.9/3.62/2.64
- 2026-05-17 11:00 | Juventus vs Fiorentina | coverage=full_team_strength_match | H=0.3925 D=0.2806 A=0.3269 | fair=2.55/3.56/3.06
- 2026-05-17 11:00 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 11:00 | Roma vs Lazio | coverage=full_team_strength_match | H=0.3939 D=0.2857 A=0.3203 | fair=2.54/3.5/3.12
- 2026-05-17 12:30 | Anderlecht vs Mechelen | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 12:30 | Man United vs Nott'm Forest | coverage=full_team_strength_match | H=0.3959 D=0.2656 A=0.3386 | fair=2.53/3.77/2.95
- 2026-05-17 13:00 | La Coruna vs Andorra | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | 1. FC Magdeburg vs 1 FC Kaiserslautern | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Arminia Bielefeld vs Hertha BSC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | AZ Alkmaar vs NAC Breda | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Dynamo Dresden vs Holstein Kiel | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Hamilton Academical WFC vs Montrose FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Hannover 96 vs 1 FC Nuremberg | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Heerenveen vs Ajax | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Heracles vs Groningen | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | FC Hradec Kralove vs FK Pardubice | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Karlsruher SC vs VfL Bochum | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Nijmegen vs Go Ahead Eagles | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | PSV Eindhoven vs Twente | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 13:30 | Schalke 04 vs Eintracht Braunschweig | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 2056
Log type: probability_only_no_market_prices
- 2026-05-17 2026-05-17 18:45:00 | Cagliari Calcio vs Torino FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 18:45:00 | Calcio Lecco 1912 vs Calcio Catania | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 18:45:00 | Sassuolo Calcio vs US Lecce | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 18:45:00 | Udinese Calcio vs US Cremonese | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Alagoinhas AC BA vs EC Jacuipense BA | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | America FC RN vs Club Laguna SAF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Athletic Club Sjdr MG vs EC Juventude RS | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Bolivar SC vs Monagas SC B | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Botafogo FR RJ vs SC Corinthians SP | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | CD Afiz vs Deportivo Escara | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Cianorte FC PR vs Cascavel PR | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Cobresal vs Universidad de Chile | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | CRA Catalano GO vs Abecat Ouvidorense GO | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | EC Bahia BA vs Gremio FB Porto Alegrense RS | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Ferroviaria Araraquara SP vs Brusque FC SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Huracan FC vs CA Atenas de San Carlos | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Lille OSC vs AJ Auxerre | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | FC Lorient vs Le Havre AC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | OGC Nice vs FC Metz | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 19:00:00 | Olympique Lyon vs Racing Club De Lens | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 465
Manual template rows: 465
Rows with complete manual odds: 0
Rows missing manual odds: 465
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-17 16:15 | 07 Vestur Sorvagur vs NSI Runavik
- 2026-05-17 13:30 | 1. FC Magdeburg vs 1 FC Kaiserslautern
- 2026-05-17 20:30 | 9 de Octubre FC vs CD El Nacional
- 2026-05-17 16:00 | ACF Fiorentina vs Lazio Rome
- 2026-05-17 14:30 | FC Abdysh-Ata vs FC Alay
- 2026-05-17 14:00 | AC Prato 1908 vs ASD Seravezza Pozzi Calcio
- 2026-05-17 14:00 | AC Vigasio vs Obermais
- 2026-05-17 16:00 | AD Cantolao vs Carlos Mannucci
- 2026-05-17 17:30 | AEK vs Olympiakos
- 2026-05-17 16:30 | AEK Athens vs Olympiacos Piraeus
- 2026-05-17 17:00 | Af Elbasani vs KF Egnatia Rrogozhine
- 2026-05-17 16:00 | AGF Aarhus vs Viborg FF
- 2026-05-17 17:00 | Aguilas FC vs Utebo FC
- 2026-05-17 14:10 | AL Bataeh vs Shabab AL Ahli Dubai Club
- 2026-05-17 14:10 | AL Wahda FC vs AL Dhafra U23

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 465
Source counts: {'odds_api_io_events_bookmaker_filtered': 385, 'football_data_fixtures_proxy': 71, 'odds_api_io_events_search': 9}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-17 16:15 | 07 Vestur Sorvagur vs NSI Runavik | faroe-islands-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 13:30 | 1. FC Magdeburg vs 1 FC Kaiserslautern | germany-2-bundesliga | odds_api_io_events_bookmaker_filtered
- 2026-05-17 20:30 | 9 de Octubre FC vs CD El Nacional | ecuador-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-17 16:00 | ACF Fiorentina vs Lazio Rome | italy-serie-a-women | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:30 | FC Abdysh-Ata vs FC Alay | kyrgyzstan-top-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:00 | AC Prato 1908 vs ASD Seravezza Pozzi Calcio | italy-serie-d-group-e | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:00 | AC Vigasio vs Obermais | italy-serie-d-group-c | odds_api_io_events_bookmaker_filtered
- 2026-05-17 16:00 | AD Cantolao vs Carlos Mannucci | peru-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-17 17:30 | AEK vs Olympiakos | G1 | football_data_fixtures_proxy
- 2026-05-17 16:30 | AEK Athens vs Olympiacos Piraeus | greece-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 17:00 | Af Elbasani vs KF Egnatia Rrogozhine | albania-kategoria-superiore | odds_api_io_events_bookmaker_filtered
- 2026-05-17 16:00 | AGF Aarhus vs Viborg FF | denmark-superliga | odds_api_io_events_bookmaker_filtered
- 2026-05-17 17:00 | Aguilas FC vs Utebo FC | spain-segunda-federacion | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:10 | AL Bataeh vs Shabab AL Ahli Dubai Club | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:10 | AL Wahda FC vs AL Dhafra U23 | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 18:00 | Al-Shabab FC (SA) vs Al-Ittihad Club | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 19:00 | Alagoinhas AC BA vs EC Jacuipense BA | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-17 21:00 | Albion FC vs Montevideo Wanderers | uruguay-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-17 18:00 | America FC MG vs Sao Paulo FC SP | brazil-u20-campeonato-brasileiro | odds_api_io_events_bookmaker_filtered
- 2026-05-17 19:00 | America FC RN vs Club Laguna SAF | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-17 21:00 | Anapolis FC GO vs Barra FC SC | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-17 12:30 | Anderlecht vs Mechelen | B1 | football_data_fixtures_proxy
- 2026-05-17 18:00 | Antalyaspor vs Kocaelispor | T1 | football_data_fixtures_proxy

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 465
Rows with complete odds: 0
- 2026-05-17 16:15 | 07 Vestur Sorvagur vs NSI Runavik | bookmaker=bet365_manual
- 2026-05-17 13:30 | 1. FC Magdeburg vs 1 FC Kaiserslautern | bookmaker=bet365_manual
- 2026-05-17 20:30 | 9 de Octubre FC vs CD El Nacional | bookmaker=bet365_manual
- 2026-05-17 16:00 | ACF Fiorentina vs Lazio Rome | bookmaker=bet365_manual
- 2026-05-17 14:30 | FC Abdysh-Ata vs FC Alay | bookmaker=bet365_manual
- 2026-05-17 14:00 | AC Prato 1908 vs ASD Seravezza Pozzi Calcio | bookmaker=bet365_manual
- 2026-05-17 14:00 | AC Vigasio vs Obermais | bookmaker=bet365_manual
- 2026-05-17 16:00 | AD Cantolao vs Carlos Mannucci | bookmaker=bet365_manual
- 2026-05-17 17:30 | AEK vs Olympiakos | bookmaker=bet365_manual
- 2026-05-17 16:30 | AEK Athens vs Olympiacos Piraeus | bookmaker=bet365_manual
- 2026-05-17 17:00 | Af Elbasani vs KF Egnatia Rrogozhine | bookmaker=bet365_manual
- 2026-05-17 16:00 | AGF Aarhus vs Viborg FF | bookmaker=bet365_manual
- 2026-05-17 17:00 | Aguilas FC vs Utebo FC | bookmaker=bet365_manual
- 2026-05-17 14:10 | AL Bataeh vs Shabab AL Ahli Dubai Club | bookmaker=bet365_manual
- 2026-05-17 14:10 | AL Wahda FC vs AL Dhafra U23 | bookmaker=bet365_manual
- 2026-05-17 18:00 | Al-Shabab FC (SA) vs Al-Ittihad Club | bookmaker=bet365_manual
- 2026-05-17 19:00 | Alagoinhas AC BA vs EC Jacuipense BA | bookmaker=bet365_manual
- 2026-05-17 21:00 | Albion FC vs Montevideo Wanderers | bookmaker=bet365_manual
- 2026-05-17 18:00 | America FC MG vs Sao Paulo FC SP | bookmaker=bet365_manual
- 2026-05-17 19:00 | America FC RN vs Club Laguna SAF | bookmaker=bet365_manual
- 2026-05-17 21:00 | Anapolis FC GO vs Barra FC SC | bookmaker=bet365_manual
- 2026-05-17 12:30 | Anderlecht vs Mechelen | bookmaker=bet365_manual
- 2026-05-17 18:00 | Antalyaspor vs Kocaelispor | bookmaker=bet365_manual
- 2026-05-17 18:30 | Argentino de Rosario vs CA Central Cordoba Rosario | bookmaker=bet365_manual

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
- 2026-05-17 16:15 | 07 Vestur Sorvagur vs NSI Runavik
- 2026-05-17 13:30 | 1. FC Magdeburg vs 1 FC Kaiserslautern
- 2026-05-17 20:30 | 9 de Octubre FC vs CD El Nacional
- 2026-05-17 16:00 | ACF Fiorentina vs Lazio Rome
- 2026-05-17 14:30 | FC Abdysh-Ata vs FC Alay
- 2026-05-17 14:00 | AC Prato 1908 vs ASD Seravezza Pozzi Calcio
- 2026-05-17 14:00 | AC Vigasio vs Obermais
- 2026-05-17 16:00 | AD Cantolao vs Carlos Mannucci
- 2026-05-17 17:30 | AEK vs Olympiakos
- 2026-05-17 16:30 | AEK Athens vs Olympiacos Piraeus
- 2026-05-17 17:00 | Af Elbasani vs KF Egnatia Rrogozhine
- 2026-05-17 16:00 | AGF Aarhus vs Viborg FF
- 2026-05-17 17:00 | Aguilas FC vs Utebo FC
- 2026-05-17 14:10 | AL Bataeh vs Shabab AL Ahli Dubai Club
- 2026-05-17 14:10 | AL Wahda FC vs AL Dhafra U23
- 2026-05-17 18:00 | Al-Shabab FC (SA) vs Al-Ittihad Club
- 2026-05-17 19:00 | Alagoinhas AC BA vs EC Jacuipense BA
- 2026-05-17 21:00 | Albion FC vs Montevideo Wanderers
- 2026-05-17 18:00 | America FC MG vs Sao Paulo FC SP

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 293
Valid forward/proxy log rows: 290
Deduped forward/proxy observation rows: 193
Duplicate forward/proxy log rows: 97
Valid automatic proxy observation rows: 290
Deduped automatic proxy observation rows: 193
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
### Genoa vs Milan
- Date/time: 2026-05-17 11:00
- League/phase: serie_a / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.5
- Fair odds: 2.9
- Model probability: 0.3447
- Probability band: 0.25-0.35
- EV: 0.5512
- Probability edge: 0.1225
- Alignment penalty: 0.5512
- Suppression action: none
- Paper tier: volume_observation
- Paper score: 0.2964
- Prediction ID: d9610f99658e74875e25
### Como vs Parma
- Date/time: 2026-05-17 11:00
- League/phase: serie_a / automatic_forward_price_proxy
- Selection: DRAW
- Market odds: 5.69
- Fair odds: 3.59
- Model probability: 0.2785
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
Newly logged paper-test picks: 15
Total logged paper-test rows: 293
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 1014, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 517, 'current_paper_picks': 25, 'newly_logged_picks': 15, 'total_logged_paper_rows': 293, 'source_used': 'automatic_forward_value_snapshots'}
- Genoa vs Milan | coverage=full_team_strength_match | selection=HOME | odds=4.5 | prob=0.3447 | EV=0.5512 | edge=0.1225 | penalty=0.5512 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.69 | prob=0.2785 | EV=0.5847 | edge=0.1028 | penalty=0.5847 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.28 | prob=0.2806 | EV=0.4816 | edge=0.0912 | penalty=0.4816 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Brentford vs Crystal Palace | coverage=full_team_strength_match | selection=AWAY | odds=4.4 | prob=0.3213 | EV=0.4137 | edge=0.094 | penalty=0.4137 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.25 | prob=0.2785 | EV=0.4621 | edge=0.088 | penalty=0.4621 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Brentford vs Crystal Palace | coverage=full_team_strength_match | selection=AWAY | odds=4.33 | prob=0.3213 | EV=0.3912 | edge=0.0904 | penalty=0.3912 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Elche vs Getafe | coverage=full_team_strength_match | selection=AWAY | odds=4.0 | prob=0.3791 | EV=0.5164 | edge=0.1291 | penalty=0.5164 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.0 | prob=0.2806 | EV=0.403 | edge=0.0806 | penalty=0.403 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Atalanta vs Bologna | coverage=full_team_strength_match | selection=AWAY | odds=5.0 | prob=0.2697 | EV=0.3485 | edge=0.0697 | penalty=0.3485 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Osasuna vs Espanol | coverage=full_team_strength_match | selection=AWAY | odds=4.0 | prob=0.3559 | EV=0.4236 | edge=0.1059 | penalty=0.4236 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=volume_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.5 | prob=0.2857 | EV=0.2857 | edge=0.0635 | penalty=0.2857 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Elche vs Getafe | coverage=full_team_strength_match | selection=AWAY | odds=3.57 | prob=0.3791 | EV=0.3534 | edge=0.099 | penalty=0.3534 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Atalanta vs Bologna | coverage=full_team_strength_match | selection=AWAY | odds=4.75 | prob=0.2697 | EV=0.2811 | edge=0.0592 | penalty=0.2811 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Ath Madrid vs Girona | coverage=full_team_strength_match | selection=AWAY | odds=4.5 | prob=0.2813 | EV=0.2658 | edge=0.0591 | penalty=0.2659 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Ath Madrid vs Girona | coverage=full_team_strength_match | selection=AWAY | odds=4.5 | prob=0.2813 | EV=0.2658 | edge=0.0591 | penalty=0.2659 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Osasuna vs Espanol | coverage=full_team_strength_match | selection=AWAY | odds=3.8 | prob=0.3559 | EV=0.3524 | edge=0.0927 | penalty=0.3524 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Wolves vs Fulham | coverage=full_team_strength_match | selection=HOME | odds=3.8 | prob=0.3554 | EV=0.3505 | edge=0.0922 | penalty=0.3505 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Wolves vs Fulham | coverage=full_team_strength_match | selection=HOME | odds=3.8 | prob=0.3554 | EV=0.3505 | edge=0.0922 | penalty=0.3505 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation

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
