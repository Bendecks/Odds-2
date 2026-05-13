# Paper Test Picks

Observation-only picks. These are not real-money recommendations.
This run uses expanded volume filters to collect more settlement evidence before tightening rules again.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Baseline coverage observations are not model signals. They exist only to test the pipeline and collect settlement evidence.
Suppressed historical bands and negative-EV controls may be tracked as observations only.

Source used: automatic_forward_value_snapshots
Current paper-test picks: 25
Newly logged paper-test picks: 3
Total logged paper-test rows: 112
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 384, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 174, 'current_paper_picks': 25, 'newly_logged_picks': 3, 'total_logged_paper_rows': 112, 'source_used': 'automatic_forward_value_snapshots'}

- Getafe vs Mallorca | coverage=full_team_strength_match | selection=AWAY | odds=3.7 | prob=0.3268 | EV=0.2092 | edge=0.0565 | penalty=0.2092 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Villarreal vs Sevilla | coverage=full_team_strength_match | selection=AWAY | odds=3.7 | prob=0.326 | EV=0.2062 | edge=0.0557 | penalty=0.2062 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Villarreal vs Sevilla | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.326 | EV=0.1736 | edge=0.0482 | penalty=0.1736 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Getafe vs Mallorca | coverage=full_team_strength_match | selection=AWAY | odds=3.51 | prob=0.3268 | EV=0.1471 | edge=0.0419 | penalty=0.1471 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Lens vs Paris SG | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3022 | EV=0.0577 | edge=0.0165 | penalty=0.0577 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Alaves vs Barcelona | coverage=full_team_strength_match | selection=DRAW | odds=3.9 | prob=0.2757 | EV=0.0752 | edge=0.0193 | penalty=0.0752 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Lens vs Paris SG | coverage=full_team_strength_match | selection=HOME | odds=3.4 | prob=0.3022 | EV=0.0275 | edge=0.0081 | penalty=0.0275 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Alaves vs Barcelona | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2757 | EV=0.0339 | edge=0.009 | penalty=0.0339 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brest vs Strasbourg | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2794 | EV=0.0058 | edge=0.0016 | penalty=0.0058 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Brest vs Strasbourg | coverage=full_team_strength_match | selection=DRAW | odds=3.6 | prob=0.2794 | EV=0.0058 | edge=0.0016 | penalty=0.0058 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Espanol vs Ath Bilbao | coverage=full_team_strength_match | selection=DRAW | odds=3.3 | prob=0.2922 | EV=-0.0357 | edge=-0.0108 | penalty=0.0357 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=negative_ev_control_observation
- Espanol vs Ath Bilbao | coverage=full_team_strength_match | selection=DRAW | odds=3.3 | prob=0.2922 | EV=-0.0357 | edge=-0.0108 | penalty=0.0357 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=negative_ev_control_observation
- PAOK Thessaloniki vs AEK Athens | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PAOK vs AEK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PAOK vs AEK | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Levadeiakos vs OFI Crete | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PAOK Thessaloniki vs AEK Athens | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Levadeiakos vs OFI Crete | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Motherwell FC vs Celtic Glasgow | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.4 | prob=0.3772 | EV=0.6597 | edge=0.1499 | penalty=0.6597 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Motherwell vs Celtic | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.4 | prob=0.3772 | EV=0.6597 | edge=0.1499 | penalty=0.6597 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Volos NFC vs Aris | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6333 | edge=0.1463 | penalty=0.6333 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Motherwell vs Celtic | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6333 | edge=0.1463 | penalty=0.6333 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Volos NFC vs Aris | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6333 | edge=0.1463 | penalty=0.6333 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Motherwell FC vs Celtic Glasgow | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.33 | prob=0.3772 | EV=0.6333 | edge=0.1463 | penalty=0.6333 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Kultsu FC vs Ips | coverage=baseline_unmatched_fixture | selection=AWAY | odds=4.75 | prob=0.3488 | EV=0.6568 | edge=0.1383 | penalty=0.6568 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation