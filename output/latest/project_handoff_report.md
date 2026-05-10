# Project Handoff Report

Generated UTC: 2026-05-10T20:36:00.094407+00:00

## Core system status

- system_readiness_report.csv: readiness_score=40, readiness_status=observation_only
- forward_test_readiness_report.csv: forward_test_status=observe_only, leakage_risk=medium, sample_usage=paper_tracking_only, system_readiness=observation_only
- clv_trend_report.csv: rows=189, avg_clv_delta=-0.7976, beat_closing_line_rate=0.4286, positive_clv_rows=81, negative_clv_rows=108
- probability_band_report.csv: band=0.30-0.40, bets=11, actual_win_rate=0.3636, avg_probability=0.3447, avg_roi=0.1727
- model_adjustment_recommendation.csv: flags=6, recommendations=4, top_recommendation=Reduce confidence in favorites and add extra shrinkage above 0.50 probability.
- sample_reliability_report.csv: settled_predictions=189, reliability_level=low, recommended_usage=paper_tracking_only

## Current strategic focus

- Improve CLV performance.
- Reduce probability overconfidence.
- Continue collecting settled predictions.
- Separate historical proxy research from real forward-testing.
- Improve calibration before adding major model complexity.