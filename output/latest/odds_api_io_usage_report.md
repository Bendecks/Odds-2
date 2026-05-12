# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T04:03:07.362395+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 20

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 73
remaining ratio: 0.73
x-ratelimit-reset: 2026-05-12T04:42:36Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 9 calls across 3 runs => 9.0 req/hr
- Last 6h: 12 calls across 4 runs => 2.0 req/hr
- Last 12h: 100 calls across 18 runs => 8.3333 req/hr
- Last 24h: 100 calls across 18 runs => 4.1667 req/hr
- Last 72h: 100 calls across 18 runs => 1.3889 req/hr
- Last 168h: 100 calls across 18 runs => 0.5952 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.