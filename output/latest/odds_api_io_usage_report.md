# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-22T14:24:41.603368+00:00
Latest run calls used: 6 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 52
remaining ratio: 0.52
x-ratelimit-reset: 2026-05-22T15:13:59Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 6 calls across 1 runs => 6.0 req/hr
- Last 6h: 6 calls across 1 runs => 1.0 req/hr
- Last 12h: 11 calls across 2 runs => 0.9167 req/hr
- Last 24h: 20 calls across 3 runs => 0.8333 req/hr
- Last 72h: 45 calls across 7 runs => 0.625 req/hr
- Last 168h: 107 calls across 15 runs => 0.6369 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.