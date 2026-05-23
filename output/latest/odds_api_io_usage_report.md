# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-23T02:16:16.546832+00:00
Latest run calls used: 7 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 7
Latest errors/status rows: 73

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 47
remaining ratio: 0.47
x-ratelimit-reset: 2026-05-23T02:58:20Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 7 calls across 1 runs => 7.0 req/hr
- Last 6h: 7 calls across 1 runs => 1.1667 req/hr
- Last 12h: 13 calls across 2 runs => 1.0833 req/hr
- Last 24h: 18 calls across 3 runs => 0.75 req/hr
- Last 72h: 44 calls across 7 runs => 0.6111 req/hr
- Last 168h: 107 calls across 15 runs => 0.6369 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.