import hashlib
import json
import os
import pathlib
from datetime import datetime, timezone

from prepare_candidates import prepare_candidates, MODEL_VERSION
from tracker import append_records

OUT_LATEST = pathlib.Path('output/latest')
OUT_REPORTS = pathlib.Path('output/reports')
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_REPORTS.mkdir(parents=True, exist_ok=True)

AI_PROVIDER = os.getenv('AI_PROVIDER', 'gemini').lower()
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4o-mini')
GEMINI_MODEL = os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')
MAX_CANDIDATES = int(os.getenv('AI_MAX_CANDIDATES', '90'))


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def stable_hash(prefix, *parts, length=16):
    raw = '|'.join(str(p or '').strip().lower() for p in parts)
    return f'{prefix}_{hashlib.sha256(raw.encode("utf-8")).hexdigest()[:length]}'


def heuristic_decision(candidate, fallback_reason=None):
    """Fallback used when AI provider is unavailable. It is intentionally conservative."""
    odds = float(candidate.get('odds') or 0)
    change = float(candidate.get('change_pct_from_first') or 0)
    movement = candidate.get('movement_from_first')
    hard = candidate.get('hard_gates') or {}
    risk_flags = []
    data_flags = []

    if fallback_reason:
        data_flags.append(fallback_reason)
    if not all(hard.values()):
        data_flags.append('failed_hard_gate')
    if odds < 1.20 or odds > 8.00:
        risk_flags.append('odds_outside_phase2_heuristic_range')
    if candidate.get('league') == 'unknown':
        data_flags.append('league_unknown')

    decision = 'PASS'
    confidence = 'low'
    paper_stake_pct = 0.0
    reasoning_code = 'NO_VALUE_SIGNAL'
    summary = 'No paper bet: no research layer and no meaningful market movement signal.'

    if fallback_reason:
        reasoning_code = 'AI_UNAVAILABLE_FALLBACK_PASS'
        summary = f'AI provider unavailable ({fallback_reason}). Conservative fallback: PASS.'
    elif movement == 'shortened' and change >= 0.10:
        decision = 'WATCH'
        confidence = 'medium'
        reasoning_code = 'SIGNIFICANT_STEAM_WATCH'
        summary = 'Significant shortening detected. Watch candidate for Phase 2.1 research, not a paper bet yet.'
    elif movement == 'shortened' and change >= 0.03:
        decision = 'WATCH'
        confidence = 'low'
        reasoning_code = 'SMALL_STEAM_WATCH'
        summary = 'Small odds shortening detected. Watch only.'

    return {
        'decision': decision,
        'confidence': confidence,
        'paper_stake_pct': paper_stake_pct,
        'reasoning_code': reasoning_code,
        'reasoning_summary': summary,
        'risk_flags': risk_flags,
        'data_flags': data_flags,
    }


def system_prompt():
    return (
        'You are the paper-only decision layer for a betting data pipeline. '
        'You do not place real bets. You must be conservative. '
        'Use only the JSON data provided. Do not invent injuries, form, news, odds comparisons, or external facts. '
        'Return valid JSON only. For each candidate return exactly one decision: PAPER_BET, PASS, or WATCH. '
        'Prefer PASS unless there is a clear reason from market data. WATCH is for candidates that need later research. '
        'PAPER_BET is allowed only for paper tracking and only when the provided market data supports it. '
        'Never use real money language. Do not recommend real betting.'
    )


def user_prompt(payload):
    compact = {
        'mode': 'paper_only',
        'model_version': payload.get('model_version'),
        'instructions': {
            'allowed_decisions': ['PAPER_BET', 'PASS', 'WATCH'],
            'no_external_knowledge': True,
            'return_schema': {
                'decisions': [
                    {
                        'market_id': 'string',
                        'decision': 'PAPER_BET|PASS|WATCH',
                        'confidence': 'low|medium|high',
                        'paper_stake_pct': 'number, 0.0 to 1.0, paper only',
                        'reasoning_code': 'UPPER_SNAKE_CASE',
                        'reasoning_summary': 'short string',
                        'risk_flags': ['string'],
                        'data_flags': ['string']
                    }
                ]
            }
        },
        'candidates': payload.get('candidates') or []
    }
    return json.dumps(compact, ensure_ascii=False)


def call_openai(payload):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return None, 'missing_openai_api_key'
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        resp = client.chat.completions.create(
            model=OPENAI_MODEL,
            temperature=0,
            response_format={'type': 'json_object'},
            messages=[
                {'role': 'system', 'content': system_prompt()},
                {'role': 'user', 'content': user_prompt(payload)},
            ],
        )
        return json.loads(resp.choices[0].message.content), None
    except Exception as exc:
        err = str(exc)
        reason = 'openai_api_error'
        if 'billing_not_active' in err or 'account is not active' in err:
            reason = 'openai_billing_not_active'
        elif 'rate_limit' in err.lower() or 'ratelimit' in err.lower():
            reason = 'openai_rate_limit'
        elif 'invalid_api_key' in err.lower() or 'incorrect api key' in err.lower():
            reason = 'openai_invalid_api_key'
        print(f'OpenAI unavailable, using conservative fallback: {reason} | {err[:300]}')
        return None, reason


def extract_json_object(text):
    raw = str(text or '').strip()
    if raw.startswith('```'):
        raw = raw.strip('`')
        raw = raw.replace('json\n', '', 1).replace('JSON\n', '', 1).strip()
    try:
        return json.loads(raw)
    except Exception:
        start = raw.find('{')
        end = raw.rfind('}')
        if start >= 0 and end > start:
            return json.loads(raw[start:end + 1])
        raise


def call_gemini(payload):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return None, 'missing_gemini_api_key'
    try:
        import requests
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={api_key}'
        prompt = system_prompt() + '\n\nReturn JSON only.\n\n' + user_prompt(payload)
        body = {
            'contents': [
                {
                    'role': 'user',
                    'parts': [{'text': prompt}]
                }
            ],
            'generationConfig': {
                'temperature': 0,
                'responseMimeType': 'application/json'
            }
        }
        resp = requests.post(url, json=body, timeout=60)
        if resp.status_code >= 400:
            err = resp.text[:500]
            reason = 'gemini_api_error'
            if resp.status_code == 429:
                reason = 'gemini_rate_limit'
            elif resp.status_code in {401, 403}:
                reason = 'gemini_auth_or_permission_error'
            print(f'Gemini unavailable, using conservative fallback: {reason} | {err}')
            return None, reason
        data = resp.json()
        text = data['candidates'][0]['content']['parts'][0]['text']
        return extract_json_object(text), None
    except Exception as exc:
        err = str(exc)
        reason = 'gemini_api_error'
        if 'api key' in err.lower():
            reason = 'gemini_invalid_api_key'
        print(f'Gemini unavailable, using conservative fallback: {reason} | {err[:300]}')
        return None, reason


def call_ai_provider(payload):
    if AI_PROVIDER == 'openai':
        output, reason = call_openai(payload)
        return output, 'openai' if output is not None else 'heuristic_fallback', reason
    if AI_PROVIDER == 'gemini':
        output, reason = call_gemini(payload)
        return output, 'gemini' if output is not None else 'heuristic_fallback', reason
    return None, 'heuristic_fallback', f'unsupported_ai_provider_{AI_PROVIDER}'


def normalize_ai_output(ai_output, candidates):
    by_id = {c['market_id']: c for c in candidates}
    decisions = []
    raw_decisions = (ai_output or {}).get('decisions') or []
    for d in raw_decisions:
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
        stake = max(0.0, min(stake, 1.0))
        decisions.append({
            'market_id': mid,
            'decision': decision,
            'confidence': confidence,
            'paper_stake_pct': stake,
            'reasoning_code': str(d.get('reasoning_code') or 'UNSPECIFIED'),
            'reasoning_summary': str(d.get('reasoning_summary') or '')[:500],
            'risk_flags': d.get('risk_flags') if isinstance(d.get('risk_flags'), list) else [],
            'data_flags': d.get('data_flags') if isinstance(d.get('data_flags'), list) else [],
        })
    missing = set(by_id) - {d['market_id'] for d in decisions}
    for mid in missing:
        c = by_id[mid]
        hd = heuristic_decision(c)
        decisions.append({'market_id': mid, **hd})
    return decisions


def build_decision_records(decisions, candidates, engine, fallback_reason=None):
    by_id = {c['market_id']: c for c in candidates}
    now = utc_now()
    records = []
    for d in decisions:
        c = by_id[d['market_id']]
        decision_id = stable_hash('dec', MODEL_VERSION, d['market_id'], now)
        model_name = GEMINI_MODEL if engine == 'gemini' else OPENAI_MODEL if engine == 'openai' else 'heuristic_fallback'
        records.append({
            'record_type': 'decision_record',
            'decision_id': decision_id,
            'created_at': now,
            'model_version': MODEL_VERSION,
            'model': model_name,
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
            'source_market_snapshot': c,
        })
    return records


def write_report(records, candidate_payload, engine, fallback_reason=None):
    counts = {}
    for r in records:
        counts[r['decision']] = counts.get(r['decision'], 0) + 1
    lines = [
        '# Odds 2 — Phase 2.0 Paper Decision Report', '',
        f'Generated: {utc_now()}',
        f'- Engine: {engine}',
        f'- Fallback reason: {fallback_reason}',
        f'- Model version: {MODEL_VERSION}',
        f'- Candidates prepared: {candidate_payload.get("candidate_count")}',
        f'- Decisions written: {len(records)}',
        f'- Decision counts: `{json.dumps(counts, ensure_ascii=False)}`', '',
        '## Decisions',
    ]
    if not records:
        lines.append('No new decisions.')
    for r in records:
        lines.extend([
            '',
            f'### {r.get("event_name")} — {r.get("line")} / {r.get("selection")} @ {r.get("odds_at_decision")}',
            f'- Decision: {r.get("decision")}',
            f'- Confidence: {r.get("confidence")}',
            f'- Paper stake pct: {r.get("paper_stake_pct")}',
            f'- Reason code: {r.get("reasoning_code")}',
            f'- Summary: {r.get("reasoning_summary")}',
            f'- Risk flags: `{r.get("risk_flags")}`',
            f'- Data flags: `{r.get("data_flags")}`',
        ])
    path = OUT_REPORTS / 'ai_decision_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)


def main():
    payload = prepare_candidates(MAX_CANDIDATES, MODEL_VERSION)
    candidates = payload.get('candidates') or []
    fallback_reason = None
    if not candidates:
        records = []
        engine = 'none_no_candidates'
    else:
        ai_output, engine, fallback_reason = call_ai_provider(payload)
        if ai_output is None:
            decisions = [heuristic_decision(c, fallback_reason=fallback_reason) | {'market_id': c['market_id']} for c in candidates]
        else:
            decisions = normalize_ai_output(ai_output, candidates)
        records = build_decision_records(decisions, candidates, engine, fallback_reason=fallback_reason)
        append_records(records)

    out = {
        'generated_at': utc_now(),
        'model_version': MODEL_VERSION,
        'mode': 'paper_only',
        'engine': engine,
        'fallback_reason': fallback_reason,
        'candidate_count': len(candidates),
        'decision_count': len(records),
        'decisions': records,
    }
    (OUT_LATEST / 'ai_decisions.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    report_path = write_report(records, payload, engine, fallback_reason=fallback_reason)
    print(f'Phase 2.0 paper decisions OK | candidates={len(candidates)} decisions={len(records)} engine={engine} fallback_reason={fallback_reason} report={report_path}')


if __name__ == '__main__':
    main()
