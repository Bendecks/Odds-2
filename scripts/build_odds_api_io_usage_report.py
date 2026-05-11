import os
from datetime import datetime, timezone, timedelta
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
history_dir = Path('output/history')
history_dir.mkdir(parents=True, exist_ok=True)

status_path = output_dir / 'odds_api_io_forward_price_status.csv'
headers_path = output_dir / 'odds_api_io_rate_limit_headers.csv'
usage_log_path = history_dir / 'odds_api_io_usage_log.csv'


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


status = safe_read_csv(status_path)
headers = safe_read_csv(headers_path)
log = safe_read_csv(usage_log_path)
now = datetime.now(timezone.utc)
run_number = os.getenv('GITHUB_RUN_NUMBER', 'local')
run_attempt = os.getenv('GITHUB_RUN_ATTEMPT', 'local')
run_id = os.getenv('GITHUB_RUN_ID', 'local')
sha = os.getenv('GITHUB_SHA', 'local')

latest_header = headers.iloc[-1].to_dict() if len(headers) else {}

new_row = None
if len(status):
    row = status.iloc[0].to_dict()
    new_row = {
        'recorded_at_utc': now.isoformat(),
        'github_run_number': run_number,
        'github_run_attempt': run_attempt,
        'github_run_id': run_id,
        'github_sha': sha,
        'enabled': row.get('enabled'),
        'calls_used': int(pd.to_numeric(row.get('calls_used'), errors='coerce') or 0),
        'max_calls': int(pd.to_numeric(row.get('max_calls'), errors='coerce') or 0),
        'max_events': int(pd.to_numeric(row.get('max_events'), errors='coerce') or 0),
        'max_price_events': int(pd.to_numeric(row.get('max_price_events'), errors='coerce') or 0),
        'discovery_mode': row.get('discovery_mode'),
        'query_source': row.get('query_source'),
        'search_queries_used': row.get('search_queries_used'),
        'selected_event_rows': int(pd.to_numeric(row.get('selected_event_rows'), errors='coerce') or 0),
        'priced_event_rows': int(pd.to_numeric(row.get('priced_event_rows'), errors='coerce') or 0),
        'price_rows': int(pd.to_numeric(row.get('price_rows'), errors='coerce') or 0),
        'errors': int(pd.to_numeric(row.get('errors'), errors='coerce') or 0),
        'odds_endpoint_mode': row.get('odds_endpoint_mode'),
        'selected_bookmakers': row.get('selected_bookmakers'),
        'selected_markets': row.get('selected_markets'),
        'provider_rate_limit_limit': row.get('latest_rate_limit_limit') or latest_header.get('x_ratelimit_limit'),
        'provider_rate_limit_remaining': row.get('latest_rate_limit_remaining') or latest_header.get('x_ratelimit_remaining'),
        'provider_rate_limit_reset': row.get('latest_rate_limit_reset') or latest_header.get('x_ratelimit_reset'),
        'provider_retry_after': row.get('latest_retry_after') or latest_header.get('retry_after'),
    }

if new_row is not None:
    new_df = pd.DataFrame([new_row])
    if len(log):
        key_cols = ['github_run_number', 'github_run_attempt', 'github_sha']
        for col in key_cols:
            if col not in log.columns:
                log[col] = None
        mask = pd.Series([False] * len(log))
        if all(col in log.columns for col in key_cols):
            mask = (
                (log['github_run_number'].astype(str) == str(new_row['github_run_number']))
                & (log['github_run_attempt'].astype(str) == str(new_row['github_run_attempt']))
                & (log['github_sha'].astype(str) == str(new_row['github_sha']))
            )
        log = log[~mask]
        log = pd.concat([log, new_df], ignore_index=True)
    else:
        log = new_df

if len(log):
    log['recorded_at_utc_parsed'] = pd.to_datetime(log['recorded_at_utc'], errors='coerce', utc=True)
    log['calls_used'] = pd.to_numeric(log['calls_used'], errors='coerce').fillna(0)
    log = log.dropna(subset=['recorded_at_utc_parsed']).sort_values('recorded_at_utc_parsed')
else:
    log['recorded_at_utc_parsed'] = []

export_log = log.drop(columns=['recorded_at_utc_parsed'], errors='ignore')
export_log.to_csv(usage_log_path, index=False)
export_log.to_csv(output_dir / 'odds_api_io_usage_log_latest.csv', index=False)

windows = [1, 6, 12, 24, 72, 168]
summary_rows = []
for hours in windows:
    if len(log):
        cutoff = now - timedelta(hours=hours)
        window = log[log['recorded_at_utc_parsed'] >= cutoff].copy()
        calls = float(window['calls_used'].sum()) if len(window) else 0.0
        runs = int(len(window))
    else:
        calls = 0.0
        runs = 0
    summary_rows.append({
        'window_hours': hours,
        'runs': runs,
        'calls_used': int(calls),
        'avg_requests_per_hour_from_repo_runs': round(calls / hours, 4),
    })
summary_df = pd.DataFrame(summary_rows)
summary_df.to_csv(output_dir / 'odds_api_io_usage_summary.csv', index=False)

latest_calls = int(new_row['calls_used']) if new_row is not None else 0
latest_max_calls = int(new_row['max_calls']) if new_row is not None else 0
latest_endpoint_mode = new_row.get('odds_endpoint_mode') if new_row is not None else None
latest_queries = new_row.get('search_queries_used') if new_row is not None else None
latest_priced = int(new_row['priced_event_rows']) if new_row is not None else 0
latest_errors = int(new_row['errors']) if new_row is not None else 0
provider_limit = new_row.get('provider_rate_limit_limit') if new_row is not None else None
provider_remaining = new_row.get('provider_rate_limit_remaining') if new_row is not None else None
provider_reset = new_row.get('provider_rate_limit_reset') if new_row is not None else None
provider_retry_after = new_row.get('provider_retry_after') if new_row is not None else None

remaining_ratio = None
try:
    remaining_ratio = round(float(provider_remaining) / float(provider_limit), 6) if provider_limit and float(provider_limit) > 0 else None
except Exception:
    remaining_ratio = None

latest_summary = {
    'latest_run_calls_used': latest_calls,
    'latest_max_calls': latest_max_calls,
    'provider_rate_limit_limit': provider_limit,
    'provider_rate_limit_remaining': provider_remaining,
    'provider_rate_limit_remaining_ratio': remaining_ratio,
    'provider_rate_limit_reset': provider_reset,
    'provider_retry_after': provider_retry_after,
    'repo_usage_log_rows': int(len(export_log)),
}
pd.DataFrame([latest_summary]).to_csv(output_dir / 'odds_api_io_provider_usage_summary.csv', index=False)

markdown = [
    '# Odds-API.io Usage Report',
    '',
    'This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.',
    '',
    f"Generated UTC: {now.isoformat()}",
    f"Latest run calls used: {latest_calls} / {latest_max_calls}",
    f"Latest endpoint mode: {latest_endpoint_mode}",
    f"Latest search queries: {latest_queries}",
    f"Latest priced event rows: {latest_priced}",
    f"Latest errors/status rows: {latest_errors}",
    '',
    '## Provider rate-limit headers',
    '',
    f"x-ratelimit-limit: {provider_limit}",
    f"x-ratelimit-remaining: {provider_remaining}",
    f"remaining ratio: {remaining_ratio}",
    f"x-ratelimit-reset: {provider_reset}",
    f"retry-after: {provider_retry_after}",
    '',
    '## Estimated repo-driven req/hr',
    '',
]

for _, row in summary_df.iterrows():
    markdown.append(
        f"- Last {int(row['window_hours'])}h: {int(row['calls_used'])} calls across {int(row['runs'])} runs "
        f"=> {row['avg_requests_per_hour_from_repo_runs']} req/hr"
    )

markdown.extend([
    '',
    '## Interpretation',
    '',
    '- Provider headers are the best available source for current API-window limit/remaining/reset.',
    '- Repo req/hr is still useful for estimating what this workflow alone consumes over time.',
    '- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.',
])

(output_dir / 'odds_api_io_usage_report.md').write_text('\n'.join(markdown), encoding='utf-8')
print({
    'latest_calls_used': latest_calls,
    'latest_max_calls': latest_max_calls,
    'provider_limit': provider_limit,
    'provider_remaining': provider_remaining,
    'usage_log_rows': int(len(export_log)),
    'summary_rows': int(len(summary_df)),
})
