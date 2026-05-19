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
- watchlist_only_pending_forward_settlement: 5
- probability_or_league_rule_suppressed: 3
- low_probability_band_under_0_35: 3
- edge_below_candidate_threshold: 1

## Row explanations

- 2026-05-19 | Qingdao West Coast FC vs Beijing Guoan | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Hapoel Ra`anana FC vs FC Kafr Qasim | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Hapoel Nof Hagalil FC vs Ironi Modiin | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | AS Korofina vs Binga FC | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | Rtc FC vs Paro FC | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | Tianjin Jinmen Tiger vs Henan | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | Helsingborgs IF vs Varbergs BoIS | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-19 | Murdoch University Melville FC vs Joondalup City | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-19 | Boston Bolts vs Vermont Green FC | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Rajasthan United vs Chanmari FC | sel=AWAY | score=0.1201 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Hapoel Petah Tikva FC vs Beitar Jerusalem FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-19 | Boston Bolts vs Vermont Green FC | sel=DRAW | score=0.1171 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration