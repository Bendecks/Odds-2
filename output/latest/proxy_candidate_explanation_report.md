# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 4
Top blocker: market_alignment_penalty_too_high_for_real_candidate
Real-money ready: False

## Blocker summary

- market_alignment_penalty_too_high_for_real_candidate: 8
- ev_above_real_candidate_cap_possible_overconfidence: 3
- watchlist_only_pending_forward_settlement: 3
- edge_below_candidate_threshold: 1

## Row explanations

- 2026-05-22 | Dalian Yingbo B vs Taian Tiankuang | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Ganzhou Ruishi FC vs Shenzhen 2028 FC | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Turan Tovuz vs Sabah Masazir | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Green Gully SC vs Heidelberg United FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-22 | Nepean FC vs South Coast Flame FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-22 | Preston Lions vs Heidelberg United FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-22 | Lanzhou Longyuan Athletic vs Dalian Kewei | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-23 | Green Gully SC vs Heidelberg United FC | sel=HOME | score=0.24 | blockers=market_alignment_penalty_too_high_for_real_candidate | improve=needs better market alignment or stricter probability calibration
- 2026-05-22 | Kingston City FC vs Werribee City FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Hubei Istar vs Chengdu Rongcheng B | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Aris Limassol FC vs AEK Larnaca | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Shahdag Qusar FK vs Baku Sporting | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge