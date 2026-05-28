# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 58
Accepted price rows: 44
Rejected price rows: 14
Rejected U-/reserve rows: 14
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-28 | Deportivo Maldonado Reserve vs Liverpool Montevideo | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | CA Lanus vs CA Platense | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | CA Sarmiento de Junin vs Rosario Central Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | CA Union Santa Fe Reserve vs Gimnasia de Mendoza Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | Gimnasia de la Plata Reserve vs CA Barracas Central Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | Nacional de Montevideo vs La Luz FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | Progreso vs Defensor Sporting | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | Red Bull Bragantino SP vs SC Corinthians SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | ACF Fiorentina vs Parma Calcio 1913 U20 | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-28 | CA River Plate (Arg) vs San Lorenzo de Almagro Res. | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-29 | Blacktown Spartans FC vs Western City Rangers FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-29 | North Star vs Brisbane Strikers | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-29 | Adelaide University FC Reserve vs Adelaide Comets FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match