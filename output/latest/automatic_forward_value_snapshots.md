# Automatic Forward Value Snapshots

Combined automatic forward market proxy joined to forward probability predictions.
Includes Football-Data delayed proxy and capped odds-api.io single-event proxy when available.
Not live/full-market coverage and not real-money ready.

Forward prediction rows: 80
Proxy price rows: 10
Matched prediction rows: 10
Value snapshot rows: 30
odds-api.io snapshot rows: 30
Positive EV rows: 15
Source counts: {'odds_api_io_Bet365_ML': 30}

- 2026-05-12 | Gold Coast Knights vs Gold Coast United FC | sel=AWAY | src=odds_api_io_Bet365_ML | odds=21.0 | prob=0.3488 | EV=6.3248 | match=1.0
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-12 | Gwangju FC vs FC Seoul | sel=HOME | src=odds_api_io_Bet365_ML | odds=8.0 | prob=0.3772 | EV=2.0176 | match=1.0
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | sel=HOME | src=odds_api_io_Bet365_ML | odds=7.0 | prob=0.3772 | EV=1.6404 | match=1.0
- 2026-05-12 | Gold Coast Knights vs Gold Coast United FC | sel=DRAW | src=odds_api_io_Bet365_ML | odds=9.5 | prob=0.274 | EV=1.603 | match=1.0
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | match=1.0
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | sel=DRAW | src=odds_api_io_Bet365_ML | odds=5.0 | prob=0.274 | EV=0.37 | match=1.0
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | sel=HOME | src=odds_api_io_Bet365_ML | odds=3.6 | prob=0.3772 | EV=0.35792 | match=1.0
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | sel=HOME | src=odds_api_io_Bet365_ML | odds=3.5 | prob=0.3772 | EV=0.3202 | match=1.0
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | sel=HOME | src=odds_api_io_Bet365_ML | odds=3.3 | prob=0.3772 | EV=0.24476 | match=1.0
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | sel=DRAW | src=odds_api_io_Bet365_ML | odds=4.2 | prob=0.274 | EV=0.1508 | match=1.0
- 2026-05-12 | Gwangju FC vs FC Seoul | sel=DRAW | src=odds_api_io_Bet365_ML | odds=4.2 | prob=0.274 | EV=0.1508 | match=1.0
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | sel=AWAY | src=odds_api_io_Bet365_ML | odds=3.1 | prob=0.3488 | EV=0.08128 | match=1.0
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | sel=DRAW | src=odds_api_io_Bet365_ML | odds=3.8 | prob=0.274 | EV=0.0412 | match=1.0
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | sel=AWAY | src=odds_api_io_Bet365_ML | odds=2.875 | prob=0.3488 | EV=0.0028 | match=1.0
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | sel=DRAW | src=odds_api_io_Bet365_ML | odds=3.5 | prob=0.274 | EV=-0.041 | match=1.0
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | sel=AWAY | src=odds_api_io_Bet365_ML | odds=2.7 | prob=0.3488 | EV=-0.05824 | match=1.0
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | sel=HOME | src=odds_api_io_Bet365_ML | odds=2.45 | prob=0.3772 | EV=-0.07586 | match=1.0
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | sel=DRAW | src=odds_api_io_Bet365_ML | odds=3.2 | prob=0.274 | EV=-0.1232 | match=1.0
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | sel=DRAW | src=odds_api_io_Bet365_ML | odds=3.1 | prob=0.274 | EV=-0.1506 | match=1.0
- 2026-05-12 | Gangwon FC vs Daejeon Citizen FC | sel=HOME | src=odds_api_io_Bet365_ML | odds=2.2 | prob=0.3772 | EV=-0.17016 | match=1.0
- 2026-05-12 | Incheon United FC vs FC Pohang Steelers | sel=DRAW | src=odds_api_io_Bet365_ML | odds=3.0 | prob=0.274 | EV=-0.178 | match=1.0
- 2026-05-12 | Cerro Porteno Asuncion vs Guarani Asuncion | sel=HOME | src=odds_api_io_Bet365_ML | odds=2.1 | prob=0.3772 | EV=-0.20788 | match=1.0
- 2026-05-12 | FC Oleksandriya vs FC Zorya Luhansk | sel=AWAY | src=odds_api_io_Bet365_ML | odds=1.95 | prob=0.3488 | EV=-0.31984 | match=1.0
- 2026-05-12 | Brothers Union vs Mohammedan SC Dhaka | sel=AWAY | src=odds_api_io_Bet365_ML | odds=1.8 | prob=0.3488 | EV=-0.37216 | match=1.0
- 2026-05-12 | Hellenic Athletic Club vs Darwin Hearts FC | sel=AWAY | src=odds_api_io_Bet365_ML | odds=1.75 | prob=0.3488 | EV=-0.3896 | match=1.0
- 2026-05-12 | Gwangju FC vs FC Seoul | sel=AWAY | src=odds_api_io_Bet365_ML | odds=1.38 | prob=0.3488 | EV=-0.518656 | match=1.0
- 2026-05-12 | Canberra White Eagles FC vs Queanbeyan City FC | sel=AWAY | src=odds_api_io_Bet365_ML | odds=1.3 | prob=0.3488 | EV=-0.54656 | match=1.0
- 2026-05-12 | Sunshine Coast Wanderers FC vs Eastern Suburbs FC | sel=AWAY | src=odds_api_io_Bet365_ML | odds=1.27 | prob=0.3488 | EV=-0.557024 | match=1.0
- 2026-05-12 | Gold Coast Knights vs Gold Coast United FC | sel=HOME | src=odds_api_io_Bet365_ML | odds=1.083 | prob=0.3772 | EV=-0.591492 | match=1.0