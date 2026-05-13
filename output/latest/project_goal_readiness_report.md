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

### forward_probability_calibration
Status: `not_ready`
Target: Settled forward rows available for Brier/accuracy/calibration review.
Current: 0 settled forward rows.
Done when: 20+ settled rows for first weak signal; 100+ for meaningful calibration.

### real_money_readiness
Status: `not_ready`
Target: Stable positive CLV, calibrated probabilities and reliable fresh odds.
Current: No real-money gate is open; candidate bets remain 0.
Done when: Positive/neutral CLV over forward sample, stable calibration, and fresh odds source verified.

## Practical definition of done

The project is not in goal when it can generate one exciting pick. It is in goal when it can repeatedly produce deduped forward observations, settle them, and show that calibration and market alignment are not obviously bad.

Minimum paper-test goal:
- 50+ deduped forward/proxy observations logged
- 20+ settled forward observations
- no duplicate fixture inflation
- proxy source clearly separated from real-money readiness

Real-money goal remains much stricter:
- 100+ settled forward observations
- stable calibration/Brier trend
- non-negative CLV/market alignment trend
- fresh odds source verified, not only delayed proxy
- candidate bet gate can remain 0 until these are met

Next goal: Increase fresh API price coverage carefully, use deduped paper-test counts, settle forward rows, and improve model-covered league filtering.