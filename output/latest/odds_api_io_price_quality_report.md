# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 43
Accepted price rows: 41
Rejected price rows: 2
Rejected U-/reserve rows: 2
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-16 | Calcio Lecco 1912 U19 vs Pisa Calcio | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Kayserispor vs Konyaspor | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match