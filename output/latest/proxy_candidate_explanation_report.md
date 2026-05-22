# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 5
Top blocker: ev_above_real_candidate_cap_possible_overconfidence
Real-money ready: False

## Blocker summary

- ev_above_real_candidate_cap_possible_overconfidence: 8
- market_alignment_penalty_too_high_for_real_candidate: 8
- watchlist_only_pending_forward_settlement: 2
- edge_below_candidate_threshold: 2
- delayed_football_data_proxy_not_fresh_api_price: 1

## Row explanations

- 2026-05-22 | Tampereen Ilves vs HPS | sel=HOME | score=0.2616 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Mps vs Leppavaaran Pallo | sel=HOME | score=0.2583 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | FK Radnik Bijeljina vs FK Borac Banja Luka | sel=HOME | score=0.2513 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | FK Jonava vs FK Babrungas Plunge | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | SV Spittal/Drau vs FC Lendorf | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Dakar Sacre Coeur vs Teungueth FC | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Gzs Tluchovia Tluchowo vs Blekitni Stargard | sel=HOME | score=0.2319 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Hestrafors IF vs Jonsereds IF | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-22 | Dfk Dainava Alytus vs Be1 Nfa | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-22 | SJK Akatemia vs FC Haka Valkeakoski | sel=HOME | score=0.2169 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | Al Jazira (UAE) vs Al Ain FC | sel=HOME | score=0.2145 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-22 | ACF Fiorentina vs Atalanta BC | sel=HOME | score=0.1919 | blockers=edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available