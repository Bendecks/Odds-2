# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 101
Proxy price rows: 57
Matched prediction rows: 53
Value snapshot rows: 183
odds-api.io snapshot rows: 156
Baseline snapshot rows: 174
Full model snapshot rows: 9
Positive EV rows: 77
Source counts: {'odds_api_io_Bet365_ML': 156, 'football_data_bet365_proxy': 9, 'football_data_max_market_proxy': 9, 'football_data_average_market_proxy': 9}

- 2026-05-18 | Universidad de Concepcion vs Colo Colo | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=26.0 | prob=0.2712 | EV=6.0512 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=23.0 | prob=0.2712 | EV=5.2376 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=22.13 | prob=0.2712 | EV=5.001656 | match=1.0
- 2026-05-18 | PFC Montana 1921 vs FK Spartak 1918 Varna | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.3772 | EV=4.658 | match=1.0
- 2026-05-18 | Universidad de Concepcion vs Colo Colo | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.274 | EV=4.206 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=DRAW | src=football_data_bet365_proxy | odds=11.0 | prob=0.2596 | EV=1.8556 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=DRAW | src=football_data_max_market_proxy | odds=11.0 | prob=0.2596 | EV=1.8556 | match=1.0
- 2026-05-18 | South Melbourne FC vs Caroline Springs George Cross FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3772 | EV=1.829 | match=1.0
- 2026-05-18 | FC Farul Constanta vs Metaloglobus Bucuresti | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-18 | HB Torshavn vs Eb/Streymur | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-18 | Arsenal vs Burnley | coverage=full_team_strength_match | sel=DRAW | src=football_data_average_market_proxy | odds=10.12 | prob=0.2596 | EV=1.627152 | match=1.0
- 2026-05-18 | FK Kudrivka vs LNZ Cherkasy | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0
- 2026-05-18 | FC Lokomotiv 1929 Sofia vs PFC Slavia Sofia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-18 | PFC Dobrudzha Dobrich vs POFC Botev Vratsa | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-18 | Tanjong Pagar United vs Hougang United FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-05-18 | FC Zorya Luhansk vs FC Polissya Zhytomyr | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3772 | EV=0.9803 | match=1.0
- 2026-05-18 | FC Haka Valkeakoski vs HJK Klubi 04 | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-18 | Club Deportivo Magallanes vs Deportes Recoleta | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-18 | FC Petrolul Ploiesti vs ASC Otelul Galati | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-18 | Talaea El Gaish vs Pharco FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.25 | prob=0.3488 | EV=0.8312 | match=1.0
- 2026-05-18 | FC Shirak Gyumri vs FC Urartu Yerevan | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.5 | prob=0.3772 | EV=0.6974 | match=1.0
- 2026-05-18 | FC Farul Constanta vs Metaloglobus Bucuresti | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.274 | EV=0.644 | match=1.0
- 2026-05-18 | PFC Montana 1921 vs FK Spartak 1918 Varna | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.274 | EV=0.644 | match=1.0
- 2026-05-18 | HB Torshavn vs Eb/Streymur | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.274 | EV=0.5755 | match=1.0
- 2026-05-18 | CS Italiano vs CSCD Laferrere | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.5 | prob=0.3488 | EV=0.5696 | match=1.0
- 2026-05-18 | Kahrabaa Ismailia vs Haras El Hodood | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.5 | prob=0.3488 | EV=0.5696 | match=1.0
- 2026-05-18 | AL Nasr SC (OMA) vs Samail SC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=4.333 | prob=0.3488 | EV=0.51135 | match=1.0
- 2026-05-18 | Laholms FK vs FC Rosengaard 1917 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | match=1.0
- 2026-05-18 | AB Argir vs Vikingur Gota | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=4.0 | prob=0.3772 | EV=0.5088 | match=1.0