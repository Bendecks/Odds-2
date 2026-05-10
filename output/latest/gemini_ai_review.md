# Gemini AI Review

Model used: `gemini-2.0-flash`

1.  **Current system status:** The system is in a research/paper-test phase. It generates predictions with positive EV, but historical ROI is negative, CLV is negative, and market alignment is moderate. The model is not ready for real-money betting.

2.  **Biggest weakness:** Negative CLV, indicating the model is consistently picking bets with worse odds than the closing line. This suggests a timing issue or that the model's edge is eroded by market movement.

3.  **Best next development step:** Improve calibration and market snapshots. Specifically, investigate why the model's implied probabilities differ from market odds and how to capture more accurate odds closer to game time.

4.  **Readiness:** Paper-test-ready

5.  **One concrete change to prioritize next:** Implement a backtesting framework that simulates betting at different times before the match (e.g., 24 hours, 12 hours, 1 hour) to identify the optimal time to place bets and improve CLV.
