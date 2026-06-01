# Odds-API.io Extra Multi-Odds Batches

Adds extra /odds/multi calls after the primary fetch, using already discovered bookmaker-filtered events.
Only direct home/away/date matches are selected. Swapped matches are not selected here.

Existing price rows before extra: 10
Extra selected event rows: 70
Extra price rows: 48
Combined price rows: 58
Extra calls used: 5 / 5
Max total price events: 80
Minimum direct match confidence: 0.72
Latest rate-limit remaining: 57
Errors/status rows: 2

## New extra prices

- 2026-06-01 18:00 | Racing Club Montevideo vs La Luz FC Reserves | odds_api_io_Bet365_ML | 2.0/3.5/3.3
- 2026-06-01 18:00 | SC Recife PE vs Paysandu SC PA | odds_api_io_Bet365_ML | 1.25/5.0/8.5
- 2026-06-01 18:00 | Ser Caxias RS vs EC Juventude RS | odds_api_io_Bet365_ML | 4.75/3.6/1.615
- 2026-06-01 18:30 | Argentino de Quilmes vs CA Ituzaingo | odds_api_io_Bet365_ML | 1.727/3.1/4.5
- 2026-06-01 18:30 | CA Fenix Pilar vs Canuelas FC | odds_api_io_Bet365_ML | 3.8/2.75/2.05
- 2026-06-01 18:30 | CS Barracas vs CA Atlas | odds_api_io_Bet365_ML | 2.1/2.8/3.5
- 2026-06-01 18:45 | Austria vs Tunisia | odds_api_io_Bet365_ML | 1.444/4.2/7.0
- 2026-06-01 19:00 | FC Atletico CE vs Piaui PI | odds_api_io_Bet365_ML | 4.0/3.1/1.833
- 2026-06-01 19:00 | Guairena FC vs Club 3 De Noviembre | odds_api_io_Bet365_ML | 1.85/3.2/3.9
- 2026-06-01 19:15 | KFG Gardabaer vs Fjolnir | odds_api_io_Bet365_ML | 5.75/5.75/1.3
- 2026-06-01 19:15 | KH Hlidarendi vs Arbaer | odds_api_io_Bet365_ML | 1.666/4.75/3.3
- 2026-06-01 19:15 | Throttur Reykjavik vs UMF Grindavik | odds_api_io_Bet365_ML | 1.65/3.75/4.1
- 2026-06-01 19:30 | Chapaquito Nacional Senac vs Club Deportivo San Martin | odds_api_io_Bet365_ML | 5.75/5.0/1.333
- 2026-06-01 20:00 | CODM Meknes vs Olympique Dcheira | odds_api_io_Bet365_ML | 1.9/3.0/4.0
- 2026-06-01 20:30 | Sport Huancayo Reserve vs Ayacucho FC | odds_api_io_Bet365_ML | 1.95/3.0/3.5
- 2026-06-01 22:00 | AA Ponte Preta SP vs Botafogo FC SP | odds_api_io_Bet365_ML | 3.0/2.9/2.6
- 2026-06-01 22:00 | Leones Futbol Club vs CSD Macara | odds_api_io_Bet365_ML | 2.6/2.9/2.875
- 2026-06-01 22:30 | Planalto EC GO vs Rolim de Moura RO | odds_api_io_Bet365_ML | 1.444/3.9/6.0
- 2026-06-01 23:00 | Barra FC SC vs Brusque FC SC | odds_api_io_Bet365_ML | 1.9/3.2/4.1
- 2026-06-01 23:00 | CA Penarol Montevideo vs Central Espanol FC | odds_api_io_Bet365_ML | 1.55/4.2/5.25
- 2026-06-01 23:00 | CD Santa Cruz vs Deportes Copiapo | odds_api_io_Bet365_ML | 2.15/3.1/3.1
- 2026-06-01 23:00 | Colombia vs Costa Rica | odds_api_io_Bet365_ML | 1.142/6.5/17.0
- 2026-06-01 23:00 | Curico Unido vs CD Antofagasta | odds_api_io_Bet365_ML | 2.875/3.4/2.1
- 2026-06-01 23:00 | Maguary PE vs Sousa EC PB | odds_api_io_Bet365_ML | 1.666/3.1/5.25
- 2026-06-01 23:15 | CN Marcilio Dias SC vs Azuriz FC PR | odds_api_io_Bet365_ML | 1.5/3.3/7.5
- 2026-06-02 00:00 | FC Universitario de Vinto vs Club Aurora | odds_api_io_Bet365_ML | 2.45/3.3/2.7
- 2026-06-02 00:30 | CD Tecnico Universitario vs Barcelona SC | odds_api_io_Bet365_ML | 2.75/3.25/2.45
- 2026-06-02 00:30 | SV Estrella vs Jong Aruba | odds_api_io_Bet365_ML | 1.3/5.0/7.5
- 2026-06-02 01:00 | Canada vs Uzbekistan | odds_api_io_Bet365_ML | 1.571/3.5/5.5
- 2026-06-02 02:00 | Stars FC vs Southern California Eagles | odds_api_io_Bet365_ML | 2.3/3.9/2.375

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 71863238
- extra_multi_odds_match: No odds payload matched event 71863280