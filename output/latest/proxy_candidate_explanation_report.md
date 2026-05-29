# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: ev_above_real_candidate_cap_possible_overconfidence
Real-money ready: False

## Blocker summary

- ev_above_real_candidate_cap_possible_overconfidence: 6
- market_alignment_penalty_too_high_for_real_candidate: 6
- watchlist_only_pending_forward_settlement: 3
- edge_below_candidate_threshold: 3
- probability_or_league_rule_suppressed: 1
- low_probability_band_under_0_35: 1

## Row explanations

- 2026-05-29 | FK Babrungas Plunge vs FK Minija 2017 | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | TPV Tampere vs Tampere United | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Deportes Temuco vs Santiago Wanderers | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | HPS vs Kuopion Palloseura | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Hoersholm-Usseroed IK vs FA 2000 | sel=HOME | score=0.2458 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-29 | Aragvi Dusheti vs FC Merani Martvili | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | Kungsangens IF vs IK Franke | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | Nacka FC vs Nykopings BIS | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-29 | Fehring 1947 vs SV Lebring | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | KFUM Oslo vs Tromsoe IL | sel=HOME | score=0.2253 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | Hinna vs Varhaug | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-29 | FK Transinvest vs FC Hegelmann Kaunas | sel=AWAY | score=0.1244 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration