# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 51
Rejected price rows: 9
Rejected U-/reserve rows: 9
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-17 | Canberra White Eagles FC vs Canberra Juventus FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-17 | Bulls FC Academy vs Manly United FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-17 | Adelaide Olympic FC Reserve vs Cumberland United Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-17 | Bulls FC Academy U23 vs Manly United FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-17 | Central Coast Mariners Academy vs Hills United FC Brumbies | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-17 | Melbourne Victory FC Youth vs Preston Lions | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-17 | Hills United FC vs Gladesville Ravens | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-17 | Sydney University SFC vs Western Sydney Wanderers Youth | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-17 | Kyrgyzstan vs Afghanistan | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match