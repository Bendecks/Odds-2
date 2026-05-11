# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 4
Explained rows: 4
Distinct blockers: 6
Top blocker: probability_or_league_rule_suppressed
Real-money ready: False

## Blocker summary

- probability_or_league_rule_suppressed: 4
- low_probability_band_under_0_35: 4
- ev_above_real_candidate_cap_possible_overconfidence: 2
- market_alignment_penalty_too_high_for_real_candidate: 2
- edge_below_candidate_threshold: 2
- delayed_football_data_proxy_not_fresh_api_price: 2

## Row explanations

- 2026-05-11 | Tottenham vs Leeds | sel=AWAY | score=0.1196 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-11 | Tottenham vs Leeds | sel=DRAW | score=0.1013 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge
- 2026-05-11 | Napoli vs Bologna | sel=DRAW | score=0.095 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Vallecano vs Girona | sel=AWAY | score=0.0904 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available