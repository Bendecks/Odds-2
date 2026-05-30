# odds-api.io Forward Price Fetch

Cautious optional API source. Hard-capped by ODDS_API_IO_MAX_CALLS, ODDS_API_IO_MAX_EVENTS, and ODDS_API_IO_MAX_PRICE_EVENTS.
Primary discovery uses /events with sport=football, status=pending, bookmaker filter, from/to RFC3339, limit and skip; /events/search is fallback only.
Selected events are matched to model-covered forward fixtures by home/away/date confidence, then priced through documented /v3/odds/multi.
At least one API call is reserved for /odds/multi when any selected event exists.
Captures provider rate-limit headers from each authenticated API response.
Not real-money ready until validated against forward results and other sources.

Enabled: True
Calls used: 4 / 14
Max discovery calls: 13
Events bookmaker: Bet365
Events discovery rows: 528
Events max pages: 6
Events lookahead days: 14
Max events per page/search: 180
Max priced events: 80
Minimum event match confidence: 0.72
Discovery mode: bookmaker_filtered_events_then_search_fallback_then_reserved_multi_odds
Query source: forward_fixture_predictions
Search fallback used: False
Search queries used: 
Selected event IDs: 67919294, 71732928, 61541450, 61541452, 71773858, 61911554, 68311632, 61894086, 61898662, 62215538, 68320820, 71799058, 62216176, 61894084, 68194442, 68492556, 67018394, 71622034, 68310924, 68311630, 67850008, 70365244, 67091330, 68310926, 68320202, 68377720, 68307880, 68307878, 67091332, 67091336, 61711886, 62036926, 65964272, 62216498, 67015218, 67017976, 69972752, 69972750, 71732838, 69972746, 71732842, 71732836, 67017978, 69972744, 67921108, 61711896, 71615194, 68194446, 61466407, 67843322, 68194444, 68311634, 68311636, 61894082, 71620934, 61541456, 61623948, 61623952, 71809044, 71730244, 71797314, 71730240, 62037532, 62038144, 62037534, 69254678, 71538044, 62037536, 66606336, 66606338, 67915892, 71813846, 62036922, 62037540, 62036312, 62036928, 67126138, 62037542, 67017096, 62274246
Multi-odds attempted: True
Multi-odds skipped reason: 
Bookmakers requested: Bet365
Odds endpoint mode: multi_event_documented_endpoint
Selected bookmakers: Bet365
Selected markets: ML
Fixture rows: 523
Event selection diagnostic rows: 39080
Selected event rows: 80
Priced event rows: 10
Price rows: 10
Errors/status rows: 70

## Provider rate-limit headers

Header rows captured: 4
Latest x-ratelimit-limit: 100
Latest x-ratelimit-remaining: 47
Latest x-ratelimit-reset: 2026-05-30T14:01:26Z
Latest retry-after: None

- 2026-05-30 13:30 | Gamle Oslo FK vs Frigg Oslo FK | odds_api_io_Bet365_ML | 1.333/5.25/6.0
- 2026-05-30 13:30 | Patriotas FC PR vs City London FC PR U20 | odds_api_io_Bet365_ML | 2.25/3.25/2.75
- 2026-05-30 13:30 | SV Kuchl vs FC Lustenau | odds_api_io_Bet365_ML | 1.45/5.0/4.5
- 2026-05-30 13:30 | SV Seekirchen vs FC Dornbirn | odds_api_io_Bet365_ML | 2.0/3.9/2.75
- 2026-05-30 13:30 | Zimbabwe vs India | odds_api_io_Bet365_ML | 1.45/3.5/7.0
- 2026-05-30 14:00 | FC 1980 Wien vs LAC Inter | odds_api_io_Bet365_ML | 2.375/3.8/2.35
- 2026-05-30 14:00 | Ariana FC vs Laholms FK | odds_api_io_Bet365_ML | 1.38/4.75/5.75
- 2026-05-30 14:00 | ASKO Kohfidisch vs SV Leithaprodersdorf | odds_api_io_Bet365_ML | 2.8/3.8/2.0
- 2026-05-30 14:00 | ASKO Kottmannsdorf vs SVG Bleiburg | odds_api_io_Bet365_ML | 2.875/3.75/2.0
- 2026-05-30 14:00 | FC Baden vs FC Collina D Oro | odds_api_io_Bet365_ML | 2.0/3.75/3.0

## Event selection diagnostics

- src=events_bookmaker_filtered | query=FC Deutschkreutz | target=FC Deutschkreutz vs SV Eberau | candidate=FC Deutschkreutz vs SV Eberau | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FK Seko Louny | target=FK Seko Louny vs SK Steti | candidate=FK Seko Louny vs SK Steti | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Gamle Oslo FK | target=Gamle Oslo FK vs Frigg Oslo FK | candidate=Gamle Oslo FK vs Frigg Oslo FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Osters IF | target=Osters IF vs Norrby IF | candidate=Osters IF vs Norrby IF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Bollstanas SK | target=Bollstanas SK vs Sunnersta AIF | candidate=Bollstanas SK vs Sunnersta AIF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Kuopion Palloseura | target=Kuopion Palloseura vs FC Inter Turku | candidate=Kuopion Palloseura vs FC Inter Turku | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Flamengo de Sucre | target=Flamengo de Sucre vs Atletico Juniors de Yotala | candidate=Flamengo de Sucre vs Atletico Juniors de Yotala | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=NK Jarun Zagreb | target=NK Jarun Zagreb vs HNK Cibalia Vinkovci | candidate=NK Jarun Zagreb vs HNK Cibalia Vinkovci | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Odds BK | target=Odds BK vs Lyn 1896 FK | candidate=Odds BK vs Lyn 1896 FK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Lahti | target=FC Lahti vs Tampereen Ilves | candidate=FC Lahti vs Tampereen Ilves | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IF Elfsborg | target=IF Elfsborg vs Enskede IK | candidate=IF Elfsborg vs Enskede IK | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SV Kuchl | target=SV Kuchl vs FC Lustenau | candidate=SV Kuchl vs FC Lustenau | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Tvaakers IF | target=Tvaakers IF vs Kristianstad FC | candidate=Tvaakers IF vs Kristianstad FC | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Orijent 1919 Rijeka | target=Orijent 1919 Rijeka vs NK Dugopolje | candidate=Orijent 1919 Rijeka vs NK Dugopolje | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=FC Meyrin | target=FC Meyrin vs CS Chenois | candidate=FC Meyrin vs CS Chenois | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=Patriotas FC PR | target=Patriotas FC PR vs City London FC PR U20 | candidate=Patriotas FC PR vs City London FC PR U20 | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=IFK Kumla | target=IFK Kumla vs Herrestads AIF | candidate=IFK Kumla vs Herrestads AIF | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SE Palmeiras SP | target=SE Palmeiras SP vs SC Corinthians SP | candidate=SE Palmeiras SP vs SC Corinthians SP | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=SC Cham | target=SC Cham vs FC Biel-Bienne | candidate=SC Cham vs FC Biel-Bienne | confidence=1.0 | selected=True | reason=
- src=events_bookmaker_filtered | query=VfB Hohenems | target=VfB Hohenems vs Wacker Innsbruck | candidate=VfB Hohenems vs Wacker Innsbruck | confidence=1.0 | selected=True | reason=

## Errors / Status

- multi_odds_match: No multi-odds payload matched event 68320820
- multi_odds_match: No multi-odds payload matched event 71799058
- multi_odds_match: No multi-odds payload matched event 62216176
- multi_odds_match: No multi-odds payload matched event 61894084
- multi_odds_match: No multi-odds payload matched event 68194442
- multi_odds_match: No multi-odds payload matched event 68492556
- multi_odds_match: No multi-odds payload matched event 67018394
- multi_odds_match: No multi-odds payload matched event 71622034
- multi_odds_match: No multi-odds payload matched event 68310924
- multi_odds_match: No multi-odds payload matched event 68311630