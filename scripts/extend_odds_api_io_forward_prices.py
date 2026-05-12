import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
raw_dir = Path('data/raw/odds_api_io')
raw_dir.mkdir(parents=True, exist_ok=True)

api_key = os.getenv('ODDS_API_IO_KEY')
base_url = 'https://api.odds-api.io/v3'
bookmakers = os.getenv('ODDS_API_IO_BOOKMAKERS', 'Bet365,1xbet').strip()
max_total_price_events = int(os.getenv('ODDS_API_IO_MAX_PRICE_EVENTS', '30'))
extra_max_calls = int(os.getenv('ODDS_API_IO_EXTRA_MULTI_CALLS', '3'))
min_direct_match_confidence = float(os.getenv('ODDS_API_IO_MIN_DIRECT_PRICE_MATCH_CONFIDENCE', '0.72'))

predictions_path = output_dir / 'forward_fixture_predictions.csv'
fixtures_path = output_dir / 'odds_api_io_forward_fixtures.csv'
prices_path = output_dir / 'odds_api_io_forward_prices.csv'
rate_path = output_dir / 'odds_api_io_extra_rate_limit_headers.csv'
summary_path = output_dir / 'odds_api_io_extra_batches_summary.csv'
report_path = output_dir / 'odds_api_io_extra_batches_report.md'

price_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'source_name', 'source_type', 'market_home_odds', 'market_draw_odds',
    'market_away_odds', 'price_captured_at_utc', 'source_quality', 'raw_source_url'
]

calls_used = 0
rate_rows = []
errors = []
selected_rows = []
new_rows = []
fetched_at = datetime.now(timezone.utc).isoformat()


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def norm_team(value) -> str:
    text = str(value or '').lower().strip()
    for token in ['hotspur', 'united', 'utd', 'town', 'city', 'fc', 'afc', 'cf', 'sc', 'sl', '.', ',', '&']:
        text = text.replace(token, ' ')
    return ' '.join(text.split())


def similarity(a, b) -> float:
    left = norm_team(a)
    right = norm_team(b)
    if not left or not right:
        return 0.0
    if left == right:
        return 1.0
    if left in right or right in left:
        return 0.92
    return SequenceMatcher(None, left, right).ratio()


def direct_confidence(pred, event) -> float:
    return round((similarity(pred.get('home_team'), event.get('home_team')) + similarity(pred.get('away_team'), event.get('away_team'))) / 2, 4)


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', utc=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(value, errors='coerce')
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def event_id_from_fixture_id(value):
    text = str(value or '')
    return text.replace('odds_api_io_', '') if text.startswith('odds_api_io_') else text


def record_headers(label, status_code, headers):
    row = {
        'captured_at_utc': datetime.now(timezone.utc).isoformat(),
        'label': label,
        'status_code': status_code,
        'x_ratelimit_limit': headers.get('x-ratelimit-limit') if headers else None,
        'x_ratelimit_remaining': headers.get('x-ratelimit-remaining') if headers else None,
        'x_ratelimit_reset': headers.get('x-ratelimit-reset') if headers else None,
        'retry_after': headers.get('retry-after') if headers else None,
    }
    rate_rows.append(row)
    (raw_dir / f'{label}_headers_latest.json').write_text(json.dumps(row, indent=2), encoding='utf-8')


def get_json(url, label):
    global calls_used
    if calls_used >= extra_max_calls:
        raise RuntimeError('ODDS_API_IO_EXTRA_MULTI_CALLS reached')
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            calls_used += 1
            record_headers(label, response.status, response.headers)
            text = response.read().decode('utf-8')
            (raw_dir / f'{label}_latest.json').write_text(text, encoding='utf-8')
            return json.loads(text)
    except urllib.error.HTTPError as exc:
        calls_used += 1
        record_headers(label, exc.code, exc.headers)
        body = exc.read().decode('utf-8', errors='replace')
        (raw_dir / f'{label}_error.txt').write_text(body, encoding='utf-8')
        raise RuntimeError(f'HTTP {exc.code}: {body[:300]}')


def number(value):
    parsed = pd.to_numeric(value, errors='coerce')
    if pd.isna(parsed):
        return None
    return float(parsed)


def market_is_match_winner(name):
    text = str(name or '').strip().lower()
    return text in {'ml', 'moneyline', 'match winner', 'match_winner', 'full time result', 'fulltime result', '1x2', '3-way result'}


def odds_response_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        if 'bookmakers' in payload and 'id' in payload:
            return [payload]
        for key in ['events', 'data', 'results', 'odds']:
            if isinstance(payload.get(key), list):
                return payload.get(key)
        values = [v for v in payload.values() if isinstance(v, dict) and 'bookmakers' in v]
        if values:
            return values
    return []


def extract_three_way_odds(odds_payload):
    bookmaker_payload = odds_payload.get('bookmakers') if isinstance(odds_payload, dict) else None
    if not isinstance(bookmaker_payload, dict):
        return None, None, None, None, None
    requested = [item.strip().lower() for item in bookmakers.split(',') if item.strip()]
    ordered_bookmakers = []
    for wanted in requested:
        ordered_bookmakers.extend([name for name in bookmaker_payload.keys() if str(name).lower() == wanted])
    ordered_bookmakers.extend([name for name in bookmaker_payload.keys() if name not in ordered_bookmakers])

    for bookmaker_name in ordered_bookmakers:
        markets = bookmaker_payload.get(bookmaker_name) or []
        if not isinstance(markets, list):
            continue
        preferred_markets = [m for m in markets if market_is_match_winner(m.get('name'))]
        preferred_markets.extend([m for m in markets if m not in preferred_markets])
        for market in preferred_markets:
            odds_items = market.get('odds') or []
            if isinstance(odds_items, dict):
                odds_items = [odds_items]
            for odds_item in odds_items:
                if not isinstance(odds_item, dict):
                    continue
                h = number(odds_item.get('home'))
                d = number(odds_item.get('draw'))
                a = number(odds_item.get('away'))
                if h and d and a and min(h, d, a) > 1:
                    return h, d, a, bookmaker_name, market.get('name')
    return None, None, None, None, None


def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]

predictions = safe_read_csv(predictions_path)
fixtures = safe_read_csv(fixtures_path)
existing_prices = safe_read_csv(prices_path)
for col in price_columns:
    if col not in existing_prices.columns:
        existing_prices[col] = None
existing_prices = existing_prices[price_columns] if len(existing_prices) else pd.DataFrame(columns=price_columns)

if not api_key:
    errors.append({'stage': 'config', 'error': 'ODDS_API_IO_KEY missing'})
elif not len(predictions) or not len(fixtures):
    errors.append({'stage': 'input', 'error': 'Missing predictions or odds-api.io fixtures'})
else:
    predictions = predictions.copy()
    fixtures = fixtures.copy()
    predictions['parsed_match_date'] = predictions.get('match_date', '').apply(parse_date)
    fixtures['parsed_match_date'] = fixtures.get('match_date', '').apply(parse_date)

    already_event_ids = set(existing_prices.get('fixture_id', pd.Series(dtype=str)).astype(str).str.replace('odds_api_io_', '', regex=False).tolist())
    selected_event_ids = set()
    for _, pred in predictions.iterrows():
        if len(already_event_ids) + len(selected_rows) >= max_total_price_events:
            break
        pred_date = pred.get('parsed_match_date')
        if not pred_date:
            continue
        candidates = fixtures[fixtures['parsed_match_date'] == pred_date].copy()
        if not len(candidates):
            continue
        best = None
        best_score = 0.0
        for _, event in candidates.iterrows():
            event_id = event_id_from_fixture_id(event.get('fixture_id'))
            if event_id in already_event_ids or event_id in selected_event_ids:
                continue
            score = direct_confidence(pred, event)
            if score > best_score:
                best = event
                best_score = score
        if best is not None and best_score >= min_direct_match_confidence:
            event_id = event_id_from_fixture_id(best.get('fixture_id'))
            selected_event_ids.add(event_id)
            selected_rows.append({
                'raw_event_id': event_id,
                'fixture_id': best.get('fixture_id'),
                'match_date': best.get('match_date'),
                'match_time': best.get('match_time'),
                'home_team': best.get('home_team'),
                'away_team': best.get('away_team'),
                'league': best.get('league'),
                'direct_match_confidence': best_score,
            })

    for batch_no, batch in enumerate(chunks(selected_rows, 10), start=1):
        if calls_used >= extra_max_calls:
            break
        event_ids = ','.join([str(item['raw_event_id']) for item in batch])
        params = {'apiKey': api_key, 'eventIds': event_ids, 'bookmakers': bookmakers}
        url = f'{base_url}/odds/multi?' + urllib.parse.urlencode(params)
        try:
            payload = get_json(url, f'odds_multi_extra_{batch_no}')
            items = odds_response_items(payload)
            odds_by_id = {str(item.get('id') or item.get('eventId') or item.get('event_id')): item for item in items if isinstance(item, dict)}
            for meta in batch:
                odds_payload = odds_by_id.get(str(meta['raw_event_id']))
                if odds_payload is None:
                    errors.append({'stage': 'extra_multi_odds_match', 'error': f'No odds payload matched event {meta["raw_event_id"]}'})
                    continue
                h, d, a, bookmaker, market = extract_three_way_odds(odds_payload)
                if h:
                    new_rows.append({
                        'fixture_id': meta.get('fixture_id'),
                        'match_date': meta.get('match_date'),
                        'match_time': meta.get('match_time'),
                        'home_team': meta.get('home_team'),
                        'away_team': meta.get('away_team'),
                        'league': meta.get('league'),
                        'source_name': f'odds_api_io_{bookmaker}_{market}',
                        'source_type': 'free_api_market_proxy',
                        'market_home_odds': round(h, 4),
                        'market_draw_odds': round(d, 4),
                        'market_away_odds': round(a, 4),
                        'price_captured_at_utc': fetched_at,
                        'source_quality': 'free_api_market_proxy_extra_multi_event_call',
                        'raw_source_url': 'https://api.odds-api.io/v3/odds/multi',
                    })
                else:
                    errors.append({'stage': 'extra_odds_parse', 'error': f'No 1X2 odds found for event {meta["raw_event_id"]}'})
        except Exception as exc:
            errors.append({'stage': 'extra_multi_odds_request_or_parse', 'error': repr(exc)})
            break

new_prices = pd.DataFrame(new_rows)
for col in price_columns:
    if col not in new_prices.columns:
        new_prices[col] = None
new_prices = new_prices[price_columns] if len(new_prices) else pd.DataFrame(columns=price_columns)
combined = pd.concat([existing_prices, new_prices], ignore_index=True)
if len(combined):
    combined = combined.drop_duplicates(['fixture_id', 'source_name'], keep='first')
combined.to_csv(prices_path, index=False)
combined.to_csv(raw_dir / 'odds_api_io_forward_prices_extended.csv', index=False)

pd.DataFrame(rate_rows).to_csv(rate_path, index=False)
pd.DataFrame(selected_rows).to_csv(output_dir / 'odds_api_io_extra_selected_events.csv', index=False)
latest_rate = rate_rows[-1] if rate_rows else {}
summary = {
    'existing_price_rows_before_extra': int(len(existing_prices)),
    'extra_selected_event_rows': int(len(selected_rows)),
    'extra_price_rows': int(len(new_prices)),
    'combined_price_rows': int(len(combined)),
    'extra_calls_used': calls_used,
    'extra_max_calls': extra_max_calls,
    'max_total_price_events': max_total_price_events,
    'min_direct_match_confidence': min_direct_match_confidence,
    'latest_rate_limit_remaining': latest_rate.get('x_ratelimit_remaining'),
    'errors': int(len(errors)),
}
pd.DataFrame([summary]).to_csv(summary_path, index=False)

markdown = [
    '# Odds-API.io Extra Multi-Odds Batches',
    '',
    'Adds extra /odds/multi calls after the primary fetch, using already discovered bookmaker-filtered events.',
    'Only direct home/away/date matches are selected. Swapped matches are not selected here.',
    '',
    f"Existing price rows before extra: {summary['existing_price_rows_before_extra']}",
    f"Extra selected event rows: {summary['extra_selected_event_rows']}",
    f"Extra price rows: {summary['extra_price_rows']}",
    f"Combined price rows: {summary['combined_price_rows']}",
    f"Extra calls used: {summary['extra_calls_used']} / {summary['extra_max_calls']}",
    f"Max total price events: {summary['max_total_price_events']}",
    f"Minimum direct match confidence: {summary['min_direct_match_confidence']}",
    f"Latest rate-limit remaining: {summary['latest_rate_limit_remaining']}",
    f"Errors/status rows: {summary['errors']}",
    '',
]
if len(new_prices):
    markdown.append('## New extra prices')
    markdown.append('')
    for _, row in new_prices.head(30).iterrows():
        markdown.append(f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | {row['source_name']} | {row['market_home_odds']}/{row['market_draw_odds']}/{row['market_away_odds']}")
if errors:
    markdown.extend(['', '## Errors / Status', ''])
    for error in errors[:20]:
        markdown.append(f"- {error['stage']}: {error['error']}")
report_path.write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
