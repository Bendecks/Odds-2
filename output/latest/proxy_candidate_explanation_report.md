# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 10
Explained rows: 10
Distinct blockers: 5
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False

## Blocker summary

- market_alignment_penalty_too_high_for_real_candidate: 7
- probability_or_league_rule_suppressed: 7
- low_probability_band_under_0_35: 7
- ev_above_real_candidate_cap_possible_overconfidence: 5
- edge_below_candidate_threshold: 2

## Row explanations

- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | sel=AWAY | score=0.1087 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35 | improve=collect settled forward results before trusting low-probability selections
- 2026-05-12 | Gwangju FC vs FC Seoul | sel=DRAW | score=0.1084 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; needs better market alignment or stricter probability calibration
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | sel=DRAW | score=0.1084 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; needs better market alignment or stricter probability calibration
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | sel=AWAY | score=0.1044 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | sel=DRAW | score=0.1034 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge