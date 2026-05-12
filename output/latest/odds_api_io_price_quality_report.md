# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a forward prediction home/away/date.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 10
Accepted price rows: 10
Rejected price rows: 0
Forward prediction rows: 80
Rule: accept_only_direct_home_away_match_against_forward_fixture_predictions

No rejected prices.