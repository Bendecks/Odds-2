# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 56
Accepted price rows: 41
Rejected price rows: 15
Rejected U-/reserve rows: 15
Forward prediction rows: 282
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-06-03 | Belconnen United FC vs Tuggeranong United FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Portugal vs Kazakhstan | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Sydney Olympic FC vs University of NSW | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Japan vs Portugal | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Philippines vs Australia | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Greece vs Serbia | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Montenegro vs Georgia | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Croatia vs Qatar | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Ivory Coast vs Venezuela | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | FC Groningen vs de Graafschap | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Estudiantes de LP Reserve vs Independiente Rivadavia de Mendoza Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Instituto AC Cordoba Reserves vs Atletico Tucuman Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Rosario Central Reserve vs Racing Club Avellaneda | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | FC Winterthur vs FC Lausanne Sport | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-03 | Portugal vs Northern Ireland | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match