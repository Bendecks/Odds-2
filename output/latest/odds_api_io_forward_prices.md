# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 3 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 223
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 68532510, 71564480, 71550354, 69195330, 69195326, 69195328, 71423470, 68532514, 68995164, 70241506, 71491232, 68995166, 68995168, 70926690, 71427486, 70224450, 68995170, 71426276, 70372968, 71426274, 65867826, 71491226, 71267604, 71553502, 71553504, 71039180, 71039184, 71553506, 71018812, 71218282, 70926694, 71501228, 68492530, 69090928, 70224448, 66053824, 66614160, 67091400, 71427488, 66053814, 70929722, 70929728, 70929726, 70929724, 71553482, 71218280, 71122914, 71218294, 68492532, 71183230, 67091402, 68214660, 68214666, 71208150, 70683972, 71509098, 69924106, 71423454, 71344718, 71344720, 71344716, 71558030, 67017952, 71342374, 71553510, 71553508, 71427484, 70224446, 67017938, 71218284, 67126668, 66918130, 67017940, 70302534, 67017942, 71386150, 67017944, 67017946, 71562580, 67017948
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 223
Event selection diagnostic rows: 14680
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 3
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 84
Latest x-ratelimit-reset: 2026-05-20T03:35:27Z
Latest retry-after: None

- 2026-05-20 05:00 | Melbourne City FC vs Tokyo Verdy Beleza | odds_api_io_Bet365_ML | 2.75/3.7/2.05
- 2026-05-20 07:30 | Taichung Blue Whale vs New Taipei Hang Yuen | odds_api_io_Bet365_ML | 3.6/4.0/1.7
- 2026-05-20 09:00 | Sydney Olympic FC vs University of NSW | odds_api_io_Bet365_ML | 3.9/4.1/1.615
- 2026-05-20 09:30 | Canberra Olympic vs Canberra Croatia FC | odds_api_io_Bet365_ML | 3.8/3.9/1.666
- 2026-05-20 09:30 | Tuggeranong United FC vs Belconnen United | odds_api_io_Bet365_ML | 41.0/19.0/1.025
- 2026-05-20 09:30 | West Canberra Wanderers FC vs Majura FC | odds_api_io_Bet365_ML | 1.071/10.0/26.0
- 2026-05-20 10:00 | Hunters FC vs FC Ulaanbaatar | odds_api_io_Bet365_ML | 9.0/6.0/1.2
- 2026-05-20 10:00 | Naegohyang Womens FC vs Suwon WFC | odds_api_io_Bet365_ML | 2.0/3.5/3.1
- 2026-05-20 11:00 | Liaoning Tieren FC vs Qingdao Hainiu FC | odds_api_io_Bet365_ML | 2.2/3.5/3.1
- 2026-05-20 11:00 | Preah Khan Reach Svay Rieng FC vs Boeung Ket Angkor FC | odds_api_io_Bet365_ML | 1.7/3.9/3.7

## Event selection diagnostics

- src=events_bookmaker_filtered | query=Kuopion Palloseura | target=Kuopion Palloseura vs FF Jaro | candidate=Kuopion Palloseura vs FF Jaro | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SK Polanka Nad Odrou | target=SK Polanka Nad Odrou vs MFk Karvina B | candidate=SK Polanka Nad Odrou vs MFk Karvina B | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Shanghai Shenhua FC | target=Shanghai Shenhua FC vs Wuhan Three Towns FC | candidate=Shanghai Shenhua FC vs Wuhan Three Towns FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Melbourne City FC | target=Melbourne City FC vs Tokyo Verdy Beleza | candidate=Melbourne City FC vs Tokyo Verdy Beleza | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IK Start | target=IK Start vs Bodoe/Glimt | candidate=IK Start vs Bodoe/Glimt | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Masry Club | target=Al Masry Club vs AL Ahly SC (EGY) | candidate=Al Masry Club vs AL Ahly SC (EGY) | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Ataka | target=FK Ataka vs FA Siauliai | candidate=FK Ataka vs FA Siauliai | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Hunters FC | target=Hunters FC vs FC Ulaanbaatar | candidate=Hunters FC vs FC Ulaanbaatar | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Grobinas SC/LFS | target=Grobinas SC/LFS vs SK Super Nova | candidate=Grobinas SC/LFS vs SK Super Nova | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=de Graafschap | target=de Graafschap vs ADO Den Haag | candidate=de Graafschap vs ADO Den Haag | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=ES Zarzis | target=ES Zarzis vs CA Bizertin | candidate=ES Zarzis vs CA Bizertin | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Al Shorta SC | target=Al Shorta SC vs Erbil SC | candidate=Al Shorta SC vs Erbil SC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Gareji Sagarejo | target=FC Gareji Sagarejo vs FC Merani Martvili | candidate=FC Gareji Sagarejo vs FC Merani Martvili | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Kuressaare | target=FC Kuressaare vs FC Nomme United | candidate=FC Kuressaare vs FC Nomme United | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SCU Torreense | target=SCU Torreense vs Casa Pia Lisbon | candidate=SCU Torreense vs Casa Pia Lisbon | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Newroz SC | target=Newroz SC vs Zakho FC | candidate=Newroz SC vs Zakho FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=CR Temouchent | target=CR Temouchent vs US Chaouia | candidate=CR Temouchent vs US Chaouia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Canberra Olympic | target=Canberra Olympic vs Canberra Croatia FC | candidate=Canberra Olympic vs Canberra Croatia FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=PFC Lokomotiv Plovdiv | target=PFC Lokomotiv Plovdiv vs PFC CSKA Sofia | candidate=PFC Lokomotiv Plovdiv vs PFC CSKA Sofia | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Maccabi Petah Tikva FC | target=Maccabi Petah Tikva FC vs Bnei Yehuda Tel Aviv FC | candidate=Maccabi Petah Tikva FC vs Bnei Yehuda Tel Aviv FC | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 71491232
- multi_odds_match: No multi-odds payload matched event 68995166
- multi_odds_match: No multi-odds payload matched event 68995168
- multi_odds_match: No multi-odds payload matched event 70926690
- multi_odds_match: No multi-odds payload matched event 71427486
- multi_odds_match: No multi-odds payload matched event 70224450
- multi_odds_match: No multi-odds payload matched event 68995170
- multi_odds_match: No multi-odds payload matched event 71426276
- multi_odds_match: No multi-odds payload matched event 70372968
- multi_odds_match: No multi-odds payload matched event 71426274