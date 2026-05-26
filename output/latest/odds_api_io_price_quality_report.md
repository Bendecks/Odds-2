# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 59
Accepted price rows: 47
Rejected price rows: 12
Rejected U-/reserve rows: 12
Forward prediction rows: 196
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-26 | Lyn 1896 FK II vs Drobak-Frogn | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | Defensa Y Justicia Reserve vs Independiente Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | Gil Vicente FC vs Santa Clara | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | SK Super Nova II vs Valmiera FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | Argentinos Juniors Reserve vs CA Banfield | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | CA Huracan vs Ferro Carril Oeste | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | Estudiantes de Rio Cuarto Reserve vs Boca Juniors | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | Fluminense FC RJ vs Cruzeiro EC MG | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | Inhumas EC GO vs AA Aparecidense GO | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | Racing Club Avellaneda vs CA Tigre Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | San Martin de San Juan Reserve vs Colon de Santa Fe Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-26 | Torque vs CA River Plate (URU) | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match