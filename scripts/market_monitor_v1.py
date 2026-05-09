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
PARSER_AUDIT_PATH = OUT_LATEST / 'parser_audit.json'
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_REPORTS.mkdir(parents=True, exist_ok=True)

MONITOR_VERSION = os.getenv('MARKET_MONITOR_VERSION', 'market_monitor_v1_consensus')
GEMINI_MODEL = os.getenv('GEMINI_MARKET_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
STRUCTURE_MODEL = os.getenv('GEMINI_MARKET_STRUCTURE_MODEL', os.getenv('GEMINI_MARKET_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash')))
MAX_CALLS = int(os.getenv('MAX_MARKET_MONITOR_CALLS', '5'))
MONITOR_ENABLED = os.getenv('MARKET_MONITOR_ENABLED', 'true').lower() == 'true'
CONSENSUS_REFRESH_HOURS = float(os.getenv('CONSENSUS_REFRESH_HOURS', '2'))
MONITOR_WINDOW_HOURS = float(os.getenv('MARKET_MONITOR_WINDOW_HOURS', '87600'))
OUTLIER_THRESHOLD = float(os.getenv('MARKET_OUTLIER_THRESHOLD', '0.05'))

BLOCKED_SOURCE_WORDS = ['prediction', 'predictions', 'tips', 'free tips', 'best bet', 'bettingexpert', 'forebet', 'sportsmole']
PREFERRED_SOURCE_WORDS = ['oddsportal', 'flashscore', 'oddschecker', 'betfair', 'pinnacle', 'unibet', 'bet365']


def now_dt():
    return datetime.now(timezone.utc)


def now_utc():
    return now_dt().replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def parse_utc(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace('Z', '+00:00'))
    except Exception:
        return None


def hours_until(value):
    dt = parse_utc(value)
    if not dt:
        return None
    return (dt - now_dt()).total_seconds() / 3600


def stable_id(prefix, *parts):
    raw = '|'.join(str(p or '').strip().lower() for p in parts)
    return f'{prefix}_{hashlib.sha256(raw.encode()).hexdigest()[:16]}'


def load_json(path, default):
    p = pathlib.Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding='utf-8'))


def audit_flagged_market_ids():
    data = load_json(PARSER_AUDIT_PATH, {})
    return set(data.get('flagged_market_ids') or [])


def latest_consensus_by_market(records):
    latest = {}
    for r in records:
        if r.get('record_type') != 'market_consensus_record':
            continue
        if r.get('monitor_version') != MONITOR_VERSION:
            continue
        mid = r.get('market_id')
        if not mid:
            continue
        if mid not in latest or (r.get('created_at') or '') > (latest[mid].get('created_at') or ''):
            latest[mid] = r
    return latest


def recent(record):
    if not record:
        return False
    created = parse_utc(record.get('created_at'))
    if not created:
        return False
    return (now_dt() - created).total_seconds() / 3600 < CONSENSUS_REFRESH_HOURS


def real_candidate(market):
    return bool(market.get('active') and (market.get('parser_confidence') or {}).get('real_bet_allowed'))


def event_time_utc(market):
    return (market.get('event_time') or {}).get('utc')


def compact_market(market, reason):
    event = market.get('event') or {}
    m = market.get('market') or {}
    h = hours_until(event_time_utc(market))
    return {
        'market_id': market.get('market_id'),
        'event_id': market.get('event_id'),
        'event_name': f'{event.get("home")} vs {event.get("away")}',
        'home': event.get('home'),
        'away': event.get('away'),
        'league': event.get('league'),
        'event_time_utc': event_time_utc(market),
        'hours_until_event': h,
        'market_type': m.get('type'),
        'line': m.get('line'),
        'selection': m.get('selection'),
        'bet365_odds': m.get('odds'),
        'monitor_reason': reason,
        'priority_score': 100 - (h or 100),
    }


def select_markets():
    state = load_json(MARKET_STATE_PATH, {'markets': []})
    latest = latest_consensus_by_market(read_tracker())
    flagged_ids = audit_flagged_market_ids()
    candidates, skipped = [], []
    for market in state.get('markets', []):
        mid = market.get('market_id')
        if not mid:
            continue
        if mid in flagged_ids:
            skipped.append({'market_id': mid, 'reason': 'parser_audit_flagged_market'}); continue
        if not real_candidate(market):
            skipped.append({'market_id': mid, 'reason': 'data_integrity_not_real_candidate'}); continue
        h = hours_until(event_time_utc(market))
        if h is None:
            skipped.append({'market_id': mid, 'reason': 'missing_event_time'}); continue
        if h <= 0:
            skipped.append({'market_id': mid, 'reason': 'event_expired'}); continue
        if h > MONITOR_WINDOW_HOURS:
            skipped.append({'market_id': mid, 'reason': 'outside_monitor_window'}); continue
        previous = latest.get(mid)
        if recent(previous):
            skipped.append({'market_id': mid, 'reason': 'recent_consensus_exists'}); continue
        reason = 'fresh_consensus_check' if not previous else 'consensus_refresh_due'
        candidates.append(compact_market(market, reason))
    candidates.sort(key=lambda c: (c.get('hours_until_event') if c.get('hours_until_event') is not None else 999, str(c.get('event_name'))))
    selected = candidates[:MAX_CALLS]
    reason_counts = {}
    for s in skipped:
        reason_counts[s['reason']] = reason_counts.get(s['reason'], 0) + 1
    payload = {'generated_at': now_utc(), 'monitor_version': MONITOR_VERSION, 'monitor_window_hours': MONITOR_WINDOW_HOURS, 'refresh_hours': CONSENSUS_REFRESH_HOURS, 'parser_audit_flagged_market_count': len(flagged_ids), 'candidate_count': len(selected), 'all_triggered_count': len(candidates), 'skipped_count': len(skipped), 'skip_reason_counts': reason_counts, 'candidates': selected, 'skipped': skipped[:250]}
    (OUT_LATEST / 'market_monitor_candidates.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
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


def monitor_prompt(c):
    return f'''Use Google Search grounding. Find current decimal 1X2 odds or odds range for this football market.
Match: {c.get('event_name')}
Selection to compare: {c.get('selection')}
Bet365 parsed odds: {c.get('bet365_odds')}
Event UTC: {c.get('event_time_utc')}
League: {c.get('league')}

Look for raw odds tables or aggregator pages first: Oddsportal, Flashscore, Oddschecker, Betfair/Pinnacle/major bookmakers if visible.
Do not use prediction/tip/affiliate pages as odds sources.
Do not recommend bets. Do not output JSON. Do not output URLs.
Return compact bullets with bookmaker/source name and decimal odds if found. If current odds are not found, say insufficient data.'''


def structure_prompt(c, raw_text, sources):
    compact_sources = [{'title': s.get('title'), 'uri': s.get('uri')} for s in sources[:8]]
    payload = {
        'task': 'Extract current market consensus data from grounded odds search text. Return JSON only.',
        'candidate': c,
        'raw_text': raw_text[:3000],
        'source_metadata': compact_sources,
        'rules': [
            'Only use odds explicitly present in raw_text.',
            'Do not invent bookmaker odds.',
            'Ignore prediction/tip/affiliate pages as odds sources.',
            'If less than 2 usable sources/odds, set consensus_status to insufficient_data.',
            'Use decimal odds only.'
        ],
        'schema': {
            'consensus_status': 'completed|insufficient_data|failed',
            'selection': c.get('selection'),
            'odds_points': [{'source_name': 'string', 'source_type': 'aggregator|bookmaker|exchange|unknown', 'decimal_odds': 0.0}],
            'market_avg_odds': 0.0,
            'min_odds': 0.0,
            'max_odds': 0.0,
            'source_count': 0,
            'confidence': 'low|medium|high',
            'market_direction': 'unknown|steaming|drifting|stable',
            'flags': [],
            'summary': 'max 250 chars'
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


def call_grounded(c):
    url = gemini_url(GEMINI_MODEL)
    if not url:
        return None, [], {'code': 'missing_gemini_api_key'}
    body = {'contents': [{'role': 'user', 'parts': [{'text': monitor_prompt(c)}]}], 'tools': [{'google_search': {}}], 'generationConfig': {'temperature': 0, 'maxOutputTokens': 1024}}
    try:
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, [], {'code': f'gemini_monitor_http_{resp.status_code}', 'response_text': resp.text[:2000]}
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        return text, extract_grounding(data), None
    except Exception as exc:
        return None, [], {'code': 'gemini_monitor_exception', 'response_text': str(exc)[:2000]}


def call_structure(c, raw_text, sources):
    url = gemini_url(STRUCTURE_MODEL)
    if not url:
        return None, {'code': 'missing_gemini_api_key'}
    body = {'contents': [{'role': 'user', 'parts': [{'text': structure_prompt(c, raw_text or '', sources)}]}], 'generationConfig': {'temperature': 0, 'responseMimeType': 'application/json', 'maxOutputTokens': 2048}}
    try:
        resp = requests.post(url, json=body, timeout=90)
        if resp.status_code >= 400:
            return None, {'code': f'gemini_monitor_structure_http_{resp.status_code}', 'response_text': resp.text[:2000]}
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        return parse_json(text), None
    except Exception as exc:
        return None, {'code': 'gemini_monitor_structure_exception', 'response_text': str(exc)[:2000]}


def source_is_blocked(source):
    title = str(source.get('title') or '').lower()
    uri = str(source.get('uri') or '').lower()
    joined = title + ' ' + uri
    return any(w in joined for w in BLOCKED_SOURCE_WORDS)


def source_is_preferred(source):
    title = str(source.get('title') or '').lower()
    uri = str(source.get('uri') or '').lower()
    joined = title + ' ' + uri
    return any(w in joined for w in PREFERRED_SOURCE_WORDS)


def compute_record(c, structured, raw_text, sources, error=None):
    if structured is None:
        structured = {'consensus_status': 'failed', 'odds_points': [], 'market_avg_odds': None, 'min_odds': None, 'max_odds': None, 'source_count': 0, 'confidence': 'low', 'market_direction': 'unknown', 'flags': [error.get('code') if isinstance(error, dict) else 'monitor_failed'], 'summary': 'Market monitor failed.'}
    points = structured.get('odds_points') if isinstance(structured.get('odds_points'), list) else []
    clean_odds = []
    for p in points:
        try:
            odd = float(p.get('decimal_odds'))
        except Exception:
            continue
        if 1.01 <= odd <= 50.0:
            clean_odds.append(odd)
    if clean_odds:
        avg = sum(clean_odds) / len(clean_odds)
        mn, mx = min(clean_odds), max(clean_odds)
    else:
        avg = structured.get('market_avg_odds') or None
        mn = structured.get('min_odds') or None
        mx = structured.get('max_odds') or None
    bet365 = c.get('bet365_odds')
    edge_hint = None
    outlier = False
    try:
        if avg and bet365:
            edge_hint = (float(bet365) - float(avg)) / float(avg)
            outlier = edge_hint >= OUTLIER_THRESHOLD
    except Exception:
        edge_hint = None
        outlier = False
    preferred = [s for s in sources if source_is_preferred(s)]
    blocked = [s for s in sources if source_is_blocked(s)]
    flags = structured.get('flags') if isinstance(structured.get('flags'), list) else []
    if blocked:
        flags.append('blocked_or_low_quality_sources_seen')
    if not preferred:
        flags.append('no_preferred_odds_source_seen')
    return {
        'record_type': 'market_consensus_record',
        'consensus_id': stable_id('cons', MONITOR_VERSION, c.get('market_id'), now_utc()),
        'monitor_version': MONITOR_VERSION,
        'created_at': now_utc(),
        'provider': 'gemini_search_twostep',
        'market_id': c.get('market_id'),
        'event_id': c.get('event_id'),
        'event_name': c.get('event_name'),
        'selection': c.get('selection'),
        'event_time_utc': c.get('event_time_utc'),
        'base_odds_bet365': bet365,
        'consensus_status': structured.get('consensus_status') or 'insufficient_data',
        'consensus': {'market_avg_odds': avg, 'min_odds': mn, 'max_odds': mx, 'source_count': int(structured.get('source_count') or len(clean_odds)), 'odds_points': points[:10]},
        'signals': {'is_bet365_outlier': outlier, 'outlier_pct': edge_hint, 'market_direction': structured.get('market_direction') or 'unknown'},
        'confidence': structured.get('confidence') if structured.get('confidence') in {'low', 'medium', 'high'} else 'low',
        'source_quality': {'preferred_source_count': len(preferred), 'blocked_source_count': len(blocked), 'total_grounding_sources': len(sources)},
        'source_links': [s.get('uri') for s in sources[:5] if s.get('uri')],
        'grounding_chunks': sources,
        'flags': list(dict.fromkeys(flags)),
        'summary': str(structured.get('summary') or '')[:1000],
        'raw_monitor_text': str(raw_text or '')[:4000],
        'error_detail': error if isinstance(error, dict) else None,
        'source_market_snapshot': c,
    }


def monitor_one(c):
    raw_text, sources, err = call_grounded(c)
    if err:
        return compute_record(c, None, raw_text, sources, err)
    structured, err2 = call_structure(c, raw_text, sources)
    return compute_record(c, structured, raw_text, sources, err2)


def write_report(payload, records):
    lines = ['# Odds 2 — Market Monitor V1 Report', '', f'Generated: {now_utc()}', f'- Monitor version: {MONITOR_VERSION}', f'- Gemini model: {GEMINI_MODEL}', f'- Structure model: {STRUCTURE_MODEL}', f'- Enabled: {MONITOR_ENABLED}', f'- Candidates selected: {payload.get("candidate_count")}', f'- All triggered markets: {payload.get("all_triggered_count")}', f'- Records written: {len(records)}', f'- Skip reason counts: `{json.dumps(payload.get("skip_reason_counts", {}), ensure_ascii=False)}`', f'- Parser-audit flagged markets: {payload.get("parser_audit_flagged_market_count")}', '']
    if not records:
        lines.append('No market consensus records written.')
    for r in records:
        cons = r.get('consensus') or {}
        sig = r.get('signals') or {}
        sq = r.get('source_quality') or {}
        lines += ['', f'### {r.get("event_name")} — {r.get("selection")} @ Bet365 {r.get("base_odds_bet365")}', f'- Status: {r.get("consensus_status")}', f'- Confidence: {r.get("confidence")}', f'- Market avg: {cons.get("market_avg_odds")}', f'- Min/max: {cons.get("min_odds")} / {cons.get("max_odds")}', f'- Source count: {cons.get("source_count")}', f'- Bet365 outlier: {sig.get("is_bet365_outlier")} ({sig.get("outlier_pct")})', f'- Direction: {sig.get("market_direction")}', f'- Preferred sources: {sq.get("preferred_source_count")}', f'- Flags: `{r.get("flags")}`', f'- Summary: {r.get("summary")}', f'- Source links: `{r.get("source_links")}`']
    path = OUT_REPORTS / 'market_monitor_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)


def main():
    payload = select_markets()
    records = []
    if MONITOR_ENABLED:
        for c in payload.get('candidates', []):
            records.append(monitor_one(c))
        append_records(records)
    (OUT_LATEST / 'market_consensus_records.json').write_text(json.dumps({'generated_at': now_utc(), 'monitor_version': MONITOR_VERSION, 'records': records}, ensure_ascii=False, indent=2), encoding='utf-8')
    path = write_report(payload, records)
    print(f'Market monitor v1 OK | candidates={payload.get("candidate_count")} records={len(records)} report={path}')


if __name__ == '__main__':
    main()
