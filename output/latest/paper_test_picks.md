# Paper Test Picks

Observation-only picks. These are not real-money recommendations.
This run uses expanded volume filters to collect more settlement evidence before tightening rules again.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Baseline coverage observations are not model signals. They exist only to test the pipeline and collect settlement evidence.
Suppressed historical bands and negative-EV controls may be tracked as observations only.

Source used: automatic_forward_value_snapshots
Current paper-test picks: 25
Newly logged paper-test picks: 23
Total logged paper-test rows: 251
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 615, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 301, 'current_paper_picks': 25, 'newly_logged_picks': 23, 'total_logged_paper_rows': 251, 'source_used': 'automatic_forward_value_snapshots'}

- Werder Bremen vs Dortmund | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3487 | EV=0.2205 | edge=0.063 | penalty=0.2205 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Werder Bremen vs Dortmund | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3487 | EV=0.2205 | edge=0.063 | penalty=0.2205 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Almeria vs Las Palmas | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3314 | EV=0.193 | edge=0.0536 | penalty=0.193 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Almeria vs Las Palmas | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3314 | EV=0.193 | edge=0.0536 | penalty=0.193 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Heidenheim vs Mainz | coverage=full_team_strength_match | selection=AWAY | odds=3.5 | prob=0.3743 | EV=0.31 | edge=0.0886 | penalty=0.3101 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3716 | EV=0.3006 | edge=0.0859 | penalty=0.3006 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- M'gladbach vs Hoffenheim | coverage=full_team_strength_match | selection=DRAW | odds=4.75 | prob=0.257 | EV=0.2208 | edge=0.0465 | penalty=0.2208 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Heidenheim vs Mainz | coverage=full_team_strength_match | selection=AWAY | odds=3.4 | prob=0.3743 | EV=0.2726 | edge=0.0802 | penalty=0.2726 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | selection=HOME | odds=3.4 | prob=0.3716 | EV=0.2634 | edge=0.0775 | penalty=0.2634 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- M'gladbach vs Hoffenheim | coverage=full_team_strength_match | selection=DRAW | odds=4.5 | prob=0.257 | EV=0.1565 | edge=0.0348 | penalty=0.1565 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Freiburg vs RB Leipzig | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2767 | EV=0.1068 | edge=0.0267 | penalty=0.1068 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Freiburg vs RB Leipzig | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2767 | EV=0.1068 | edge=0.0267 | penalty=0.1068 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Union Berlin vs Augsburg | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2746 | EV=0.0984 | edge=0.0246 | penalty=0.0984 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- St Pauli vs Wolfsburg | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2858 | EV=0.0717 | edge=0.0191 | penalty=0.0717 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- St Pauli vs Wolfsburg | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2858 | EV=0.0717 | edge=0.0191 | penalty=0.0717 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Union Berlin vs Augsburg | coverage=full_team_strength_match | selection=DRAW | odds=3.9 | prob=0.2746 | EV=0.0709 | edge=0.0182 | penalty=0.0709 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Chelsea FC vs Manchester City | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Celtic vs Hearts | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.01 | prob=0.3488 | EV=0.7475 | edge=0.1492 | penalty=0.7475 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Borussia Monchengladbach vs TSG Hoffenheim | coverage=baseline_unmatched_fixture | selection=HOME | odds=4.5 | prob=0.3772 | EV=0.6974 | edge=0.155 | penalty=0.6974 | band=0.35-0.45 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Celtic vs Hearts | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Casa Pia vs Rio Ave | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Casa Pia vs Rio Ave | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Casa Pia Lisbon vs Rio Ave FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- Casa Pia Lisbon vs Rio Ave FC | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation
- SC Braga vs Estrela Amadora | coverage=baseline_unmatched_fixture | selection=AWAY | odds=5.0 | prob=0.3488 | EV=0.744 | edge=0.1488 | penalty=0.744 | band=0.25-0.35 | risk=baseline_coverage_only | rule=baseline_coverage_observe_only | tier=baseline_coverage_observation