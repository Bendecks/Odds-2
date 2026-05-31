# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 52
Rejected price rows: 8
Rejected U-/reserve rows: 8
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-31 | Bulls FC Academy vs Western City Rangers FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-31 | Broadmeadow Magic FC Reserve vs Lambton Jaffas FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-31 | Sydney United 58 FC vs Sutherland Sharks FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-31 | ST Albans Saints Dinamo SC vs Preston Lions FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-31 | West Adelaide SC Reserve vs Adelaide City FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-31 | Heidelberg United FC vs Dandenong Thunder FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-31 | Sydney Olympic FC vs Western Sydney Wanderers Youth | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-31 | Prospect United vs Northern Tigers FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match