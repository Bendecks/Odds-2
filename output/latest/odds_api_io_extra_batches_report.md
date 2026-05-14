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
Latest rate-limit remaining: 77
Errors/status rows: 1

## New extra prices

- 2026-05-14 13:00 | Red Arrows vs Green Eagles | odds_api_io_Bet365_ML | 1.75/2.9/5.0
- 2026-05-14 13:00 | Shahrdari Nowshahr vs FC Fard Alborz | odds_api_io_Bet365_ML | 2.6/2.75/2.75
- 2026-05-14 13:00 | Simal vs Difai Agsu | odds_api_io_Bet365_ML | 3.2/3.5/2.0
- 2026-05-14 13:00 | Union Saint-Gilloise vs RSC Anderlecht | odds_api_io_Bet365_ML | 1.571/3.6/5.5
- 2026-05-14 13:15 | Mashujaa FC vs Simba SC | odds_api_io_Bet365_ML | 7.5/3.5/1.444
- 2026-05-14 13:15 | Sanat Mes Kerman FC vs Mes Shahr-e Babak | odds_api_io_Bet365_ML | 3.4/2.625/2.35
- 2026-05-14 13:30 | FK Vidar vs Sotra SK | odds_api_io_Bet365_ML | 5.25/4.2/1.5
- 2026-05-14 13:30 | Mjallby AIF vs Hammarby IF | odds_api_io_Bet365_ML | 3.4/3.7/2.0
- 2026-05-14 14:00 | Angelholms FF vs Aatvidabergs FF | odds_api_io_Bet365_ML | 2.375/3.25/2.625
- 2026-05-14 14:00 | HB Torshavn vs Vikingur Gota | odds_api_io_Bet365_ML | 2.15/3.5/2.7
- 2026-05-14 14:00 | IF Karlstad Fotbol vs IFK Stocksund | odds_api_io_Bet365_ML | 1.333/5.25/6.0
- 2026-05-14 14:00 | IF Vestri vs Grotta | odds_api_io_Bet365_ML | 1.48/5.0/4.2
- 2026-05-14 14:00 | KA Akureyri vs KF Aegir | odds_api_io_Bet365_ML | 1.142/7.5/13.0
- 2026-05-14 14:00 | Kjp Kouvola vs Lautp | odds_api_io_Bet365_ML | 2.875/4.2/1.909
- 2026-05-14 14:00 | Trelleborgs FF vs Jonkopings Sodra IF | odds_api_io_Bet365_ML | 1.85/3.4/3.7
- 2026-05-14 14:00 | FC Trollhattan vs Ariana FC | odds_api_io_Bet365_ML | 2.5/3.6/2.3
- 2026-05-14 14:00 | VfL Wolfsburg vs Bayern Munich | odds_api_io_Bet365_ML | 5.5/4.1/1.444
- 2026-05-14 14:05 | Dhofar SCSC vs Al Shabab | odds_api_io_Bet365_ML | 3.9/3.5/1.75
- 2026-05-14 14:30 | AL Naft vs AL Minaa | odds_api_io_Bet365_ML | 2.0/3.0/3.6
- 2026-05-14 14:30 | AL Naft Maysan vs AL Karma | odds_api_io_Bet365_ML | 4.0/3.3/1.8
- 2026-05-14 14:30 | FC Basel 1893 vs FC St. Gallen 1879 | odds_api_io_Bet365_ML | 2.7/3.5/2.45
- 2026-05-14 14:30 | FC Sion vs FC Lugano | odds_api_io_Bet365_ML | 2.1/3.5/3.4
- 2026-05-14 14:30 | Stade Renard vs Aigle Royal | odds_api_io_Bet365_ML | 1.95/3.6/3.1
- 2026-05-14 14:30 | FC Thun vs Young Boys Bern | odds_api_io_Bet365_ML | 2.2/3.8/2.875
- 2026-05-14 14:40 | Al Jahra vs Al-Nasr SC | odds_api_io_Bet365_ML | 2.8/3.0/2.375
- 2026-05-14 14:45 | POFC Botev Vratsa vs PFC Montana 1921 | odds_api_io_Bet365_ML | 1.666/3.7/5.0
- 2026-05-14 15:00 | AS Fortuna vs Coton Sport de Garoua | odds_api_io_Bet365_ML | 5.25/3.9/1.5
- 2026-05-14 15:00 | Austria Lustenau vs SKU Amstetten | odds_api_io_Bet365_ML | 1.6/4.0/5.0
- 2026-05-14 15:00 | FC Copenhagen vs FC Midtjylland | odds_api_io_Bet365_ML | 2.6/3.2/2.7
- 2026-05-14 15:00 | CS Sfaxien vs ES Sahel | odds_api_io_Bet365_ML | 1.444/3.3/8.5

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 69448904