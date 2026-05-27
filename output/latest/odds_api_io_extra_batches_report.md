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
Latest rate-limit remaining: 57
Errors/status rows: 1

## New extra prices

- 2026-05-27 11:00 | Guangzhou Dandelion Alpha FC vs Ganzhou Ruishi FC | odds_api_io_Bet365_ML | 1.7/3.1/4.75
- 2026-05-27 11:30 | Nantong Haimen Codion vs Shanghai Second | odds_api_io_Bet365_ML | 1.571/3.6/5.0
- 2026-05-27 11:30 | Wuhan Three Towns B vs Guangdong Mingtu | odds_api_io_Bet365_ML | 2.2/2.875/3.2
- 2026-05-27 12:00 | Buriram United vs Selangor FC | odds_api_io_Bet365_ML | 1.45/4.333/5.25
- 2026-05-27 12:30 | Mighty Wanderers FC vs Karonga United FC | odds_api_io_Bet365_ML | 1.5/3.4/6.25
- 2026-05-27 13:00 | Gazelle FA de Garoua vs Stade Renard | odds_api_io_Bet365_ML | 1.3/4.2/9.0
- 2026-05-27 13:00 | FC Irtysh Pavlodar vs Ulytau FC | odds_api_io_Bet365_ML | 2.4/3.1/2.625
- 2026-05-27 13:00 | Manila Digger FC vs Kaya FC–Iloilo | odds_api_io_Bet365_ML | 5.0/4.75/1.42
- 2026-05-27 13:00 | Shahrdari Nowshahr vs FC Pars Jonoubi Jam | odds_api_io_Bet365_ML | 2.625/2.6/2.875
- 2026-05-27 13:15 | Niroye Zamini Tehran vs Havadar SC | odds_api_io_Bet365_ML | 2.5/2.625/2.9
- 2026-05-27 13:30 | Sanat Mes Kerman FC vs Nassaji Mazandaran FC | odds_api_io_Bet365_ML | 3.6/2.625/2.15
- 2026-05-27 14:00 | Avai FC SC vs CR Vasco da Gama RJ | odds_api_io_Bet365_ML | 4.75/4.0/1.533
- 2026-05-27 14:00 | Pakhtakor vs FC Kattaqorgon | odds_api_io_Bet365_ML | 1.1/8.0/13.0
- 2026-05-27 14:00 | FC Yaypan Fergana vs FK Termez Surkhon | odds_api_io_Bet365_ML | 3.0/3.1/2.2
- 2026-05-27 14:30 | FC Alga vs FC Bishkek City | odds_api_io_Bet365_ML | 1.727/3.4/4.1
- 2026-05-27 15:00 | AL Karma vs Diyala FC | odds_api_io_Bet365_ML | 1.7/3.5/4.2
- 2026-05-27 15:00 | Amanat Baghdad SC vs Al-Gharraf SC | odds_api_io_Bet365_ML | 2.55/3.1/2.55
- 2026-05-27 15:00 | Coton Sport de Garoua vs Panthere Sportive | odds_api_io_Bet365_ML | 1.48/3.6/6.25
- 2026-05-27 15:00 | Duhok FC vs Al Kahrabaa SC | odds_api_io_Bet365_ML | 2.1/3.2/3.0
- 2026-05-27 15:00 | FK Famos Vojkovici vs FK Zvijezda 09 | odds_api_io_Bet365_ML | 1.833/3.25/3.8
- 2026-05-27 15:00 | FC KTP vs FC Honka | odds_api_io_Bet365_ML | 7.0/6.5/1.222
- 2026-05-27 15:00 | Velez Nevesinje vs FK Sutjeska Foca | odds_api_io_Bet365_ML | 1.65/3.6/4.5
- 2026-05-27 15:30 | ETO FC Gyor vs MTK Hungaria Budapest | odds_api_io_Bet365_ML | 2.15/3.6/2.7
- 2026-05-27 15:30 | Jypk vs Ons Oulu | odds_api_io_Bet365_ML | 2.25/3.75/2.5
- 2026-05-27 15:30 | SJK Akatemia/2 vs JS Hercules | odds_api_io_Bet365_ML | 1.95/4.1/2.75
- 2026-05-27 15:30 | Tampereen Ilves vs Turun Palloseura | odds_api_io_Bet365_ML | 1.666/4.0/3.9
- 2026-05-27 16:00 | Al-Merrikh SC (SDN) vs Apr FC | odds_api_io_Bet365_ML | 2.45/2.9/2.7
- 2026-05-27 16:00 | HJK Klubi 04 vs PK-35 Helsinki | odds_api_io_Bet365_ML | 3.1/3.4/1.95
- 2026-05-27 16:00 | JJK Jyvaskyla/2 vs Komeetat | odds_api_io_Bet365_ML | 1.111/9.5/13.0
- 2026-05-27 16:00 | JK Tallinna Kalev vs Viimsi JK | odds_api_io_Bet365_ML | 3.5/4.0/1.727

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 68751822