# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 274
Proxy price rows: 85
Matched prediction rows: 75
Value snapshot rows: 327
odds-api.io snapshot rows: 174
Baseline snapshot rows: 318
Full model snapshot rows: 9
Positive EV rows: 160
Source counts: {'odds_api_io_Bet365_ML': 174, 'football_data_bet365_proxy': 51, 'football_data_max_market_proxy': 51, 'football_data_average_market_proxy': 51}

- 2026-05-31 | Madrid CFF vs FC Barcelona | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=1.0
- 2026-05-31 | Madrid CFF vs FC Barcelona | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.274 | EV=3.658 | match=1.0
- 2026-05-31 | Santander vs Cadiz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-31 | Santander vs Cadiz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-31 | Racing Santander vs Cadiz CF | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-31 | Racing Santander vs Cadiz CF | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-31 | NK Celik Zenica vs FK Igman Konjic | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-31 | Racing Santander vs Cadiz CF | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.9 | prob=0.3488 | EV=1.75552 | match=0.96
- 2026-05-31 | Santander vs Cadiz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.9 | prob=0.3488 | EV=1.75552 | match=1.0
- 2026-05-31 | UD Almeria vs Real Valladolid | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.8 | prob=0.3488 | EV=1.72064 | match=0.92
- 2026-05-31 | Brighton and Hove Albion WFC vs Manchester City WFC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-31 | India vs Bangladesh | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-31 | Esperance Sportive de Tunis vs ES Zarzis | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-31 | Kongsvinger IL Toppfotball vs Aasane Fotball | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-31 | UD Almeria vs Real Valladolid | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.54 | prob=0.3488 | EV=1.281152 | match=0.92
- 2026-05-31 | Burgos vs Andorra | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.33 | prob=0.3488 | EV=1.207904 | match=1.0
- 2026-05-31 | Levanger FK vs IK Junkeren | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3488 | EV=1.18 | match=1.0
- 2026-05-31 | Almeria vs Valladolid | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=7.8 | prob=0.2746 | EV=1.14188 | match=1.0
- 2026-05-31 | Ebk vs HJK Akatemia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-31 | Burgos vs Andorra | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=5.98 | prob=0.3488 | EV=1.085824 | match=1.0
- 2026-05-31 | Husqvarna FF vs Linkopings FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-05-31 | UD Almeria vs Real Valladolid | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.75 | prob=0.3488 | EV=1.0056 | match=0.92
- 2026-05-31 | Burgos vs Andorra | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-31 | Cordoba CF vs SD Huesca | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=0.96
- 2026-05-31 | Cordoba vs Huesca | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-31 | Paide Linnameeskond vs FC Kuressaare | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-31 | Cordoba vs Huesca | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-31 | Castellon vs Eibar | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-31 | Cordoba CF vs SD Huesca | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=0.96
- 2026-05-31 | CD Castellon vs SD Eibar | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=0.92