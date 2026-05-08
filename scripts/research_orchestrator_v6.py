import hashlib
import json
import os
import pathlib
import re
from datetime import datetime, timezone

import requests

from tracker import append_records, read_tracker

OUT_LATEST = pathlib.Path('output/latest')
OUT_REPORTS = pathlib.Path('output/reports')
MARKET_STATE_PATH = OUT_LATEST / 'market_state.json'
AI_DECISIONS_PATH = OUT_LATEST / 'ai_decisions.json'
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_REPORTS.mkdir(parents=True, exist_ok=True)

MODEL = os.getenv('GEMINI_RESEARCH_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
VERSION = os.getenv('RESEARCH_VERSION', 'phase2_1_gemini_research_v6')
MAX_CALLS = int(os.getenv('MAX_RESEARCH_CALLS', '5'))
ENABLED = os.getenv('RESEARCH_ENABLED', 'true').lower() == 'true'
FORCE_ONE = os.getenv('SIMULATE_RESEARCH_TRIGGER', 'false').lower() == 'true'
FAKE_WRITE = os.getenv('SIMULATE_RESEARCH_WRITE_RECORD', 'false').lower() == 'true'
PRIORITY_LEAGUES = {'Premier League', 'Superligaen', 'Bundesliga', 'Serie A', 'LaLiga', 'Ligue 1', 'Champions League', 'Europa League'}


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def stable_id(prefix, *parts):
    raw = '|'.join(str(p or '').lower().strip() for p in parts)
    return f'{prefix}_{hashlib.sha256(raw.encode()).hexdigest()[:16]}'


def load_json(path, default):
    p = pathlib.Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding='utf-8'))


def existing_research(records):
    return {r.get('market_id') for r in records if r.get('record_type') == 'research_record' and r.get('research_version') == VERSION and r.get('market_id')}


def decisions_by_market():
    data = load_json(AI_DECISIONS_PATH, {'decisions': []})
    return {d.get('market_id'): d for d in data.get('decisions', []) if d.get('market_id')}


def trigger_reasons(market, decision):
    ms = market.get('movement_summary') or {}
    change = float(ms.get('change_pct_from_first') or 0)
    league = (market.get('event') or {}).get('league')
    out = []
    if change >= 0.10:
        out.append('significant_odds_change_10pct_plus')
    elif change >= 0.03:
        out.append('small_odds_movement_3pct_plus')
    if decision and decision.get('decision') == 'WATCH':
        out.append('ai_decision_watch')
    if league in PRIORITY_LEAGUES and change >= 0.03:
        out.append('priority_league_with_movement')
    if market.get('force_research') is True:
        out.append('manual_force_research')
    return out


def compact_market(market, decision, reasons):
    event = market.get('event') or {}
    m = market.get('market') or {}
    ms = market.get('movement_summary') or {}
    score = 1 if 'simulated_research_trigger' in reasons else 0
    if 'significant_odds_change_10pct_plus' in reasons:
        score += 100
    if 'small_odds_movement_3pct_plus' in reasons:
        score += 40
    if 'ai_decision_watch' in reasons:
        score += 35
    if event.get('league') in PRIORITY_LEAGUES:
        score += 10
    return {
        'market_id': market.get('market_id'),
        'event_id': market.get('event_id'),
        'event_name': f'{event.get("home")} vs {event.get("away")}',
        'league': event.get('league'),
        'event_time_utc': (market.get('event_time') or {}).get('utc'),
        'market_type': m.get('type'),
        'line': m.get('line'),
        'selection': m.get('selection'),
        'odds': m.get('odds'),
        'movement_summary': ms,
        'decision': decision,
        'trigger_reasons': reasons,
        'priority_score': score,
    }


def select_candidates():
    state = load_json(MARKET_STATE_PATH, {'markets': []})
    existing = existing_research(read_tracker())
    decisions = decisions_by_market()
    candidates, skipped, eligible_no_trigger = [], [], []
    for market in state.get('markets', []):
        mid = market.get('market_id')
        if not mid:
            continue
        if mid in existing:
            skipped.append({'market_id': mid, 'reason': 'research_exists_for_version'}); continue
        if not market.get('active'):
            skipped.append({'market_id': mid, 'reason': 'inactive_market'}); continue
        if not (market.get('parser_confidence') or {}).get('real_bet_allowed'):
            skipped.append({'market_id': mid, 'reason': 'data_integrity_not_real_candidate'}); continue
        decision = decisions.get(mid)
        reasons = trigger_reasons(market, decision)
        if not reasons:
            eligible_no_trigger.append((market, decision)); skipped.append({'market_id': mid, 'reason': 'no_research_trigger'}); continue
        candidates.append(compact_market(market, decision, reasons))
    if FORCE_ONE and not candidates and eligible_no_trigger:
        market, decision = eligible_no_trigger[0]
        candidates.append(compact_market(market, decision, ['simulated_research_trigger']))
    candidates.sort(key=lambda c: (-c.get('priority_score', 0), c.get('event_time_utc') or ''))
    selected = candidates[:MAX_CALLS]
    payload = {'generated_at': now_utc(), 'research_version': VERSION, 'candidate_count': len(selected), 'all_triggered_count': len(candidates), 'skipped_count': len(skipped), 'simulate_research_trigger': FORCE_ONE, 'simulate_research_write_record': FAKE_WRITE, 'candidates': selected, 'skipped': skipped[:250]}
    (OUT_LATEST / 'research_candidates.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    return payload


def prompt(candidate):
    return f'''Use Google Search grounding. Return ONLY minified JSON. No markdown. No URLs.
Match: {candidate.get('event_name')}. Selection: {candidate.get('selection')}. Odds: {candidate.get('odds')}. UTC: {candidate.get('event_time_utc')}. League: {candidate.get('league')}.
Find current probability-changing info. Prefer official/reputable sources. Ignore betting-tip pages and odds-only pages.
Output exactly this compact schema with short values:
{{"status":"completed|insufficient_data|failed","hard":"max 180 chars: injuries/suspensions/lineups only","soft":"max 180 chars: form/motivation/schedule only","risk":"none|low|medium|high","confidence":"low|medium|high","summary":"max 160 chars","flags":[]}}
'''


def parse_json_text(text):
    raw = str(text or '').strip()
    m = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', raw, flags=re.S | re.I)
    if m:
        raw = m.group(1)
    try:
        return json.loads(raw)
    except Exception:
        start, end = raw.find('{'), raw.rfind('}')
        if start >= 0 and end > start:
            return json.loads(raw[start:end + 1])
        raise


def extract_grounding(data):
    chunks = []
    gm = data.get('candidates', [{}])[0].get('groundingMetadata') or {}
    for ch in gm.get('groundingChunks') or []:
        web = ch.get('web') or {}
        uri = web.get('uri')
        if uri:
            chunks.append({'uri': uri, 'title': web.get('title')})
    return chunks


def fallback_record(text, chunks, parse_error):
    return {
        'status': 'completed_unstructured' if text and len(text.strip()) > 30 else 'insufficient_data',
        'hard': '', 'soft': '', 'risk': 'medium', 'confidence': 'low',
        'summary': 'Grounded response returned but JSON parsing failed.',
        'flags': ['json_parse_fallback', 'needs_prompt_tuning'],
        'grounding_chunks': chunks,
        '_error_detail': {'code': 'gemini_research_json_parse_fallback', 'parse_error': str(parse_error)[:500], 'response_text': str(text)[:2000]},
    }


def gemini_research(candidate):
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        return None, {'code': 'missing_gemini_api_key'}
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={key}'
    body = {
        'contents': [{'role': 'user', 'parts': [{'text': prompt(candidate)}]}],
        'tools': [{'google_search': {}}],
        'generationConfig': {'temperature': 0, 'maxOutputTokens': 2048},
    }
    features = {'google_search_enabled': True, 'response_mime_type': None, 'model': MODEL, 'version': VERSION}
    try:
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, {'code': f'gemini_research_http_{resp.status_code}', 'status_code': resp.status_code, 'response_text': resp.text[:2000], 'request_features': features}
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        chunks = extract_grounding(data)
        try:
            parsed = parse_json_text(text)
        except Exception as exc:
            parsed = fallback_record(text, chunks, exc)
        parsed['grounding_chunks'] = chunks
        parsed['source_links'] = [x.get('uri') for x in chunks[:3] if x.get('uri')]
        err = parsed.pop('_error_detail', None)
        return parsed, err
    except Exception as exc:
        return None, {'code': 'gemini_research_exception', 'response_text': str(exc)[:2000], 'request_features': features}


def fake_output():
    return {'status': 'simulated', 'hard': '', 'soft': '', 'risk': 'none', 'confidence': 'low', 'summary': 'Simulated research record.', 'flags': ['simulated_research_record', 'not_real_research'], 'grounding_chunks': [], 'source_links': []}


def error_code(error):
    return error.get('code') if isinstance(error, dict) else error or 'research_unavailable'


def normalize(candidate, output, error=None):
    if output is None:
        output = {'status': 'failed', 'hard': '', 'soft': '', 'risk': 'high', 'confidence': 'low', 'summary': f'Research failed: {error_code(error)}', 'flags': [error_code(error)], 'grounding_chunks': [], 'source_links': []}
    status = output.get('status') or output.get('research_status') or 'completed'
    hard = str(output.get('hard') or '')[:300]
    soft = str(output.get('soft') or '')[:300]
    risk = output.get('risk') if output.get('risk') in {'none', 'low', 'medium', 'high'} else 'medium'
    return {'record_type': 'research_record', 'research_id': stable_id('res', VERSION, candidate.get('market_id'), now_utc()), 'research_version': VERSION, 'created_at': now_utc(), 'provider': 'simulation' if FAKE_WRITE else 'gemini', 'model': 'simulated_research' if FAKE_WRITE else MODEL, 'market_id': candidate.get('market_id'), 'event_id': candidate.get('event_id'), 'event_name': candidate.get('event_name'), 'selection': candidate.get('selection'), 'odds': candidate.get('odds'), 'trigger_reasons': candidate.get('trigger_reasons'), 'priority_score': candidate.get('priority_score'), 'research_status': status, 'source_links': output.get('source_links') if isinstance(output.get('source_links'), list) else [], 'source_quality': {'primary_source_count': 0, 'secondary_source_count': len(output.get('source_links') or []), 'echo_chamber_risk': risk}, 'signals': {'hard': [hard] if hard else [], 'soft': [soft] if soft else [], 'contradictions': [], 'injuries': [hard] if hard else [], 'lineups': [], 'motivation': [soft] if soft else [], 'form': [], 'market_consensus': None}, 'confidence': output.get('confidence') if output.get('confidence') in {'low', 'medium', 'high'} else 'low', 'summary': str(output.get('summary') or '')[:1000], 'research_flags': output.get('flags') if isinstance(output.get('flags'), list) else [], 'error_detail': error if isinstance(error, dict) else None, 'grounding_chunks': output.get('grounding_chunks') if isinstance(output.get('grounding_chunks'), list) else [], 'source_market_snapshot': candidate}


def write_report(payload, records):
    lines = ['# Odds 2 — Phase 2.1 Research Report', '', f'Generated: {now_utc()}', f'- Research version: {VERSION}', f'- Gemini model: {MODEL}', f'- Research enabled: {ENABLED}', f'- Simulate research trigger: {FORCE_ONE}', f'- Simulate research write record: {FAKE_WRITE}', f'- Research candidates selected: {payload.get("candidate_count")}', f'- All triggered markets: {payload.get("all_triggered_count")}', f'- Research records written: {len(records)}', '']
    if not records:
        lines.append('No research records written. No markets met research triggers.')
    for r in records:
        sq, err, sig = r.get('source_quality') or {}, r.get('error_detail') or {}, r.get('signals') or {}
        lines += ['', f'### {r.get("event_name")} — {r.get("selection")} @ {r.get("odds")}', f'- Status: {r.get("research_status")}', f'- Provider: {r.get("provider")}', f'- Confidence: {r.get("confidence")}', f'- Echo chamber risk: {sq.get("echo_chamber_risk")}', f'- Source counts: primary={sq.get("primary_source_count")}, secondary={sq.get("secondary_source_count")}', f'- Triggers: `{r.get("trigger_reasons")}`', f'- Hard signals: `{sig.get("hard")}`', f'- Soft signals: `{sig.get("soft")}`', f'- Summary: {r.get("summary")}', f'- Source links: `{r.get("source_links")}`', f'- Research flags: `{r.get("research_flags")}`', f'- Error code: `{err.get("code") if isinstance(err, dict) else None}`', f'- Error detail: `{err.get("response_text") if isinstance(err, dict) else None}`']
    path = OUT_REPORTS / 'research_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)


def main():
    payload = select_candidates()
    records = []
    if ENABLED:
        for c in payload.get('candidates', []):
            output, error = (fake_output(), None) if FAKE_WRITE else gemini_research(c)
            records.append(normalize(c, output, error))
        append_records(records)
    (OUT_LATEST / 'research_records.json').write_text(json.dumps({'generated_at': now_utc(), 'research_version': VERSION, 'records': records}, ensure_ascii=False, indent=2), encoding='utf-8')
    path = write_report(payload, records)
    print(f'Phase 2.1 research OK | candidates={payload.get("candidate_count")} records={len(records)} report={path}')


if __name__ == '__main__':
    main()
