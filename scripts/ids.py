import hashlib
import re


def norm(value):
    x = str(value or '').strip().lower()
    x = re.sub(r'\s+', ' ', x)
    return x


def stable_hash(prefix, *parts, length=16):
    raw = '|'.join(norm(p) for p in parts)
    return f'{prefix}_{hashlib.sha256(raw.encode("utf-8")).hexdigest()[:length]}'


def event_id(home, away, league, event_time_utc):
    return stable_hash('evt', home, away, league, event_time_utc)


def market_id(evt_id, market_type, line, selection):
    return stable_hash('mkt', evt_id, market_type, line, selection)


def observation_id(mkt_id, capture_time_utc, source_file, odds):
    return stable_hash('obs', mkt_id, capture_time_utc, source_file, odds)


def file_record_id(source_file, file_id):
    return stable_hash('file', source_file, file_id)
