# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 59
Accepted price rows: 30
Rejected price rows: 29
Rejected U-/reserve rows: 29
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-30 | Canberra Juventus FC vs Tuggeranong United FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Metrostars Reserve vs West Adelaide Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | O'Connor Knights SC vs Queanbeyan City FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Gold Coast United FC vs Peninsula Power | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | University of NSW vs Wollongong Wolves FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Adelaide Cobras Reserves vs Adelaide Atletico Victory Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Adelaide Croatia Raiders SC Reserve vs Modbury Jets SC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Cumberland United Reserve vs Salisbury United Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Para Hills Knights SC Reserve vs Croydon Kings FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | South Adelaide Reserve vs Eastern United Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Campbelltown City SC Reserves vs Salisbury Inter Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Brindabella Blues FC vs Canberra Olympic FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Belconnen United FC vs Canberra Croatia FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Maitland FC Reserve vs Belmont Swansea United FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | North Eastern Metrostars SC Reserves vs Campbelltown City SC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Brunswick City SC vs Manningham United Blues FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Curtin University SC Reserves vs Joondalup City FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Fremantle City FC vs Perth Redstar FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Gwelup Croatia SC Reserves vs Quinns FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Inglewood United Reserves vs Cockburn City SC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Jeonbuk FC II vs Busan Transportation Corporation FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Mandurah City FC Reserves vs Floreat Athena FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | FC Melbourne Srbija vs Langwarrin SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Murdoch University Melville FC Reserves vs Kingsley Westside FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Olympic Kingsway SC vs Dianella White Eagles SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Sorrento FC vs Bayswater City SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Stirling Macedonia FC vs Balcatta Etna FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | Subiaco AFC Reserve vs Uwa Nedlands FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-30 | The Cove FC Reserves vs Adelaide Blue Eagles Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match