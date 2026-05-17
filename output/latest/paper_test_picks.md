# Paper Test Picks

Observation-only picks. These are not real-money recommendations.
This run uses expanded volume filters to collect more settlement evidence before tightening rules again.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Baseline coverage observations are not model signals. They exist only to test the pipeline and collect settlement evidence.
Suppressed historical bands and negative-EV controls may be tracked as observations only.

Source used: automatic_forward_value_snapshots
Current paper-test picks: 25
Newly logged paper-test picks: 15
Total logged paper-test rows: 278
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 609, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 299, 'current_paper_picks': 25, 'newly_logged_picks': 15, 'total_logged_paper_rows': 278, 'source_used': 'automatic_forward_value_snapshots'}

- Genoa vs Milan | coverage=full_team_strength_match | selection=HOME | odds=4.5 | prob=0.3447 | EV=0.5512 | edge=0.1225 | penalty=0.5512 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.69 | prob=0.2785 | EV=0.5847 | edge=0.1028 | penalty=0.5847 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.28 | prob=0.2806 | EV=0.4816 | edge=0.0912 | penalty=0.4816 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.25 | prob=0.2785 | EV=0.4621 | edge=0.088 | penalty=0.4621 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.0 | prob=0.2806 | EV=0.403 | edge=0.0806 | penalty=0.403 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.5 | prob=0.2857 | EV=0.2857 | edge=0.0635 | penalty=0.2857 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.09 | prob=0.2857 | EV=0.1685 | edge=0.0412 | penalty=0.1685 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Man United vs Nott'm Forest | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.3386 | EV=0.7776 | edge=0.1481 | penalty=0.7777 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Man United vs Nott'm Forest | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.3386 | EV=0.7776 | edge=0.1481 | penalty=0.7777 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Genoa vs Milan | coverage=full_team_strength_match | selection=HOME | odds=4.85 | prob=0.3447 | EV=0.6718 | edge=0.1385 | penalty=0.6718 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Gimhae FC vs Daegu FC | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Heracles vs Groningen | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Heracles Almelo vs FC Groningen | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- V-Varen Nagasaki vs Vissel Kobe | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- PEC Zwolle vs Feyenoord Rotterdam | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Zwolle vs Feyenoord | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.75 | prob=0.3772 | EV=0.7917 | edge=0.1667 | penalty=0.7917 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ternana vs AC Milan | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.65 | prob=0.3772 | EV=0.754 | edge=0.1621 | penalty=0.754 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Genoa CFC vs AC Milan | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.65 | prob=0.3772 | EV=0.754 | edge=0.1621 | penalty=0.754 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Heracles Almelo vs FC Groningen | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.63 | prob=0.3772 | EV=0.7464 | edge=0.1612 | penalty=0.7464 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Heracles vs Groningen | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.63 | prob=0.3772 | EV=0.7464 | edge=0.1612 | penalty=0.7464 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Genoa CFC vs AC Milan | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- La Coruna vs Andorra | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.01 | prob=0.3488 | EV=0.7475 | edge=0.1492 | penalty=0.7475 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- RC Deportivo De La Coruna vs FC Andorra | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.01 | prob=0.3488 | EV=0.7475 | edge=0.1492 | penalty=0.7475 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Ternana vs AC Milan | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Okayama Yunogo Belle vs Nittaidai FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation