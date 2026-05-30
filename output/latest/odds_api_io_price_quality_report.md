# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 57
Rejected price rows: 3
Rejected U-/reserve rows: 3
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-30 | Patriotas FC PR vs City London FC PR U20 | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | FC Concordia Basel vs Grasshopper Club Zurich II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | LKS Goczalkowice-Zdroj vs Zaglebie Lubin II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match