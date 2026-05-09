import json

import gemini_simple_pipeline as base

ALLOWED_SELECTIONS = {'1', 'X', '2'}

_old_decision_prompt = base.decision_prompt
_old_normalize_picks = base.normalize_picks


def pass_payload(decision_matches, reason, note):
    return {
        'analysis_version': 'simple_decision_v7_concise_grounded_notes',
        'picks': [],
        'passes': [
            {
                'match_id': m.get('match_id'),
                'match': f'{m.get("home_team")} vs {m.get("away_team")}',
                'reason': reason,
                'short_note': note,
            }
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
            'visible_selections': ['1', 'X', '2'],
            'odds': {'1': m.get('odds_1'), 'X': m.get('odds_x'), '2': m.get('odds_2')},
        }
        for m in decision_matches
    ]


def decision_prompt(decision_matches, total_valid):
    return json.dumps({
        'analysis_version': 'simple_decision_v7_concise_grounded_notes',
        'role': 'Skeptical paper-only football value analyst. Default is PASS.',
        'task': 'Use Google Search only to make concise notes. Do NOT return JSON in this first step. Analyze only the supplied visible 1X2 markets. You may choose at most 3 tentative paper-bet candidates, but only from selection 1, X, or 2. If the best idea is X2/1X/DNB/over/under/handicap, mark PASS because that market is not visible.',
        'source_rules': [
            'Prefer official club/league sites, BBC, Sky, The Athletic, Reuters/AP, Premier Injuries, Bold.dk, Tipsbladet, Oddsportal, Betfair, Pinnacle.',
            'Do not use Sportskeeda, CaughtOffside, 90min, Stretty News, GoonersGuide, Sportsgambler, BeSoccer, FCTables, Footlive, FootyStats, APWin, ScoreStrike, WinDrawWin, Sports Mole, tipster/free-picks/prediction/affiliate sites as evidence.',
            'If useful source quality is weak, say PASS.'
        ],
        'output_format': 'Plain text only. For each candidate use: MATCH_ID | MATCH | SELECTION_OR_PASS | ODDS | 2 short evidence bullets | source names | risk flags. Keep total output under 1800 words.',
        'validated_matches': compact_match_list(decision_matches),
    }, ensure_ascii=False)


def structure_prompt(raw_text, decision_matches, total_valid):
    schema = {
        'analysis_version': 'simple_decision_v7_concise_grounded_notes',
        'picks': [{
            'match_id': 'string from validated_matches',
            'match': 'string',
            'selection': '1|X|2|PASS',
            'selection_label': 'home|draw|away|pass',
            'odds': 0.0,
            'decision': 'PAPER_BET|PASS',
            'confidence_score': 0.0,
            'stake_units': 0.0,
            'value_case': 'short',
            'evidence_summary': 'short',
            'evidence_items': [{
                'type': 'injury|suspension|lineup|motivation|form|market_odds|context|other',
                'signal': 'short factual signal',
                'supports_selection': True,
                'importance': 'low|medium|high',
                'source_tier': 'tier1|tier2|tier3|prohibited|unknown',
                'source_type': 'official|sports_media|odds_aggregator|fan_media|prohibited|unknown',
                'source_name': 'single source only',
                'source_url': 'https://source-or-grounding-url',
                'published_or_checked_date': 'string if available'
            }],
            'source_quality': {
                'has_grounded_sources': True,
                'tier1_source_count': 0,
                'tier2_source_count': 0,
                'tier3_source_count': 0,
                'odds_sources': 0,
                'prohibited_sources_used': False,
                'all_evidence_has_urls': True
            },
            'risk_flags': ['string'],
            'why_not_pass': 'short'
        }],
        'passes': [{
            'match_id': 'string',
            'match': 'string',
            'reason': 'insufficient_edge|insufficient_evidence|source_policy_failed|non_visible_market_only|json_not_stable',
            'short_note': 'short'
        }]
    }
    return json.dumps({
        'task': 'Convert the concise analyst notes into strict JSON. Use only match_id values from validated_matches. PAPER_BET is allowed only for selection 1, X, or 2. Any X2/1X/DNB/double chance/over/under/handicap idea must become PASS with reason non_visible_market_only. If source quality is weak or evidence is generic, use PASS. Return JSON only.',
        'schema': schema,
        'validated_matches': compact_match_list(decision_matches),
        'raw_grounded_notes': raw_text[:7000]
    }, ensure_ascii=False)


def call_decision(decision_matches, total_valid):
    if not decision_matches:
        return {'analysis_version': 'simple_decision_v7_concise_grounded_notes', 'picks': [], 'passes': []}, None, [], {}
    url = base.gemini_url()
    if not url:
        return pass_payload(decision_matches, 'system_error', 'Missing GEMINI_API_KEY; fail-closed PASS.'), None, [], {}

    grounding_sources = []
    debug = {}
    try:
        grounded_body = {
            'contents': [{'role': 'user', 'parts': [{'text': decision_prompt(decision_matches, total_valid)}]}],
            'tools': [{'google_search': {}}],
            'generationConfig': {'temperature': 0, 'maxOutputTokens': 4096}
        }
        grounded_resp = base.requests.post(url, json=grounded_body, timeout=180)
        if grounded_resp.status_code >= 400:
            return pass_payload(decision_matches, 'system_error', f'Grounded call failed HTTP {grounded_resp.status_code}; fail-closed PASS.'), None, [], {'grounded_http_status': grounded_resp.status_code, 'response_text': grounded_resp.text[:1000]}
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
            return pass_payload(decision_matches, 'json_not_stable', f'Structure call failed HTTP {structure_resp.status_code}; fail-closed PASS.'), None, grounding_sources, debug
        structure_data = structure_resp.json()
        structured_text = structure_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        debug['structured_text_preview'] = structured_text[:1200]
        try:
            return base.extract_json(structured_text), None, grounding_sources, debug
        except Exception as exc:
            debug['structure_parse_error'] = str(exc)[:500]
            return pass_payload(decision_matches, 'json_not_stable', 'Gemini structure output was not valid JSON; fail-closed PASS.'), None, grounding_sources, debug
    except Exception as exc:
        debug['exception'] = str(exc)[:500]
        return pass_payload(decision_matches, 'system_error', 'Decision step hit an exception; fail-closed PASS.'), None, grounding_sources, debug


def normalize_selection(value):
    return str(value or '').upper().strip()


def normalize_picks(decision_payload, decision_matches):
    records = []
    for candidate in (decision_payload or {}).get('picks') or []:
        selection = normalize_selection(candidate.get('selection'))
        if str(candidate.get('decision') or '').upper() == 'PAPER_BET' and selection not in ALLOWED_SELECTIONS:
            candidate = dict(candidate)
            original_selection = selection
            candidate['decision'] = 'PAPER_BET'
            candidate['selection'] = '1'
            patched = _old_normalize_picks({'picks': [candidate]}, decision_matches)
            if patched:
                patched[0]['decision'] = 'PASS'
                patched[0]['selection'] = 'PASS'
                patched[0]['odds'] = None
                patched[0]['stake_units'] = 0.0
                patched[0]['settlement'] = 'NOT_APPLICABLE'
                patched[0]['blocked_by_safety'] = f'non_visible_market_selection:{original_selection or "empty"}'
                patched[0]['analysis_version'] = 'simple_decision_v7_concise_grounded_notes'
                records.extend(patched)
        else:
            patched = _old_normalize_picks({'picks': [candidate]}, decision_matches)
            for item in patched:
                item['analysis_version'] = 'simple_decision_v7_concise_grounded_notes'
            records.extend(patched)
    return records


base.decision_prompt = decision_prompt
base.call_decision = call_decision
base.normalize_picks = normalize_picks
base.main()
