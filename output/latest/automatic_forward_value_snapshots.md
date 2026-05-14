# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 300
Proxy price rows: 65
Matched prediction rows: 62
Value snapshot rows: 228
odds-api.io snapshot rows: 174
Baseline snapshot rows: 210
Full model snapshot rows: 18
Positive EV rows: 110
Source counts: {'odds_api_io_Bet365_ML': 174, 'football_data_bet365_proxy': 18, 'football_data_max_market_proxy': 18, 'football_data_average_market_proxy': 18}

- 2026-05-14 | East Riffa vs Qalali Club | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=26.0 | prob=0.3488 | EV=8.0688 | match=1.0
- 2026-05-14 | KA Akureyri vs KF Aegir | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=0.96
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=0.96
- 2026-05-14 | East Riffa vs Qalali Club | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-05-14 | CS Sfaxien vs ES Sahel | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-14 | Mashujaa FC vs Simba SC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3772 | EV=1.829 | match=1.0
- 2026-05-14 | Azam FC vs Pamba Jiji SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-14 | SV Wildon vs SC Stadtwerke Bruck/Mur | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-14 | SKN St Polten vs FC Hertha Wels | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-14 | IF Karlstad Fotbol vs IFK Stocksund | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-14 | VfL Wolfsburg vs Bayern Munich | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-05-14 | KA Akureyri vs KF Aegir | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.274 | EV=1.055 | match=1.0
- 2026-05-14 | Hoenefoss BK vs Stjordals-Blink | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-14 | FK Vidar vs Sotra SK | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3772 | EV=0.9803 | match=1.0
- 2026-05-14 | Hapoel Nir Ramat Hasharon vs Maccabi Kishronot Hadera | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3772 | EV=0.9803 | match=1.0
- 2026-05-14 | AS Fortuna vs Coton Sport de Garoua | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3772 | EV=0.9803 | match=1.0
- 2026-05-14 | Union Saint-Gilloise vs RSC Anderlecht | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=0.96
- 2026-05-14 | Bouri vs AL Tadamun Buri | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-14 | Al-Fateh SC vs Al-Najma | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-14 | Red Arrows vs Green Eagles | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0
- 2026-05-14 | POFC Botev Vratsa vs PFC Montana 1921 | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0