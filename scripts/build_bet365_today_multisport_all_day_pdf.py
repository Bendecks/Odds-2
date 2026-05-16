import argparse
import csv
import json
import os
import time
from datetime import timedelta
from pathlib import Path

import build_bet365_today_multisport_good_options_report as base

OUTPUT_DIR = Path('output/bet365/latest')
RAW_DIR = Path('data/raw/odds_api_io/bet365_today_multisport_all_day_report')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
RAW_DIR.mkdir(parents=True, exist_ok=True)

ALL_DAY_STATUSES = 'pending,live,settled'
HOURS_AHEAD = 12


def upcoming_window():
    now = base.now_dk()
    end = now + timedelta(hours=HOURS_AHEAD)
    return now.strftime('%Y-%m-%d %H:%M'), now, end


def write_csv(path, rows):
    if not rows:
        path.write_text('', encoding='utf-8')
        return
    with path.open('w', newline='', encoding='utf-8') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def to_float(value):
    try:
        if value in (None, ''):
            return None
        return float(value)
    except Exception:
        return None


def first_float(*values):
    for value in values:
        parsed = to_float(value)
        if parsed is not None:
            return parsed
    return None


def classify_market(row):
    market = (row.get('market') or '').lower()
    if market in {'ml', 'moneyline', 'match winner', '3-way result', '1x2'} or 'winner' in market or 'result' in market:
        return 'match_result'
    if 'total' in market or 'over' in market or 'under' in market:
        return 'total'
    if 'handicap' in market or 'spread' in market:
        return 'handicap_or_spread'
    if 'both teams' in market or 'btts' in market:
        return 'both_teams_to_score'
    if 'corner' in market:
        return 'corners'
    if 'card' in market or 'booking' in market:
        return 'cards_or_bookings'
    if row.get('label'):
        return 'player_or_labelled_prop'
    return 'other'


def market_selection(row):
    if row.get('home_odds'):
        return 'home'
    if row.get('draw_odds'):
        return 'draw'
    if row.get('away_odds'):
        return 'away'
    if row.get('over'):
        return 'over'
    if row.get('under'):
        return 'under'
    if row.get('yes'):
        return 'yes'
    if row.get('no'):
        return 'no'
    return row.get('label') or 'unknown'


def decimal_odds(row):
    return first_float(row.get('home_odds'), row.get('draw_odds'), row.get('away_odds'), row.get('over'), row.get('under'), row.get('yes'), row.get('no'))


def implied_probability(odds):
    if not odds or odds <= 1:
        return None
    return round(1 / odds, 6)


def write_jsonl(path, markets):
    with path.open('w', encoding='utf-8') as handle:
        for row in markets:
            odds = decimal_odds(row)
            record = {
                'event_id': row.get('event_id'),
                'sport': row.get('sport'),
                'league': row.get('league'),
                'kickoff_denmark': row.get('date_denmark'),
                'home': row.get('home'),
                'away': row.get('away'),
                'bookmaker': row.get('bookmaker'),
                'market': row.get('market'),
                'market_type': classify_market(row),
                'selection': market_selection(row),
                'label': row.get('label'),
                'line': row.get('hdp'),
                'decimal_odds': odds,
                'implied_probability': implied_probability(odds),
                'home_odds': row.get('home_odds'),
                'draw_odds': row.get('draw_odds'),
                'away_odds': row.get('away_odds'),
                'over': row.get('over'),
                'under': row.get('under'),
                'yes': row.get('yes'),
                'no': row.get('no'),
                'updated_at': row.get('updated_at'),
                'raw_odds': row.get('raw_odds'),
            }
            handle.write(json.dumps(record, ensure_ascii=False, separators=(',', ':')) + '\n')


def write_events_json(path, events, markets):
    by_event = {}
    for event in events:
        by_event[event.get('event_id')] = {
            'event_id': event.get('event_id'),
            'sport': event.get('sport'),
            'league': event.get('league'),
            'kickoff_utc': event.get('date_utc'),
            'kickoff_denmark': event.get('date_denmark'),
            'home': event.get('home'),
            'away': event.get('away'),
            'status': event.get('status'),
            'markets': [],
        }
    for row in markets:
        event = by_event.setdefault(row.get('event_id'), {
            'event_id': row.get('event_id'),
            'sport': row.get('sport'),
            'league': row.get('league'),
            'kickoff_denmark': row.get('date_denmark'),
            'home': row.get('home'),
            'away': row.get('away'),
            'status': '',
            'markets': [],
        })
        odds = decimal_odds(row)
        event['markets'].append({
            'market': row.get('market'),
            'market_type': classify_market(row),
            'selection': market_selection(row),
            'label': row.get('label'),
            'line': row.get('hdp'),
            'decimal_odds': odds,
            'implied_probability': implied_probability(odds),
            'home_odds': row.get('home_odds'),
            'draw_odds': row.get('draw_odds'),
            'away_odds': row.get('away_odds'),
            'over': row.get('over'),
            'under': row.get('under'),
            'yes': row.get('yes'),
            'no': row.get('no'),
            'updated_at': row.get('updated_at'),
            'raw_odds': row.get('raw_odds'),
        })
    path.write_text(json.dumps(list(by_event.values()), ensure_ascii=False, indent=2), encoding='utf-8')


def fetch_all_day_events_for_sport(api_key, sport_slug, max_events, max_pages, min_bookmaker_count, headers_log):
    report_date, start, end = upcoming_window()
    kept, excluded = [], []
    seen = set()
    for page in range(max_pages):
        params = {
            'apiKey': api_key,
            'sport': sport_slug,
            'status': ALL_DAY_STATUSES,
            'bookmaker': base.BOOKMAKER,
            'from': base.iso_z(start),
            'to': base.iso_z(end),
            'limit': max_events,
            'skip': page * max_events,
        }
        payload, error = base.request_json(f'{base.BASE_URL}/events', params, f'{sport_slug}_all_day_events_page_{page + 1}', headers_log)
        if error or payload is None:
            excluded.append({'sport_query': sport_slug, 'reason': error, 'event_id': '', 'date_denmark': '', 'home': '', 'away': '', 'league': '', 'bookmaker_count': '', 'status': ''})
            break
        rows = base.event_items(payload)
        for event in rows:
            eid = base.event_id(event)
            if not eid or eid in seen:
                continue
            seen.add(eid)
            row = {
                'sport_query': sport_slug,
                'event_id': eid,
                'date_denmark': base.dk_time(base.event_date(event)),
                'home': base.team(event, 'home'),
                'away': base.team(event, 'away'),
                'league': base.league(event),
                'sport': base.sport_name(event),
                'bookmaker_count': base.bookmaker_count(event),
                'status': base.safe(event.get('status')),
            }
            if base.is_excluded_event(event):
                row['reason'] = 'excluded_youth_reserve_friendly_or_exhibition'
                excluded.append(row)
            elif base.is_good_competition(event, min_bookmaker_count):
                kept.append(event)
            else:
                row['reason'] = 'not_good_competition_or_low_coverage'
                excluded.append(row)
        if len(rows) < max_events:
            break
    return report_date, kept, excluded


def write_all_day_pdf(path, report_date, events, markets, args, excluded_count):
    try:
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    except Exception as exc:
        path.with_suffix('.pdf_error.txt').write_text(f'ReportLab not available: {exc}', encoding='utf-8')
        return False
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    by_event, market_counts, sport_counts = base.summarize(events, markets)
    status_counts = {}
    for event in events:
        status = event.get('status') or 'unknown'
        status_counts[status] = status_counts.get(status, 0) + 1
    story = [Paragraph('Bet365 multisport - kommende 12 timer', styles['Title']), Paragraph(f'Vindue startet: {report_date} | Events i PDF: {len(events)} | Markedsraekker i CSV: {len(markets)} | Frasorteret: {excluded_count}', styles['Normal']), Paragraph(f'Statusser hentet: {ALL_DAY_STATUSES}. Kommende {HOURS_AHEAD} timer. Separat PDF setup.', styles['Normal']), Spacer(1, 10)]
    if status_counts:
        story.append(Paragraph('Statusfordeling', styles['Heading2']))
        data = [['Status', 'Events']] + [[k, str(v)] for k, v in sorted(status_counts.items(), key=lambda x: (-x[1], x[0]))]
        table = Table(data, colWidths=[320, 80])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey), ('GRID', (0, 0), (-1, -1), 0.25, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
        story.extend([table, Spacer(1, 10)])
    if sport_counts:
        story.append(Paragraph('Sportsgrene', styles['Heading2']))
        data = [['Sport', 'Events']] + [[k, str(v)] for k, v in sorted(sport_counts.items(), key=lambda x: (-x[1], x[0]))]
        table = Table(data, colWidths=[320, 80])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey), ('GRID', (0, 0), (-1, -1), 0.25, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
        story.extend([table, Spacer(1, 10)])
    if market_counts:
        story.append(Paragraph('Markeder fundet', styles['Heading2']))
        data = [['Marked', 'Raekker']] + [[k, str(v)] for k, v in sorted(market_counts.items(), key=lambda x: (-x[1], x[0]))[:60]]
        table = Table(data, colWidths=[330, 80])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey), ('GRID', (0, 0), (-1, -1), 0.25, colors.grey), ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
        story.extend([table, Spacer(1, 10), PageBreak()])
    sorted_events = sorted(events, key=lambda e: (e.get('date_denmark', ''), e.get('sport', ''), e.get('league', ''), e.get('home', '')))
    current_sport = None
    for event in sorted_events:
        sport = event.get('sport') or 'unknown'
        if sport != current_sport:
            current_sport = sport
            story.append(Paragraph(str(sport), styles['Heading1']))
        status = event.get('status') or 'unknown'
        story.append(Paragraph(f"{event.get('home', '')} vs {event.get('away', '')}", styles['Heading2']))
        story.append(Paragraph(f"{event.get('date_denmark', '')} | {status} | {event.get('league', '')}", styles['Normal']))
        rows = [['Marked', 'Odds / outcomes']]
        event_markets = by_event.get(event['event_id'], [])
        for row in event_markets[:30]:
            rows.append([Paragraph(row['market'], styles['BodyText']), Paragraph(base.outcome_line(row), styles['BodyText'])])
        if len(event_markets) > 30:
            rows.append([Paragraph('Flere markeder', styles['BodyText']), Paragraph(f'{len(event_markets) - 30} ekstra markedsraekker findes i CSV-filen', styles['BodyText'])])
        table = Table(rows, colWidths=[140, 290])
        table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.whitesmoke), ('GRID', (0, 0), (-1, -1), 0.25, colors.lightgrey), ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
        story.extend([table, Spacer(1, 9)])
    doc.build(story)
    return True


def main():
    parser = argparse.ArgumentParser(description='Build separate upcoming 12 hour Bet365 multisport PDF report')
    parser.add_argument('--sports', default=os.getenv('BET365_ALL_DAY_SPORTS', ','.join(base.DEFAULT_SPORTS)))
    parser.add_argument('--max-events', type=int, default=int(os.getenv('BET365_ALL_DAY_MAX_EVENTS', '100')))
    parser.add_argument('--max-pages', type=int, default=int(os.getenv('BET365_ALL_DAY_MAX_PAGES', '10')))
    parser.add_argument('--max-price-events-per-sport', type=int, default=int(os.getenv('BET365_ALL_DAY_MAX_PRICE_EVENTS_PER_SPORT', '200')))
    parser.add_argument('--min-bookmaker-count', type=int, default=int(os.getenv('BET365_ALL_DAY_MIN_BOOKMAKER_COUNT', '10')))
    args = parser.parse_args()
    args.sports = [s.strip() for s in args.sports.split(',') if s.strip()]
    api_key = os.getenv('ODDS_API_IO_KEY')
    if not api_key:
        raise SystemExit('ODDS_API_IO_KEY is missing')
    headers_log = []
    all_events, all_excluded = [], []
    report_date = upcoming_window()[0]
    base.RAW_DIR = RAW_DIR
    for sport_slug in args.sports:
        report_date, kept, excluded = fetch_all_day_events_for_sport(api_key, sport_slug, args.max_events, args.max_pages, args.min_bookmaker_count, headers_log)
        for event in kept:
            event['_sport_query'] = sport_slug
        all_events.extend(kept)
        all_excluded.extend(excluded)
        time.sleep(0.1)
    all_events.sort(key=lambda e: (base.event_date(e), base.sport_name(e), base.league(e)))
    selected, odds_payloads = base.fetch_odds(api_key, all_events, args.max_price_events_per_sport, headers_log)
    events, markets = base.flatten(odds_payloads)
    write_csv(OUTPUT_DIR / 'bet365_today_multisport_all_day_events.csv', events)
    write_csv(OUTPUT_DIR / 'bet365_today_multisport_all_day_markets.csv', markets)
    write_csv(OUTPUT_DIR / 'bet365_today_multisport_all_day_excluded.csv', all_excluded)
    write_csv(OUTPUT_DIR / 'bet365_today_multisport_all_day_rate_limit_headers.csv', headers_log)
    write_jsonl(OUTPUT_DIR / 'bet365_today_multisport_all_day_markets.jsonl', markets)
    write_events_json(OUTPUT_DIR / 'bet365_today_multisport_all_day_events.json', events, markets)
    pdf_ok = write_all_day_pdf(OUTPUT_DIR / 'bet365_today_multisport_all_day_report.pdf', report_date, events, markets, args, len(all_excluded))
    status_counts = {}
    for event in events:
        status = event.get('status') or 'unknown'
        status_counts[status] = status_counts.get(status, 0) + 1
    summary = {
        'generated_at_dk': base.now_dk().strftime('%Y-%m-%d %H:%M'),
        'window_hours': HOURS_AHEAD,
        'window_started_dk': report_date,
        'bookmaker': base.BOOKMAKER,
        'statuses_requested': ALL_DAY_STATUSES,
        'sports_requested': ','.join(args.sports),
        'events_after_filters': len(all_events),
        'events_requested_for_odds': len(selected),
        'events_with_odds': len(events),
        'event_status_counts': status_counts,
        'market_rows': len(markets),
        'excluded_events': len(all_excluded),
        'min_bookmaker_count': args.min_bookmaker_count,
        'max_pages': args.max_pages,
        'max_price_events_per_sport': args.max_price_events_per_sport,
        'primary_ai_file': 'bet365_today_multisport_all_day_markets.jsonl',
        'secondary_ai_file': 'bet365_today_multisport_all_day_events.json',
        'csv_backup_file': 'bet365_today_multisport_all_day_markets.csv',
        'pdf_created': pdf_ok,
        'latest_rate_limit_remaining': headers_log[-1].get('x_ratelimit_remaining', '') if headers_log else '',
        'latest_rate_limit_limit': headers_log[-1].get('x_ratelimit_limit', '') if headers_log else '',
    }
    (OUTPUT_DIR / 'bet365_today_multisport_all_day_summary.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(summary, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
