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
Latest rate-limit remaining: 54
Errors/status rows: 2

## New extra prices

- 2026-05-28 17:00 | PPJ/Ruoholahti vs Mps | odds_api_io_Bet365_ML | 1.85/4.1/3.0
- 2026-05-28 17:20 | Ylojarvi United FC vs FC Haka J | odds_api_io_Bet365_ML | 1.95/4.75/2.625
- 2026-05-28 17:30 | Assyriska FF vs Vasalunds IF | odds_api_io_Bet365_ML | 2.3/3.75/2.45
- 2026-05-28 17:30 | Hedensted IF vs Fuglebakken KFUM | odds_api_io_Bet365_ML | 2.1/4.2/2.6
- 2026-05-28 17:30 | Zakho FC vs Erbil SC | odds_api_io_Bet365_ML | 2.5/3.0/2.6
- 2026-05-28 18:00 | CA Aldosivi Reserve vs CA Talleres de Cordoba Reserve | odds_api_io_Bet365_ML | 3.4/3.2/2.05
- 2026-05-28 18:00 | CA Lanus vs CA Platense | odds_api_io_Bet365_ML | 1.666/3.5/4.5
- 2026-05-28 18:00 | CA Sarmiento de Junin vs Rosario Central Reserve | odds_api_io_Bet365_ML | 3.25/3.3/2.05
- 2026-05-28 18:00 | CA Union Santa Fe Reserve vs Gimnasia de Mendoza Reserve | odds_api_io_Bet365_ML | 1.833/3.1/4.1
- 2026-05-28 18:00 | Gimnasia de la Plata Reserve vs CA Barracas Central Reserve | odds_api_io_Bet365_ML | 1.8/3.4/4.0
- 2026-05-28 18:00 | Nacional de Montevideo vs La Luz FC Reserves | odds_api_io_Bet365_ML | 1.666/3.6/4.2
- 2026-05-28 18:00 | Progreso vs Defensor Sporting | odds_api_io_Bet365_ML | 2.15/3.2/2.9
- 2026-05-28 18:00 | Red Bull Bragantino SP vs SC Corinthians SP | odds_api_io_Bet365_ML | 1.55/4.2/4.333
- 2026-05-28 18:30 | ACF Fiorentina vs Parma Calcio 1913 U20 | odds_api_io_Bet365_ML | 2.05/3.2/3.1
- 2026-05-28 18:30 | East Fife Lfc vs Falkirk FC | odds_api_io_Bet365_ML | 2.1/3.7/2.7
- 2026-05-28 18:30 | FK Decic Tuzi vs FK Mornar Bar | odds_api_io_Bet365_ML | 3.1/3.1/2.1
- 2026-05-28 18:30 | Wieczysta Krakow vs Polonia Warszawa | odds_api_io_Bet365_ML | 1.833/3.6/3.3
- 2026-05-28 18:45 | Ireland vs Qatar | odds_api_io_Bet365_ML | 1.45/4.2/6.0
- 2026-05-28 19:00 | Atletico Mineiro MG vs EC Vitoria BA | odds_api_io_Bet365_ML | 1.3/4.333/8.5
- 2026-05-28 19:00 | CA Piauiense PI vs Santos FC SP | odds_api_io_Bet365_ML | 3.4/3.3/1.95
- 2026-05-28 19:00 | Casa Pia Lisbon vs SCU Torreense | odds_api_io_Bet365_ML | 2.3/2.8/3.4
- 2026-05-28 20:00 | CD Real Santander vs Once Caldas Sa | odds_api_io_Bet365_ML | 2.5/2.8/2.75
- 2026-05-28 20:30 | Llaneros FC vs Independiente Santa Fe | odds_api_io_Bet365_ML | 7.5/4.2/1.333
- 2026-05-28 21:00 | CR Vasco da Gama RJ vs America FC MG | odds_api_io_Bet365_ML | 1.65/4.0/4.0
- 2026-05-28 21:30 | Cruzeiro EC MG vs Doce Mel EC BA | odds_api_io_Bet365_ML | 1.03/17.0/41.0
- 2026-05-28 22:00 | CA River Plate (Arg) vs San Lorenzo de Almagro Res. | odds_api_io_Bet365_ML | 1.7/3.5/4.333
- 2026-05-28 22:00 | Cerro Porteno vs Sporting Cristal | odds_api_io_Bet365_ML | 1.65/3.6/5.75
- 2026-05-28 22:00 | SE Palmeiras SP vs CD Junior FC | odds_api_io_Bet365_ML | 1.222/6.0/13.0
- 2026-05-28 23:00 | CD El Nacional vs CD Universidad Catolica del Ecuador | odds_api_io_Bet365_ML | 8.5/4.75/1.285
- 2026-05-28 23:00 | Paradise SC vs Kickstart Rush | odds_api_io_Bet365_ML | 2.0/3.75/2.875

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 71639628
- extra_multi_odds_match: No odds payload matched event 71639506