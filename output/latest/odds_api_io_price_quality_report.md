# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 54
Accepted price rows: 29
Rejected price rows: 25
Rejected U-/reserve rows: 25
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-23 | Eastern United Reserve vs Adelaide Blue Eagles Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Green Gully SC vs Heidelberg United FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Adelaide Atletico Victory Reserves vs South Adelaide Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Canberra White Eagles FC vs O'Connor Knights SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Croydon Kings FC Reserve vs North Eastern Metrostars SC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Salisbury United Reserve vs Adelaide Cobras Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Gold Coast United FC vs Rochedale Rovers | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Port Melbourne Sharks SC vs Brunswick Juventus FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Queanbeyan City FC vs Canberra Juventus FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Bentleigh Greens SC vs Caroline Springs George Cross FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | FC Fujizakura vs Jfa Academy Fukushima | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Holland Park Hawks vs Sunshine Coast Wanderers | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Perth Redstar FC vs Perth SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Upper Hutt City FC vs Wellington Phoenix FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Adelaide Comets Reserves vs Para Hills Knights SC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Adelaide Croatia Raiders SC Reserve vs Adelaide Olympic FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Campbelltown City SC Reserve vs Sturt Lions Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Fulham United FC Reserve vs The Cove FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Modbury Jets SC Reserve vs Cumberland United Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Playford City Reserve vs West Adelaide SC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Moreton City Excelsior U23 vs Brisbane City | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Edgeworth FC Reserve vs Lambton Jaffas FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | North Star vs Logan Lightning | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Balcatta Etna FC vs Western Knights SC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-23 | Cockburn City SC Reserves vs Floreat Athena FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match