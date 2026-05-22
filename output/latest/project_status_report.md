# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-21T14:48:58.266091+00:00`
GitHub run: `364` attempt `1`
GitHub SHA: `b85a9c7bd25ce4871c8aadf478a2621263de6eab`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 6 |  |  |
| Football-Data upcoming odds proxy | True | 15 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 38 |  |  |
| odds-api.io forward fixtures | True | 306 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 213 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 5 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 7 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 300 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 192
- Positive EV proxy rows: 87
- Proxy observation rows: 25
- Valid forward/proxy log rows: 474
- Deduped forward/proxy log rows: 340
- Duplicate forward/proxy log rows identified: 134
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
Current: 192 value snapshots; fresh API coverage rate 0.1767.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 340 deduped forward/proxy rows; 134 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 11
Upcoming fixture rows: 0
Proxy price rows: 0
Sources attempted: 1
Errors: 0
No usable proxy odds rows were available from Football-Data fixtures source.

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 551
Fixture team rows unmatched: 1093
Ready for model-fixture join: False
Automatic forward price rows: 53
odds-api.io price rows: 53
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 9 de Octubre FC | suggestion=nan | type=unmatched
- Manta FC | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Atalanta BC | suggestion=Atalanta | type=suggested_alias_needed
- Aarhus Fremad | suggestion=nan | type=unmatched
- Aalborg BK | suggestion=nan | type=unmatched
- AB Gladsaxe | suggestion=nan | type=unmatched
- HIK Hellerup | suggestion=nan | type=unmatched
- AC Omonia Nicosia | suggestion=nan | type=unmatched
- Apollon Limassol | suggestion=nan | type=unmatched
- ADO Den Haag | suggestion=nan | type=unmatched
- PEC Zwolle | suggestion=nan | type=unmatched
- Afturelding | suggestion=nan | type=unmatched
- Throttur Reykjavik | suggestion=nan | type=unmatched
- Ajel de Rufisque | suggestion=nan | type=unmatched
- ASC Linguere | suggestion=nan | type=unmatched
- Al Jazira (UAE) | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 53
Value snapshot rows: 192
Matches with any automatic price: 53
Matches with fresh API price: 53
Matches with odds-api.io price: 53
Fresh API match coverage rate: 0.1767
odds-api.io match coverage rate: 0.1767
Real-money ready: False
## Match coverage
- 2026-05-22 | Auckland FC Reserves vs Eastern Suburbs AFC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-22 | Dalian Yingbo B vs Taian Tiankuang | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Northcote City FC vs Brunswick City SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Arema FC vs Psim Yogyakarta | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | West Adelaide Reserve vs Flinders United Wfc Reserves | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-22 | Salisbury Inter vs Adelaide Comets FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Ho Chi Minh City FC vs Truong Tuoi Dong Nai FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Bentleigh Greens vs Caroline Springs George Cross FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Box Hill United FC vs Springvale White Eagles | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Green Gully SC vs Heidelberg United FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Moreton City Excelsior FC vs Brisbane City FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Dandenong City SC vs ST Albans Saints Dinamo SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Keilor Park SC vs Eastern Lions SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Kingston City FC vs Werribee City FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | FC Altai Oskemen vs FC Okzhetpes | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Fraser Park FC vs Camden Tigers FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-22 | Gornik Zabrze II vs KS Gornik Polkowice | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 53
Matched prediction rows: 61
Value snapshot rows: 192
odds-api.io snapshot rows: 192
Baseline snapshot rows: 192
Full model snapshot rows: 0
Positive EV rows: 87
Source counts: {'odds_api_io_Bet365_ML': 192}
- 2026-05-22 | Maitland FC vs Newcastle Olympic FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3488 | EV=16.7888 | match=1.0
- 2026-05-22 | Maitland FC vs Newcastle Olympic FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.274 | EV=4.754 | match=1.0
- 2026-05-22 | Mindil Aces vs Garuda FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-05-22 | FK Septemvri Sofia vs PFC Dobrudzha Dobrich | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-22 | Preston Lions vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=0.7222
- 2026-05-23 | Green Gully SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-22 | Green Gully SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-22 | Young Africans SC vs Singida Black Stars SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-22 | Ho Chi Minh City FC vs Truong Tuoi Dong Nai FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-22 | Mounties Wanderers FC vs Granville Rage | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-22 | Mindil Aces vs Garuda FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.274 | EV=1.466 | match=1.0
- 2026-05-22 | Zaqatala FK vs Safa | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-22 | The Cong - Viettel FC vs PVF Cong An Nhan Dan FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-22 | FK Spartak 1918 Varna vs FC Lokomotiv 1929 Sofia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-22 | PFC Slavia Sofia vs PFC Montana 1921 | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-22 | Fraser Park FC vs Camden Tigers FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-22 | Mounties Wanderers FC vs Granville Rage | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.274 | EV=0.781 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 192
Pre-dedupe proxy candidate observation rows: 69
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-22 | Dalian Yingbo B vs Taian Tiankuang | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-22 | Ganzhou Ruishi FC vs Shenzhen 2028 FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-22 | Turan Tovuz vs Sabah Masazir | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-22 | Green Gully SC vs Heidelberg United FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-22 | Nepean FC vs South Coast Flame FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-22 | Preston Lions vs Heidelberg United FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-22 | Lanzhou Longyuan Athletic vs Dalian Kewei | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-23 | Green Gully SC vs Heidelberg United FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-22 | Kingston City FC vs Werribee City FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-22 | Hubei Istar vs Chengdu Rongcheng B | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3772 | EV=0.08445 | edge=0.029374 | penalty=0.08445027111256764 | tier=proxy_watchlist | score=0.2308
- 2026-05-22 | Aris Limassol FC vs AEK Larnaca | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-22 | Shahdag Qusar FK vs Baku Sporting | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 4
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False
## Blocker summary
- market_alignment_penalty_too_high_for_real_candidate: 8
- ev_above_real_candidate_cap_possible_overconfidence: 3
- watchlist_only_pending_forward_settlement: 3
- edge_below_candidate_threshold: 1
## Row explanations
- 2026-05-22 | Dalian Yingbo B vs Taian Tiankuang | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Ganzhou Ruishi FC vs Shenzhen 2028 FC | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Turan Tovuz vs Sabah Masazir | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Green Gully SC vs Heidelberg United FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-22 | Nepean FC vs South Coast Flame FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-22 | Preston Lions vs Heidelberg United FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-22 | Lanzhou Longyuan Athletic vs Dalian Kewei | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-23 | Green Gully SC vs Heidelberg United FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-22 | Kingston City FC vs Werribee City FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Hubei Istar vs Chengdu Rongcheng B | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Aris Limassol FC vs AEK Larnaca | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Shahdag Qusar FK vs Baku Sporting | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 192
Paper proxy observation rows: 25
Positive EV value rows: 87
Suppressed-band observation rows: 0
Distinct matches: 23
Distinct sources: 0
Max EV: 0.781
Average EV: 0.473717
Max probability edge: 0.1488
Average match confidence: None
## By selection
- away: rows=12, avg_ev=0.5008, max_ev=0.744
- draw: rows=8, avg_ev=0.4984, max_ev=0.781
- home: rows=5, avg_ev=0.3692, max_ev=0.5088

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 551
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-22 07:00 | Auckland FC Reserves vs Eastern Suburbs AFC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 07:00 | Dalian Yingbo B vs Taian Tiankuang | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 08:15 | Northcote City FC vs Brunswick City SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 08:30 | Arema FC vs Psim Yogyakarta | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 08:30 | West Adelaide Reserve vs Flinders United Wfc Reserves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 08:45 | Salisbury Inter vs Adelaide Comets FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 09:00 | Ho Chi Minh City FC vs Truong Tuoi Dong Nai FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 09:30 | Bentleigh Greens vs Caroline Springs George Cross FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 09:30 | Box Hill United FC vs Springvale White Eagles | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 09:30 | Green Gully SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 09:30 | Moreton City Excelsior FC vs Brisbane City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 09:45 | Dandenong City SC vs ST Albans Saints Dinamo SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 09:45 | Keilor Park SC vs Eastern Lions SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 09:45 | Kingston City FC vs Werribee City FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 10:00 | FC Altai Oskemen vs FC Okzhetpes | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 10:00 | Fraser Park FC vs Camden Tigers FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 10:00 | Gornik Zabrze II vs KS Gornik Polkowice | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 10:00 | Maitland FC vs Newcastle Olympic FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 10:00 | Mounties Wanderers FC vs Granville Rage | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 10:00 | Nepean FC vs South Coast Flame FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-22 10:00 | Zaglebie Lubin II vs Miedz Legnica II | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 2893
Log type: probability_only_no_market_prices
- 2026-05-23 2026-05-22 04:45:00 | North Star vs Logan Lightning | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Avondale FC vs Alamein FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Cockburn City SC Reserves vs Floreat Athena FC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Dandenong City SC vs ST Albans Saints Dinamo SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Essendon Royals SC vs Box Hill United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Gwelup Croatia SC Reserves vs Kingsley Westside FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Joondalup City FC Reserve vs Inglewood United Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Keilor Park SC vs Spring Hills FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Melbourne Victory FC Youth vs FC Bulleen Lions | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Port Melbourne Sharks vs Brunswick Juventus FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:00:00 | Subiaco AFC Reserve vs Curtin University SC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:15:00 | Metrostars Reserve vs Campbelltown City SC Reserves | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 05:45:00 | Brisbane Strikers vs Capalaba FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 06:00:00 | Altona Magic SC vs Hume City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 06:00:00 | Broadbeach United vs Redlands United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 06:15:00 | FC Bulleen Lions vs Manningham United Blues FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 06:30:00 | Rydalmere Lions FC vs Bankstown City FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 07:00:00 | Logan Lightning vs Peninsula Power FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 07:00:00 | Metrostars vs Campbelltown City SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-23 2026-05-22 07:00:00 | Palm Beach SC vs Grange Thistle | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 551
Manual template rows: 551
Rows with complete manual odds: 0
Rows missing manual odds: 551
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-22 20:00 | 9 de Octubre FC vs Manta FC
- 2026-05-22 18:45 | ACF Fiorentina vs Atalanta BC
- 2026-05-22 16:00 | Aarhus Fremad vs Aalborg BK
- 2026-05-22 17:00 | AB Gladsaxe vs HIK Hellerup
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol
- 2026-05-22 18:00 | ADO Den Haag vs PEC Zwolle
- 2026-05-22 19:15 | Afturelding vs Throttur Reykjavik
- 2026-05-22 17:00 | Ajel de Rufisque vs ASC Linguere
- 2026-05-22 15:40 | Al Jazira (UAE) vs Al Ain FC
- 2026-05-22 10:00 | FC Altai Oskemen vs FC Okzhetpes
- 2026-05-22 08:30 | Arema FC vs Psim Yogyakarta
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca
- 2026-05-22 18:30 | Arsenal de Sarandi vs CA Villa San Carlos
- 2026-05-22 16:30 | AS Real Bamako vs FC Diarra
- 2026-05-22 12:00 | FC Astana vs Ulytau FC

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 551
Source counts: {'odds_api_io_events_bookmaker_filtered': 547, 'odds_api_io_events_search': 3, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-22 20:00 | 9 de Octubre FC vs Manta FC | ecuador-copa-ecuador | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:45 | ACF Fiorentina vs Atalanta BC | italy-serie-a | odds_api_io_events_bookmaker_filtered
- 2026-05-22 16:00 | Aarhus Fremad vs Aalborg BK | denmark-1-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 17:00 | AB Gladsaxe vs HIK Hellerup | denmark-2nd-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol | cyprus-1st-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:00 | ADO Den Haag vs PEC Zwolle | netherlands-eredivisie-women | odds_api_io_events_bookmaker_filtered
- 2026-05-22 19:15 | Afturelding vs Throttur Reykjavik | iceland-1-deild | odds_api_io_events_bookmaker_filtered
- 2026-05-22 17:00 | Ajel de Rufisque vs ASC Linguere | senegal-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 15:40 | Al Jazira (UAE) vs Al Ain FC | united-arab-emirates-presidents-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-22 10:00 | FC Altai Oskemen vs FC Okzhetpes | kazakhstan-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-22 08:30 | Arema FC vs Psim Yogyakarta | indonesia-liga-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca | cyprus-1st-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:30 | Arsenal de Sarandi vs CA Villa San Carlos | argentina-primera-b | odds_api_io_events_bookmaker_filtered
- 2026-05-22 16:30 | AS Real Bamako vs FC Diarra | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 12:00 | FC Astana vs Ulytau FC | kazakhstan-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:45 | Athlone Town AFC vs Cork City FC | ireland-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-22 07:00 | Auckland FC Reserves vs Eastern Suburbs AFC | new-zealand-national-league | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:00 | Ayacucho FC vs AD Comerciantes FC | peru-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 18:00 | AZ Alkmaar vs Excelsior Rotterdam | netherlands-eredivisie-women | odds_api_io_events_bookmaker_filtered
- 2026-05-22 15:30 | Azam FC vs Tanzania Prisons | tanzania-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-22 09:30 | Bentleigh Greens vs Caroline Springs George Cross FC | australia-victoria-npl | odds_api_io_events_bookmaker_filtered
- 2026-05-22 09:30 | Box Hill United FC vs Springvale White Eagles | australia-victoria-premier-league-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-22 17:00 | Brabrand IF vs Skive IK | denmark-2nd-division | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 551
Rows with complete odds: 0
- 2026-05-22 20:00 | 9 de Octubre FC vs Manta FC | bookmaker=bet365_manual
- 2026-05-22 18:45 | ACF Fiorentina vs Atalanta BC | bookmaker=bet365_manual
- 2026-05-22 16:00 | Aarhus Fremad vs Aalborg BK | bookmaker=bet365_manual
- 2026-05-22 17:00 | AB Gladsaxe vs HIK Hellerup | bookmaker=bet365_manual
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol | bookmaker=bet365_manual
- 2026-05-22 18:00 | ADO Den Haag vs PEC Zwolle | bookmaker=bet365_manual
- 2026-05-22 19:15 | Afturelding vs Throttur Reykjavik | bookmaker=bet365_manual
- 2026-05-22 17:00 | Ajel de Rufisque vs ASC Linguere | bookmaker=bet365_manual
- 2026-05-22 15:40 | Al Jazira (UAE) vs Al Ain FC | bookmaker=bet365_manual
- 2026-05-22 10:00 | FC Altai Oskemen vs FC Okzhetpes | bookmaker=bet365_manual
- 2026-05-22 08:30 | Arema FC vs Psim Yogyakarta | bookmaker=bet365_manual
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca | bookmaker=bet365_manual
- 2026-05-22 18:30 | Arsenal de Sarandi vs CA Villa San Carlos | bookmaker=bet365_manual
- 2026-05-22 16:30 | AS Real Bamako vs FC Diarra | bookmaker=bet365_manual
- 2026-05-22 12:00 | FC Astana vs Ulytau FC | bookmaker=bet365_manual
- 2026-05-22 18:45 | Athlone Town AFC vs Cork City FC | bookmaker=bet365_manual
- 2026-05-22 07:00 | Auckland FC Reserves vs Eastern Suburbs AFC | bookmaker=bet365_manual
- 2026-05-22 18:00 | Ayacucho FC vs AD Comerciantes FC | bookmaker=bet365_manual
- 2026-05-22 18:00 | AZ Alkmaar vs Excelsior Rotterdam | bookmaker=bet365_manual
- 2026-05-22 15:30 | Azam FC vs Tanzania Prisons | bookmaker=bet365_manual
- 2026-05-22 09:30 | Bentleigh Greens vs Caroline Springs George Cross FC | bookmaker=bet365_manual
- 2026-05-22 09:30 | Box Hill United FC vs Springvale White Eagles | bookmaker=bet365_manual
- 2026-05-22 17:00 | Brabrand IF vs Skive IK | bookmaker=bet365_manual
- 2026-05-22 19:15 | Breidablik Kopavogur vs KR Reykjavik | bookmaker=bet365_manual

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
- 2026-05-22 20:00 | 9 de Octubre FC vs Manta FC
- 2026-05-22 18:45 | ACF Fiorentina vs Atalanta BC
- 2026-05-22 16:00 | Aarhus Fremad vs Aalborg BK
- 2026-05-22 17:00 | AB Gladsaxe vs HIK Hellerup
- 2026-05-22 14:30 | AC Omonia Nicosia vs Apollon Limassol
- 2026-05-22 18:00 | ADO Den Haag vs PEC Zwolle
- 2026-05-22 19:15 | Afturelding vs Throttur Reykjavik
- 2026-05-22 17:00 | Ajel de Rufisque vs ASC Linguere
- 2026-05-22 15:40 | Al Jazira (UAE) vs Al Ain FC
- 2026-05-22 10:00 | FC Altai Oskemen vs FC Okzhetpes
- 2026-05-22 08:30 | Arema FC vs Psim Yogyakarta
- 2026-05-22 14:30 | Aris Limassol FC vs AEK Larnaca
- 2026-05-22 18:30 | Arsenal de Sarandi vs CA Villa San Carlos
- 2026-05-22 16:30 | AS Real Bamako vs FC Diarra
- 2026-05-22 12:00 | FC Astana vs Ulytau FC
- 2026-05-22 18:45 | Athlone Town AFC vs Cork City FC
- 2026-05-22 07:00 | Auckland FC Reserves vs Eastern Suburbs AFC
- 2026-05-22 18:00 | Ayacucho FC vs AD Comerciantes FC
- 2026-05-22 18:00 | AZ Alkmaar vs Excelsior Rotterdam

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 477
Valid forward/proxy log rows: 474
Deduped forward/proxy observation rows: 340
Duplicate forward/proxy log rows: 134
Valid automatic proxy observation rows: 474
Deduped automatic proxy observation rows: 340
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-15 | Brisbane Roar FC vs Lions FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Broadmeadow Magic FC vs Newcastle Olympic FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Semen Padang FC vs Persebaya Surabaya | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-19 | Northeast United FC vs Mohammedan SC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-22 | Fraser Park FC vs Camden Tigers FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0585
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-15 | Cong An TP Ho Chi Minh City FC vs SHB Da Nang | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0577
- 2026-05-19 | Chengdu Rongcheng vs Shanghai Port FC | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
- 2026-05-21 | BFC Daugavpils vs Ogre United | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0568
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
### Kongsvinger IL Toppfotball 2 vs Tromsoe 2
- Date/time: 2026-05-22 14:00
- League/phase: norway-3rd-division-group-5 / automatic_forward_price_proxy
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
- Prediction ID: 5bf00fa136fb193a2bbe
### Mounties Wanderers FC vs Granville Rage
- Date/time: 2026-05-22 10:00
- League/phase: australia-nsw-league-two / automatic_forward_price_proxy
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
Newly logged paper-test picks: 25
Total logged paper-test rows: 477
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 192, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 86, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 477, 'source_used': 'automatic_forward_value_snapshots'}
- Kongsvinger IL Toppfotball 2 vs Tromsoe 2 | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mounties Wanderers FC vs Granville Rage | coverage=baseline_unmatched_fixture | selection=DRAW | odds=6.5 | prob=0.274 | EV=0.781 | edge=0.1202 | penalty=0.781 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Guizhou Guiyang Athletic vs Hangzhou Linping Wuyue | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Astana vs Ulytau FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Pafos FC vs APOEL Nikosia | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.5 | prob=0.3488 | EV=0.5696 | edge=0.1266 | penalty=0.5696 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Eastern United Reserve vs Adelaide Blue Eagles Reserves | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Eastern United vs Adelaide Blue Eagles | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.0 | prob=0.3772 | EV=0.5088 | edge=0.1272 | penalty=0.5088 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Xuan Thien Phu Tho FC vs CS. Dong Thap | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Moreton City Excelsior FC vs Brisbane City FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Moreton City Excelsior U23 vs Brisbane City | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Dewa United vs Bali United | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- West Torrens Birkalla vs Modbury Vista | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Septemvri Sofia vs PFC Dobrudzha Dobrich | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.75 | prob=0.274 | EV=0.5755 | edge=0.1001 | penalty=0.5755 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Northcote City FC vs Brunswick City SC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Dalian Yingbo B vs Taian Tiankuang | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Green Gully SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Preston Lions vs Heidelberg United FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Green Gully SC vs Heidelberg United FC | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
