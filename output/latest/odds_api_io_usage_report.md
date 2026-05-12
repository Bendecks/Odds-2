# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T03:43:27.663930+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 0

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 94
remaining ratio: 0.94
x-ratelimit-reset: 2026-05-12T04:42:36Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 3 calls across 1 runs => 3.0 req/hr
- Last 6h: 23 calls across 4 runs => 3.8333 req/hr
- Last 12h: 94 calls across 16 runs => 7.8333 req/hr
- Last 24h: 94 calls across 16 runs => 3.9167 req/hr
- Last 72h: 94 calls across 16 runs => 1.3056 req/hr
- Last 168h: 94 calls across 16 runs => 0.5595 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.