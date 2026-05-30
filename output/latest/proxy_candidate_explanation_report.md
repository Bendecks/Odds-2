# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: ev_above_real_candidate_cap_possible_overconfidence
Real-money ready: False

## Blocker summary

- ev_above_real_candidate_cap_possible_overconfidence: 8
- market_alignment_penalty_too_high_for_real_candidate: 8
- watchlist_only_pending_forward_settlement: 2
- edge_below_candidate_threshold: 2
- probability_or_league_rule_suppressed: 1
- low_probability_band_under_0_35: 1

## Row explanations

- 2026-05-30 | Bunnys Gunma FC White Star vs Diavorosso Hiroshima | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | Nara Club vs Oita Trinita | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | FC Gangneung vs Changwon FC | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | Nagoya Grampus vs Machida Zelvia | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | Moreland City FC vs Eastern Lions SC | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-30 | South Adelaide FC vs Eastern United | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-30 | Gold Coast United FC vs Peninsula Power | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | O'Connor Knights SC vs Queanbeyan City FC | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | Adelaide Croatia Raiders SC Reserve vs Modbury Jets SC Reserve | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | O'Connor Knights FC vs Queanbeyan City FC | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | Adelaide Croatia Raiders SC vs Modbury Jets SC | sel=HOME | score=0.212 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | Vegalta Sendai vs Ventforet Kofu | sel=AWAY | score=0.1201 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration