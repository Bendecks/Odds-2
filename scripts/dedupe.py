from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation

DUPLICATE_WINDOW_MINUTES = 5
SMALL_ODDS_CHANGE_PCT = Decimal('0.03')
SIGNIFICANT_ODDS_CHANGE_PCT = Decimal('0.10')
EVENT_TIME_TOLERANCE_MINUTES = 10


def parse_dt(value):
    if not value:
        return None
    return datetime.fromisoformat(str(value).replace('Z', '+00:00')).astimezone(timezone.utc)


def minutes_between(a, b):
    da, db = parse_dt(a), parse_dt(b)
    if not da or not db:
        return None
    return abs((da - db).total_seconds()) / 60


def odds_decimal(value):
    try:
        return Decimal(str(value)).quantize(Decimal('0.01'))
    except (InvalidOperation, TypeError, ValueError):
        return Decimal('0.00')


def odds_change_pct(previous, latest):
    prev = odds_decimal(previous)
    new = odds_decimal(latest)
    if prev <= 0:
        return Decimal('0.00')
    return abs(new - prev) / prev


def latest_by_market(records):
    latest = {}
    for r in records:
        if r.get('record_type') not in {'market_observation', 'parsed_candidate'}:
            continue
        if r.get('dedupe_status') == 'duplicate_noise':
            continue
        mkt = r.get('market_id')
        if not mkt:
            continue
        cap = ((r.get('capture') or {}).get('utc')) or r.get('capture_time_utc')
        if not cap:
            continue
        if mkt not in latest or parse_dt(cap) > parse_dt(((latest[mkt].get('capture') or {}).get('utc')) or latest[mkt].get('capture_time_utc')):
            latest[mkt] = r
    return latest


def classify_odds_change(previous_odds, latest_odds):
    pct = odds_change_pct(previous_odds, latest_odds)
    if pct >= SIGNIFICANT_ODDS_CHANGE_PCT:
        return 'significant_odds_change', pct
    if pct >= SMALL_ODDS_CHANGE_PCT:
        return 'odds_movement', pct
    return 'small_movement', pct


def dedupe_observations(new_observations, previous_records):
    latest = latest_by_market(previous_records)
    out = []
    report = {
        'new_observation': 0,
        'duplicate_noise': 0,
        'new_observation_same_odds': 0,
        'small_movement': 0,
        'odds_movement': 0,
        'significant_odds_change': 0,
        'parser_conflict': 0
    }

    seen_this_batch = {}

    for obs in new_observations:
        row = dict(obs)
        mkt = row.get('market_id')
        prev = seen_this_batch.get(mkt) or latest.get(mkt)
        if not prev:
            row['dedupe_status'] = 'new_observation'
            out.append(row)
            report['new_observation'] += 1
            latest[mkt] = row
            seen_this_batch[mkt] = row
            continue

        prev_odds = odds_decimal((prev.get('market') or {}).get('odds'))
        new_odds = odds_decimal((row.get('market') or {}).get('odds'))
        cap_prev = (prev.get('capture') or {}).get('utc')
        cap_new = (row.get('capture') or {}).get('utc')
        mins = minutes_between(cap_prev, cap_new)
        same_odds = prev_odds == new_odds

        prev_event_time = (prev.get('event_time') or {}).get('utc')
        new_event_time = (row.get('event_time') or {}).get('utc')
        time_delta = minutes_between(prev_event_time, new_event_time)
        if time_delta is not None and time_delta > EVENT_TIME_TOLERANCE_MINUTES:
            row['dedupe_status'] = 'parser_conflict'
            row['parser_conflict'] = {
                'reason': 'same_market_id_but_event_time_mismatch',
                'previous_event_time_utc': prev_event_time,
                'new_event_time_utc': new_event_time,
                'delta_minutes': round(time_delta, 2)
            }
            out.append(row)
            report['parser_conflict'] += 1
            continue

        if same_odds and mins is not None and mins <= DUPLICATE_WINDOW_MINUTES:
            row['dedupe_status'] = 'duplicate_noise'
            row['duplicate_of_observation_id'] = prev.get('observation_id')
            out.append(row)
            report['duplicate_noise'] += 1
            continue

        if same_odds:
            row['dedupe_status'] = 'new_observation_same_odds'
            row['previous_observation_id'] = prev.get('observation_id')
            out.append(row)
            report['new_observation_same_odds'] += 1
            latest[mkt] = row
            seen_this_batch[mkt] = row
            continue

        status, pct = classify_odds_change(prev_odds, new_odds)
        movement = 'shortened' if new_odds < prev_odds else 'drifted'
        row['dedupe_status'] = status
        row['odds_movement'] = {
            'previous_odds': float(prev_odds),
            'latest_odds': float(new_odds),
            'change_pct': float(pct.quantize(Decimal('0.0001'))),
            'movement': movement,
            'previous_observation_id': prev.get('observation_id')
        }
        out.append(row)
        report[status] += 1
        latest[mkt] = row
        seen_this_batch[mkt] = row

    return out, report
