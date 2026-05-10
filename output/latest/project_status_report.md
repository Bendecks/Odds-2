# Project Status Report

This file is the main AI-readable summary of the current Odds-2 system state.

## free_data_status

# Free Data Source Status
Generated UTC: `2026-05-10T20:07:05.227603+00:00`
GitHub run: `114` attempt `1`
GitHub SHA: `727af59d918eefaf4943e7b3ceeff741d9b0d353`
Overall status: `OK`
| Source | OK | Rows | Missing columns | Error |
|---|---:|---:|---|---|
| football-data.co.uk Premier League 24/25 | True | 380 |  |  |
| ClubElo latest snapshot | True | 630 |  |  |
| Basic team strength model | True | 119 |  |  |
| Poisson predictions | True | 7 |  |  |
| Expected value calculations | True | 7 |  |  |
| Prediction log output | True | 189 |  |  |
| Settled predictions output | True | 189 |  |  |

## betting_performance

# Betting Performance Report
Readiness: research-only
Recommendation: NO REAL MONEY - continue research
Total predictions: 189
Historical candidate predictions: 86
Current candidate bets: 1
Settled predictions: 189
Wins: 63
Total ROI units: -1.8
Average ROI per bet: -0.0095
Beat closing line rate: 0.4286
Average CLV delta: -0.7976
## Interpretation
The model is not ready for real-money betting. Focus remains on CLV improvement, calibration and realistic market snapshots.

## model_health

# Model Health Report
Model state: not_beating_market
Largest problem: negative_clv
Recommended focus: improve calibration and snapshots
Tracked CLV rows: 189
Settled predictions: 189

## daily_betting_card

# Daily Betting Card
Status: research/paper-test only. No real-money recommendation yet.
## Liverpool vs Crystal Palace
- Date/time: 25/05/2025 2026-05-10 16:00:00
- Selection: HOME
- Market: 1X2
- Market odds: 2.67
- Fair odds: 2.17
- Model probability: 0.4611
- EV: 0.2311
- Signal strength: 0.2842
- Prediction ID: 1e63a316578345cf188d
## Snapshot summary
Snapshot rows: 21
Candidate rows: 1

## market_alignment

# Market Alignment Report
Total usable rows: 21
Average alignment gap: 0.1052
Median alignment gap: 0.0866
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
Max probability: 0.5771
Min probability: 0.1974
Std probability: 0.1026
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
