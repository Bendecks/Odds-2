import json
import pathlib
from collections import Counter, defaultdict
from datetime import datetime, timezone

from tracker import read_tracker

MARKET_STATE_PATH = pathlib.Path('output/latest/market_state.json')
OUT_PATH = pathlib.Path('output/latest/ai_candidates.json')
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

MODEL_VERSION = 'phase2_chatgpt_paper_v2'
CONTEXT_RECORD_TYPES = {'research_record', 'market_consensus_record'}


def utc_now_dt():
    return datetime.now(timezone.utc)


def parse_utc(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    except Exception:
        return None


def is_expired_market(market):
    dt = parse_utc((market.get('event_time') or {}).get('utc'))
    if not dt:
        return False
    return dt <= utc_now_dt()


def load_market_state(path=MARKET_STATE_PATH):
    if not path.exists():
        return {'markets': []}
    return json.loads(path.read_text(encoding='utf-8'))


def decision_and_context_state(records, model_version=MODEL_VERSION):
    """Decision dedupe is scoped to market snapshot, but new context permits reevaluation."""
    decision_times = {}
    legacy_market_ids = set()
    latest_context_time = {}
    latest_context_type = {}
    for r in records:
        rtype = r.get('record_type')
        market_id = r.get('market_id')
        if not market_id:
            continue
        created = r.get('created_at') or r.get('generated_at') or ''
        if rtype in CONTEXT_RECORD_TYPES:
            if created > latest_context_time.get(market_id, ''):
                latest_context_time[market_id] = created
                latest_context_type[market_id] = rtype
            continue
        if rtype != 'decision_record':
            continue
        if r.get('model_version') != model_version:
            continue
        latest_observation_id = r.get('latest_observation_id')
        if market_id and latest_observation_id:
            key = (market_id, latest_observation_id)
            if created > decision_times.get(key, ''):
                decision_times[key] = created
        elif market_id:
            legacy_market_ids.add(market_id)
    return decision_times, legacy_market_ids, latest_context_time, latest_context_type


def market_is_eligible(market):
    if not market.get('active'):
        return False, 'inactive_market'
    if is_expired_market(market):
        return False, 'event_expired'
    m = market.get('market') or {}
    if m.get('type') != '1X2':
        return False, 'unsupported_market_type'
    pc = market.get('parser_confidence') or {}
    if not pc.get('real_bet_allowed'):
        return False, 'real_bet_not_allowed_by_data_integrity'
    if market.get('latest_dedupe_status') == 'parser_conflict':
        return False, 'parser_conflict'
    return True, 'eligible'


def compact_candidate(market):
    event = market.get('event') or {}
    m = market.get('market') or {}
    ms = market.get('movement_summary') or {}
    pc = market.get('parser_confidence') or {}
    return {
        'market_id': market.get('market_id'),
        'event_id': market.get('event_id'),
        'event_name': f'{event.get("home")} vs {event.get("away")}',
        'league': event.get('league'),
        'sport': event.get('sport'),
        'event_time_utc': (market.get('event_time') or {}).get('utc'),
        'market_type': m.get('type'),
        'line': m.get('line'),
        'selection': m.get('selection'),
        'odds': m.get('odds'),
        'first_seen_odds': ms.get('first_seen_odds'),
        'latest_seen_odds': ms.get('latest_seen_odds'),
        'movement_from_first': ms.get('movement_from_first'),
        'change_pct_from_first': ms.get('change_pct_from_first'),
        'observation_count': ms.get('observation_count'),
        'non_duplicate_observation_count': ms.get('non_duplicate_observation_count'),
        'dedupe_counts': ms.get('dedupe_counts'),
        'parser_confidence_total': pc.get('total'),
        'parser_confidence_status': pc.get('status'),
        'hard_gates': pc.get('hard_gates'),
        'latest_observation_id': market.get('latest_observation_id'),
    }


def prepare_candidates(max_candidates=90, model_version=MODEL_VERSION):
    state = load_market_state()
    records = read_tracker()
    decision_times, legacy_market_ids, latest_context_time, latest_context_type = decision_and_context_state(records, model_version)
    eligible = []
    skipped = []
    reason_counts = Counter()

    for market in state.get('markets') or []:
        mid = market.get('market_id')
        latest_observation_id = market.get('latest_observation_id')
        ok, reason = market_is_eligible(market)
        if not ok:
            skipped.append({'market_id': mid, 'reason': reason})
            reason_counts[reason] += 1
            continue
        key = (mid, latest_observation_id)
        decision_time = decision_times.get(key)
        context_time = latest_context_time.get(mid)
        if decision_time and (not context_time or decision_time >= context_time):
            skipped.append({'market_id': mid, 'latest_observation_id': latest_observation_id, 'reason': 'decision_exists_for_market_observation_model_no_new_context'})
            reason_counts['decision_exists_for_market_observation_model_no_new_context'] += 1
            continue
        if decision_time and context_time and context_time > decision_time:
            skipped.append({'market_id': mid, 'latest_observation_id': latest_observation_id, 'reason': 'reevaluate_due_to_new_context', 'context_type': latest_context_type.get(mid)})
            reason_counts['reevaluate_due_to_new_context'] += 1
        if mid in legacy_market_ids:
            skipped.append({'market_id': mid, 'reason': 'legacy_decision_ignored_no_observation_scope'})
            reason_counts['legacy_decision_ignored_no_observation_scope'] += 1
        eligible.append(compact_candidate(market))

    grouped = defaultdict(list)
    for c in eligible:
        grouped[c['event_id']].append(c)
    ordered = []
    for event_id in sorted(grouped.keys(), key=lambda eid: min(x.get('event_time_utc') or '' for x in grouped[eid])):
        ordered.extend(sorted(grouped[event_id], key=lambda x: str(x.get('line'))))
    selected = ordered[:max_candidates]
    payload = {
        'model_version': model_version,
        'mode': 'paper_only',
        'candidate_count': len(selected),
        'eligible_count': len(eligible),
        'skipped_count': len(skipped),
        'skip_reason_counts': dict(reason_counts),
        'candidates': selected,
        'skipped': skipped[:300]
    }
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    return payload


if __name__ == '__main__':
    p = prepare_candidates()
    print(f'Prepared AI candidates: {p["candidate_count"]} | eligible={p["eligible_count"]} | skipped={p["skipped_count"]} | reasons={p["skip_reason_counts"]}')
