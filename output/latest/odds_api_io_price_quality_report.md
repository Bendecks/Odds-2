# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 59
Accepted price rows: 54
Rejected price rows: 5
Rejected U-/reserve rows: 5
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-29 | Blacktown Spartans FC vs Western City Rangers FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-29 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-29 | Spring Hills FC vs Melbourne City Youth | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-29 | Itabirito FC MG vs AE Uberabinha MG | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-29 | Atletico Mineiro MG vs Chapecoense SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match