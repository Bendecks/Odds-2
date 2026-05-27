# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 59
Accepted price rows: 49
Rejected price rows: 10
Rejected U-/reserve rows: 10
Forward prediction rows: 187
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-27 | Avai FC SC vs CR Vasco da Gama RJ | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Deportivo Riestra Afbc Reserve vs Estudiantes de LP Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Kings SC Kuopio vs KuPS Akatemia II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | AC Goianiense GO vs Operario Ferroviario EC PR | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Atletico Mineiro MG vs Chapecoense SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Atletico Tucuman Reserve vs CD Godoy Cruz | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | CA Belgrano vs CA Quilmes Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | CA Paranaense PR vs EC Juventude RS | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Ceara SC CE vs Brusque SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Coritiba FC PR vs Botafogo FC SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match