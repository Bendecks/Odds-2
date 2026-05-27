# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: ev_above_real_candidate_cap_possible_overconfidence
Real-money ready: False

## Blocker summary

- ev_above_real_candidate_cap_possible_overconfidence: 7
- market_alignment_penalty_too_high_for_real_candidate: 7
- watchlist_only_pending_forward_settlement: 4
- probability_or_league_rule_suppressed: 4
- low_probability_band_under_0_35: 4
- edge_below_candidate_threshold: 1

## Row explanations

- 2026-05-27 | JK Tallinna Kalev vs Viimsi JK | sel=HOME | score=0.2633 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | CA Defensores Unidos vs Villa Dalmine | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | HJK Klubi 04 vs PK-35 Helsinki | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Al-Merrikh SC (SDN) vs Apr FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | VVSB Noordwijkerhout vs Excelsior Maassluis | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | IF Vestri vs UMF Njardvik | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-27 | ADO 20 Heemskerk vs FC Lisse | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-27 | VfB Hohenems vs FC Lauterach | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Heips RJ vs Coritiba FC PR | sel=DRAW | score=0.1145 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Newroz SC vs AL Mosul SC | sel=AWAY | score=0.1139 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-27 | Tampereen Ilves vs Turun Palloseura | sel=DRAW | score=0.1118 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration