# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 30
Accepted price rows: 21
Rejected price rows: 9
Rejected U-/reserve rows: 9
Forward prediction rows: 136
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-12 | Central Espanol Reserve vs Defensor Sporting | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Real Madrid vs Borussia Dortmund | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Colon FC Reserve vs Liverpool Montevideo | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Defensa Y Justicia Reserve vs CA Platense | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Gimnasia de la Plata Reserve vs CA Banfield | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Newells Old Boys vs CA Quilmes Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Racing Club Avellaneda vs Velez Sarsfield Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Cerro Largo FC vs Boston River | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Penarol Montevideo vs Nacional de Montevideo | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match