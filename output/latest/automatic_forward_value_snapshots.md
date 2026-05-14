# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 278
Proxy price rows: 48
Matched prediction rows: 45
Value snapshot rows: 171
odds-api.io snapshot rows: 117
Baseline snapshot rows: 153
Full model snapshot rows: 18
Positive EV rows: 81
Source counts: {'odds_api_io_Bet365_ML': 111, 'football_data_bet365_proxy': 18, 'football_data_max_market_proxy': 18, 'football_data_average_market_proxy': 18, 'odds_api_io_Bet365 (no latency)_ML': 6}

- 2026-05-14 | FC Salzburg Frauen vs FK Austria Wien | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3772 | EV=3.1492 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=1.0
- 2026-05-14 | KA Akureyri vs KF Aegir | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=0.96
- 2026-05-14 | IF Karlstad Fotbol vs IFK Stocksund | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-14 | Union Saint-Gilloise vs RSC Anderlecht | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-14 | FK Vidar vs Sotra SK | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3772 | EV=0.886 | match=1.0
- 2026-05-14 | JaPS vs FC KTP | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3772 | EV=0.886 | match=1.0
- 2026-05-14 | Viking FK 2 vs Akra | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-14 | Real Madrid vs Real Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_average_market_proxy | odds=6.28 | prob=0.274 | EV=0.72072 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_average_market_proxy | odds=6.28 | prob=0.274 | EV=0.72072 | match=1.0
- 2026-05-14 | KA Akureyri vs KF Aegir | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.274 | EV=0.7125 | match=1.0
- 2026-05-14 | Red Arrows vs Green Eagles | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3488 | EV=0.6568 | match=1.0
- 2026-05-14 | Sidama Bunna SC vs Hadiya Hossana FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.75 | prob=0.3488 | EV=0.6568 | match=1.0
- 2026-05-14 | JaPS vs FC KTP | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.274 | EV=0.644 | match=1.0
- 2026-05-14 | Oppsal IF vs Raade IL | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | match=1.0
- 2026-05-14 | SJK-J vs FC Kiisto | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3772 | EV=0.634408 | match=1.0
- 2026-05-14 | FK Septemvri Sofia vs FK Spartak 1918 Varna | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.5 | prob=0.3488 | EV=0.5696 | match=1.0
- 2026-05-14 | FC Salzburg Frauen vs FK Austria Wien | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.274 | EV=0.507 | match=1.0
- 2026-05-14 | Mtibwa Sugar FC vs Kmc FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3488 | EV=0.3952 | match=1.0
- 2026-05-14 | Viking FK 2 vs Akra | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | match=1.0
- 2026-05-14 | IF Karlstad Fotbol vs IFK Stocksund | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | match=1.0