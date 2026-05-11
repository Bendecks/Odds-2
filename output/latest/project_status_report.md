# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-11T09:19:38.789236+00:00`
GitHub run: `232` attempt `1`
GitHub SHA: `9b32185e40733efb4709eb8aab8bd61d11ec8cda`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| Football-Data upcoming odds proxy | True | 405 |  |  |
| Football-Data upcoming odds status | True | 1 |  |  |
| Automatic forward value snapshots | True | 9 |  |  |
| Automatic forward value snapshot summary | True | 1 |  |  |
| Automatic forward value match diagnostics | True | 1 |  |  |
| Proxy observation quality report | True | 1 |  |  |
| Proxy observation by selection | True | 2 |  |  |
| Upcoming fixtures | True | 1 |  |  |
| Forward fixture results | True | 1 |  |  |
| Forward fixture result status | True | 1 |  |  |
| Forward probability calibration report | True | 1 |  |  |
| Forward probability calibration summary | True | 1 |  |  |
| Automatic forward source report | True | 1 |  |  |
| Automatic forward prices | True | 405 |  |  |
| Forward price source adapter | True | 1 |  |  |
| Fixture model match report | True | 2 |  |  |
| Fixture model match summary | True | 1 |  |  |
| Forward fixture predictions | True | 1 |  |  |
| Forward fixture prediction summary | True | 1 |  |  |
| Forward fixture prediction log | True | 1 |  |  |
| Forward fixture prediction log status | True | 1 |  |  |
| Manual odds template | True | 1 |  |  |

## football_data_upcoming_odds

# Football-Data Upcoming Odds Proxy
Free delayed market proxy. Not live odds and not real-money ready.
Raw rows: 135
Proxy price rows: 405
Sources attempted: 1
Errors: 0
- 08/05/2026 19:45 | Standard vs Oud-Heverlee Leuven | football_data_bet365_proxy | 2.0/3.5/3.5
- 08/05/2026 19:45 | Standard vs Oud-Heverlee Leuven | football_data_max_market_proxy | 2.07/3.5/3.66
- 08/05/2026 19:45 | Standard vs Oud-Heverlee Leuven | football_data_average_market_proxy | 2.01/3.41/3.48
- 09/05/2026 15:00 | RAAL La Louviere vs Cercle Brugge | football_data_bet365_proxy | 3.1/3.3/2.15
- 09/05/2026 15:00 | RAAL La Louviere vs Cercle Brugge | football_data_max_market_proxy | 3.2/3.6/2.2
- 09/05/2026 15:00 | RAAL La Louviere vs Cercle Brugge | football_data_average_market_proxy | 3.06/3.45/2.16
- 09/05/2026 15:00 | Waregem vs Dender | football_data_bet365_proxy | 1.55/3.9/5.5
- 09/05/2026 15:00 | Waregem vs Dender | football_data_max_market_proxy | 1.6/4.35/5.8
- 09/05/2026 15:00 | Waregem vs Dender | football_data_average_market_proxy | 1.54/4.1/5.38
- 09/05/2026 19:45 | Club Brugge vs St Truiden | football_data_bet365_proxy | 1.45/4.5/5.5
- 09/05/2026 19:45 | Club Brugge vs St Truiden | football_data_max_market_proxy | 1.53/4.75/6.0
- 09/05/2026 19:45 | Club Brugge vs St Truiden | football_data_average_market_proxy | 1.47/4.6/5.5
- 10/05/2026 12:30 | Gent vs Anderlecht | football_data_bet365_proxy | 2.3/3.4/2.75
- 10/05/2026 12:30 | Gent vs Anderlecht | football_data_max_market_proxy | 2.45/3.6/2.9
- 10/05/2026 12:30 | Gent vs Anderlecht | football_data_average_market_proxy | 2.34/3.43/2.75
- 10/05/2026 15:00 | Antwerp vs Charleroi | football_data_bet365_proxy | 2.3/3.2/2.9
- 10/05/2026 15:00 | Antwerp vs Charleroi | football_data_max_market_proxy | 2.37/3.35/3.2
- 10/05/2026 15:00 | Antwerp vs Charleroi | football_data_average_market_proxy | 2.28/3.25/2.97
- 10/05/2026 17:30 | St. Gilloise vs Mechelen | football_data_bet365_proxy | 1.33/4.5/8.0
- 10/05/2026 17:30 | St. Gilloise vs Mechelen | football_data_max_market_proxy | 1.36/5.5/11.5
- 10/05/2026 17:30 | St. Gilloise vs Mechelen | football_data_average_market_proxy | 1.31/5.06/8.7
- 10/05/2026 18:15 | Genk vs Westerlo | football_data_bet365_proxy | 1.6/4.0/4.5
- 10/05/2026 18:15 | Genk vs Westerlo | football_data_max_market_proxy | 1.67/4.5/5.2
- 10/05/2026 18:15 | Genk vs Westerlo | football_data_average_market_proxy | 1.6/4.16/4.63

## automatic_forward_source

# Automatic Forward Source Report
Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data fixture odds are treated as delayed/free proxy prices: paper-test only, never real-money ready.
Upcoming fixture rows: 1
Fixture team rows checked: 2
Fixture team rows unmatched: 0
Ready for model-fixture join: True
Configured forward sources: 1
Enabled forward sources: 1
Automatic forward price rows: 405
Automatic forward status: automatic_forward_proxy_available
Blocker: none_for_proxy_testing
Next development step: evaluate_proxy_value_snapshots_and_paper_filters
## Team matching
All fixture teams match the model team table.
## Interpretation
Automatic delayed proxy prices are available. Use only for paper-test/proxy observation, not real money.

## automatic_forward_value_snapshots

# Automatic Forward Value Snapshots
Delayed/free market proxy joined to forward probability predictions.
Not live odds, not Bet365 direct, and not real-money ready.
Forward prediction rows: 1
Proxy price rows: 405
Matched prediction rows: 1
Value snapshot rows: 9
Positive EV rows: 5
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=AWAY | src=football_data_max_market_proxy | odds=4.1 | prob=0.3152 | EV=0.29232 | match=1.0
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=AWAY | src=football_data_average_market_proxy | odds=3.92 | prob=0.3152 | EV=0.235584 | match=1.0
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=AWAY | src=football_data_bet365_proxy | odds=3.75 | prob=0.3152 | EV=0.182 | match=1.0
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=DRAW | src=football_data_max_market_proxy | odds=4.1 | prob=0.259 | EV=0.0619 | match=1.0
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=DRAW | src=football_data_bet365_proxy | odds=4.1 | prob=0.259 | EV=0.0619 | match=1.0
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=DRAW | src=football_data_average_market_proxy | odds=3.82 | prob=0.259 | EV=-0.01062 | match=1.0
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=HOME | src=football_data_max_market_proxy | odds=1.86 | prob=0.4257 | EV=-0.208198 | match=1.0
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=HOME | src=football_data_bet365_proxy | odds=1.83 | prob=0.4257 | EV=-0.220969 | match=1.0
- 2026-05-11 | Tottenham Hotspur vs Leeds United | sel=HOME | src=football_data_average_market_proxy | odds=1.82 | prob=0.4257 | EV=-0.225226 | match=1.0

## proxy_observation_quality

# Proxy Observation Quality Report
Quality diagnostics for automatic delayed-market proxy paper observations.
This is not real-money ready and does not override suppression rules for candidate bets.
Value snapshot rows: 9
Paper proxy observation rows: 5
Positive EV value rows: 5
Suppressed-band observation rows: 5
Distinct matches: 1
Distinct sources: 0
Max EV: 0.29232
Average EV: 0.166741
Max probability edge: 0.071298
Average match confidence: None
## By selection
- away: rows=3, avg_ev=0.2366, max_ev=0.2923
- draw: rows=2, avg_ev=0.0619, max_ev=0.0619

## forward_fixture_predictions

# Forward Fixture Predictions
Probability-only forward fixture model output. Not a betting card and not a real-money recommendation.
Upcoming fixture rows: 1
Forward fixture prediction rows: 1
Ready for price join: True
- 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United | H=0.4257 D=0.259 A=0.3152 | fair=2.35/3.86/3.17

## forward_fixture_prediction_log

# Forward Fixture Prediction Log
Probability-only forward prediction log. This is not a betting log and contains no stake or real-money signal.
Current forward fixture predictions: 1
New forward fixture predictions logged: 0
Total forward fixture predictions logged: 1
Log type: probability_only_no_market_prices
- 2026-05-11 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United | H=0.4257 D=0.259 A=0.31520000000000004

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
Upcoming fixtures: 1
Manual template rows: 1
Rows with complete manual odds: 0
Rows missing manual odds: 1
Manual forward snapshot rows: 0
Manual odds mode: optional_fallback_paused
Manual odds is blocker: False
Automatic forward source needed: True
## Current automatic-forward blocker
Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.
## Optional manual fallback status
Manual odds are not required in the current phase. These rows are only kept for later fallback use:
- 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United

## upcoming_fixtures

# Upcoming Fixtures
Fixture source: TheSportsDB eventsnextleague API.
Primary development target: automatic/free delayed market proxy, not manual Bet365.
Fixtures found: 1
- 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United | premier_league

## manual_odds_template

# Manual Odds Template
Use this only for forward paper-testing. Do not use for real-money betting.
Existing filled odds are preserved when fixtures refresh.
Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV or run the workflow manually.
Template rows: 1
Rows with complete odds: 0
- 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United | bookmaker=bet365_manual

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
- 2026-05-11 19:00:00 | Tottenham Hotspur vs Leeds United
## After filling odds
Run the workflow again. Expected result:
- `manual_forward_snapshots` becomes greater than 0
- `paper_test_picks` may become greater than 0
- `candidate_bets` may still remain 0, which is acceptable

## manual_forward_snapshots

# Manual Forward Snapshots
Built from manually captured pre-match odds. Observation-only; not real-money recommendations.
Forward snapshot rows: 0
No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.

## paper_test_log_status

# Paper Test Log Status
Raw log rows: 8
Valid forward/proxy log rows: 5
Valid automatic proxy observation rows: 5
Invalid historical/proxy log rows excluded: 3
Has valid forward log: True
## Valid rows
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=away | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
- 2026-05-11 | Tottenham Hotspur vs Leeds United | selection=draw | phase=automatic_forward_price_proxy | tier=suppressed_band_proxy_observation
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
### Tottenham Hotspur vs Leeds United
- Date/time: 2026-05-11 19:00:00
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
- Prediction ID: a34fb57cd5c2b5199b69
### Tottenham Hotspur vs Leeds United
- Date/time: 2026-05-11 19:00:00
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
Current paper-test picks: 5
Newly logged paper-test picks: 0
Total logged paper-test rows: 8
- Tottenham Hotspur vs Leeds United | selection=AWAY | odds=4.1 | prob=0.3152 | EV=0.2923 | edge=0.0713 | penalty=0.2923 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Tottenham Hotspur vs Leeds United | selection=AWAY | odds=3.92 | prob=0.3152 | EV=0.2356 | edge=0.0601 | penalty=0.2356 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Tottenham Hotspur vs Leeds United | selection=AWAY | odds=3.75 | prob=0.3152 | EV=0.182 | edge=0.0485 | penalty=0.182 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Tottenham Hotspur vs Leeds United | selection=DRAW | odds=4.1 | prob=0.259 | EV=0.0619 | edge=0.0151 | penalty=0.0619 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation
- Tottenham Hotspur vs Leeds United | selection=DRAW | odds=4.1 | prob=0.259 | EV=0.0619 | edge=0.0151 | penalty=0.0619 | band=0.00-0.35 | rule=proxy_suppressed_band_observe_only | tier=suppressed_band_proxy_observation

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
