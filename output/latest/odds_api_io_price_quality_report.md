# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 30
Accepted price rows: 23
Rejected price rows: 7
Rejected U-/reserve rows: 7
Forward prediction rows: 160
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-12 | Gwelup Croatia SC Reserves vs Cockburn City SC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Murdoch University Melville FC Reserves vs Joondalup City FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Deportivo Maldonado Reserve vs Racing Club Montevideo | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | AL Ittihad Kalba vs AL Nasr | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | AL Wasl vs AL Jazira | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | Zaglebie Lubin II vs Mkp Carina Gubin | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-12 | AL Wahda FC vs Khorfakkan | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match