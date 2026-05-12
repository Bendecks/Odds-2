# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 136
Proxy price rows: 99
Matched prediction rows: 61
Value snapshot rows: 447
odds-api.io snapshot rows: 69
Baseline snapshot rows: 345
Full model snapshot rows: 102
Positive EV rows: 217
Source counts: {'football_data_bet365_proxy': 126, 'football_data_max_market_proxy': 126, 'football_data_average_market_proxy': 126, 'odds_api_io_Bet365_ML': 69}

- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.96
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.2857 | EV=3.2855 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.2857 | EV=2.642675 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.2857 | EV=2.4284 | match=1.0
- 2026-05-12 | Hapoel Tel Aviv FC vs Hapoel Petah Tikva FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-12 | TS Galaxy FC vs Mamelodi Sundowns | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.7814
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-13 | Olympiacos Piraeus vs Panathinaikos Athens | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=0.7814
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=1.0
- 2026-05-13 | Heart of Midlothian FC vs Falkirk FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=0.7
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.82 | prob=0.3488 | EV=1.378816 | match=1.0
- 2026-05-13 | Heart of Midlothian FC vs Falkirk FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.82 | prob=0.3488 | EV=1.378816 | match=0.7
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-13 | Heart of Midlothian FC vs Falkirk FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=6.5 | prob=0.3488 | EV=1.2672 | match=0.7
- 2026-05-13 | Glasgow Rangers vs Hibernian FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.0 | prob=0.3488 | EV=1.0928 | match=0.96
- 2026-05-13 | Rangers vs Hibernian | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.5 | prob=0.274 | EV=1.055 | match=0.96
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.5 | prob=0.274 | EV=1.055 | match=0.96
- 2026-05-13 | Glasgow Rangers vs Hibernian FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.75 | prob=0.3488 | EV=1.0056 | match=0.96
- 2026-05-13 | Rangers vs Hibernian | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-12 | FC Luzern vs FC Zurich | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0