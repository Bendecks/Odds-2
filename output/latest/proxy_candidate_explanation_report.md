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
- watchlist_only_pending_forward_settlement: 3
- delayed_football_data_proxy_not_fresh_api_price: 2
- edge_below_candidate_threshold: 1

## Row explanations

- 2026-05-17 | Houston Dynamo vs Vancouver Whitecaps FC | sel=HOME | score=0.2649 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Fort Wayne FC vs Indy Eleven | sel=HOME | score=0.2549 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Lagarto FC SE vs CS Sergipe SE | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-17 | Corpus Christi FC vs FC Tulsa | sel=HOME | score=0.2477 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Chattanooga Red Wolves SC vs Birmingham Legion FC | sel=HOME | score=0.2439 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration
- 2026-05-16 | Point Michel vs Middleham United FC | sel=HOME | score=0.236 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-17 | Deportes Limache vs CD Universidad Catolica | sel=HOME | score=0.2308 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | Falkirk vs Rangers | sel=HOME | score=0.2276 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-17 | Oakland Roots SC vs Sacramento Republic FC | sel=HOME | score=0.2275 | blockers=watchlist_only_pending_forward_settlement | improve=monitor until settled forward sample is large enough
- 2026-05-16 | Ceuta vs Malaga | sel=HOME | score=0.2257 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-16 | Floresta EC CE vs Amazonas FC AM | sel=HOME | score=0.223 | blockers=edge_below_candidate_threshold | improve=needs stronger model-vs-market edge
- 2026-05-17 | FC Western vs Upper Hutt City FC | sel=HOME | score=0.2223 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration