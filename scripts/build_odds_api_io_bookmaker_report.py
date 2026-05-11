import json
import os
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
raw_dir = Path('data/raw/odds_api_io')
output_dir.mkdir(parents=True, exist_ok=True)
raw_dir.mkdir(parents=True, exist_ok=True)

base_url = 'https://api.odds-api.io/v3'
api_key = os.getenv('ODDS_API_IO_KEY')
configured_bookmakers = [
    item.strip()
    for item in os.getenv('ODDS_API_IO_BOOKMAKERS', 'Bet365,1xbet').split(',')
    if item.strip()
]
extra_watchlist = ['Bet365', 'Unibet', 'SingBet', 'Pinnacle', 'Betfair', '1xbet', '1xBet', '1XBet']
watchlist = []
for name in configured_bookmakers + extra_watchlist:
    if name.lower() not in {item.lower() for item in watchlist}:
        watchlist.append(name)

calls_used = 0
errors = []
rate_rows = []


def record_headers(label: str, status_code, headers):
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


def get_json(url: str, label: str, authenticated: bool = False):
    global calls_used
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            if authenticated:
                calls_used += 1
            record_headers(label, response.status, response.headers)
            text = response.read().decode('utf-8')
            (raw_dir / f'{label}_latest.json').write_text(text, encoding='utf-8')
            return json.loads(text)
    except urllib.error.HTTPError as exc:
        if authenticated:
            calls_used += 1
        record_headers(label, exc.code, exc.headers)
        body = exc.read().decode('utf-8', errors='replace')
        (raw_dir / f'{label}_error.txt').write_text(body, encoding='utf-8')
        errors.append({'stage': label, 'error': f'HTTP {exc.code}: {body[:300]}'})
        return None
    except Exception as exc:
        errors.append({'stage': label, 'error': repr(exc)})
        return None


bookmakers_payload = get_json(f'{base_url}/bookmakers', 'bookmakers', authenticated=False)
selected_payload = None
if api_key:
    selected_url = f'{base_url}/bookmakers/selected?' + urllib.parse.urlencode({'apiKey': api_key})
    selected_payload = get_json(selected_url, 'bookmakers_selected', authenticated=True)
else:
    errors.append({'stage': 'config', 'error': 'ODDS_API_IO_KEY missing; selected bookmakers not fetched'})

bookmaker_rows = []
if isinstance(bookmakers_payload, list):
    for item in bookmakers_payload:
        if isinstance(item, dict):
            bookmaker_rows.append({
                'name': item.get('name'),
                'active': item.get('active'),
                'source': 'all_bookmakers',
            })
bookmakers_df = pd.DataFrame(bookmaker_rows)
for col in ['name', 'active', 'source']:
    if col not in bookmakers_df.columns:
        bookmakers_df[col] = None
bookmakers_df = bookmakers_df[['name', 'active', 'source']]
bookmakers_df.to_csv(output_dir / 'odds_api_io_bookmakers.csv', index=False)

selected_rows = []
if isinstance(selected_payload, dict):
    if isinstance(selected_payload.get('bookmakers'), list):
        for item in selected_payload.get('bookmakers'):
            selected_rows.append({'name': item if not isinstance(item, dict) else item.get('name'), 'raw': json.dumps(item)})
    else:
        for key, value in selected_payload.items():
            if isinstance(value, list):
                for item in value:
                    selected_rows.append({'name': item if not isinstance(item, dict) else item.get('name'), 'raw': json.dumps(item)})
            elif isinstance(value, (str, int, float, bool)):
                selected_rows.append({'name': key if isinstance(value, bool) else value, 'raw': json.dumps({key: value})})
elif isinstance(selected_payload, list):
    for item in selected_payload:
        selected_rows.append({'name': item if not isinstance(item, dict) else item.get('name'), 'raw': json.dumps(item)})
selected_df = pd.DataFrame(selected_rows)
for col in ['name', 'raw']:
    if col not in selected_df.columns:
        selected_df[col] = None
selected_df = selected_df[['name', 'raw']]
selected_df.to_csv(output_dir / 'odds_api_io_selected_bookmakers.csv', index=False)

available_names = bookmakers_df['name'].dropna().astype(str).tolist() if len(bookmakers_df) else []
available_lower = {name.lower(): name for name in available_names}
active_by_lower = {
    str(row.get('name')).lower(): row.get('active')
    for _, row in bookmakers_df.iterrows()
    if pd.notna(row.get('name'))
}

watch_rows = []
for requested in watchlist:
    exact_name = available_lower.get(requested.lower())
    watch_rows.append({
        'requested_name': requested,
        'found': exact_name is not None,
        'canonical_name': exact_name,
        'active': active_by_lower.get(requested.lower()),
        'is_configured': requested.lower() in {item.lower() for item in configured_bookmakers},
    })
watch_df = pd.DataFrame(watch_rows)
watch_df.to_csv(output_dir / 'odds_api_io_bookmaker_watchlist.csv', index=False)

rate_df = pd.DataFrame(rate_rows)
rate_df.to_csv(output_dir / 'odds_api_io_bookmaker_rate_limit_headers.csv', index=False)

configured_found = int(watch_df.loc[watch_df['is_configured'], 'found'].sum()) if len(watch_df) else 0
configured_total = int(watch_df['is_configured'].sum()) if len(watch_df) else 0
active_total = int(bookmakers_df['active'].fillna(False).astype(bool).sum()) if len(bookmakers_df) and 'active' in bookmakers_df.columns else 0
latest_rate = rate_rows[-1] if rate_rows else {}
summary = {
    'generated_at_utc': datetime.now(timezone.utc).isoformat(),
    'all_bookmaker_rows': int(len(bookmakers_df)),
    'active_bookmaker_rows': active_total,
    'selected_bookmaker_rows': int(len(selected_df)),
    'configured_bookmakers': ', '.join(configured_bookmakers),
    'configured_bookmakers_found': configured_found,
    'configured_bookmakers_total': configured_total,
    'watchlist_rows': int(len(watch_df)),
    'authenticated_calls_used': calls_used,
    'errors': int(len(errors)),
    'latest_rate_limit_limit': latest_rate.get('x_ratelimit_limit'),
    'latest_rate_limit_remaining': latest_rate.get('x_ratelimit_remaining'),
    'latest_rate_limit_reset': latest_rate.get('x_ratelimit_reset'),
}
pd.DataFrame([summary]).to_csv(output_dir / 'odds_api_io_bookmaker_summary.csv', index=False)

markdown = [
    '# Odds-API.io Bookmaker Diagnostics',
    '',
    'Diagnostics for exact bookmaker names and selected bookmaker state.',
    'This is not a betting signal and does not affect real-money readiness.',
    '',
    f"Generated UTC: {summary['generated_at_utc']}",
    f"All bookmaker rows: {summary['all_bookmaker_rows']}",
    f"Active bookmaker rows: {summary['active_bookmaker_rows']}",
    f"Selected bookmaker rows: {summary['selected_bookmaker_rows']}",
    f"Configured bookmakers: {summary['configured_bookmakers']}",
    f"Configured bookmakers found: {summary['configured_bookmakers_found']} / {summary['configured_bookmakers_total']}",
    f"Authenticated calls used: {summary['authenticated_calls_used']}",
    f"Errors/status rows: {summary['errors']}",
    '',
    '## Provider rate-limit headers',
    '',
    f"Latest x-ratelimit-limit: {summary['latest_rate_limit_limit']}",
    f"Latest x-ratelimit-remaining: {summary['latest_rate_limit_remaining']}",
    f"Latest x-ratelimit-reset: {summary['latest_rate_limit_reset']}",
    '',
    '## Watchlist',
    '',
]
for _, row in watch_df.iterrows():
    markdown.append(
        f"- requested={row['requested_name']} | found={row['found']} | canonical={row['canonical_name']} | active={row['active']} | configured={row['is_configured']}"
    )

if len(selected_df):
    markdown.extend(['', '## Selected bookmakers', ''])
    for _, row in selected_df.head(50).iterrows():
        markdown.append(f"- {row['name']}")

if errors:
    markdown.extend(['', '## Errors / Status', ''])
    for error in errors[:20]:
        markdown.append(f"- {error['stage']}: {error['error']}")

(output_dir / 'odds_api_io_bookmaker_report.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
