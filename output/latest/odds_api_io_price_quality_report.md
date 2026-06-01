# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 44
Rejected price rows: 16
Rejected U-/reserve rows: 16
Forward prediction rows: 113
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-06-01 | FC Bulleen Lions vs Port Melbourne Sharks SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Vietnam vs Timor-Leste | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Juventud de Las Piedras vs Montevideo Wanderers | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Indonesia vs Myanmar | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Japan vs Ivory Coast | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Nacional de Montevideo vs Albion FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Barra FC SC vs Nacao | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Venezuela vs Canada Youth | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Athletic Club MG vs Atletico Mineiro MG | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | CA River Plate (URU) vs Colon FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | EC Sao Jose RS vs Ypiranga RS | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Lyn 1896 FK II vs FK Gjoevik-Lyn | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Racing Club Montevideo vs La Luz FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Ser Caxias RS vs EC Juventude RS | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Santa Clara vs Gil Vicente FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Sport Huancayo Reserve vs Ayacucho FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match