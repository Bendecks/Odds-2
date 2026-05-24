# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-23T02:16:35.186306+00:00`
GitHub run: `367` attempt `1`
GitHub SHA: `4a8c7ba599995d3fc09d7c1f7c4c03a5ea678b17`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 46 |  |  |
| Football-Data upcoming odds proxy | True | 135 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 29 |  |  |
| odds-api.io forward fixtures | True | 891 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 99 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 4 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 300 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 552
- Positive EV proxy rows: 306
- Proxy observation rows: 25
- Valid forward/proxy log rows: 549
- Deduped forward/proxy log rows: 401
- Duplicate forward/proxy log rows identified: 148
- Fresh API match coverage rate: 0.1767
- Matches with fresh API price: 53
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
Current: 552 value snapshots; fresh API coverage rate 0.1767.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 401 deduped forward/proxy rows; 148 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 47
Upcoming fixture rows: 32
Proxy price rows: 93
Sources attempted: 1
Errors: 0
- 2026-05-24 17:30 | Club Brugge vs Gent | football_data_max_market_proxy | 1.78/4.33/3.8
- 2026-05-24 17:30 | Club Brugge vs Gent | football_data_average_market_proxy | 1.72/4.15/3.67
- 2026-05-24 17:30 | St Truiden vs Mechelen | football_data_max_market_proxy | 1.88/4.1/3.65
- 2026-05-24 17:30 | St Truiden vs Mechelen | football_data_average_market_proxy | 1.82/3.85/3.53
- 2026-05-24 17:30 | St. Gilloise vs Anderlecht | football_data_max_market_proxy | 1.5/4.33/6.66
- 2026-05-24 17:30 | St. Gilloise vs Anderlecht | football_data_average_market_proxy | 1.44/4.2/6.26
- 2026-05-24 16:00 | Brighton vs Man United | football_data_bet365_proxy | 1.85/4.2/3.6
- 2026-05-24 16:00 | Brighton vs Man United | football_data_max_market_proxy | 1.92/4.2/3.75
- 2026-05-24 16:00 | Brighton vs Man United | football_data_average_market_proxy | 1.86/3.98/3.58
- 2026-05-24 16:00 | Burnley vs Wolves | football_data_bet365_proxy | 2.35/3.5/2.9
- 2026-05-24 16:00 | Burnley vs Wolves | football_data_max_market_proxy | 2.48/3.6/2.9
- 2026-05-24 16:00 | Burnley vs Wolves | football_data_average_market_proxy | 2.36/3.5/2.77
- 2026-05-24 16:00 | Crystal Palace vs Arsenal | football_data_bet365_proxy | 4.2/4.0/1.75
- 2026-05-24 16:00 | Crystal Palace vs Arsenal | football_data_max_market_proxy | 4.33/4.2/1.82
- 2026-05-24 16:00 | Crystal Palace vs Arsenal | football_data_average_market_proxy | 4.13/3.86/1.76
- 2026-05-24 16:00 | Fulham vs Newcastle | football_data_bet365_proxy | 2.88/3.8/2.25
- 2026-05-24 16:00 | Fulham vs Newcastle | football_data_max_market_proxy | 2.9/3.8/2.37
- 2026-05-24 16:00 | Fulham vs Newcastle | football_data_average_market_proxy | 2.82/3.66/2.27
- 2026-05-24 16:00 | Liverpool vs Brentford | football_data_bet365_proxy | 1.8/4.2/3.8
- 2026-05-24 16:00 | Liverpool vs Brentford | football_data_max_market_proxy | 1.84/4.35/4.0
- 2026-05-24 16:00 | Liverpool vs Brentford | football_data_average_market_proxy | 1.8/4.09/3.73
- 2026-05-24 16:00 | Man City vs Aston Villa | football_data_bet365_proxy | 1.29/6.0/9.0
- 2026-05-24 16:00 | Man City vs Aston Villa | football_data_max_market_proxy | 1.31/6.25/9.5

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 492
Fixture team rows unmatched: 931
Ready for model-fixture join: False
Automatic forward price rows: 146
odds-api.io price rows: 53
Football-Data price rows: 93
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. FC Slovacko B | suggestion=nan | type=unmatched
- SK Polanka Nad Odrou | suggestion=nan | type=unmatched
- AFC Eskilstuna | suggestion=nan | type=unmatched
- Vasalunds IF | suggestion=nan | type=unmatched
- AFC Hermannstadt | suggestion=nan | type=unmatched
- SC FC Voluntari | suggestion=nan | type=unmatched
- AA Internacional Limeira SP | suggestion=nan | type=unmatched
- AO Itabaiana SE | suggestion=nan | type=unmatched
- Aatvidabergs FF | suggestion=nan | type=unmatched
- Laholms FK | suggestion=nan | type=unmatched
- ABC FC RN | suggestion=nan | type=unmatched
- America FC RN | suggestion=nan | type=unmatched
- AC Goianiense GO | suggestion=nan | type=unmatched
- Sao Bernardo FC | suggestion=nan | type=unmatched
- AC Milan | suggestion=nan | type=unmatched
- Cagliari Calcio | suggestion=nan | type=unmatched
- Acao Futebol MT | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 146
Value snapshot rows: 552
Matches with any automatic price: 78
Matches with fresh API price: 53
Matches with odds-api.io price: 53
Fresh API match coverage rate: 0.1767
odds-api.io match coverage rate: 0.1767
Real-money ready: False
## Match coverage
- 2026-05-24 | Bigfoot FC vs West Seattle Junction FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Blacktown City FC vs Sydney Olympic FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Cooks Hill United vs Belmont Swansea United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Island Bay United vs Petone FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Kahibah FC Reserve vs Adamstown Rosebud FC Reserve | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-24 | Orca Kamogawa FC vs Viamaterasu Miyazaki | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Wollongong Wolves FC vs St George FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-24 | Fagiano Okayama vs Cerezo Osaka | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Brisbane Roar FC vs Eastern Suburbs FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Kingborough Lions United FC vs Launceston City | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | NHK Spring Yokohama FC Seagulls vs AS Harima Albion | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Vanraure Hachinohe FC vs Tochigi SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | West Canberra Wanderers FC vs Tuggeranong United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Launceston City FC vs Devonport City SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Robina City vs Caboolture FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Belconnen United vs Canberra Olympic | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-24 | Blaublitz Akita vs Tochigi City FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 146
Matched prediction rows: 100
Value snapshot rows: 552
odds-api.io snapshot rows: 165
Baseline snapshot rows: 444
Full model snapshot rows: 108
Positive EV rows: 306
Source counts: {'odds_api_io_Bet365_ML': 165, 'football_data_max_market_proxy': 135, 'football_data_average_market_proxy': 135, 'football_data_bet365_proxy': 117}
- 2026-05-24 | Belconnen United vs Canberra Olympic | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3488 | EV=9.1152 | match=1.0
- 2026-05-24 | Uwa Nedlands FC vs Fremantle City FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=23.0 | prob=0.3772 | EV=7.6756 | match=1.0
- 2026-05-24 | FC Slovan Liberec vs Slavia Prague | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-24 | North Lakes United vs Mitchelton FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-24 | Manchester City vs Aston Villa | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=0.96
- 2026-05-24 | Gold Coast United FC vs Eastern Suburbs FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-24 | Manchester City vs Aston Villa | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-24 | Belconnen United vs Canberra Olympic | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.274 | EV=2.014 | match=1.0
- 2026-05-24 | Uwa Nedlands FC vs Fremantle City FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.274 | EV=2.014 | match=1.0
- 2026-05-24 | Manchester City vs Aston Villa | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.39 | prob=0.3488 | EV=1.926432 | match=0.96
- 2026-05-24 | SSC Napoli vs Udinese Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.92
- 2026-05-24 | SSC Napoli vs Udinese Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.92
- 2026-05-24 | Man City vs Aston Villa | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.29 | EV=1.755 | match=1.0
- 2026-05-24 | Subiaco AFC vs Perth Azzurri | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-24 | UD Las Palmas vs Real Zaragoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=0.92
- 2026-05-24 | Las Palmas vs Zaragoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-24 | Man City vs Aston Villa | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.29 | EV=1.61 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 552
Pre-dedupe proxy candidate observation rows: 244
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-24 | Giravanz Kitakyushu vs Kagoshima United | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-24 | Hellenic Athletic Club vs Port Darwin FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-24 | Western City Rangers FC vs Macarthur Rams | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.8 | prob=0.3772 | EV=0.43336 | edge=0.114042 | penalty=0.4333594266562293 | tier=proxy_watchlist | score=0.2649
- 2026-05-24 | Kamatamare Sanuki vs FC Osaka | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-24 | Launceston City FC vs Devonport City SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-24 | Montedio Yamagata vs Shonan Bellmare | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.2 | prob=0.3772 | EV=0.20704 | edge=0.0647 | penalty=0.2070399999999999 | tier=proxy_watchlist | score=0.2439
- 2026-05-24 | Preston Lions FC vs Oakleigh Cannons | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-24 | Yongin City FC vs Chungnam Asan FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-24 | Kahibah FC Reserve vs Adamstown Rosebud FC Reserve | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-24 | Orca Kamogawa FC vs Viamaterasu Miyazaki | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-24 | Kahibah FC vs Adamstown Rosebud FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-24 | Mito Hollyhock vs Kawasaki Frontale | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 3
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 8
- ev_above_real_candidate_cap_possible_overconfidence: 6
- watchlist_only_pending_forward_settlement: 4
## Row explanations
- 2026-05-24 | Giravanz Kitakyushu vs Kagoshima United | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-24 | Hellenic Athletic Club vs Port Darwin FC | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-24 | Western City Rangers FC vs Macarthur Rams | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-24 | Kamatamare Sanuki vs FC Osaka | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-24 | Launceston City FC vs Devonport City SC | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-24 | Montedio Yamagata vs Shonan Bellmare | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-24 | Preston Lions FC vs Oakleigh Cannons | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-24 | Yongin City FC vs Chungnam Asan FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-24 | Kahibah FC Reserve vs Adamstown Rosebud FC Reserve | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-24 | Orca Kamogawa FC vs Viamaterasu Miyazaki | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-24 | Kahibah FC vs Adamstown Rosebud FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-24 | Mito Hollyhock vs Kawasaki Frontale | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 552
Paper proxy observation rows: 25
Positive EV value rows: 306
Suppressed-band observation rows: 0
Distinct matches: 13
Distinct sources: 0
Max EV: 0.744
Average EV: 0.263045
Max probability edge: 0.1488
Average match confidence: None
## By selection
- away: rows=13, avg_ev=0.2795, max_ev=0.744
- draw: rows=6, avg_ev=0.2865, max_ev=0.6687
- home: rows=6, avg_ev=0.2039, max_ev=0.2994

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 492
Forward fixture prediction rows: 300
Full model prediction rows: 12
Baseline prediction rows: 288
Max forward predictions: 300
Ready for price join: True
- 2026-05-24 02:50 | Bigfoot FC vs West Seattle Junction FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 03:00 | Blacktown City FC vs Sydney Olympic FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 03:00 | Cooks Hill United vs Belmont Swansea United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 03:00 | Island Bay United vs Petone FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 03:00 | Kahibah FC Reserve vs Adamstown Rosebud FC Reserve | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 03:00 | Orca Kamogawa FC vs Viamaterasu Miyazaki | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 03:00 | Wollongong Wolves FC vs St George FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 03:55 | Fagiano Okayama vs Cerezo Osaka | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 04:00 | Brisbane Roar FC vs Eastern Suburbs FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 04:00 | Kingborough Lions United FC vs Launceston City | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 04:00 | NHK Spring Yokohama FC Seagulls vs AS Harima Albion | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 04:00 | Vanraure Hachinohe FC vs Tochigi SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 04:00 | West Canberra Wanderers FC vs Tuggeranong United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 04:30 | Launceston City FC vs Devonport City SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 04:30 | Robina City vs Caboolture FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 05:00 | Belconnen United vs Canberra Olympic | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 05:00 | Blaublitz Akita vs Tochigi City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 05:00 | Boroondara Eagles vs Melbourne City Youth | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 05:00 | Canberra Croatia FC vs Monaro Panthers FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 05:00 | Central Coast Mariners Academy vs Prospect United | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-24 05:00 | Gainare Tottori vs Oita Trinita | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 3422
Log type: probability_only_no_market_prices
- 2026-05-24 2026-05-24 17:25:00 | Al-Nasr SC vs Kuwait SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Cadiz vs Leganes | H=0.3592 D=0.2873 A=0.35350000000000004
- 2026-05-24 2026-05-24 17:30:00 | Club Brugge vs Gent | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Coastal Union FC vs Mashujaa FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Cultural Leonesa vs Burgos | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Eibar vs Cordoba | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | FK IMT Novi Beograd vs FK TSC Backa Topola | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | FK Mladost Lucani vs FK Napredak Krusevac | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | FK Radnicki 1923 Kragujevac vs FK Javor Ivanjica | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | FK Radnicki Nis vs FK Spartak Subotica | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Fotbal Club FCSB vs FC Botosani | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Garcia Agreda vs Chapaquito Nacional Senac | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Huesca vs Castellon | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Las Palmas vs Zaragoza | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Malaga vs Santander | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Mirandes vs Granada | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Olimpia Grudziadz vs KS Hutnik Krakow SSA | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | Sp Gijon vs Almeria | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | St. Gilloise vs Anderlecht | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-24 2026-05-24 17:30:00 | St Truiden vs Mechelen | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 492
Manual template rows: 492
Rows with complete manual odds: 0
Rows missing manual odds: 492
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-24 08:15 | 1. FC Slovacko B vs SK Polanka Nad Odrou
- 2026-05-24 14:00 | AFC Eskilstuna vs Vasalunds IF
- 2026-05-24 14:30 | AFC Hermannstadt vs SC FC Voluntari
- 2026-05-24 19:30 | AA Internacional Limeira SP vs AO Itabaiana SE
- 2026-05-24 14:00 | Aatvidabergs FF vs Laholms FK
- 2026-05-24 19:00 | ABC FC RN vs America FC RN
- 2026-05-24 19:00 | AC Goianiense GO vs Sao Bernardo FC
- 2026-05-24 18:45 | AC Milan vs Cagliari Calcio
- 2026-05-24 19:00 | Acao Futebol MT vs Itabirito FC MG
- 2026-05-24 18:30 | AD Berazategui vs Argentino de Rosario
- 2026-05-24 21:00 | AD Confianca SE vs Figueirense FC SC
- 2026-05-24 17:00 | Adr Jicaral vs Inter San Carlos
- 2026-05-24 12:00 | AE Uberabinha MG vs Inter de Minas MG
- 2026-05-24 17:00 | Af Elbasani vs FC Dinamo City
- 2026-05-24 16:30 | Afrique Football Elite vs Binga FC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 492
Source counts: {'odds_api_io_events_bookmaker_filtered': 457, 'football_data_fixtures_proxy': 32, 'odds_api_io_events_search': 2, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-24 08:15 | 1. FC Slovacko B vs SK Polanka Nad Odrou | czechia-msfl | odds_api_io_events_bookmaker_filtered
- 2026-05-24 14:00 | AFC Eskilstuna vs Vasalunds IF | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-24 14:30 | AFC Hermannstadt vs SC FC Voluntari | romania-superliga | odds_api_io_events_bookmaker_filtered
- 2026-05-24 19:30 | AA Internacional Limeira SP vs AO Itabaiana SE | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-24 14:00 | Aatvidabergs FF vs Laholms FK | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-24 19:00 | ABC FC RN vs America FC RN | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-24 19:00 | AC Goianiense GO vs Sao Bernardo FC | brazil-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-24 18:45 | AC Milan vs Cagliari Calcio | italy-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-05-24 19:00 | Acao Futebol MT vs Itabirito FC MG | brazil-brasileiro-serie-a2-women | odds_api_io_events_bookmaker_filtered
- 2026-05-24 18:30 | AD Berazategui vs Argentino de Rosario | argentina-primera-c | odds_api_io_events_bookmaker_filtered
- 2026-05-24 21:00 | AD Confianca SE vs Figueirense FC SC | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-24 17:00 | Adr Jicaral vs Inter San Carlos | costa-rica-liga-de-ascenso-clausura | odds_api_io_events_bookmaker_filtered
- 2026-05-24 12:00 | AE Uberabinha MG vs Inter de Minas MG | brazil-u20-mineiro-1-divisao | odds_api_io_events_bookmaker_filtered
- 2026-05-24 17:00 | Af Elbasani vs FC Dinamo City | albania-kategoria-superiore | odds_api_io_events_bookmaker_filtered
- 2026-05-24 16:30 | Afrique Football Elite vs Binga FC | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-24 10:00 | Aguilas FC vs UD Poblense | spain-segunda-federacion | odds_api_io_events_bookmaker_filtered
- 2026-05-24 10:15 | Ajax Amsterdam vs FC Utrecht | netherlands-eredivisie | odds_api_io_events_bookmaker_filtered
- 2026-05-24 17:25 | Al-Nasr SC vs Kuwait SC | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-24 15:15 | Albacete vs Sociedad B | SP2 | football_data_fixtures_proxy
- 2026-05-24 14:15 | Albacete Balompie vs Real Sociedad San Sebastian B | spain-laliga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-24 10:30 | Albacete Basket vs AB Castello | spain-segunda-feb | odds_api_io_events_search
- 2026-05-24 20:30 | Alianza Atletico vs FC Cajamarca | peru-liga-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-24 19:30 | Amazonas FC AM vs Ferroviaria Araraquara SP | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 492
Rows with complete odds: 0
- 2026-05-24 08:15 | 1. FC Slovacko B vs SK Polanka Nad Odrou | bookmaker=bet365_manual
- 2026-05-24 14:00 | AFC Eskilstuna vs Vasalunds IF | bookmaker=bet365_manual
- 2026-05-24 14:30 | AFC Hermannstadt vs SC FC Voluntari | bookmaker=bet365_manual
- 2026-05-24 19:30 | AA Internacional Limeira SP vs AO Itabaiana SE | bookmaker=bet365_manual
- 2026-05-24 14:00 | Aatvidabergs FF vs Laholms FK | bookmaker=bet365_manual
- 2026-05-24 19:00 | ABC FC RN vs America FC RN | bookmaker=bet365_manual
- 2026-05-24 19:00 | AC Goianiense GO vs Sao Bernardo FC | bookmaker=bet365_manual
- 2026-05-24 18:45 | AC Milan vs Cagliari Calcio | bookmaker=bet365_manual
- 2026-05-24 19:00 | Acao Futebol MT vs Itabirito FC MG | bookmaker=bet365_manual
- 2026-05-24 18:30 | AD Berazategui vs Argentino de Rosario | bookmaker=bet365_manual
- 2026-05-24 21:00 | AD Confianca SE vs Figueirense FC SC | bookmaker=bet365_manual
- 2026-05-24 17:00 | Adr Jicaral vs Inter San Carlos | bookmaker=bet365_manual
- 2026-05-24 12:00 | AE Uberabinha MG vs Inter de Minas MG | bookmaker=bet365_manual
- 2026-05-24 17:00 | Af Elbasani vs FC Dinamo City | bookmaker=bet365_manual
- 2026-05-24 16:30 | Afrique Football Elite vs Binga FC | bookmaker=bet365_manual
- 2026-05-24 10:00 | Aguilas FC vs UD Poblense | bookmaker=bet365_manual
- 2026-05-24 10:15 | Ajax Amsterdam vs FC Utrecht | bookmaker=bet365_manual
- 2026-05-24 17:25 | Al-Nasr SC vs Kuwait SC | bookmaker=bet365_manual
- 2026-05-24 15:15 | Albacete vs Sociedad B | bookmaker=bet365_manual
- 2026-05-24 14:15 | Albacete Balompie vs Real Sociedad San Sebastian B | bookmaker=bet365_manual
- 2026-05-24 10:30 | Albacete Basket vs AB Castello | bookmaker=bet365_manual
- 2026-05-24 20:30 | Alianza Atletico vs FC Cajamarca | bookmaker=bet365_manual
- 2026-05-24 19:30 | Amazonas FC AM vs Ferroviaria Araraquara SP | bookmaker=bet365_manual
- 2026-05-24 13:00 | America FC MG vs Itabirito FC MG | bookmaker=bet365_manual

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
- 2026-05-24 08:15 | 1. FC Slovacko B vs SK Polanka Nad Odrou
- 2026-05-24 14:00 | AFC Eskilstuna vs Vasalunds IF
- 2026-05-24 14:30 | AFC Hermannstadt vs SC FC Voluntari
- 2026-05-24 19:30 | AA Internacional Limeira SP vs AO Itabaiana SE
- 2026-05-24 14:00 | Aatvidabergs FF vs Laholms FK
- 2026-05-24 19:00 | ABC FC RN vs America FC RN
- 2026-05-24 19:00 | AC Goianiense GO vs Sao Bernardo FC
- 2026-05-24 18:45 | AC Milan vs Cagliari Calcio
- 2026-05-24 19:00 | Acao Futebol MT vs Itabirito FC MG
- 2026-05-24 18:30 | AD Berazategui vs Argentino de Rosario
- 2026-05-24 21:00 | AD Confianca SE vs Figueirense FC SC
- 2026-05-24 17:00 | Adr Jicaral vs Inter San Carlos
- 2026-05-24 12:00 | AE Uberabinha MG vs Inter de Minas MG
- 2026-05-24 17:00 | Af Elbasani vs FC Dinamo City
- 2026-05-24 16:30 | Afrique Football Elite vs Binga FC
- 2026-05-24 10:00 | Aguilas FC vs UD Poblense
- 2026-05-24 10:15 | Ajax Amsterdam vs FC Utrecht
- 2026-05-24 17:25 | Al-Nasr SC vs Kuwait SC
- 2026-05-24 15:15 | Albacete vs Sociedad B

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 552
Valid forward/proxy log rows: 549
Deduped forward/proxy observation rows: 401
Duplicate forward/proxy log rows: 148
Valid automatic proxy observation rows: 549
Deduped automatic proxy observation rows: 401
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-23 | Vonds Ichihara FC vs Shizuoka SSU Bonita | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-15 | Cong An TP Ho Chi Minh City FC vs SHB Da Nang | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-21 | BFC Daugavpils vs Ogre United | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-23 | Canberra Olympic vs Belconnen United | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-19 | Derby Academie vs Onze Createurs | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Al Kahrabaa SC vs Al-Gharraf SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Diyala FC vs Amanat Baghdad SC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0567
- 2026-05-19 | Deportivo Capiata vs Club Fernando de La Mora | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.056100000000000004
- 2026-05-23 | Clarence Zebras FC vs Kingborough Lions United FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0557
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
### Man City vs Aston Villa
- Date/time: 2026-05-24 16:00
- League/phase: premier_league / automatic_forward_price_proxy
- Selection: DRAW
- Market odds: 5.93
- Fair odds: 3.75
- Model probability: 0.267
- Probability band: 0.25-0.35
- EV: 0.5833
- Probability edge: 0.0984
- Alignment penalty: 0.5833
- Suppression action: none
- Paper tier: volume_observation
- Paper score: 0.2864
- Prediction ID: d5c8e7e735aaae5b83e3
### Liverpool vs Brentford
- Date/time: 2026-05-24 16:00
- League/phase: premier_league / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.0
- Fair odds: 2.95
- Model probability: 0.3393
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
Total logged paper-test rows: 552
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 552, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 279, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 552, 'source_used': 'automatic_forward_value_snapshots'}
- Man City vs Aston Villa | coverage=full_team_strength_match | selection=DRAW | odds=5.93 | prob=0.267 | EV=0.5833 | edge=0.0984 | penalty=0.5833 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Liverpool vs Brentford | coverage=full_team_strength_match | selection=AWAY | odds=4.0 | prob=0.3393 | EV=0.3572 | edge=0.0893 | penalty=0.3572 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Tottenham vs Everton | coverage=full_team_strength_match | selection=AWAY | odds=4.3 | prob=0.3577 | EV=0.5381 | edge=0.1251 | penalty=0.5381 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=volume_observation
- Liverpool vs Brentford | coverage=full_team_strength_match | selection=AWAY | odds=3.8 | prob=0.3393 | EV=0.2893 | edge=0.0761 | penalty=0.2893 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Crystal Palace vs Arsenal | coverage=full_team_strength_match | selection=HOME | odds=4.33 | prob=0.3001 | EV=0.2994 | edge=0.0692 | penalty=0.2994 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brighton vs Man United | coverage=full_team_strength_match | selection=AWAY | odds=3.75 | prob=0.3301 | EV=0.2379 | edge=0.0634 | penalty=0.2379 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- West Ham vs Leeds | coverage=full_team_strength_match | selection=AWAY | odds=4.0 | prob=0.312 | EV=0.248 | edge=0.062 | penalty=0.248 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Crystal Palace vs Arsenal | coverage=full_team_strength_match | selection=HOME | odds=4.2 | prob=0.3001 | EV=0.2604 | edge=0.062 | penalty=0.2604 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Tottenham vs Everton | coverage=full_team_strength_match | selection=AWAY | odds=3.8 | prob=0.3577 | EV=0.3593 | edge=0.0945 | penalty=0.3593 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Napoli vs Udinese | coverage=full_team_strength_match | selection=DRAW | odds=4.33 | prob=0.2872 | EV=0.2436 | edge=0.0563 | penalty=0.2436 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brighton vs Man United | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3301 | EV=0.1884 | edge=0.0523 | penalty=0.1884 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- West Ham vs Leeds | coverage=full_team_strength_match | selection=AWAY | odds=3.75 | prob=0.312 | EV=0.17 | edge=0.0453 | penalty=0.17 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Napoli vs Udinese | coverage=full_team_strength_match | selection=DRAW | odds=4.07 | prob=0.2872 | EV=0.1689 | edge=0.0415 | penalty=0.1689 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Nott'm Forest vs Bournemouth | coverage=full_team_strength_match | selection=HOME | odds=3.3 | prob=0.3675 | EV=0.2127 | edge=0.0645 | penalty=0.2128 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Nott'm Forest vs Bournemouth | coverage=full_team_strength_match | selection=HOME | odds=3.3 | prob=0.3675 | EV=0.2127 | edge=0.0645 | penalty=0.2128 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Parma vs Sassuolo | coverage=full_team_strength_match | selection=HOME | odds=2.7 | prob=0.4145 | EV=0.1192 | edge=0.0441 | penalty=0.1192 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Parma vs Sassuolo | coverage=full_team_strength_match | selection=HOME | odds=2.7 | prob=0.4145 | EV=0.1192 | edge=0.0441 | penalty=0.1192 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Burnley vs Wolves | coverage=full_team_strength_match | selection=AWAY | odds=2.9 | prob=0.3891 | EV=0.1284 | edge=0.0443 | penalty=0.1284 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation

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
