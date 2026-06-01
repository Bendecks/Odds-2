# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 58
Accepted price rows: 45
Rejected price rows: 13
Rejected U-/reserve rows: 13
Forward prediction rows: 150
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-06-01 | Athletic Club MG vs Atletico Mineiro MG | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | CA River Plate (URU) vs Colon FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | EC Sao Jose RS vs Ypiranga RS | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Lyn 1896 FK II vs FK Gjoevik-Lyn | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Racing Club Montevideo vs La Luz FC Reserves | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Ser Caxias RS vs EC Juventude RS | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-01 | Sport Huancayo Reserve vs Ayacucho FC | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-02 | North Star vs Brisbane Strikers | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-02 | Lake Macquarie City FC Reserve vs New Lambton FC Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-02 | Podbeskidzie Bielsko-Biała vs Slask II Wroclaw | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-02 | China vs Congo Dr Youth | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-02 | Malaysia vs Singapore | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-02 | Olimpia Grudziadz vs Sandecja Nowy Sacz | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match