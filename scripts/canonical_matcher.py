import json
import pathlib
import re
import unicodedata
from difflib import SequenceMatcher
from datetime import datetime, timezone

DATA_DIR = pathlib.Path('data')
ALIASES_PATH = DATA_DIR / 'team_aliases.json'
SUGGESTIONS_PATH = DATA_DIR / 'team_alias_suggestions.json'


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def strip_accents(value):
    return ''.join(c for c in unicodedata.normalize('NFKD', str(value)) if not unicodedata.combining(c))


def normalize_name(value):
    x = strip_accents(value).lower().strip()
    x = x.replace('…', '...')
    x = re.sub(r'\b(fc|if|bk|cf|afc|sc|ss|rc|ca|cd|ud|vfl|tsg)\b', ' ', x)
    x = re.sub(r'[^a-z0-9]+', ' ', x)
    x = re.sub(r'\s+', ' ', x).strip()
    return x


def load_aliases():
    if not ALIASES_PATH.exists():
        return []
    data = json.loads(ALIASES_PATH.read_text(encoding='utf-8'))
    return data.get('teams') or []


def candidate_names(team):
    vals = [team.get('canonical')]
    vals.extend(team.get('aliases') or [])
    return [v for v in vals if v]


def score_pair(raw, candidate):
    rn = normalize_name(raw)
    cn = normalize_name(candidate)
    if not rn or not cn:
        return 0.0
    if rn == cn:
        return 1.0
    # Truncation handling: bet365 often cuts with ellipsis.
    raw_truncated = str(raw).strip().endswith(('…', '...'))
    if raw_truncated:
        prefix = rn.replace('...', '').strip()
        if prefix and cn.startswith(prefix):
            return min(0.98, 0.86 + len(prefix) / max(len(cn), 1) * 0.14)
    if rn in cn or cn in rn:
        return max(0.72, min(len(rn), len(cn)) / max(len(rn), len(cn)))
    return SequenceMatcher(None, rn, cn).ratio()


def league_bonus(team, league_hint):
    if not league_hint:
        return 0.0
    hints = ' '.join(team.get('league_hint') or []).lower()
    lh = str(league_hint).lower()
    if not hints or not lh:
        return 0.0
    return 0.05 if any(part and part in lh for part in hints.split()) else 0.0


def match_team(raw_name, league_hint=None, threshold=0.85):
    teams = load_aliases()
    best = None
    best_alias = None
    best_score = 0.0
    best_method = 'none'

    for team in teams:
        for alias in candidate_names(team):
            s = score_pair(raw_name, alias)
            method = 'direct_or_fuzzy'
            if str(raw_name).strip() == str(alias).strip():
                method = 'exact_alias'
            elif str(raw_name).strip().endswith(('…', '...')):
                method = 'truncated_or_fuzzy'
            s = min(1.0, s + league_bonus(team, league_hint))
            if s > best_score:
                best_score = s
                best = team
                best_alias = alias
                best_method = method

    if not best:
        return {
            'raw_name': raw_name,
            'canonical_name': None,
            'match_score': 0.0,
            'match_method': 'no_alias_data',
            'requires_review': True,
            'country': None,
            'league_hint': None,
            'matched_alias': None
        }

    requires_review = best_score < threshold
    return {
        'raw_name': raw_name,
        'canonical_name': best.get('canonical') if not requires_review else None,
        'suggested_canonical': best.get('canonical'),
        'match_score': round(best_score, 4),
        'match_method': best_method,
        'requires_review': requires_review,
        'country': best.get('country'),
        'league_hint': best.get('league_hint'),
        'matched_alias': best_alias
    }


def load_suggestions():
    if not SUGGESTIONS_PATH.exists():
        return {'version': 1, 'updated_at': None, 'suggestions': []}
    return json.loads(SUGGESTIONS_PATH.read_text(encoding='utf-8'))


def save_suggestions(data):
    DATA_DIR.mkdir(exist_ok=True)
    data['updated_at'] = utc_now()
    SUGGESTIONS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def add_alias_suggestion(raw_name, match, source_event=None):
    data = load_suggestions()
    key = (str(raw_name), str(match.get('suggested_canonical')))
    existing = {(s.get('raw_name'), s.get('suggested_canonical')) for s in data.get('suggestions', [])}
    if key in existing:
        return False
    data.setdefault('suggestions', []).append({
        'raw_name': raw_name,
        'suggested_canonical': match.get('suggested_canonical'),
        'reason': 'low_confidence_or_unknown_team',
        'confidence': match.get('match_score'),
        'match_method': match.get('match_method'),
        'source_event': source_event,
        'status': 'pending_review',
        'created_at': utc_now()
    })
    save_suggestions(data)
    return True
