import hashlib
import json
import os
import pathlib
from datetime import datetime, timezone

import requests

from prepare_candidates import prepare_candidates
from tracker import append_records, read_tracker

OUT_LATEST = pathlib.Path('output/latest')
OUT_REPORTS = pathlib.Path('output/reports')
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_REPORTS.mkdir(parents=True, exist_ok=True)

MODEL_VERSION = os.getenv('AI_DECISION_VERSION', 'phase2_decision_v3_2_expired_event_gate')
AI_PROVIDER = os.getenv('AI_PROVIDER', 'gemini').lower()
GEMINI_MODEL = os.getenv('GEMINI_DECISION_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
MAX_CANDIDATES = int(os.getenv('AI_MAX_CANDIDATES', '90'))
MAX_AI_EVAL = int(os.getenv('AI_V3_MAX_EVAL_CANDIDATES', '15'))
VALID_RESEARCH_STATUSES = {'completed', 'insufficient_data'}
INVALID_RESEARCH_STATUSES = {'failed', 'simulated', 'completed_unstructured'}


def utc_now_dt():
    return datetime.now(timezone.utc)


def utc_now():
    return utc_now_dt().replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def parse_utc(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    except Exception:
        return None


def is_expired(candidate):
    dt = parse_utc(candidate.get('event_time_utc'))
    if not dt:
        return False
    return dt <= utc_now_dt()


def stable_hash(prefix, *parts, length=16):
    raw = '|'.join(str(p or '').strip().lower() for p in parts)
    return f'{prefix}_{hashlib.sha256(raw.encode("utf-8")).hexdigest()[:length]}'


def latest_valid_research_by_market():
    latest = {}
    ignored = {}
    for r in read_tracker():
        if r.get('record_type') != 'research_record':
            continue
        mid = r.get('market_id')
        if not mid:
            continue
        status = r.get('research_status')
        provider = r.get('provider')
        flags = r.get('research_flags') or []
        invalid = provider == 'simulation' or status in INVALID_RESEARCH_STATUSES or 'simulated_research_record' in flags or 'not_real_research' in flags
        if invalid:
            ignored[mid] = {'reason': 'invalid_or_simulated_research', 'status': status, 'provider': provider}
            continue
        if status not in VALID_RESEARCH_STATUSES:
            ignored[mid] = {'reason': 'unsupported_research_status', 'status': status, 'provider': provider}
            continue
        created = r.get('created_at') or ''
        if mid not in latest or created > (latest[mid].get('created_at') or ''):
            latest[mid] = r
    return latest, ignored


def research_context_for(research):
    if not research:
        return None
    signals = research.get('signals') or {}
    sq = research.get('source_quality') or {}
    return {
        'research_id': research.get('research_id'),
        'research_version': research.get('research_version'),
        'research_status': research.get('research_status'),
        'created_at': research.get('created_at'),
        'provider': research.get('provider'),
        'confidence': research.get('confidence'),
        'summary': research.get('summary'),
        'trigger_reasons': research.get('trigger_reasons') or [],
        'source_quality': {
            'primary_source_count': sq.get('primary_source_count', 0),
            'secondary_source_count': sq.get('secondary_source_count', 0),
            'echo_chamber_risk': sq.get('echo_chamber_risk'),
        },
        'signals': {
            'hard': signals.get('hard') or signals.get('injuries') or [],
            'soft': signals.get('soft') or signals.get('motivation') or [],
            'contradictions': signals.get('contradictions') or [],
        },
        'research_flags': research.get('research_flags') or [],
        'source_links_count': len(research.get('source_links') or []),
    }


def enrich_candidates(candidates):
    research_by_market, ignored = latest_valid_research_by_market()
    enriched = []
    for c in candidates:
        mid = c.get('market_id')
        r = research_by_market.get(mid)
        e = dict(c)
        e['is_expired'] = is_expired(e)
        e['research_context'] = research_context_for(r)
        e['has_valid_research'] = r is not None
        if not r and mid in ignored:
            e['ignored_research'] = ignored[mid]
        enriched.append(e)
    return enriched


def has_market_signal(candidate):
    try:
        change = float(candidate.get('change_pct_from_first') or 0)
    except Exception:
        change = 0.0
    return candidate.get('movement_from_first') == 'shortened' and change >= 0.03


def has_research_sources(research_context):
    if not research_context:
        return False
    sq = research_context.get('source_quality') or {}
    total = int(sq.get('primary_source_count') or 0) + int(sq.get('secondary_source_count') or 0) + int(research_context.get('source_links_count') or 0)
    return total > 0


def is_forced_only_research(research_context):
    reasons = (research_context or {}).get('trigger_reasons') or []
    return reasons == ['simulated_research_trigger']


def is_interesting_for_ai(candidate):
    if candidate.get('is_expired'):
        return False
    return bool(candidate.get('has_valid_research') or has_market_signal(candidate))


def candidate_priority(candidate):
    try:
        change = float(candidate.get('change_pct_from_first') or 0)
    except Exception:
        change = 0.0
    score = change
    if candidate.get('has_valid_research'):
        score += 1.0
    if candidate.get('movement_from_first') == 'shortened':
        score += 0.1
    return score


def conservative_decision(candidate, fallback_reason=None):
    research = candidate.get('research_context')
    data_flags = []
    risk_flags = []
    if fallback_reason:
        data_flags.append(fallback_reason)
    if candidate.get('is_expired'):
        data_flags.append('event_expired')
        return {'decision': 'PASS', 'confidence': 'high', 'paper_stake_pct': 0.0, 'reasoning_code': 'EVENT_EXPIRED_PASS', 'reasoning_summary': 'PASS: event time has passed. No paper decision allowed.', 'risk_flags': risk_flags, 'data_flags': data_flags}
    if candidate.get('ignored_research'):
        data_flags.append('ignored_invalid_research')
    if not research:
        data_flags.append('no_valid_research_context')
    elif research.get('research_status') == 'insufficient_data':
        data_flags.append('research_insufficient_data')
    if research and not has_research_sources(research):
        data_flags.append('research_has_no_sources')
    if research and is_forced_only_research(research):
        data_flags.append('forced_research_not_real_trigger')

    decision, confidence, stake = 'PASS', 'low', 0.0
    code = 'NO_VALID_EDGE_CONTEXT'
    summary = 'PASS: no valid research-backed edge. Paper-only system stays conservative.'
    if fallback_reason:
        code = 'AI_UNAVAILABLE_FALLBACK_PASS'; summary = f'PASS: AI unavailable ({fallback_reason}); conservative fallback.'
    elif research and research.get('research_status') == 'insufficient_data':
        code = 'RESEARCH_INSUFFICIENT_DATA_PASS'; summary = 'PASS: research layer returned insufficient data.'
    elif research and has_market_signal(candidate) and has_research_sources(research) and not is_forced_only_research(research):
        decision = 'WATCH'; confidence = 'medium'; code = 'RESEARCH_BACKED_MARKET_SIGNAL_WATCH'; summary = 'WATCH: valid sourced research plus market signal. Calibration required before PAPER_BET.'
    elif has_market_signal(candidate):
        decision = 'WATCH'; confidence = 'low'; code = 'MOVEMENT_WITHOUT_RESEARCH_WATCH'; summary = 'WATCH: market movement detected but valid sourced research missing.'
    return {'decision': decision, 'confidence': confidence, 'paper_stake_pct': stake, 'reasoning_code': code, 'reasoning_summary': summary, 'risk_flags': risk_flags, 'data_flags': data_flags}


def compact_for_ai(candidate):
    keep = ['market_id', 'event_name', 'event_time_utc', 'is_expired', 'market_type', 'line', 'selection', 'odds', 'movement_from_first', 'change_pct_from_first', 'has_valid_research', 'research_context']
    return {k: candidate.get(k) for k in keep}


def system_prompt():
    return 'Decision Layer V3.2. Paper-only. Use only provided JSON. Return JSON only. If is_expired is true, decision must be PASS. PAPER_BET requires valid sourced research + real market signal + no contradictions + non-forced research trigger. Use PASS if unsure.'


def user_prompt(candidates):
    return json.dumps({
        'mode': 'paper_only',
        'rules': {
            'allowed_decisions': ['PAPER_BET', 'PASS', 'WATCH'],
            'max_paper_stake_pct': 1.0,
            'paper_bet_requires_valid_research': True,
            'paper_bet_requires_research_sources': True,
            'paper_bet_requires_market_signal': True,
            'paper_bet_forbidden_if_only_forced_research': True,
            'pass_if_is_expired': True,
            'pass_if_research_status': ['insufficient_data'],
            'pass_if_echo_chamber_risk': ['high'],
            'pass_if_contradictions_present': True,
            'no_external_knowledge': True,
        },
        'return_schema': {'decisions': [{'market_id': 'string', 'decision': 'PAPER_BET|PASS|WATCH', 'confidence': 'low|medium|high', 'paper_stake_pct': 0.0, 'reasoning_code': 'UPPER_SNAKE_CASE', 'reasoning_summary': 'short', 'risk_flags': [], 'data_flags': []}]},
        'candidates': [compact_for_ai(c) for c in candidates],
    }, ensure_ascii=False)


def extract_json(text):
    raw = str(text or '').strip()
    if raw.startswith('```'):
        raw = raw.strip('`').replace('json\n', '', 1).replace('JSON\n', '', 1).strip()
    try:
        return json.loads(raw)
    except Exception:
        start, end = raw.find('{'), raw.rfind('}')
        if start >= 0 and end > start:
            return json.loads(raw[start:end + 1])
        raise


def call_gemini(candidates):
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        return None, 'missing_gemini_api_key'
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={key}'
    body = {'contents': [{'role': 'user', 'parts': [{'text': system_prompt() + '\n\n' + user_prompt(candidates)}]}], 'generationConfig': {'temperature': 0, 'responseMimeType': 'application/json', 'maxOutputTokens': 4096}}
    try:
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, f'gemini_http_{resp.status_code}'
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        return extract_json(text), None
    except Exception as exc:
        return None, f'gemini_exception_{str(exc)[:120]}'


def normalize_ai_output(ai_output, candidates):
    by_id = {c['market_id']: c for c in candidates}
    out = []
    for d in (ai_output or {}).get('decisions') or []:
        mid = d.get('market_id')
        if mid not in by_id:
            continue
        decision = str(d.get('decision') or 'PASS').upper()
        if decision not in {'PAPER_BET', 'PASS', 'WATCH'}:
            decision = 'PASS'
        confidence = str(d.get('confidence') or 'low').lower()
        if confidence not in {'low', 'medium', 'high'}:
            confidence = 'low'
        try:
            stake = float(d.get('paper_stake_pct') or 0.0)
        except Exception:
            stake = 0.0
        if decision != 'PAPER_BET':
            stake = 0.0
        c = by_id[mid]
        rc = c.get('research_context') or {}
        sq = rc.get('source_quality') or {}
        contradictions = (rc.get('signals') or {}).get('contradictions') or []
        safety_block = (
            c.get('is_expired')
            or not c.get('has_valid_research')
            or rc.get('research_status') == 'insufficient_data'
            or sq.get('echo_chamber_risk') == 'high'
            or contradictions
            or not has_market_signal(c)
            or not has_research_sources(rc)
            or is_forced_only_research(rc)
        )
        if decision == 'PAPER_BET' and safety_block:
            decision = 'PASS'; stake = 0.0
            if not isinstance(d.get('data_flags'), list):
                d['data_flags'] = []
            d['data_flags'].append('paper_bet_blocked_by_v3_2_safety_gate')
            if not has_market_signal(c):
                d['data_flags'].append('missing_market_signal')
            if not has_research_sources(rc):
                d['data_flags'].append('research_has_no_sources')
            if is_forced_only_research(rc):
                d['data_flags'].append('forced_research_not_real_trigger')
        out.append({'market_id': mid, 'decision': decision, 'confidence': confidence, 'paper_stake_pct': max(0.0, min(stake, 1.0)), 'reasoning_code': str(d.get('reasoning_code') or 'UNSPECIFIED'), 'reasoning_summary': str(d.get('reasoning_summary') or '')[:700], 'risk_flags': d.get('risk_flags') if isinstance(d.get('risk_flags'), list) else [], 'data_flags': d.get('data_flags') if isinstance(d.get('data_flags'), list) else []})
    missing = set(by_id) - {d['market_id'] for d in out}
    for mid in missing:
        out.append({'market_id': mid, **conservative_decision(by_id[mid])})
    return out


def build_records(decisions, candidates, engine, fallback_reason=None, ai_eval_ids=None):
    ai_eval_ids = ai_eval_ids or set()
    by_id = {c['market_id']: c for c in candidates}
    now = utc_now()
    records = []
    for d in decisions:
        c = by_id[d['market_id']]
        rc = c.get('research_context')
        records.append({'record_type': 'decision_record', 'decision_id': stable_hash('dec', MODEL_VERSION, d['market_id'], now), 'created_at': now, 'model_version': MODEL_VERSION, 'model': GEMINI_MODEL if engine == 'gemini_scoped' else 'heuristic_fallback', 'engine': engine, 'fallback_reason': fallback_reason, 'ai_eval_used': d['market_id'] in ai_eval_ids and engine == 'gemini_scoped', 'mode': 'paper_only', 'market_id': d['market_id'], 'event_id': c.get('event_id'), 'latest_observation_id': c.get('latest_observation_id'), 'event_name': c.get('event_name'), 'event_time_utc': c.get('event_time_utc'), 'is_expired': c.get('is_expired'), 'market_type': c.get('market_type'), 'line': c.get('line'), 'selection': c.get('selection'), 'odds_at_decision': c.get('odds'), 'decision': d.get('decision'), 'confidence': d.get('confidence'), 'paper_stake_pct': d.get('paper_stake_pct'), 'reasoning_code': d.get('reasoning_code'), 'reasoning_summary': d.get('reasoning_summary'), 'risk_flags': d.get('risk_flags'), 'data_flags': d.get('data_flags'), 'research_used': rc is not None, 'research_id': rc.get('research_id') if rc else None, 'research_status': rc.get('research_status') if rc else None, 'research_confidence': rc.get('confidence') if rc else None, 'source_market_snapshot': c})
    return records


def write_report(records, engine, fallback_reason, total_candidates, ai_eval_count):
    counts = {}
    for r in records:
        counts[r['decision']] = counts.get(r['decision'], 0) + 1
    lines = ['# Odds 2 — Decision Layer V3.2 Report', '', f'Generated: {utc_now()}', f'- Engine: {engine}', f'- Fallback reason: {fallback_reason}', f'- Model version: {MODEL_VERSION}', f'- Candidates prepared: {total_candidates}', f'- AI-evaluated candidates: {ai_eval_count}', f'- Decisions written: {len(records)}', f'- Decision counts: `{json.dumps(counts, ensure_ascii=False)}`', '', '## Decisions']
    for r in records:
        lines += ['', f'### {r.get("event_name")} — {r.get("line")} / {r.get("selection")} @ {r.get("odds_at_decision")}', f'- Decision: {r.get("decision")}', f'- Confidence: {r.get("confidence")}', f'- Paper stake pct: {r.get("paper_stake_pct")}', f'- Reason code: {r.get("reasoning_code")}', f'- Summary: {r.get("reasoning_summary")}', f'- Is expired: {r.get("is_expired")}', f'- Research used: {r.get("research_used")}', f'- Research status: {r.get("research_status")}', f'- AI eval used: {r.get("ai_eval_used")}', f'- Risk flags: `{r.get("risk_flags")}`', f'- Data flags: `{r.get("data_flags")}`']
    path = OUT_REPORTS / 'ai_decision_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)


def main():
    base = prepare_candidates(MAX_CANDIDATES, MODEL_VERSION)
    candidates = enrich_candidates(base.get('candidates') or [])
    interesting = sorted([c for c in candidates if is_interesting_for_ai(c)], key=candidate_priority, reverse=True)[:MAX_AI_EVAL]
    fallback_reason = None
    engine = 'heuristic_scoped'
    decisions_by_id = {c['market_id']: conservative_decision(c) for c in candidates}
    ai_eval_ids = {c['market_id'] for c in interesting}

    if interesting and AI_PROVIDER == 'gemini':
        ai_output, err = call_gemini(interesting)
        if ai_output is None:
            fallback_reason = err
            for c in interesting:
                decisions_by_id[c['market_id']] = conservative_decision(c, fallback_reason=err)
            engine = 'heuristic_fallback'
        else:
            engine = 'gemini_scoped'
            for d in normalize_ai_output(ai_output, interesting):
                decisions_by_id[d['market_id']] = {k: v for k, v in d.items() if k != 'market_id'}
    elif interesting:
        fallback_reason = f'unsupported_provider_{AI_PROVIDER}'
        for c in interesting:
            decisions_by_id[c['market_id']] = conservative_decision(c, fallback_reason=fallback_reason)
        engine = 'heuristic_fallback'

    decisions = [{'market_id': c['market_id'], **decisions_by_id[c['market_id']]} for c in candidates]
    records = build_records(decisions, candidates, engine, fallback_reason, ai_eval_ids)
    append_records(records)
    out = {'generated_at': utc_now(), 'model_version': MODEL_VERSION, 'mode': 'paper_only', 'engine': engine, 'fallback_reason': fallback_reason, 'candidate_count': len(candidates), 'ai_eval_candidate_count': len(interesting), 'decision_count': len(records), 'decisions': records}
    (OUT_LATEST / 'ai_decisions.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    path = write_report(records, engine, fallback_reason, len(candidates), len(interesting))
    print(f'Decision Layer V3.2 OK | candidates={len(candidates)} ai_eval={len(interesting)} decisions={len(records)} engine={engine} fallback_reason={fallback_reason} report={path}')


if __name__ == '__main__':
    main()
