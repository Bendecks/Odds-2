# Proxy Candidate Explanation Report

Explains why proxy candidate observations are not promoted to real candidate bets.
This report is paper/proxy-only and never real-money ready.

Proxy candidate rows: 12
Explained rows: 12
Distinct blockers: 6
Top blocker: delayed_football_data_proxy_not_fresh_api_price
Real-money ready: False

## Blocker summary

- delayed_football_data_proxy_not_fresh_api_price: 12
- probability_or_league_rule_suppressed: 11
- low_probability_band_under_0_35: 11
- ev_above_real_candidate_cap_possible_overconfidence: 8
- market_alignment_penalty_too_high_for_real_candidate: 8
- edge_below_candidate_threshold: 3

## Row explanations

- 2026-05-11 | Estrela vs Famalicao | sel=HOME | score=0.2243 | blockers=ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Tondela vs Moreirense | sel=AWAY | score=0.1066 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Huesca vs Sociedad B | sel=AWAY | score=0.1054 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Santa Clara vs Nacional | sel=AWAY | score=0.1023 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Tottenham vs Leeds | sel=AWAY | score=0.1 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Benfica vs Sp Braga | sel=DRAW | score=0.0986 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Napoli vs Bologna | sel=DRAW | score=0.095 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Guimaraes vs Casa Pia | sel=DRAW | score=0.0908 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Vallecano vs Girona | sel=AWAY | score=0.0904 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Tottenham vs Leeds | sel=DRAW | score=0.0889 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Gil Vicente vs Arouca | sel=DRAW | score=0.0886 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; edge_below_candidate_threshold; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; needs stronger model-vs-market edge; prefer odds-api.io/API-Football fresh price where available
- 2026-05-11 | Gil Vicente vs Arouca | sel=AWAY | score=0.0883 | blockers=probability_or_league_rule_suppressed; low_probability_band_under_0_35; ev_above_real_candidate_cap_possible_overconfidence; market_alignment_penalty_too_high_for_real_candidate; delayed_football_data_proxy_not_fresh_api_price | improve=collect settled forward results before trusting low-probability selections; calibration should reduce overconfident EV spikes; needs better market alignment or stricter probability calibration; prefer odds-api.io/API-Football fresh price where available