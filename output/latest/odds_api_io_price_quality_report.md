# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 30
Accepted price rows: 22
Rejected price rows: 8
Rejected U-/reserve rows: 8
Forward prediction rows: 160
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Sportivo Ameliano vs Deportivo Recoleta Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Murdoch University Melville FC Reserves vs Joondalup City FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Deportivo Maldonado Reserve vs Racing Club Montevideo | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | AL Ittihad Kalba vs AL Nasr | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | AL Wasl vs AL Jazira | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match