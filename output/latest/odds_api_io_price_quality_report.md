# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 47
Rejected price rows: 13
Rejected U-/reserve rows: 13
Forward prediction rows: 210
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-19 | Boston River vs Central Espanol Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | CA River Plate (URU) vs Deportivo Maldonado Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | Sarpsborg 08 2 vs Lyn 1896 FK II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | Barra FC SC vs Concordia SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | CA Banfield vs CA Aldosivi Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | CA Quilmes Reserve vs CA Lanus | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | Colon de Santa Fe Reserve vs Ferro Carril Oeste | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | Gremio Novorizontino SP vs Goias EC GO | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | Independiente Reserve vs Estudiantes de Rio Cuarto Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | San Lorenzo de Almagro Res. vs Racing Club Avellaneda | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | San Martin de San Juan Reserve vs Independiente Rivadavia de Mendoza Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | Vila Nova FC GO vs Coritiba FC PR | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-19 | SC Corinthians SP vs SE Palmeiras SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match