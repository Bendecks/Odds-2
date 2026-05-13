# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 52
Rejected price rows: 8
Rejected U-/reserve rows: 8
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-05-13 | GKS Belchatow vs Widzew Lodz II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-13 | Gzs Tluchovia Tluchowo vs Lech II Poznan | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-13 | Korona II Kielce SA vs KS Wisloka Debica | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-13 | KS Warta Sieradz vs Wisla Plock II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-13 | Legia Warszawa II vs GKS Wikielec | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-13 | Pogon Szczecin II vs Elana Torun | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-13 | MKS Mlawianka Mlawa vs Jagiellonia II Bialystok | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-05-13 | Wisla II Krakow vs Cracovia Krakow II | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match