# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 300
Proxy price rows: 357
Matched prediction rows: 87
Value snapshot rows: 615
odds-api.io snapshot rows: 147
Baseline snapshot rows: 513
Full model snapshot rows: 102
Positive EV rows: 312
Source counts: {'football_data_max_market_proxy': 162, 'football_data_average_market_proxy': 162, 'odds_api_io_Bet365_ML': 147, 'football_data_bet365_proxy': 144}

- 2026-05-16 | CE Carroi vs Inter Club de Escaldes | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3772 | EV=5.4124 | match=1.0
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=16.0 | prob=0.3488 | EV=4.5808 | match=0.7308
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=14.0 | prob=0.3488 | EV=3.8832 | match=0.7308
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=12.84 | prob=0.3488 | EV=3.478592 | match=0.7308
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=16.0 | prob=0.2402 | EV=2.8432 | match=1.0
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-16 | Porto vs Santa Clara | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=10.25 | prob=0.3488 | EV=2.5752 | match=1.0
- 2026-05-16 | FC Porto vs Santa Clara Azores | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=10.25 | prob=0.3488 | EV=2.5752 | match=0.96
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=14.0 | prob=0.2402 | EV=2.3628 | match=1.0
- 2026-05-16 | Bayer Leverkusen vs Hamburger SV | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=0.92
- 2026-05-16 | Bayer Leverkusen vs Hamburger SV | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=0.92
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.84 | prob=0.2402 | EV=2.084168 | match=1.0
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.83 | prob=0.3488 | EV=2.079904 | match=1.0
- 2026-05-16 | Bayer Leverkusen vs Hamburger SV | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.83 | prob=0.3488 | EV=2.079904 | match=0.92
- 2026-05-16 | FC Porto vs Santa Clara Azores | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.82 | prob=0.3488 | EV=2.076416 | match=0.96
- 2026-05-16 | Porto vs Santa Clara | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.82 | prob=0.3488 | EV=2.076416 | match=1.0
- 2026-05-16 | Porto vs Santa Clara | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=1.0
- 2026-05-16 | FC Porto vs Santa Clara Azores | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.0 | prob=0.3488 | EV=1.7904 | match=0.96
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.2402 | EV=1.6422 | match=0.7308
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=0.92
- 2026-05-16 | Bayer Leverkusen vs Hamburger SV | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-16 | KSZO Ostrowiec Swietokrzyski vs Sokol Kolbuszowa Dolna | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_bet365_proxy | odds=9.5 | prob=0.274 | EV=1.603 | match=0.7308
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_max_market_proxy | odds=9.5 | prob=0.274 | EV=1.603 | match=0.7308
- 2026-05-16 | Molde FK vs Kristiansund BK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-16 | Racing Santander vs Real Valladolid | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.0 | prob=0.3488 | EV=1.4416 | match=0.92
- 2026-05-16 | Santander vs Valladolid | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=7.0 | prob=0.3488 | EV=1.4416 | match=1.0
- 2026-05-16 | Bayern Munich vs 1. FC Cologne | coverage=baseline_unmatched_fixture | sel=DRAW | src=football_data_average_market_proxy | odds=8.71 | prob=0.274 | EV=1.38654 | match=0.7308