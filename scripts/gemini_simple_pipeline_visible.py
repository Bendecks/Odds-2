import json

import gemini_simple_pipeline as base

ALLOWED_SELECTIONS = {'1', 'X', '2'}
PROHIBITED_TERMS = [
    'sportskeeda', 'caughtoffside', '90min', 'stretty', 'goonersguide', 'sportsgambler',
    'besoccer', 'fctables', 'footlive', 'footystats', 'apwin', 'scorestrike', 'windrawwin',
    'sports mole', 'free picks', 'expert picks', 'betting tips', 'tipster', 'affiliate'
]


def pass_payload(decision_matches, reason, note):
    return {
        'analysis_version': 'final_pick_decision_v1',
        'summary': {'matches_analyzed': len(decision_matches), 'picks_count': 0, 'pass_count': len(decision_matches), 'overall_note': note},
        'picks': [],
        'passes': [
            {'match_id': m.get('match_id'), 'match': f'{m.get("home_team")} vs {m.get("away_team")}', 'reason': reason, 'short_note': note}
            for m in decision_matches
        ],
    }


def compact_match_list(decision_matches):
    return [
        {
            'match_id': m.get('match_id'),
            'match': f'{m.get("home_team")} vs {m.get("away_team")}',
            'league': m.get('league'),
            'date_display': m.get('date_display'),
            'time_display': m.get('time_display'),
            'allowed_selections': ['1', 'X', '2'],
            'odds': {'1': m.get('odds_1'), 'X': m.get('odds_x'), '2': m.get('odds_2')},
        }
        for m in decision_matches
    ]


def decision_prompt(decision_matches, total_valid):
    return json.dumps({
        'analysis_version': 'final_pick_decision_v1',
        'role': 'Odds-2 Oracle. Practical football value analyst. Return concrete PICKS only when the visible 1X2 price is worth taking; otherwise PASS.',
        'goal': 'Produce a finished practical PICK/PASS decision. Aim for 1-3 PICKS if plausible value exists. Do not force picks when nothing is plausible.',
        'market_rules': [
            'Only select 1, X, or 2 from the supplied odds object.',
            'Never suggest X2, 1X, DNB, double chance, over/under, handicap, BTTS, or any market not in input.',
            'A PICK must explain why this exact odds number is worth taking, not just who is likely to win.'
        ],
        'decision_rules': [
            'A PICK requires at least two signals: price/value logic, form/table/motivation, home-away contrast, injury/suspension/lineup news, market comparison, or schedule/rotation context.',
            'Strong source URLs are helpful but not mandatory. Use source_quality=limited when sources are weak or unavailable.',
            'Never use prohibited betting-tip/affiliate/prediction sites as the main reason.',
            'Never pick based only on better team, strong form, famous club, or home advantage.',
            'Most PICKS should be 0.25 or 0.5 units. Use 0.75 rarely and 1.0 almost never.',
            'Confidence above 0.75 should be rare. Limited-source picks should be max 0.59 confidence.'
        ],
        'prohibited_sources': PROHIBITED_TERMS,
        'output_format': 'Plain text notes only, not JSON. For up to 3 PICKS use: PICK | MATCH_ID | MATCH | SELECTION | ODDS | CONFIDENCE | STAKE | VALUE CASE | SIGNAL 1 | SIGNAL 2 | SOURCE QUALITY | RISKS. Then list PASS for the rest briefly. Keep under 1400 words.',
        'validated_matches': compact_match_list(decision_matches),
    }, ensure_ascii=False)


def structure_prompt(raw_text, decision_matches, total_valid):
    return json.dumps({
        'task': 'Convert the analyst notes into strict JSON for the final Odds-2 PICK/PASS output. Keep PICKS if they select only 1, X, or 2 and include at least two distinct signals. If a pick is based only on favorite/team strength or a non-visible market, convert to PASS. Return JSON only.',
        'schema': {
            'analysis_version': 'final_pick_decision_v1',
            'summary': {'matches_analyzed': 0, 'picks_count': 0, 'pass_count': 0, 'overall_note': 'short'},
            'picks': [{
                'match_id': 'string', 'match': 'string', 'selection': '1|X|2', 'selection_label': 'home|draw|away',
                'odds': 0.0, 'decision': 'PAPER_BET', 'confidence_score': 0.0, 'stake_units': 0.25,
                'value_case': 'why this exact odds is worth taking',
                'main_signals': ['signal 1', 'signal 2'],
                'evidence_summary': 'short',
                'evidence_items': [
                    {'type': 'form|motivation|market_odds|context|injury|lineup|other', 'signal': 'short', 'supports_selection': True, 'importance': 'low|medium|high', 'source_tier': 'tier1|tier2|tier3|unknown|limited', 'source_type': 'official|sports_media|odds_aggregator|stats|unknown', 'source_name': 'single source if known', 'source_url': '', 'published_or_checked_date': ''}
                ],
                'source_quality': {'has_grounded_sources': True, 'tier1_source_count': 0, 'tier2_source_count': 0, 'tier3_source_count': 0, 'odds_sources': 0, 'prohibited_sources_used': False, 'all_evidence_has_urls': False, 'quality_label': 'strong|acceptable|limited'},
                'risk_flags': ['limited_sources'],
                'why_not_pass': 'why this is worth picking rather than passing',
                'final_reasoning': 'short practical reasoning'
            }],
            'passes': [{'match_id': 'string', 'match': 'string', 'reason': 'no_edge|weak_price|non_visible_market|bad_sources|too_uncertain|odds_too_low|generic_only', 'short_note': 'short'}]
        },
        'validated_matches': compact_match_list(decision_matches),
        'raw_notes': raw_text[:6000]
    }, ensure_ascii=False)


def call_decision(decision_matches, total_valid):
    if not decision_matches:
        return pass_payload(decision_matches, 'no_matches', 'No matches to analyze.'), None, [], {}
    url = base.gemini_url()
    if not url:
        return pass_payload(decision_matches, 'system_error', 'Missing GEMINI_API_KEY; fail-closed PASS.'), None, [], {}
    try:
        grounded_body = {
            'contents': [{'role': 'user', 'parts': [{'text': decision_prompt(decision_matches, total_valid)}]}],
            'tools': [{'google_search': {}}],
            'generationConfig': {'temperature': 0.2, 'maxOutputTokens': 4096}
        }
        grounded_resp = base.requests.post(url, json=grounded_body, timeout=180)
        if grounded_resp.status_code >= 400:
            return pass_payload(decision_matches, 'system_error', f'Grounded call HTTP {grounded_resp.status_code}.'), None, [], {}
        grounded_data = grounded_resp.json()
        grounded_text = grounded_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        grounding_sources = base.extract_grounding_sources(grounded_data)
        debug = base.compact_response_debug(grounded_data, grounded_text)
        debug['grounded_text_preview'] = grounded_text[:1800]

        structure_body = {
            'contents': [{'role': 'user', 'parts': [{'text': structure_prompt(grounded_text, decision_matches, total_valid)}]}],
            'generationConfig': {'temperature': 0, 'responseMimeType': 'application/json', 'maxOutputTokens': 4096}
        }
        structure_resp = base.requests.post(url, json=structure_body, timeout=120)
        if structure_resp.status_code >= 400:
            return pass_payload(decision_matches, 'json_not_stable', f'Structure call HTTP {structure_resp.status_code}.'), None, grounding_sources, debug
        structure_data = structure_resp.json()
        structured_text = structure_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        debug['structured_text_preview'] = structured_text[:1200]
        try:
            return base.extract_json(structured_text), None, grounding_sources, debug
        except Exception as exc:
            debug['structure_parse_error'] = str(exc)[:500]
            return pass_payload(decision_matches, 'json_not_stable', 'Structure output was not valid JSON.'), None, grounding_sources, debug
    except Exception as exc:
        return pass_payload(decision_matches, 'system_error', f'Decision exception: {str(exc)[:200]}'), None, [], {}


def normalize_selection(value):
    return str(value or '').upper().strip()


def text_has_prohibited_source(candidate):
    text = json.dumps(candidate, ensure_ascii=False).lower()
    return any(term in text for term in PROHIBITED_TERMS)


def enough_signals(candidate):
    signals = candidate.get('main_signals') or []
    items = candidate.get('evidence_items') or []
    signal_count = len([s for s in signals if str(s).strip()])
    if signal_count >= 2:
        return True
    item_count = len([i for i in items if isinstance(i, dict) and str(i.get('signal') or '').strip()])
    return item_count >= 2


def normalize_picks(decision_payload, decision_matches):
    by_id = {m['match_id']: m for m in decision_matches}
    records = []
    paper_count = 0
    for candidate in (decision_payload or {}).get('picks') or []:
        mid = candidate.get('match_id')
        if mid not in by_id:
            continue
        m = by_id[mid]
        selection = normalize_selection(candidate.get('selection'))
        decision = 'PAPER_BET'
        block_reason = None
        if selection not in ALLOWED_SELECTIONS:
            decision = 'PASS'; selection = 'PASS'; block_reason = f'non_visible_market_selection:{selection or "empty"}'
        elif text_has_prohibited_source(candidate):
            decision = 'PASS'; selection = 'PASS'; block_reason = 'prohibited_source_used'
        elif not enough_signals(candidate):
            decision = 'PASS'; selection = 'PASS'; block_reason = 'not_enough_signals'
        try:
            confidence = float(candidate.get('confidence_score') or 0.5)
        except Exception:
            confidence = 0.5
        try:
            stake = float(candidate.get('stake_units') or 0.25)
        except Exception:
            stake = 0.25
        if decision == 'PAPER_BET':
            paper_count += 1
            if paper_count > 3:
                decision = 'PASS'; selection = 'PASS'; block_reason = 'max_picks_exceeded'
            stake = min(max(stake, 0.25), 1.0)
            confidence = min(max(confidence, 0.5), 0.85)
            odds = {'1': m.get('odds_1'), 'X': m.get('odds_x'), '2': m.get('odds_2')}[selection]
        else:
            stake = 0.0; odds = None
        evidence_items = candidate.get('evidence_items') if isinstance(candidate.get('evidence_items'), list) else []
        records.append({
            'record_type': 'simple_pick', 'pick_id': base.stable_id('pick', mid, base.now_utc(), selection, odds),
            'created_at': base.now_utc(), 'mode': 'final_pick', 'analysis_version': 'final_pick_decision_v1',
            'match_id': mid, 'match': candidate.get('match') or f'{m.get("home_team")} vs {m.get("away_team")}',
            'league': m.get('league'), 'date_display': m.get('date_display'), 'time_display': m.get('time_display'),
            'selection': selection, 'selection_label': candidate.get('selection_label') if decision == 'PAPER_BET' else 'pass',
            'odds': odds, 'decision': decision, 'confidence_score': confidence, 'stake_units': stake,
            'value_case': str(candidate.get('value_case') or '')[:700],
            'evidence_summary': str(candidate.get('evidence_summary') or candidate.get('final_reasoning') or '')[:700],
            'evidence_items': evidence_items,
            'evidence_lines': [base.evidence_line(i) for i in evidence_items if isinstance(i, dict)],
            'verified_source_tiers': [base.source_tier(i) for i in evidence_items if isinstance(i, dict)],
            'source_quality': candidate.get('source_quality') if isinstance(candidate.get('source_quality'), dict) else {'quality_label': 'limited'},
            'redirect_source_count': 0,
            'risk_flags': candidate.get('risk_flags') if isinstance(candidate.get('risk_flags'), list) else [],
            'why_not_pass': str(candidate.get('why_not_pass') or candidate.get('final_reasoning') or '')[:500],
            'blocked_by_safety': block_reason,
            'short_reason': str(candidate.get('final_reasoning') or candidate.get('evidence_summary') or candidate.get('value_case') or '')[:500],
            'source_match': m, 'settlement': 'PENDING' if decision == 'PAPER_BET' else 'NOT_APPLICABLE'
        })
    return records


base.call_decision = call_decision
base.normalize_picks = normalize_picks
base.main()
