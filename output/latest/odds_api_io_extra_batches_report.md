# Odds-API.io Extra Multi-Odds Batches

Adds extra /odds/multi calls after the primary fetch, using already discovered bookmaker-filtered events.
Only direct home/away/date matches are selected. Swapped matches are not selected here.

Existing price rows before extra: 8
Extra selected event rows: 72
Extra price rows: 33
Combined price rows: 41
Extra calls used: 5 / 5
Max total price events: 80
Minimum direct match confidence: 0.72
Latest rate-limit remaining: 78
Errors/status rows: 17

## New extra prices

- 2026-05-14 11:00 | Tanzania Prisons vs Fountain Gate FC | odds_api_io_Bet365_ML | 2.25/2.875/3.1
- 2026-05-14 11:00 | Torslanda IK vs Qviding FIF | odds_api_io_Bet365 (no latency)_ML | 2.05/3.9/2.7
- 2026-05-14 12:00 | Ellidi vs Vaengir Jupiters | odds_api_io_Bet365_ML | 1.8/4.2/3.1
- 2026-05-14 12:00 | Hinna vs FK Haugesund 2 | odds_api_io_Bet365_ML | 2.0/4.1/2.7
- 2026-05-14 12:00 | HPS II vs FC Honka | odds_api_io_Bet365_ML | 10.0/6.5/1.181
- 2026-05-14 12:00 | Nardo FK vs Byaasen | odds_api_io_Bet365_ML | 2.05/4.0/2.625
- 2026-05-14 12:00 | Ntnui vs Orkla | odds_api_io_Bet365_ML | 1.666/4.333/3.5
- 2026-05-14 12:00 | Oppsal IF vs Raade IL | odds_api_io_Bet365_ML | 4.333/4.75/1.48
- 2026-05-14 12:00 | Shire Endaselassie FC vs Ethiopian Coffee SC | odds_api_io_Bet365_ML | 3.4/2.8/2.2
- 2026-05-14 12:00 | Stabaek Fotball 2 vs Brodd | odds_api_io_Bet365_ML | 2.35/4.1/2.2
- 2026-05-14 12:00 | Umea FF vs Fransta IK | odds_api_io_Bet365_ML | 1.7/4.1/3.5
- 2026-05-14 12:00 | Viking FK 2 vs Akra | odds_api_io_Bet365_ML | 1.4/5.0/5.25
- 2026-05-14 12:15 | FK Septemvri Sofia vs FK Spartak 1918 Varna | odds_api_io_Bet365_ML | 1.75/3.4/4.5
- 2026-05-14 12:30 | FC Salzburg Frauen vs FK Austria Wien | odds_api_io_Bet365_ML | 11.0/5.5/1.2
- 2026-05-14 13:00 | Fauve Azur de Yaounde vs Gazelle FA de Garoua | odds_api_io_Bet365_ML | 3.1/3.1/2.1
- 2026-05-14 13:00 | Fk Kvik Trondheim vs Strindheim TF | odds_api_io_Bet365_ML | 2.0/4.1/2.7
- 2026-05-14 13:00 | Herentals FC vs Dynamos Harare FC | odds_api_io_Bet365_ML | 2.1/2.75/3.6
- 2026-05-14 13:00 | Lillehammer FK vs FK Gjoevik-Lyn | odds_api_io_Bet365_ML | 2.3/4.0/2.3
- 2026-05-14 13:00 | Lokomotiv Oslo vs FK Union Carl Berner | odds_api_io_Bet365_ML | 2.1/4.1/2.5
- 2026-05-14 13:00 | Masku vs LTU | odds_api_io_Bet365_ML | 1.571/4.5/3.8
- 2026-05-14 13:00 | Raelingen vs Brumunddal Fotball | odds_api_io_Bet365_ML | 1.65/4.5/3.5
- 2026-05-14 13:00 | Red Arrows vs Green Eagles | odds_api_io_Bet365_ML | 1.75/3.0/4.75
- 2026-05-14 13:00 | Shahrdari Nowshahr vs FC Fard Alborz | odds_api_io_Bet365_ML | 2.6/2.75/2.75
- 2026-05-14 13:00 | Simal vs Difai Agsu | odds_api_io_Bet365_ML | 2.6/3.4/2.375
- 2026-05-14 13:00 | Union Saint-Gilloise vs RSC Anderlecht | odds_api_io_Bet365_ML | 1.533/3.75/5.75
- 2026-05-14 13:15 | Sanat Mes Kerman FC vs Mes Shahr-e Babak | odds_api_io_Bet365_ML | 2.8/2.6/2.7
- 2026-05-14 13:30 | FK Vidar vs Sotra SK | odds_api_io_Bet365_ML | 5.0/4.0/1.533
- 2026-05-14 14:00 | HB Torshavn vs Vikingur Gota | odds_api_io_Bet365_ML | 2.15/3.7/2.7
- 2026-05-14 14:00 | IF Karlstad Fotbol vs IFK Stocksund | odds_api_io_Bet365_ML | 1.333/5.0/6.0
- 2026-05-14 14:00 | IF Vestri vs Grotta | odds_api_io_Bet365_ML | 1.6/4.75/3.6

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 67915816
- extra_multi_odds_match: No odds payload matched event 68344646
- extra_multi_odds_match: No odds payload matched event 70344940
- extra_odds_parse: No 1X2 odds found for event 68310884
- extra_multi_odds_match: No odds payload matched event 67915570
- extra_odds_parse: No 1X2 odds found for event 68311588
- extra_multi_odds_match: No odds payload matched event 68310886
- extra_multi_odds_match: No odds payload matched event 68377654
- extra_multi_odds_match: No odds payload matched event 68377658
- extra_multi_odds_match: No odds payload matched event 68344650
- extra_multi_odds_match: No odds payload matched event 67915820
- extra_multi_odds_match: No odds payload matched event 68310888
- extra_multi_odds_match: No odds payload matched event 67915572
- extra_multi_odds_match: No odds payload matched event 68320174
- extra_odds_parse: No 1X2 odds found for event 70267784
- extra_multi_odds_match: No odds payload matched event 68311590
- extra_multi_odds_match: No odds payload matched event 68311594