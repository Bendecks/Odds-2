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

MODEL = os.getenv('GEMINI_RESEARCH_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
VERSION = os.getenv('RESEARCH_VERSION', 'phase2_1_gemini_research_v2')
MAX_CALLS = int(os.getenv('MAX_RESEARCH_CALLS', '5'))
ENABLED = os.getenv('RESEARCH_ENABLED', 'true').lower() == 'true'
FORCE_ONE = os.getenv('SIMULATE_RESEARCH_TRIGGER', 'false').lower() == 'true'
FAKE_WRITE = os.getenv('SIMULATE_RESEARCH_WRITE_RECORD', 'false').lower() == 'true'
PRIORITY_LEAGUES = {'Premier League', 'Superligaen', 'Bundesliga', 'Serie A', 'LaLiga', 'Ligue 1', 'Champions League', 'Europa League'}


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def h(prefix, *parts):
    raw = '|'.join(str(p or '').lower().strip() for p in parts)
    return f'{prefix}_{hashlib.sha256(raw.encode()).hexdigest()[:16]}'


def load(path, default):
    path = pathlib.Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding='utf-8'))


def existing_research(records):
    return {r.get('market_id') for r in records if r.get('record_type') == 'research_record' and r.get('research_version') == VERSION and r.get('market_id')}


def decisions_by_market():
    return {d.get('market_id'): d for d in load(AI_DECISIONS_PATH, {'decisions': []}).get('decisions', []) if d.get('market_id')}


def reasons_for(market, decision):
    ms = market.get('movement_summary') or {}
    change = float(ms.get('change_pct_from_first') or 0)
    league = (market.get('event') or {}).get('league')
    reasons = []
    if change >= 0.10:
        reasons.append('significant_odds_change_10pct_plus')
    elif change >= 0.03:
        reasons.append('small_odds_movement_3pct_plus')
    if decision and decision.get('decision') == 'WATCH':
        reasons.append('ai_decision_watch')
    if league in PRIORITY_LEAGUES and change >= 0.03:
        reasons.append('priority_league_with_movement')
    if market.get('force_research') is True:
        reasons.append('manual_force_research')
    return reasons


def compact(market, decision, reasons):
    event = market.get('event') or {}
    m = market.get('market') or {}
    ms = market.get('movement_summary') or {}
    score = 1 if 'simulated_research_trigger' in reasons else 0
    if 'significant_odds_change_10pct_plus' in reasons: score += 100
    if 'small_odds_movement_3pct_plus' in reasons: score += 40
    if 'ai_decision_watch' in reasons: score += 35
    if event.get('league') in PRIORITY_LEAGUES: score += 10
    return {
        'market_id': market.get('market_id'), 'event_id': market.get('event_id'),
        'event_name': f'{event.get("home")} vs {event.get("away")}',
        'home': event.get('home'), 'away': event.get('away'), 'league': event.get('league'),
        'event_time_utc': (market.get('event_time') or {}).get('utc'),
        'market_type': m.get('type'), 'line': m.get('line'), 'selection': m.get('selection'), 'odds': m.get('odds'),
        'movement_summary': ms, 'decision': decision, 'trigger_reasons': reasons, 'priority_score': score,
    }


def select_candidates():
    state = load(MARKET_STATE_PATH, {'markets': []})
    records = read_tracker()
    existing = existing_research(records)
    decisions = decisions_by_market()
    candidates, skipped, eligible_without_trigger = [], [], []
    for market in state.get('markets', []):
        mid = market.get('market_id')
        if not mid: continue
        if mid in existing:
            skipped.append({'market_id': mid, 'reason': 'research_exists_for_version'}); continue
        if not market.get('active'):
            skipped.append({'market_id': mid, 'reason': 'inactive_market'}); continue
        pc = market.get('parser_confidence') or {}
        if not pc.get('real_bet_allowed'):
            skipped.append({'market_id': mid, 'reason': 'data_integrity_not_real_candidate'}); continue
        decision = decisions.get(mid)
        reasons = reasons_for(market, decision)
        if not reasons:
            eligible_without_trigger.append((market, decision)); skipped.append({'market_id': mid, 'reason': 'no_research_trigger'}); continue
        candidates.append(compact(market, decision, reasons))
    if FORCE_ONE and not candidates and eligible_without_trigger:
        market, decision = eligible_without_trigger[0]
        candidates.append(compact(market, decision, ['simulated_research_trigger']))
    candidates.sort(key=lambda x: (-x.get('priority_score', 0), x.get('event_time_utc') or ''))
    selected = candidates[:MAX_CALLS]
    payload = {'generated_at': now_utc(), 'research_version': VERSION, 'candidate_count': len(selected), 'all_triggered_count': len(candidates), 'skipped_count': len(skipped), 'simulate_research_trigger': FORCE_ONE, 'simulate_research_write_record': FAKE_WRITE, 'candidates': selected, 'skipped': skipped[:250]}
    (OUT_LATEST / 'research_candidates.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    return payload


def prompt(candidate):
    obj = {
        'task': 'Research this football market using web search. Return only compact JSON. No markdown.',
        'rules': ['probability-changing facts only', 'prefer official/reputable sources', 'avoid betting-tip/affiliate pages', 'do not treat odds movement as independent evidence', 'max 3 items per array'],
        'schema': {'research_status': 'completed|insufficient_data|failed', 'source_links': [], 'source_quality': {'primary_sources': [], 'secondary_sources': [], 'discarded_or_weak_sources': [], 'echo_chamber_risk': 'none|low|medium|high'}, 'signals': {'injuries': [], 'lineups': [], 'motivation': [], 'form': [], 'market_consensus': None, 'contradictions': []}, 'confidence': 'low|medium|high', 'summary': 'max 300 chars', 'research_flags': []},
        'candidate': candidate,
    }
    return json.dumps(obj, ensure_ascii=False)


def parse_json_text(text):
    raw = str(text or '').strip()
    if raw.startswith('```'):
        raw = raw.strip('`').replace('json\n', '', 1).replace('JSON\n', '', 1).strip()
    try:
        return json.loads(raw)
    except Exception:
        start, end = raw.find('{'), raw.rfind('}')
        if start >= 0 and end > start:
            return json.loads(raw[start:end+1])
        raise


def gemini_research(candidate):
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        return None, {'code': 'missing_gemini_api_key'}
    features = {'google_search_enabled': True, 'response_mime_type': None, 'model': MODEL, 'version': VERSION}
    url = f'https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={key}'
    body = {'contents': [{'role': 'user', 'parts': [{'text': prompt(candidate)}]}], 'tools': [{'google_search': {}}], 'generationConfig': {'temperature': 0, 'maxOutputTokens': 2048}}
    try:
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, {'code': f'gemini_research_http_{resp.status_code}', 'status_code': resp.status_code, 'response_text': resp.text[:2000], 'request_features': features}
        data = resp.json()
        text = data['candidates'][0]['content']['parts'][0].get('text', '')
        try:
            parsed = parse_json_text(text)
        except Exception as exc:
            return None, {'code': 'gemini_research_json_parse_error', 'parse_error': str(exc)[:500], 'response_text': text[:4000], 'request_features': features}
        chunks = []
        gm = data['candidates'][0].get('groundingMetadata') or {}
        for ch in gm.get('groundingChunks') or []:
            web = ch.get('web') or {}
            if web.get('uri'): chunks.append({'uri': web.get('uri'), 'title': web.get('title')})
        if chunks and not parsed.get('source_links'):
            parsed['source_links'] = [x['uri'] for x in chunks]
        parsed['grounding_chunks'] = chunks
        return parsed, None
    except Exception as exc:
        return None, {'code': 'gemini_research_exception', 'response_text': str(exc)[:2000], 'request_features': features}


def fake_output():
    return {'research_status': 'simulated', 'source_links': [], 'source_quality': {'primary_sources': [], 'secondary_sources': [], 'discarded_or_weak_sources': [], 'echo_chamber_risk': 'none'}, 'signals': {'injuries': [], 'lineups': [], 'motivation': [], 'form': [], 'market_consensus': None, 'contradictions': []}, 'confidence': 'low', 'summary': 'Simulated research record. Used only to verify plumbing.', 'research_flags': ['simulated_research_record', 'not_real_research']}


def code(error):
    return error.get('code') if isinstance(error, dict) else error or 'research_unavailable'


def normalize(candidate, output, error=None):
    if output is None:
        output = {'research_status': 'failed', 'source_links': [], 'source_quality': {'primary_sources': [], 'secondary_sources': [], 'discarded_or_weak_sources': [], 'echo_chamber_risk': 'high'}, 'signals': {'injuries': [], 'lineups': [], 'motivation': [], 'form': [], 'market_consensus': None, 'contradictions': []}, 'confidence': 'low', 'summary': f'Research failed or unavailable: {code(error)}', 'research_flags': [code(error)]}
    sq = output.get('source_quality') if isinstance(output.get('source_quality'), dict) else {}
    sig = output.get('signals') if isinstance(output.get('signals'), dict) else {}
    return {'record_type': 'research_record', 'research_id': h('res', VERSION, candidate.get('market_id'), now_utc()), 'research_version': VERSION, 'created_at': now_utc(), 'provider': 'simulation' if FAKE_WRITE else 'gemini', 'model': 'simulated_research' if FAKE_WRITE else MODEL, 'market_id': candidate.get('market_id'), 'event_id': candidate.get('event_id'), 'event_name': candidate.get('event_name'), 'selection': candidate.get('selection'), 'odds': candidate.get('odds'), 'trigger_reasons': candidate.get('trigger_reasons'), 'priority_score': candidate.get('priority_score'), 'research_status': output.get('research_status') or 'completed', 'source_links': output.get('source_links') if isinstance(output.get('source_links'), list) else [], 'source_quality': {'primary_sources': sq.get('primary_sources') if isinstance(sq.get('primary_sources'), list) else [], 'secondary_sources': sq.get('secondary_sources') if isinstance(sq.get('secondary_sources'), list) else [], 'discarded_or_weak_sources': sq.get('discarded_or_weak_sources') if isinstance(sq.get('discarded_or_weak_sources'), list) else [], 'echo_chamber_risk': sq.get('echo_chamber_risk') if sq.get('echo_chamber_risk') in {'none','low','medium','high'} else 'medium'}, 'signals': {'injuries': sig.get('injuries') if isinstance(sig.get('injuries'), list) else [], 'lineups': sig.get('lineups') if isinstance(sig.get('lineups'), list) else [], 'motivation': sig.get('motivation') if isinstance(sig.get('motivation'), list) else [], 'form': sig.get('form') if isinstance(sig.get('form'), list) else [], 'market_consensus': sig.get('market_consensus'), 'contradictions': sig.get('contradictions') if isinstance(sig.get('contradictions'), list) else []}, 'confidence': output.get('confidence') if output.get('confidence') in {'low','medium','high'} else 'low', 'summary': str(output.get('summary') or '')[:1000], 'research_flags': output.get('research_flags') if isinstance(output.get('research_flags'), list) else [], 'error_detail': error if isinstance(error, dict) else None, 'grounding_chunks': output.get('grounding_chunks') if isinstance(output.get('grounding_chunks'), list) else [], 'source_market_snapshot': candidate}


def report(payload, records):
    lines = ['# Odds 2 — Phase 2.1 Research Report', '', f'Generated: {now_utc()}', f'- Research version: {VERSION}', f'- Gemini model: {MODEL}', f'- Research enabled: {ENABLED}', f'- Simulate research trigger: {FORCE_ONE}', f'- Simulate research write record: {FAKE_WRITE}', f'- Research candidates selected: {payload.get("candidate_count")}', f'- All triggered markets: {payload.get("all_triggered_count")}', f'- Research records written: {len(records)}', '']
    if not records: lines.append('No research records written. No markets met research triggers.')
    for r in records:
        sq, err = r.get('source_quality') or {}, r.get('error_detail') or {}
        lines += ['', f'### {r.get("event_name")} — {r.get("selection")} @ {r.get("odds")}', f'- Status: {r.get("research_status")}', f'- Provider: {r.get("provider")}', f'- Confidence: {r.get("confidence")}', f'- Echo chamber risk: {sq.get("echo_chamber_risk")}', f'- Triggers: `{r.get("trigger_reasons")}`', f'- Summary: {r.get("summary")}', f'- Primary sources: `{sq.get("primary_sources")}`', f'- Secondary sources: `{sq.get("secondary_sources")}`', f'- Source links: `{r.get("source_links")}`', f'- Research flags: `{r.get("research_flags")}`', f'- Error code: `{err.get("code") if isinstance(err, dict) else None}`', f'- Error detail: `{err.get("response_text") if isinstance(err, dict) else None}`']
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
    path = report(payload, records)
    print(f'Phase 2.1 research OK | candidates={payload.get("candidate_count")} records={len(records)} report={path}')


if __name__ == '__main__':
    main()
