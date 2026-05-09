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

MODEL_VERSION = os.getenv('AI_DECISION_VERSION', 'phase2_decision_v3_research_context')
AI_PROVIDER = os.getenv('AI_PROVIDER', 'gemini').lower()
GEMINI_MODEL = os.getenv('GEMINI_DECISION_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
MAX_CANDIDATES = int(os.getenv('AI_MAX_CANDIDATES', '90'))

VALID_RESEARCH_STATUSES = {'completed', 'insufficient_data'}
INVALID_RESEARCH_STATUSES = {'failed', 'simulated', 'completed_unstructured'}


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


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
        invalid = (
            provider == 'simulation'
            or status in INVALID_RESEARCH_STATUSES
            or 'simulated_research_record' in flags
            or 'not_real_research' in flags
        )
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


def research_context_for(candidate, research):
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
        'research_model': research.get('research_model') or research.get('model'),
        'structure_model': research.get('structure_model'),
        'confidence': research.get('confidence'),
        'summary': research.get('summary'),
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
        e['research_context'] = research_context_for(c, r)
        e['has_valid_research'] = r is not None
        if not r and mid in ignored:
            e['ignored_research'] = ignored[mid]
        enriched.append(e)
    return enriched


def conservative_decision(candidate, fallback_reason=None):
    change = float(candidate.get('change_pct_from_first') or 0)
    movement = candidate.get('movement_from_first')
    research = candidate.get('research_context')
    data_flags = []
    risk_flags = []

    if fallback_reason:
        data_flags.append(fallback_reason)
    if candidate.get('ignored_research'):
        data_flags.append('ignored_invalid_research')
    if not research:
        data_flags.append('no_valid_research_context')
    elif research.get('research_status') == 'insufficient_data':
        data_flags.append('research_insufficient_data')

    decision = 'PASS'
    confidence = 'low'
    stake = 0.0
    code = 'NO_VALID_EDGE_CONTEXT'
    summary = 'PASS: no valid research-backed edge. Paper-only system stays conservative.'

    if fallback_reason:
        code = 'AI_UNAVAILABLE_FALLBACK_PASS'
        summary = f'PASS: AI unavailable ({fallback_reason}); conservative fallback.'
    elif research and research.get('research_status') == 'insufficient_data':
        code = 'RESEARCH_INSUFFICIENT_DATA_PASS'
        summary = 'PASS: research layer returned insufficient data.'
    elif research and movement == 'shortened' and change >= 0.10:
        decision = 'WATCH'
        confidence = 'medium'
        code = 'RESEARCH_BACKED_SIGNIFICANT_MOVEMENT_WATCH'
        summary = 'WATCH: valid research exists and significant shortening detected; still not enough for PAPER_BET without V3 calibration.'
    elif research and movement == 'shortened' and change >= 0.03:
        decision = 'WATCH'
        confidence = 'low'
        code = 'RESEARCH_BACKED_SMALL_MOVEMENT_WATCH'
        summary = 'WATCH: valid research exists and small shortening detected.'
    elif movement == 'shortened' and change >= 0.03:
        decision = 'WATCH'
        confidence = 'low'
        code = 'MOVEMENT_WITHOUT_RESEARCH_WATCH'
        summary = 'WATCH: movement detected but valid research context is missing.'

    return {'decision': decision, 'confidence': confidence, 'paper_stake_pct': stake, 'reasoning_code': code, 'reasoning_summary': summary, 'risk_flags': risk_flags, 'data_flags': data_flags}


def system_prompt():
    return (
        'You are Decision Layer V3 for a paper-only betting research pipeline. '
        'Use only provided JSON. Do not use outside knowledge. Do not recommend real betting. '
        'You must ignore simulated, failed, and completed_unstructured research; those are already filtered out. '
        'PAPER_BET is allowed only when valid research_context and market movement both support the same side, data quality is acceptable, and no major contradiction exists. '
        'Use PASS for insufficient data, expired/irrelevant research, contradictions, or no clear edge. '
        'Use WATCH when research or movement is interesting but not strong enough. '
        'Return valid JSON only.'
    )


def user_prompt(payload):
    compact = {
        'mode': 'paper_only',
        'model_version': MODEL_VERSION,
        'rules': {
            'allowed_decisions': ['PAPER_BET', 'PASS', 'WATCH'],
            'max_paper_stake_pct': 1.0,
            'paper_bet_requires_valid_research': True,
            'paper_bet_requires_market_signal': True,
            'pass_if_research_status': ['insufficient_data'],
            'pass_if_echo_chamber_risk': ['high'],
            'pass_if_contradictions_present': True,
            'no_external_knowledge': True,
        },
        'return_schema': {'decisions': [{'market_id': 'string', 'decision': 'PAPER_BET|PASS|WATCH', 'confidence': 'low|medium|high', 'paper_stake_pct': 0.0, 'reasoning_code': 'UPPER_SNAKE_CASE', 'reasoning_summary': 'short', 'risk_flags': [], 'data_flags': []}]},
        'candidates': payload.get('candidates') or [],
    }
    return json.dumps(compact, ensure_ascii=False)


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


def call_gemini(payload):
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        return None, 'missing_gemini_api_key'
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={key}'
    body = {
        'contents': [{'role': 'user', 'parts': [{'text': system_prompt() + '\n\n' + user_prompt(payload)}]}],
        'generationConfig': {'temperature': 0, 'responseMimeType': 'application/json', 'maxOutputTokens': 8192},
    }
    try:
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, f'gemini_http_{resp.status_code}'
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        return extract_json(text), None
    except Exception as exc:
        return None, f'gemini_exception_{str(exc)[:120]}'


def call_ai(payload):
    if AI_PROVIDER != 'gemini':
        return None, 'heuristic_fallback', f'unsupported_provider_for_v3_{AI_PROVIDER}'
    out, err = call_gemini(payload)
    if out is None:
        return None, 'heuristic_fallback', err
    return out, 'gemini', None


def normalize_ai_output(ai_output, candidates):
    by_id = {c['market_id']: c for c in candidates}
    out = []
    raw = (ai_output or {}).get('decisions') or []
    for d in raw:
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
        if decision == 'PAPER_BET':
            c = by_id[mid]
            rc = c.get('research_context') or {}
            sq = rc.get('source_quality') or {}
            contradictions = (rc.get('signals') or {}).get('contradictions') or []
            if not c.get('has_valid_research') or rc.get('research_status') == 'insufficient_data' or sq.get('echo_chamber_risk') == 'high' or contradictions:
                decision = 'PASS'
                stake = 0.0
                d.setdefault('data_flags', [])
                if isinstance(d['data_flags'], list):
                    d['data_flags'].append('paper_bet_blocked_by_v3_safety_gate')
        stake = max(0.0, min(stake, 1.0))
        out.append({'market_id': mid, 'decision': decision, 'confidence': confidence, 'paper_stake_pct': stake, 'reasoning_code': str(d.get('reasoning_code') or 'UNSPECIFIED'), 'reasoning_summary': str(d.get('reasoning_summary') or '')[:700], 'risk_flags': d.get('risk_flags') if isinstance(d.get('risk_flags'), list) else [], 'data_flags': d.get('data_flags') if isinstance(d.get('data_flags'), list) else []})
    missing = set(by_id) - {d['market_id'] for d in out}
    for mid in missing:
        out.append({'market_id': mid, **conservative_decision(by_id[mid])})
    return out


def build_records(decisions, candidates, engine, fallback_reason=None):
    by_id = {c['market_id']: c for c in candidates}
    now = utc_now()
    records = []
    for d in decisions:
        c = by_id[d['market_id']]
        rc = c.get('research_context')
        records.append({
            'record_type': 'decision_record',
            'decision_id': stable_hash('dec', MODEL_VERSION, d['market_id'], now),
            'created_at': now,
            'model_version': MODEL_VERSION,
            'model': GEMINI_MODEL if engine == 'gemini' else 'heuristic_fallback',
            'engine': engine,
            'fallback_reason': fallback_reason,
            'mode': 'paper_only',
            'market_id': d['market_id'],
            'event_id': c.get('event_id'),
            'latest_observation_id': c.get('latest_observation_id'),
            'event_name': c.get('event_name'),
            'event_time_utc': c.get('event_time_utc'),
            'market_type': c.get('market_type'),
            'line': c.get('line'),
            'selection': c.get('selection'),
            'odds_at_decision': c.get('odds'),
            'decision': d.get('decision'),
            'confidence': d.get('confidence'),
            'paper_stake_pct': d.get('paper_stake_pct'),
            'reasoning_code': d.get('reasoning_code'),
            'reasoning_summary': d.get('reasoning_summary'),
            'risk_flags': d.get('risk_flags'),
            'data_flags': d.get('data_flags'),
            'research_used': rc is not None,
            'research_id': rc.get('research_id') if rc else None,
            'research_status': rc.get('research_status') if rc else None,
            'research_confidence': rc.get('confidence') if rc else None,
            'source_market_snapshot': c,
        })
    return records


def write_report(records, payload, engine, fallback_reason=None):
    counts = {}
    for r in records:
        counts[r['decision']] = counts.get(r['decision'], 0) + 1
    lines = ['# Odds 2 — Decision Layer V3 Report', '', f'Generated: {utc_now()}', f'- Engine: {engine}', f'- Fallback reason: {fallback_reason}', f'- Model version: {MODEL_VERSION}', f'- Candidates prepared: {payload.get("candidate_count")}', f'- Decisions written: {len(records)}', f'- Decision counts: `{json.dumps(counts, ensure_ascii=False)}`', '', '## Decisions']
    if not records:
        lines.append('No new decisions.')
    for r in records:
        lines += ['', f'### {r.get("event_name")} — {r.get("line")} / {r.get("selection")} @ {r.get("odds_at_decision")}', f'- Decision: {r.get("decision")}', f'- Confidence: {r.get("confidence")}', f'- Paper stake pct: {r.get("paper_stake_pct")}', f'- Reason code: {r.get("reasoning_code")}', f'- Summary: {r.get("reasoning_summary")}', f'- Research used: {r.get("research_used")}', f'- Research status: {r.get("research_status")}', f'- Risk flags: `{r.get("risk_flags")}`', f'- Data flags: `{r.get("data_flags")}`']
    path = OUT_REPORTS / 'ai_decision_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)


def main():
    base_payload = prepare_candidates(MAX_CANDIDATES, MODEL_VERSION)
    candidates = enrich_candidates(base_payload.get('candidates') or [])
    payload = dict(base_payload)
    payload['model_version'] = MODEL_VERSION
    payload['candidates'] = candidates
    payload['candidate_count'] = len(candidates)
    fallback_reason = None
    if not candidates:
        records = []
        engine = 'none_no_candidates'
    else:
        ai_output, engine, fallback_reason = call_ai(payload)
        if ai_output is None:
            decisions = [{'market_id': c['market_id'], **conservative_decision(c, fallback_reason=fallback_reason)} for c in candidates]
        else:
            decisions = normalize_ai_output(ai_output, candidates)
        records = build_records(decisions, candidates, engine, fallback_reason)
        append_records(records)
    out = {'generated_at': utc_now(), 'model_version': MODEL_VERSION, 'mode': 'paper_only', 'engine': engine, 'fallback_reason': fallback_reason, 'candidate_count': len(candidates), 'decision_count': len(records), 'decisions': records}
    (OUT_LATEST / 'ai_decisions.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    path = write_report(records, payload, engine, fallback_reason)
    print(f'Decision Layer V3 OK | candidates={len(candidates)} decisions={len(records)} engine={engine} fallback_reason={fallback_reason} report={path}')


if __name__ == '__main__':
    main()
