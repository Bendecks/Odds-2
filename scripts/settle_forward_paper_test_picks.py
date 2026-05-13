import json
import os
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import pandas as pd
import requests

BASE_URL = 'https://api.odds-api.io/v3'
output_dir = Path('output/latest')
log_path = Path('data/predictions/paper_test_log.jsonl')
settlements_path = output_dir / 'forward_paper_test_settlements.csv'
summary_path = output_dir / 'forward_paper_test_settlement_summary.csv'
report_path = output_dir / 'forward_paper_test_settlement_report.md'
raw_dir = Path('data/raw/odds_api_io/forward_settlement')
raw_dir.mkdir(parents=True, exist_ok=True)

MAX_CALLS = int(os.getenv('ODDS_API_IO_SETTLEMENT_MAX_CALLS', '30'))
SLEEP_SECONDS = float(os.getenv('ODDS_API_IO_SETTLEMENT_SLEEP_SECONDS', '0.15'))
SETTLEMENT_MIN_HOURS_AFTER_KICKOFF = float(os.getenv('SETTLEMENT_MIN_HOURS_AFTER_KICKOFF', '2'))
FORWARD_PHASES = {'paper_forward_test', 'live_forward_snapshot', 'upcoming_fixture', 'automatic_forward_price_proxy'}
FINAL_STATUS_HINTS = {'finished', 'finish', 'completed', 'complete', 'ended', 'closed', 'final', 'ft', 'fulltime', 'settled'}
NON_FINAL_STATUS_HINTS = {'pending', 'scheduled', 'upcoming', 'not_started', 'not started', 'live', 'inplay', 'in_play', 'in progress', 'started'}


def clean(value):
    if pd.isna(value):
        return ''
    text = str(value).strip()
    if text.lower() in {'nan', 'none', 'nat'}:
        return ''
    return text


def parse_any_datetime(text):
    if not text:
        return pd.NaT
    parsed = pd.to_datetime(text, errors='coerce', utc=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(text, errors='coerce', dayfirst=True, utc=True)
    return parsed


def parse_dt(row):
    date_text = clean(row.get('match_date'))
    time_text = clean(row.get('match_time'))

    # Some upstream rows store a full datetime in match_time, e.g. "2026-05-13 10:00:00".
    if resemblances_full_datetime(time_text):
        parsed = parse_any_datetime(time_text)
        if not pd.isna(parsed):
            return parsed

    # Some rows store full datetime in match_date.
    if resemblances_full_datetime(date_text):
        parsed_date = parse_any_datetime(date_text)
        if not pd.isna(parsed_date):
            if time_text and not resemblances_full_datetime(time_text):
                date_only = parsed_date.strftime('%Y-%m-%d')
                parsed = parse_any_datetime(f'{date_only} {time_text}')
                if not pd.isna(parsed):
                    return parsed
            return parsed_date

    candidate = f'{date_text} {time_text}'.strip()
    return parse_any_datetime(candidate)


def resemblances_full_datetime(text):
    text = clean(text)
    if not text:
        return False
    return bool(pd.Series([text]).str.contains(r'\d{4}-\d{2}-\d{2}').iloc[0])


def make_bet_key(row):
    return '|'.join([
        clean(row.get('event_id')),
        clean(row.get('match_date')),
        clean(row.get('home_team')).lower(),
        clean(row.get('away_team')).lower(),
        clean(row.get('selection')).lower(),
    ])


def safe_read_jsonl(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_json(path, lines=True)
    except Exception:
        return pd.DataFrame()


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def fetch_event(api_key: str, event_id: str, call_no: int):
    url = f'{BASE_URL}/events/{event_id}'
    response = requests.get(url, params={'apiKey': api_key}, timeout=30)
    raw_path = raw_dir / f'event_{event_id}.json'
    raw_path.write_text(response.text, encoding='utf-8')
    headers = {
        'status_code': response.status_code,
        'x_ratelimit_limit': response.headers.get('x-ratelimit-limit', ''),
        'x_ratelimit_remaining': response.headers.get('x-ratelimit-remaining', ''),
        'x_ratelimit_reset': response.headers.get('x-ratelimit-reset', ''),
        'call_no': call_no,
    }
    if response.status_code >= 400:
        return None, headers, f'HTTP {response.status_code}'
    try:
        return response.json(), headers, ''
    except Exception as exc:
        return None, headers, f'json_error:{exc}'


def get_score(event):
    scores = event.get('scores') if isinstance(event, dict) else None
    if not isinstance(scores, dict):
        return None, None
    home = scores.get('home')
    away = scores.get('away')
    try:
        if home is None or away is None:
            return None, None
        return int(home), int(away)
    except Exception:
        return None, None


def is_final_event(event, kickoff):
    status = clean(event.get('status')).lower() if isinstance(event, dict) else ''
    has_final_hint = any(hint in status for hint in FINAL_STATUS_HINTS)
    has_non_final_hint = any(hint in status for hint in NON_FINAL_STATUS_HINTS)
    score_home, score_away = get_score(event)
    has_score = score_home is not None and score_away is not None
    if has_score and has_final_hint:
        return True
    if has_score and not has_non_final_hint and not pd.isna(kickoff):
        try:
            return kickoff.to_pydatetime() < datetime.now(timezone.utc) - timedelta(hours=3)
        except Exception:
            return False
    return False


def result_from_score(home_score, away_score):
    if home_score > away_score:
        return 'home'
    if away_score > home_score:
        return 'away'
    return 'draw'


def result_code(selection):
    text = clean(selection).lower()
    if text == 'home':
        return 'H'
    if text == 'away':
        return 'A'
    if text == 'draw':
        return 'D'
    return ''


api_key = os.getenv('ODDS_API_IO_KEY')
raw_log = safe_read_jsonl(log_path)
previous = safe_read_csv(settlements_path)

if not len(raw_log):
    empty = pd.DataFrame()
    empty.to_csv(settlements_path, index=False)
    pd.DataFrame([{'forward_log_rows': 0, 'settled_forward_picks': 0, 'pending_forward_picks': 0, 'api_calls_used': 0}]).to_csv(summary_path, index=False)
    report_path.write_text('# Forward paper-test settlement\n\nNo paper-test log found.', encoding='utf-8')
    print('No paper-test log found')
    raise SystemExit(0)

for col in ['sample_phase', 'event_id', 'match_date', 'match_time', 'home_team', 'away_team', 'selection', 'market_odds', 'paper_test_tier']:
    if col not in raw_log.columns:
        raw_log[col] = ''

forward = raw_log[raw_log['sample_phase'].fillna('').astype(str).isin(FORWARD_PHASES)].copy()
forward['bet_key'] = forward.apply(make_bet_key, axis=1)
forward['kickoff_dt'] = forward.apply(parse_dt, axis=1)
forward['market_odds_num'] = pd.to_numeric(forward['market_odds'], errors='coerce')
forward = forward.sort_values(['kickoff_dt'], ascending=True, na_position='last').drop_duplicates('bet_key', keep='last')

previous_settled_keys = set()
previous_rows = []
if len(previous):
    if 'settlement_status' in previous.columns and 'bet_key' in previous.columns:
        settled_prev = previous[previous['settlement_status'].astype(str).str.lower() == 'settled'].copy()
        previous_settled_keys = set(settled_prev['bet_key'].astype(str).tolist())
        previous_rows = settled_prev.to_dict(orient='records')

eligible = forward.copy()
if len(eligible):
    now = datetime.now(timezone.utc)
    eligible = eligible[eligible['kickoff_dt'].notna()].copy()
    eligible = eligible[eligible['kickoff_dt'] < pd.Timestamp(now - timedelta(hours=SETTLEMENT_MIN_HOURS_AFTER_KICKOFF))].copy()
    eligible = eligible[~eligible['bet_key'].isin(previous_settled_keys)].copy()
    eligible = eligible[eligible['event_id'].fillna('').astype(str).str.len() > 0].copy()

calls_used = 0
event_cache = {}
new_rows = []
api_error_rows = []

if api_key and len(eligible):
    for event_id in eligible['event_id'].astype(str).drop_duplicates().tolist():
        if calls_used >= MAX_CALLS:
            break
        calls_used += 1
        event, headers, error = fetch_event(api_key, event_id, calls_used)
        event_cache[event_id] = {'event': event, 'headers': headers, 'error': error}
        if SLEEP_SECONDS:
            time.sleep(SLEEP_SECONDS)
else:
    if not api_key:
        api_error_rows.append({'error': 'ODDS_API_IO_KEY missing'})

for _, row in forward.iterrows():
    bet_key = row['bet_key']
    if bet_key in previous_settled_keys:
        continue
    kickoff = row.get('kickoff_dt')
    event_id = clean(row.get('event_id'))
    base = row.drop(labels=['kickoff_dt'], errors='ignore').to_dict()
    base['bet_key'] = bet_key
    base['parsed_kickoff_utc'] = '' if pd.isna(kickoff) else kickoff.isoformat()
    base['settled_checked_at_utc'] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    base['settlement_source'] = 'odds_api_io_event_by_id'

    cache = event_cache.get(event_id)
    if cache is None:
        base['settlement_status'] = 'pending'
        base['settlement_note'] = 'not_eligible_yet_or_call_cap'
        new_rows.append(base)
        continue

    event = cache.get('event')
    error = cache.get('error')
    if error or not isinstance(event, dict):
        base['settlement_status'] = 'pending'
        base['settlement_note'] = error or 'event_fetch_failed'
        new_rows.append(base)
        continue

    score_home, score_away = get_score(event)
    base['api_event_status'] = clean(event.get('status'))
    base['api_score_home'] = score_home
    base['api_score_away'] = score_away

    if not is_final_event(event, kickoff):
        base['settlement_status'] = 'pending'
        base['settlement_note'] = 'event_not_final_or_no_score'
        new_rows.append(base)
        continue

    actual = result_from_score(score_home, score_away)
    selection = clean(row.get('selection')).lower()
    won = selection == actual
    odds = row.get('market_odds_num')
    roi = float(odds) - 1.0 if won and not pd.isna(odds) else -1.0
    base['settlement_status'] = 'settled'
    base['actual_result'] = actual
    base['match_result'] = result_code(actual)
    base['won'] = bool(won)
    base['roi_units'] = round(float(roi), 4)
    base['settlement_note'] = 'settled_from_odds_api_event_score'
    new_rows.append(base)

combined_rows = previous_rows + new_rows
settlements = pd.DataFrame(combined_rows)
if len(settlements):
    settlements = settlements.drop_duplicates('bet_key', keep='last')
settlements.to_csv(settlements_path, index=False)

settled_count = int((settlements.get('settlement_status', pd.Series(dtype=str)).astype(str).str.lower() == 'settled').sum()) if len(settlements) else 0
pending_count = int((settlements.get('settlement_status', pd.Series(dtype=str)).astype(str).str.lower() != 'settled').sum()) if len(settlements) else 0
wins = int((settlements.get('won', pd.Series(dtype=object)).astype(str).str.lower() == 'true').sum()) if len(settlements) else 0
losses = int((settlements.get('won', pd.Series(dtype=object)).astype(str).str.lower() == 'false').sum()) if len(settlements) else 0
roi = float(pd.to_numeric(settlements.get('roi_units', pd.Series(dtype=float)), errors='coerce').fillna(0).sum()) if len(settlements) else 0.0
parseable_kickoffs = int(forward['kickoff_dt'].notna().sum()) if len(forward) else 0

summary = {
    'forward_log_rows': int(len(forward)),
    'parseable_kickoffs': parseable_kickoffs,
    'eligible_to_check': int(len(eligible)),
    'api_calls_used': int(calls_used),
    'settled_forward_picks': settled_count,
    'pending_forward_picks': pending_count,
    'wins': wins,
    'losses': losses,
    'roi_units': round(roi, 4),
    'api_key_present': bool(api_key),
    'settlement_min_hours_after_kickoff': SETTLEMENT_MIN_HOURS_AFTER_KICKOFF,
}
pd.DataFrame([summary]).to_csv(summary_path, index=False)

lines = [
    '# Forward paper-test settlement',
    '',
    f"Forward log rows: {summary['forward_log_rows']}",
    f"Parseable kickoffs: {summary['parseable_kickoffs']}",
    f"Eligible to check: {summary['eligible_to_check']}",
    f"API calls used: {summary['api_calls_used']}",
    f"Settled forward picks: {summary['settled_forward_picks']}",
    f"Pending forward picks: {summary['pending_forward_picks']}",
    f"Wins: {summary['wins']}",
    f"Losses: {summary['losses']}",
    f"ROI units: {summary['roi_units']}",
    '',
]

if len(settlements):
    settled_display = settlements[settlements['settlement_status'].astype(str).str.lower() == 'settled'].copy() if 'settlement_status' in settlements.columns else pd.DataFrame()
    if len(settled_display):
        lines.extend(['## Settled picks', ''])
        for _, row in settled_display.tail(50).iterrows():
            result = 'Vundet' if str(row.get('won')).lower() == 'true' else 'Tabt'
            lines.append(f"- {row.get('match_date')} | {row.get('home_team')} vs {row.get('away_team')} | selection={row.get('selection')} | score={row.get('api_score_home')}-{row.get('api_score_away')} | {result} | ROI={row.get('roi_units')}")

pending_display = settlements[settlements['settlement_status'].astype(str).str.lower() != 'settled'].copy() if len(settlements) and 'settlement_status' in settlements.columns else pd.DataFrame()
if len(pending_display):
    lines.extend(['', '## Pending sample', ''])
    for _, row in pending_display.tail(30).iterrows():
        lines.append(f"- {row.get('match_date')} {row.get('match_time')} | parsed={row.get('parsed_kickoff_utc')} | {row.get('home_team')} vs {row.get('away_team')} | note={row.get('settlement_note')}")

report_path.write_text('\n'.join(lines), encoding='utf-8')
print(summary)
