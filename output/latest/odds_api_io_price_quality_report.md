# Odds-API.io Price Quality Filter

Filters raw Odds-API.io prices before they are used as automatic forward prices.
A price is accepted only when API home/away/date directly matches a senior-team forward prediction home/away/date.
Youth, U-teams, reserve teams, academy teams and B-teams are rejected before paper-pick generation.
Swapped home/away matches are rejected because venue affects both model probabilities and market odds.

Input price rows: 60
Accepted price rows: 45
Rejected price rows: 15
Rejected U-/reserve rows: 15
Forward prediction rows: 300
Rule: accept_only_direct_senior_home_away_match_against_forward_fixture_predictions

## Rejected prices

- 2026-06-04 | Bulgaria vs Albania | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | Sweden vs Finland | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | Slovenia vs Bosnia and Herzegovina | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | Germany vs Denmark | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | Moldova vs Malta | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | America FC SP vs CA Juventus SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | Araucaria ECR PR vs FC Cascavel PR | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | Avai FC SC vs Nacao | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | CA Barracas Central Reserve vs CA Aldosivi Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | CD Godoy Cruz vs CA Union Santa Fe Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | GD Prudente SP vs SE Palmeiras SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | San Lorenzo de Almagro Res. vs Velez Sarsfield Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | CA Central Cordoba SE Reserve vs San Martin de San Juan Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | CA Talleres de Cordoba Reserve vs Argentinos Juniors Reserve | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match
- 2026-06-04 | Osasco Sporting SP vs AE Velo Clube SP | odds_api_io_Bet365_ML | status=rejected_youth_or_reserve_match