import json
import pathlib
import re
from normalize_time import normalize_event_time
from canonical_matcher import match_team, add_alias_suggestion
from parser_confidence import calculate_parser_confidence
from ids import event_id, market_id, observation_id

DECIMAL_ODDS_RE = re.compile(r'^\d{1,2}[\.,]\d{2}$')
TIME_ONLY_RE = re.compile(r'^\d{1,2}:\d{2}$')
TIME_WITH_COUNT_RE = re.compile(r'^(\d{1,2}:\d{2})\d+$')
TIME_WITH_DAY_RE = re.compile(r'^(Man|Tir|Ons|Tor|Fre|Lør|Søn)\s+\d{1,2}:\d{2}$', re.I)
DATE_HEADER_RE = re.compile(r'^(Man|Tir|Ons|Tor|Fre|Lør|Søn)\s+\d{1,2}\s+[A-Za-zÆØÅæøå]+$', re.I)
ODDS_TRIPLE_RE = re.compile(r'^(\d{1,2}[\.,]\d{2})\s+(\d{1,2}[\.,]\d{2})\s+(\d{1,2}[\.,]\d{2})$')
KNOWN_LAYOUTS_PATH = pathlib.Path('data/known_layouts.json')

NOISE_EXACT = {
    'bet365', 'bet', '365', 'ÅBN', 'Ansvarsfuldt spil', 'Sport', 'Live', 'Casino', 'Væddemål',
    'Hjem Sport Live Væddemål Casino', 'Information og forsinkelser i udsendelsen', 'Indstillinger',
    'Tilbud', 'Åbningstilbud', 'Lyd', 'Statistik', 'Resultater', 'Livescore Resultater', 'Hjælp',
    'Indbetalinger Udbetalinger', 'Fodbold', 'Bedste ligaer', 'KOMMENDE KAMPE Se alle'
}
BAD_PREFIXES = ('© ', 'Ved at besøge', 'Denne side er beskyttet', 'StopSpillet', 'Du kan ', 'bet365 er ', 'Server Tid', 'Session ')


def load_known_layout_hashes():
    if not KNOWN_LAYOUTS_PATH.exists():
        return set()
    try:
        data = json.loads(KNOWN_LAYOUTS_PATH.read_text(encoding='utf-8'))
    except Exception:
        return set()
    hashes = set()
    for layout in data.get('layouts') or []:
        for h in layout.get('layout_hashes') or []:
            hashes.add(h)
        if layout.get('layout_hash'):
            hashes.add(layout.get('layout_hash'))
    return hashes


def is_decimal_odds(x):
    return bool(DECIMAL_ODDS_RE.fullmatch(str(x).strip()))


def parse_float(x):
    return float(str(x).replace(',', '.'))


def normalize_time_token(x):
    raw = str(x).strip()
    m = TIME_WITH_COUNT_RE.fullmatch(raw)
    if m:
        return m.group(1)
    return raw


def is_time(x):
    raw = normalize_time_token(x)
    return bool(TIME_ONLY_RE.fullmatch(raw) or TIME_WITH_DAY_RE.fullmatch(raw))


def is_date_header(x):
    return bool(DATE_HEADER_RE.fullmatch(str(x).strip()))


def date_header_day(x):
    raw = str(x).strip()
    if is_date_header(raw):
        return raw.split()[0].title()
    return None


def clean_lines(lines):
    out = []
    for raw in lines:
        line = str(raw).strip()
        if not line:
            continue
        if line in NOISE_EXACT or line.startswith(BAD_PREFIXES):
            continue
        m = ODDS_TRIPLE_RE.fullmatch(line)
        if m:
            out.extend([m.group(1), m.group(2), m.group(3)])
            continue
        out.append(line)
    return out


def looks_like_team(x):
    x = str(x).strip()
    if not x or len(x) < 2 or len(x) > 70:
        return False
    if x in NOISE_EXACT or x.startswith(BAD_PREFIXES):
        return False
    if is_date_header(x) or is_time(x) or is_decimal_odds(x):
        return False
    if re.search(r'\b1\s+X\s+2\b', x, re.I):
        return False
    if re.fullmatch(r'\d+\s+kampe', x, re.I):
        return False
    return bool(re.search(r'[A-Za-zÆØÅæøå]', x))


def infer_league_context(lines, idx):
    nearby = lines[max(0, idx - 20):idx + 20]
    joined = ' '.join(nearby)
    for key in ['Superligaen', 'Premier League', 'Championship', 'Bundesliga', 'Serie A', 'Ligue 1', 'LaLiga', 'Danmark', 'England', 'Tyskland', 'Italien', 'Spanien', 'Frankrig']:
        if key.lower() in joined.lower():
            return key
    return None


def status_from_confidence(confidence):
    mode = (confidence.get('execution_mode') or {}).get('mode')
    if mode == 'real_candidate':
        return 'parsed_candidate'
    if mode == 'paper_or_shadow_only':
        return 'shadow_only'
    return 'requires_review'


def make_observations(home_raw, away_raw, t_raw, odds_values, extraction, capture, timezone_name, league_hint, layout_approved, extraction_confidence):
    event_time = normalize_event_time(t_raw, capture, timezone_name)
    home_match = match_team(home_raw, league_hint=league_hint)
    away_match = match_team(away_raw, league_hint=league_hint)

    if home_match.get('requires_review'):
        add_alias_suggestion(home_raw, home_match, source_event=f'{home_raw} vs {away_raw}')
    if away_match.get('requires_review'):
        add_alias_suggestion(away_raw, away_match, source_event=f'{home_raw} vs {away_raw}')

    home_canon = home_match.get('canonical_name') or home_raw
    away_canon = away_match.get('canonical_name') or away_raw
    completeness = bool(home_raw and away_raw and t_raw and len(odds_values) == 3)
    confidence = calculate_parser_confidence(
        True,
        home_match,
        away_match,
        odds_values,
        event_time,
        completeness=completeness,
        extraction_confidence=extraction_confidence,
        layout_approved=layout_approved,
    )

    evt_id = event_id(home_canon, away_canon, league_hint, event_time.get('utc'))
    selections = [('1', home_canon, odds_values[0]), ('X', 'Draw', odds_values[1]), ('2', away_canon, odds_values[2])]
    status = status_from_confidence(confidence)
    observations = []
    for line, selection, price in selections:
        mkt_id = market_id(evt_id, '1X2', line, selection)
        obs_id = observation_id(mkt_id, capture.get('utc'), extraction.get('source_file'), price)
        observations.append({
            'record_type': 'market_observation',
            'event_id': evt_id,
            'market_id': mkt_id,
            'observation_id': obs_id,
            'source_file': extraction.get('source_file'),
            'file_id': extraction.get('file_id'),
            'capture': capture,
            'event_time': event_time,
            'event': {'raw_home': home_raw, 'raw_away': away_raw, 'home': home_canon, 'away': away_canon, 'league': league_hint, 'sport': 'football'},
            'canonical': {'home': home_match, 'away': away_match},
            'market': {'type': '1X2', 'line': line, 'selection': selection, 'odds': price},
            'parser_confidence': confidence,
            'text_extraction': extraction.get('text_extraction'),
            'status': status,
            'warnings': list(set((event_time.get('warnings') or []) + (extraction.get('text_extraction') or {}).get('warnings', []) + ([] if layout_approved else ['unknown_layout_warning'])))
        })
    return observations


def parse_inline_layout(lines, extraction, capture, timezone_name, layout_approved, extraction_confidence):
    observations = []
    i = 0
    while i <= len(lines) - 6:
        home_raw, away_raw, t_raw = lines[i], lines[i + 1], normalize_time_token(lines[i + 2])
        o1, ox, o2 = lines[i + 3], lines[i + 4], lines[i + 5]
        if looks_like_team(home_raw) and looks_like_team(away_raw) and is_time(t_raw) and all(is_decimal_odds(x) for x in [o1, ox, o2]):
            league_hint = infer_league_context(lines, i) or 'unknown'
            odds = [parse_float(o1), parse_float(ox), parse_float(o2)]
            observations.extend(make_observations(home_raw, away_raw, t_raw, odds, extraction, capture, timezone_name, league_hint, layout_approved, extraction_confidence))
            i += 6
        else:
            i += 1
    return observations


def parse_grouped_layout(lines, extraction, capture, timezone_name, layout_approved, extraction_confidence):
    observations = []
    current_day = None
    i = 0
    while i < len(lines):
        if is_date_header(lines[i]):
            current_day = date_header_day(lines[i])
        # Pattern: home, away, time, repeated, then one odds block with 3 odds per event.
        if i <= len(lines) - 3 and looks_like_team(lines[i]) and looks_like_team(lines[i + 1]) and is_time(lines[i + 2]):
            events = []
            start = i
            j = i
            while j <= len(lines) - 3 and looks_like_team(lines[j]) and looks_like_team(lines[j + 1]) and is_time(lines[j + 2]):
                t = normalize_time_token(lines[j + 2])
                if current_day and TIME_ONLY_RE.fullmatch(t):
                    t = f'{current_day} {t}'
                events.append((lines[j], lines[j + 1], t, j))
                j += 3
            odds = []
            k = j
            while k < len(lines) and is_decimal_odds(lines[k]) and len(odds) < len(events) * 3:
                odds.append(parse_float(lines[k]))
                k += 1
            if events and len(odds) >= len(events) * 3:
                league_hint = infer_league_context(lines, start) or 'unknown'
                for idx, (home_raw, away_raw, t_raw, event_idx) in enumerate(events):
                    event_odds = odds[idx * 3: idx * 3 + 3]
                    observations.extend(make_observations(home_raw, away_raw, t_raw, event_odds, extraction, capture, timezone_name, league_hint, layout_approved, extraction_confidence))
                i = k
                continue
        i += 1
    return observations


def parse_events_from_extraction(extraction, capture, timezone_name='Europe/Copenhagen'):
    lines = clean_lines(extraction.get('lines') or [])
    parser_errors = []
    known_hashes = load_known_layout_hashes()
    layout_hash = (extraction.get('text_extraction') or {}).get('layout_hash')
    layout_approved = layout_hash in known_hashes
    extraction_confidence = float((extraction.get('text_extraction') or {}).get('extraction_confidence') or 0)

    observations = parse_inline_layout(lines, extraction, capture, timezone_name, layout_approved, extraction_confidence)
    # Newer Safari/full-page PDFs sometimes place teams/times first and all odds below.
    grouped = parse_grouped_layout(lines, extraction, capture, timezone_name, layout_approved, extraction_confidence)
    existing_ids = {o.get('observation_id') for o in observations}
    for obs in grouped:
        if obs.get('observation_id') not in existing_ids:
            observations.append(obs)
            existing_ids.add(obs.get('observation_id'))
    return observations, parser_errors
