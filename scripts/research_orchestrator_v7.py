import hashlib
import json
import os
import pathlib
from datetime import datetime, timezone

import requests

from tracker import append_records, read_tracker

OUT_LATEST = pathlib.Path('output/latest')
OUT_REPORTS = pathlib.Path('output/reports')
MARKET_STATE_PATH = OUT_LATEST / 'market_state.json'
AI_DECISIONS_PATH = OUT_LATEST / 'ai_decisions.json'
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_REPORTS.mkdir(parents=True, exist_ok=True)

RESEARCH_MODEL = os.getenv('GEMINI_RESEARCH_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
STRUCTURE_MODEL = os.getenv('GEMINI_STRUCTURE_MODEL', os.getenv('GEMINI_RESEARCH_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')))
VERSION = os.getenv('RESEARCH_VERSION', 'phase2_1_gemini_research_v7_twostep')
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


def gemini_url(model):
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        return None
    return f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}'


def extract_grounding(data):
    chunks = []
    gm = data.get('candidates', [{}])[0].get('groundingMetadata') or {}
    for ch in gm.get('groundingChunks') or []:
        web = ch.get('web') or {}
        uri = web.get('uri')
        if uri:
            chunks.append({'uri': uri, 'title': web.get('title')})
    return chunks


def research_prompt(candidate):
    return f'''Use Google Search grounding. Write a short research bulletin for a paper-only football model.
Match: {candidate.get('event_name')}
Selection: {candidate.get('selection')}
Odds: {candidate.get('odds')}
Event UTC: {candidate.get('event_time_utc')}
League: {candidate.get('league')}

Find current probability-changing facts only: injuries, suspensions, likely lineups, goalkeeper changes, fixture congestion, table motivation, weather/pitch, and market consensus if available.
Prefer official club/league/competition sources and reputable sports media.
Avoid betting-tip sites, affiliate pages, and odds-only previews.
Do not recommend bets. Do not output JSON. Do not output URLs.
Use 4 bullets max, each under 160 characters. If data is weak, say insufficient data.'''


def structure_prompt(candidate, raw_text, sources):
    compact_sources = [{'title': s.get('title'), 'uri': s.get('uri')} for s in sources[:5]]
    payload = {
        'task': 'Convert grounded football research text into a validated JSON research record for paper-only analysis.',
        'candidate': candidate,
        'raw_research_text': raw_text[:3000],
        'source_metadata': compact_sources,
        'rules': [
            'Return JSON only.',
            'Do not invent facts not present in raw_research_text.',
            'Keep all strings short.',
            'Use hard for injuries, suspensions, lineups, goalkeeper changes.',
            'Use soft for motivation, form, schedule, weather, market consensus.',
            'If evidence is weak, use insufficient_data and low confidence.'
        ],
        'schema': {
            'research_status': 'completed|insufficient_data|failed',
            'source_quality': {'primary_source_count': 0, 'secondary_source_count': 0, 'echo_chamber_risk': 'none|low|medium|high'},
            'signals': {'hard': [], 'soft': [], 'contradictions': []},
            'confidence': 'low|medium|high',
            'summary': 'max 250 chars',
            'research_flags': []
        }
    }
    return json.dumps(payload, ensure_ascii=False)


def parse_json(text):
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


def call_research_step(candidate):
    url = gemini_url(RESEARCH_MODEL)
    if not url:
        return None, [], {'code': 'missing_gemini_api_key'}
    body = {
        'contents': [{'role': 'user', 'parts': [{'text': research_prompt(candidate)}]}],
        'tools': [{'google_search': {}}],
        'generationConfig': {'temperature': 0, 'maxOutputTokens': 1024},
    }
    try:
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, [], {'code': f'gemini_research_http_{resp.status_code}', 'status_code': resp.status_code, 'response_text': resp.text[:2000]}
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        return text, extract_grounding(data), None
    except Exception as exc:
        return None, [], {'code': 'gemini_research_exception', 'response_text': str(exc)[:2000]}


def call_structure_step(candidate, raw_text, sources):
    url = gemini_url(STRUCTURE_MODEL)
    if not url:
        return None, {'code': 'missing_gemini_api_key'}
    body = {
        'contents': [{'role': 'user', 'parts': [{'text': structure_prompt(candidate, raw_text, sources)}]}],
        'generationConfig': {'temperature': 0, 'responseMimeType': 'application/json', 'maxOutputTokens': 2048},
    }
    try:
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, {'code': f'gemini_structure_http_{resp.status_code}', 'status_code': resp.status_code, 'response_text': resp.text[:2000]}
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        return parse_json(text), None
    except Exception as exc:
        return None, {'code': 'gemini_structure_exception', 'response_text': str(exc)[:2000]}


def two_step_research(candidate):
    raw_text, sources, research_error = call_research_step(candidate)
    if research_error:
        return None, research_error
    structured, structure_error = call_structure_step(candidate, raw_text or '', sources)
    if structure_error:
        fallback = {
            'research_status': 'completed_unstructured',
            'source_quality': {'primary_source_count': 0, 'secondary_source_count': len(sources), 'echo_chamber_risk': 'medium'},
            'signals': {'hard': [], 'soft': [raw_text[:300]] if raw_text else [], 'contradictions': []},
            'confidence': 'low',
            'summary': 'Grounded research succeeded, but structure step failed.',
            'research_flags': ['structure_step_failed'],
        }
        fallback['raw_research_text'] = raw_text
        fallback['grounding_chunks'] = sources
        fallback['source_links'] = [s.get('uri') for s in sources[:3] if s.get('uri')]
        return fallback, structure_error
    structured['raw_research_text'] = raw_text
    structured['grounding_chunks'] = sources
    structured['source_links'] = [s.get('uri') for s in sources[:3] if s.get('uri')]
    return structured, None


def fake_output():
    return {'research_status': 'simulated', 'source_links': [], 'source_quality': {'primary_source_count': 0, 'secondary_source_count': 0, 'echo_chamber_risk': 'none'}, 'signals': {'hard': [], 'soft': [], 'contradictions': []}, 'confidence': 'low', 'summary': 'Simulated research record.', 'research_flags': ['simulated_research_record', 'not_real_research'], 'grounding_chunks': [], 'raw_research_text': ''}


def error_code(error):
    return error.get('code') if isinstance(error, dict) else error or 'research_unavailable'


def normalize(candidate, output, error=None):
    if output is None:
        output = {'research_status': 'failed', 'source_links': [], 'source_quality': {'primary_source_count': 0, 'secondary_source_count': 0, 'echo_chamber_risk': 'high'}, 'signals': {'hard': [], 'soft': [], 'contradictions': []}, 'confidence': 'low', 'summary': f'Research failed: {error_code(error)}', 'research_flags': [error_code(error)], 'grounding_chunks': [], 'raw_research_text': ''}
    sq = output.get('source_quality') if isinstance(output.get('source_quality'), dict) else {}
    sig = output.get('signals') if isinstance(output.get('signals'), dict) else {}
    return {
        'record_type': 'research_record',
        'research_id': stable_id('res', VERSION, candidate.get('market_id'), now_utc()),
        'research_version': VERSION,
        'created_at': now_utc(),
        'provider': 'simulation' if FAKE_WRITE else 'gemini_twostep',
        'research_model': RESEARCH_MODEL,
        'structure_model': STRUCTURE_MODEL,
        'market_id': candidate.get('market_id'),
        'event_id': candidate.get('event_id'),
        'event_name': candidate.get('event_name'),
        'selection': candidate.get('selection'),
        'odds': candidate.get('odds'),
        'trigger_reasons': candidate.get('trigger_reasons'),
        'priority_score': candidate.get('priority_score'),
        'research_status': output.get('research_status') or 'completed',
        'source_links': output.get('source_links') if isinstance(output.get('source_links'), list) else [],
        'source_quality': {
            'primary_source_count': int(sq.get('primary_source_count') or 0),
            'secondary_source_count': int(sq.get('secondary_source_count') or len(output.get('source_links') or [])),
            'echo_chamber_risk': sq.get('echo_chamber_risk') if sq.get('echo_chamber_risk') in {'none', 'low', 'medium', 'high'} else 'medium',
        },
        'signals': {
            'hard': sig.get('hard') if isinstance(sig.get('hard'), list) else [],
            'soft': sig.get('soft') if isinstance(sig.get('soft'), list) else [],
            'contradictions': sig.get('contradictions') if isinstance(sig.get('contradictions'), list) else [],
            'injuries': sig.get('hard') if isinstance(sig.get('hard'), list) else [],
            'lineups': [],
            'motivation': sig.get('soft') if isinstance(sig.get('soft'), list) else [],
            'form': [],
            'market_consensus': None,
        },
        'confidence': output.get('confidence') if output.get('confidence') in {'low', 'medium', 'high'} else 'low',
        'summary': str(output.get('summary') or '')[:1000],
        'research_flags': output.get('research_flags') if isinstance(output.get('research_flags'), list) else [],
        'error_detail': error if isinstance(error, dict) else None,
        'grounding_chunks': output.get('grounding_chunks') if isinstance(output.get('grounding_chunks'), list) else [],
        'raw_research_text': str(output.get('raw_research_text') or '')[:4000],
        'source_market_snapshot': candidate,
    }


def write_report(payload, records):
    lines = ['# Odds 2 — Phase 2.1 Research Report', '', f'Generated: {now_utc()}', f'- Research version: {VERSION}', f'- Research model: {RESEARCH_MODEL}', f'- Structure model: {STRUCTURE_MODEL}', f'- Research enabled: {ENABLED}', f'- Simulate research trigger: {FORCE_ONE}', f'- Simulate research write record: {FAKE_WRITE}', f'- Research candidates selected: {payload.get("candidate_count")}', f'- All triggered markets: {payload.get("all_triggered_count")}', f'- Research records written: {len(records)}', '']
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
            output, error = (fake_output(), None) if FAKE_WRITE else two_step_research(c)
            records.append(normalize(c, output, error))
        append_records(records)
    (OUT_LATEST / 'research_records.json').write_text(json.dumps({'generated_at': now_utc(), 'research_version': VERSION, 'records': records}, ensure_ascii=False, indent=2), encoding='utf-8')
    path = write_report(payload, records)
    print(f'Phase 2.1 two-step research OK | candidates={payload.get("candidate_count")} records={len(records)} report={path}')


if __name__ == '__main__':
    main()
