import json
import pathlib
from datetime import datetime, timezone

TRACKER_PATH = pathlib.Path('data/pick_tracker.jsonl')
TRACKER_PATH.parent.mkdir(parents=True, exist_ok=True)


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def read_tracker(path=TRACKER_PATH):
    records = []
    if not path.exists():
        return records
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except Exception:
            records.append({'record_type': 'tracker_parse_error', 'raw_line': line[:500], 'seen_at': utc_now()})
    return records


def append_records(records, path=TRACKER_PATH):
    if not records:
        return 0
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as f:
        for r in records:
            row = dict(r)
            row.setdefault('tracker_appended_at', utc_now())
            f.write(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n')
    return len(records)
