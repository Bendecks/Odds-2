# Odds-API.io Extra Multi-Odds Batches

Adds extra /odds/multi calls after the primary fetch, using already discovered bookmaker-filtered events.
Only direct home/away/date matches are selected. Swapped matches are not selected here.

Existing price rows before extra: 10
Extra selected event rows: 70
Extra price rows: 49
Combined price rows: 59
Extra calls used: 5 / 5
Max total price events: 80
Minimum direct match confidence: 0.72
Latest rate-limit remaining: 30
Errors/status rows: 1

## New extra prices

- 2026-05-26 16:00 | FC Honka vs VJS | odds_api_io_Bet365_ML | 2.75/3.5/2.1
- 2026-05-26 16:00 | KPV/Akatemia vs FC Kiisto | odds_api_io_Bet365_ML | 8.0/7.0/1.222
- 2026-05-26 16:00 | LSK Kvinner FK vs Hoenefoss BK | odds_api_io_Bet365_ML | 1.533/3.8/4.75
- 2026-05-26 16:00 | Lyn 1896 FK II vs Drobak-Frogn | odds_api_io_Bet365_ML | 1.666/4.2/3.6
- 2026-05-26 16:00 | Molde FK vs Rosenborg BK Kvinner | odds_api_io_Bet365_ML | 6.5/5.0/1.333
- 2026-05-26 16:00 | SK Brann vs Lyn | odds_api_io_Bet365_ML | 1.142/7.0/15.0
- 2026-05-26 16:00 | SK Herd vs Aalesund FK 2 | odds_api_io_Bet365_ML | 1.3/5.25/6.25
- 2026-05-26 16:00 | Stabaek Fotball vs Haugesund | odds_api_io_Bet365_ML | 1.727/3.5/3.9
- 2026-05-26 16:00 | Stroemsgodset 2 vs Lillestrom SK 2 | odds_api_io_Bet365_ML | 2.2/5.0/2.15
- 2026-05-26 16:00 | Vaalerenga Oslo vs Bodoe/Glimt | odds_api_io_Bet365_ML | 1.015/26.0/41.0
- 2026-05-26 16:30 | Defensa Y Justicia Reserve vs Independiente Reserve | odds_api_io_Bet365_ML | 2.15/3.7/2.8
- 2026-05-26 17:00 | Aasane Fotball 2 vs Gneist | odds_api_io_Bet365_ML | 1.7/4.5/3.3
- 2026-05-26 17:00 | Alhama CF vs Levante UD | odds_api_io_Bet365_ML | 2.25/3.2/2.8
- 2026-05-26 17:00 | FC Badalona Women vs Real Madrid | odds_api_io_Bet365_ML | 4.333/4.333/1.533
- 2026-05-26 17:00 | Gil Vicente FC vs Santa Clara | odds_api_io_Bet365_ML | 1.55/3.9/4.75
- 2026-05-26 17:00 | Granada CF vs Madrid CFF | odds_api_io_Bet365_ML | 2.15/3.4/2.8
- 2026-05-26 17:00 | Orebro SK vs Helsingborgs IF | odds_api_io_Bet365_ML | 2.25/3.3/2.875
- 2026-05-26 17:00 | Raade IL vs Sarpsborg 08 2 | odds_api_io_Bet365_ML | 1.222/6.0/7.5
- 2026-05-26 17:00 | Sevilla FC vs SD Eibar | odds_api_io_Bet365_ML | 1.95/3.5/3.1
- 2026-05-26 17:00 | SK Super Nova II vs Valmiera FC | odds_api_io_Bet365_ML | 4.0/4.2/1.571
- 2026-05-26 17:30 | Hapoel Be`er Sheva FC vs Maccabi Tel Aviv FC | odds_api_io_Bet365_ML | 1.95/3.75/3.1
- 2026-05-26 18:00 | Argentinos Juniors Reserve vs CA Banfield | odds_api_io_Bet365_ML | 1.7/3.5/4.75
- 2026-05-26 18:00 | CA Huracan vs Ferro Carril Oeste | odds_api_io_Bet365_ML | 1.615/3.5/5.0
- 2026-05-26 18:00 | Estudiantes de Rio Cuarto Reserve vs Boca Juniors | odds_api_io_Bet365_ML | 6.5/4.2/1.4
- 2026-05-26 18:00 | Fluminense FC RJ vs Cruzeiro EC MG | odds_api_io_Bet365_ML | 2.375/3.2/2.7
- 2026-05-26 18:00 | Inhumas EC GO vs AA Aparecidense GO | odds_api_io_Bet365_ML | 2.05/3.2/3.2
- 2026-05-26 18:00 | Racing Club Avellaneda vs CA Tigre Reserve | odds_api_io_Bet365_ML | 1.666/3.4/4.75
- 2026-05-26 18:00 | San Martin de San Juan Reserve vs Colon de Santa Fe Reserve | odds_api_io_Bet365_ML | 4.5/3.6/1.65
- 2026-05-26 18:00 | Torque vs CA River Plate (URU) | odds_api_io_Bet365_ML | 1.727/3.9/3.6
- 2026-05-26 18:30 | CD Armenio vs Argentino de Merlo | odds_api_io_Bet365_ML | 3.1/2.6/2.4

## Errors / Status

- extra_odds_parse: No 1X2 odds found for event 71553982