# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 55
Rejected price rows: 5
Rejected U-/reserve rows: 5
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-14 | SK Sturm Graz II vs Rapid Wien II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-14 | CA Huracan vs Independiente Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-14 | FK Suduva Marijampole B vs FK Utenos Utenis | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-14 | RC Celta de Vigo vs UD Las Palmas | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-14 | Granada CF vs CF Valencia | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match