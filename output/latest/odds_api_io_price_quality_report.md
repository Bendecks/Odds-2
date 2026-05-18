# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 51
Rejected price rows: 9
Rejected U-/reserve rows: 9
Forward prediction rows: 198
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-18 | NK Samobor vs GNK Dinamo Zagreb | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-18 | AL Qadisiya vs AL Fateh | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-18 | Inter Miami CF II vs Crown Legacy FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-18 | EC Bahia BA vs CA Paranaense PR | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-18 | Liverpool Montevideo vs La Luz FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-18 | Montevideo Wanderers vs Progreso | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-18 | Nacional de Montevideo vs Cerro Largo FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-18 | Penarol Montevideo vs Club Oriental de Football | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-18 | Racing Club Montevideo vs Torque | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match