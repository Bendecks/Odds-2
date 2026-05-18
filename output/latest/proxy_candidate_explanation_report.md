# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False

## Blocker summary

- market_alignment_penalty_too_high_for_real_candidate: 10
- ev_above_real_candidate_cap_possible_overconfidence: 7
- watchlist_only_pending_forward_settlement: 1
- edge_below_candidate_threshold: 1
- probability_or_league_rule_suppressed: 1
- low_probability_band_under_0_35: 1

## Row explanations

- 2026-05-18 | GIF Sundsvall vs Landskrona BoIS | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Bahla Club vs Al Nahda | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Ghazl El Mahallah vs Al Ittihad Al Sakandary | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Al Shabab vs Al-Seeb | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-18 | Ibri vs Dhofar SCSC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-18 | Puszcza Niepolomice vs LKS Lodz | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-18 | SJK Akatemia/2 vs VPS Akatemia | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-18 | Waterford FC vs Drogheda United FC | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-18 | AB Argir vs Vikingur Gota | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Laholms FK vs FC Rosengaard 1917 | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | Orgryte IS vs IFK Goteborg | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-18 | CS Italiano vs CSCD Laferrere | sel=AWAY | score=0.123 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration