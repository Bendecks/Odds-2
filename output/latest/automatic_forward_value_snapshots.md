# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 27
Proxy price rows: 78
Matched prediction rows: 27
Value snapshot rows: 243
odds-api.io snapshot rows: 0
Baseline snapshot rows: 144
Full model snapshot rows: 99
Positive EV rows: 119
Source counts: {'football_data_bet365_proxy': 81, 'football_data_max_market_proxy': 81, 'football_data_average_market_proxy': 81}

- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.3488 | EV=4.232 | match=0.96
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.3488 | EV=3.4472 | match=0.96
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.2857 | EV=3.2855 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.5 | prob=0.3488 | EV=3.0112 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.75 | prob=0.2857 | EV=2.642675 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.42 | prob=0.3488 | EV=2.634496 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.2857 | EV=2.4284 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-13 | Olympiakos vs Panathinaikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.59 | prob=0.3488 | EV=1.647392 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.82 | prob=0.3488 | EV=1.378816 | match=1.0
- 2026-05-13 | Hearts vs Falkirk | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-13 | Rangers vs Hibernian | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.5 | prob=0.274 | EV=1.055 | match=0.96
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.5 | prob=0.274 | EV=1.055 | match=0.96
- 2026-05-13 | Rangers vs Hibernian | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=DRAW | src=football_data_max_market_proxy | odds=7.5 | prob=0.2635 | EV=0.97625 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=DRAW | src=football_data_bet365_proxy | odds=7.5 | prob=0.2635 | EV=0.97625 | match=1.0
- 2026-05-13 | Rangers vs Hibernian | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=5.62 | prob=0.3488 | EV=0.960256 | match=1.0
- 2026-05-13 | Manchester City vs Crystal Palace | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_average_market_proxy | odds=7.03 | prob=0.274 | EV=0.92622 | match=0.96
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-14 | Real Madrid vs Oviedo | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-13 | Man City vs Crystal Palace | coverage=full_team_strength_match | sel=DRAW | src=football_data_average_market_proxy | odds=7.03 | prob=0.2635 | EV=0.852405 | match=1.0
- 2026-05-13 | Levadeiakos vs OFI Crete | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0
- 2026-05-12 | Asteras Tripolis vs Panserraikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0
- 2026-05-13 | PAOK vs AEK | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0
- 2026-05-13 | PAOK vs AEK | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.0 | prob=0.3488 | EV=0.744 | match=1.0