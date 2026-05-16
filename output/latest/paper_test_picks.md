# Paper Test Picks

Observation-only picks. These are not real-money recommendations.
This run uses expanded volume filters to collect more settlement evidence before tightening rules again.
Automatic proxy prices are delayed/free market proxies, not live bookmaker odds.
Baseline coverage observations are not model signals. They exist only to test the pipeline and collect settlement evidence.
Suppressed historical bands and negative-EV controls may be tracked as observations only.

Source used: automatic_forward_value_snapshots
Current paper-test picks: 25
Newly logged paper-test picks: 12
Total logged paper-test rows: 263
Max visible paper picks: 25
Filter summary: {'forward_rows_before_filter': 675, 'max_visible_paper_picks': 25, 'odds_range': '1.3-9.0', 'probability_range': '0.15-0.72', 'edge_range': '-0.03-0.32', 'ev_range': '-0.05-1.1', 'max_alignment_penalty': 0.8, 'rows_after_observation_filter': 329, 'current_paper_picks': 25, 'newly_logged_picks': 12, 'total_logged_paper_rows': 263, 'source_used': 'automatic_forward_value_snapshots'}

- Genoa vs Milan | coverage=full_team_strength_match | selection=HOME | odds=4.5 | prob=0.3447 | EV=0.5512 | edge=0.1225 | penalty=0.5512 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.69 | prob=0.2785 | EV=0.5847 | edge=0.1028 | penalty=0.5847 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.28 | prob=0.2806 | EV=0.4816 | edge=0.0912 | penalty=0.4816 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Como vs Parma | coverage=full_team_strength_match | selection=DRAW | odds=5.25 | prob=0.2785 | EV=0.4621 | edge=0.088 | penalty=0.4621 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Juventus vs Fiorentina | coverage=full_team_strength_match | selection=DRAW | odds=5.0 | prob=0.2806 | EV=0.403 | edge=0.0806 | penalty=0.403 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=volume_observation
- Werder Bremen vs Dortmund | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3487 | EV=0.2205 | edge=0.063 | penalty=0.2205 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Werder Bremen vs Dortmund | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3487 | EV=0.2205 | edge=0.063 | penalty=0.2205 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.5 | prob=0.2857 | EV=0.2857 | edge=0.0635 | penalty=0.2857 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Almeria vs Las Palmas | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3314 | EV=0.193 | edge=0.0536 | penalty=0.193 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Almeria vs Las Palmas | coverage=full_team_strength_match | selection=AWAY | odds=3.6 | prob=0.3314 | EV=0.193 | edge=0.0536 | penalty=0.193 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Heidenheim vs Mainz | coverage=full_team_strength_match | selection=AWAY | odds=3.5 | prob=0.3743 | EV=0.31 | edge=0.0886 | penalty=0.3101 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | selection=HOME | odds=3.5 | prob=0.3716 | EV=0.3006 | edge=0.0859 | penalty=0.3006 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- M'gladbach vs Hoffenheim | coverage=full_team_strength_match | selection=DRAW | odds=4.75 | prob=0.257 | EV=0.2208 | edge=0.0465 | penalty=0.2208 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Heidenheim vs Mainz | coverage=full_team_strength_match | selection=AWAY | odds=3.4 | prob=0.3743 | EV=0.2726 | edge=0.0802 | penalty=0.2726 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Ein Frankfurt vs Stuttgart | coverage=full_team_strength_match | selection=HOME | odds=3.4 | prob=0.3716 | EV=0.2634 | edge=0.0775 | penalty=0.2634 | band=0.35-0.45 | risk=proxy_price_source | rule=monitor | tier=priority_proxy_observation
- Roma vs Lazio | coverage=full_team_strength_match | selection=DRAW | odds=4.09 | prob=0.2857 | EV=0.1685 | edge=0.0412 | penalty=0.1685 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Man United vs Nott'm Forest | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.3386 | EV=0.7776 | edge=0.1481 | penalty=0.7777 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Man United vs Nott'm Forest | coverage=full_team_strength_match | selection=AWAY | odds=5.25 | prob=0.3386 | EV=0.7776 | edge=0.1481 | penalty=0.7777 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- M'gladbach vs Hoffenheim | coverage=full_team_strength_match | selection=DRAW | odds=4.5 | prob=0.257 | EV=0.1565 | edge=0.0348 | penalty=0.1565 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Genoa vs Milan | coverage=full_team_strength_match | selection=HOME | odds=4.85 | prob=0.3447 | EV=0.6718 | edge=0.1385 | penalty=0.6718 | band=0.25-0.35 | risk=market_misalignment | rule=none | tier=volume_observation
- Freiburg vs RB Leipzig | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2767 | EV=0.1068 | edge=0.0267 | penalty=0.1068 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Freiburg vs RB Leipzig | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2767 | EV=0.1068 | edge=0.0267 | penalty=0.1068 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- Union Berlin vs Augsburg | coverage=full_team_strength_match | selection=DRAW | odds=4.0 | prob=0.2746 | EV=0.0984 | edge=0.0246 | penalty=0.0984 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- St Pauli vs Wolfsburg | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2858 | EV=0.0717 | edge=0.0191 | penalty=0.0717 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation
- St Pauli vs Wolfsburg | coverage=full_team_strength_match | selection=DRAW | odds=3.75 | prob=0.2858 | EV=0.0717 | edge=0.0191 | penalty=0.0717 | band=0.25-0.35 | risk=proxy_price_source | rule=none | tier=priority_proxy_observation