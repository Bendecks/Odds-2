import hashlib
import json
import os
import pathlib
import re
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
    'windrawwin', 'sports mole', 'free tips', 'prediction', 'predictions', 'expert picks',
    'best bet', 'betting tips', 'tipster', 'forebet', 'bettingexpert', 'footballwhispers'
]
TIER1_TERMS = [
    'premierinjuries', 'premier injuries', 'bbc sport', 'sky sports', 'the athletic', 'reuters',
    'ap news', 'official club', 'official league', 'bold.dk', 'tipsbladet', 'oddsportal',
    'betfair', 'pinnacle'
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


def norm_text(value):
    return re.sub(r'[^a-z0-9æøå]+', ' ', str(value or '').lower()).strip()


def match_key(m):
    return '|'.join([
        norm_text(m.get('home_team')),
        norm_text(m.get('away_team')),
        norm_text(m.get('date_display')),
        norm_text(m.get('time_display')),
    ])


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
            item['match_key'] = match_key(item)
            item['match_id'] = stable_id('match', item['match_key'])
            ov = overround(item)
            item['overround'] = round(ov, 4) if ov is not None else None
            if ov is None:
                item['audit_status'] = 'rejected'; item['audit_reason'] = 'invalid_odds'; rejected.append(item)
            elif not (MIN_OVERROUND <= ov <= MAX_OVERROUND):
                item['audit_status'] = 'rejected'; item['audit_reason'] = f'overround_outside_{MIN_OVERROUND}_{MAX_OVERROUND}'; rejected.append(item)
            else:
                item['audit_status'] = 'accepted'; item['audit_reason'] = 'overround_ok'; matches.append(item)
    return matches, rejected


def dedupe_matches(matches):
    kept = {}
    duplicates = []
    for m in matches:
        key = m.get('match_key') or match_key(m)
        if key not in kept:
            kept[key] = m
        else:
            duplicates.append({
                'match_key': key,
                'kept_match_id': kept[key].get('match_id'),
                'duplicate_match_id': m.get('match_id'),
                'match': f'{m.get("home_team")} vs {m.get("away_team")}',
                'kept_source_file': kept[key].get('source_file'),
                'duplicate_source_file': m.get('source_file'),
            })
    return list(kept.values()), duplicates


def source_policy_block():
    return {
        'title': 'STRICT SOURCE POLICY SOP-03',
        'tier_1_gold': ['Official club/league/competition websites', 'BBC Sport', 'Sky Sports', 'The Athletic', 'Reuters', 'AP', 'Premier Injuries', 'Bold.dk', 'Tipsbladet', 'Betfair Exchange', 'Pinnacle', 'Oddsportal'],
        'tier_2_silver': ['Guardian', 'ESPN', 'TV2 Sport', 'DR Sport', 'official club social media if verifiable', 'Flashscore', 'Oddschecker'],
        'tier_3_context_only': ['Transfermarkt, fan-led media and stats-only pages are context only. They cannot supply the required Tier 1 evidence.'],
        'prohibited_instant_pass': ['Sportskeeda', 'CaughtOffside', '90min', 'Stretty News', 'GoonersGuide', 'Sportsgambler', 'BeSoccer', 'FCTables', 'Footlive', 'FootyStats', 'APWin', 'ScoreStrike', 'WinDrawWin', 'Sports Mole', 'free tips', 'predictions', 'expert picks', 'best bets', 'affiliate betting previews'],
        'paper_bet_requirements': ['At least 2 evidence_items', 'At least 1 verified Tier 1 source by source_name or true domain', 'Every evidence_item must contain exactly one source_url', 'No comma-packed source_name/source_url', 'If evidence is conflicting/stale/vague/Tier 3 only: PASS']
    }


def compact_matches(valid_matches):
    return [{
        'match_id': m.get('match_id'), 'match': f'{m.get("home_team")} vs {m.get("away_team")}',
        'league': m.get('league'), 'date_display': m.get('date_display'), 'time_display': m.get('time_display'),
        'odds': {'1': m.get('odds_1'), 'X': m.get('odds_x'), '2': m.get('odds_2')}, 'overround': m.get('overround')
    } for m in valid_matches]


def decision_prompt(decision_matches, total_valid):
    return json.dumps({
        'analysis_version': 'simple_decision_v5_deduped_source_audit',
        'persona': 'Odds-2 Analyst: skeptical paper-only football value analyst. Default action is PASS.',
        'task': f'Analyze only the {len(decision_matches)} supplied unique matches out of {total_valid} valid unique matches. Use Google Search grounding. Return 0-{MAX_PICKS} paper-only picks. PASS when evidence is insufficient. Always return pass records for all analyzed matches not selected.',
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
            'analysis_version': 'simple_decision_v5_deduped_source_audit',
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
            'passes': [{'match_id': 'string', 'match': 'string', 'reason': 'insufficient edge|insufficient evidence|odds too low|conflicting signals|generic favorite only|source_policy_failed', 'short_note': 'max 220 chars'}]
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


def compact_response_debug(data, text):
    cand = (data.get('candidates') or [{}])[0]
    gm = cand.get('groundingMetadata') or cand.get('grounding_metadata') or {}
    return {
        'top_level_keys': list(data.keys()),
        'candidate_keys': list(cand.keys()),
        'grounding_metadata_keys': list(gm.keys()) if isinstance(gm, dict) else [],
        'text_preview': str(text or '')[:1000],
    }


def extract_grounding_sources(data):
    sources = []
    cand = (data.get('candidates') or [{}])[0]
    metadata = cand.get('groundingMetadata') or cand.get('grounding_metadata') or {}
    chunks = metadata.get('groundingChunks') or metadata.get('grounding_chunks') or []
    for i, chunk in enumerate(chunks):
        web = chunk.get('web') or {}
        uri, title = web.get('uri'), web.get('title')
        if uri or title:
            sources.append({'index': i, 'title': title, 'uri': uri, 'domain': domain_from_url(uri)})
    return sources


def call_decision(decision_matches, total_valid):
    if not decision_matches:
        return {'analysis_version': 'simple_decision_v5_deduped_source_audit', 'picks': [], 'passes': []}, None, [], {}
    url = gemini_url()
    if not url:
        return None, {'code': 'missing_gemini_api_key'}, [], {}
    body = {
        'contents': [{'role': 'user', 'parts': [{'text': decision_prompt(decision_matches, total_valid)}]}],
        'tools': [{'google_search': {}}],
        'generationConfig': {'temperature': 0, 'maxOutputTokens': 16384}
    }
    try:
        resp = requests.post(url, json=body, timeout=180)
        if resp.status_code >= 400:
            return None, {'code': f'gemini_decision_http_{resp.status_code}', 'response_text': resp.text[:2000]}, [], {}
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        debug = compact_response_debug(data, text)
        return extract_json(text), None, extract_grounding_sources(data), debug
    except Exception as exc:
        return None, {'code': 'gemini_decision_exception', 'response_text': str(exc)[:2000]}, [], {}


def source_text(item):
    return ' '.join(str(item.get(k) or '').lower() for k in ['source_name', 'source_url'])


def item_text(item):
    return ' '.join(str(item.get(k) or '').lower() for k in ['source_name', 'source_url', 'signal'])


def source_is_prohibited(item):
    haystack = source_text(item)
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
    domain = domain_from_url(item.get('source_url'))
    text = source_text(item)
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


def evidence_line(item):
    return f"{item.get('type')} | {item.get('source_name')} | verified={source_tier(item)} | declared={item.get('source_tier')} | {item.get('source_url')} | {item.get('signal')}"


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
            'created_at': now_utc(), 'mode': 'paper_only', 'analysis_version': 'simple_decision_v5_deduped_source_audit',
            'match_id': mid, 'match': f'{m.get("home_team")} vs {m.get("away_team")}', 'league': m.get('league'),
            'date_display': m.get('date_display'), 'time_display': m.get('time_display'),
            'selection': selection, 'selection_label': p.get('selection_label') if decision == 'PAPER_BET' else 'pass',
            'odds': odds, 'decision': decision, 'confidence_score': confidence, 'stake_units': stake,
            'value_case': str(p.get('value_case') or '')[:700], 'evidence_summary': str(p.get('evidence_summary') or '')[:700],
            'evidence_items': evidence_items, 'evidence_lines': [evidence_line(i) for i in evidence_items if isinstance(i, dict)],
            'verified_source_tiers': verified_tiers, 'source_quality': p.get('source_quality') if isinstance(p.get('source_quality'), dict) else {},
            'redirect_source_count': redirect_source_count, 'risk_flags': p.get('risk_flags') if isinstance(p.get('risk_flags'), list) else [],
            'why_not_pass': str(p.get('why_not_pass') or '')[:500], 'blocked_by_safety': block_reason,
            'short_reason': str(p.get('evidence_summary') or p.get('value_case') or '')[:500],
            'source_match': m, 'settlement': 'PENDING' if decision == 'PAPER_BET' else 'NOT_APPLICABLE'
        })
    return out


def normalize_passes(decision_payload, decision_matches, decision_records):
    by_id = {m['match_id']: m for m in decision_matches}
    paper_ids = {p.get('match_id') for p in decision_records if p.get('decision') == 'PAPER_BET'}
    out = []
    raw_passes = (decision_payload or {}).get('passes') or []
    seen = set()
    for p in raw_passes:
        mid = p.get('match_id')
        if mid not in by_id or mid in paper_ids or mid in seen:
            continue
        seen.add(mid)
        m = by_id[mid]
        out.append({'match_id': mid, 'match': p.get('match') or f'{m.get("home_team")} vs {m.get("away_team")}', 'reason': str(p.get('reason') or 'pass').strip()[:120], 'short_note': str(p.get('short_note') or '').strip()[:300], 'odds': {'1': m.get('odds_1'), 'X': m.get('odds_x'), '2': m.get('odds_2')}})
    for d in decision_records:
        mid = d.get('match_id')
        if d.get('decision') == 'PASS' and d.get('blocked_by_safety') and mid not in seen:
            seen.add(mid)
            out.append({'match_id': mid, 'match': d.get('match'), 'reason': f'blocked_by_safety:{d.get("blocked_by_safety")}', 'short_note': d.get('short_reason') or d.get('value_case') or '', 'odds': d.get('source_match', {})})
    for mid, m in by_id.items():
        if mid not in paper_ids and mid not in seen:
            out.append({'match_id': mid, 'match': f'{m.get("home_team")} vs {m.get("away_team")}', 'reason': 'no_pass_reason_returned', 'short_note': 'Gemini returned no explicit pass reason for this analyzed match.', 'odds': {'1': m.get('odds_1'), 'X': m.get('odds_x'), '2': m.get('odds_2')}})
    return out


def write_json(path, data):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def append_log(records):
    paper_records = [r for r in records if r.get('decision') == 'PAPER_BET']
    if not paper_records:
        return 0
    with PICKS_LOG.open('a', encoding='utf-8') as f:
        for r in paper_records:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    return len(paper_records)


def write_report(payload):
    lines = ['# Odds 2 — Simple Gemini Pipeline', '', f'Generated: {payload.get("generated_at")}', f'- Analysis version: simple_decision_v5_deduped_source_audit', f'- Files processed: {payload.get("files_processed")}', f'- Raw matches: {payload.get("raw_match_count")}', f'- Valid matches: {payload.get("valid_match_count")}', f'- Unique valid matches: {payload.get("unique_valid_match_count")}', f'- Duplicate matches removed: {payload.get("duplicate_match_count")}', f'- Decision matches: {payload.get("decision_match_count")}', f'- Rejected matches: {payload.get("rejected_match_count")}', f'- Gemini decision records: {payload.get("decision_record_count")}', f'- PAPER_BET logged: {payload.get("paper_bet_count")}', f'- Blocked decisions: {payload.get("blocked_decision_count")}', f'- Passes returned: {len(payload.get("passes") or [])}', f'- Decision error: `{payload.get("decision_error")}`', f'- Grounding sources: {len(payload.get("decision_grounding_sources") or [])}', '']
    paper_bets = [p for p in (payload.get('decisions') or []) if p.get('decision') == 'PAPER_BET']
    blocked = [p for p in (payload.get('decisions') or []) if p.get('blocked_by_safety')]
    if paper_bets:
        lines.append('## PAPER_BET')
        for p in paper_bets:
            lines += ['', f'### {p.get("match")}', f'- Selection: {p.get("selection")}', f'- Odds: {p.get("odds")}', f'- Stake units: {p.get("stake_units")}', f'- Confidence: {p.get("confidence_score")}', f'- Verified source tiers: `{p.get("verified_source_tiers")}`', f'- Value case: {p.get("value_case")}', f'- Evidence: {p.get("evidence_summary")}', '- Evidence sources:']
            for line in p.get('evidence_lines') or []:
                lines.append(f'  - {line}')
    else:
        lines.append('No PAPER_BET passed safety gates.')
    if blocked:
        lines += ['', '## Blocked Gemini suggestions']
        for p in blocked:
            lines += ['', f'### {p.get("match")}', f'- Suggested selection: {p.get("selection")}', f'- Blocked by safety: `{p.get("blocked_by_safety")}`', f'- Verified source tiers: `{p.get("verified_source_tiers")}`', f'- Redirect source count: {p.get("redirect_source_count")}', f'- Value case: {p.get("value_case")}', '- Evidence sources:']
            for line in p.get('evidence_lines') or []:
                lines.append(f'  - {line}')
    lines += ['', '## Pass reasons']
    for p in (payload.get('passes') or [])[:MAX_DECISION_MATCHES]:
        lines.append(f'- {p.get("match")}: {p.get("reason")} — {p.get("short_note") or ""}')
    lines += ['', '## Duplicate matches removed']
    for d in (payload.get('duplicate_matches') or [])[:25]:
        lines.append(f'- {d.get("match")}: kept {d.get("kept_source_file")}, removed {d.get("duplicate_source_file")}')
    lines += ['', '## Gemini grounding sources']
    sources = payload.get('decision_grounding_sources') or []
    if not sources:
        lines.append('No grounding sources returned or parsed.')
    for s in sources[:25]:
        lines.append(f'- {s.get("title") or "Untitled"} — {s.get("domain") or "unknown"} — {s.get("uri")}')
    lines += ['', '## Grounding debug']
    lines.append(f'`{json.dumps(payload.get("decision_response_debug") or {}, ensure_ascii=False)}`')
    path = OUT_REPORTS / 'simple_pipeline_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)


def main():
    files = list_pdfs()[:MAX_FILES]
    parsed_files = [parse_pdf(p) for p in files]
    parser_payload = {'generated_at': now_utc(), 'parser_source': 'gemini_pdf_vision', 'files_processed': len(files), 'files': parsed_files, 'summary': {'matches_total': sum(len(f.get('matches') or []) for f in parsed_files), 'files_with_errors': sum(1 for f in parsed_files if f.get('error'))}}
    valid, rejected = flatten_matches(parser_payload)
    unique_valid, duplicates = dedupe_matches(valid)
    decision_matches = unique_valid[:MAX_DECISION_MATCHES]
    decision_payload, decision_error, decision_grounding_sources, decision_response_debug = call_decision(decision_matches, len(unique_valid))
    decisions = normalize_picks(decision_payload, decision_matches) if decision_payload else []
    passes = normalize_passes(decision_payload, decision_matches, decisions) if decision_payload else []
    logged_count = append_log(decisions)
    paper_bets = [d for d in decisions if d.get('decision') == 'PAPER_BET']
    blocked = [d for d in decisions if d.get('blocked_by_safety')]
    output = {'generated_at': now_utc(), 'pipeline': 'gemini_simple_pipeline_v5_deduped_source_audit', 'files_processed': len(files), 'raw_match_count': parser_payload['summary']['matches_total'], 'valid_match_count': len(valid), 'unique_valid_match_count': len(unique_valid), 'duplicate_match_count': len(duplicates), 'decision_match_count': len(decision_matches), 'rejected_match_count': len(rejected), 'decision_error': decision_error, 'decision_record_count': len(decisions), 'paper_bet_count': len(paper_bets), 'blocked_decision_count': len(blocked), 'logged_count': logged_count, 'pick_count': len(paper_bets), 'pass_count': len(passes), 'decision_grounding_sources': decision_grounding_sources, 'decision_response_debug': decision_response_debug, 'duplicate_matches': duplicates, 'parser_payload': parser_payload, 'valid_matches': valid, 'unique_valid_matches': unique_valid, 'decision_matches': decision_matches, 'rejected_matches': rejected, 'decision_payload': decision_payload, 'decisions': decisions, 'picks': paper_bets, 'blocked_decisions': blocked, 'passes': passes}
    write_json(OUT_LATEST / 'simple_pipeline_output.json', output)
    report = write_report(output)
    print(f'Simple Gemini pipeline v5 OK | files={len(files)} raw={output["raw_match_count"]} valid={len(valid)} unique={len(unique_valid)} duplicates={len(duplicates)} decision_matches={len(decision_matches)} paper_bets={len(paper_bets)} blocked={len(blocked)} passes={len(passes)} grounding_sources={len(decision_grounding_sources)} report={report}')


if __name__ == '__main__':
    main()
