import hashlib
import json
import os
import pathlib
import requests
from datetime import datetime, timezone

from tracker import read_tracker, append_records

MARKET_STATE_PATH = pathlib.Path('output/latest/market_state.json')
AI_DECISIONS_PATH = pathlib.Path('output/latest/ai_decisions.json')
OUT_LATEST = pathlib.Path('output/latest')
OUT_REPORTS = pathlib.Path('output/reports')
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_REPORTS.mkdir(parents=True, exist_ok=True)

GEMINI_MODEL = os.getenv('GEMINI_RESEARCH_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
MAX_RESEARCH_CALLS = int(os.getenv('MAX_RESEARCH_CALLS', '5'))
RESEARCH_VERSION = os.getenv('RESEARCH_VERSION', 'phase2_1_gemini_research_v1')
RESEARCH_ENABLED = os.getenv('RESEARCH_ENABLED', 'true').lower() == 'true'
SIMULATE_RESEARCH_TRIGGER = os.getenv('SIMULATE_RESEARCH_TRIGGER', 'false').lower() == 'true'
SIMULATE_RESEARCH_WRITE_RECORD = os.getenv('SIMULATE_RESEARCH_WRITE_RECORD', 'false').lower() == 'true'

PRIORITY_LEAGUES = {
    'Premier League', 'Superligaen', 'Bundesliga', 'Serie A', 'LaLiga', 'Ligue 1',
    'Champions League', 'Europa League'
}


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def stable_hash(prefix, *parts, length=16):
    raw = '|'.join(str(p or '').strip().lower() for p in parts)
    return f'{prefix}_{hashlib.sha256(raw.encode("utf-8")).hexdigest()[:length]}'


def load_json(path, default):
    path = pathlib.Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding='utf-8'))


def existing_research_keys(records):
    return {
        r.get('market_id')
        for r in records
        if r.get('record_type') == 'research_record'
        and r.get('research_version') == RESEARCH_VERSION
        and r.get('market_id')
    }


def latest_decisions_by_market():
    data = load_json(AI_DECISIONS_PATH, {'decisions': []})
    return {d.get('market_id'): d for d in data.get('decisions', []) if d.get('market_id')}


def trigger_reasons(market, decision):
    reasons = []
    ms = market.get('movement_summary') or {}
    change = float(ms.get('change_pct_from_first') or 0)
    league = (market.get('event') or {}).get('league')

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


def market_to_research_candidate(market, decision, reasons):
    event = market.get('event') or {}
    m = market.get('market') or {}
    ms = market.get('movement_summary') or {}
    priority_score = 0
    if 'significant_odds_change_10pct_plus' in reasons:
        priority_score += 100
    if 'small_odds_movement_3pct_plus' in reasons:
        priority_score += 40
    if 'ai_decision_watch' in reasons:
        priority_score += 35
    if event.get('league') in PRIORITY_LEAGUES:
        priority_score += 10
    if 'simulated_research_trigger' in reasons:
        priority_score += 1

    return {
        'market_id': market.get('market_id'),
        'event_id': market.get('event_id'),
        'event_name': f'{event.get("home")} vs {event.get("away")}',
        'home': event.get('home'),
        'away': event.get('away'),
        'league': event.get('league'),
        'sport': event.get('sport'),
        'event_time_utc': (market.get('event_time') or {}).get('utc'),
        'market_type': m.get('type'),
        'line': m.get('line'),
        'selection': m.get('selection'),
        'odds': m.get('odds'),
        'movement_summary': ms,
        'decision': decision,
        'trigger_reasons': reasons,
        'priority_score': priority_score,
    }


def eligible_market(market):
    if not market.get('active'):
        return False, 'inactive_market'
    pc = market.get('parser_confidence') or {}
    if not pc.get('real_bet_allowed'):
        return False, 'data_integrity_not_real_candidate'
    return True, 'eligible'


def select_research_candidates():
    state = load_json(MARKET_STATE_PATH, {'markets': []})
    records = read_tracker()
    existing = existing_research_keys(records)
    decisions = latest_decisions_by_market()
    candidates = []
    skipped = []
    eligible_without_trigger = []

    for market in state.get('markets') or []:
        mid = market.get('market_id')
        if not mid:
            continue
        if mid in existing:
            skipped.append({'market_id': mid, 'reason': 'research_exists_for_version'})
            continue
        ok, reason = eligible_market(market)
        if not ok:
            skipped.append({'market_id': mid, 'reason': reason})
            continue
        decision = decisions.get(mid)
        reasons = trigger_reasons(market, decision)
        if not reasons:
            eligible_without_trigger.append((market, decision))
            skipped.append({'market_id': mid, 'reason': 'no_research_trigger'})
            continue
        candidates.append(market_to_research_candidate(market, decision, reasons))

    if SIMULATE_RESEARCH_TRIGGER and not candidates and eligible_without_trigger:
        market, decision = eligible_without_trigger[0]
        candidates.append(market_to_research_candidate(market, decision, ['simulated_research_trigger']))

    candidates.sort(key=lambda c: (-c.get('priority_score', 0), c.get('event_time_utc') or '', c.get('event_name') or ''))
    selected = candidates[:MAX_RESEARCH_CALLS]
    payload = {
        'generated_at': utc_now(),
        'research_version': RESEARCH_VERSION,
        'max_research_calls': MAX_RESEARCH_CALLS,
        'simulate_research_trigger': SIMULATE_RESEARCH_TRIGGER,
        'simulate_research_write_record': SIMULATE_RESEARCH_WRITE_RECORD,
        'candidate_count': len(selected),
        'all_triggered_count': len(candidates),
        'skipped_count': len(skipped),
        'candidates': selected,
        'skipped': skipped[:250],
    }
    (OUT_LATEST / 'research_candidates.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    return payload


def research_prompt(candidate):
    return json.dumps({
        'role': 'paper_only_research_layer',
        'instruction': (
            'Research this football market for probability-changing information only. '
            'Do not recommend real betting. Do not invent facts. Use current web information if available. '
            'Prefer primary or near-primary sources: official club websites, official league sites, official competition sites, '
            'verified club announcements, reputable team-news sources, and established local/national sports media. '
            'Avoid betting-tip sites, odds-preview articles, affiliate betting pages, and articles whose main evidence is only odds movement. '
            'Do not double-count market movement as research evidence: if a source is only explaining odds movement, mark it as market_echo risk. '
            'Focus on concrete probability-changing signals: confirmed injuries, suspensions, likely lineups, goalkeeper changes, fixture congestion, '
            'motivation with table context, weather/pitch if relevant, and whether market consensus appears meaningfully different from the parsed odds. '
            'Return only a valid JSON object. Do not include markdown formatting or backticks.'
        ),
        'source_policy': {
            'preferred_sources': ['official_club', 'official_league', 'official_competition', 'reputable_sports_media', 'credible_local_media'],
            'discouraged_sources': ['betting_tips', 'affiliate_betting_pages', 'odds_only_previews', 'unsourced_social_media'],
            'echo_chamber_rule': 'Do not treat an article based only on odds movement as an independent research signal.'
        },
        'return_schema': {
            'research_status': 'completed|insufficient_data|failed',
            'source_links': ['url string'],
            'source_quality': {
                'primary_sources': ['url string'],
                'secondary_sources': ['url string'],
                'discarded_or_weak_sources': ['url string or description'],
                'echo_chamber_risk': 'none|low|medium|high'
            },
            'signals': {
                'injuries': ['short factual signal'],
                'lineups': ['short factual signal'],
                'motivation': ['short factual signal'],
                'form': ['short factual signal'],
                'market_consensus': 'short string or null',
                'contradictions': ['short factual contradiction']
            },
            'confidence': 'low|medium|high',
            'summary': 'short summary',
            'research_flags': ['string']
        },
        'candidate': candidate,
    }, ensure_ascii=False)


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


def call_gemini_research(candidate):
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        return None, {'code': 'missing_gemini_api_key'}
    request_features = {
        'google_search_enabled': True,
        'response_mime_type': None,
        'model': GEMINI_MODEL,
        'endpoint': 'v1beta/generateContent',
    }
    try:
        url = f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={api_key}'
        body = {
            'contents': [
                {'role': 'user', 'parts': [{'text': research_prompt(candidate)}]}
            ],
            'tools': [{'google_search': {}}],
            'generationConfig': {
                'temperature': 0
            }
        }
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, {
                'code': f'gemini_research_http_{resp.status_code}',
                'status_code': resp.status_code,
                'response_text': resp.text[:2000],
                'request_features': request_features,
            }
        data = resp.json()
        text = data['candidates'][0]['content']['parts'][0]['text']
        parsed = extract_json_object(text)
        grounding_chunks = []
        try:
            gm = data['candidates'][0].get('groundingMetadata') or {}
            for ch in gm.get('groundingChunks') or []:
                web = ch.get('web') or {}
                if web.get('uri'):
                    grounding_chunks.append({'uri': web.get('uri'), 'title': web.get('title')})
        except Exception:
            pass
        if grounding_chunks and not parsed.get('source_links'):
            parsed['source_links'] = [x['uri'] for x in grounding_chunks]
        parsed['grounding_chunks'] = grounding_chunks
        return parsed, None
    except Exception as exc:
        return None, {
            'code': 'gemini_research_exception',
            'response_text': str(exc)[:2000],
            'request_features': request_features,
        }


def simulated_research_output(candidate):
    return {
        'research_status': 'simulated',
        'source_links': [],
        'source_quality': {
            'primary_sources': [],
            'secondary_sources': [],
            'discarded_or_weak_sources': [],
            'echo_chamber_risk': 'none'
        },
        'signals': {
            'injuries': [],
            'lineups': [],
            'motivation': [],
            'form': [],
            'market_consensus': None,
            'contradictions': []
        },
        'confidence': 'low',
        'summary': 'Simulated research record. Used only to verify trigger, JSONL append and report plumbing.',
        'research_flags': ['simulated_research_record', 'not_real_research']
    }


def error_code(error):
    if isinstance(error, dict):
        return error.get('code') or 'research_error'
    return error or 'research_unavailable'


def normalize_research_output(candidate, output, error=None):
    now = utc_now()
    research_id = stable_hash('res', RESEARCH_VERSION, candidate.get('market_id'), now)
    if output is None:
        output = {
            'research_status': 'failed',
            'source_links': [],
            'source_quality': {
                'primary_sources': [],
                'secondary_sources': [],
                'discarded_or_weak_sources': [],
                'echo_chamber_risk': 'high'
            },
            'signals': {
                'injuries': [],
                'lineups': [],
                'motivation': [],
                'form': [],
                'market_consensus': None,
                'contradictions': []
            },
            'confidence': 'low',
            'summary': f'Research failed or unavailable: {error_code(error)}',
            'research_flags': [error_code(error)]
        }
    signals = output.get('signals') if isinstance(output.get('signals'), dict) else {}
    source_quality = output.get('source_quality') if isinstance(output.get('source_quality'), dict) else {}
    return {
        'record_type': 'research_record',
        'research_id': research_id,
        'research_version': RESEARCH_VERSION,
        'created_at': now,
        'provider': 'gemini' if not SIMULATE_RESEARCH_WRITE_RECORD else 'simulation',
        'model': GEMINI_MODEL if not SIMULATE_RESEARCH_WRITE_RECORD else 'simulated_research',
        'market_id': candidate.get('market_id'),
        'event_id': candidate.get('event_id'),
        'event_name': candidate.get('event_name'),
        'selection': candidate.get('selection'),
        'odds': candidate.get('odds'),
        'trigger_reasons': candidate.get('trigger_reasons') or [],
        'priority_score': candidate.get('priority_score'),
        'research_status': output.get('research_status') or 'completed',
        'source_links': output.get('source_links') if isinstance(output.get('source_links'), list) else [],
        'source_quality': {
            'primary_sources': source_quality.get('primary_sources') if isinstance(source_quality.get('primary_sources'), list) else [],
            'secondary_sources': source_quality.get('secondary_sources') if isinstance(source_quality.get('secondary_sources'), list) else [],
            'discarded_or_weak_sources': source_quality.get('discarded_or_weak_sources') if isinstance(source_quality.get('discarded_or_weak_sources'), list) else [],
            'echo_chamber_risk': source_quality.get('echo_chamber_risk') if source_quality.get('echo_chamber_risk') in {'none', 'low', 'medium', 'high'} else 'medium',
        },
        'signals': {
            'injuries': signals.get('injuries') if isinstance(signals.get('injuries'), list) else [],
            'lineups': signals.get('lineups') if isinstance(signals.get('lineups'), list) else [],
            'motivation': signals.get('motivation') if isinstance(signals.get('motivation'), list) else [],
            'form': signals.get('form') if isinstance(signals.get('form'), list) else [],
            'market_consensus': signals.get('market_consensus'),
            'contradictions': signals.get('contradictions') if isinstance(signals.get('contradictions'), list) else [],
        },
        'confidence': output.get('confidence') if output.get('confidence') in {'low', 'medium', 'high'} else 'low',
        'summary': str(output.get('summary') or '')[:1000],
        'research_flags': output.get('research_flags') if isinstance(output.get('research_flags'), list) else [],
        'error_detail': error if isinstance(error, dict) else {'code': error} if error else None,
        'grounding_chunks': output.get('grounding_chunks') if isinstance(output.get('grounding_chunks'), list) else [],
        'source_market_snapshot': candidate,
    }


def write_report(candidate_payload, records):
    lines = [
        '# Odds 2 — Phase 2.1 Research Report', '',
        f'Generated: {utc_now()}',
        f'- Research version: {RESEARCH_VERSION}',
        f'- Gemini model: {GEMINI_MODEL}',
        f'- Research enabled: {RESEARCH_ENABLED}',
        f'- Simulate research trigger: {SIMULATE_RESEARCH_TRIGGER}',
        f'- Simulate research write record: {SIMULATE_RESEARCH_WRITE_RECORD}',
        f'- Research candidates selected: {candidate_payload.get("candidate_count")}',
        f'- All triggered markets: {candidate_payload.get("all_triggered_count")}',
        f'- Research records written: {len(records)}', '',
    ]
    if not records:
        lines.append('No research records written. No markets met research triggers.')
    for r in records:
        sq = r.get('source_quality') or {}
        err = r.get('error_detail') or {}
        lines.extend([
            '',
            f'### {r.get("event_name")} — {r.get("selection")} @ {r.get("odds")}',
            f'- Status: {r.get("research_status")}',
            f'- Provider: {r.get("provider")}',
            f'- Confidence: {r.get("confidence")}',
            f'- Echo chamber risk: {sq.get("echo_chamber_risk")}',
            f'- Triggers: `{r.get("trigger_reasons")}`',
            f'- Summary: {r.get("summary")}',
            f'- Primary sources: `{sq.get("primary_sources")}`',
            f'- Secondary sources: `{sq.get("secondary_sources")}`',
            f'- Source links: `{r.get("source_links")}`',
            f'- Research flags: `{r.get("research_flags")}`',
            f'- Error code: `{err.get("code") if isinstance(err, dict) else None}`',
            f'- Error detail: `{(err.get("response_text") if isinstance(err, dict) else None)}`',
        ])
    path = OUT_REPORTS / 'research_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)


def main():
    payload = select_research_candidates()
    records = []
    if RESEARCH_ENABLED:
        for c in payload.get('candidates') or []:
            if SIMULATE_RESEARCH_WRITE_RECORD:
                output, error = simulated_research_output(c), None
            else:
                output, error = call_gemini_research(c)
            records.append(normalize_research_output(c, output, error=error))
        append_records(records)
    (OUT_LATEST / 'research_records.json').write_text(json.dumps({
        'generated_at': utc_now(),
        'research_version': RESEARCH_VERSION,
        'records': records,
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    report_path = write_report(payload, records)
    print(f'Phase 2.1 research OK | candidates={payload.get("candidate_count")} records={len(records)} report={report_path}')


if __name__ == '__main__':
    main()
