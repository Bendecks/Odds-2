# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 8
Explained rows: 8
Distinct blockers: 6
Top blocker: delayed_football_data_proxy_not_fresh_api_price
Real-money ready: False

## Blocker summary

- delayed_football_data_proxy_not_fresh_api_price: 8
- probability_or_league_rule_suppressed: 7
- low_probability_band_under_0_35: 7
- ev_above_real_candidate_cap_possible_overconfidence: 2
- market_alignment_penalty_too_high_for_real_candidate: 2
- edge_below_candidate_threshold: 2

## Row explanations

- 2026-05-21 | Gent vs St. Gilloise | sel=HOME | score=0.1903 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Mechelen vs Club Brugge | sel=DRAW | score=0.1025 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Kifisia vs Larisa | sel=AWAY | score=0.0947 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Anderlecht vs St Truiden | sel=AWAY | score=0.0932 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Panetolikos vs Asteras Tripolis | sel=AWAY | score=0.0924 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Atromitos vs Panserraikos | sel=DRAW | score=0.0908 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Gent vs St. Gilloise | sel=DRAW | score=0.0886 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-21 | Anderlecht vs St Truiden | sel=DRAW | score=0.0881 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available