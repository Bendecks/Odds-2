# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T04:14:13.858587+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 20

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 57
remaining ratio: 0.57
x-ratelimit-reset: 2026-05-12T04:42:36Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 12 calls across 4 runs => 12.0 req/hr
- Last 6h: 15 calls across 5 runs => 2.5 req/hr
- Last 12h: 103 calls across 19 runs => 8.5833 req/hr
- Last 24h: 103 calls across 19 runs => 4.2917 req/hr
- Last 72h: 103 calls across 19 runs => 1.4306 req/hr
- Last 168h: 103 calls across 19 runs => 0.6131 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.