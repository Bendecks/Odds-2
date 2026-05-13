# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-13T12:27:30.423930+00:00`
GitHub run: `341` attempt `1`
GitHub SHA: `b8f20aaf158cdc2eb74a6a12241219ca97bc701a`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 17 |  |  |
| Football-Data upcoming odds proxy | True | 51 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 0 |  |  |
| odds-api.io forward fixtures | True | 0 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 162 |  |  |
| Forward price coverage report | True | 18 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 3 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 18 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 300
- Automatic value snapshots: 384
- Positive EV proxy rows: 195
- Proxy observation rows: 25
- Valid forward/proxy log rows: 109
- Deduped forward/proxy log rows: 55
- Duplicate forward/proxy log rows identified: 54
- Fresh API match coverage rate: 0.1733
- Matches with fresh API price: 52
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
Current: 384 value snapshots; fresh API coverage rate 0.1733.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 55 deduped forward/proxy rows; 54 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 26
Upcoming fixture rows: 17
Proxy price rows: 51
Sources attempted: 1
Errors: 0
- 2026-05-13 20:00 | Man City vs Crystal Palace | football_data_bet365_proxy | 1.2/7.5/12.0
- 2026-05-13 20:00 | Man City vs Crystal Palace | football_data_max_market_proxy | 1.22/7.5/15.0
- 2026-05-13 20:00 | Man City vs Crystal Palace | football_data_average_market_proxy | 1.19/7.03/12.75
- 2026-05-13 18:00 | Brest vs Strasbourg | football_data_bet365_proxy | 2.63/3.6/2.5
- 2026-05-13 18:00 | Brest vs Strasbourg | football_data_max_market_proxy | 2.8/3.6/2.5
- 2026-05-13 18:00 | Brest vs Strasbourg | football_data_average_market_proxy | 2.68/3.47/2.42
- 2026-05-13 20:00 | Lens vs Paris SG | football_data_bet365_proxy | 3.4/4.0/1.95
- 2026-05-13 20:00 | Lens vs Paris SG | football_data_max_market_proxy | 3.5/4.0/2.05
- 2026-05-13 20:00 | Lens vs Paris SG | football_data_average_market_proxy | 3.3/3.91/1.95
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_bet365_proxy | 1.57/4.2/5.0
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_max_market_proxy | 1.68/4.2/5.0
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | football_data_average_market_proxy | 1.6/3.89/4.66
- 2026-05-13 15:00 | Volos NFC vs Aris | football_data_bet365_proxy | 4.33/3.2/1.91
- 2026-05-13 15:00 | Volos NFC vs Aris | football_data_max_market_proxy | 4.33/3.6/2.05
- 2026-05-13 15:00 | Volos NFC vs Aris | football_data_average_market_proxy | 3.57/3.29/1.96
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | football_data_bet365_proxy | 1.41/4.2/8.0
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | football_data_max_market_proxy | 1.42/4.5/8.5
- 2026-05-13 17:30 | Olympiakos vs Panathinaikos | football_data_average_market_proxy | 1.38/4.21/7.59
- 2026-05-13 17:30 | PAOK vs AEK | football_data_bet365_proxy | 1.68/3.7/5.0
- 2026-05-13 17:30 | PAOK vs AEK | football_data_max_market_proxy | 1.74/3.8/5.0
- 2026-05-13 17:30 | PAOK vs AEK | football_data_average_market_proxy | 1.69/3.53/4.56
- 2026-05-13 20:00 | Hearts vs Falkirk | football_data_bet365_proxy | 1.41/4.75/6.5
- 2026-05-13 20:00 | Hearts vs Falkirk | football_data_max_market_proxy | 1.44/4.9/7.5

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 466
Fixture team rows unmatched: 900
Ready for model-fixture join: False
Automatic forward price rows: 103
odds-api.io price rows: 52
Football-Data price rows: 51
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- AB Gladsaxe | suggestion=nan | type=unmatched
- FC Roskilde | suggestion=nan | type=unmatched
- AC Goianiense GO | suggestion=nan | type=unmatched
- Botafogo FC SP | suggestion=nan | type=unmatched
- AC Renate | suggestion=nan | type=unmatched
- S.S.D. Casarano Calcio | suggestion=nan | type=unmatched
- Academia Puerto Cabello | suggestion=nan | type=unmatched
- Portuguesa FC | suggestion=nan | type=unmatched
- AD Pasto | suggestion=nan | type=unmatched
- CD Tolima | suggestion=nan | type=unmatched
- AD Taubate SP | suggestion=nan | type=unmatched
- 3B Sport AM | suggestion=nan | type=unmatched
- Afturelding | suggestion=nan | type=unmatched
- UMF Njardvik | suggestion=nan | type=unmatched
- Ahlafors IF | suggestion=nan | type=unmatched
- Herrestads AIF | suggestion=nan | type=unmatched
- Ajel de Rufisque | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 300
Automatic price rows: 103
Value snapshot rows: 384
Matches with any automatic price: 66
Matches with fresh API price: 52
Matches with odds-api.io price: 52
Fresh API match coverage rate: 0.1733
odds-api.io match coverage rate: 0.1733
Real-money ready: False
## Match coverage
- 2026-05-13 | PFC CSKA Sofia vs FC CSKA 1948 | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | Al-Raed Club vs Abha Club | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | BFC Daugavpils vs FC RFS | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | Coquimbo Unido vs Deportes Iquique | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | Deportes Recoleta vs Universidad Catolica | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | Forge FC Hamilton vs FC Supra Du Quebec | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | GKS Belchatow vs Widzew Lodz II | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-13 | GKS Pniowek Pawlowice vs KS Gornik Polkowice | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | Gzs Tluchovia Tluchowo vs Lech II Poznan | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-13 | HIFK vs JaPS | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | Kaisar Kyzylorda vs Tobol Kostanay | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | Korona II Kielce SA vs KS Wisloka Debica | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-13 | KS Ck Troszyn vs Lechia Tomaszow Mazowiecki | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML
- 2026-05-13 | KS Warta Sieradz vs Wisla Plock II | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-13 | Legia Warszawa II vs GKS Wikielec | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-13 | Levadeiakos vs OFI Crete | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-13 | MSK Zilina vs MFK Ruzomberok | any=True | fresh_api=True | odds_api_io=True | rows=1 | sources=odds_api_io_Bet365_ML

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.
Forward prediction rows: 300
Proxy price rows: 103
Matched prediction rows: 76
Value snapshot rows: 384
odds-api.io snapshot rows: 159
Baseline snapshot rows: 321
Full model snapshot rows: 63
Positive EV rows: 195
Source counts: {'odds_api_io_Bet365_ML': 159, 'football_data_bet365_proxy': 75, 'football_data_max_market_proxy': 75, 'football_data_average_market_proxy': 75}
- 2026-05-13 | Deportes Recoleta vs Universidad Catolica | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3772 | EV=11.8248 | match=1.0
- 2026-05-13 | P-Iirot vs Tampereen Ilves | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.3772 | EV=6.9212 | match=1.0
- 2026-05-13 | IFK Mariehamn vs Puistolan Urheilijat | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-13 | Turun Palloseura vs HJS | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.96
- 2026-05-13 | FC Shakhtar Donetsk vs FC Obolon Kyiv | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.2857 | EV=3.2855 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.96
- 2026-05-13 | Deportes Recoleta vs Universidad Catolica | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.2857 | EV=2.642675 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.2857 | EV=2.4284 | match=1.0
- 2026-05-13 | GKS Pniowek Pawlowice vs KS Gornik Polkowice | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-13 | FC Mali Coura vs Djoliba AC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-13 | P-Iirot vs Tampereen Ilves | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.274 | EV=2.014 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 384
Pre-dedupe proxy candidate observation rows: 135
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 0
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-13 | FC Milsami vs FC Zimbru Chisinau | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-13 | MKS Arka Gdynia vs Gornik Zabrze | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.75 | prob=0.3772 | EV=0.4145 | edge=0.110533 | penalty=0.41449823187721013 | tier=proxy_watchlist | score=0.2633
- 2026-05-13 | Swit Nowy Dwor Mazowiecki vs LKS 1926 Lomza | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2616
- 2026-05-13 | Swidniczanka Swidnik vs Pogon Sokol Lubaczow | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | edge=0.099422 | penalty=0.35791891366486883 | tier=proxy_watchlist | score=0.2583
- 2026-05-13 | Bahla Club vs AL Nasr SC (OMA) | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.4 | prob=0.3772 | EV=0.28248 | edge=0.083082 | penalty=0.28247846102584684 | tier=proxy_watchlist | score=0.2513
- 2026-05-13 | KS Polonia Nysa vs KS Lechia Zielona Gora | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | edge=0.07417 | penalty=0.2447612447612446 | tier=proxy_watchlist | score=0.2477
- 2026-05-13 | HIFK vs JaPS | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-13 | Busaiteen vs AL Hala | selection=HOME | source=odds_api_io_Bet365_ML | odds=3.0 | prob=0.3772 | EV=0.1316 | edge=0.043867 | penalty=0.13160113160113163 | tier=proxy_watchlist | score=0.236
- 2026-05-13 | Kaisar Kyzylorda vs Tobol Kostanay | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-13 | KuPS Akatemia vs FC Honka | selection=HOME | source=odds_api_io_Bet365_ML | odds=2.9 | prob=0.3772 | EV=0.09388 | edge=0.032372 | penalty=0.09387868734557503 | tier=proxy_watchlist | score=0.2319
- 2026-05-13 | Volos NFC vs Aris | selection=HOME | source=football_data_average_market_proxy | odds=3.57 | prob=0.3772 | EV=0.346604 | edge=0.097088 | penalty=0.3466042154566742 | tier=proxy_watchlist | score=0.2205
- 2026-05-13 | Racing Club De Lens vs Paris Saint-Germain | selection=HOME | source=football_data_max_market_proxy | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.091486 | penalty=0.3202013202013201 | tier=proxy_watchlist | score=0.2184

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
- delayed_football_data_proxy_not_fresh_api_price: 2
## Row explanations
- 2026-05-13 | FC Milsami vs FC Zimbru Chisinau | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-13 | MKS Arka Gdynia vs Gornik Zabrze | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-13 | Swit Nowy Dwor Mazowiecki vs LKS 1926 Lomza | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-13 | Swidniczanka Swidnik vs Pogon Sokol Lubaczow | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-13 | Bahla Club vs AL Nasr SC (OMA) | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-13 | KS Polonia Nysa vs KS Lechia Zielona Gora | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-13 | HIFK vs JaPS | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-13 | Busaiteen vs AL Hala | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-13 | Kaisar Kyzylorda vs Tobol Kostanay | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-13 | KuPS Akatemia vs FC Honka | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-13 | Volos NFC vs Aris | sel=HOME | score=0.2205 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-13 | Racing Club De Lens vs Paris Saint-Germain | sel=HOME | score=0.2184 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 384
Paper proxy observation rows: 25
Positive EV value rows: 195
Suppressed-band observation rows: 0
Distinct matches: 13
Distinct sources: 0
Max EV: 0.744
Average EV: 0.393751
Max probability edge: 0.149927
Average match confidence: None
## By selection
- away: rows=11, avg_ev=0.5324, max_ev=0.744
- draw: rows=6, avg_ev=0.0082, max_ev=0.0752
- home: rows=8, avg_ev=0.4922, max_ev=0.6597

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 466
Forward fixture prediction rows: 300
Full model prediction rows: 7
Baseline prediction rows: 293
Max forward predictions: 300
Ready for price join: True
- 2026-05-13 14:45 | PFC CSKA Sofia vs FC CSKA 1948 | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 14:50 | Al-Raed Club vs Abha Club | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | BFC Daugavpils vs FC RFS | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Coquimbo Unido vs Deportes Iquique | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Deportes Recoleta vs Universidad Catolica | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Forge FC Hamilton vs FC Supra Du Quebec | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | GKS Belchatow vs Widzew Lodz II | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | GKS Pniowek Pawlowice vs KS Gornik Polkowice | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Gzs Tluchovia Tluchowo vs Lech II Poznan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | HIFK vs JaPS | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Kaisar Kyzylorda vs Tobol Kostanay | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Korona II Kielce SA vs KS Wisloka Debica | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | KS Ck Troszyn vs Lechia Tomaszow Mazowiecki | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | KS Warta Sieradz vs Wisla Plock II | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Legia Warszawa II vs GKS Wikielec | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Levadeiakos vs OFI Crete | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | MSK Zilina vs MFK Ruzomberok | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | FC Ordabasy vs Zhetysu Taldykorgan | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | P-Iirot vs Tampereen Ilves | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Pogon Nowe Skalmierzyce vs Blekitni Stargard | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-13 15:00 | Pogon Szczecin II vs Elana Torun | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 300
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 589
Log type: probability_only_no_market_prices
- 2026-05-14 2026-05-13 13:00:00 | Lillehammer FK vs FK Gjoevik-Lyn | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:00:00 | Lokomotiv Oslo vs FK Union Carl Berner | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:00:00 | Masku vs LTU | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:00:00 | Raelingen vs Brumunddal Fotball | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:00:00 | Red Arrows vs Green Eagles | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:00:00 | Shahrdari Nowshahr vs FC Fard Alborz | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:00:00 | Simal vs Difai Agsu | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:00:00 | Union Saint-Gilloise vs RSC Anderlecht | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:15:00 | Sanat Mes Kerman FC vs Mes Shahr-e Babak | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 13:30:00 | FK Vidar vs Sotra SK | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | Angelholms FF vs Aatvidabergs FF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | HB Torshavn vs Vikingur Gota | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | IF Karlstad Fotbol vs IFK Stocksund | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | IF Vestri vs Grotta | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | KA Akureyri vs KF Aegir | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | Kjp Kouvola vs Lautp | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | Trelleborgs FF vs Jonkopings Sodra IF | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | FC Trollhattan vs Ariana FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:00:00 | VfL Wolfsburg vs Bayern Munich | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-14 2026-05-13 14:05:00 | Dhofar SCSC vs Al Shabab | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 466
Manual template rows: 466
Rows with complete manual odds: 0
Rows missing manual odds: 466
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-13 16:00 | AB Gladsaxe vs FC Roskilde
- 2026-05-13 18:30 | AC Goianiense GO vs Botafogo FC SP
- 2026-05-13 18:00 | AC Renate vs S.S.D. Casarano Calcio
- 2026-05-13 23:30 | Academia Puerto Cabello vs Portuguesa FC
- 2026-05-13 23:00 | AD Pasto vs CD Tolima
- 2026-05-13 18:00 | AD Taubate SP vs 3B Sport AM
- 2026-05-13 19:15 | Afturelding vs UMF Njardvik
- 2026-05-13 17:00 | Ahlafors IF vs Herrestads AIF
- 2026-05-13 17:00 | Ajel de Rufisque vs Guediawaye FC
- 2026-05-13 16:00 | Al Ittihad vs Um Alhassam
- 2026-05-13 17:00 | Al Ittihad Al Sakandary vs Talaea El Gaish
- 2026-05-13 16:10 | Al-Adalah vs Al Jubail
- 2026-05-13 16:10 | Al-Arabi SC (SA) vs AL Jandal
- 2026-05-13 14:50 | Al-Raed Club vs Abha Club
- 2026-05-13 15:05 | Al-Tai vs Jeddah Club

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 466
Source counts: {'odds_api_io_events_bookmaker_filtered': 440, 'football_data_fixtures_proxy': 17, 'odds_api_io_events_search': 8, 'thesportsdb_eventsnextleague': 1}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-13 16:00 | AB Gladsaxe vs FC Roskilde | denmark-2nd-division | odds_api_io_events_bookmaker_filtered
- 2026-05-13 18:30 | AC Goianiense GO vs Botafogo FC SP | brazil-u20-brasileiro-serie-b | odds_api_io_events_bookmaker_filtered
- 2026-05-13 18:00 | AC Renate vs S.S.D. Casarano Calcio | italy-serie-c-promotion-playoffs | odds_api_io_events_bookmaker_filtered
- 2026-05-13 23:30 | Academia Puerto Cabello vs Portuguesa FC | venezuela-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-13 23:00 | AD Pasto vs CD Tolima | colombia-primera-a-apertura | odds_api_io_events_bookmaker_filtered
- 2026-05-13 18:00 | AD Taubate SP vs 3B Sport AM | brazil-copa-do-brasil-women | odds_api_io_events_bookmaker_filtered
- 2026-05-13 19:15 | Afturelding vs UMF Njardvik | iceland-cup | odds_api_io_events_bookmaker_filtered
- 2026-05-13 17:00 | Ahlafors IF vs Herrestads AIF | sweden-division-2-promotion-playoffs | odds_api_io_events_bookmaker_filtered
- 2026-05-13 17:00 | Ajel de Rufisque vs Guediawaye FC | senegal-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-13 16:00 | Al Ittihad vs Um Alhassam | bahrain-2nd-division | odds_api_io_events_bookmaker_filtered
- 2026-05-13 17:00 | Al Ittihad Al Sakandary vs Talaea El Gaish | egypt-premier-league | odds_api_io_events_bookmaker_filtered
- 2026-05-13 16:10 | Al-Adalah vs Al Jubail | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-13 16:10 | Al-Arabi SC (SA) vs AL Jandal | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-13 14:50 | Al-Raed Club vs Abha Club | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-13 15:05 | Al-Tai vs Jeddah Club | saudi-arabia-division-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-13 20:30 | Alaves vs Barcelona | la_liga | football_data_fixtures_proxy
- 2026-05-13 18:45 | Alloa Athletic FC vs Stenhousemuir FC | scotland-championship | odds_api_io_events_bookmaker_filtered
- 2026-05-13 18:00 | Almere City FC vs Willem II Tilburg | netherlands-eredivisie | odds_api_io_events_bookmaker_filtered
- 2026-05-13 18:00 | Argentinos Juniors Reserve vs CA Tigre Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered
- 2026-05-13 17:30 | FC Arlanda vs Karlbergs BK | sweden-ettan-relegation/promotion | odds_api_io_events_bookmaker_filtered
- 2026-05-13 18:00 | Arsenal WFC vs Everton FC | england-amateur-super-league-women | odds_api_io_events_bookmaker_filtered
- 2026-05-13 18:30 | AS Bakaridjan vs AS Korofina | mali-ligue-1 | odds_api_io_events_bookmaker_filtered
- 2026-05-13 18:00 | Atletico Tucuman Reserve vs CA Barracas Central Reserve | argentina-copa-proyeccion-final-reserves | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 466
Rows with complete odds: 0
- 2026-05-13 16:00 | AB Gladsaxe vs FC Roskilde | bookmaker=bet365_manual
- 2026-05-13 18:30 | AC Goianiense GO vs Botafogo FC SP | bookmaker=bet365_manual
- 2026-05-13 18:00 | AC Renate vs S.S.D. Casarano Calcio | bookmaker=bet365_manual
- 2026-05-13 23:30 | Academia Puerto Cabello vs Portuguesa FC | bookmaker=bet365_manual
- 2026-05-13 23:00 | AD Pasto vs CD Tolima | bookmaker=bet365_manual
- 2026-05-13 18:00 | AD Taubate SP vs 3B Sport AM | bookmaker=bet365_manual
- 2026-05-13 19:15 | Afturelding vs UMF Njardvik | bookmaker=bet365_manual
- 2026-05-13 17:00 | Ahlafors IF vs Herrestads AIF | bookmaker=bet365_manual
- 2026-05-13 17:00 | Ajel de Rufisque vs Guediawaye FC | bookmaker=bet365_manual
- 2026-05-13 16:00 | Al Ittihad vs Um Alhassam | bookmaker=bet365_manual
- 2026-05-13 17:00 | Al Ittihad Al Sakandary vs Talaea El Gaish | bookmaker=bet365_manual
- 2026-05-13 16:10 | Al-Adalah vs Al Jubail | bookmaker=bet365_manual
- 2026-05-13 16:10 | Al-Arabi SC (SA) vs AL Jandal | bookmaker=bet365_manual
- 2026-05-13 14:50 | Al-Raed Club vs Abha Club | bookmaker=bet365_manual
- 2026-05-13 15:05 | Al-Tai vs Jeddah Club | bookmaker=bet365_manual
- 2026-05-13 20:30 | Alaves vs Barcelona | bookmaker=bet365_manual
- 2026-05-13 18:45 | Alloa Athletic FC vs Stenhousemuir FC | bookmaker=bet365_manual
- 2026-05-13 18:00 | Almere City FC vs Willem II Tilburg | bookmaker=bet365_manual
- 2026-05-13 18:00 | Argentinos Juniors Reserve vs CA Tigre Reserve | bookmaker=bet365_manual
- 2026-05-13 17:30 | FC Arlanda vs Karlbergs BK | bookmaker=bet365_manual
- 2026-05-13 18:00 | Arsenal WFC vs Everton FC | bookmaker=bet365_manual
- 2026-05-13 18:30 | AS Bakaridjan vs AS Korofina | bookmaker=bet365_manual
- 2026-05-13 18:00 | Atletico Tucuman Reserve vs CA Barracas Central Reserve | bookmaker=bet365_manual
- 2026-05-13 15:00 | BFC Daugavpils vs FC RFS | bookmaker=bet365_manual

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
- 2026-05-13 16:00 | AB Gladsaxe vs FC Roskilde
- 2026-05-13 18:30 | AC Goianiense GO vs Botafogo FC SP
- 2026-05-13 18:00 | AC Renate vs S.S.D. Casarano Calcio
- 2026-05-13 23:30 | Academia Puerto Cabello vs Portuguesa FC
- 2026-05-13 23:00 | AD Pasto vs CD Tolima
- 2026-05-13 18:00 | AD Taubate SP vs 3B Sport AM
- 2026-05-13 19:15 | Afturelding vs UMF Njardvik
- 2026-05-13 17:00 | Ahlafors IF vs Herrestads AIF
- 2026-05-13 17:00 | Ajel de Rufisque vs Guediawaye FC
- 2026-05-13 16:00 | Al Ittihad vs Um Alhassam
- 2026-05-13 17:00 | Al Ittihad Al Sakandary vs Talaea El Gaish
- 2026-05-13 16:10 | Al-Adalah vs Al Jubail
- 2026-05-13 16:10 | Al-Arabi SC (SA) vs AL Jandal
- 2026-05-13 14:50 | Al-Raed Club vs Abha Club
- 2026-05-13 15:05 | Al-Tai vs Jeddah Club
- 2026-05-13 20:30 | Alaves vs Barcelona
- 2026-05-13 18:45 | Alloa Athletic FC vs Stenhousemuir FC
- 2026-05-13 18:00 | Almere City FC vs Willem II Tilburg
- 2026-05-13 18:00 | Argentinos Juniors Reserve vs CA Tigre Reserve

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 112
Valid forward/proxy log rows: 109
Deduped forward/proxy observation rows: 55
Duplicate forward/proxy log rows: 54
Valid automatic proxy observation rows: 109
Deduped automatic proxy observation rows: 55
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-13 | Motherwell vs Celtic | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0712
- 2026-05-13 | Motherwell FC vs Celtic Glasgow | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0712
- 2026-05-13 | PAOK vs AEK | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | Levadeiakos vs OFI Crete | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | PAOK Thessaloniki vs AEK Athens | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | APO Levadiakos FC vs OFI Crete | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | Machida Zelvia vs Tokyo Verdy | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-13 | Vissel Kobe vs Kyoto Sanga FC | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0711
- 2026-05-12 | AL Wasl vs AL Jazira | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0711
- 2026-05-12 | Sportivo Ameliano vs Deportivo Recoleta Reserve | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0711
- 2026-05-12 | AL Ittihad Kalba vs AL Nasr | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.07060000000000001
- 2026-05-12 | El Gouna FC vs Kahrabaa Ismailia | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.07060000000000001
- 2026-05-13 | Volos NFC vs Aris | selection=home | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0698
- 2026-05-12 | URA FC vs Calvary | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0693
- 2026-05-13 | Kultsu FC vs Ips | selection=away | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0692
- 2026-05-12 | Gwangju FC vs FC Seoul | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.0684
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.06810000000000001
- 2026-05-14 | Real Madrid vs Oviedo | selection=draw | phase=automatic_forward_price_proxy | tier=baseline_coverage_observation | score=0.0675
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.067
- 2026-05-12 | AL Faisaly (Jor) vs Ramtha SC | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.067

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
### Getafe vs Mallorca
- Date/time: 2026-05-13 20:30
- League/phase: la_liga / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 3.7
- Fair odds: 3.06
- Model probability: 0.3268
- Probability band: 0.25-0.35
- EV: 0.2092
- Probability edge: 0.0565
- Alignment penalty: 0.2092
- Suppression action: none
- Paper tier: priority_proxy_observation
- Paper score: 0.2564
- Prediction ID: 512b2aaa4dc6a4610a3d
### Villarreal vs Sevilla
- Date/time: 2026-05-13 18:00
- League/phase: la_liga / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 3.7
- Fair odds: 3.07
- Model probability: 0.326
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
Newly logged paper-test picks: 3
Total logged paper-test rows: 112
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 384, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 174, 'current_paper_picks': 25, 'newly_logged_picks': 3, 'total_logged_paper_rows': 112, 'source_used': 'automatic_forward_value_snapshots'}
- Getafe vs Mallorca | coverage=full_team_strength_match | selection=AWAY | odds=3.7 | prob=0.3268 | EV=0.2092 | edge=0.0565 | penalty=0.2092 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Villarreal vs Sevilla | coverage=full_team_strength_match | selection=AWAY | odds=3.7 | prob=0.326 | EV=0.2062 | edge=0.0557 | penalty=0.2062 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Villarreal vs Sevilla | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.326 | EV=0.1736 | edge=0.0482 | penalty=0.1736 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Getafe vs Mallorca | coverage=full_team_strength_match | selection=AWAY | odds=3.51 | prob=0.3268 | EV=0.1471 | edge=0.0419 | penalty=0.1471 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Lens vs Paris SG | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3022 | EV=0.0577 | edge=0.0165 | penalty=0.0577 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Alaves vs Barcelona | coverage=full_team_strength_match | selection=DRAW | odds=3.9 | prob=0.2757 | EV=0.0752 | edge=0.0193 | penalty=0.0752 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Lens vs Paris SG | coverage=full_team_strength_match | selection=HOME | odds=3.4 | prob=0.3022 | EV=0.0275 | edge=0.0081 | penalty=0.0275 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Alaves vs Barcelona | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2757 | EV=0.0339 | edge=0.009 | penalty=0.0339 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brest vs Strasbourg | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2794 | EV=0.0058 | edge=0.0016 | penalty=0.0058 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brest vs Strasbourg | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2794 | EV=0.0058 | edge=0.0016 | penalty=0.0058 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Espanol vs Ath Bilbao | coverage=full_team_strength_match | selection=DRAW | odds=3.3 | prob=0.2922 | EV=-0.0357 | edge=-0.0108 | penalty=0.0357 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=negative_ev_control_observation
- Espanol vs Ath Bilbao | coverage=full_team_strength_match | selection=DRAW | odds=3.3 | prob=0.2922 | EV=-0.0357 | edge=-0.0108 | penalty=0.0357 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=negative_ev_control_observation
- PAOK Thessaloniki vs AEK Athens | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PAOK vs AEK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PAOK vs AEK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Levadeiakos vs OFI Crete | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PAOK Thessaloniki vs AEK Athens | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Levadeiakos vs OFI Crete | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation

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
