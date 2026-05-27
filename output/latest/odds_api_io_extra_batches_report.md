# Odds-API.io Extra Multi-Odds Batches

Adds extra /odds/multi calls after the primary fetch, using already discovered bookmaker-filtered events.
Only direct home/away/date matches are selected. Swapped matches are not selected here.

Existing price rows before extra: 5
Extra selected event rows: 75
Extra price rows: 45
Combined price rows: 50
Extra calls used: 5 / 5
Max total price events: 80
Minimum direct match confidence: 0.72
Latest rate-limit remaining: 42
Errors/status rows: 5

## New extra prices

- 2026-05-27 16:00 | HJK Klubi 04 vs PK-35 Helsinki | odds_api_io_Bet365_ML | 3.25/3.5/1.9
- 2026-05-27 16:00 | JJK Jyvaskyla/2 vs Komeetat | odds_api_io_Bet365_ML | 1.27/6.5/6.5
- 2026-05-27 16:00 | JK Tallinna Kalev vs Viimsi JK | odds_api_io_Bet365_ML | 3.75/4.1/1.666
- 2026-05-27 16:00 | Primorje Ajdovscina vs Nafta 1903 Lendava | odds_api_io_Bet365_ML | 2.45/3.3/2.5
- 2026-05-27 16:00 | SK Artis Brno vs 1. FC Slovacko Uherske Hradiste | odds_api_io_Bet365_ML | 3.0/3.2/2.25
- 2026-05-27 16:30 | Deportivo Riestra Afbc Reserve vs Estudiantes de LP Reserve | odds_api_io_Bet365_ML | 3.1/3.0/2.15
- 2026-05-27 16:30 | Sparta Prague B vs FC Hradec Kralove | odds_api_io_Bet365_ML | 2.5/3.8/2.25
- 2026-05-27 16:45 | Kings SC Kuopio vs KuPS Akatemia II | odds_api_io_Bet365_ML | 1.666/4.5/3.4
- 2026-05-27 17:00 | AIK DFF vs Hacken Gothenburg | odds_api_io_Bet365_ML | 5.25/3.9/1.48
- 2026-05-27 17:00 | FC Barcelona vs Real Sociedad San Sebastian | odds_api_io_Bet365_ML | 1.111/9.0/15.0
- 2026-05-27 17:00 | Eskilstuna United DFF vs Hammarby IF | odds_api_io_Bet365_ML | 7.5/6.0/1.27
- 2026-05-27 17:00 | VfB Hohenems vs FC Lauterach | odds_api_io_Bet365_ML | 1.38/5.0/5.25
- 2026-05-27 17:30 | Al Zawraa vs AL Naft | odds_api_io_Bet365_ML | 1.6/3.5/5.0
- 2026-05-27 17:30 | Newroz SC vs AL Mosul SC | odds_api_io_Bet365_ML | 1.95/3.2/3.4
- 2026-05-27 18:00 | AC Goianiense GO vs Operario Ferroviario EC PR | odds_api_io_Bet365_ML | 1.444/4.5/4.75
- 2026-05-27 18:00 | ADO 20 Heemskerk vs FC Lisse | odds_api_io_Bet365_ML | 2.7/3.75/2.15
- 2026-05-27 18:00 | America FC MG vs CR Flamengo RJ | odds_api_io_Bet365_ML | 2.0/3.25/3.3
- 2026-05-27 18:00 | Atletico Mineiro MG vs Chapecoense SC | odds_api_io_Bet365_ML | 1.2/6.25/8.0
- 2026-05-27 18:00 | Atletico Tucuman Reserve vs CD Godoy Cruz | odds_api_io_Bet365_ML | 1.8/3.2/4.1
- 2026-05-27 18:00 | CA Belgrano vs CA Quilmes Reserve | odds_api_io_Bet365_ML | 1.8/3.25/4.1
- 2026-05-27 18:00 | CA Paranaense PR vs EC Juventude RS | odds_api_io_Bet365_ML | 1.4/4.333/5.75
- 2026-05-27 18:00 | Ceara SC CE vs Brusque SC | odds_api_io_Bet365_ML | 1.09/9.0/21.0
- 2026-05-27 18:00 | Coritiba FC PR vs Botafogo FC SP | odds_api_io_Bet365_ML | 2.25/3.2/2.75
- 2026-05-27 18:00 | CR Brasil AL vs Gremio Novorizontino SP | odds_api_io_Bet365_ML | 3.0/3.6/2.0
- 2026-05-27 18:00 | Criciuma EC SC vs EC Bahia BA | odds_api_io_Bet365_ML | 2.9/3.5/2.1
- 2026-05-27 18:00 | EC Vitoria BA vs Sao Paulo FC SP | odds_api_io_Bet365_ML | 2.875/3.1/2.25
- 2026-05-27 18:00 | Fortaleza EC CE vs SE Palmeiras SP | odds_api_io_Bet365_ML | 4.1/3.7/1.65
- 2026-05-27 18:00 | Goias EC GO vs Mirassol FC SP | odds_api_io_Bet365_ML | 1.5/4.333/4.75
- 2026-05-27 18:00 | Heips RJ vs Coritiba FC PR | odds_api_io_Bet365_ML | 9.5/4.75/1.27
- 2026-05-27 18:00 | HK Kopavogur vs Volsungur | odds_api_io_Bet365_ML | 1.25/5.5/7.5

## Errors / Status

- extra_odds_parse: No 1X2 odds found for event 70773710
- extra_odds_parse: No 1X2 odds found for event 71685272
- extra_odds_parse: No 1X2 odds found for event 71238562
- extra_odds_parse: No 1X2 odds found for event 71679480
- extra_odds_parse: No 1X2 odds found for event 71238560