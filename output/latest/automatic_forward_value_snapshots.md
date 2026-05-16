# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 300
Proxy price rows: 372
Matched prediction rows: 114
Value snapshot rows: 675
odds-api.io snapshot rows: 171
Baseline snapshot rows: 549
Full model snapshot rows: 126
Positive EV rows: 348
Source counts: {'football_data_max_market_proxy': 171, 'football_data_average_market_proxy': 171, 'odds_api_io_Bet365_ML': 171, 'football_data_bet365_proxy': 162}

- 2026-05-16 | Cerro Porteno vs Recoleta FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=51.0 | prob=0.3488 | EV=16.7888 | match=1.0
- 2026-05-16 | Cerro Porteno vs Recoleta FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=23.0 | prob=0.274 | EV=5.302 | match=1.0
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3488 | EV=3.5344 | match=0.92
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=0.92
- 2026-05-16 | Sp Lisbon vs Gil Vicente | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=12.0 | prob=0.3488 | EV=3.1856 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=13.0 | prob=0.3217 | EV=3.1821 | match=1.0
- 2026-05-17 | Como 1907 vs Parma Calcio | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3488 | EV=2.955392 | match=0.92
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=12.0 | prob=0.3217 | EV=2.8604 | match=1.0
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=16.0 | prob=0.2402 | EV=2.8432 | match=1.0
- 2026-05-17 | Como vs Parma | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=11.34 | prob=0.3217 | EV=2.648078 | match=1.0
- 2026-05-16 | Porto vs Santa Clara | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=10.25 | prob=0.3488 | EV=2.5752 | match=1.0
- 2026-05-16 | Sp Lisbon vs Gil Vicente | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=10.07 | prob=0.3488 | EV=2.512416 | match=1.0
- 2026-05-16 | Sp Lisbon vs Gil Vicente | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=10.0 | prob=0.3488 | EV=2.488 | match=1.0
- 2026-05-16 | Estoril vs Benfica | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-17 | Pisa SC vs SSC Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=0.92
- 2026-05-17 | Pisa SC vs SSC Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=0.92
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-16 | Estoril vs Benfica | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=9.0 | prob=0.3772 | EV=2.3948 | match=1.0
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_bet365_proxy | odds=14.0 | prob=0.2402 | EV=2.3628 | match=1.0
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.5 | prob=0.3488 | EV=2.3136 | match=1.0
- 2026-05-17 | Juventus Turin vs ACF Fiorentina | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=9.4 | prob=0.3488 | EV=2.27872 | match=0.92
- 2026-05-16 | Bayern Munich vs FC Koln | coverage=full_team_strength_match | sel=AWAY | src=football_data_average_market_proxy | odds=12.84 | prob=0.2402 | EV=2.084168 | match=1.0
- 2026-05-16 | Leverkusen vs Hamburg | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.83 | prob=0.3488 | EV=2.079904 | match=1.0
- 2026-05-16 | Porto vs Santa Clara | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=8.82 | prob=0.3488 | EV=2.076416 | match=1.0
- 2026-05-17 | Juventus vs Fiorentina | coverage=full_team_strength_match | sel=AWAY | src=football_data_max_market_proxy | odds=9.4 | prob=0.3269 | EV=2.07286 | match=1.0
- 2026-05-17 | Pisa vs Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=8.06 | prob=0.3772 | EV=2.040232 | match=1.0
- 2026-05-17 | Pisa SC vs SSC Napoli | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=8.06 | prob=0.3772 | EV=2.040232 | match=0.92
- 2026-05-17 | Juventus Turin vs ACF Fiorentina | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=8.5 | prob=0.3488 | EV=1.9648 | match=0.92