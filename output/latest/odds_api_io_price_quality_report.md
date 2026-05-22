# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 53
Rejected price rows: 7
Rejected U-/reserve rows: 7
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-22 | Auckland FC Reserves vs Eastern Suburbs AFC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-22 | Northcote City FC vs Brunswick City SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-22 | West Adelaide Reserve vs Flinders United Wfc Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-22 | Salisbury Inter Reserve vs Adelaide Comets FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-22 | Gornik Zabrze II vs KS Gornik Polkowice | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-22 | Zaglebie Lubin II vs Miedz Legnica II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-22 | FC Pakhtakor Tashkent II vs FC Yaypan Fergana | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match