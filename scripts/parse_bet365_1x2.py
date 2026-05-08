import re
from normalize_time import normalize_event_time
from canonical_matcher import match_team, add_alias_suggestion
from parser_confidence import calculate_parser_confidence
from ids import event_id, market_id, observation_id

DECIMAL_ODDS_RE = re.compile(r'^\d{1,2}[\.,]\d{2}$')
TIME_ONLY_RE = re.compile(r'^\d{1,2}:\d{2}$')
TIME_WITH_DAY_RE = re.compile(r'^(Man|Tir|Ons|Tor|Fre|Lør|Søn)\s+\d{1,2}:\d{2}$', re.I)
ODDS_TRIPLE_RE = re.compile(r'^(\d{1,2}[\.,]\d{2})\s+(\d{1,2}[\.,]\d{2})\s+(\d{1,2}[\.,]\d{2})$')

NOISE_EXACT = {
    'bet365', 'bet', '365', 'ÅBN', 'Ansvarsfuldt spil', 'Sport', 'Live', 'Casino', 'Væddemål',
    'Hjem Sport Live Væddemål Casino', 'Information og forsinkelser i udsendelsen', 'Indstillinger',
    'Tilbud', 'Åbningstilbud', 'Lyd', 'Statistik', 'Resultater', 'Livescore Resultater', 'Hjælp',
    'Indbetalinger Udbetalinger', 'Fodbold', 'Bedste ligaer', 'KOMMENDE KAMPE Se alle'
}
BAD_PREFIXES = ('© ', 'Ved at besøge', 'Denne side er beskyttet', 'StopSpillet', 'Du kan ', 'bet365 er ', 'Server Tid', 'Session ')


def is_decimal_odds(x):
    return bool(DECIMAL_ODDS_RE.fullmatch(str(x).strip()))


def parse_float(x):
    return float(str(x).replace(',', '.'))


def is_time(x):
    raw = str(x).strip()
    return bool(TIME_ONLY_RE.fullmatch(raw) or TIME_WITH_DAY_RE.fullmatch(raw))


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
    if is_time(x) or is_decimal_odds(x):
        return False
    if re.search(r'\b1\s+X\s+2\b', x, re.I):
        return False
    if re.fullmatch(r'\d+\s+kampe', x, re.I):
        return False
    return bool(re.search(r'[A-Za-zÆØÅæøå]', x))


def infer_league_context(lines, idx):
    # Conservative local context: nearby line containing common league/country hints.
    nearby = lines[max(0, idx - 12):idx]
    joined = ' '.join(nearby)
    for key in ['Superligaen', 'Premier League', 'Championship', 'Bundesliga', 'Serie A', 'Ligue 1', 'LaLiga', 'Danmark', 'England', 'Tyskland', 'Italien', 'Spanien', 'Frankrig']:
        if key.lower() in joined.lower():
            return key
    return None


def parse_events_from_extraction(extraction, capture, timezone_name='Europe/Copenhagen'):
    lines = clean_lines(extraction.get('lines') or [])
    observations = []
    parser_errors = []
    i = 0
    while i <= len(lines) - 6:
        home_raw, away_raw, t_raw = lines[i], lines[i + 1], lines[i + 2]
        o1, ox, o2 = lines[i + 3], lines[i + 4], lines[i + 5]
        if looks_like_team(home_raw) and looks_like_team(away_raw) and is_time(t_raw) and all(is_decimal_odds(x) for x in [o1, ox, o2]):
            league_hint = infer_league_context(lines, i) or 'unknown'
            event_time = normalize_event_time(t_raw, capture, timezone_name)
            home_match = match_team(home_raw, league_hint=league_hint)
            away_match = match_team(away_raw, league_hint=league_hint)

            if home_match.get('requires_review'):
                add_alias_suggestion(home_raw, home_match, source_event=f'{home_raw} vs {away_raw}')
            if away_match.get('requires_review'):
                add_alias_suggestion(away_raw, away_match, source_event=f'{home_raw} vs {away_raw}')

            home_canon = home_match.get('canonical_name') or home_raw
            away_canon = away_match.get('canonical_name') or away_raw
            odds = [parse_float(o1), parse_float(ox), parse_float(o2)]
            completeness = bool(home_raw and away_raw and t_raw and len(odds) == 3)
            confidence = calculate_parser_confidence(True, home_match, away_match, odds, event_time, completeness=completeness)

            league = league_hint
            evt_id = event_id(home_canon, away_canon, league, event_time.get('utc'))
            selections = [
                ('1', home_canon, odds[0]),
                ('X', 'Draw', odds[1]),
                ('2', away_canon, odds[2]),
            ]
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
                    'event': {
                        'raw_home': home_raw,
                        'raw_away': away_raw,
                        'home': home_canon,
                        'away': away_canon,
                        'league': league,
                        'sport': 'football'
                    },
                    'canonical': {
                        'home': home_match,
                        'away': away_match
                    },
                    'market': {
                        'type': '1X2',
                        'line': line,
                        'selection': selection,
                        'odds': price
                    },
                    'parser_confidence': confidence,
                    'text_extraction': extraction.get('text_extraction'),
                    'status': 'parsed_candidate' if confidence.get('total', 0) >= 0.90 else 'shadow_only',
                    'warnings': list(set((event_time.get('warnings') or []) + (extraction.get('text_extraction') or {}).get('warnings', [])))
                })
            i += 6
        else:
            i += 1
    return observations, parser_errors
