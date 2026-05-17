# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 300
Proxy price rows: 262
Matched prediction rows: 103
Value snapshot rows: 609
odds-api.io snapshot rows: 156
Baseline snapshot rows: 555
Full model snapshot rows: 54
Positive EV rows: 348
Source counts: {'odds_api_io_Bet365_ML': 156, 'football_data_max_market_proxy': 153, 'football_data_average_market_proxy': 153, 'football_data_bet365_proxy': 147}

- 2026-05-17 | Canberra Olympic vs Tuggeranong United FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3488 | EV=16.7888 | match=1.0
- 2026-05-17 | Maitland FC vs Lake Macquarie City FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3488 | EV=10.8592 | match=1.0
- 2026-05-17 | Canberra Olympic vs Tuggeranong United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.274 | EV=4.754 | match=1.0
- 2026-05-17 | Inter Milano vs Hellas Verona | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.92
- 2026-05-17 | Logan Roos FC vs Redcliffe Dolphins | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=0.8114
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=0.92
- 2026-05-17 | Inter Milano vs Hellas Verona | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.88 | prob=0.3488 | EV=3.492544 | match=0.92
- 2026-05-17 | Inter vs Verona | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.292 | EV=3.38 | match=1.0
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.92
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3217 | EV=3.1821 | match=1.0
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3488 | EV=2.955392 | match=0.92
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3217 | EV=2.8604 | match=1.0
- 2026-05-17 | Perth Redstar FC vs Subiaco AFC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-17 | Wuhan Lianzhen FC vs Guandong GZ-Power FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.3772 | EV=2.772 | match=1.0
- 2026-05-17 | Inter vs Verona | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.88 | prob=0.292 | EV=2.76096 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3217 | EV=2.648078 | match=1.0
- 2026-05-17 | Maitland FC vs Lake Macquarie City FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.13 | prob=0.3488 | EV=2.533344 | match=0.8114
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=10.0 | prob=0.3488 | EV=2.488 | match=0.8114
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Pisa SC vs SSC Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=0.92
- 2026-05-17 | Pisa SC vs SSC Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=0.92
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Juventus Turin vs ACF Fiorentina | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.4 | prob=0.3488 | EV=2.27872 | match=0.92
- 2026-05-17 | Inter Milano vs Hellas Verona | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.92
- 2026-05-17 | Juventus vs Fiorentina | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=9.4 | prob=0.3269 | EV=2.07286 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=8.06 | prob=0.3772 | EV=2.040232 | match=1.0
- 2026-05-17 | Pisa SC vs SSC Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=8.06 | prob=0.3772 | EV=2.040232 | match=0.92
- 2026-05-17 | Juventus Turin vs ACF Fiorentina | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.92