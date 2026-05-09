import json
import pathlib
from collections import defaultdict, Counter
from datetime import datetime, timezone

MARKET_STATE_PATH = pathlib.Path('output/latest/market_state.json')
OUT_LATEST = pathlib.Path('output/latest')
OUT_REPORTS = pathlib.Path('output/reports')
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_REPORTS.mkdir(parents=True, exist_ok=True)


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def load_state():
    if not MARKET_STATE_PATH.exists():
        return {'markets': []}
    return json.loads(MARKET_STATE_PATH.read_text(encoding='utf-8'))


def implied_prob(odds):
    try:
        o = float(odds)
        if o <= 1.0:
            return None
        return 1.0 / o
    except Exception:
        return None


def audit_event(markets):
    flags = []
    by_line = {str((m.get('market') or {}).get('line')): m for m in markets}
    required = {'1', 'X', '2'}
    missing = sorted(required - set(by_line))
    if missing:
        flags.append({'severity': 'fail', 'code': 'missing_1x2_lines', 'detail': ','.join(missing)})
        return flags

    odds = {line: (by_line[line].get('market') or {}).get('odds') for line in required}
    probs = {line: implied_prob(odds[line]) for line in required}
    if any(v is None for v in probs.values()):
        flags.append({'severity': 'fail', 'code': 'invalid_odds_value', 'detail': str(odds)})
        return flags

    overround = sum(probs.values())
    if overround < 1.00:
        flags.append({'severity': 'fail', 'code': 'underround_below_1_00', 'detail': round(overround, 4)})
    elif overround > 1.16:
        flags.append({'severity': 'fail', 'code': 'overround_above_1_16', 'detail': round(overround, 4)})
    elif overround > 1.12:
        flags.append({'severity': 'warn', 'code': 'overround_high_1_12_plus', 'detail': round(overround, 4)})

    draw = float(odds['X'])
    home = float(odds['1'])
    away = float(odds['2'])
    if draw < 1.80:
        flags.append({'severity': 'fail', 'code': 'draw_odds_implausibly_low', 'detail': draw})
    if draw < min(home, away) * 0.85:
        flags.append({'severity': 'fail', 'code': 'draw_much_shorter_than_both_sides', 'detail': {'home': home, 'draw': draw, 'away': away}})
    if min(home, draw, away) < 1.05:
        flags.append({'severity': 'fail', 'code': 'odds_below_1_05', 'detail': {'home': home, 'draw': draw, 'away': away}})
    if max(home, draw, away) > 25:
        flags.append({'severity': 'warn', 'code': 'odds_above_25', 'detail': {'home': home, 'draw': draw, 'away': away}})

    # If the draw is shorter than both teams, it is not impossible, but it is unusual enough
    # to require review unless the full book still looks normal.
    if draw < home and draw < away and overround > 1.10:
        flags.append({'severity': 'warn', 'code': 'draw_shortest_with_high_overround', 'detail': {'overround': round(overround, 4), 'home': home, 'draw': draw, 'away': away}})
    return flags


def main():
    state = load_state()
    groups = defaultdict(list)
    for m in state.get('markets') or []:
        if (m.get('market') or {}).get('type') == '1X2':
            groups[m.get('event_id')].append(m)

    flagged_market_ids = set()
    events = []
    counts = Counter()
    for event_id, markets in groups.items():
        flags = audit_event(markets)
        if not flags:
            continue
        severity = 'fail' if any(f.get('severity') == 'fail' for f in flags) else 'warn'
        for f in flags:
            counts[f.get('code')] += 1
        for m in markets:
            flagged_market_ids.add(m.get('market_id'))
        event = markets[0].get('event') or {}
        odds = {str((m.get('market') or {}).get('line')): (m.get('market') or {}).get('odds') for m in markets}
        events.append({
            'event_id': event_id,
            'event_name': f'{event.get("home")} vs {event.get("away")}',
            'event_time_utc': (markets[0].get('event_time') or {}).get('utc'),
            'source_file': markets[0].get('source_file'),
            'severity': severity,
            'odds': odds,
            'flags': flags,
            'market_ids': [m.get('market_id') for m in markets],
        })

    payload = {
        'generated_at': now_utc(),
        'audit_version': 'parser_audit_v1_1x2_mapping',
        'events_checked': len(groups),
        'events_flagged': len(events),
        'flagged_market_count': len(flagged_market_ids),
        'flag_counts': dict(counts),
        'flagged_market_ids': sorted(flagged_market_ids),
        'events': sorted(events, key=lambda e: (e.get('severity') != 'fail', e.get('event_time_utc') or '', e.get('event_name') or '')),
    }
    (OUT_LATEST / 'parser_audit.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')

    lines = ['# Odds 2 — Parser Audit Report', '', f'Generated: {payload["generated_at"]}', f'- Audit version: {payload["audit_version"]}', f'- Events checked: {payload["events_checked"]}', f'- Events flagged: {payload["events_flagged"]}', f'- Flagged markets: {payload["flagged_market_count"]}', f'- Flag counts: `{json.dumps(payload["flag_counts"], ensure_ascii=False)}`', '']
    if not events:
        lines.append('No suspicious 1X2 mappings found.')
    for e in payload['events']:
        lines += ['', f'## {e["event_name"]}', f'- Severity: {e["severity"]}', f'- Event time UTC: {e.get("event_time_utc")}', f'- Source file: {e.get("source_file")}', f'- Odds: `{json.dumps(e.get("odds"), ensure_ascii=False)}`', f'- Flags: `{json.dumps(e.get("flags"), ensure_ascii=False)}`']
    (OUT_REPORTS / 'parser_audit_report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'Parser audit OK | events_checked={payload["events_checked"]} events_flagged={payload["events_flagged"]} flagged_markets={payload["flagged_market_count"]}')


if __name__ == '__main__':
    main()
