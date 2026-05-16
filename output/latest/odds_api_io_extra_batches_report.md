# Odds-API.io Extra Multi-Odds Batches

Adds extra /odds/multi calls after the primary fetch, using already discovered bookmaker-filtered events.
Only direct home/away/date matches are selected. Swapped matches are not selected here.

Existing price rows before extra: 10
Extra selected event rows: 70
Extra price rows: 33
Combined price rows: 43
Extra calls used: 5 / 5
Max total price events: 80
Minimum direct match confidence: 0.72
Latest rate-limit remaining: 20
Errors/status rows: 17

## New extra prices

- 2026-05-16 13:30 | Hoek vs Rijnsburgse Boys | odds_api_io_Bet365_ML | 2.05/3.9/2.625
- 2026-05-16 13:30 | Rkav Volendam vs BVV Barendrecht | odds_api_io_Bet365_ML | 2.25/3.9/2.35
- 2026-05-16 13:30 | SC Freiburg vs RB Leipzig | odds_api_io_Bet365_ML | 2.45/3.9/2.55
- 2026-05-16 13:30 | FC St. Pauli vs VFL Wolfsburg | odds_api_io_Bet365_ML | 2.55/3.7/2.55
- 2026-05-16 13:30 | SV Meerssen vs FC Rijnvogels | odds_api_io_Bet365_ML | 3.6/4.1/1.7
- 2026-05-16 13:30 | SV Spakenburg vs VV Katwijk | odds_api_io_Bet365_ML | 2.5/3.9/2.1
- 2026-05-16 13:30 | SV Togb vs Groene Ster | odds_api_io_Bet365_ML | 2.15/4.0/2.5
- 2026-05-16 13:30 | USV Hercules vs Harkemase Boys | odds_api_io_Bet365_ML | 2.45/3.6/2.375
- 2026-05-16 13:30 | VV Gemert vs Stedoco | odds_api_io_Bet365_ML | 1.65/4.1/3.9
- 2026-05-16 13:30 | Werder Bremen vs Borussia Dortmund | odds_api_io_Bet365_ML | 3.3/4.0/2.0
- 2026-05-16 14:00 | A-Xiii Auhof Center vs WAF Vorwarts Brigittenau | odds_api_io_Bet365_ML | 1.38/4.5/6.0
- 2026-05-16 14:00 | Bryne FK vs Stroemmen IF | odds_api_io_Bet365_ML | 1.615/4.1/4.75
- 2026-05-16 14:00 | CA Independiente Cbba vs Club Tigres FC | odds_api_io_Bet365_ML | 2.05/3.75/2.75
- 2026-05-16 14:00 | Calcio Lecco 1912 U19 vs Pisa Calcio | odds_api_io_Bet365_ML | 1.7/3.9/3.7
- 2026-05-16 14:00 | CE Carroi vs Inter Club de Escaldes | odds_api_io_Bet365_ML | 17.0/8.5/1.111
- 2026-05-16 14:00 | Chelsea FC vs Manchester City | odds_api_io_Bet365_ML | 4.5/3.9/1.727
- 2026-05-16 14:00 | Corluspor 1947 vs Malatya Yesilyurt Belediyespor | odds_api_io_Bet365_ML | 1.75/3.3/4.0
- 2026-05-16 14:00 | DLR Waves vs Cork City Wfc | odds_api_io_Bet365_ML | 1.42/3.9/6.5
- 2026-05-16 14:00 | Floriana FC vs Marsaxlokk FC | odds_api_io_Bet365_ML | 2.05/3.25/3.1
- 2026-05-16 14:00 | Fredrikstad FK vs HamKam | odds_api_io_Bet365_ML | 1.95/3.4/3.75
- 2026-05-16 14:00 | IFK Goteborg vs Orebro SK Soder | odds_api_io_Bet365_ML | 1.666/3.7/4.0
- 2026-05-16 14:00 | IFK Lidingo FK vs FC Gute | odds_api_io_Bet365_ML | 2.4/3.6/2.4
- 2026-05-16 14:00 | FC Irtysh Pavlodar vs FC Yelimai | odds_api_io_Bet365_ML | 2.875/3.3/2.15
- 2026-05-16 14:00 | Kayserispor vs Konyaspor | odds_api_io_Bet365_ML | 2.1/3.75/2.75
- 2026-05-16 14:00 | KF Bashkimi Kumanovo 1947 vs FK Makedonija Gjorce Petrov | odds_api_io_Bet365_ML | 1.363/4.333/6.25
- 2026-05-16 14:00 | KF Tefik Canga vs KF Kika | odds_api_io_Bet365_ML | 1.8/4.2/3.1
- 2026-05-16 14:00 | KF Teuta vs KS Pogradeci | odds_api_io_Bet365_ML | 1.571/3.4/5.5
- 2026-05-16 14:00 | KSZO Ostrowiec Swietokrzyski vs Sokol Kolbuszowa Dolna | odds_api_io_Bet365_ML | 1.27/5.0/7.5
- 2026-05-16 14:00 | KV Vesturbaer vs Hottur/Huginn | odds_api_io_Bet365_ML | 3.0/3.8/1.95
- 2026-05-16 14:00 | LAC Inter vs Gerasd. Stammersd. | odds_api_io_Bet365_ML | 1.65/4.0/4.0

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 61967626
- extra_multi_odds_match: No odds payload matched event 61967618
- extra_multi_odds_match: No odds payload matched event 67915836
- extra_multi_odds_match: No odds payload matched event 71243190
- extra_multi_odds_match: No odds payload matched event 61730244
- extra_multi_odds_match: No odds payload matched event 67017926
- extra_multi_odds_match: No odds payload matched event 68310894
- extra_multi_odds_match: No odds payload matched event 68214652
- extra_multi_odds_match: No odds payload matched event 68954834
- extra_odds_parse: No 1X2 odds found for event 61286593
- extra_multi_odds_match: No odds payload matched event 67017928
- extra_odds_parse: No 1X2 odds found for event 67091306
- extra_multi_odds_match: No odds payload matched event 69109000
- extra_multi_odds_match: No odds payload matched event 67017930
- extra_multi_odds_match: No odds payload matched event 61467293
- extra_multi_odds_match: No odds payload matched event 67017932
- extra_multi_odds_match: No odds payload matched event 70730400