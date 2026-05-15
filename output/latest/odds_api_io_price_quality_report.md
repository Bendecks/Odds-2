# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 49
Rejected price rows: 11
Rejected U-/reserve rows: 11
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-15 | Auckland FC Reserves vs Auckland City FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Kyrgyzstan vs Turkmenistan | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Hurstville FC vs Prospect United | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Maitland FC Reserve vs Cooks Hill United FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Melbourne Knights FC vs Eltham Redbacks FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Northcote City FC vs FC Bulleen Lions | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Caboolture Sports FC vs North Star | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Slovakia vs San Marino | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Blacktown Spartans vs Bull FC Academy | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Libertad Asuncion vs Sportivo 2 de Mayo | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-15 | Ferencvarosi TC vs Illes Akademia | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match