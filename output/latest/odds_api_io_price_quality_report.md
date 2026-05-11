# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a forward prediction home/away/date.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 1
Accepted price rows: 0
Rejected price rows: 1
Forward prediction rows: 80
Rule: accept_only_direct_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-13 | SC Braga vs Benfica Lisboa | odds_api_io_1xbet_3-Way Result | status=rejected_no_direct_forward_prediction_match