import hashlib
import json
import os
import pathlib
from datetime import datetime, timezone
from urllib.parse import urlparse

import requests

from gemini_pdf_parser import parse_pdf, list_pdfs

ROOT = pathlib.Path('.')
OUT_LATEST = ROOT / 'output' / 'latest'
OUT_REPORTS = ROOT / 'output' / 'reports'
DATA_DIR = ROOT / 'data'
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_REPORTS.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)

GEMINI_MODEL = os.getenv('GEMINI_DECISION_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
MAX_FILES = int(os.getenv('ODDS_MAX_FILES', '5'))
MAX_PICKS = int(os.getenv('SIMPLE_MAX_PICKS', '3'))
MAX_DECISION_MATCHES = int(os.getenv('SIMPLE_MAX_DECISION_MATCHES', '12'))
MIN_OVERROUND = float(os.getenv('SIMPLE_MIN_OVERROUND', '1.00'))
MAX_OVERROUND = float(os.getenv('SIMPLE_MAX_OVERROUND', '1.20'))
PICKS_LOG = DATA_DIR / 'simple_picks_log.jsonl'

PROHIBITED_SOURCE_TERMS = [
    'sportskeeda', 'caughtoffside', '90min', 'strettynews', 'stretty news', 'goonersguide',
    'sportsgambler', 'besoccer', 'fctables', 'footlive', 'footystats', 'apwin', 'scorestrike',
    'windrawwin', 'free tips', 'prediction', 'predictions', 'expert picks', 'best bet',
    'betting tips', 'tipster', 'forebet', 'bettingexpert', 'footballwhispers'
]
TIER1_TERMS = [
    'premierinjuries', 'bbc sport', 'sky sports', 'the athletic', 'reuters', 'ap news',
    'premier league', 'uefa', 'fifa', 'bold.dk', 'tipsbladet', 'superliga',
    'oddsportal', 'betfair', 'pinnacle'
]
TIER2_TERMS = [
    'espn', 'guardian', 'tv 2 sport', 'tv2 sport', 'dr sport', 'flashscore', 'oddschecker',
    'liverpoolfc', 'chelseafc', 'manutd', 'arsenal', 'aston villa'
]
TIER1_DOMAINS = ['premierinjuries.com', 'bbc.com', 'bbc.co.uk', 'skysports.com', 'theathletic.com', 'reuters.com', 'apnews.com', 'premierleague.com', 'uefa.com', 'fifa.com', 'bold.dk', 'tipsbladet.dk', 'superliga.dk', '3fsuperliga.dk', 'oddsportal.com', 'betfair.com', 'pinnacle.com']
TIER2_DOMAINS = ['espn.com', 'theguardian.com', 'tv2.dk', 'dr.dk', 'flashscore.com', 'oddschecker.com', 'liverpoolfc.com', 'chelseafc.com', 'manutd.com', 'arsenal.com', 'avfc.co.uk']


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def stable_id(prefix, *parts):
    raw = '|'.join(str(p or '').strip().lower() for p in parts)
    return f'{prefix}_{hashlib.sha256(raw.encode()).hexdigest()[:16]}'


def gemini_url():
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        return None
    return f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={key}'


def safe_float(value):
    try:
        return float(value)
    except Exception:
        return None


def overround(match):
    odds = [safe_float(match.get('odds_1')), safe_float(match.get('odds_x')), safe_float(match.get('odds_2'))]
    if any(o is None or o <= 1.0 or o > 50 for o in odds):
        return None
    return sum(1 / o for o in odds)


def flatten_matches(parser_payload):
    matches, rejected = [], []
    for file_obj in parser_payload.get('files') or []:
        source_file, file_id = file_obj.get('source_file'), file_obj.get('file_id')
        for m in file_obj.get('matches') or []:
            item = dict(m)
            item['source_file'] = source_file
            item['file_id'] = file_id
            item['match_id'] = stable_id('match', source_file, m.get('home_team'), m.get('away_team'), m.get('date_display'), m.get('time_display'))
            ov = overround(item)
            item['overround'] = round(ov, 4) if ov is not None else None
            if ov is None:
                item['audit_status'] = 'rejected'; item['audit_reason'] = 'invalid_odds'; rejected.append(item)
            elif not (MIN_OVERROUND <= ov <= MAX_OVERROUND):
                item['audit_status'] = 'rejected'; item['audit_reason'] = f'overround_outside_{MIN_OVERROUND}_{MAX_OVERROUND}'; rejected.append(item)
            else:
                item['audit_status'] = 'accepted'; item['audit_reason'] = 'overround_ok'; matches.append(item)
    return matches, rejected


def source_policy_block():
    return {
        'title': 'STRICT SOURCE POLICY SOP-02',
        'tier_1_gold': ['Official club/league/competition websites', 'BBC Sport', 'Sky Sports', 'The Athletic', 'Reuters', 'AP', 'Premier Injuries', 'Bold.dk', 'Tipsbladet', 'Betfair Exchange', 'Pinnacle', 'Oddsportal'],
        'tier_2_silver': ['Guardian', 'ESPN', 'TV2 Sport', 'DR Sport', 'official club social media if verifiable', 'Flashscore', 'Oddschecker'],
        'tier_3_context_only': ['Transfermarkt, fan-led media and stats-only pages are context only. They cannot supply the required Tier 1 evidence.'],
        'prohibited_instant_pass': ['Sportskeeda', 'CaughtOffside', '90min', 'Stretty News', 'GoonersGuide', 'Sportsgambler', 'BeSoccer', 'FCTables', 'Footlive', 'FootyStats', 'APWin', 'ScoreStrike', 'WinDrawWin', 'free tips', 'predictions', 'expert picks', 'best bets', 'affiliate betting previews'],
        'paper_bet_requirements': ['At least 2 evidence_items', 'At least 1 verified Tier 1 source by domain/name', 'Every evidence_item must contain exactly one source_url', 'No comma-packed source_name/source_url', 'If evidence is conflicting/stale/vague/Tier 3 only: PASS']
    }


def compact_matches(valid_matches):
    return [{
        'match_id': m.get('match_id'), 'match': f'{m.get("home_team")} vs {m.get("away_team")}',
        'league': m.get('league'), 'date_display': m.get('date_display'), 'time_display': m.get('time_display'),
        'odds': {'1': m.get('odds_1'), 'X': m.get('odds_x'), '2': m.get('odds_2')}, 'overround': m.get('overround')
    } for m in valid_matches]


def decision_prompt(decision_matches, total_valid):
    return json.dumps({
        'analysis_version': 'simple_decision_v4_verified_sources',
        'persona': 'Odds-2 Analyst: skeptical paper-only football value analyst. Default action is PASS.',
        'task': f'Analyze only the {len(decision_matches)} supplied matches out of {total_valid} valid matches. Use Google Search grounding. Return 0-{MAX_PICKS} paper-only picks. PASS when evidence is insufficient.',
        'source_policy': source_policy_block(),
        'hard_rules': [
            'Paper-only. Never imply real-money betting advice.',
            f'Max {MAX_PICKS} PAPER_BET picks total. Zero picks is acceptable.',
            'PAPER_BET requires at least 2 concrete evidence_items.',
            'PAPER_BET requires at least 1 verified Tier 1 evidence item. Do not self-label weak sources as Tier 1.',
            'Each evidence_item must cite exactly one source_name and exactly one source_url. Do not pack multiple sources into one field.',
            'Do not use prohibited sources as evidence. If only prohibited, stats-only, or Tier 3 sources exist, PASS.',
            'PAPER_BET requires a value_case explaining why the Bet365 odds may be wrong; generic favorite reasoning is not enough.',
            'Low odds under 1.50 require exceptional evidence. Draw picks require exceptional evidence.',
            'Stake units: PASS=0; weak edge=0.25; moderate=0.5; strong=0.75; max=1.0.',
            'Return strict JSON only. Do not use markdown fences.'
        ],
        'return_schema': {
            'analysis_version': 'simple_decision_v4_verified_sources',
            'picks': [{
                'match_id': 'string', 'match': 'string', 'selection': '1|X|2|PASS', 'selection_label': 'home|draw|away|pass',
                'odds': 0.0, 'decision': 'PAPER_BET|PASS', 'confidence_score': 0.0, 'stake_units': 0.0,
                'value_case': 'short explanation of why price may be wrong', 'evidence_summary': 'short summary',
                'evidence_items': [{
                    'type': 'injury|suspension|lineup|motivation|form|market_odds|context|other',
                    'signal': 'short factual signal', 'supports_selection': True, 'importance': 'low|medium|high',
                    'source_tier': 'tier1|tier2|tier3|prohibited|unknown', 'source_type': 'official|sports_media|odds_aggregator|fan_media|prohibited|unknown',
                    'source_name': 'single source only', 'source_url': 'single direct or Gemini grounding URL', 'published_or_checked_date': 'string if available'
                }],
                'source_quality': {'has_grounded_sources': True, 'tier1_source_count': 0, 'tier2_source_count': 0, 'tier3_source_count': 0, 'odds_sources': 0, 'prohibited_sources_used': False, 'all_evidence_has_urls': True},
                'risk_flags': ['low_confidence|insufficient_sources|possible_rotation|odds_too_short|market_not_verified|tier3_only|no_source_url'],
                'why_not_pass': 'why this is stronger than simply passing'
            }],
            'passes': [{'match_id': 'string', 'match': 'string', 'reason': 'insufficient edge|insufficient evidence|odds too low|conflicting signals|generic favorite only|source_policy_failed'}]
        },
        'validated_matches': compact_matches(decision_matches),
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


def domain_from_url(url):
    try:
        return urlparse(str(url)).netloc.lower().replace('www.', '')
    except Exception:
        return ''


def extract_grounding_sources(data):
    sources = []
    metadata = data.get('candidates', [{}])[0].get('groundingMetadata') or {}
    chunks = metadata.get('groundingChunks') or []
    for i, chunk in enumerate(chunks):
        web = chunk.get('web') or {}
        uri, title = web.get('uri'), web.get('title')
        if uri or title:
            sources.append({'index': i, 'title': title, 'uri': uri, 'domain': domain_from_url(uri)})
    return sources


def call_decision(decision_matches, total_valid):
    if not decision_matches:
        return {'analysis_version': 'simple_decision_v4_verified_sources', 'picks': [], 'passes': []}, None, []
    url = gemini_url()
    if not url:
        return None, {'code': 'missing_gemini_api_key'}, []
    body = {
        'contents': [{'role': 'user', 'parts': [{'text': decision_prompt(decision_matches, total_valid)}]}],
        'tools': [{'google_search': {}}],
        'generationConfig': {'temperature': 0, 'maxOutputTokens': 16384}
    }
    try:
        resp = requests.post(url, json=body, timeout=180)
        if resp.status_code >= 400:
            return None, {'code': f'gemini_decision_http_{resp.status_code}', 'response_text': resp.text[:2000]}, []
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        return extract_json(text), None, extract_grounding_sources(data)
    except Exception as exc:
        return None, {'code': 'gemini_decision_exception', 'response_text': str(exc)[:2000]}, []


def item_text(item):
    return ' '.join(str(item.get(k) or '').lower() for k in ['source_name', 'source_url', 'signal'])


def source_is_prohibited(item):
    haystack = item_text(item)
    return any(term in haystack for term in PROHIBITED_SOURCE_TERMS) or str(item.get('source_tier')).lower() == 'prohibited'


def source_has_single_url(item):
    url = str(item.get('source_url') or '').strip()
    if ',' in url or ' ' in url:
        return False
    return url.startswith('http://') or url.startswith('https://')


def source_has_single_name(item):
    name = str(item.get('source_name') or '').strip()
    return bool(name) and ',' not in name and ' and ' not in name.lower()


def source_is_redirect(item):
    return 'vertexaisearch.cloud.google.com' in str(item.get('source_url') or '').lower()


def source_tier(item):
    # Do not trust Gemini's self-declared tier. Classify from source_name and URL/domain.
    domain = domain_from_url(item.get('source_url'))
    text = item_text(item)
    if any(d in domain for d in TIER1_DOMAINS) or any(t in text for t in TIER1_TERMS):
        return 'tier1'
    if any(d in domain for d in TIER2_DOMAINS) or any(t in text for t in TIER2_TERMS):
        return 'tier2'
    if source_is_prohibited(item):
        return 'prohibited'
    return 'unknown'


def evidence_ok(p):
    items = p.get('evidence_items') if isinstance(p.get('evidence_items'), list) else []
    if len(items) < 2:
        return False, 'not_enough_evidence_items'
    for i in items:
        if not isinstance(i, dict):
            return False, 'invalid_evidence_item'
        if source_is_prohibited(i):
            return False, 'prohibited_source_used'
        if not source_has_single_url(i):
            return False, 'missing_or_packed_source_url'
        if not source_has_single_name(i):
            return False, 'missing_or_packed_source_name'
    tiers = [source_tier(i) for i in items]
    if 'tier1' not in tiers:
        return False, 'no_verified_tier1_source'
    if not any(str(i.get('importance')).lower() in {'medium', 'high'} for i in items):
        return False, 'no_medium_or_high_importance_evidence'
    sq = p.get('source_quality') if isinstance(p.get('source_quality'), dict) else {}
    if sq.get('prohibited_sources_used') is True or sq.get('affiliate_or_tip_sources_used') is True:
        return False, 'source_quality_prohibited_sources_used'
    if not sq.get('has_grounded_sources'):
        return False, 'no_grounded_sources'
    generic_text = f"{p.get('value_case') or ''} {p.get('evidence_summary') or ''} {p.get('why_not_pass') or ''}".lower()
    generic = ['strong form', 'better team', 'superior squad', 'home record', 'title-contending', 'inconsistent']
    if any(g in generic_text for g in generic) and len(items) < 3:
        return False, 'generic_reasoning_without_enough_evidence'
    return True, None


def normalize_picks(decision_payload, decision_matches):
    by_id = {m['match_id']: m for m in decision_matches}
    out, paper_count = [], 0
    for p in (decision_payload or {}).get('picks') or []:
        mid = p.get('match_id')
        if mid not in by_id:
            continue
        m = by_id[mid]
        decision = str(p.get('decision') or 'PASS').upper()
        selection = str(p.get('selection') or 'PASS').upper()
        block_reason = None
        if decision == 'PAPER_BET':
            ok, block_reason = evidence_ok(p)
            if not ok:
                decision, selection = 'PASS', 'PASS'
        if decision != 'PAPER_BET' or selection not in {'1', 'X', '2'}:
            decision, selection, stake, odds = 'PASS', 'PASS', 0.0, None
        else:
            paper_count += 1
            if paper_count > MAX_PICKS:
                decision, selection, stake, odds, block_reason = 'PASS', 'PASS', 0.0, None, 'max_picks_exceeded'
            else:
                stake = min(max(float(p.get('stake_units') or 0), 0.0), 1.0)
                odds = {'1': m.get('odds_1'), 'X': m.get('odds_x'), '2': m.get('odds_2')}[selection]
        try:
            confidence = min(max(float(p.get('confidence_score') or 0), 0.0), 1.0)
        except Exception:
            confidence = 0.0
        evidence_items = p.get('evidence_items') if isinstance(p.get('evidence_items'), list) else []
        redirect_source_count = sum(1 for i in evidence_items if isinstance(i, dict) and source_is_redirect(i))
        verified_tiers = [source_tier(i) for i in evidence_items if isinstance(i, dict)]
        out.append({
            'record_type': 'simple_pick', 'pick_id': stable_id('pick', mid, now_utc(), selection, odds),
            'created_at': now_utc(), 'mode': 'paper_only', 'analysis_version': 'simple_decision_v4_verified_sources',
            'match_id': mid, 'match': f'{m.get("home_team")} vs {m.get("away_team")}', 'league': m.get('league'),
            'date_display': m.get('date_display'), 'time_display': m.get('time_display'),
            'selection': selection, 'selection_label': p.get('selection_label') if decision == 'PAPER_BET' else 'pass',
            'odds': odds, 'decision': decision, 'confidence_score': confidence, 'stake_units': stake,
            'value_case': str(p.get('value_case') or '')[:700], 'evidence_summary': str(p.get('evidence_summary') or '')[:700],
            'evidence_items': evidence_items, 'verified_source_tiers': verified_tiers,
            'source_quality': p.get('source_quality') if isinstance(p.get('source_quality'), dict) else {},
            'redirect_source_count': redirect_source_count,
            'risk_flags': p.get('risk_flags') if isinstance(p.get('risk_flags'), list) else [],
            'why_not_pass': str(p.get('why_not_pass') or '')[:500], 'blocked_by_safety': block_reason,
            'short_reason': str(p.get('evidence_summary') or p.get('value_case') or '')[:500],
            'source_match': m, 'settlement': 'PENDING' if decision == 'PAPER_BET' else 'NOT_APPLICABLE'
        })
    return out


def write_json(path, data):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def append_log(records):
    if not records:
        return 0
    with PICKS_LOG.open('a', encoding='utf-8') as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    return len(records)


def write_report(payload):
    lines = ['# Odds 2 — Simple Gemini Pipeline', '', f'Generated: {payload.get("generated_at")}', f'- Analysis version: simple_decision_v4_verified_sources', f'- Files processed: {payload.get("files_processed")}', f'- Raw matches: {payload.get("raw_match_count")}', f'- Valid matches: {payload.get("valid_match_count")}', f'- Decision matches: {payload.get("decision_match_count")}', f'- Rejected matches: {payload.get("rejected_match_count")}', f'- Picks logged: {payload.get("pick_count")}', f'- Decision error: `{payload.get("decision_error")}`', f'- Grounding sources: {len(payload.get("decision_grounding_sources") or [])}', '']
    if payload.get('picks'):
        lines.append('## Picks / Decisions')
        for p in payload.get('picks'):
            lines += ['', f'### {p.get("match")}', f'- Decision: {p.get("decision")}', f'- Selection: {p.get("selection")}', f'- Odds: {p.get("odds")}', f'- Stake units: {p.get("stake_units")}', f'- Confidence: {p.get("confidence_score")}', f'- Blocked by safety: `{p.get("blocked_by_safety")}`', f'- Verified source tiers: `{p.get("verified_source_tiers")}`', f'- Redirect source count: {p.get("redirect_source_count")}', f'- Value case: {p.get("value_case")}', f'- Evidence: {p.get("evidence_summary")}', f'- Evidence items: `{json.dumps(p.get("evidence_items"), ensure_ascii=False)}`', f'- Source quality: `{json.dumps(p.get("source_quality"), ensure_ascii=False)}`', f'- Risk flags: `{p.get("risk_flags")}`', f'- Why not pass: {p.get("why_not_pass")}']
    else:
        lines.append('No picks returned.')
    lines += ['', '## Gemini grounding sources']
    for s in (payload.get('decision_grounding_sources') or [])[:25]:
        lines.append(f'- {s.get("title") or "Untitled"} — {s.get("domain") or "unknown"} — {s.get("uri")}')
    path = OUT_REPORTS / 'simple_pipeline_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)


def main():
    files = list_pdfs()[:MAX_FILES]
    parsed_files = [parse_pdf(p) for p in files]
    parser_payload = {'generated_at': now_utc(), 'parser_source': 'gemini_pdf_vision', 'files_processed': len(files), 'files': parsed_files, 'summary': {'matches_total': sum(len(f.get('matches') or []) for f in parsed_files), 'files_with_errors': sum(1 for f in parsed_files if f.get('error'))}}
    valid, rejected = flatten_matches(parser_payload)
    decision_matches = valid[:MAX_DECISION_MATCHES]
    decision_payload, decision_error, decision_grounding_sources = call_decision(decision_matches, len(valid))
    picks = normalize_picks(decision_payload, decision_matches) if decision_payload else []
    append_log(picks)
    output = {'generated_at': now_utc(), 'pipeline': 'gemini_simple_pipeline_v4_verified_sources', 'files_processed': len(files), 'raw_match_count': parser_payload['summary']['matches_total'], 'valid_match_count': len(valid), 'decision_match_count': len(decision_matches), 'rejected_match_count': len(rejected), 'decision_error': decision_error, 'pick_count': len(picks), 'decision_grounding_sources': decision_grounding_sources, 'parser_payload': parser_payload, 'valid_matches': valid, 'decision_matches': decision_matches, 'rejected_matches': rejected, 'decision_payload': decision_payload, 'picks': picks}
    write_json(OUT_LATEST / 'simple_pipeline_output.json', output)
    report = write_report(output)
    print(f'Simple Gemini pipeline v4 OK | files={len(files)} raw={output["raw_match_count"]} valid={len(valid)} decision_matches={len(decision_matches)} rejected={len(rejected)} picks={len(picks)} grounding_sources={len(decision_grounding_sources)} report={report}')


if __name__ == '__main__':
    main()
