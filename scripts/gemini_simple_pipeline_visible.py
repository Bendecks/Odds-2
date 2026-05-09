import json

import gemini_simple_pipeline as base

ALLOWED_SELECTIONS = {'1', 'X', '2'}

_old_decision_prompt = base.decision_prompt


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
    data['return_schema']['passes'][0]['reason'] += '|non_visible_market_only'
    for m in data.get('validated_matches', []):
        m['visible_selections'] = ['1', 'X', '2']
    return json.dumps(data, ensure_ascii=False)


def normalize_selection(value):
    return str(value or '').upper().strip()


def normalize_picks(decision_payload, decision_matches):
    records = []
    for candidate in (decision_payload or {}).get('picks') or []:
        selection = normalize_selection(candidate.get('selection'))
        if str(candidate.get('decision') or '').upper() == 'PAPER_BET' and selection not in ALLOWED_SELECTIONS:
            candidate = dict(candidate)
            candidate['decision'] = 'PAPER_BET'
            candidate['selection'] = '1'
            patched = base.normalize_picks({'picks': [candidate]}, decision_matches)
            if patched:
                patched[0]['decision'] = 'PASS'
                patched[0]['selection'] = 'PASS'
                patched[0]['odds'] = None
                patched[0]['stake_units'] = 0.0
                patched[0]['settlement'] = 'NOT_APPLICABLE'
                patched[0]['blocked_by_safety'] = f'non_visible_market_selection:{selection or "empty"}'
                patched[0]['analysis_version'] = 'simple_decision_v6_visible_markets_only'
                records.extend(patched)
        else:
            patched = base.normalize_picks({'picks': [candidate]}, decision_matches)
            for item in patched:
                item['analysis_version'] = 'simple_decision_v6_visible_markets_only'
            records.extend(patched)
    return records


base.decision_prompt = decision_prompt
base.normalize_picks = normalize_picks
base.main()
