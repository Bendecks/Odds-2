# Gemini AI Review

Model used: `gemini-2.0-flash`

1.  Current system status: Negative ROI, negative CLV, poor calibration, research-only. Suppression rules are active. Market alignment is acceptable for experiments.

2.  Biggest weakness: Negative CLV and poor calibration, indicating the model consistently misprices bets relative to the closing line and true probabilities.

3.  Best next development step: Improve calibration by recalibrating probabilities, potentially using isotonic regression or Platt scaling.

4.  Readiness: Paper-test-ready.

5.  Concrete change to prioritize next: Implement isotonic regression to recalibrate predicted probabilities.
