# Project Handoff Report

Generated UTC: 2026-05-11T13:26:18.167668+00:00

## Core system status

- system_readiness_report.csv: readiness_score=33, readiness_status=observation_only
- forward_test_readiness_report.csv: forward_test_status=observe_only_with_forward_picks, leakage_risk=medium, sample_usage=paper_tracking_only, system_readiness=observation_only, forward_paper_picks=7
- clv_trend_report.csv: rows=210, avg_clv_delta=-0.8542, beat_closing_line_rate=0.419, positive_clv_rows=88, negative_clv_rows=122, interpretation=negative_clv_signal
- clv_band_report.csv: probability_band=0.00-0.35, rows=39, avg_clv_delta=-1.5456, beat_closing_line_rate=0.2564, avg_ev=-0.007
- probability_calibration_rules.csv: probability_band=0.00-0.35, calibration_action=very_strong_shrink, adjustments=13
- signal_suppression_rules.csv: rule_type=probability_band, target=0.00-0.35, action=suppress, reason=avg_clv_delta=-1.5456 with rows=39
- rule_action_summary.csv: action=monitor, rules=1, targets=0.35-0.45
- phase_performance_report.csv: sample_phase=historical_proxy_research, settled_rows=21, win_rate=0.3333, roi_units=-1.65, avg_roi_per_bet=-0.0786, clv_rows=21
- probability_band_report.csv: band=0.30-0.40, bets=11, actual_win_rate=0.3636, avg_probability=0.3447, avg_roi=0.1727
- model_adjustment_recommendation.csv: flags=9, recommendations=6, suppression_targets=3, top_recommendation=Reduce confidence in favorites and add extra shrinkage above 0.50 probability.
- sample_reliability_report.csv: settled_predictions=210, reliability_level=low, recommended_usage=paper_tracking_only

## Current strategic focus

- Improve CLV performance before relaxing candidate filters.
- Keep probability distribution conservative while CLV is negative.
- Evaluate whether the CLV-band probability calibration layer improves future CLV.
- Use CLV probability-band diagnostics to suppress toxic bands.
- Keep historical proxy research separate from paper forward-testing.
- Use league-specific evaluation only as diagnostics until samples are larger.
- Do not add real-money features.