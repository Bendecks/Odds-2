# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 300
Proxy price rows: 271
Matched prediction rows: 138
Value snapshot rows: 1014
odds-api.io snapshot rows: 225
Baseline snapshot rows: 846
Full model snapshot rows: 168
Positive EV rows: 515
Source counts: {'football_data_max_market_proxy': 267, 'football_data_average_market_proxy': 267, 'football_data_bet365_proxy': 255, 'odds_api_io_Bet365_ML': 225}

- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=0.8114
- 2026-05-17 | Elversberg vs Preußen Münster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=1.0
- 2026-05-17 | Inter vs Verona | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=15.0 | prob=0.292 | EV=3.38 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3217 | EV=3.1821 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3217 | EV=2.8604 | match=1.0
- 2026-05-17 | Fenerbahce vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-17 | Fenerbahce Istanbul vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=11.0 | prob=0.3488 | EV=2.8368 | match=0.96
- 2026-05-17 | Inter vs Verona | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.88 | prob=0.292 | EV=2.76096 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3217 | EV=2.648078 | match=1.0
- 2026-05-17 | Elversberg vs Preußen Münster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.13 | prob=0.3488 | EV=2.533344 | match=1.0
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.13 | prob=0.3488 | EV=2.533344 | match=0.8114
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=10.0 | prob=0.3488 | EV=2.488 | match=0.8114
- 2026-05-17 | Elversberg vs Preußen Münster | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Fenerbahce vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=9.53 | prob=0.3488 | EV=2.324064 | match=1.0
- 2026-05-17 | Fenerbahce Istanbul vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=9.53 | prob=0.3488 | EV=2.324064 | match=0.96
- 2026-05-17 | Elversberg vs Preußen Münster | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.8114
- 2026-05-17 | Fenerbahce vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-17 | Fenerbahce Istanbul vs Eyupspor | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-17 | SV 07 Elversberg vs SC Preussen 06 Munster | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3488 | EV=2.1392 | match=1.0
- 2026-05-17 | Juventus vs Fiorentina | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=9.4 | prob=0.3269 | EV=2.07286 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=8.06 | prob=0.3772 | EV=2.040232 | match=1.0
- 2026-05-17 | OGC Nice vs FC Metz | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.96
- 2026-05-17 | Lille OSC vs AJ Auxerre | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.92
- 2026-05-17 | Hamilton Academical WFC vs Montrose FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3772 | EV=1.829 | match=1.0
- 2026-05-17 | Nijmegen vs Go Ahead Eagles | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-17 | Juventus vs Fiorentina | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=8.5 | prob=0.3269 | EV=1.77865 | match=1.0
- 2026-05-17 | Lille OSC vs AJ Auxerre | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=7.87 | prob=0.3488 | EV=1.745056 | match=0.92
- 2026-05-17 | Juventus vs Fiorentina | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=8.38 | prob=0.3269 | EV=1.739422 | match=1.0