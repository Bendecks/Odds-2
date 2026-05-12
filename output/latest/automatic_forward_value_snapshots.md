# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 160
Proxy price rows: 101
Matched prediction rows: 63
Value snapshot rows: 441
odds-api.io snapshot rows: 72
Baseline snapshot rows: 441
Full model snapshot rows: 0
Positive EV rows: 204
Source counts: {'football_data_bet365_proxy': 123, 'football_data_max_market_proxy': 123, 'football_data_average_market_proxy': 123, 'odds_api_io_Bet365_ML': 72}

- 2026-05-12 | FC Elva vs Paide Linnameeskond | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=41.0 | prob=0.3772 | EV=14.4652 | match=1.0
- 2026-05-12 | FC Inter Turku vs JS Hercules | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3488 | EV=10.8592 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=1.0
- 2026-05-12 | FC Inter Turku vs JS Hercules | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.274 | EV=4.206 | match=1.0
- 2026-05-12 | Mohun Bagan Super Giant vs Inter Kashi FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=0.96
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-12 | FC Elva vs Paide Linnameeskond | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=15.0 | prob=0.274 | EV=3.11 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.7814
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=1.0
- 2026-05-12 | URA FC vs Calvary | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-13 | Heart of Midlothian FC vs Falkirk FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=0.7
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-12 | FK Liepaja vs Ogre United | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-13 | Heart of Midlothian FC vs Falkirk FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.82 | prob=0.3488 | EV=1.378816 | match=0.7
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.82 | prob=0.3488 | EV=1.378816 | match=1.0
- 2026-05-12 | FC Epitsentr Kamianets-Podilskyi vs FC Polissya Zhytomyr | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3772 | EV=1.3575 | match=1.0
- 2026-05-13 | Heart of Midlothian FC vs Falkirk FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=6.5 | prob=0.3488 | EV=1.2672 | match=0.7
- 2026-05-12 | Singida Black Stars SC vs Namungo FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-13 | Glasgow Rangers vs Hibernian FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.0 | prob=0.3488 | EV=1.0928 | match=0.96
- 2026-05-13 | Rangers vs Hibernian | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.5 | prob=0.274 | EV=1.055 | match=0.96