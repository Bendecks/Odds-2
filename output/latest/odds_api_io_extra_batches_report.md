# Odds-API.io Extra Multi-Odds Batches

Adds extra /odds/multi calls after the primary fetch, using already discovered bookmaker-filtered events.
Only direct home/away/date matches are selected. Swapped matches are not selected here.

Existing price rows before extra: 10
Extra selected event rows: 70
Extra price rows: 46
Combined price rows: 56
Extra calls used: 5 / 5
Max total price events: 80
Minimum direct match confidence: 0.72
Latest rate-limit remaining: 52
Errors/status rows: 4

## New extra prices

- 2026-06-03 09:30 | Belconnen United vs Tuggeranong Utd | odds_api_io_Bet365_ML | 2.15/4.2/2.375
- 2026-06-03 13:00 | Milford FC vs Magesi FC | odds_api_io_Bet365_ML | 3.1/2.875/2.3
- 2026-06-03 13:00 | Philippines vs Australia | odds_api_io_Bet365_ML | 34.0/15.0/1.04
- 2026-06-03 14:30 | FK Gazalkent vs FC Jayxun | odds_api_io_Bet365_ML | 1.25/5.0/8.5
- 2026-06-03 15:00 | Greece vs Serbia | odds_api_io_Bet365_ML | 2.875/3.2/2.2
- 2026-06-03 15:00 | India vs Bhutan | odds_api_io_Bet365_ML | 1.111/9.5/15.0
- 2026-06-03 15:00 | Montenegro vs Georgia | odds_api_io_Bet365_ML | 1.5/4.5/4.333
- 2026-06-03 15:30 | Croatia vs Qatar | odds_api_io_Bet365_ML | 1.5/3.8/5.25
- 2026-06-03 16:00 | Renaissance Zemamra vs US Yacoub Mansour | odds_api_io_Bet365_ML | 2.2/2.9/3.2
- 2026-06-03 16:00 | SV Anthering vs SV Burmoos | odds_api_io_Bet365_ML | 3.75/4.2/1.65
- 2026-06-03 16:30 | FC Hard vs SC Rothis | odds_api_io_Bet365_ML | 2.9/4.0/1.909
- 2026-06-03 16:30 | Ivory Coast vs Venezuela | odds_api_io_Bet365_ML | 1.666/3.6/4.1
- 2026-06-03 16:30 | SV Spittal/Drau vs KAC 1909 | odds_api_io_Bet365_ML | 2.5/3.7/2.25
- 2026-06-03 17:00 | Atus Velden vs FC Gleisdorf 09 | odds_api_io_Bet365_ML | 1.65/3.9/3.9
- 2026-06-03 17:00 | BK Olympic vs Lunds BK | odds_api_io_Bet365_ML | 2.375/3.6/2.5
- 2026-06-03 17:00 | Gibraltar vs Virgin Islands, British | odds_api_io_Bet365_ML | 1.333/4.75/7.5
- 2026-06-03 17:00 | FC Groningen vs de Graafschap | odds_api_io_Bet365_ML | 2.1/3.9/2.6
- 2026-06-03 17:00 | Helsingin Ponnistus vs Toukolan Teras/Tapio | odds_api_io_Bet365_ML | 2.05/4.5/2.45
- 2026-06-03 17:00 | IFK Umea vs Taftea IK | odds_api_io_Bet365_ML | 7.0/4.75/1.333
- 2026-06-03 17:00 | FC Marchfeld Donauauen vs SR Donaufeld | odds_api_io_Bet365_ML | 1.95/3.6/3.1
- 2026-06-03 17:00 | Ntnui vs Fk Kvik Trondheim | odds_api_io_Bet365_ML | 3.3/4.2/1.727
- 2026-06-03 17:00 | SC Kalsdorf vs SPG Wallern/ASV St. Marienkirchen | odds_api_io_Bet365_ML | 1.7/4.0/3.6
- 2026-06-03 17:00 | SK Bischofshofen vs SC Schwaz | odds_api_io_Bet365_ML | 1.533/4.2/4.333
- 2026-06-03 17:00 | TSV Grafenstein vs SV Dellach/Gail | odds_api_io_Bet365_ML | 1.95/3.9/2.875
- 2026-06-03 17:00 | Viggbyholms IK FF vs Sollentuna FK | odds_api_io_Bet365_ML | 8.0/4.5/1.3
- 2026-06-03 17:30 | SC Neusiedl am See 1919 vs SC Wiener Viktoria | odds_api_io_Bet365_ML | 3.25/4.1/1.75
- 2026-06-03 17:30 | SV Donau vs SC/ESV Parndorf 1919 | odds_api_io_Bet365_ML | 4.2/4.0/1.6
- 2026-06-03 17:30 | SV Leobendorf vs FCM Traiskirchen | odds_api_io_Bet365_ML | 2.4/3.8/2.3
- 2026-06-03 17:30 | Vasalunds IF vs FC Jarfalla | odds_api_io_Bet365_ML | 1.6/4.1/4.2
- 2026-06-03 17:45 | America FC RJ vs Sao Goncalo EC RJ | odds_api_io_Bet365_ML | 1.9/2.9/4.1

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 71863252
- extra_multi_odds_match: No odds payload matched event 71792798
- extra_multi_odds_match: No odds payload matched event 71792536
- extra_odds_parse: No 1X2 odds found for event 70673122