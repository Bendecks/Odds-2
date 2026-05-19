# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes capped odds-api.io proxy when available. Not live/full-market coverage and not real-money ready.
Baseline model rows are coverage-expansion observations only.

Forward prediction rows: 210
Proxy price rows: 77
Matched prediction rows: 58
Value snapshot rows: 294
odds-api.io snapshot rows: 159
Baseline snapshot rows: 294
Full model snapshot rows: 0
Positive EV rows: 145
Source counts: {'odds_api_io_Bet365_ML': 159, 'football_data_max_market_proxy': 48, 'football_data_average_market_proxy': 48, 'football_data_bet365_proxy': 39}

- 2026-05-19 | FK Pempininkai vs FK Minija 2017 | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=34.0 | prob=0.3772 | EV=11.8248 | match=1.0
- 2026-05-19 | FC Haka J vs Saaksjaerven Loiske | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=19.0 | prob=0.3488 | EV=5.6272 | match=1.0
- 2026-05-19 | CA Rosario Central vs UCV FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-19 | Fluminense FC RJ vs Club Bolivar | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.3488 | EV=4.9296 | match=1.0
- 2026-05-19 | FK Pempininkai vs FK Minija 2017 | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=17.0 | prob=0.274 | EV=3.658 | match=1.0
- 2026-05-19 | FK Riteriai vs FK Kauno Zalgiris | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=12.0 | prob=0.3772 | EV=3.5264 | match=1.0
- 2026-05-19 | FC Noah Yerevan vs Ararat Yerevan FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=11.0 | prob=0.3488 | EV=2.8368 | match=1.0
- 2026-05-19 | FC Haka J vs Saaksjaerven Loiske | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=13.0 | prob=0.274 | EV=2.562 | match=1.0
- 2026-05-19 | Ben Aknoun vs ES Mostaganem | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=8.5 | prob=0.3488 | EV=1.9648 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_bet365_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_max_market_proxy | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-19 | FC Kiisto vs Vpv | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=7.5 | prob=0.3488 | EV=1.616 | match=1.0
- 2026-05-21 | Mechelen vs Club Brugge | coverage=baseline_unmatched_fixture | sel=HOME | src=football_data_average_market_proxy | odds=6.57 | prob=0.3772 | EV=1.478204 | match=1.0
- 2026-05-19 | FC Noah Yerevan vs Ararat Yerevan FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.0 | prob=0.274 | EV=1.466 | match=1.0
- 2026-05-19 | Hapoel Petah Tikva FC vs Beitar Jerusalem FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=6.25 | prob=0.3772 | EV=1.3575 | match=1.0
- 2026-05-19 | Velez Nevesinje vs FK Vlasenica | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.5 | prob=0.3488 | EV=1.2672 | match=1.0
- 2026-05-19 | KRC Genk vs Royal Antwerp FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-21 | Atromitos vs Panserraikos | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=6.0 | prob=0.3488 | EV=1.0928 | match=1.0
- 2026-05-19 | Genk vs Antwerp | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=6.0 | prob=0.3488 | EV=1.0928 | match=0.92
- 2026-05-19 | Klaipedos Fsm vs Dfk Dainava Alytus | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.5 | prob=0.3772 | EV=1.0746 | match=1.0
- 2026-05-19 | Genk vs Antwerp | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.8 | prob=0.3488 | EV=1.02304 | match=1.0
- 2026-05-19 | KRC Genk vs Royal Antwerp FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_max_market_proxy | odds=5.8 | prob=0.3488 | EV=1.02304 | match=0.92
- 2026-05-19 | AC Monza vs Juve Stabia | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-19 | LSK Kvinner FK vs Hoenefoss BK | coverage=baseline_unmatched_fixture | sel=AWAY | src=odds_api_io_Bet365_ML | odds=5.75 | prob=0.3488 | EV=1.0056 | match=1.0
- 2026-05-19 | KRC Genk vs Royal Antwerp FC | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=0.92
- 2026-05-19 | Genk vs Antwerp | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_bet365_proxy | odds=5.5 | prob=0.3488 | EV=0.9184 | match=1.0
- 2026-05-19 | CA Rosario Central vs UCV FC | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-19 | FK Riteriai vs FK Kauno Zalgiris | coverage=baseline_unmatched_fixture | sel=DRAW | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.274 | EV=0.918 | match=1.0
- 2026-05-19 | Boston Bolts vs Vermont Green FC | coverage=baseline_unmatched_fixture | sel=HOME | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.3772 | EV=0.886 | match=1.0
- 2026-05-19 | Genk vs Antwerp | coverage=baseline_unmatched_fixture | sel=AWAY | src=football_data_average_market_proxy | odds=5.36 | prob=0.3488 | EV=0.869568 | match=1.0