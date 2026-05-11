# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-11T14:25:01.506408+00:00`
GitHub run: `250` attempt `1`
GitHub SHA: `c6fe2bf5b866abfe8b91e014b47b24885f901511`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Project goal readiness summary | True | 1 |  |  |
| Project goal readiness stages | True | 5 |  |  |
| Football-Data upcoming fixtures proxy | True | 11 |  |  |
| Football-Data upcoming odds proxy | True | 33 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| odds-api.io forward prices | True | 0 |  |  |
| odds-api.io forward fixtures | True | 0 |  |  |
| odds-api.io forward price status | True | 1 |  |  |
| API-Football forward prices | True | 0 |  |  |
| API-Football forward fixtures | True | 0 |  |  |
| API-Football forward price status | True | 1 |  |  |
| Automatic forward value snapshots | True | 27 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 3 |  |  |
| Proxy observation quality report | True | 1 |  |  |
| Proxy observation by selection | True | 2 |  |  |
| Upcoming fixtures | True | 11 |  |  |
| Forward fixture results | True | 1 |  |  |
| Forward fixture result status | True | 1 |  |  |
| Forward probability calibration report | True | 1 |  |  |
| Forward probability calibration summary | True | 1 |  |  |
| Automatic forward source report | True | 1 |  |  |

## project_goal_readiness

# Project Goal Readiness Report
Overall project stage: `proxy_paper_testing_started`
## Current counts
- Forward fixture predictions: 3
- Automatic value snapshots: 27
- Positive EV proxy rows: 13
- Proxy observation rows: 7
- Valid forward/proxy log rows: 12
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
Current: 27 value snapshots from delayed proxy prices.
Done when: Keep Football-Data as baseline; add optional API source for fresher odds.
### paper_forward_testing
Status: `started_not_mature`
Target: At least 50-100 logged proxy observations across several matchdays.
Current: 12 valid forward/proxy log rows.
Done when: Minimum 50 observations before drawing early conclusions; 100+ preferred.
### forward_probability_calibration
Status: `not_ready`
Target: Settled forward rows available for Brier/accuracy/calibration review.
Current: 0 settled forward rows.

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
Upcoming fixture rows: 19
Fixture team rows unmatched: 32
Ready for model-fixture join: False
Automatic forward price rows: 33
odds-api.io price rows: 0
Football-Data price rows: 33
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures
## Team matching
- Guapore  RO | suggestion=nan | type=unmatched
- Galvez EC AC | suggestion=nan | type=unmatched
- Aguia de Maraba FC PA | suggestion=nan | type=unmatched
- Oratorio RC AP | suggestion=nan | type=unmatched
- FC Aktobe | suggestion=nan | type=unmatched
- Kaisar Kyzylorda | suggestion=nan | type=unmatched
- Kwun Tong | suggestion=nan | type=unmatched
- Hoi King | suggestion=nan | type=unmatched
- Pas Pyrgos | suggestion=nan | type=unmatched
- APS Zakynthos | suggestion=nan | type=unmatched
- Real San Joaquin | suggestion=nan | type=unmatched
- Deportes Colina | suggestion=nan | type=unmatched
- Yokohama F Marinos | suggestion=nan | type=unmatched
- Kashima Antlers | suggestion=nan | type=unmatched
- Benfica | suggestion=nan | type=unmatched
- Sp Braga | suggestion=nan | type=unmatched
- Estrela | suggestion=nan | type=unmatched

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Delayed/free market proxy joined to forward probability predictions.
Not live odds, not Bet365 direct, and not real-money ready.
Forward prediction rows: 3
Proxy price rows: 33
Matched prediction rows: 3
Value snapshot rows: 27
Positive EV rows: 13
- 2026-05-11 | Napoli vs Bologna | sel=AWAY | src=football_data_max_market_proxy | odds=6.5 | prob=0.3149 | EV=1.04685 | match=1.0
- 2026-05-11 | Napoli vs Bologna | sel=AWAY | src=football_data_average_market_proxy | odds=6.06 | prob=0.3149 | EV=0.908294 | match=1.0
- 2026-05-11 | Napoli vs Bologna | sel=AWAY | src=football_data_bet365_proxy | odds=6.0 | prob=0.3149 | EV=0.8894 | match=1.0
- 2026-05-11 | Tottenham vs Leeds | sel=AWAY | src=football_data_max_market_proxy | odds=4.1 | prob=0.3152 | EV=0.29232 | match=1.0
- 2026-05-11 | Tottenham vs Leeds | sel=AWAY | src=football_data_average_market_proxy | odds=3.92 | prob=0.3152 | EV=0.235584 | match=1.0
- 2026-05-11 | Napoli vs Bologna | sel=DRAW | src=football_data_max_market_proxy | odds=4.2 | prob=0.2843 | EV=0.19406 | match=1.0
- 2026-05-11 | Napoli vs Bologna | sel=DRAW | src=football_data_bet365_proxy | odds=4.2 | prob=0.2843 | EV=0.19406 | match=1.0
- 2026-05-11 | Tottenham vs Leeds | sel=AWAY | src=football_data_bet365_proxy | odds=3.75 | prob=0.3152 | EV=0.182 | match=1.0
- 2026-05-11 | Napoli vs Bologna | sel=DRAW | src=football_data_average_market_proxy | odds=4.01 | prob=0.2843 | EV=0.140043 | match=1.0
- 2026-05-11 | Tottenham vs Leeds | sel=DRAW | src=football_data_max_market_proxy | odds=4.1 | prob=0.259 | EV=0.0619 | match=1.0
- 2026-05-11 | Tottenham vs Leeds | sel=DRAW | src=football_data_bet365_proxy | odds=4.1 | prob=0.259 | EV=0.0619 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=AWAY | src=football_data_max_market_proxy | odds=3.05 | prob=0.3376 | EV=0.02968 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=AWAY | src=football_data_bet365_proxy | odds=3.0 | prob=0.3376 | EV=0.0128 | match=1.0
- 2026-05-11 | Tottenham vs Leeds | sel=DRAW | src=football_data_average_market_proxy | odds=3.82 | prob=0.259 | EV=-0.01062 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=AWAY | src=football_data_average_market_proxy | odds=2.92 | prob=0.3376 | EV=-0.014208 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=DRAW | src=football_data_max_market_proxy | odds=3.5 | prob=0.279 | EV=-0.0235 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=DRAW | src=football_data_bet365_proxy | odds=3.5 | prob=0.279 | EV=-0.0235 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=DRAW | src=football_data_average_market_proxy | odds=3.39 | prob=0.279 | EV=-0.05419 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=HOME | src=football_data_max_market_proxy | odds=2.38 | prob=0.3833 | EV=-0.087746 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=HOME | src=football_data_bet365_proxy | odds=2.3 | prob=0.3833 | EV=-0.11841 | match=1.0
- 2026-05-11 | Vallecano vs Girona | sel=HOME | src=football_data_average_market_proxy | odds=2.3 | prob=0.3833 | EV=-0.11841 | match=1.0
- 2026-05-11 | Tottenham vs Leeds | sel=HOME | src=football_data_max_market_proxy | odds=1.86 | prob=0.4257 | EV=-0.208198 | match=1.0

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 27
Paper proxy observation rows: 7
Positive EV value rows: 13
Suppressed-band observation rows: 7
Distinct matches: 3
Distinct sources: 0
Max EV: 0.29232
Average EV: 0.181107
Max probability edge: 0.071298
Average match confidence: None
## By selection
- away: rows=4, avg_ev=0.1849, max_ev=0.2923
- draw: rows=3, avg_ev=0.1761, max_ev=0.1941

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Upcoming fixture rows: 19
Forward fixture prediction rows: 3
Ready for price join: True
- 2026-05-11 19:45 | Napoli vs Bologna | H=0.4007 D=0.2843 A=0.3149 | fair=2.5/3.52/3.18
- 2026-05-11 20:00 | Tottenham vs Leeds | H=0.4257 D=0.259 A=0.3152 | fair=2.35/3.86/3.17
- 2026-05-11 20:00 | Vallecano vs Girona | H=0.3833 D=0.279 A=0.3376 | fair=2.61/3.58/2.96

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 3
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 4
Log type: probability_only_no_market_prices
- 2026-05-11 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United | H=0.4257 D=0.259 A=0.31520000000000004
- 2026-05-11 2026-05-11 20:00:00 | Tottenham vs Leeds | H=0.4257 D=0.259 A=0.31520000000000004
- 2026-05-11 2026-05-11 19:45:00 | Napoli vs Bologna | H=0.4007 D=0.2843 A=0.3149
- 2026-05-11 2026-05-11 20:00:00 | Vallecano vs Girona | H=0.38330000000000003 D=0.279 A=0.3376

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
Upcoming fixtures: 19
Manual template rows: 19
Rows with complete manual odds: 0
Rows missing manual odds: 19
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-09 23:30 | Guapore  RO vs Galvez EC AC
- 2026-05-10 20:00 | Aguia de Maraba FC PA vs Oratorio RC AP
- 2026-05-10 12:00 | FC Aktobe vs Kaisar Kyzylorda
- 2026-05-10 07:30 | Kwun Tong vs Hoi King
- 2026-05-10 13:00 | Pas Pyrgos vs APS Zakynthos
- 2026-05-10 19:00 | Real San Joaquin vs Deportes Colina
- 2026-05-10 05:00 | Yokohama F Marinos vs Kashima Antlers
- 2026-05-11 20:15 | Benfica vs Sp Braga
- 2026-05-11 20:15 | Estrela vs Famalicao
- 2026-05-11 20:15 | Gil Vicente vs Arouca
- 2026-05-11 20:15 | Guimaraes vs Casa Pia
- 2026-05-11 19:30 | Huesca vs Sociedad B
- 2026-05-11 19:45 | Napoli vs Bologna
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon
- 2026-05-11 20:15 | Santa Clara vs Nacional

## upcoming_fixtures

# Upcoming Fixtures
Fixture sources: TheSportsDB, Football-Data fixtures proxy, cautious odds-api.io events, and disabled-by-default API-Football status.
Duplicate fixtures are deduplicated by date and normalized teams, preferring odds-api.io then Football-Data for odds alignment.
Primary development target: automatic/free market proxy, not manual Bet365.
Fixtures found: 19
Source counts: {'football_data_fixtures_proxy': 11, 'odds_api_io_events': 8}
Dedupe strategy: date_normalized_home_away_prefer_odds_api_then_football_data
- 2026-05-09 23:30 | Guapore  RO vs Galvez EC AC | brazil-brasileiro-serie-d | odds_api_io_events
- 2026-05-10 20:00 | Aguia de Maraba FC PA vs Oratorio RC AP | brazil-brasileiro-serie-d | odds_api_io_events
- 2026-05-10 12:00 | FC Aktobe vs Kaisar Kyzylorda | kazakhstan-premier-league | odds_api_io_events
- 2026-05-10 07:30 | Kwun Tong vs Hoi King | hong-kong-china-1-division | odds_api_io_events
- 2026-05-10 13:00 | Pas Pyrgos vs APS Zakynthos | greece-gamma-ethniki | odds_api_io_events
- 2026-05-10 19:00 | Real San Joaquin vs Deportes Colina | chile-segunda-division | odds_api_io_events
- 2026-05-10 05:00 | Yokohama F Marinos vs Kashima Antlers | japan-jleague | odds_api_io_events
- 2026-05-11 20:15 | Benfica vs Sp Braga | P1 | football_data_fixtures_proxy
- 2026-05-11 20:15 | Estrela vs Famalicao | P1 | football_data_fixtures_proxy
- 2026-05-11 20:15 | Gil Vicente vs Arouca | P1 | football_data_fixtures_proxy
- 2026-05-11 20:15 | Guimaraes vs Casa Pia | P1 | football_data_fixtures_proxy
- 2026-05-11 19:30 | Huesca vs Sociedad B | SP2 | football_data_fixtures_proxy
- 2026-05-11 19:45 | Napoli vs Bologna | serie_a | football_data_fixtures_proxy
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon | P1 | football_data_fixtures_proxy
- 2026-05-11 20:15 | Santa Clara vs Nacional | P1 | football_data_fixtures_proxy
- 2026-05-11 20:15 | Tondela vs Moreirense | P1 | football_data_fixtures_proxy
- 2026-05-11 20:00 | Tottenham vs Leeds | premier_league | football_data_fixtures_proxy
- 2026-05-11 20:00 | Vallecano vs Girona | la_liga | football_data_fixtures_proxy
- 2026-05-11 07:00 | Vietnam vs Australia | international-youth-u17-afc-asian-cup-women | odds_api_io_events

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 19
Rows with complete odds: 0
- 2026-05-09 23:30 | Guapore  RO vs Galvez EC AC | bookmaker=bet365_manual
- 2026-05-10 20:00 | Aguia de Maraba FC PA vs Oratorio RC AP | bookmaker=bet365_manual
- 2026-05-10 12:00 | FC Aktobe vs Kaisar Kyzylorda | bookmaker=bet365_manual
- 2026-05-10 07:30 | Kwun Tong vs Hoi King | bookmaker=bet365_manual
- 2026-05-10 13:00 | Pas Pyrgos vs APS Zakynthos | bookmaker=bet365_manual
- 2026-05-10 19:00 | Real San Joaquin vs Deportes Colina | bookmaker=bet365_manual
- 2026-05-10 05:00 | Yokohama F Marinos vs Kashima Antlers | bookmaker=bet365_manual
- 2026-05-11 20:15 | Benfica vs Sp Braga | bookmaker=bet365_manual
- 2026-05-11 20:15 | Estrela vs Famalicao | bookmaker=bet365_manual
- 2026-05-11 20:15 | Gil Vicente vs Arouca | bookmaker=bet365_manual
- 2026-05-11 20:15 | Guimaraes vs Casa Pia | bookmaker=bet365_manual
- 2026-05-11 19:30 | Huesca vs Sociedad B | bookmaker=bet365_manual
- 2026-05-11 19:45 | Napoli vs Bologna | bookmaker=bet365_manual
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon | bookmaker=bet365_manual
- 2026-05-11 20:15 | Santa Clara vs Nacional | bookmaker=bet365_manual
- 2026-05-11 20:15 | Tondela vs Moreirense | bookmaker=bet365_manual
- 2026-05-11 20:00 | Tottenham vs Leeds | bookmaker=bet365_manual
- 2026-05-11 20:00 | Vallecano vs Girona | bookmaker=bet365_manual
- 2026-05-11 07:00 | Vietnam vs Australia | bookmaker=bet365_manual

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
- 2026-05-09 23:30 | Guapore  RO vs Galvez EC AC
- 2026-05-10 20:00 | Aguia de Maraba FC PA vs Oratorio RC AP
- 2026-05-10 12:00 | FC Aktobe vs Kaisar Kyzylorda
- 2026-05-10 07:30 | Kwun Tong vs Hoi King
- 2026-05-10 13:00 | Pas Pyrgos vs APS Zakynthos
- 2026-05-10 19:00 | Real San Joaquin vs Deportes Colina
- 2026-05-10 05:00 | Yokohama F Marinos vs Kashima Antlers
- 2026-05-11 20:15 | Benfica vs Sp Braga
- 2026-05-11 20:15 | Estrela vs Famalicao
- 2026-05-11 20:15 | Gil Vicente vs Arouca
- 2026-05-11 20:15 | Guimaraes vs Casa Pia
- 2026-05-11 19:30 | Huesca vs Sociedad B
- 2026-05-11 19:45 | Napoli vs Bologna
- 2026-05-11 20:15 | Rio Ave vs Sp Lisbon
- 2026-05-11 20:15 | Santa Clara vs Nacional
- 2026-05-11 20:15 | Tondela vs Moreirense
- 2026-05-11 20:00 | Tottenham vs Leeds
- 2026-05-11 20:00 | Vallecano vs Girona
- 2026-05-11 07:00 | Vietnam vs Australia

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 15
Valid forward/proxy log rows: 12
Valid automatic proxy observation rows: 12
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Valid rows
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
## Invalid rows excluded
- 25/05/2025 | Liverpool vs Crystal Palace | phase=historical_proxy_research
- 25/05/2025 | Fulham vs Man City | phase=historical_proxy_research
- 25/05/2025 | Southampton vs Arsenal | phase=historical_proxy_research

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
### Tottenham vs Leeds
- Date/time: 2026-05-11 20:00
- League/phase: premier_league / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 4.1
- Fair odds: 3.17
- Model probability: 0.3152
- Probability band: 0.00-0.35
- EV: 0.2923
- Probability edge: 0.0713
- Alignment penalty: 0.2923
- Suppression action: proxy_suppressed_band_observe_only
- Paper tier: suppressed_band_proxy_observation
- Paper score: 0.1299
- Prediction ID: 7b65a9bf28de71b10d96
### Tottenham vs Leeds
- Date/time: 2026-05-11 20:00
- League/phase: premier_league / automatic_forward_price_proxy
- Selection: AWAY
- Market odds: 3.92
- Fair odds: 3.17
- Model probability: 0.3152
- Probability band: 0.00-0.35

## paper_test_picks

# Paper Test Picks
Observation-only picks. These are not real-money recommendations.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Suppressed historical bands may be tracked only as proxy observation and remain excluded from real-money readiness.
Source used: automatic_forward_value_snapshots
Current paper-test picks: 7
Newly logged paper-test picks: 0
Total logged paper-test rows: 15
- Tottenham vs Leeds | selection=AWAY | odds=4.1 | prob=0.3152 | EV=0.2923 | edge=0.0713 | penalty=0.2923 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Tottenham vs Leeds | selection=AWAY | odds=3.92 | prob=0.3152 | EV=0.2356 | edge=0.0601 | penalty=0.2356 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Tottenham vs Leeds | selection=AWAY | odds=3.75 | prob=0.3152 | EV=0.182 | edge=0.0485 | penalty=0.182 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Napoli vs Bologna | selection=DRAW | odds=4.2 | prob=0.2843 | EV=0.1941 | edge=0.0462 | penalty=0.1941 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Napoli vs Bologna | selection=DRAW | odds=4.2 | prob=0.2843 | EV=0.1941 | edge=0.0462 | penalty=0.1941 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Napoli vs Bologna | selection=DRAW | odds=4.01 | prob=0.2843 | EV=0.14 | edge=0.0349 | penalty=0.14 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Vallecano vs Girona | selection=AWAY | odds=3.05 | prob=0.3376 | EV=0.0297 | edge=0.0097 | penalty=0.0297 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation

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
