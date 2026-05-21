# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 48
Accepted price rows: 38
Rejected price rows: 10
Rejected U-/reserve rows: 10
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-21 | Odd BK vs KFUM Oslo | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | CA Barracas Central Reserve vs CA Union Santa Fe Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | CA Paranaense PR vs Botafogo FR RJ | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | CR Vasco da Gama RJ vs America FC MG | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | EC Bahia BA vs Fortaleza EC CE | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | Estudiantes de LP Reserve vs CA Belgrano | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | Gimnasia de Mendoza Reserve vs Atletico Tucuman Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | Instituto AC Cordoba Reserves vs CD Godoy Cruz | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | Red Bull Bragantino SP vs Gremio FB Porto Alegrense RS | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-21 | Velez Sarsfield Reserve vs CA River Plate (Arg) | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match