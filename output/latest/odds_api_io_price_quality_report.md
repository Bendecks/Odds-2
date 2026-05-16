# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 35
Rejected price rows: 25
Rejected U-/reserve rows: 25
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-16 | Essendon Royals SC U20 vs South Melbourne FC U20 | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | O'Connor Knights SC vs Canberra Croatia FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Adelaide Atletico Victory Reserves vs Eastern United Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Bentleigh Greens SC vs Heidelberg United FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Dandenong Thunder FC vs ST Albans Saints Dinamo SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Manningham United Blues FC vs Brunswick Juventus FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Sturt Lions Reserve vs Croydon Kings FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | University of NSW vs Rockdale Ilinden FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Wellington Phoenix FC Reserve vs Island Bay United | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Adelaide Blue Eagles Reserves vs Fulham United FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | South Adelaide Reserve vs Salisbury United Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | West Adelaide SC Reserve vs West Torrens Birkalla Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Belconnen United FC vs Monaro Panthers FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Brisbane Strikers vs Holland Park Hawks | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Chuncheon FC vs Jeonbuk FC II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Cockburn City SC Reserves vs Joondalup City FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Curtin University SC Reserves vs Murdoch University Melville FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Dandenong City SC vs Oakleigh Cannons FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Fremantle City FC vs Olympic Kingsway SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Inglewood United Reserves vs Quinns FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Mandurah City FC Reserves vs Uwa Nedlands FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | FC Melbourne Srbija vs Brunswick City SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | North Eastern Metrostars SC Reserves vs Adelaide Comets Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Perth Redstar FC vs Armadale SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-16 | Sorrento FC vs Perth SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match