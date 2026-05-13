import argparse
import csv
import html
import json
import os
import re
import time
from datetime import datetime, time as dtime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

BASE_URL = 'https://api.odds-api.io/v3'
BOOKMAKER = 'Bet365'
TZ = ZoneInfo('Europe/Copenhagen')
OUTPUT_DIR = Path('output/bet365/latest')
RAW_DIR = Path('data/raw/odds_api_io/bet365_today_multisport_report')

EXCLUDED_PATTERN = re.compile(
    r'(\bu\s?\d{2}\b|\bunder\s?\d{2}\b|\breserve\b|\breserves\b|\breserver\b|\byouth\b|\bacademy\b|\bb\s?team\b|\bii\b|\bexhibition\b|\bfriendly\b|\bfriendlies\b)',
    re.IGNORECASE,
)

GOOD_COMPETITION_PATTERN = re.compile(
    r'('
    # Football
    r'premier league|championship|fa cup|efl cup|laliga|la liga|segunda|copa del rey|serie a|serie b|coppa italia|'
    r'bundesliga|2\. bundesliga|dfb pokal|ligue 1|ligue 2|eredivisie|primeira liga|liga portugal|pro league|'
    r'premiership|superliga|allsvenskan|superettan|eliteserien|super league|austrian bundesliga|1\. liga|'
    r'super lig|saudi pro league|mls|brasileiro|brazil - serie a|argentina|liga mx|uefa|champions league|europa league|conference league|libertadores|sudamericana|'
    # Tennis
    r'atp|wta|grand slam|australian open|french open|roland garros|wimbledon|us open|masters|davis cup|billie jean king cup|'
    # Basketball
    r'nba|wnba|euroleague|eurocup|ncaa|liga acb|basketball bundesliga|legabasket|lnb|'
    # Ice hockey
    r'nhl|ahl|shl|liiga|del|national league|khl|'
    # American football / baseball
    r'nfl|ncaaf|mlb|npb|kbo|'
    # Cricket / rugby / handball / esports
    r'ipl|big bash|psl|t20 blast|world cup|six nations|top 14|premiership rugby|champions cup|ehf|handball bundesliga|lec|lcs|lck|lpl|major|iem|blast|valorant|dota|league of legends|counter-strike|cs2'
    r')',
    re.IGNORECASE,
)

DEFAULT_SPORTS = [
    'football',
    'tennis',
    'basketball',
    'ice-hockey',
    'american-football',
    'baseball',
    'cricket',
    'rugby-union',
    'rugby-league',
    'handball',
    'esports',
]


def now_dk():
    return datetime.now(TZ)


def today_window():
    today = now_dk().date()
    start = datetime.combine(today, dtime.min, tzinfo=TZ)
    end = datetime.combine(today, dtime.max, tzinfo=TZ).replace(microsecond=0)
    return today.isoformat(), start, end


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


def sport_name(event):
    value = event.get('sport')
    if isinstance(value, dict):
        return safe(value.get('name') or value.get('slug'))
    return safe(value)


def event_date(event):
    return safe(event.get('date') or event.get('startTime') or event.get('commence_time') or event.get('start_time'))


def bookmaker_count(event):
    return as_int(event.get('bookmakerCount') or event.get('bookmaker_count') or event.get('bookmakersCount'), 0)


def is_excluded_event(event):
    text = ' '.join([team(event, 'home'), team(event, 'away'), league(event), sport_name(event)])
    return bool(EXCLUDED_PATTERN.search(text))


def is_good_competition(event, min_bookmaker_count):
    comp = league(event)
    if GOOD_COMPETITION_PATTERN.search(comp):
        return True
    if min_bookmaker_count > 0 and bookmaker_count(event) >= min_bookmaker_count:
        return True
    return False


def request_json(url, params, label, headers_log):
    response = requests.get(url, params=params, timeout=30)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    redacted_url = response.url.replace(params.get('apiKey', ''), '***') if params.get('apiKey') else response.url
    headers_log.append({
        'label': label,
        'sport': params.get('sport', ''),
        'status_code': response.status_code,
        'x_ratelimit_limit': response.headers.get('x-ratelimit-limit', ''),
        'x_ratelimit_remaining': response.headers.get('x-ratelimit-remaining', ''),
        'x_ratelimit_reset': response.headers.get('x-ratelimit-reset', ''),
        'url': redacted_url,
    })
    (RAW_DIR / f'{label}.json').write_text(response.text, encoding='utf-8')
    if response.status_code >= 400:
        return None, f'HTTP {response.status_code}: {response.text[:300]}'
    try:
        return response.json(), ''
    except Exception as exc:
        return None, f'json_error:{exc}'


def fetch_events_for_sport(api_key, sport_slug, max_events, max_pages, min_bookmaker_count, headers_log):
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
        payload, error = request_json(f'{BASE_URL}/events', params, f'{sport_slug}_events_page_{page + 1}', headers_log)
        if error or payload is None:
            excluded.append({'sport_query': sport_slug, 'reason': error, 'event_id': '', 'date_denmark': '', 'home': '', 'away': '', 'league': '', 'bookmaker_count': ''})
            break
        rows = event_items(payload)
        for event in rows:
            eid = event_id(event)
            if not eid or eid in seen:
                continue
            seen.add(eid)
            row = {
                'sport_query': sport_slug,
                'event_id': eid,
                'date_denmark': dk_time(event_date(event)),
                'home': team(event, 'home'),
                'away': team(event, 'away'),
                'league': league(event),
                'sport': sport_name(event),
                'bookmaker_count': bookmaker_count(event),
            }
            if is_excluded_event(event):
                row['reason'] = 'excluded_youth_reserve_friendly_or_exhibition'
                excluded.append(row)
            elif is_good_competition(event, min_bookmaker_count):
                kept.append(event)
            else:
                row['reason'] = 'not_good_competition_or_low_coverage'
                excluded.append(row)
        if len(rows) < max_events:
            break
    return report_date, kept, excluded


def chunks(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]


def fetch_odds(api_key, events, max_price_events_per_sport, headers_log):
    by_sport = {}
    for event in events:
        key = safe(event.get('_sport_query')) or sport_name(event).lower() or 'unknown'
        by_sport.setdefault(key, []).append(event)
    selected = []
    all_payloads = []
    for sport_slug, sport_events in by_sport.items():
        sport_selected = sport_events[:max_price_events_per_sport]
        selected.extend(sport_selected)
        for batch_no, batch in enumerate(chunks(sport_selected, 10), start=1):
            ids = ','.join(event_id(e) for e in batch if event_id(e))
            if not ids:
                continue
            payload, error = request_json(
                f'{BASE_URL}/odds/multi',
                {'apiKey': api_key, 'eventIds': ids, 'bookmakers': BOOKMAKER},
                f'{sport_slug}_odds_multi_{batch_no}',
                headers_log,
            )
            if not error and payload is not None:
                all_payloads.extend(odds_items(payload))
            time.sleep(0.1)
    return selected, all_payloads


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
                'sport': sport_name(event),
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
                    'sport': sport_name(event),
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


def outcome_line(row):
    parts = []
    for label, key in [('H', 'home_odds'), ('X', 'draw_odds'), ('A', 'away_odds'), ('Over', 'over'), ('Under', 'under'), ('Yes', 'yes'), ('No', 'no')]:
        if row.get(key):
            parts.append(f'{label}: {row[key]}')
    text = ' | '.join(parts) if parts else row.get('raw_odds', '')[:140]
    if row.get('label'):
        text = f"{row['label']}: {text}"
    return text


def write_html(path, report_date, events, markets, headers_log, excluded, args):
    by_event = {}
    market_counts = {}
    sport_counts = {}
    for event in events:
        sport_counts[event.get('sport') or 'unknown'] = sport_counts.get(event.get('sport') or 'unknown', 0) + 1
    for row in markets:
        by_event.setdefault(row['event_id'], []).append(row)
        market_counts[row['market']] = market_counts.get(row['market'], 0) + 1
    sport_list = ''.join(f'<li>{html.escape(k)}: {v} events</li>' for k, v in sorted(sport_counts.items(), key=lambda x: (-x[1], x[0])))
    market_list = ''.join(f'<li>{html.escape(k)}: {v}</li>' for k, v in sorted(market_counts.items(), key=lambda x: (-x[1], x[0]))[:100])
    cards = []
    for event in sorted(events, key=lambda e: (e.get('date_denmark', ''), e.get('sport', ''), e.get('league', ''))):
        rows = by_event.get(event['event_id'], [])
        lines = [f"<li><strong>{html.escape(r['market'])}</strong> - {html.escape(outcome_line(r))}</li>" for r in rows[:45]]
        if len(rows) > 45:
            lines.append(f'<li>... {len(rows)-45} flere markedsrækker i CSV-filen</li>')
        cards.append(f"""
<section class="card">
  <div class="time">{html.escape(event['date_denmark'])} · {html.escape(event['sport'])}</div>
  <h2>{html.escape(event['home'])} vs {html.escape(event['away'])}</h2>
  <p>{html.escape(event['league'])}</p>
  <ul>{''.join(lines)}</ul>
</section>
""")
    latest = headers_log[-1] if headers_log else {}
    path.write_text(f"""<!doctype html><html lang="da"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bet365 multisport gode valg i dag</title><style>
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f6f6f6;margin:0;padding:16px;color:#111}}h1{{font-size:27px;margin:0 0 8px}}.summary,.card{{background:white;border-radius:14px;padding:16px;margin:12px 0;box-shadow:0 1px 5px rgba(0,0,0,.08)}}h2{{font-size:20px;margin:4px 0 6px}}.time{{font-size:14px;color:#555}}ul{{padding-left:20px}}li{{margin:7px 0;line-height:1.35}}.badge{{display:inline-block;background:#e8f1ff;padding:4px 8px;border-radius:999px;margin:2px}}.small{{color:#666;font-size:13px}}
</style></head><body>
<h1>Bet365 multisport – gode valg i dag</h1>
<div class="summary"><p><span class="badge">Dato: {html.escape(report_date)}</span><span class="badge">Bookmaker: Bet365</span><span class="badge">Sportsgrene: {len(args.sports)}</span><span class="badge">Events: {len(events)}</span><span class="badge">Markedsrækker: {len(markets)}</span><span class="badge">Frasorteret: {len(excluded)}</span></p><p class="small">Rent data-overblik til andet projekt. Alle Bet365-markeder gemmes. Kun gode/større turneringer, bredt dækkede events og ingen U/reserve/friendly/exhibition.</p><p class="small">Genereret {html.escape(now_dk().strftime('%Y-%m-%d %H:%M'))}. Rate-limit tilbage: {html.escape(str(latest.get('x_ratelimit_remaining','')))} / {html.escape(str(latest.get('x_ratelimit_limit','')))}</p></div>
<div class="summary"><h2>Sportsgrene fundet</h2><ul>{sport_list if sport_list else '<li>Ingen events</li>'}</ul></div>
<div class="summary"><h2>Markeder fundet</h2><ul>{market_list if market_list else '<li>Ingen markeder</li>'}</ul></div>
{''.join(cards) if cards else '<div class="card">Ingen gode Bet365-events fundet for i dag.</div>'}
</body></html>""", encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='Build multisport Bet365 all-market report for good betting options today')
    parser.add_argument('--sports', default=os.getenv('BET365_MULTI_SPORTS', ','.join(DEFAULT_SPORTS)))
    parser.add_argument('--max-events', type=int, default=int(os.getenv('BET365_MULTI_MAX_EVENTS', '100')))
    parser.add_argument('--max-pages', type=int, default=int(os.getenv('BET365_MULTI_MAX_PAGES', '3')))
    parser.add_argument('--max-price-events-per-sport', type=int, default=int(os.getenv('BET365_MULTI_MAX_PRICE_EVENTS_PER_SPORT', '25')))
    parser.add_argument('--min-bookmaker-count', type=int, default=int(os.getenv('BET365_MULTI_MIN_BOOKMAKER_COUNT', '15')))
    args = parser.parse_args()
    args.sports = [s.strip() for s in args.sports.split(',') if s.strip()]
    api_key = os.getenv('ODDS_API_IO_KEY')
    if not api_key:
        raise SystemExit('ODDS_API_IO_KEY is missing')
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    headers_log = []
    all_events, all_excluded = [], []
    report_date = today_window()[0]
    for sport_slug in args.sports:
        report_date, kept, excluded = fetch_events_for_sport(api_key, sport_slug, args.max_events, args.max_pages, args.min_bookmaker_count, headers_log)
        for event in kept:
            event['_sport_query'] = sport_slug
        all_events.extend(kept)
        all_excluded.extend(excluded)
        time.sleep(0.1)
    all_events.sort(key=lambda e: (event_date(e), sport_name(e), league(e)))
    selected, odds_payloads = fetch_odds(api_key, all_events, args.max_price_events_per_sport, headers_log)
    events, markets = flatten(odds_payloads)
    write_csv(OUTPUT_DIR / 'bet365_today_multisport_events.csv', events)
    write_csv(OUTPUT_DIR / 'bet365_today_multisport_markets.csv', markets)
    write_csv(OUTPUT_DIR / 'bet365_today_multisport_excluded.csv', all_excluded)
    write_csv(OUTPUT_DIR / 'bet365_today_multisport_rate_limit_headers.csv', headers_log)
    write_html(OUTPUT_DIR / 'bet365_today_multisport_report.html', report_date, events, markets, headers_log, all_excluded, args)
    summary = {
        'generated_at_dk': now_dk().strftime('%Y-%m-%d %H:%M'),
        'report_date_dk': report_date,
        'bookmaker': BOOKMAKER,
        'sports_requested': ','.join(args.sports),
        'events_after_filters': len(all_events),
        'events_requested_for_odds': len(selected),
        'events_with_odds': len(events),
        'market_rows': len(markets),
        'excluded_events': len(all_excluded),
        'min_bookmaker_count': args.min_bookmaker_count,
        'latest_rate_limit_remaining': headers_log[-1].get('x_ratelimit_remaining', '') if headers_log else '',
        'latest_rate_limit_limit': headers_log[-1].get('x_ratelimit_limit', '') if headers_log else '',
    }
    (OUTPUT_DIR / 'bet365_today_multisport_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
