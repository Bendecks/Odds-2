import json

import gemini_simple_pipeline as base

ALLOWED_SELECTIONS = {'1', 'X', '2'}

_old_decision_prompt = base.decision_prompt
_old_normalize_picks = base.normalize_picks


def pass_payload(decision_matches, reason, note):
    return {
        'analysis_version': 'simple_decision_v6_visible_markets_only',
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


def decision_prompt(decision_matches, total_valid):
    data = json.loads(_old_decision_prompt(decision_matches, total_valid))
    data['analysis_version'] = 'simple_decision_v6_visible_markets_only'
    data['market_policy'] = {
        'visible_markets_only': True,
        'allowed_selections': ['1', 'X', '2'],
        'forbidden_selections': ['1X', 'X2', '12', 'DNB', 'double chance', 'over', 'under', 'handicap'],
        'rule': 'Only choose a selection that is visible in the supplied odds object. Do not invent safer adjacent markets.'
    }
    data['task'] = data.get('task', '') + ' Only 1, X, or 2 may be selected. If the best idea is another market, return PASS.'
    data['hard_rules'].insert(1, 'Only selections 1, X, and 2 are allowed because these are the only markets parsed and validated from the PDF.')
    data['hard_rules'].insert(2, 'Never output X2, 1X, 12, DNB, double chance, over/under, handicap, or any non-visible market.')
    data['return_schema']['analysis_version'] = 'simple_decision_v6_visible_markets_only'
    data['return_schema']['passes'][0]['reason'] += '|non_visible_market_only|json_not_stable'
    for m in data.get('validated_matches', []):
        m['visible_selections'] = ['1', 'X', '2']
    return json.dumps(data, ensure_ascii=False)


def structure_prompt(raw_text, decision_matches, total_valid):
    prompt_obj = json.loads(decision_prompt(decision_matches, total_valid))
    return json.dumps({
        'task': 'Convert the analyst output into strict JSON. If the analyst output is malformed, too vague, or suggests any market other than 1/X/2, return only PASS records. Return JSON only.',
        'schema': prompt_obj.get('return_schema'),
        'validated_matches': prompt_obj.get('validated_matches'),
        'raw_grounded_output': raw_text[:8000]
    }, ensure_ascii=False)


def call_decision(decision_matches, total_valid):
    if not decision_matches:
        return {'analysis_version': 'simple_decision_v6_visible_markets_only', 'picks': [], 'passes': []}, None, [], {}
    url = base.gemini_url()
    if not url:
        return pass_payload(decision_matches, 'system_error', 'Missing GEMINI_API_KEY; fail-closed PASS.'), None, [], {}

    grounding_sources = []
    debug = {}
    try:
        grounded_body = {
            'contents': [{'role': 'user', 'parts': [{'text': decision_prompt(decision_matches, total_valid)}]}],
            'tools': [{'google_search': {}}],
            'generationConfig': {'temperature': 0, 'maxOutputTokens': 8192}
        }
        grounded_resp = base.requests.post(url, json=grounded_body, timeout=180)
        if grounded_resp.status_code >= 400:
            return pass_payload(decision_matches, 'system_error', f'Grounded call failed HTTP {grounded_resp.status_code}; fail-closed PASS.'), None, [], {'grounded_http_status': grounded_resp.status_code, 'response_text': grounded_resp.text[:1000]}
        grounded_data = grounded_resp.json()
        grounded_text = grounded_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        grounding_sources = base.extract_grounding_sources(grounded_data)
        debug = base.compact_response_debug(grounded_data, grounded_text)
        debug['grounded_text_preview'] = grounded_text[:1200]

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
                patched[0]['analysis_version'] = 'simple_decision_v6_visible_markets_only'
                records.extend(patched)
        else:
            patched = _old_normalize_picks({'picks': [candidate]}, decision_matches)
            for item in patched:
                item['analysis_version'] = 'simple_decision_v6_visible_markets_only'
            records.extend(patched)
    return records


base.decision_prompt = decision_prompt
base.call_decision = call_decision
base.normalize_picks = normalize_picks
base.main()
