# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-27T15:00:58.828849+00:00`
GitHub run: `376` attempt `1`
GitHub SHA: `4ca5963be263919b815ac4f484462dfb1165aae8`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 0 |  |  |
| Football-Data upcoming odds proxy | True | 0 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 30 |  |  |
| odds-api.io forward fixtures | True | 168 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 90 |  |  |
| Forward price coverage report | True | 169 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 2 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 169 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 147
- Positive EV proxy rows: 68
- Proxy observation rows: 25
- Valid forward/proxy log rows: 695
- Deduped forward/proxy log rows: 528
- Duplicate forward/proxy log rows identified: 167
- Fresh API match coverage rate: 0.1633
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
Current: 147 value snapshots; fresh API coverage rate 0.1633.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 528 deduped forward/proxy rows; 167 duplicate raw rows identified.
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
Upcoming fixture rows: 447
Fixture team rows unmatched: 890
Ready for model-fixture join: False
Automatic forward price rows: 49
odds-api.io price rows: 49
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- 1. FC Lokomotive Leipzig | suggestion=nan | type=unmatched
- FC Wurzburger Kickers | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Parma Calcio 1913 U20 | suggestion=nan | type=unmatched
- AL Karkh | suggestion=nan | type=unmatched
- Al Shorta SC | suggestion=nan | type=unmatched
- AL Minaa | suggestion=nan | type=unmatched
- AL Talaba | suggestion=nan | type=unmatched
- AL Naft Maysan | suggestion=nan | type=unmatched
- Al Quwa Al Jawiya | suggestion=nan | type=unmatched
- Al-Fahaheel | suggestion=nan | type=unmatched
- Al-Salmiya SC | suggestion=nan | type=unmatched
- Assyriska FF | suggestion=nan | type=unmatched
- Vasalunds IF | suggestion=nan | type=unmatched
- Atletico Mineiro MG | suggestion=nan | type=unmatched
- EC Vitoria BA | suggestion=nan | type=unmatched
- Auckland FC Reserves | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 49
Value snapshot rows: 147
Matches with any automatic price: 49
Matches with fresh API price: 49
Matches with odds-api.io price: 49
Fresh API match coverage rate: 0.1633
odds-api.io match coverage rate: 0.1633
Real-money ready: False
## Match coverage
- 2026-05-28 | Stars FC vs AMSG FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Auckland FC Reserves vs Auckland United FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-28 | Birkenhead United AFC vs East Coast Bays | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Melville United AFC vs Tauranga City AFC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FC Okzhetpes vs FC Aktobe | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FC Kyzylzhar SK vs Zhetysu Taldykorgan | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Sri Lanka vs Bhutan | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FK Atyrau vs Tobol Kostanay | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FK Kukesi vs Butrinti Sarande | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FK Septemvri Sofia vs FC Yantra Gabrovo | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Ismaily SC vs Pharco FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Kaisar Kyzylorda vs FC Yelimai | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Petrojet FC vs El Gouna FC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Talaea El Gaish vs Wadi Degla SC | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | FC Zhenis vs FC Kaspiy Aktau | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Gabala FK vs Energetik Mingechevir | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-28 | Ilbirs Bishkek FC vs FC Abdysh-Ata | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 49
Matched prediction rows: 49
Value snapshot rows: 147
odds-api.io snapshot rows: 147
Baseline snapshot rows: 147
Full model snapshot rows: 0
Positive EV rows: 68
Source counts: {'odds_api_io_Bet365_ML': 147}
- 2026-05-28 | Cruzeiro EC MG vs Doce Mel EC BA | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3488 | EV=10.8592 | match=1.0
- 2026-05-28 | Sri Lanka vs Bhutan | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3772 | EV=3.9036 | match=1.0
- 2026-05-28 | Cruzeiro EC MG vs Doce Mel EC BA | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.274 | EV=3.658 | match=1.0
- 2026-05-28 | Llaneros FC vs Independiente Santa Fe | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-28 | FK Kukesi vs Butrinti Sarande | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-28 | Sri Lanka vs Bhutan | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.274 | EV=1.74 | match=1.0
- 2026-05-28 | Atletico Mineiro MG vs EC Vitoria BA | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-28 | Gabala FK vs Energetik Mingechevir | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-28 | FK Septemvri Sofia vs FC Yantra Gabrovo | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-28 | FC Torpedo Kutaisi vs FC Gagra | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-28 | Birkenhead United AFC vs East Coast Bays | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-28 | FCM Traiskirchen vs SC Neusiedl am See 1919 | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-28 | Ireland vs Qatar | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3488 | EV=0.6568 | match=1.0
- 2026-05-28 | Kolding IF vs Dbk Fortuna Hjoerring | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.2 | prob=0.3772 | EV=0.58424 | match=1.0
- 2026-05-28 | FC Ylivieska vs Lapuan Virkia | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.274 | EV=0.507 | match=1.0
- 2026-05-28 | Kultsu FC vs Kjp Kouvola | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.2 | prob=0.3488 | EV=0.46496 | match=1.0
- 2026-05-28 | Mikkelin Pallo-Kissat vs HaPK Edustus | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.1 | prob=0.3488 | EV=0.43008 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 147
Pre-dedupe proxy candidate observation rows: 55
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-28 | CA Piauiense PI vs Santos FC SP | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-28 | AL Karkh vs Al Shorta SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-28 | Puskas Akademia Felcsut vs Ferencvarosi Budapest | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2549
- 2026-05-28 | FK Atyrau vs Tobol Kostanay | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-28 | Ilbirs Bishkek FC vs FC Abdysh-Ata | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-28 | AL Naft Maysan vs Al Quwa Al Jawiya | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.069508 | penalty=0.22590122590122585 | tier=proxy_watchlist | score=0.2458
- 2026-05-28 | Al-Fahaheel vs Al-Salmiya SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3772 | EV=0.16932 | edge=0.054619 | penalty=0.16931871374941476 | tier=proxy_watchlist | score=0.24
- 2026-05-28 | Stars FC vs AMSG FC | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-28 | Kaisar Kyzylorda vs FC Yelimai | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-28 | Chrobry Glogow vs LKS Lodz | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-28 | FC Jazz vs SalPa | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-28 | Zakho FC vs Erbil SC | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319

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
- market_alignment_penalty_too_high_for_real_candidate: 7
- ev_above_real_candidate_cap_possible_overconfidence: 6
- watchlist_only_pending_forward_settlement: 5
## Row explanations
- 2026-05-28 | CA Piauiense PI vs Santos FC SP | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | AL Karkh vs Al Shorta SC | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | Puskas Akademia Felcsut vs Ferencvarosi Budapest | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | FK Atyrau vs Tobol Kostanay | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | Ilbirs Bishkek FC vs FC Abdysh-Ata | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | AL Naft Maysan vs Al Quwa Al Jawiya | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-28 | Al-Fahaheel vs Al-Salmiya SC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-28 | Stars FC vs AMSG FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-28 | Kaisar Kyzylorda vs FC Yelimai | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-28 | Chrobry Glogow vs LKS Lodz | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-28 | FC Jazz vs SalPa | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-28 | Zakho FC vs Erbil SC | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 147
Paper proxy observation rows: 25
Positive EV value rows: 68
Suppressed-band observation rows: 0
Distinct matches: 22
Distinct sources: 0
Max EV: 0.6568
Average EV: 0.340673
Max probability edge: 0.139105
Average match confidence: None
## By selection
- away: rows=11, avg_ev=0.3492, max_ev=0.6568
- draw: rows=6, avg_ev=0.3586, max_ev=0.507
- home: rows=8, avg_ev=0.3155, max_ev=0.5842

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 447
Forward fixture prediction rows: 300
Full model prediction rows: 0
Baseline prediction rows: 300
Max forward predictions: 300
Ready for price join: True
- 2026-05-28 02:30 | Stars FC vs AMSG FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 07:00 | Auckland FC Reserves vs Auckland United FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 07:00 | Birkenhead United AFC vs East Coast Bays | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 07:00 | Melville United AFC vs Tauranga City AFC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 10:00 | FC Okzhetpes vs FC Aktobe | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 11:00 | FC Kyzylzhar SK vs Zhetysu Taldykorgan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 11:00 | Sri Lanka vs Bhutan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 13:00 | FK Atyrau vs Tobol Kostanay | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 13:00 | FK Kukesi vs Butrinti Sarande | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 14:00 | FK Septemvri Sofia vs FC Yantra Gabrovo | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 14:00 | Ismaily SC vs Pharco FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 14:00 | Kaisar Kyzylorda vs FC Yelimai | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 14:00 | Petrojet FC vs El Gouna FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 14:00 | Talaea El Gaish vs Wadi Degla SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 14:00 | FC Zhenis vs FC Kaspiy Aktau | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 14:30 | Gabala FK vs Energetik Mingechevir | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 14:30 | Ilbirs Bishkek FC vs FC Abdysh-Ata | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 15:00 | AL Karkh vs Al Shorta SC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 15:00 | AL Minaa vs AL Talaba | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 15:00 | AL Naft Maysan vs Al Quwa Al Jawiya | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-28 15:00 | FC Ordabasy vs FC Kairat Almaty | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 4162
Log type: probability_only_no_market_prices
- 2026-05-30 2026-05-28 14:00:00 | FC Trollhattan vs Aatvidabergs FF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 14:00:00 | Tvaakers IF vs Kristianstad FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 14:15:00 | AD Ceuta vs Albacete Balompie | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 14:15:00 | Real Sociedad San Sebastian B vs Cultural Leonesa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 15:00:00 | Osters IF vs Norrby IF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 15:30:00 | Central Ballester vs CSDC Espanol | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 16:00:00 | Uruguay Montevideo FC vs Plaza Colonia | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 17:30:00 | CA Claypole vs CA Central Cordoba Rosario | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 17:30:00 | CA Lugano vs Deportivo Paraguayo | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 17:30:00 | Club Comunicaciones vs CD Armenio | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 17:30:00 | Club El Porvenir vs Deportivo Muniz | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 17:30:00 | CS Dock Sud vs CA Brown de Adrogue | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 17:30:00 | Kansas City NWSL vs Boston Legacy FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 18:00:00 | Bentin Tacna Heroica vs CD Estudiantil Cni | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 18:00:00 | Danubio FC vs CA Progreso | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 18:00:00 | River Light FC vs Minnesota Aurora | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 18:30:00 | Argentino de Rosario vs Club Estrella Del Sur (Alejandro Korn) | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 18:30:00 | CA Puerto Nuevo vs Club Mercedes | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 18:30:00 | Club Lujan vs Leones de Rosario FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-30 2026-05-28 18:30:00 | Real Pilar FC vs CD UAI Urquiza | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 447
Manual template rows: 447
Rows with complete manual odds: 0
Rows missing manual odds: 447
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
- 2026-05-28 15:00 | AL Karkh vs Al Shorta SC
- 2026-05-28 15:00 | AL Minaa vs AL Talaba
- 2026-05-28 15:00 | AL Naft Maysan vs Al Quwa Al Jawiya
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA
- 2026-05-28 07:00 | Auckland FC Reserves vs Auckland United FC
- 2026-05-28 07:00 | Birkenhead United AFC vs East Coast Bays
- 2026-05-28 18:00 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve
- 2026-05-28 18:00 | CA Lanus vs CA Platense
- 2026-05-28 19:00 | CA Piauiense PI vs Santos FC SP
- 2026-05-28 22:00 | CA River Plate (Arg) vs San Lorenzo de Almagro Res.
- 2026-05-28 18:00 | CA Sarmiento de Junin vs Rosario Central Reserve

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 447
Source counts: {'odds_api_io_events_bookmaker_filtered': 444, 'odds_api_io_events_search': 3}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-28 17:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | germany-amateur-regionalliga-playoffs | odds_api_io_events_bookmaker_filtered
- 2026-05-28 18:30 | ACF Fiorentina vs Parma Calcio 1913 U20 | italy-primavera-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-28 15:00 | AL Karkh vs Al Shorta SC | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-28 15:00 | AL Minaa vs AL Talaba | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-28 15:00 | AL Naft Maysan vs Al Quwa Al Jawiya | iraq-iraqi-league | odds_api_io_events_bookmaker_filtered
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC | kuwait-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF | sweden-svenska-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-28 07:00 | Auckland FC Reserves vs Auckland United FC | new-zealand-national-league | odds_api_io_events_bookmaker_filtered
- 2026-05-28 07:00 | Birkenhead United AFC vs East Coast Bays | new-zealand-national-league | odds_api_io_events_bookmaker_filtered
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
- 2026-05-28 15:30 | Chrobry Glogow vs LKS Lodz | poland-i-liga | odds_api_io_events_bookmaker_filtered
- 2026-05-28 21:00 | CR Vasco da Gama RJ vs America FC MG | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-28 21:30 | Cruzeiro EC MG vs Doce Mel EC BA | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 447
Rows with complete odds: 0
- 2026-05-28 17:00 | 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | bookmaker=bet365_manual
- 2026-05-28 18:30 | ACF Fiorentina vs Parma Calcio 1913 U20 | bookmaker=bet365_manual
- 2026-05-28 15:00 | AL Karkh vs Al Shorta SC | bookmaker=bet365_manual
- 2026-05-28 15:00 | AL Minaa vs AL Talaba | bookmaker=bet365_manual
- 2026-05-28 15:00 | AL Naft Maysan vs Al Quwa Al Jawiya | bookmaker=bet365_manual
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC | bookmaker=bet365_manual
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF | bookmaker=bet365_manual
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA | bookmaker=bet365_manual
- 2026-05-28 07:00 | Auckland FC Reserves vs Auckland United FC | bookmaker=bet365_manual
- 2026-05-28 07:00 | Birkenhead United AFC vs East Coast Bays | bookmaker=bet365_manual
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
- 2026-05-28 15:30 | Chrobry Glogow vs LKS Lodz | bookmaker=bet365_manual
- 2026-05-28 21:00 | CR Vasco da Gama RJ vs America FC MG | bookmaker=bet365_manual
- 2026-05-28 21:30 | Cruzeiro EC MG vs Doce Mel EC BA | bookmaker=bet365_manual
- 2026-05-28 16:00 | Deportivo Maldonado Reserve vs Liverpool Montevideo | bookmaker=bet365_manual

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
- 2026-05-28 15:00 | AL Karkh vs Al Shorta SC
- 2026-05-28 15:00 | AL Minaa vs AL Talaba
- 2026-05-28 15:00 | AL Naft Maysan vs Al Quwa Al Jawiya
- 2026-05-28 16:20 | Al-Fahaheel vs Al-Salmiya SC
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA
- 2026-05-28 07:00 | Auckland FC Reserves vs Auckland United FC
- 2026-05-28 07:00 | Birkenhead United AFC vs East Coast Bays
- 2026-05-28 18:00 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve
- 2026-05-28 18:00 | CA Lanus vs CA Platense
- 2026-05-28 19:00 | CA Piauiense PI vs Santos FC SP
- 2026-05-28 22:00 | CA River Plate (Arg) vs San Lorenzo de Almagro Res.
- 2026-05-28 18:00 | CA Sarmiento de Junin vs Rosario Central Reserve
- 2026-05-28 18:00 | CA Union Santa Fe Reserve vs Gimnasia de Mendoza Reserve
- 2026-05-28 19:00 | Casa Pia Lisbon vs SCU Torreense
- 2026-05-28 23:00 | CD El Nacional vs CD Universidad Catolica del Ecuador
- 2026-05-28 20:00 | CD Real Santander vs Once Caldas Sa

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 698
Valid forward/proxy log rows: 695
Deduped forward/proxy observation rows: 528
Duplicate forward/proxy log rows: 167
Valid automatic proxy observation rows: 695
Deduped automatic proxy observation rows: 528
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
### Ireland vs Qatar
- Date/time: 2026-05-28 18:45
- League/phase: international-int-friendly-games / automatic_forward_price_proxy
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
- Prediction ID: 7ee8b67ba999202f1249
### Kolding IF vs Dbk Fortuna Hjoerring
- Date/time: 2026-05-28 17:00
- League/phase: denmark-kvindeligaen-women / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 4.2
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
Total logged paper-test rows: 698
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 147, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 61, 'current_paper_picks': 25, 'newly_logged_picks': 25, 'total_logged_paper_rows': 698, 'source_used': 'automatic_forward_value_snapshots'}
- Ireland vs Qatar | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kolding IF vs Dbk Fortuna Hjoerring | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.2 | prob=0.3772 | EV=0.5842 | edge=0.1391 | penalty=0.5842 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kultsu FC vs Kjp Kouvola | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.2 | prob=0.3488 | EV=0.465 | edge=0.1107 | penalty=0.465 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CA Piauiense PI vs Santos FC SP | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.7 | prob=0.3772 | EV=0.3956 | edge=0.1069 | penalty=0.3956 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Mikkelin Pallo-Kissat vs HaPK Edustus | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- CR Vasco da Gama RJ vs America FC MG | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AL Karkh vs Al Shorta SC | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.6 | prob=0.3772 | EV=0.3579 | edge=0.0994 | penalty=0.3579 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Ylivieska vs Lapuan Virkia | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.5 | prob=0.274 | EV=0.507 | edge=0.0922 | penalty=0.507 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Zhenis vs FC Kaspiy Aktau | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.9 | prob=0.3488 | EV=0.3603 | edge=0.0924 | penalty=0.3603 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Puskas Akademia Felcsut vs Ferencvarosi Budapest | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Kyzylzhar SK vs Zhetysu Taldykorgan | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.0821 | penalty=0.308 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- 1. FC Lokomotive Leipzig vs FC Wurzburger Kickers | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.0821 | penalty=0.308 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FK Atyrau vs Tobol Kostanay | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.3 | prob=0.3772 | EV=0.2448 | edge=0.0742 | penalty=0.2448 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Birkenhead United AFC vs East Coast Bays | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FCM Traiskirchen vs SC Neusiedl am See 1919 | coverage=baseline_unmatched_fixture | selection=DRAW | odds=5.0 | prob=0.274 | EV=0.37 | edge=0.074 | penalty=0.37 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- FC Ylivieska vs Lapuan Virkia | coverage=baseline_unmatched_fixture | selection=AWAY | odds=3.6 | prob=0.3488 | EV=0.2557 | edge=0.071 | penalty=0.2557 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- AL Naft Maysan vs Al Quwa Al Jawiya | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.0695 | penalty=0.2259 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ilbirs Bishkek FC vs FC Abdysh-Ata | coverage=baseline_unmatched_fixture | selection=HOME | odds=3.25 | prob=0.3772 | EV=0.2259 | edge=0.0695 | penalty=0.2259 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
