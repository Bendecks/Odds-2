# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 4
Top blocker: watchlist_only_pending_forward_settlement
Real-money ready: False

## Blocker summary

- watchlist_only_pending_forward_settlement: 6
- ev_above_real_candidate_cap_possible_overconfidence: 3
- market_alignment_penalty_too_high_for_real_candidate: 3
- edge_below_candidate_threshold: 3

## Row explanations

- 2026-05-30 | IK Kongahalla vs Astorps FF | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | NK BSK Bijelo Brdo vs NK Croatia Zmijavci | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | CS Minerul Lupeni vs CSM Unirea Alba Iulia | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-30 | FC Lausanne Sports vs FC Schaffhausen | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | SC Cham vs FC Biel-Bienne | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | Moss FK vs Stabaek IF | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | NK Varteks vs NK Segesta | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | ASKO Kottmannsdorf vs SVG Bleiburg | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | ASKO Kohfidisch vs SV Leithaprodersdorf | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-30 | Bollstanas SK vs Sunnersta AIF | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-30 | AD Ceuta vs Albacete Balompie | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-30 | Ceuta vs Albacete | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge