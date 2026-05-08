import json
import pathlib
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from decimal import Decimal, InvalidOperation

TRACKER_PATH = pathlib.Path('data/pick_tracker.jsonl')
OUT_PATH = pathlib.Path('output/latest/market_state.json')
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

ACTIVE_WINDOW_PAST_HOURS = 24
ACTIVE_WINDOW_FUTURE_DAYS = 7


def utc_now_dt():
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso_utc(dt):
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def parse_dt(value):
    if not value:
        return None
    return datetime.fromisoformat(str(value).replace('Z', '+00:00')).astimezone(timezone.utc)


def odds_decimal(value):
    try:
        return Decimal(str(value)).quantize(Decimal('0.01'))
    except (InvalidOperation, TypeError, ValueError):
        return Decimal('0.00')


def read_jsonl(path=TRACKER_PATH):
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except Exception:
            continue
    return rows


def is_market_observation(row):
    return row.get('record_type') == 'market_observation' and row.get('market_id') and row.get('market')


def movement_summary(rows):
    clean = [r for r in rows if r.get('dedupe_status') != 'duplicate_noise']
    clean.sort(key=lambda r: parse_dt((r.get('capture') or {}).get('utc')) or datetime.min.replace(tzinfo=timezone.utc))
    if not clean:
        return {}
    first = clean[0]
    latest = clean[-1]
    first_odds = odds_decimal((first.get('market') or {}).get('odds'))
    latest_odds = odds_decimal((latest.get('market') or {}).get('odds'))
    change_pct = Decimal('0.00') if first_odds <= 0 else abs(latest_odds - first_odds) / first_odds
    movement = 'unchanged'
    if latest_odds < first_odds:
        movement = 'shortened'
    elif latest_odds > first_odds:
        movement = 'drifted'
    return {
        'first_seen_odds': float(first_odds),
        'latest_seen_odds': float(latest_odds),
        'first_seen_capture_utc': (first.get('capture') or {}).get('utc'),
        'latest_seen_capture_utc': (latest.get('capture') or {}).get('utc'),
        'change_pct_from_first': float(change_pct.quantize(Decimal('0.0001'))),
        'movement_from_first': movement,
        'observation_count': len(rows),
        'non_duplicate_observation_count': len(clean),
        'dedupe_counts': dict(__import__('collections').Counter(r.get('dedupe_status') for r in rows))
    }


def build_market_state(records=None):
    records = records if records is not None else read_jsonl()
    grouped = defaultdict(list)
    for r in records:
        if is_market_observation(r):
            grouped[r.get('market_id')].append(r)

    now = utc_now_dt()
    active_after = now - timedelta(hours=ACTIVE_WINDOW_PAST_HOURS)
    active_before = now + timedelta(days=ACTIVE_WINDOW_FUTURE_DAYS)
    markets = []
    for market_id, rows in grouped.items():
        rows.sort(key=lambda r: parse_dt((r.get('capture') or {}).get('utc')) or datetime.min.replace(tzinfo=timezone.utc))
        latest = rows[-1]
        ev_time = parse_dt((latest.get('event_time') or {}).get('utc'))
        active = bool(ev_time and active_after <= ev_time <= active_before)
        item = {
            'market_id': market_id,
            'event_id': latest.get('event_id'),
            'active': active,
            'event': latest.get('event'),
            'event_time': latest.get('event_time'),
            'market': latest.get('market'),
            'parser_confidence': latest.get('parser_confidence'),
            'latest_dedupe_status': latest.get('dedupe_status'),
            'movement_summary': movement_summary(rows),
            'latest_observation_id': latest.get('observation_id'),
            'source_file': latest.get('source_file')
        }
        markets.append(item)

    markets.sort(key=lambda m: ((m.get('event_time') or {}).get('utc') or '', (m.get('event') or {}).get('home') or '', (m.get('market') or {}).get('line') or ''))
    significant = [m for m in markets if (m.get('movement_summary') or {}).get('change_pct_from_first', 0) >= 0.10]
    small_or_more = [m for m in markets if (m.get('movement_summary') or {}).get('change_pct_from_first', 0) >= 0.03]
    state = {
        'generated_at': iso_utc(now),
        'source': 'data/pick_tracker.jsonl',
        'active_window': {
            'past_hours': ACTIVE_WINDOW_PAST_HOURS,
            'future_days': ACTIVE_WINDOW_FUTURE_DAYS
        },
        'summary': {
            'markets_total': len(markets),
            'markets_active': sum(1 for m in markets if m.get('active')),
            'markets_with_small_or_larger_movement': len(small_or_more),
            'markets_with_significant_movement': len(significant)
        },
        'significant_movements': significant[:50],
        'markets': markets
    }
    return state


def write_market_state(state=None):
    state = state or build_market_state()
    OUT_PATH.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
    return state


if __name__ == '__main__':
    s = write_market_state()
    print(f'Market state OK | markets={s["summary"]["markets_total"]} active={s["summary"]["markets_active"]}')
