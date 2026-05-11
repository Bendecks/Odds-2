# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-11T21:42:28.411829+00:00`
GitHub run: `303` attempt `1`
GitHub SHA: `65e221a84a21f7ad16bd056a44177e6344c5c51e`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 11 |  |  |
| Football-Data upcoming odds proxy | True | 33 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 1 |  |  |
| odds-api.io forward fixtures | True | 142 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 99 |  |  |
| Forward price coverage report | True | 80 |  |  |
| Forward price coverage summary | True | 1 |  |  |
| Forward price source summary | True | 4 |  |  |
| Proxy candidate observations | True | 12 |  |  |
| Proxy candidate observation summary | True | 1 |  |  |
| Proxy candidate explanation report | True | 12 |  |  |
| Proxy candidate explanation summary | True | 1 |  |  |
| Proxy candidate blocker summary | True | 6 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 80 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 80
- Automatic value snapshots: 99
- Positive EV proxy rows: 49
- Proxy observation rows: 7
- Valid forward/proxy log rows: 20
- Deduped forward/proxy log rows: 7
- Duplicate forward/proxy log rows identified: 13
- Fresh API match coverage rate: 0.0
- Matches with fresh API price: 0
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
Current: 99 value snapshots; fresh API coverage rate 0.0.
Done when: Keep Football-Data as baseline; improve odds-api.io/API-Football coverage carefully.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 deduped proxy observations across several matchdays.
Current: 7 deduped forward/proxy rows; 13 duplicate raw rows identified.
Done when: Minimum 50 deduped observations before drawing early conclusions; 100+ preferred.

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 135
Upcoming fixture rows: 11
Proxy price rows: 33
Sources attempted: 1
Errors: 0
- 2026-05-11 20:00 | Tottenham vs Leeds | football_data_bet365_proxy | 1.83/4.1/3.75
- 2026-05-11 20:00 | Tottenham vs Leeds | football_data_max_market_proxy | 1.86/4.1/4.1
- 2026-05-11 20:00 | Tottenham vs Leeds | football_data_average_market_proxy | 1.82/3.82/3.92
- 2026-05-11 19:45 | Napoli vs Bologna | football_data_bet365_proxy | 1.53/4.2/6.0
- 2026-05-11 19:45 | Napoli vs Bologna | football_data_max_market_proxy | 1.57/4.2/6.5
- 2026-05-11 19:45 | Napoli vs Bologna | football_data_average_market_proxy | 1.52/4.01/6.06
- 2026-05-11 20:15 | Benfica vs Sp Braga | football_data_bet365_proxy | 1.39/4.33/7.0
- 2026-05-11 20:15 | Benfica vs Sp Braga | football_data_max_market_proxy | 1.44/4.8/7.5
- 2026-05-11 20:15 | Benfica vs Sp Braga | football_data_average_market_proxy | 1.4/4.45/6.61
- 2026-05-11 20:15 | Estrela vs Famalicao | football_data_bet365_proxy | 3.5/3.6/1.96
- 2026-05-11 20:15 | Estrela vs Famalicao | football_data_max_market_proxy | 3.7/3.6/2.0
- 2026-05-11 20:15 | Estrela vs Famalicao | football_data_average_market_proxy | 3.51/3.42/1.96
- 2026-05-11 20:15 | Gil Vicente vs Arouca | football_data_bet365_proxy | 1.66/3.8/4.75
- 2026-05-11 20:15 | Gil Vicente vs Arouca | football_data_max_market_proxy | 1.73/3.8/4.9
- 2026-05-11 20:15 | Gil Vicente vs Arouca | football_data_average_market_proxy | 1.69/3.67/4.55
- 2026-05-11 20:15 | Guimaraes vs Casa Pia | football_data_bet365_proxy | 1.71/3.75/4.33
- 2026-05-11 20:15 | Guimaraes vs Casa Pia | football_data_max_market_proxy | 1.78/4.0/4.75
- 2026-05-11 20:15 | Guimaraes vs Casa Pia | football_data_average_market_proxy | 1.72/3.67/4.3
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon | football_data_bet365_proxy | 10.0/5.5/1.24
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon | football_data_max_market_proxy | 11.0/6.4/1.28
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon | football_data_average_market_proxy | 9.64/5.89/1.23
- 2026-05-11 20:15 | Santa Clara vs Nacional | football_data_bet365_proxy | 2.05/3.4/3.5
- 2026-05-11 20:15 | Santa Clara vs Nacional | football_data_max_market_proxy | 2.12/3.4/3.75

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.
Upcoming fixture rows: 151
Fixture team rows unmatched: 292
Ready for model-fixture join: False
Automatic forward price rows: 33
odds-api.io price rows: 0
Football-Data price rows: 33
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- Benfica | suggestion=nan | type=unmatched
- Sp Braga | suggestion=nan | type=unmatched
- Cerro Largo FC | suggestion=nan | type=unmatched
- CA Penarol Montevideo | suggestion=nan | type=unmatched
- Cerro Porteno | suggestion=nan | type=unmatched
- Club Guarani Asuncion | suggestion=nan | type=unmatched
- CR Flamengo RJ | suggestion=nan | type=unmatched
- Ferroviaria SP | suggestion=nan | type=unmatched
- Deportivo Cali | suggestion=nan | type=unmatched
- CA Bucaramanga | suggestion=nan | type=unmatched
- Deportivo Saprissa | suggestion=nan | type=unmatched
- Sporting FC | suggestion=nan | type=unmatched
- Estrela | suggestion=nan | type=unmatched
- Famalicao | suggestion=nan | type=unmatched
- G3X FC | suggestion=nan | type=unmatched
- Capim FC | suggestion=nan | type=unmatched
- Gil Vicente | suggestion=nan | type=unmatched

## forward_price_coverage

# Forward Price Coverage Report
Measures automatic price coverage for forward predictions.
Fresh API price means odds-api.io or API-Football. This is still paper/proxy-only and not real-money ready.
Forward prediction rows: 80
Automatic price rows: 33
Value snapshot rows: 99
Matches with any automatic price: 11
Matches with fresh API price: 0
Matches with odds-api.io price: 0
Fresh API match coverage rate: 0.0
odds-api.io match coverage rate: 0.0
Real-money ready: False
## Match coverage
- 2026-05-11 | Huesca vs Sociedad B | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Napoli vs Bologna | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Tottenham vs Leeds | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Vallecano vs Girona | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Benfica vs Sp Braga | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Estrela vs Famalicao | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Gil Vicente vs Arouca | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Guimaraes vs Casa Pia | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Rio Ave vs Sp Lisbon | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Santa Clara vs Nacional | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | Tondela vs Moreirense | any=True | fresh_api=False | odds_api_io=False | rows=3 | sources=football_data_average_market_proxy, football_data_bet365_proxy, football_data_max_market_proxy
- 2026-05-11 | CR Flamengo RJ vs Ferroviaria SP | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-11 | Deportivo Saprissa vs Sporting FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-11 | Loud SC vs Funkbol Clube | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-11 | Piaui PI vs Ferroviario AC CE | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-11 | Sol de America Villa Elisa vs Guairena FC | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=
- 2026-05-11 | Cerro Porteno vs Club Guarani Asuncion | any=False | fresh_api=False | odds_api_io=False | rows=0 | sources=

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Combined automatic forward market proxy joined to forward probability predictions.
Includes Football-Data delayed proxy and capped odds-api.io single-event proxy when available.
Not live/full-market coverage and not real-money ready.
Forward prediction rows: 80
Proxy price rows: 34
Matched prediction rows: 11
Value snapshot rows: 99
odds-api.io snapshot rows: 0
Positive EV rows: 49
Source counts: {'football_data_bet365_proxy': 33, 'football_data_max_market_proxy': 33, 'football_data_average_market_proxy': 33}
- 2026-05-11 | Rio Ave vs Sp Lisbon | sel=HOME | src=football_data_max_market_proxy | odds=11.0 | prob=0.3772 | EV=3.1492 | match=1.0
- 2026-05-11 | Rio Ave vs Sp Lisbon | sel=HOME | src=football_data_bet365_proxy | odds=10.0 | prob=0.3772 | EV=2.772 | match=1.0
- 2026-05-11 | Rio Ave vs Sp Lisbon | sel=HOME | src=football_data_average_market_proxy | odds=9.64 | prob=0.3772 | EV=2.636208 | match=1.0
- 2026-05-11 | Benfica vs Sp Braga | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-11 | Benfica vs Sp Braga | sel=AWAY | src=football_data_bet365_proxy | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-11 | Benfica vs Sp Braga | sel=AWAY | src=football_data_average_market_proxy | odds=6.61 | prob=0.3488 | EV=1.305568 | match=1.0
- 2026-05-11 | Napoli vs Bologna | sel=AWAY | src=football_data_max_market_proxy | odds=6.5 | prob=0.3149 | EV=1.04685 | match=1.0
- 2026-05-11 | Napoli vs Bologna | sel=AWAY | src=football_data_average_market_proxy | odds=6.06 | prob=0.3149 | EV=0.908294 | match=1.0
- 2026-05-11 | Napoli vs Bologna | sel=AWAY | src=football_data_bet365_proxy | odds=6.0 | prob=0.3149 | EV=0.8894 | match=1.0
- 2026-05-11 | Rio Ave vs Sp Lisbon | sel=DRAW | src=football_data_max_market_proxy | odds=6.4 | prob=0.274 | EV=0.7536 | match=1.0
- 2026-05-11 | Gil Vicente vs Arouca | sel=AWAY | src=football_data_max_market_proxy | odds=4.9 | prob=0.3488 | EV=0.70912 | match=1.0
- 2026-05-11 | Guimaraes vs Casa Pia | sel=AWAY | src=football_data_max_market_proxy | odds=4.75 | prob=0.3488 | EV=0.6568 | match=1.0
- 2026-05-11 | Gil Vicente vs Arouca | sel=AWAY | src=football_data_bet365_proxy | odds=4.75 | prob=0.3488 | EV=0.6568 | match=1.0
- 2026-05-11 | Rio Ave vs Sp Lisbon | sel=DRAW | src=football_data_average_market_proxy | odds=5.89 | prob=0.274 | EV=0.61386 | match=1.0
- 2026-05-11 | Gil Vicente vs Arouca | sel=AWAY | src=football_data_average_market_proxy | odds=4.55 | prob=0.3488 | EV=0.58704 | match=1.0
- 2026-05-11 | Guimaraes vs Casa Pia | sel=AWAY | src=football_data_bet365_proxy | odds=4.33 | prob=0.3488 | EV=0.510304 | match=1.0
- 2026-05-11 | Rio Ave vs Sp Lisbon | sel=DRAW | src=football_data_bet365_proxy | odds=5.5 | prob=0.274 | EV=0.507 | match=1.0
- 2026-05-11 | Guimaraes vs Casa Pia | sel=AWAY | src=football_data_average_market_proxy | odds=4.3 | prob=0.3488 | EV=0.49984 | match=1.0
- 2026-05-11 | Tondela vs Moreirense | sel=AWAY | src=football_data_bet365_proxy | odds=4.1 | prob=0.3488 | EV=0.43008 | match=1.0

## proxy_candidate_observations

# Proxy Candidate Observations
Intermediate layer between paper-test picks and real candidate bets.
These rows are proxy/paper observations only and must not be treated as real-money candidates.
Deduplicated by match date, normalized teams, and selection; best proxy score is kept.
Automatic value rows: 99
Pre-dedupe proxy candidate observation rows: 36
Proxy candidate observation rows: 12
Proxy candidate-like rows: 0
Suppressed proxy watchlist rows: 11
Dedupe strategy: match_date_normalized_teams_selection_keep_best_score
Real-money ready: False
- 2026-05-11 | Estrela vs Famalicao | selection=HOME | source=football_data_max_market_proxy | odds=3.7 | prob=0.3772 | EV=0.39564 | edge=0.10693 | penalty=0.39564139564139555 | tier=proxy_watchlist | score=0.2243
- 2026-05-11 | Tondela vs Moreirense | selection=AWAY | source=football_data_bet365_proxy | odds=4.1 | prob=0.3488 | EV=0.43008 | edge=0.104898 | penalty=0.4300825741486334 | tier=suppressed_proxy_watchlist | score=0.1066
- 2026-05-11 | Huesca vs Sociedad B | selection=AWAY | source=football_data_max_market_proxy | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | tier=suppressed_proxy_watchlist | score=0.1054
- 2026-05-11 | Santa Clara vs Nacional | selection=AWAY | source=football_data_max_market_proxy | odds=3.75 | prob=0.3488 | EV=0.308 | edge=0.082133 | penalty=0.3079983650020437 | tier=suppressed_proxy_watchlist | score=0.1023
- 2026-05-11 | Tottenham vs Leeds | selection=AWAY | source=football_data_max_market_proxy | odds=4.1 | prob=0.3152 | EV=0.29232 | edge=0.071298 | penalty=0.29232232618018705 | tier=suppressed_proxy_watchlist | score=0.1
- 2026-05-11 | Benfica vs Sp Braga | selection=DRAW | source=football_data_max_market_proxy | odds=4.8 | prob=0.274 | EV=0.3152 | edge=0.065667 | penalty=0.31520210432336704 | tier=suppressed_proxy_watchlist | score=0.0986
- 2026-05-11 | Napoli vs Bologna | selection=DRAW | source=football_data_bet365_proxy | odds=4.2 | prob=0.2843 | EV=0.19406 | edge=0.046205 | penalty=0.19406119406119404 | tier=suppressed_proxy_watchlist | score=0.095
- 2026-05-11 | Guimaraes vs Casa Pia | selection=DRAW | source=football_data_max_market_proxy | odds=4.0 | prob=0.274 | EV=0.096 | edge=0.024 | penalty=0.09600000000000009 | tier=suppressed_proxy_watchlist | score=0.0908
- 2026-05-11 | Vallecano vs Girona | selection=AWAY | source=football_data_max_market_proxy | odds=3.05 | prob=0.3376 | EV=0.02968 | edge=0.009731 | penalty=0.029679536644208415 | tier=suppressed_proxy_watchlist | score=0.0904
- 2026-05-11 | Tottenham vs Leeds | selection=DRAW | source=football_data_bet365_proxy | odds=4.1 | prob=0.259 | EV=0.0619 | edge=0.015098 | penalty=0.06190191142344048 | tier=suppressed_proxy_watchlist | score=0.0889
- 2026-05-11 | Gil Vicente vs Arouca | selection=DRAW | source=football_data_bet365_proxy | odds=3.8 | prob=0.274 | EV=0.0412 | edge=0.010842 | penalty=0.041199583520166616 | tier=suppressed_proxy_watchlist | score=0.0886
- 2026-05-11 | Gil Vicente vs Arouca | selection=AWAY | source=football_data_average_market_proxy | odds=4.55 | prob=0.3488 | EV=0.58704 | edge=0.12902 | penalty=0.587041587041587 | tier=suppressed_proxy_watchlist | score=0.0883

## proxy_candidate_explanations

# Proxy Candidate Explanation Report
Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.
Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: delayed_football_data_proxy_not_fresh_api_price
Real-money ready: False
## Blocker summary
- delayed_football_data_proxy_not_fresh_api_price: 12
- probability_or_league_rule_suppressed: 11
- low_probability_band_under_0_35: 11
- ev_above_real_candidate_cap_possible_overconfidence: 8
- market_alignment_penalty_too_high_for_real_candidate: 8
- edge_below_candidate_threshold: 3
## Row explanations
- 2026-05-11 | Estrela vs Famalicao | sel=HOME | score=0.2243 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Tondela vs Moreirense | sel=AWAY | score=0.1066 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Huesca vs Sociedad B | sel=AWAY | score=0.1054 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Santa Clara vs Nacional | sel=AWAY | score=0.1023 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Tottenham vs Leeds | sel=AWAY | score=0.1 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Benfica vs Sp Braga | sel=DRAW | score=0.0986 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Napoli vs Bologna | sel=DRAW | score=0.095 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Guimaraes vs Casa Pia | sel=DRAW | score=0.0908 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Vallecano vs Girona | sel=AWAY | score=0.0904 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Tottenham vs Leeds | sel=DRAW | score=0.0889 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Gil Vicente vs Arouca | sel=DRAW | score=0.0886 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Gil Vicente vs Arouca | sel=AWAY | score=0.0883 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 99
Paper proxy observation rows: 7
Positive EV value rows: 49
Suppressed-band observation rows: 4
Distinct matches: 3
Distinct sources: 0
Max EV: 0.43008
Average EV: 0.374373
Max probability edge: 0.10693
Average match confidence: None
## By selection
- away: rows=4, avg_ev=0.3952, max_ev=0.4301
- home: rows=3, avg_ev=0.3466, max_ev=0.3956

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Full model rows use matched team-strength data. Baseline rows are conservative league-average placeholders used to increase odds-matching coverage only.
Upcoming fixture rows: 151
Forward fixture prediction rows: 80
Full model prediction rows: 3
Baseline prediction rows: 77
Max forward predictions: 80
Ready for price join: True
- 2026-05-11 19:30 | Huesca vs Sociedad B | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 19:45 | Napoli vs Bologna | coverage=full_team_strength_match | H=0.4007 D=0.2843 A=0.3149 | fair=2.5/3.52/3.18
- 2026-05-11 20:00 | Tottenham vs Leeds | coverage=full_team_strength_match | H=0.4257 D=0.259 A=0.3152 | fair=2.35/3.86/3.17
- 2026-05-11 20:00 | Vallecano vs Girona | coverage=full_team_strength_match | H=0.3833 D=0.279 A=0.3376 | fair=2.61/3.58/2.96
- 2026-05-11 20:15 | Benfica vs Sp Braga | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 20:15 | Estrela vs Famalicao | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 20:15 | Gil Vicente vs Arouca | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 20:15 | Guimaraes vs Casa Pia | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 20:15 | Santa Clara vs Nacional | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 20:15 | Tondela vs Moreirense | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 22:00 | CR Flamengo RJ vs Ferroviaria SP | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 22:00 | Deportivo Saprissa vs Sporting FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 22:00 | Loud SC vs Funkbol Clube | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 22:00 | Piaui PI vs Ferroviario AC CE | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 22:30 | Sol de America Villa Elisa vs Guairena FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 23:00 | Cerro Porteno vs Club Guarani Asuncion | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 23:00 | Deportivo Cali vs CA Bucaramanga | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 23:00 | G3X FC vs Capim FC | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 23:00 | Maringa FC PR vs Guarani FC SP | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87
- 2026-05-11 23:00 | Sportivo Trinidense vs Sportivo Luqueno | coverage=baseline_unmatched_fixture | H=0.3772 D=0.274 A=0.3488 | fair=2.65/3.65/2.87

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 80
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 86
Log type: probability_only_no_market_prices
- 2026-05-12 2026-05-11 14:10:00 | AL Wasl vs AL Jazira | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 14:45:00 | PFC Cherno More Varna vs PFC Lokomotiv Plovdiv | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:00:00 | AL Faisaly (Jor) vs Ramtha SC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:00:00 | FK Liepaja vs Ogre United | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:00:00 | JS Omrane vs Avenir S Marsa | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:00:00 | FC Metalist 1925 Kharkiv vs Karpaty Lviv | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:00:00 | MFK Chrudim vs FK Pribram | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:00:00 | Veres Rivne vs FC Kryvbas Kriviy Rih | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:00:00 | Zaglebie Lubin II vs Mkp Carina Gubin | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:30:00 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:30:00 | AL Wahda FC vs Khorfakkan | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:30:00 | FK Mlada Boleslav vs Dukla Prague | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 15:30:00 | FC Zlin vs FK Teplice | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 16:00:00 | AE Kifisia FC vs Atromitos Athinon | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 16:00:00 | Asteras Tripolis vs Panserraikos FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 16:00:00 | FC Elva vs Paide Linnameeskond | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 16:00:00 | Panaitolikos Agrinio vs AE Larissa FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 16:00:00 | Rayon Sports FC vs Gorilla FC | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 16:00:00 | Riga FC vs FK Auda Riga | H=0.37720000000000004 D=0.274 A=0.3488
- 2026-05-12 2026-05-11 16:00:00 | Sarpsborg 08 FF vs Hoenefoss BK | H=0.37720000000000004 D=0.274 A=0.3488

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
Upcoming fixtures: 151
Manual template rows: 151
Rows with complete manual odds: 0
Rows missing manual odds: 151
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-11 20:15 | Benfica vs Sp Braga
- 2026-05-11 23:30 | Cerro Largo FC vs CA Penarol Montevideo
- 2026-05-11 23:00 | Cerro Porteno vs Club Guarani Asuncion
- 2026-05-11 22:00 | CR Flamengo RJ vs Ferroviaria SP
- 2026-05-11 23:00 | Deportivo Cali vs CA Bucaramanga
- 2026-05-11 22:00 | Deportivo Saprissa vs Sporting FC
- 2026-05-11 20:15 | Estrela vs Famalicao
- 2026-05-11 23:00 | G3X FC vs Capim FC
- 2026-05-11 20:15 | Gil Vicente vs Arouca
- 2026-05-11 20:15 | Guimaraes vs Casa Pia
- 2026-05-11 19:30 | Huesca vs Sociedad B
- 2026-05-11 22:00 | Loud SC vs Funkbol Clube
- 2026-05-11 23:00 | Maringa FC PR vs Guarani FC SP
- 2026-05-11 19:45 | Napoli vs Bologna
- 2026-05-11 22:00 | Piaui PI vs Ferroviario AC CE

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 151
Source counts: {'odds_api_io_events_bookmaker_filtered': 126, 'odds_api_io_events_search': 14, 'football_data_fixtures_proxy': 11}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-11 20:15 | Benfica vs Sp Braga | P1 | football_data_fixtures_proxy
- 2026-05-11 23:30 | Cerro Largo FC vs CA Penarol Montevideo | uruguay-primera-division | odds_api_io_events_bookmaker_filtered
- 2026-05-11 23:00 | Cerro Porteno vs Club Guarani Asuncion | paraguay-division-de-honor-apertura | odds_api_io_events_bookmaker_filtered
- 2026-05-11 22:00 | CR Flamengo RJ vs Ferroviaria SP | brazil-campeonato-brasileiro-women | odds_api_io_events_bookmaker_filtered
- 2026-05-11 23:00 | Deportivo Cali vs CA Bucaramanga | colombia-copa-colombia | odds_api_io_events_bookmaker_filtered
- 2026-05-11 22:00 | Deportivo Saprissa vs Sporting FC | costa-rica-primera-division-women | odds_api_io_events_bookmaker_filtered
- 2026-05-11 20:15 | Estrela vs Famalicao | P1 | football_data_fixtures_proxy
- 2026-05-11 23:00 | G3X FC vs Capim FC | soccerspecials-kings-league-brazil | odds_api_io_events_bookmaker_filtered
- 2026-05-11 20:15 | Gil Vicente vs Arouca | P1 | football_data_fixtures_proxy
- 2026-05-11 20:15 | Guimaraes vs Casa Pia | P1 | football_data_fixtures_proxy
- 2026-05-11 19:30 | Huesca vs Sociedad B | SP2 | football_data_fixtures_proxy
- 2026-05-11 22:00 | Loud SC vs Funkbol Clube | soccerspecials-kings-league-brazil | odds_api_io_events_bookmaker_filtered
- 2026-05-11 23:00 | Maringa FC PR vs Guarani FC SP | brazil-brasileiro-serie-c | odds_api_io_events_bookmaker_filtered
- 2026-05-11 19:45 | Napoli vs Bologna | serie_a | football_data_fixtures_proxy
- 2026-05-11 22:00 | Piaui PI vs Ferroviario AC CE | brazil-brasileiro-serie-d | odds_api_io_events_bookmaker_filtered
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon | P1 | football_data_fixtures_proxy
- 2026-05-11 20:15 | Santa Clara vs Nacional | P1 | football_data_fixtures_proxy
- 2026-05-11 22:30 | Sol de America Villa Elisa vs Guairena FC | paraguay-segunda-division | odds_api_io_events_bookmaker_filtered
- 2026-05-11 23:00 | Sportivo Trinidense vs Sportivo Luqueno | paraguay-camopeonato-femenino-women | odds_api_io_events_bookmaker_filtered
- 2026-05-11 20:15 | Tondela vs Moreirense | P1 | football_data_fixtures_proxy
- 2026-05-11 20:00 | Tottenham vs Leeds | premier_league | football_data_fixtures_proxy
- 2026-05-11 20:00 | Vallecano vs Girona | la_liga | football_data_fixtures_proxy
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | czechia-1-liga | odds_api_io_events_bookmaker_filtered

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 151
Rows with complete odds: 0
- 2026-05-11 20:15 | Benfica vs Sp Braga | bookmaker=bet365_manual
- 2026-05-11 23:30 | Cerro Largo FC vs CA Penarol Montevideo | bookmaker=bet365_manual
- 2026-05-11 23:00 | Cerro Porteno vs Club Guarani Asuncion | bookmaker=bet365_manual
- 2026-05-11 22:00 | CR Flamengo RJ vs Ferroviaria SP | bookmaker=bet365_manual
- 2026-05-11 23:00 | Deportivo Cali vs CA Bucaramanga | bookmaker=bet365_manual
- 2026-05-11 22:00 | Deportivo Saprissa vs Sporting FC | bookmaker=bet365_manual
- 2026-05-11 20:15 | Estrela vs Famalicao | bookmaker=bet365_manual
- 2026-05-11 23:00 | G3X FC vs Capim FC | bookmaker=bet365_manual
- 2026-05-11 20:15 | Gil Vicente vs Arouca | bookmaker=bet365_manual
- 2026-05-11 20:15 | Guimaraes vs Casa Pia | bookmaker=bet365_manual
- 2026-05-11 19:30 | Huesca vs Sociedad B | bookmaker=bet365_manual
- 2026-05-11 22:00 | Loud SC vs Funkbol Clube | bookmaker=bet365_manual
- 2026-05-11 23:00 | Maringa FC PR vs Guarani FC SP | bookmaker=bet365_manual
- 2026-05-11 19:45 | Napoli vs Bologna | bookmaker=bet365_manual
- 2026-05-11 22:00 | Piaui PI vs Ferroviario AC CE | bookmaker=bet365_manual
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon | bookmaker=bet365_manual
- 2026-05-11 20:15 | Santa Clara vs Nacional | bookmaker=bet365_manual
- 2026-05-11 22:30 | Sol de America Villa Elisa vs Guairena FC | bookmaker=bet365_manual
- 2026-05-11 23:00 | Sportivo Trinidense vs Sportivo Luqueno | bookmaker=bet365_manual
- 2026-05-11 20:15 | Tondela vs Moreirense | bookmaker=bet365_manual
- 2026-05-11 20:00 | Tottenham vs Leeds | bookmaker=bet365_manual
- 2026-05-11 20:00 | Vallecano vs Girona | bookmaker=bet365_manual
- 2026-05-12 15:30 | 1. FC Slovacko Uherske Hradiste vs FC Banik Ostrava | bookmaker=bet365_manual
- 2026-05-12 18:45 | Aberdeen FC vs St Mirren FC | bookmaker=bet365_manual

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
- 2026-05-11 20:15 | Benfica vs Sp Braga
- 2026-05-11 23:30 | Cerro Largo FC vs CA Penarol Montevideo
- 2026-05-11 23:00 | Cerro Porteno vs Club Guarani Asuncion
- 2026-05-11 22:00 | CR Flamengo RJ vs Ferroviaria SP
- 2026-05-11 23:00 | Deportivo Cali vs CA Bucaramanga
- 2026-05-11 22:00 | Deportivo Saprissa vs Sporting FC
- 2026-05-11 20:15 | Estrela vs Famalicao
- 2026-05-11 23:00 | G3X FC vs Capim FC
- 2026-05-11 20:15 | Gil Vicente vs Arouca
- 2026-05-11 20:15 | Guimaraes vs Casa Pia
- 2026-05-11 19:30 | Huesca vs Sociedad B
- 2026-05-11 22:00 | Loud SC vs Funkbol Clube
- 2026-05-11 23:00 | Maringa FC PR vs Guarani FC SP
- 2026-05-11 19:45 | Napoli vs Bologna
- 2026-05-11 22:00 | Piaui PI vs Ferroviario AC CE
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon
- 2026-05-11 20:15 | Santa Clara vs Nacional
- 2026-05-11 22:30 | Sol de America Villa Elisa vs Guairena FC
- 2026-05-11 23:00 | Sportivo Trinidense vs Sportivo Luqueno

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 23
Valid forward/proxy log rows: 20
Deduped forward/proxy observation rows: 7
Duplicate forward/proxy log rows: 13
Valid automatic proxy observation rows: 20
Deduped automatic proxy observation rows: 7
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Deduped valid rows
- 2026-05-11 | Estrela vs Famalicao | selection=home | phase=automatic_forward_price_proxy | tier=proxy_observation | score=0.2607
- 2026-05-11 | Tondela vs Moreirense | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.13470000000000001
- 2026-05-11 | Huesca vs Sociedad B | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.134
- 2026-05-11 | Tottenham vs Leeds | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1313
- 2026-05-11 | Napoli vs Bologna | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.12610000000000002
- 2026-05-11 | Vallecano vs Girona | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1245
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation | score=0.1216
## Raw valid rows
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham vs Leeds | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham vs Leeds | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham vs Leeds | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Napoli vs Bologna | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Napoli vs Bologna | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Napoli vs Bologna | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Vallecano vs Girona | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation

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
### Estrela vs Famalicao
- Date/time: 2026-05-11 20:15
- League/phase: P1 / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 3.7
- Fair odds: 2.65
- Model probability: 0.3772
- Probability band: 0.35-0.45
- EV: 0.3956
- Probability edge: 0.1069
- Alignment penalty: 0.3956
- Suppression action: monitor
- Paper tier: proxy_observation
- Paper score: 0.2607
- Prediction ID: f3a5bbf9203d8903e4e0
### Estrela vs Famalicao
- Date/time: 2026-05-11 20:15
- League/phase: P1 / automatic_forward_price_proxy
- Selection: HOME
- Market odds: 3.51
- Fair odds: 2.65
- Model probability: 0.3772
- Probability band: 0.35-0.45

## paper_test_picks

# Paper Test Picks
Observation-only picks. These are not real-money recommendations.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Suppressed historical bands may be tracked only as proxy observation and remain excluded from real-money readiness.
Source used: automatic_forward_value_snapshots
Current paper-test picks: 7
Newly logged paper-test picks: 0
Total logged paper-test rows: 23
- Estrela vs Famalicao | selection=HOME | odds=3.7 | prob=0.3772 | EV=0.3956 | edge=0.1069 | penalty=0.3956 | band=0.35-0.45 | rule=monitor | tier=proxy_observation
- Estrela vs Famalicao | selection=HOME | odds=3.51 | prob=0.3772 | EV=0.324 | edge=0.0923 | penalty=0.324 | band=0.35-0.45 | rule=monitor | tier=priority_proxy_observation
- Estrela vs Famalicao | selection=HOME | odds=3.5 | prob=0.3772 | EV=0.3202 | edge=0.0915 | penalty=0.3202 | band=0.35-0.45 | rule=monitor | tier=priority_proxy_observation
- Tondela vs Moreirense | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Tondela vs Moreirense | selection=AWAY | odds=4.1 | prob=0.3488 | EV=0.4301 | edge=0.1049 | penalty=0.4301 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Huesca vs Sociedad B | selection=AWAY | odds=4.0 | prob=0.3488 | EV=0.3952 | edge=0.0988 | penalty=0.3952 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Huesca vs Sociedad B | selection=AWAY | odds=3.8 | prob=0.3488 | EV=0.3254 | edge=0.0856 | penalty=0.3254 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation

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
