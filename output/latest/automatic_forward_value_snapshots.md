# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 300
Proxy price rows: 146
Matched prediction rows: 100
Value snapshot rows: 552
odds-api.io snapshot rows: 165
Baseline snapshot rows: 444
Full model snapshot rows: 108
Positive EV rows: 306
Source counts: {'odds_api_io_Bet365_ML': 165, 'football_data_max_market_proxy': 135, 'football_data_average_market_proxy': 135, 'football_data_bet365_proxy': 117}

- 2026-05-24 | Belconnen United vs Canberra Olympic | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=29.0 | prob=0.3488 | EV=9.1152 | match=1.0
- 2026-05-24 | Uwa Nedlands FC vs Fremantle City FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=23.0 | prob=0.3772 | EV=7.6756 | match=1.0
- 2026-05-24 | FC Slovan Liberec vs Slavia Prague | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-24 | North Lakes United vs Mitchelton FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-24 | Manchester City vs Aston Villa | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=0.96
- 2026-05-24 | Gold Coast United FC vs Eastern Suburbs FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3772 | EV=2.2062 | match=1.0
- 2026-05-24 | Manchester City vs Aston Villa | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.3488 | EV=2.1392 | match=0.96
- 2026-05-24 | Belconnen United vs Canberra Olympic | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.274 | EV=2.014 | match=1.0
- 2026-05-24 | Uwa Nedlands FC vs Fremantle City FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.274 | EV=2.014 | match=1.0
- 2026-05-24 | Manchester City vs Aston Villa | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.39 | prob=0.3488 | EV=1.926432 | match=0.96
- 2026-05-24 | SSC Napoli vs Udinese Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.92
- 2026-05-24 | SSC Napoli vs Udinese Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.92
- 2026-05-24 | Man City vs Aston Villa | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.29 | EV=1.755 | match=1.0
- 2026-05-24 | Subiaco AFC vs Perth Azzurri | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-24 | UD Las Palmas vs Real Zaragoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=0.92
- 2026-05-24 | Las Palmas vs Zaragoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-24 | Man City vs Aston Villa | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=9.0 | prob=0.29 | EV=1.61 | match=1.0
- 2026-05-24 | Napoli vs Udinese | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=8.0 | prob=0.306 | EV=1.448 | match=1.0
- 2026-05-24 | Napoli vs Udinese | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.306 | EV=1.448 | match=1.0
- 2026-05-24 | Las Palmas vs Zaragoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-24 | Lake Macquarie City FC vs Charlestown Azzurri FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-24 | UD Las Palmas vs Real Zaragoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=7.0 | prob=0.3488 | EV=1.4416 | match=0.92
- 2026-05-24 | Grange Thistle vs Samford Rangers | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-24 | Man City vs Aston Villa | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=8.39 | prob=0.29 | EV=1.4331 | match=1.0
- 2026-05-24 | UD Las Palmas vs Real Zaragoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.73 | prob=0.3488 | EV=1.347424 | match=0.92
- 2026-05-24 | Las Palmas vs Zaragoza | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.73 | prob=0.3488 | EV=1.347424 | match=1.0
- 2026-05-24 | SSC Napoli vs Udinese Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=6.72 | prob=0.3488 | EV=1.343936 | match=0.92
- 2026-05-24 | Union Saint-Gilloise vs RSC Anderlecht | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.66 | prob=0.3488 | EV=1.323008 | match=0.7503
- 2026-05-24 | St. Gilloise vs Anderlecht | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.66 | prob=0.3488 | EV=1.323008 | match=1.0
- 2026-05-24 | Tegevajaro Miyazaki vs Reilac Shiga FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0