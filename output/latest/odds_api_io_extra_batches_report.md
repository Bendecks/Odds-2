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
Latest rate-limit remaining: 47
Errors/status rows: 1

## New extra prices

- 2026-05-19 12:00 | Juventud de Las Piedras vs Colon FC Reserve | odds_api_io_Bet365_ML | 1.666/3.7/4.1
- 2026-05-19 12:00 | Qingdao West Coast FC vs Beijing Guoan | odds_api_io_Bet365_ML | 3.6/3.6/1.95
- 2026-05-19 12:00 | Tajikistan vs Kyrgyzstan | odds_api_io_Bet365_ML | 2.375/3.2/2.625
- 2026-05-19 12:00 | Uwa Nedlands FC Reserves vs Inglewood United Reserves | odds_api_io_Bet365_ML | 1.285/5.75/6.0
- 2026-05-19 13:00 | Al-Horiyah vs Al-Jaish SC (Syr) | odds_api_io_Bet365_ML | 2.25/2.9/3.1
- 2026-05-19 13:00 | Deportivo Capiata vs Club Fernando de La Mora | odds_api_io_Bet365_ML | 2.05/3.2/3.25
- 2026-05-19 13:00 | Rajasthan United vs Chanmari FC | odds_api_io_Bet365_ML | 1.727/3.6/3.8
- 2026-05-19 13:00 | Tacuary Asuncion vs Encarnacion FC | odds_api_io_Bet365_ML | 2.3/3.1/2.8
- 2026-05-19 14:30 | Al Kahrabaa SC vs Al-Gharraf SC | odds_api_io_Bet365_ML | 2.05/3.1/3.3
- 2026-05-19 14:30 | Diyala FC vs Amanat Baghdad SC | odds_api_io_Bet365_ML | 2.0/3.2/3.3
- 2026-05-19 14:30 | MFK Zvolen vs KFC Komarno | odds_api_io_Bet365_ML | 2.625/3.2/2.625
- 2026-05-19 15:00 | Ben Aknoun vs ES Mostaganem | odds_api_io_Bet365_ML | 1.363/4.333/7.5
- 2026-05-19 15:00 | Klaipedos Fsm vs Dfk Dainava Alytus | odds_api_io_Bet365_ML | 4.5/3.7/1.571
- 2026-05-19 15:00 | MB Rouissat vs Paradou AC | odds_api_io_Bet365_ML | 1.95/3.0/3.6
- 2026-05-19 15:00 | FC Noah Yerevan vs Ararat Yerevan FC | odds_api_io_Bet365_ML | 1.111/9.5/13.0
- 2026-05-19 15:00 | Velez Nevesinje vs FK Vlasenica | odds_api_io_Bet365_ML | 1.444/4.0/6.25
- 2026-05-19 16:00 | FC Haka J vs Saaksjaerven Loiske | odds_api_io_Bet365_ML | 1.3/5.5/6.25
- 2026-05-19 16:00 | Hapoel Acre FC vs Hapoel Hadera FC | odds_api_io_Bet365_ML | 1.571/3.6/5.0
- 2026-05-19 16:00 | Hapoel Nof Hagalil FC vs Ironi Modiin | odds_api_io_Bet365_ML | 2.9/3.0/2.25
- 2026-05-19 16:00 | Hapoel Ra`anana FC vs FC Kafr Qasim | odds_api_io_Bet365_ML | 3.2/3.2/2.05
- 2026-05-19 16:00 | FC Kiisto vs Vpv | odds_api_io_Bet365_ML | 1.25/5.75/7.0
- 2026-05-19 16:00 | LSK Kvinner FK vs Hoenefoss BK | odds_api_io_Bet365_ML | 1.42/4.1/6.25
- 2026-05-19 16:00 | Maccabi Kabilio Jaffa vs Hapoel Afula FC | odds_api_io_Bet365_ML | 2.15/3.25/3.0
- 2026-05-19 16:00 | SK Brann 2 vs Sogndal 2 | odds_api_io_Bet365_ML | 2.0/4.2/2.625
- 2026-05-19 16:30 | AS Korofina vs Binga FC | odds_api_io_Bet365_ML | 2.9/2.875/2.375
- 2026-05-19 16:30 | Derby Academie vs Onze Createurs | odds_api_io_Bet365_ML | 2.25/2.7/3.3
- 2026-05-19 16:30 | SV Ried vs Wolfsberger AC | odds_api_io_Bet365_ML | 2.25/3.3/3.2
- 2026-05-19 16:45 | CS Constantine vs USM Khenchela | odds_api_io_Bet365_ML | 1.5/3.5/6.0
- 2026-05-19 17:00 | AL Naft vs Duhok FC | odds_api_io_Bet365_ML | 2.35/3.0/2.8
- 2026-05-19 17:00 | AL Talaba vs AL Karma | odds_api_io_Bet365_ML | 2.6/3.0/2.55

## Errors / Status

- extra_multi_odds_match: No odds payload matched event 71240280