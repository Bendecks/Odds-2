# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 58
Rejected price rows: 2
Rejected U-/reserve rows: 2
Forward prediction rows: 234
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-20 | Sydney Olympic FC vs University of NSW | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-20 | de Graafschap vs ADO Den Haag | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match