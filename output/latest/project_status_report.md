# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-29T02:33:45.335296+00:00`
GitHub run: `379` attempt `1`
GitHub SHA: `043dbae2db361098f1d2b7b729c71949d24e4a7b`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 54 |  |  |
| odds-api.io forward fixtures | True | 465 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 171 |  |  |
| Forward price coverage report | True | 300 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
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
- Automatic value snapshots: 174
- Positive EV proxy rows: 92
- Proxy observation rows: 25
- Valid forward/proxy log rows: 766
- Deduped forward/proxy log rows: 587
- Duplicate forward/proxy log rows identified: 179
- Fresh API match coverage rate: 0.1933
- Matches with fresh API price: 58
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
Current: 174 value snapshots; fresh API coverage rate 0.1933.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 587 deduped forward/proxy rows; 179 duplicate raw rows identified.
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
Upcoming fixture rows: 604
Fixture team rows unmatched: 1203
Ready for model-fixture join: False
Automatic forward price rows: 58
odds-api.io price rows: 58
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AFC Ann Arbor | suggestion=nan | type=unmatched
- Union FC Macomb | suggestion=nan | type=unmatched
- AA Flamengo SP | suggestion=nan | type=unmatched
- Referencia FC SP | suggestion=nan | type=unmatched
- Aalesunds FK | suggestion=nan | type=unmatched
- HamKam | suggestion=nan | type=unmatched
- Aberdeen LFC | suggestion=nan | type=unmatched
- Queen's Park LFC | suggestion=nan | type=unmatched
- AC Monza | suggestion=nan | type=unmatched
- US Catanzaro | suggestion=nan | type=unmatched
- AE Velo Clube SP | suggestion=nan | type=unmatched
- CA Bandeirante SP | suggestion=nan | type=unmatched
- Al Shabab Kuwait | suggestion=nan | type=unmatched
- AL Tadhamon | suggestion=nan | type=unmatched
- America de Cali Sa | suggestion=nan | type=unmatched
- International FC | suggestion=nan | type=unmatched
- America FC RN | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 58
Value snapshot rows: 174
Matches with any automatic price: 58
Matches with fresh API price: 58
Matches with odds-api.io price: 58
Fresh API match coverage rate: 0.1933
odds-api.io match coverage rate: 0.1933
Real-money ready: False
## Match coverage
- 2026-05-29 | Deportes Temuco vs Santiago Wanderers | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | FC Dila Gori vs FC Samgurali Tskaltubo | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | FK Babrungas Plunge vs FK Minija 2017 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Riga FC vs Grobinas SC/LFS | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | FC Haka Valkeakoski vs JIPPO | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | HJK Helsinki vs VIFK | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | HPS vs Kuopion Palloseura | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Huima/Urho vs GBK Kokkola | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | KaaPo vs LTU | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | Kopa vs Lautp | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | KPV Kokkola vs FC Inter Turku 2 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | FC KTP Kotka vs SJK Akatemia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | NK Mladost Zdralovi vs NK Kustosija Zagreb | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | NK Opatija vs NK Karlovac 1919 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | NK Rudes Zagreb vs NK Sesvete | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | NK Solin vs NK Uskok | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-29 | PK Keski-Uusimaa vs KuPS Akatemia | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 58
Matched prediction rows: 58
Value snapshot rows: 174
odds-api.io snapshot rows: 174
Baseline snapshot rows: 174
Full model snapshot rows: 0
Positive EV rows: 92
Source counts: {'odds_api_io_Bet365_ML': 174}
- 2026-05-29 | HJK Helsinki vs VIFK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3488 | EV=16.7888 | match=1.0
- 2026-05-29 | Harju JK Laagri vs Paide Linnameeskond | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3772 | EV=5.4124 | match=1.0
- 2026-05-29 | SR Donaufeld vs TWL Elektra | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-29 | South Africa vs Nicaragua | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-29 | HJK Helsinki vs VIFK | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.274 | EV=3.658 | match=1.0
- 2026-05-29 | Riga FC vs Grobinas SC/LFS | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-29 | Andorra vs Iraq | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-29 | FK Riteriai vs FK Suduva Marijampole | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-29 | MKS Kluczbork vs KS Sleza Wroclaw | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-29 | FK Garliava vs FA Siauliai B | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-29 | SR Donaufeld vs TWL Elektra | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.274 | EV=1.603 | match=1.0
- 2026-05-29 | Harju JK Laagri vs Paide Linnameeskond | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.274 | EV=1.603 | match=1.0
- 2026-05-29 | NK Opatija vs NK Karlovac 1919 | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-29 | SC Zulimanit vs Tou | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-29 | KPV Kokkola vs FC Inter Turku 2 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-05-29 | Riga FC vs Grobinas SC/LFS | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.274 | EV=1.055 | match=1.0
- 2026-05-29 | FC KTP Kotka vs SJK Akatemia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 174
Pre-dedupe proxy candidate observation rows: 67
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 1
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-29 | FK Babrungas Plunge vs FK Minija 2017 | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-29 | TPV Tampere vs Tampere United | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-29 | Deportes Temuco vs Santiago Wanderers | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-29 | HPS vs Kuopion Palloseura | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-29 | Hoersholm-Usseroed IK vs FA 2000 | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-29 | Aragvi Dusheti vs FC Merani Martvili | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-29 | Kungsangens IF vs IK Franke | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-29 | Nacka FC vs Nykopings BIS | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.8 | prob=0.3772 | EV=0.05616 | edge=0.020057 | penalty=0.05615957753616896 | tier=proxy_watchlist | score=0.2275
- 2026-05-29 | Fehring 1947 vs SV Lebring | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-29 | KFUM Oslo vs Tromsoe IL | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.75 | prob=0.3772 | EV=0.0373 | edge=0.013564 | penalty=0.037301037301037177 | tier=proxy_watchlist | score=0.2253
- 2026-05-29 | Hinna vs Varhaug | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3772 | EV=0.01844 | edge=0.00683 | penalty=0.01844101844101842 | tier=proxy_watchlist | score=0.223
- 2026-05-29 | FK Transinvest vs FC Hegelmann Kaunas | selection=AWAY | source=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1244

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
- watchlist_only_pending_forward_settlement: 3
- edge_below_candidate_threshold: 3
- probability_or_league_rule_suppressed: 1
- low_probability_band_under_0_35: 1
## Row explanations
- 2026-05-29 | FK Babrungas Plunge vs FK Minija 2017 | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | TPV Tampere vs Tampere United | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Deportes Temuco vs Santiago Wanderers | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | HPS vs Kuopion Palloseura | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Hoersholm-Usseroed IK vs FA 2000 | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Aragvi Dusheti vs FC Merani Martvili | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | Kungsangens IF vs IK Franke | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | Nacka FC vs Nykopings BIS | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | Fehring 1947 vs SV Lebring | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | KFUM Oslo vs Tromsoe IL | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | Hinna vs Varhaug | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | FK Transinvest vs FC Hegelmann Kaunas | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 174
Paper proxy observation rows: 25
Positive EV value rows: 92
Suppressed-band observation rows: 0
Distinct matches: 24
Distinct sources: 0
Max EV: 0.7917
Average EV: 0.428869
Max probability edge: 0.166674
Average match confidence: None
## By selection
- away: rows=12, avg_ev=0.4097, max_ev=0.6568
- draw: rows=5, avg_ev=0.4111, max_ev=0.507
- home: rows=8, avg_ev=0.4687, max_ev=0.7917

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 604
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-29 15:00 | Deportes Temuco vs Santiago Wanderers | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:00 | FC Dila Gori vs FC Samgurali Tskaltubo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:00 | FK Babrungas Plunge vs FK Minija 2017 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:00 | Riga FC vs Grobinas SC/LFS | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | FC Haka Valkeakoski vs JIPPO | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | HJK Helsinki vs VIFK | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | HPS vs Kuopion Palloseura | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | Huima/Urho vs GBK Kokkola | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | KaaPo vs LTU | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | Kopa vs Lautp | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | KPV Kokkola vs FC Inter Turku 2 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | FC KTP Kotka vs SJK Akatemia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | NK Mladost Zdralovi vs NK Kustosija Zagreb | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | NK Opatija vs NK Karlovac 1919 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | NK Rudes Zagreb vs NK Sesvete | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | NK Solin vs NK Uskok | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | PK Keski-Uusimaa vs KuPS Akatemia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 15:30 | Pogon Sokol Lubaczow vs Star Starachowice | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 16:00 | Andorra vs Iraq | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 16:00 | Apollon Limassol vs Pafos FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-29 16:00 | Dfk Dainava Alytus vs FK Ekranas | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 4377
Log type: probability_only_no_market_prices
- 2026-05-30 2026-05-29 05:00:00 | Vegalta Sendai vs Ventforet Kofu | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 05:30:00 | Adelaide Cobras vs Adelaide Atletico VSC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 05:30:00 | Adelaide Croatia Raiders SC vs Modbury Jets SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 05:30:00 | Cumberland United vs Salisbury United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 05:30:00 | Monaro Panthers FC vs Canberra White Eagles FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 05:30:00 | South Adelaide FC vs Eastern United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 06:45:00 | Launceston United vs Kingborough Lions United FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Dangjin Citizen vs Yangpyeong FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Ehime FC vs Roasso Kumamoto | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:00:00 | Yanbian Longding vs Changchun Yatai | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:30:00 | Mungyeong Sangmu Wfc vs Hwacheon KSPO FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 07:30:00 | The Cove FC vs Adelaide Blue Eagles | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 08:00:00 | Chuncheon FC vs Gyeongju FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 08:15:00 | FC Viktoria Marianske Lazne vs SK Ujezd Praha 4 | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 09:00:00 | CS. Dong Thap vs DH van Hien | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 09:00:00 | K. Khanh Hoa vs Quang Ninh FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 09:00:00 | Kataller Toyama vs Tegevajaro Miyazaki | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 09:00:00 | PVF Cand B vs Xuan Thien Phu Tho FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 09:00:00 | Quy Nhon Binh Dinh vs Bac Ninh | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-29 09:00:00 | Truong Tuoi Dong Nai FC vs Long An FC | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 604
Manual template rows: 604
Rows with complete manual odds: 0
Rows missing manual odds: 604
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-29 23:00 | AFC Ann Arbor vs Union FC Macomb
- 2026-05-29 18:00 | AA Flamengo SP vs Referencia FC SP
- 2026-05-29 17:00 | Aalesunds FK vs HamKam
- 2026-05-29 18:35 | Aberdeen LFC vs Queen's Park LFC
- 2026-05-29 18:00 | AC Monza vs US Catanzaro
- 2026-05-29 18:00 | AE Velo Clube SP vs CA Bandeirante SP
- 2026-05-29 16:20 | Al Shabab Kuwait vs AL Tadhamon
- 2026-05-29 21:00 | America de Cali Sa vs International FC
- 2026-05-29 22:30 | America FC RN vs Central SC PE
- 2026-05-29 16:00 | Andorra vs Iraq
- 2026-05-29 16:00 | Apollon Limassol vs Pafos FC
- 2026-05-29 17:00 | Aragvi Dusheti vs FC Merani Martvili
- 2026-05-29 20:00 | Asociacion Deportivo Cali vs Asociacion Deportivo Pasto
- 2026-05-29 17:30 | ASV Siegendorf vs ASK Horitschon/U
- 2026-05-29 17:45 | Atletico Andahuaylas vs Club Yanapuma

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 604
Source counts: {'odds_api_io_events_bookmaker_filtered': 598, 'odds_api_io_events_search': 6}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-29 23:00 | AFC Ann Arbor vs Union FC Macomb | usa-usl-league-two | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:00 | AA Flamengo SP vs Referencia FC SP | brazil-u20-paulista | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:00 | Aalesunds FK vs HamKam | norway-eliteserien | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:35 | Aberdeen LFC vs Queen's Park LFC | scotland-premier-league-women | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:00 | AC Monza vs US Catanzaro | italy-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:00 | AE Velo Clube SP vs CA Bandeirante SP | brazil-u20-paulista | odds_api_io_events_bookmaker_filtered
- 2026-05-29 16:20 | Al Shabab Kuwait vs AL Tadhamon | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-29 21:00 | America de Cali Sa vs International FC | colombia-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-29 22:30 | America FC RN vs Central SC PE | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-29 16:00 | Andorra vs Iraq | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-05-29 16:00 | Apollon Limassol vs Pafos FC | cyprus-cyprus-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:00 | Aragvi Dusheti vs FC Merani Martvili | georgia-erovnuli-liga-2 | odds_api_io_events_bookmaker_filtered
- 2026-05-29 20:00 | Asociacion Deportivo Cali vs Asociacion Deportivo Pasto | colombia-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:30 | ASV Siegendorf vs ASK Horitschon/U | austria-amateur-burgenland-burgenlandliga | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:45 | Atletico Andahuaylas vs Club Yanapuma | peru-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-29 20:00 | Atletico Grau vs CD Moquegua | peru-liga-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-29 20:00 | Atletico Nacional SA vs Internacional de Bogota | colombia-liga-femenina | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:00 | Austria Lustenau II vs FC Egg | austria-amateur-vorarlberg-eliteliga | odds_api_io_events_bookmaker_filtered
- 2026-05-29 17:00 | BK Fremad Amager vs Skive IK | denmark-2nd-division | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:30 | Bosnia and Herzegovina vs North Macedonia | international-int-friendly-games | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:00 | Boston City FC MG vs Coimbra Sports MG | brazil-u20-mineiro-1-divisao | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:45 | Bray Wanderers AFC vs Wexford FC | ireland-first-division | odds_api_io_events_bookmaker_filtered
- 2026-05-29 18:00 | Carlos Renaux SC vs Joinville EC SC | brazil-u20-catarinense-serie-a | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 604
Rows with complete odds: 0
- 2026-05-29 23:00 | AFC Ann Arbor vs Union FC Macomb | bookmaker=bet365_manual
- 2026-05-29 18:00 | AA Flamengo SP vs Referencia FC SP | bookmaker=bet365_manual
- 2026-05-29 17:00 | Aalesunds FK vs HamKam | bookmaker=bet365_manual
- 2026-05-29 18:35 | Aberdeen LFC vs Queen's Park LFC | bookmaker=bet365_manual
- 2026-05-29 18:00 | AC Monza vs US Catanzaro | bookmaker=bet365_manual
- 2026-05-29 18:00 | AE Velo Clube SP vs CA Bandeirante SP | bookmaker=bet365_manual
- 2026-05-29 16:20 | Al Shabab Kuwait vs AL Tadhamon | bookmaker=bet365_manual
- 2026-05-29 21:00 | America de Cali Sa vs International FC | bookmaker=bet365_manual
- 2026-05-29 22:30 | America FC RN vs Central SC PE | bookmaker=bet365_manual
- 2026-05-29 16:00 | Andorra vs Iraq | bookmaker=bet365_manual
- 2026-05-29 16:00 | Apollon Limassol vs Pafos FC | bookmaker=bet365_manual
- 2026-05-29 17:00 | Aragvi Dusheti vs FC Merani Martvili | bookmaker=bet365_manual
- 2026-05-29 20:00 | Asociacion Deportivo Cali vs Asociacion Deportivo Pasto | bookmaker=bet365_manual
- 2026-05-29 17:30 | ASV Siegendorf vs ASK Horitschon/U | bookmaker=bet365_manual
- 2026-05-29 17:45 | Atletico Andahuaylas vs Club Yanapuma | bookmaker=bet365_manual
- 2026-05-29 20:00 | Atletico Grau vs CD Moquegua | bookmaker=bet365_manual
- 2026-05-29 20:00 | Atletico Nacional SA vs Internacional de Bogota | bookmaker=bet365_manual
- 2026-05-29 17:00 | Austria Lustenau II vs FC Egg | bookmaker=bet365_manual
- 2026-05-29 17:00 | BK Fremad Amager vs Skive IK | bookmaker=bet365_manual
- 2026-05-29 18:30 | Bosnia and Herzegovina vs North Macedonia | bookmaker=bet365_manual
- 2026-05-29 18:00 | Boston City FC MG vs Coimbra Sports MG | bookmaker=bet365_manual
- 2026-05-29 18:45 | Bray Wanderers AFC vs Wexford FC | bookmaker=bet365_manual
- 2026-05-29 18:00 | Carlos Renaux SC vs Joinville EC SC | bookmaker=bet365_manual
- 2026-05-29 20:30 | Cde Juventud Italiana vs CD Tecnico Universitario | bookmaker=bet365_manual

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
- 2026-05-29 23:00 | AFC Ann Arbor vs Union FC Macomb
- 2026-05-29 18:00 | AA Flamengo SP vs Referencia FC SP
- 2026-05-29 17:00 | Aalesunds FK vs HamKam
- 2026-05-29 18:35 | Aberdeen LFC vs Queen's Park LFC
- 2026-05-29 18:00 | AC Monza vs US Catanzaro
- 2026-05-29 18:00 | AE Velo Clube SP vs CA Bandeirante SP
- 2026-05-29 16:20 | Al Shabab Kuwait vs AL Tadhamon
- 2026-05-29 21:00 | America de Cali Sa vs International FC
- 2026-05-29 22:30 | America FC RN vs Central SC PE
- 2026-05-29 16:00 | Andorra vs Iraq
- 2026-05-29 16:00 | Apollon Limassol vs Pafos FC
- 2026-05-29 17:00 | Aragvi Dusheti vs FC Merani Martvili
- 2026-05-29 20:00 | Asociacion Deportivo Cali vs Asociacion Deportivo Pasto
- 2026-05-29 17:30 | ASV Siegendorf vs ASK Horitschon/U
- 2026-05-29 17:45 | Atletico Andahuaylas vs Club Yanapuma
- 2026-05-29 20:00 | Atletico Grau vs CD Moquegua
- 2026-05-29 20:00 | Atletico Nacional SA vs Internacional de Bogota
- 2026-05-29 17:00 | Austria Lustenau II vs FC Egg
- 2026-05-29 17:00 | BK Fremad Amager vs Skive IK

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 769
Valid forward/proxy log rows: 766
Deduped forward/proxy observation rows: 587
Duplicate forward/proxy log rows: 179
Valid automatic proxy observation rows: 766
Deduped automatic proxy observation rows: 587
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
### Hoenefoss BK vs Stabaek Fotball
- Date/time: 2026-05-29 16:00
- League/phase: norway-toppserien-women / automatic_forward_price_proxy
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
- Prediction ID: 054b0991a859d0d66b81
### Gerasd. Stammersd. vs SV Dinamo Helfort 15
- Date/time: 2026-05-29 16:00
- League/phase: austria-amateur-wien-wiener-stadtliga / automatic_forward_price_proxy
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
Total logged paper-test rows: 769
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 174, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 79, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 769, 'source_used': 'automatic_forward_value_snapshots'}
- Hoenefoss BK vs Stabaek Fotball | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Gerasd. Stammersd. vs SV Dinamo Helfort 15 | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kopa vs Lautp | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SC Red Star Penzing vs WAF Vorwarts Brigittenau | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Dfk Dainava Alytus vs FK Ekranas | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- KaaPo vs LTU | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- NK Rudes Zagreb vs NK Sesvete | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Landvetter IS vs Qviding FIF | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.33 | prob=0.3488 | EV=0.5113 | edge=0.118 | penalty=0.5114 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Transinvest vs FC Hegelmann Kaunas | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- TPV Tampere vs Tampere United | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Babrungas Plunge vs FK Minija 2017 | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SC Zulimanit vs Tou | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Garliava vs FA Siauliai B | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Fredrikstad FK vs IK Start | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Riteriai vs FK Suduva Marijampole | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.25 | prob=0.274 | EV=0.4385 | edge=0.0835 | penalty=0.4385 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Huima/Urho vs GBK Kokkola | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Deportes Temuco vs Santiago Wanderers | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.4 | prob=0.3772 | EV=0.2825 | edge=0.0831 | penalty=0.2825 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PK Keski-Uusimaa vs KuPS Akatemia | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.7 | prob=0.3488 | EV=0.2906 | edge=0.0785 | penalty=0.2906 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
