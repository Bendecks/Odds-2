# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 300
Proxy price rows: 79
Matched prediction rows: 71
Value snapshot rows: 315
odds-api.io snapshot rows: 162
Baseline snapshot rows: 303
Full model snapshot rows: 12
Positive EV rows: 159
Source counts: {'odds_api_io_Bet365_ML': 159, 'football_data_bet365_proxy': 51, 'football_data_max_market_proxy': 51, 'football_data_average_market_proxy': 51, 'odds_api_io_Bet365 (no latency)_ML': 3}

- 2026-05-31 | Uwa Nedlands FC vs Balcatta FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3772 | EV=11.8248 | match=1.0
- 2026-05-31 | Canberra Olympic vs West Canberra Wanderers FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3488 | EV=10.8592 | match=1.0
- 2026-05-31 | Perth Azzurri vs Sorrento FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3488 | EV=9.1152 | match=1.0
- 2026-05-31 | South Hobart FC 2 vs Hobart United FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-31 | Tuggeranong United FC vs Majura FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-31 | Japan vs Iceland | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-31 | Magic United Tfa vs Lions FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3772 | EV=3.1492 | match=1.0
- 2026-05-31 | Canberra Olympic vs West Canberra Wanderers FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-05-31 | Perth Azzurri vs Sorrento FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-05-31 | Uwa Nedlands FC vs Balcatta FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.274 | EV=2.288 | match=1.0
- 2026-05-31 | Santander vs Cadiz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-31 | Racing Santander vs Cadiz CF | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-31 | Santander vs Cadiz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-31 | Racing Santander vs Cadiz CF | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-31 | SK Slovan HAC vs SV Wienerberg 1921 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-31 | Canberra Croatia FC vs Belconnen United | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-31 | Real Madrid vs Granada CF | coverage=full_team_strength_match | sel=AWAY | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.2345 | EV=1.814 | match=1.0
- 2026-05-31 | Santander vs Cadiz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.9 | prob=0.3488 | EV=1.75552 | match=1.0
- 2026-05-31 | Racing Santander vs Cadiz CF | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.9 | prob=0.3488 | EV=1.75552 | match=0.96
- 2026-05-31 | South Hobart FC 2 vs Hobart United FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=10.0 | prob=0.274 | EV=1.74 | match=1.0
- 2026-05-31 | UD Almeria vs Real Valladolid | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.8 | prob=0.3488 | EV=1.72064 | match=0.92
- 2026-05-31 | Redcliffe Dolphins vs Springfield United | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-31 | Subiaco AFC vs Fremantle City FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-31 | Siheung Citizen FC vs FC Mokpo | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-31 | UD Almeria vs Real Valladolid | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.54 | prob=0.3488 | EV=1.281152 | match=0.92
- 2026-05-31 | Clarence Zebras FC vs South East United FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-31 | Burgos vs Andorra | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.33 | prob=0.3488 | EV=1.207904 | match=1.0
- 2026-05-31 | AGF Aarhus vs HB Koege | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3772 | EV=1.1689 | match=1.0
- 2026-05-31 | Almeria vs Valladolid | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=7.8 | prob=0.2746 | EV=1.14188 | match=1.0
- 2026-05-31 | CD Tenerife vs RC Deportivo De La Coruna | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0