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
Latest rate-limit remaining: 76
Errors/status rows: 1

## New extra prices

- 2026-05-13 16:00 | MKS Arka Gdynia vs Gornik Zabrze | odds_api_io_Bet365_ML | 3.5/3.25/2.05
- 2026-05-13 16:30 | Olympiacos Piraeus vs Panathinaikos Athens | odds_api_io_Bet365_ML | 1.45/4.1/8.0
- 2026-05-13 16:30 | PAOK Thessaloniki vs AEK Athens | odds_api_io_Bet365_ML | 1.666/3.75/5.25
- 2026-05-13 17:00 | Espanyol Barcelona vs Athletic Bilbao | odds_api_io_Bet365_ML | 2.625/3.3/2.7
- 2026-05-13 17:00 | Falkenbergs FF vs Varbergs BoIS | odds_api_io_Bet365_ML | 2.5/3.25/2.6
- 2026-05-13 17:00 | Helsingborgs IF vs IK Oddevold | odds_api_io_Bet365_ML | 2.35/3.3/2.75
- 2026-05-13 17:00 | IFK Norrkoping FK vs Nordic United FC | odds_api_io_Bet365_ML | 1.7/3.7/4.1
- 2026-05-13 17:00 | IK Brage vs Ostersunds FK | odds_api_io_Bet365_ML | 2.2/3.25/3.0
- 2026-05-13 17:00 | Osters IF vs Sandvikens IF | odds_api_io_Bet365_ML | 1.95/3.5/3.3
- 2026-05-13 17:00 | Stade Brest 29 vs Strasbourg Alsace | odds_api_io_Bet365_ML | 2.8/3.6/2.4
- 2026-05-13 17:15 | PFC Ludogorets 1945 Razgrad vs PFC Levski Sofia | odds_api_io_Bet365_ML | 1.7/3.6/5.25
- 2026-05-13 18:00 | Arsenal WFC vs Everton FC | odds_api_io_Bet365_ML | 1.09/9.5/21.0
- 2026-05-13 18:00 | FK Vojvodina Novi Sad vs FK Crvena Zvezda Belgrade | odds_api_io_Bet365_ML | 7.5/4.75/1.363
- 2026-05-13 17:00 | Villarreal CF vs Sevilla FC | odds_api_io_Bet365_ML | 2.05/3.4/3.7
- 2026-05-13 18:30 | RKS Rakow Czestochowa vs Jagiellonia Bialystok | odds_api_io_Bet365_ML | 2.05/3.4/3.25
- 2026-05-13 18:45 | Alloa Athletic FC vs Stenhousemuir FC | odds_api_io_Bet365_ML | 2.4/3.3/2.875
- 2026-05-13 19:00 | Glasgow Rangers vs Hibernian FC | odds_api_io_Bet365_ML | 1.5/4.75/5.5
- 2026-05-13 19:00 | Heart of Midlothian FC vs Falkirk FC | odds_api_io_Bet365_ML | 1.42/4.75/7.0
- 2026-05-13 19:00 | Lazio Rome vs Inter Milano | odds_api_io_Bet365_ML | 5.0/3.8/1.666
- 2026-05-13 19:00 | Motherwell FC vs Celtic Glasgow | odds_api_io_Bet365_ML | 4.5/4.2/1.666
- 2026-05-13 19:00 | Racing Club De Lens vs Paris Saint-Germain | odds_api_io_Bet365_ML | 3.3/3.9/2.0
- 2026-05-13 19:00 | Stockport County FC vs Stevenage FC | odds_api_io_Bet365_ML | 1.833/3.4/4.333
- 2026-05-13 19:00 | Manchester City vs Crystal Palace | odds_api_io_Bet365_ML | 1.2/7.5/12.0
- 2026-05-13 19:30 | Deportivo Alaves vs FC Barcelona | odds_api_io_Bet365_ML | 3.25/4.0/2.05
- 2026-05-13 19:30 | Getafe CF vs RCD Mallorca | odds_api_io_Bet365_ML | 2.1/3.0/3.25
- 2026-05-13 21:00 | Bogota FC vs Barranquilla FC | odds_api_io_Bet365_ML | 1.75/3.7/4.333
- 2026-05-13 21:45 | CA Rosario Central vs Racing Club Avellaneda | odds_api_io_Bet365_ML | 2.25/3.0/3.6
- 2026-05-13 22:00 | CR Vasco da Gama RJ vs Paysandu SC PA | odds_api_io_Bet365_ML | 1.25/5.5/11.0
- 2026-05-13 22:00 | EC Juventude RS vs Sao Paulo FC SP | odds_api_io_Bet365_ML | 3.6/3.2/2.1
- 2026-05-13 22:30 | Coritiba FC PR vs Santos FC SP | odds_api_io_Bet365_ML | 2.7/2.8/3.0

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 69254646