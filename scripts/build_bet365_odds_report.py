import argparse
import csv
import html
import json
import os
import sys
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import requests

BASE_URL = 'https://api.odds-api.io/v3'
OUTPUT_DIR = Path('output/bet365/latest')
RAW_DIR = Path('data/raw/odds_api_io/bet365_manual_report')
BOOKMAKER = 'Bet365'


def now_utc():
    return datetime.now(timezone.utc)


def iso_z(dt):
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def dk_time(value):
    if not value:
        return ''
    try:
        dt = datetime.fromisoformat(str(value).replace('Z', '+00:00'))
        return dt.astimezone(ZoneInfo('Europe/Copenhagen')).strftime('%Y-%m-%d %H:%M')
    except Exception:
        return str(value)


def safe_text(value):
    if value is None:
        return ''
    return str(value).strip()


def event_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for key in ['events', 'data', 'results']:
            if isinstance(payload.get(key), list):
                return payload[key]
    return []


def odds_response_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        if 'bookmakers' in payload and ('id' in payload or 'eventId' in payload or 'event_id' in payload):
            return [payload]
        for key in ['events', 'data', 'results', 'odds']:
            if isinstance(payload.get(key), list):
                return payload[key]
        values = [value for value in payload.values() if isinstance(value, dict) and 'bookmakers' in value]
        if values:
            return values
    return []


def get_event_id(event):
    return safe_text(event.get('id') or event.get('eventId') or event.get('event_id'))


def get_team(event, key):
    if key == 'home':
        return safe_text(event.get('home') or event.get('homeTeam') or event.get('home_team'))
    return safe_text(event.get('away') or event.get('awayTeam') or event.get('away_team'))


def get_league(event):
    league = event.get('league')
    if isinstance(league, dict):
        return safe_text(league.get('name') or league.get('slug'))
    return safe_text(league)


def get_sport(event):
    sport = event.get('sport')
    if isinstance(sport, dict):
        return safe_text(sport.get('name') or sport.get('slug'))
    return safe_text(sport)


def get_event_date(event):
    return safe_text(event.get('date') or event.get('startTime') or event.get('commence_time') or event.get('start_time'))


def request_json(url, params, label, headers_log, raw_dir):
    response = requests.get(url, params=params, timeout=30)
    headers_log.append({
        'label': label,
        'status_code': response.status_code,
        'x_ratelimit_limit': response.headers.get('x-ratelimit-limit', ''),
        'x_ratelimit_remaining': response.headers.get('x-ratelimit-remaining', ''),
        'x_ratelimit_reset': response.headers.get('x-ratelimit-reset', ''),
        'retry_after': response.headers.get('retry-after', ''),
        'url': response.url.replace(params.get('apiKey', ''), '***') if params.get('apiKey') else response.url,
    })
    raw_path = raw_dir / f'{label}.json'
    raw_path.write_text(response.text, encoding='utf-8')
    if response.status_code >= 400:
        raise RuntimeError(f'{label}: HTTP {response.status_code}: {response.text[:500]}')
    return response.json()


def fetch_events(api_key, sport, lookahead_days, max_events, max_pages, headers_log):
    start = now_utc()
    end = start + timedelta(days=lookahead_days)
    all_events = []
    seen = set()
    for page in range(max_pages):
        params = {
            'apiKey': api_key,
            'sport': sport,
            'status': 'pending',
            'bookmaker': BOOKMAKER,
            'from': iso_z(start),
            'to': iso_z(end),
            'limit': max_events,
            'skip': page * max_events,
        }
        payload = request_json(f'{BASE_URL}/events', params, f'events_page_{page + 1}', headers_log, RAW_DIR)
        rows = event_items(payload)
        for event in rows:
            event_id = get_event_id(event)
            if event_id and event_id not in seen:
                seen.add(event_id)
                all_events.append(event)
        if len(rows) < max_events:
            break
    return all_events


def chunks(items, size):
    for start in range(0, len(items), size):
        yield items[start:start + size]


def fetch_odds(api_key, events, max_price_events, headers_log):
    selected = events[:max_price_events]
    all_odds = []
    for batch_no, batch in enumerate(chunks(selected, 10), start=1):
        event_ids = ','.join(get_event_id(event) for event in batch if get_event_id(event))
        if not event_ids:
            continue
        params = {
            'apiKey': api_key,
            'eventIds': event_ids,
            'bookmakers': BOOKMAKER,
        }
        payload = request_json(f'{BASE_URL}/odds/multi', params, f'odds_multi_{batch_no}', headers_log, RAW_DIR)
        all_odds.extend(odds_response_items(payload))
    return selected, all_odds


def flatten_markets(odds_items):
    market_rows = []
    event_rows = []
    seen_event_rows = set()
    for event in odds_items:
        if not isinstance(event, dict):
            continue
        event_id = get_event_id(event)
        home = get_team(event, 'home')
        away = get_team(event, 'away')
        date = get_event_date(event)
        league = get_league(event)
        sport = get_sport(event)
        if event_id and event_id not in seen_event_rows:
            seen_event_rows.add(event_id)
            event_rows.append({
                'event_id': event_id,
                'sport': sport,
                'league': league,
                'date_utc': date,
                'date_denmark': dk_time(date),
                'home': home,
                'away': away,
                'status': safe_text(event.get('status')),
            })
        bookmakers = event.get('bookmakers')
        if not isinstance(bookmakers, dict):
            continue
        markets = bookmakers.get(BOOKMAKER) or bookmakers.get(BOOKMAKER.lower()) or []
        if not isinstance(markets, list):
            continue
        for market in markets:
            if not isinstance(market, dict):
                continue
            market_name = safe_text(market.get('name')) or 'Unknown market'
            updated_at = safe_text(market.get('updatedAt'))
            odds_values = market.get('odds') or []
            if isinstance(odds_values, dict):
                odds_values = [odds_values]
            if not odds_values:
                market_rows.append({
                    'event_id': event_id,
                    'date_denmark': dk_time(date),
                    'home': home,
                    'away': away,
                    'league': league,
                    'bookmaker': BOOKMAKER,
                    'market': market_name,
                    'label': '',
                    'home_odds': '',
                    'draw_odds': '',
                    'away_odds': '',
                    'over': '',
                    'under': '',
                    'yes': '',
                    'no': '',
                    'hdp': '',
                    'raw_odds': '',
                    'updated_at': updated_at,
                })
            for odd in odds_values:
                if not isinstance(odd, dict):
                    continue
                market_rows.append({
                    'event_id': event_id,
                    'date_denmark': dk_time(date),
                    'home': home,
                    'away': away,
                    'league': league,
                    'bookmaker': BOOKMAKER,
                    'market': market_name,
                    'label': safe_text(odd.get('label')),
                    'home_odds': safe_text(odd.get('home')),
                    'draw_odds': safe_text(odd.get('draw')),
                    'away_odds': safe_text(odd.get('away')),
                    'over': safe_text(odd.get('over')),
                    'under': safe_text(odd.get('under')),
                    'yes': safe_text(odd.get('yes')),
                    'no': safe_text(odd.get('no')),
                    'hdp': safe_text(odd.get('hdp')),
                    'raw_odds': json.dumps(odd, ensure_ascii=False),
                    'updated_at': updated_at,
                })
    return event_rows, market_rows


def write_csv(path, rows):
    if not rows:
        path.write_text('', encoding='utf-8')
        return
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_html(path, event_rows, market_rows, headers_log, args):
    market_counts = {}
    for row in market_rows:
        market_counts[row['market']] = market_counts.get(row['market'], 0) + 1
    cards = []
    by_event = {}
    for row in market_rows:
        by_event.setdefault(row['event_id'], []).append(row)
    for event in event_rows:
        rows = by_event.get(event['event_id'], [])
        top_rows = rows[:25]
        market_lines = []
        for row in top_rows:
            parts = []
            for label, key in [('H', 'home_odds'), ('X', 'draw_odds'), ('A', 'away_odds'), ('Over', 'over'), ('Under', 'under'), ('Yes', 'yes'), ('No', 'no')]:
                if row.get(key):
                    parts.append(f'{label}: {html.escape(row[key])}')
            line = ' | '.join(parts) if parts else html.escape(row.get('raw_odds', '')[:120])
            if row.get('label'):
                line = f"{html.escape(row['label'])}: {line}"
            market_lines.append(f"<li><strong>{html.escape(row['market'])}</strong> - {line}</li>")
        if len(rows) > len(top_rows):
            market_lines.append(f'<li>... {len(rows) - len(top_rows)} flere markedsrækker i CSV-filen</li>')
        cards.append(f"""
        <section class="card">
          <div class="time">{html.escape(event['date_denmark'])}</div>
          <h2>{html.escape(event['home'])} vs {html.escape(event['away'])}</h2>
          <p>{html.escape(event['league'])}</p>
          <ul>{''.join(market_lines)}</ul>
        </section>
        """)
    market_count_lines = ''.join(f'<li>{html.escape(name)}: {count}</li>' for name, count in sorted(market_counts.items(), key=lambda x: (-x[1], x[0]))[:40])
    latest_header = headers_log[-1] if headers_log else {}
    path.write_text(f"""<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bet365 odds report</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background:#f6f6f6; margin:0; padding:16px; color:#111; }}
h1 {{ font-size: 28px; margin: 0 0 8px; }}
.summary, .card {{ background:white; border-radius:14px; padding:16px; margin:12px 0; box-shadow:0 1px 5px rgba(0,0,0,.08); }}
h2 {{ font-size:20px; margin:4px 0 6px; }}
.time {{ font-size:14px; color:#555; }}
ul {{ padding-left:20px; }}
li {{ margin:7px 0; line-height:1.35; }}
.badge {{ display:inline-block; background:#e8f1ff; padding:4px 8px; border-radius:999px; margin:2px; }}
.small {{ color:#666; font-size:13px; }}
</style>
</head>
<body>
<h1>Bet365 odds report</h1>
<div class="summary">
  <p><span class="badge">Sport: {html.escape(args.sport)}</span><span class="badge">Bookmaker: Bet365</span><span class="badge">Events: {len(event_rows)}</span><span class="badge">Market rows: {len(market_rows)}</span></p>
  <p class="small">Genereret: {html.escape(dk_time(iso_z(now_utc())))} dansk tid. Lookahead: {args.lookahead_days} dage. Maks events med odds: {args.max_price_events}.</p>
  <p class="small">Seneste rate-limit remaining: {html.escape(str(latest_header.get('x_ratelimit_remaining', '')))} / {html.escape(str(latest_header.get('x_ratelimit_limit', '')))}</p>
</div>
<div class="summary"><h2>Markeder fundet</h2><ul>{market_count_lines}</ul></div>
{''.join(cards) if cards else '<div class="card">Ingen Bet365 odds fundet.</div>'}
</body>
</html>""", encoding='utf-8')


def write_markdown(path, event_rows, market_rows, headers_log, args):
    market_counts = {}
    for row in market_rows:
        market_counts[row['market']] = market_counts.get(row['market'], 0) + 1
    lines = [
        '# Bet365 odds report',
        '',
        f'- Sport: **{args.sport}**',
        '- Bookmaker: **Bet365**',
        f'- Events med odds: **{len(event_rows)}**',
        f'- Markedsrækker: **{len(market_rows)}**',
        f'- Genereret: **{dk_time(iso_z(now_utc()))} dansk tid**',
        f'- Lookahead: **{args.lookahead_days} dage**',
        '',
        '## Markeder fundet',
        '',
    ]
    if market_counts:
        for name, count in sorted(market_counts.items(), key=lambda x: (-x[1], x[0]))[:50]:
            lines.append(f'- {name}: {count}')
    else:
        lines.append('- Ingen markeder fundet')
    lines.extend(['', '## Kampe', ''])
    by_event = {}
    for row in market_rows:
        by_event.setdefault(row['event_id'], []).append(row)
    for event in event_rows:
        lines.extend([
            f"### {event['home']} vs {event['away']}",
            f"- Kampstart: **{event['date_denmark']}**",
            f"- Liga: **{event['league']}**",
        ])
        for row in by_event.get(event['event_id'], [])[:20]:
            parts = []
            for label, key in [('H', 'home_odds'), ('X', 'draw_odds'), ('A', 'away_odds'), ('Over', 'over'), ('Under', 'under'), ('Yes', 'yes'), ('No', 'no')]:
                if row.get(key):
                    parts.append(f'{label}: {row[key]}')
            suffix = ' | '.join(parts) if parts else row.get('raw_odds', '')[:120]
            if row.get('label'):
                suffix = f"{row['label']}: {suffix}"
            lines.append(f"- **{row['market']}** - {suffix}")
        lines.append('')
    path.write_text('\n'.join(lines), encoding='utf-8')


def write_pdf(path, event_rows, market_rows, args):
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    except Exception as exc:
        path.with_suffix('.pdf_error.txt').write_text(f'ReportLab not available: {exc}', encoding='utf-8')
        return False

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=24, leftMargin=24, topMargin=24, bottomMargin=24)
    story = []
    story.append(Paragraph('Bet365 odds report', styles['Title']))
    story.append(Paragraph(f"Sport: {args.sport} | Events: {len(event_rows)} | Generated: {dk_time(iso_z(now_utc()))} DK time", styles['Normal']))
    story.append(Spacer(1, 12))

    market_counts = {}
    for row in market_rows:
        market_counts[row['market']] = market_counts.get(row['market'], 0) + 1
    story.append(Paragraph('Markets found', styles['Heading2']))
    data = [['Market', 'Rows']] + [[name, str(count)] for name, count in sorted(market_counts.items(), key=lambda x: (-x[1], x[0]))[:20]]
    table = Table(data, colWidths=[360, 70])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 0.25, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(table)
    story.append(Spacer(1, 12))

    by_event = {}
    for row in market_rows:
        by_event.setdefault(row['event_id'], []).append(row)
    for event in event_rows[:30]:
        story.append(Paragraph(f"{event['home']} vs {event['away']}", styles['Heading2']))
        story.append(Paragraph(f"Kickoff: {event['date_denmark']} | League: {event['league']}", styles['Normal']))
        rows = [['Market', 'Odds / outcomes']]
        for row in by_event.get(event['event_id'], [])[:10]:
            parts = []
            for label, key in [('H', 'home_odds'), ('X', 'draw_odds'), ('A', 'away_odds'), ('Over', 'over'), ('Under', 'under'), ('Yes', 'yes'), ('No', 'no')]:
                if row.get(key):
                    parts.append(f'{label}: {row[key]}')
            suffix = ' | '.join(parts) if parts else row.get('raw_odds', '')[:90]
            if row.get('label'):
                suffix = f"{row['label']}: {suffix}"
            rows.append([Paragraph(row['market'], styles['BodyText']), Paragraph(suffix, styles['BodyText'])])
        t = Table(rows, colWidths=[140, 290])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 0.25, colors.lightgrey),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        story.append(t)
        story.append(Spacer(1, 10))
    doc.build(story)
    return True


def main():
    parser = argparse.ArgumentParser(description='Build a manual Bet365 odds report from Odds-API.io')
    parser.add_argument('--sport', default=os.getenv('BET365_REPORT_SPORT', 'football'))
    parser.add_argument('--lookahead-days', type=int, default=int(os.getenv('BET365_REPORT_LOOKAHEAD_DAYS', '7')))
    parser.add_argument('--max-events', type=int, default=int(os.getenv('BET365_REPORT_MAX_EVENTS', '100')))
    parser.add_argument('--max-pages', type=int, default=int(os.getenv('BET365_REPORT_MAX_PAGES', '2')))
    parser.add_argument('--max-price-events', type=int, default=int(os.getenv('BET365_REPORT_MAX_PRICE_EVENTS', '30')))
    args = parser.parse_args()

    api_key = os.getenv('ODDS_API_IO_KEY')
    if not api_key:
        print('ODDS_API_IO_KEY is missing', file=sys.stderr)
        return 2

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    headers_log = []
    events = fetch_events(api_key, args.sport, args.lookahead_days, args.max_events, args.max_pages, headers_log)
    selected_events, odds_items = fetch_odds(api_key, events, args.max_price_events, headers_log)
    event_rows, market_rows = flatten_markets(odds_items)

    write_csv(OUTPUT_DIR / 'bet365_events.csv', event_rows)
    write_csv(OUTPUT_DIR / 'bet365_markets.csv', market_rows)
    write_csv(OUTPUT_DIR / 'bet365_rate_limit_headers.csv', headers_log)
    write_html(OUTPUT_DIR / 'bet365_odds_report.html', event_rows, market_rows, headers_log, args)
    write_markdown(OUTPUT_DIR / 'bet365_odds_report.md', event_rows, market_rows, headers_log, args)
    pdf_ok = write_pdf(OUTPUT_DIR / 'bet365_odds_report.pdf', event_rows, market_rows, args)

    summary = {
        'generated_at_utc': iso_z(now_utc()),
        'sport': args.sport,
        'bookmaker': BOOKMAKER,
        'events_discovered': len(events),
        'events_requested_for_odds': len(selected_events),
        'events_with_odds': len(event_rows),
        'market_rows': len(market_rows),
        'pdf_created': pdf_ok,
        'latest_rate_limit_remaining': headers_log[-1].get('x_ratelimit_remaining', '') if headers_log else '',
        'latest_rate_limit_limit': headers_log[-1].get('x_ratelimit_limit', '') if headers_log else '',
    }
    (OUTPUT_DIR / 'bet365_report_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
