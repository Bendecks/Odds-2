# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 300
Proxy price rows: 103
Matched prediction rows: 76
Value snapshot rows: 384
odds-api.io snapshot rows: 159
Baseline snapshot rows: 321
Full model snapshot rows: 63
Positive EV rows: 195
Source counts: {'odds_api_io_Bet365_ML': 159, 'football_data_bet365_proxy': 75, 'football_data_max_market_proxy': 75, 'football_data_average_market_proxy': 75}

- 2026-05-13 | Deportes Recoleta vs Universidad Catolica | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3772 | EV=11.8248 | match=1.0
- 2026-05-13 | P-Iirot vs Tampereen Ilves | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.3772 | EV=6.9212 | match=1.0
- 2026-05-13 | IFK Mariehamn vs Puistolan Urheilijat | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-13 | Turun Palloseura vs HJS | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.96
- 2026-05-13 | FC Shakhtar Donetsk vs FC Obolon Kyiv | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.2857 | EV=3.2855 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.96
- 2026-05-13 | Deportes Recoleta vs Universidad Catolica | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.2857 | EV=2.642675 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.2857 | EV=2.4284 | match=1.0
- 2026-05-13 | GKS Pniowek Pawlowice vs KS Gornik Polkowice | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-13 | FC Mali Coura vs Djoliba AC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-13 | P-Iirot vs Tampereen Ilves | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.274 | EV=2.014 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-13 | FC Ordabasy vs Zhetysu Taldykorgan | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.7814
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=1.0
- 2026-05-13 | Heart of Midlothian FC vs Falkirk FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=0.7
- 2026-05-13 | SJK Akatemia vs KPV Kokkola | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-13 | Manama Club vs Etehad Alreef | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-13 | Turun Palloseura vs HJS | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.274 | EV=1.603 | match=1.0
- 2026-05-13 | HNK Rijeka vs GNK Dinamo Zagreb | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3772 | EV=1.4518 | match=1.0