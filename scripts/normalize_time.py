import re
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

DK_WEEKDAYS = {'Man': 0, 'Tir': 1, 'Ons': 2, 'Tor': 3, 'Fre': 4, 'Lør': 5, 'Søn': 6}
WEEKDAY_BY_IDX = ['Man', 'Tir', 'Ons', 'Tor', 'Fre', 'Lør', 'Søn']
CAPTURE_RE = re.compile(r'(\d{2})\.(\d{2})\.(\d{4}),\s*(\d{1,2})[\.:](\d{2})')
TIME_WITH_DAY_RE = re.compile(r'^(Man|Tir|Ons|Tor|Fre|Lør|Søn)\s+(\d{1,2}):(\d{2})$', re.I)
TIME_ONLY_RE = re.compile(r'^(\d{1,2}):(\d{2})$')


def iso_utc(dt):
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def parse_capture_time(text, tz_name='Europe/Copenhagen'):
    tz = ZoneInfo(tz_name)
    matches = list(CAPTURE_RE.finditer(str(text)))
    if not matches:
        now = datetime.now(tz).replace(microsecond=0)
        return {
            'raw_display': None,
            'local': now.isoformat(),
            'utc': iso_utc(now),
            'timezone': tz_name,
            'confidence': 0.45,
            'source': 'workflow_now_fallback',
            'trusted_capture_date': False,
            'warnings': ['capture_time_not_found_using_workflow_now']
        }
    m = matches[-1]
    day, month, year, hour, minute = map(int, m.groups())
    local = datetime(year, month, day, hour, minute, tzinfo=tz)
    return {
        'raw_display': m.group(0),
        'local': local.isoformat(),
        'utc': iso_utc(local),
        'timezone': tz_name,
        'confidence': 0.95,
        'source': 'bet365_pdf_text',
        'trusted_capture_date': True,
        'warnings': []
    }


def parse_dt(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))


def normalize_event_time(raw_time, capture, tz_name='Europe/Copenhagen', context='next_24_hours'):
    tz = ZoneInfo(tz_name)
    warnings = []
    raw = str(raw_time or '').strip()
    cap_local = parse_dt(capture['local']).astimezone(tz)
    trusted_capture_date = bool(capture.get('trusted_capture_date')) and float(capture.get('confidence') or 0) >= 0.90

    m_day = TIME_WITH_DAY_RE.fullmatch(raw)
    m_time = TIME_ONLY_RE.fullmatch(raw)
    method = None
    confidence = 0.0
    rollover_applied = False

    if m_day:
        day_name = m_day.group(1).title()
        hour, minute = int(m_day.group(2)), int(m_day.group(3))
        target_wd = DK_WEEKDAYS.get(day_name)
        delta_days = (target_wd - cap_local.weekday()) % 7
        event_local = (cap_local + timedelta(days=delta_days)).replace(hour=hour, minute=minute, second=0, microsecond=0)
        if event_local < cap_local - timedelta(minutes=30):
            event_local += timedelta(days=7)
            rollover_applied = True
        method = 'weekday_plus_time_from_capture_date'
        confidence = 0.95
    elif m_time:
        hour, minute = int(m_time.group(1)), int(m_time.group(2))
        event_local = cap_local.replace(hour=hour, minute=minute, second=0, microsecond=0)
        if event_local < cap_local - timedelta(minutes=30):
            if context == 'next_24_hours':
                event_local += timedelta(days=1)
                rollover_applied = True
                method = 'trusted_capture_date_next_24h_rollover' if trusted_capture_date else 'same_day_or_next_day_rollover_from_capture_date'
                confidence = 0.90 if trusted_capture_date else 0.80
            else:
                method = 'same_day_from_capture_date_time_passed'
                confidence = 0.25
                warnings.append('event_time_appears_to_be_in_past')
        else:
            method = 'trusted_capture_date_next_24h_same_day' if trusted_capture_date and context == 'next_24_hours' else 'same_day_from_capture_date'
            confidence = 0.90 if trusted_capture_date and context == 'next_24_hours' else 0.75
    else:
        return {
            'raw_display': raw,
            'local': None,
            'utc': None,
            'timezone': tz_name,
            'inference_method': 'unparsed',
            'rollover_applied': False,
            'confidence': 0.0,
            'checks': {'event_time_found': False},
            'warnings': ['event_time_unparsed']
        }

    now_utc = parse_dt(capture['utc']).astimezone(timezone.utc)
    event_utc_dt = event_local.astimezone(timezone.utc)
    in_future = event_utc_dt >= now_utc - timedelta(minutes=30)
    within_7_days = event_utc_dt <= now_utc + timedelta(days=7)
    if not in_future:
        confidence = min(confidence, 0.20)
        warnings.append('event_time_not_in_future')
    if not within_7_days:
        confidence = min(confidence, 0.35)
        warnings.append('event_time_outside_7_days')

    return {
        'raw_display': raw,
        'local': event_local.isoformat(),
        'utc': iso_utc(event_local),
        'timezone': tz_name,
        'inference_method': method,
        'rollover_applied': rollover_applied,
        'confidence': confidence,
        'trusted_capture_date_used': trusted_capture_date,
        'checks': {
            'event_time_found': True,
            'timezone_known': True,
            'event_in_future': in_future,
            'event_within_7_days': within_7_days,
            'dst_active': bool(event_local.dst()),
            'offset_seconds': int(event_local.utcoffset().total_seconds())
        },
        'warnings': warnings
    }
