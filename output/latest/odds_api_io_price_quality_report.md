# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 50
Accepted price rows: 30
Rejected price rows: 20
Rejected U-/reserve rows: 20
Forward prediction rows: 169
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-27 | Deportivo Riestra Afbc Reserve vs Estudiantes de LP Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Kings SC Kuopio vs KuPS Akatemia II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | AC Goianiense GO vs Operario Ferroviario EC PR | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | America FC MG vs CR Flamengo RJ | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Atletico Mineiro MG vs Chapecoense SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Atletico Tucuman Reserve vs CD Godoy Cruz | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | CA Belgrano vs CA Quilmes Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | CA Paranaense PR vs EC Juventude RS | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Ceara SC CE vs Brusque SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Coritiba FC PR vs Botafogo FC SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | CR Brasil AL vs Gremio Novorizontino SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Criciuma EC SC vs EC Bahia BA | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | EC Vitoria BA vs Sao Paulo FC SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Fortaleza EC CE vs SE Palmeiras SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Goias EC GO vs Mirassol FC SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Independiente Rivadavia de Mendoza Reserve vs CA Central Cordoba SE Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Santos FC SP vs Botafogo FR RJ | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | SC Internacional RS vs Paysandu SC PA | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | SC Recife PE vs Vila Nova FC GO | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-27 | Velez Sarsfield Reserve vs Instituto AC Cordoba Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match