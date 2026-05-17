# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-16T21:30:00.238669+00:00`
GitHub run: `354` attempt `1`
GitHub SHA: `02c15b3f57629d0be34b6cfd6b8874d924b4c2b8`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 107 |  |  |
| Football-Data upcoming odds proxy | True | 316 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 56 |  |  |
| odds-api.io forward fixtures | True | 659 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 675 |  |  |
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
- Automatic value snapshots: 609
- Positive EV proxy rows: 348
- Proxy observation rows: 25
- Valid forward/proxy log rows: 275
- Deduped forward/proxy log rows: 184
- Duplicate forward/proxy log rows identified: 91
- Fresh API match coverage rate: 0.17
- Matches with fresh API price: 51
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
Current: 609 value snapshots; fresh API coverage rate 0.17.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 184 deduped forward/proxy rows; 91 duplicate raw rows identified.
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
Upcoming fixture rows: 641
Fixture team rows unmatched: 1187
Ready for model-fixture join: False
Automatic forward price rows: 262
odds-api.io price rows: 51
Football-Data price rows: 211
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 07 Vestur Sorvagur | suggestion=nan | type=unmatched
- NSI Runavik | suggestion=nan | type=unmatched
- 1. FC Magdeburg | suggestion=nan | type=unmatched
- 1 FC Kaiserslautern | suggestion=nan | type=unmatched
- 1. FC Slovacko Uherske Hradiste | suggestion=nan | type=unmatched
- FC Slovan Liberec | suggestion=nan | type=unmatched
- 9 de Octubre FC | suggestion=nan | type=unmatched
- CD El Nacional | suggestion=nan | type=unmatched
- ACF Brescia | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Lazio Rome | suggestion=nan | type=unmatched
- FC Abdysh-Ata | suggestion=nan | type=unmatched
- FC Alay | suggestion=nan | type=unmatched
- AC Prato 1908 | suggestion=nan | type=unmatched
- ASD Seravezza Pozzi Calcio | suggestion=nan | type=unmatched
- AC Vigasio | suggestion=nan | type=unmatched
- Obermais | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 262
Value snapshot rows: 609
Matches with any automatic price: 71
Matches with fresh API price: 51
Matches with odds-api.io price: 51
Fresh API match coverage rate: 0.17
odds-api.io match coverage rate: 0.17
Real-money ready: False
## Match coverage
- 2026-05-17 | San Jose Earthquakes vs FC Dallas | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Canberra White Eagles FC vs Canberra Juventus FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Broadmeadow Magic FC vs Edgeworth FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Okayama Yunogo Belle vs Nittaidai FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | V-Varen Nagasaki vs Vissel Kobe | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Canberra Olympic vs Tuggeranong United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Diavorosso Hiroshima vs Yamato Sylphid | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Fukien vs Kwong Wah | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Bulls FC Academy vs Manly United FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-17 | Adelaide Olympic FC Reserve vs Cumberland United Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-17 | Central Coast Mariners Academy vs Hills United FC Brumbies | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-17 | Fagiano Okayama vs Shimizu S-Pulse | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | FC Imabari vs Kamatamare Sanuki | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Iwaki FC vs Matsumoto Yamaga FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | JEF United Chiba vs Kashima Antlers | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Kagoshima United vs Roasso Kumamoto | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-17 | Kataller Toyama vs Tokushima Vortis | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 262
Matched prediction rows: 103
Value snapshot rows: 609
odds-api.io snapshot rows: 156
Baseline snapshot rows: 555
Full model snapshot rows: 54
Positive EV rows: 348
Source counts: {'odds_api_io_Bet365_ML': 156, 'football_data_max_market_proxy': 153, 'football_data_average_market_proxy': 153, 'football_data_bet365_proxy': 147}
- 2026-05-17 | Canberra Olympic vs Tuggeranong United FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3488 | EV=16.7888 | match=1.0
- 2026-05-17 | Maitland FC vs Lake Macquarie City FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3488 | EV=10.8592 | match=1.0
- 2026-05-17 | Canberra Olympic vs Tuggeranong United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.274 | EV=4.754 | match=1.0
- 2026-05-17 | Inter Milano vs Hellas Verona | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.92
- 2026-05-17 | Logan Roos FC vs Redcliffe Dolphins | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=0.8114
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=0.92
- 2026-05-17 | Inter Milano vs Hellas Verona | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.88 | prob=0.3488 | EV=3.492544 | match=0.92
- 2026-05-17 | Inter vs Verona | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.292 | EV=3.38 | match=1.0
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.92
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3217 | EV=3.1821 | match=1.0
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3488 | EV=2.955392 | match=0.92
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3217 | EV=2.8604 | match=1.0
- 2026-05-17 | Perth Redstar FC vs Subiaco AFC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-17 | Wuhan Lianzhen FC vs Guandong GZ-Power FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3772 | EV=2.772 | match=1.0
- 2026-05-17 | Inter vs Verona | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.88 | prob=0.292 | EV=2.76096 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3217 | EV=2.648078 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 609
Pre-dedupe proxy candidate observation rows: 238
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-17 | Kyoto Sanga FC vs Sanfrecce Hiroshima | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-17 | Oita Trinita vs Tegevajaro Miyazaki | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-17 | Samford Rangers vs Taringa Rovers SFC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-17 | Tatung FC vs Taichung Futuro FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-17 | Reilac Shiga FC vs Giravanz Kitakyushu | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-17 | Hwaseong FC vs Busan I Park | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-17 | Taichung Rock FC vs AC Taipei | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-17 | Kochi United SC vs Ehime FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-17 | NGU Loveledge Nagoya vs Shizuoka SSU Bonita | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-17 | Garuda FC vs Palmerston Rovers | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-17 | SV Darmstadt 98 vs SC Paderborn 07 | selection=HOME | source=football_data_max_market_proxy | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2184
- 2026-05-17 | FC Mokpo vs Gyeongju FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5087999999999999 | tier=proxy_watchlist | score=0.2145

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
- market_alignment_penalty_too_high_for_real_candidate: 8
- ev_above_real_candidate_cap_possible_overconfidence: 7
- edge_below_candidate_threshold: 3
- watchlist_only_pending_forward_settlement: 1
- delayed_football_data_proxy_not_fresh_api_price: 1
## Row explanations
- 2026-05-17 | Kyoto Sanga FC vs Sanfrecce Hiroshima | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Oita Trinita vs Tegevajaro Miyazaki | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Samford Rangers vs Taringa Rovers SFC | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Tatung FC vs Taichung Futuro FC | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Reilac Shiga FC vs Giravanz Kitakyushu | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Hwaseong FC vs Busan I Park | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-17 | Taichung Rock FC vs AC Taipei | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-17 | Kochi United SC vs Ehime FC | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-17 | NGU Loveledge Nagoya vs Shizuoka SSU Bonita | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-17 | Garuda FC vs Palmerston Rovers | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-17 | SV Darmstadt 98 vs SC Paderborn 07 | sel=HOME | score=0.2184 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-17 | FC Mokpo vs Gyeongju FC | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 609
Paper proxy observation rows: 25
Positive EV value rows: 348
Suppressed-band observation rows: 0
Distinct matches: 16
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.661943
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=5, avg_ev=0.7589, max_ev=0.7776
- draw: rows=6, avg_ev=0.3976, max_ev=0.5847
- home: rows=14, avg_ev=0.7406, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 641
Forward fixture prediction rows: 300
Full model prediction rows: 6
Baseline prediction rows: 294
Max forward predictions: 300
Ready for price join: True
- 2026-05-17 02:30 | San Jose Earthquakes vs FC Dallas | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 02:45 | Canberra White Eagles FC vs Canberra Juventus FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 03:00 | Broadmeadow Magic FC vs Edgeworth FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 04:00 | Okayama Yunogo Belle vs Nittaidai FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 04:00 | V-Varen Nagasaki vs Vissel Kobe | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 04:30 | Canberra Olympic vs Tuggeranong United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 04:30 | Diavorosso Hiroshima vs Yamato Sylphid | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 04:30 | Fukien vs Kwong Wah | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 04:40 | Bulls FC Academy vs Manly United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 04:45 | Adelaide Olympic FC Reserve vs Cumberland United Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Central Coast Mariners Academy vs Hills United FC Brumbies | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Fagiano Okayama vs Shimizu S-Pulse | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | FC Imabari vs Kamatamare Sanuki | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Iwaki FC vs Matsumoto Yamaga FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | JEF United Chiba vs Kashima Antlers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Kagoshima United vs Roasso Kumamoto | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Kataller Toyama vs Tokushima Vortis | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Kochi United SC vs Ehime FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Logan Roos FC vs Redcliffe Dolphins | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Macarthur Rams vs Northern Tigers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-17 05:00 | Maitland FC vs Lake Macquarie City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 1826
Log type: probability_only_no_market_prices
- 2026-05-17 2026-05-17 14:00:00 | KF Dukagjini vs FC Drita | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | FC Kuressaare vs Nomme Kalju FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Leeds United vs Brighton & Hove Albion | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Livingston vs Kilmarnock | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Lommel SK vs FCV Dender EH | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Mamelodi Sundowns vs AS Far Rabat | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | FC Mendrisio vs USV Eschen-Mauren | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | FC Meyrin vs FC Echallens Region | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Mohun Bagan Super Giant vs SC East Bengal | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | National Bank of Egypt SC vs El Gouna FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | NK Slaven Belupo vs GNK Dinamo Zagreb | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | OFI Crete vs Volos NPS | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | FC Rodange 91 vs FC Mamer 32 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Sabah Masazir vs Neftchi Baku PFC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Santos FC SP vs Coritiba FC PR | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | SC Bettembourg vs FC Etzella Ettelbruck | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Scafatese Calcio 1922 vs Barletta Calcio | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | SCD Ligorna 1922 vs Varese FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Skala IF vs B36 Torshavn | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-17 2026-05-17 14:00:00 | Skiljebo SK vs Kungsangens IF | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 641
Manual template rows: 641
Rows with complete manual odds: 0
Rows missing manual odds: 641
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
- 2026-05-17 12:00 | 1. FC Slovacko Uherske Hradiste vs FC Slovan Liberec
- 2026-05-17 20:30 | 9 de Octubre FC vs CD El Nacional
- 2026-05-17 13:00 | ACF Brescia vs Bologna FC
- 2026-05-17 16:00 | ACF Fiorentina vs Lazio Rome
- 2026-05-17 14:30 | FC Abdysh-Ata vs FC Alay
- 2026-05-17 14:00 | AC Prato 1908 vs ASD Seravezza Pozzi Calcio
- 2026-05-17 14:00 | AC Vigasio vs Obermais
- 2026-05-17 16:00 | AD Cantolao vs Carlos Mannucci
- 2026-05-17 07:00 | Adelaide Olympic FC vs Cumberland United
- 2026-05-17 04:45 | Adelaide Olympic FC Reserve vs Cumberland United Reserve
- 2026-05-17 17:30 | AEK vs Olympiakos
- 2026-05-17 16:30 | AEK Athens vs Olympiacos Piraeus
- 2026-05-17 17:00 | Af Elbasani vs KF Egnatia Rrogozhine

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 641
Source counts: {'odds_api_io_events_bookmaker_filtered': 565, 'football_data_fixtures_proxy': 71, 'odds_api_io_events_search': 5}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-17 16:15 | 07 Vestur Sorvagur vs NSI Runavik | faroe-islands-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 13:30 | 1. FC Magdeburg vs 1 FC Kaiserslautern | germany-2-bundesliga | odds_api_io_events_bookmaker_filtered
- 2026-05-17 12:00 | 1. FC Slovacko Uherske Hradiste vs FC Slovan Liberec | czechia-1-liga-women | odds_api_io_events_bookmaker_filtered
- 2026-05-17 20:30 | 9 de Octubre FC vs CD El Nacional | ecuador-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-17 13:00 | ACF Brescia vs Bologna FC | italy-serie-b-women | odds_api_io_events_bookmaker_filtered
- 2026-05-17 16:00 | ACF Fiorentina vs Lazio Rome | italy-serie-a-women | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:30 | FC Abdysh-Ata vs FC Alay | kyrgyzstan-top-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:00 | AC Prato 1908 vs ASD Seravezza Pozzi Calcio | italy-serie-d-group-e | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:00 | AC Vigasio vs Obermais | italy-serie-d-group-c | odds_api_io_events_bookmaker_filtered
- 2026-05-17 16:00 | AD Cantolao vs Carlos Mannucci | peru-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-17 07:00 | Adelaide Olympic FC vs Cumberland United | australia-south-australia-state-league-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-17 04:45 | Adelaide Olympic FC Reserve vs Cumberland United Reserve | australia-south-australia-state-league-1-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-17 17:30 | AEK vs Olympiakos | G1 | football_data_fixtures_proxy
- 2026-05-17 16:30 | AEK Athens vs Olympiacos Piraeus | greece-super-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 17:00 | Af Elbasani vs KF Egnatia Rrogozhine | albania-kategoria-superiore | odds_api_io_events_bookmaker_filtered
- 2026-05-17 16:00 | AGF Aarhus vs Viborg FF | denmark-superliga | odds_api_io_events_bookmaker_filtered
- 2026-05-17 17:00 | Aguilas FC vs Utebo FC | spain-segunda-federacion | odds_api_io_events_bookmaker_filtered
- 2026-05-17 13:00 | AIK DFF vs Piteaa IF DFF | sweden-damallsvenskan | odds_api_io_events_bookmaker_filtered
- 2026-05-17 13:00 | AJ Auxerre vs OGC Nice | france-seconde-ligue-women | odds_api_io_events_bookmaker_filtered
- 2026-05-17 13:00 | FC Aktobe vs FK Atyrau | kazakhstan-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:10 | AL Bataeh vs Shabab AL Ahli Dubai Club | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 14:10 | AL Wahda FC vs AL Dhafra U23 | united-arab-emirates-u23-pro-league | odds_api_io_events_bookmaker_filtered
- 2026-05-17 18:00 | Al-Shabab FC (SA) vs Al-Ittihad Club | saudi-arabia-saudi-pro-league | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 641
Rows with complete odds: 0
- 2026-05-17 16:15 | 07 Vestur Sorvagur vs NSI Runavik | bookmaker=bet365_manual
- 2026-05-17 13:30 | 1. FC Magdeburg vs 1 FC Kaiserslautern | bookmaker=bet365_manual
- 2026-05-17 12:00 | 1. FC Slovacko Uherske Hradiste vs FC Slovan Liberec | bookmaker=bet365_manual
- 2026-05-17 20:30 | 9 de Octubre FC vs CD El Nacional | bookmaker=bet365_manual
- 2026-05-17 13:00 | ACF Brescia vs Bologna FC | bookmaker=bet365_manual
- 2026-05-17 16:00 | ACF Fiorentina vs Lazio Rome | bookmaker=bet365_manual
- 2026-05-17 14:30 | FC Abdysh-Ata vs FC Alay | bookmaker=bet365_manual
- 2026-05-17 14:00 | AC Prato 1908 vs ASD Seravezza Pozzi Calcio | bookmaker=bet365_manual
- 2026-05-17 14:00 | AC Vigasio vs Obermais | bookmaker=bet365_manual
- 2026-05-17 16:00 | AD Cantolao vs Carlos Mannucci | bookmaker=bet365_manual
- 2026-05-17 07:00 | Adelaide Olympic FC vs Cumberland United | bookmaker=bet365_manual
- 2026-05-17 04:45 | Adelaide Olympic FC Reserve vs Cumberland United Reserve | bookmaker=bet365_manual
- 2026-05-17 17:30 | AEK vs Olympiakos | bookmaker=bet365_manual
- 2026-05-17 16:30 | AEK Athens vs Olympiacos Piraeus | bookmaker=bet365_manual
- 2026-05-17 17:00 | Af Elbasani vs KF Egnatia Rrogozhine | bookmaker=bet365_manual
- 2026-05-17 16:00 | AGF Aarhus vs Viborg FF | bookmaker=bet365_manual
- 2026-05-17 17:00 | Aguilas FC vs Utebo FC | bookmaker=bet365_manual
- 2026-05-17 13:00 | AIK DFF vs Piteaa IF DFF | bookmaker=bet365_manual
- 2026-05-17 13:00 | AJ Auxerre vs OGC Nice | bookmaker=bet365_manual
- 2026-05-17 13:00 | FC Aktobe vs FK Atyrau | bookmaker=bet365_manual
- 2026-05-17 14:10 | AL Bataeh vs Shabab AL Ahli Dubai Club | bookmaker=bet365_manual
- 2026-05-17 14:10 | AL Wahda FC vs AL Dhafra U23 | bookmaker=bet365_manual
- 2026-05-17 18:00 | Al-Shabab FC (SA) vs Al-Ittihad Club | bookmaker=bet365_manual
- 2026-05-17 19:00 | Alagoinhas AC BA vs EC Jacuipense BA | bookmaker=bet365_manual

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
- 2026-05-17 12:00 | 1. FC Slovacko Uherske Hradiste vs FC Slovan Liberec
- 2026-05-17 20:30 | 9 de Octubre FC vs CD El Nacional
- 2026-05-17 13:00 | ACF Brescia vs Bologna FC
- 2026-05-17 16:00 | ACF Fiorentina vs Lazio Rome
- 2026-05-17 14:30 | FC Abdysh-Ata vs FC Alay
- 2026-05-17 14:00 | AC Prato 1908 vs ASD Seravezza Pozzi Calcio
- 2026-05-17 14:00 | AC Vigasio vs Obermais
- 2026-05-17 16:00 | AD Cantolao vs Carlos Mannucci
- 2026-05-17 07:00 | Adelaide Olympic FC vs Cumberland United
- 2026-05-17 04:45 | Adelaide Olympic FC Reserve vs Cumberland United Reserve
- 2026-05-17 17:30 | AEK vs Olympiakos
- 2026-05-17 16:30 | AEK Athens vs Olympiacos Piraeus
- 2026-05-17 17:00 | Af Elbasani vs KF Egnatia Rrogozhine
- 2026-05-17 16:00 | AGF Aarhus vs Viborg FF
- 2026-05-17 17:00 | Aguilas FC vs Utebo FC
- 2026-05-17 13:00 | AIK DFF vs Piteaa IF DFF
- 2026-05-17 13:00 | AJ Auxerre vs OGC Nice

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 278
Valid forward/proxy log rows: 275
Deduped forward/proxy observation rows: 184
Duplicate forward/proxy log rows: 91
Valid automatic proxy observation rows: 275
Deduped automatic proxy observation rows: 184
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
Total logged paper-test rows: 278
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 609, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 299, 'current_paper_picks': 25, 'newly_logged_picks': 15, 'total_logged_paper_rows': 278, 'source_used': 'automatic_forward_value_snapshots'}
- Genoa vs Milan | coverage=full_team_strength_match | selection=HOME | odds=4.5 | prob=0.3447 | EV=0.5512 | edge=0.1225 | penalty=0.5512 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.69 | prob=0.2785 | EV=0.5847 | edge=0.1028 | penalty=0.5847 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.28 | prob=0.2806 | EV=0.4816 | edge=0.0912 | penalty=0.4816 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.25 | prob=0.2785 | EV=0.4621 | edge=0.088 | penalty=0.4621 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.0 | prob=0.2806 | EV=0.403 | edge=0.0806 | penalty=0.403 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.5 | prob=0.2857 | EV=0.2857 | edge=0.0635 | penalty=0.2857 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.09 | prob=0.2857 | EV=0.1685 | edge=0.0412 | penalty=0.1685 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Man United vs Nott'm Forest | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.3386 | EV=0.7776 | edge=0.1481 | penalty=0.7777 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Man United vs Nott'm Forest | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.3386 | EV=0.7776 | edge=0.1481 | penalty=0.7777 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Genoa vs Milan | coverage=full_team_strength_match | selection=HOME | odds=4.85 | prob=0.3447 | EV=0.6718 | edge=0.1385 | penalty=0.6718 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Gimhae FC vs Daegu FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Heracles vs Groningen | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Heracles Almelo vs FC Groningen | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- V-Varen Nagasaki vs Vissel Kobe | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PEC Zwolle vs Feyenoord Rotterdam | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Zwolle vs Feyenoord | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ternana vs AC Milan | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.65 | prob=0.3772 | EV=0.754 | edge=0.1621 | penalty=0.754 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Genoa CFC vs AC Milan | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.65 | prob=0.3772 | EV=0.754 | edge=0.1621 | penalty=0.754 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
