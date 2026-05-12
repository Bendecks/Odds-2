import argparse
import csv
import html
import json
import os
import re
import sys
from datetime import datetime, time, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

BASE_URL = 'https://api.odds-api.io/v3'
BOOKMAKER = 'Bet365'
TZ = ZoneInfo('Europe/Copenhagen')
OUTPUT_DIR = Path('output/bet365/latest')
RAW_DIR = Path('data/raw/odds_api_io/bet365_today_major_report')

EXCLUDED_PATTERN = re.compile(
    r'(\bu\s?\d{2}\b|\bunder\s?\d{2}\b|\breserve\b|\breserves\b|\breserver\b|\byouth\b|\bacademy\b|\bb\s?team\b|\bii\b)',
    re.IGNORECASE,
)

MAJOR_LEAGUE_PATTERN = re.compile(
    r'('
    r'england - premier league|england - championship|england - fa cup|england - efl cup|'
    r'spain - laliga|spain - la liga|spain - segunda|spain - copa del rey|'
    r'italy - serie a|italy - serie b|italy - coppa italia|'
    r'germany - bundesliga|germany - 2\. bundesliga|germany - dfb pokal|'
    r'france - ligue 1|france - ligue 2|france - coupe de france|'
    r'netherlands - eredivisie|netherlands - eerste divisie|'
    r'portugal - primeira liga|portugal - liga portugal|'
    r'belgium - pro league|belgium - first division|'
    r'scotland - premiership|scotland - championship|'
    r'denmark - superliga|sweden - allsvenskan|sweden - superettan|norway - eliteserien|'
    r'switzerland - super league|austria - bundesliga|czechia - 1\. liga|'
    r'greece - super league|turkey - super lig|turkiye - super lig|'
    r'saudi arabia - saudi pro league|united states - mls|usa - mls|'
    r'brazil - serie a|argentina - primera|mexico - liga mx|'
    r'uefa|champions league|europa league|conference league|copa libertadores|copa sudamericana'
    r')',
    re.IGNORECASE,
)


def now_dk():
    return datetime.now(TZ)


def iso_z(dt):
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def dk_time(value):
    if not value:
        return ''
    try:
        return datetime.fromisoformat(str(value).replace('Z', '+00:00')).astimezone(TZ).strftime('%Y-%m-%d %H:%M')
    except Exception:
        return str(value)


def safe(value):
    return '' if value is None else str(value).strip()


def as_int(value, default=0):
    try:
        return int(float(value))
    except Exception:
        return default


def event_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ['events', 'data', 'results']:
            if isinstance(payload.get(key), list):
                return payload[key]
    return []


def odds_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        if 'bookmakers' in payload and ('id' in payload or 'eventId' in payload or 'event_id' in payload):
            return [payload]
        for key in ['events', 'data', 'results', 'odds']:
            if isinstance(payload.get(key), list):
                return payload[key]
        values = [v for v in payload.values() if isinstance(v, dict) and 'bookmakers' in v]
        if values:
            return values
    return []


def event_id(event):
    return safe(event.get('id') or event.get('eventId') or event.get('event_id'))


def team(event, side):
    if side == 'home':
        return safe(event.get('home') or event.get('homeTeam') or event.get('home_team'))
    return safe(event.get('away') or event.get('awayTeam') or event.get('away_team'))


def league(event):
    value = event.get('league')
    if isinstance(value, dict):
        return safe(value.get('name') or value.get('slug'))
    return safe(value)


def sport(event):
    value = event.get('sport')
    if isinstance(value, dict):
        return safe(value.get('name') or value.get('slug'))
    return safe(value)


def event_date(event):
    return safe(event.get('date') or event.get('startTime') or event.get('commence_time') or event.get('start_time'))


def bookmaker_count(event):
    return as_int(event.get('bookmakerCount') or event.get('bookmaker_count') or event.get('bookmakersCount'), 0)


def is_youth_or_reserve(event):
    text = ' '.join([team(event, 'home'), team(event, 'away'), league(event)])
    return bool(EXCLUDED_PATTERN.search(text))


def is_major_league(event):
    return bool(MAJOR_LEAGUE_PATTERN.search(league(event)))


def event_row(event, reason=''):
    return {
        'event_id': event_id(event),
        'date_denmark': dk_time(event_date(event)),
        'home': team(event, 'home'),
        'away': team(event, 'away'),
        'league': league(event),
        'sport': sport(event),
        'bookmaker_count': bookmaker_count(event),
        'is_major_league': is_major_league(event),
        'reason': reason,
    }


def request_json(url, params, label, headers_log):
    response = requests.get(url, params=params, timeout=30)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    redacted_url = response.url.replace(params.get('apiKey', ''), '***') if params.get('apiKey') else response.url
    headers_log.append({
        'label': label,
        'status_code': response.status_code,
        'x_ratelimit_limit': response.headers.get('x-ratelimit-limit', ''),
        'x_ratelimit_remaining': response.headers.get('x-ratelimit-remaining', ''),
        'x_ratelimit_reset': response.headers.get('x-ratelimit-reset', ''),
        'url': redacted_url,
    })
    (RAW_DIR / f'{label}.json').write_text(response.text, encoding='utf-8')
    if response.status_code >= 400:
        raise RuntimeError(f'{label}: HTTP {response.status_code}: {response.text[:500]}')
    return response.json()


def today_window():
    today = now_dk().date()
    start = datetime.combine(today, time.min, tzinfo=TZ)
    end = datetime.combine(today, time.max, tzinfo=TZ).replace(microsecond=0)
    return today.isoformat(), start, end


def fetch_events(api_key, sport_slug, max_events, max_pages, min_bookmaker_count, headers_log):
    report_date, start, end = today_window()
    kept, excluded = [], []
    seen = set()
    for page in range(max_pages):
        params = {
            'apiKey': api_key,
            'sport': sport_slug,
            'status': 'pending',
            'bookmaker': BOOKMAKER,
            'from': iso_z(start),
            'to': iso_z(end),
            'limit': max_events,
            'skip': page * max_events,
        }
        payload = request_json(f'{BASE_URL}/events', params, f'today_major_events_page_{page + 1}', headers_log)
        rows = event_items(payload)
        for event in rows:
            eid = event_id(event)
            if not eid or eid in seen:
                continue
            seen.add(eid)
            if is_youth_or_reserve(event):
                excluded.append(event_row(event, 'youth_or_reserve'))
            elif is_major_league(event):
                kept.append(event)
            elif min_bookmaker_count > 0 and bookmaker_count(event) >= min_bookmaker_count:
                kept.append(event)
            else:
                excluded.append(event_row(event, 'not_major_league_or_low_coverage'))
        if len(rows) < max_events:
            break
    kept.sort(key=lambda e: (event_date(e), league(e), team(e, 'home')))
    return report_date, kept, excluded


def chunks(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]


def fetch_odds(api_key, events, max_price_events, headers_log):
    selected = events[:max_price_events]
    output = []
    for batch_no, batch in enumerate(chunks(selected, 10), start=1):
        ids = ','.join(event_id(e) for e in batch if event_id(e))
        if not ids:
            continue
        payload = request_json(f'{BASE_URL}/odds/multi', {
            'apiKey': api_key,
            'eventIds': ids,
            'bookmakers': BOOKMAKER,
        }, f'today_major_odds_multi_{batch_no}', headers_log)
        output.extend(odds_items(payload))
    return selected, output


def flatten(odds_payloads):
    events, markets = [], []
    seen = set()
    for event in odds_payloads:
        if not isinstance(event, dict):
            continue
        eid = event_id(event)
        home, away, date = team(event, 'home'), team(event, 'away'), event_date(event)
        if eid and eid not in seen:
            seen.add(eid)
            events.append({
                'event_id': eid,
                'sport': sport(event),
                'league': league(event),
                'date_utc': date,
                'date_denmark': dk_time(date),
                'home': home,
                'away': away,
                'status': safe(event.get('status')),
            })
        bookmakers = event.get('bookmakers')
        if not isinstance(bookmakers, dict):
            continue
        bookmaker_markets = bookmakers.get(BOOKMAKER) or bookmakers.get(BOOKMAKER.lower()) or []
        if not isinstance(bookmaker_markets, list):
            continue
        for market in bookmaker_markets:
            if not isinstance(market, dict):
                continue
            odds_rows = market.get('odds') or []
            if isinstance(odds_rows, dict):
                odds_rows = [odds_rows]
            for odd in odds_rows or [{}]:
                if not isinstance(odd, dict):
                    odd = {}
                markets.append({
                    'event_id': eid,
                    'date_denmark': dk_time(date),
                    'home': home,
                    'away': away,
                    'league': league(event),
                    'bookmaker': BOOKMAKER,
                    'market': safe(market.get('name')) or 'Unknown market',
                    'label': safe(odd.get('label')),
                    'home_odds': safe(odd.get('home')),
                    'draw_odds': safe(odd.get('draw')),
                    'away_odds': safe(odd.get('away')),
                    'over': safe(odd.get('over')),
                    'under': safe(odd.get('under')),
                    'yes': safe(odd.get('yes')),
                    'no': safe(odd.get('no')),
                    'hdp': safe(odd.get('hdp')),
                    'raw_odds': json.dumps(odd, ensure_ascii=False),
                    'updated_at': safe(market.get('updatedAt')),
                })
    return events, markets


def write_csv(path, rows):
    if not rows:
        path.write_text('', encoding='utf-8')
        return
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def market_counts(markets):
    counts = {}
    for row in markets:
        counts[row['market']] = counts.get(row['market'], 0) + 1
    return counts


def outcome_line(row):
    parts = []
    for label, key in [('H', 'home_odds'), ('X', 'draw_odds'), ('A', 'away_odds'), ('Over', 'over'), ('Under', 'under'), ('Yes', 'yes'), ('No', 'no')]:
        if row.get(key):
            parts.append(f'{label}: {row[key]}')
    text = ' | '.join(parts) if parts else row.get('raw_odds', '')[:140]
    if row.get('label'):
        text = f"{row['label']}: {text}"
    return text


def write_html(path, report_date, events, markets, headers_log, args, excluded_count):
    counts = market_counts(markets)
    by_event = {}
    for row in markets:
        by_event.setdefault(row['event_id'], []).append(row)
    cards = []
    for event in events:
        rows = by_event.get(event['event_id'], [])
        lines = [f"<li><strong>{html.escape(r['market'])}</strong> - {html.escape(outcome_line(r))}</li>" for r in rows[:40]]
        if len(rows) > 40:
            lines.append(f'<li>... {len(rows)-40} flere markedsrækker i CSV-filen</li>')
        cards.append(f"""
<section class="card">
  <div class="time">{html.escape(event['date_denmark'])}</div>
  <h2>{html.escape(event['home'])} vs {html.escape(event['away'])}</h2>
  <p>{html.escape(event['league'])}</p>
  <ul>{''.join(lines)}</ul>
</section>
""")
    market_list = ''.join(f'<li>{html.escape(k)}: {v}</li>' for k, v in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:80])
    latest = headers_log[-1] if headers_log else {}
    path.write_text(f"""<!doctype html><html lang="da"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bet365 større ligaer i dag</title><style>
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f6f6f6;margin:0;padding:16px;color:#111}}h1{{font-size:28px;margin:0 0 8px}}.summary,.card{{background:white;border-radius:14px;padding:16px;margin:12px 0;box-shadow:0 1px 5px rgba(0,0,0,.08)}}h2{{font-size:20px;margin:4px 0 6px}}.time{{font-size:14px;color:#555}}ul{{padding-left:20px}}li{{margin:7px 0;line-height:1.35}}.badge{{display:inline-block;background:#e8f1ff;padding:4px 8px;border-radius:999px;margin:2px}}.small{{color:#666;font-size:13px}}
</style></head><body>
<h1>Bet365 odds – større ligaer i dag</h1>
<div class="summary"><p><span class="badge">Dato: {html.escape(report_date)}</span><span class="badge">Sport: {html.escape(args.sport)}</span><span class="badge">Bookmaker: Bet365</span><span class="badge">Kampe: {len(events)}</span><span class="badge">Markedsrækker: {len(markets)}</span><span class="badge">Frasorteret: {excluded_count}</span></p><p class="small">Rent data-overblik. Alle Bet365-markeder fra raw odds-responsen vises/lagres. Større ligaer vælges via allowlist. U-/reservekampe sorteres fra før odds hentes.</p><p class="small">Genereret {html.escape(now_dk().strftime('%Y-%m-%d %H:%M'))}. Rate-limit tilbage: {html.escape(str(latest.get('x_ratelimit_remaining','')))} / {html.escape(str(latest.get('x_ratelimit_limit','')))}</p></div>
<div class="summary"><h2>Markeder fundet</h2><ul>{market_list if market_list else '<li>Ingen markeder fundet</li>'}</ul></div>
{''.join(cards) if cards else '<div class="card">Ingen større Bet365-kampe fundet for i dag.</div>'}
</body></html>""", encoding='utf-8')


def write_markdown(path, report_date, events, markets, args, excluded_count):
    counts = market_counts(markets)
    by_event = {}
    for row in markets:
        by_event.setdefault(row['event_id'], []).append(row)
    lines = ['# Bet365 odds – større ligaer i dag', '', f'- Dato: **{report_date}**', f'- Sport: **{args.sport}**', '- Bookmaker: **Bet365**', f'- Kampe med odds: **{len(events)}**', f'- Markedsrækker: **{len(markets)}**', f'- Frasorteret: **{excluded_count}**', '', '## Markeder fundet', '']
    for name, count in sorted(counts.items(), key=lambda x: (-x[1], x[0]))[:80]:
        lines.append(f'- {name}: {count}')
    if not counts:
        lines.append('- Ingen markeder fundet')
    lines.extend(['', '## Kampe', ''])
    for event in events:
        lines.extend([f"### {event['home']} vs {event['away']}", f"- Kampstart: **{event['date_denmark']}**", f"- Liga: **{event['league']}**"])
        for row in by_event.get(event['event_id'], [])[:35]:
            lines.append(f"- **{row['market']}** - {outcome_line(row)}")
        lines.append('')
    path.write_text('\n'.join(lines), encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Build today Bet365 all-market report for major football events')
    parser.add_argument('--sport', default=os.getenv('BET365_REPORT_SPORT', 'football'))
    parser.add_argument('--max-events', type=int, default=int(os.getenv('BET365_REPORT_MAX_EVENTS', '100')))
    parser.add_argument('--max-pages', type=int, default=int(os.getenv('BET365_REPORT_MAX_PAGES', '6')))
    parser.add_argument('--max-price-events', type=int, default=int(os.getenv('BET365_REPORT_MAX_PRICE_EVENTS', '80')))
    parser.add_argument('--min-bookmaker-count', type=int, default=int(os.getenv('BET365_REPORT_MIN_BOOKMAKER_COUNT', '0')))
    args = parser.parse_args()
    api_key = os.getenv('ODDS_API_IO_KEY')
    if not api_key:
        print('ODDS_API_IO_KEY is missing', file=sys.stderr)
        return 2
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    headers_log = []
    report_date, discovered, excluded = fetch_events(api_key, args.sport, args.max_events, args.max_pages, args.min_bookmaker_count, headers_log)
    selected, odds_payloads = fetch_odds(api_key, discovered, args.max_price_events, headers_log)
    events, markets = flatten(odds_payloads)
    write_csv(OUTPUT_DIR / 'bet365_today_major_events.csv', events)
    write_csv(OUTPUT_DIR / 'bet365_today_major_markets.csv', markets)
    write_csv(OUTPUT_DIR / 'bet365_today_major_excluded.csv', excluded)
    write_csv(OUTPUT_DIR / 'bet365_today_major_rate_limit_headers.csv', headers_log)
    write_html(OUTPUT_DIR / 'bet365_today_major_odds_report.html', report_date, events, markets, headers_log, args, len(excluded))
    write_markdown(OUTPUT_DIR / 'bet365_today_major_odds_report.md', report_date, events, markets, args, len(excluded))
    summary = {
        'generated_at_dk': now_dk().strftime('%Y-%m-%d %H:%M'),
        'report_date_dk': report_date,
        'sport': args.sport,
        'bookmaker': BOOKMAKER,
        'filter': 'major_league_allowlist_plus_optional_bookmaker_count',
        'min_bookmaker_count': args.min_bookmaker_count,
        'events_after_filters': len(discovered),
        'events_requested_for_odds': len(selected),
        'events_with_odds': len(events),
        'market_rows': len(markets),
        'excluded_events': len(excluded),
        'latest_rate_limit_remaining': headers_log[-1].get('x_ratelimit_remaining', '') if headers_log else '',
        'latest_rate_limit_limit': headers_log[-1].get('x_ratelimit_limit', '') if headers_log else '',
    }
    (OUTPUT_DIR / 'bet365_today_major_report_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
