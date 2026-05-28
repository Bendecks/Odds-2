# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-28T15:34:25.921618+00:00
Latest run calls used: 6 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Panadura SC, Baduraliya CC
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 59
remaining ratio: 0.59
x-ratelimit-reset: 2026-05-28T16:25:43Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 6 calls across 1 runs => 6.0 req/hr
- Last 6h: 6 calls across 1 runs => 1.0 req/hr
- Last 12h: 6 calls across 1 runs => 0.5 req/hr
- Last 24h: 9 calls across 2 runs => 0.375 req/hr
- Last 72h: 22 calls across 6 runs => 0.3056 req/hr
- Last 168h: 47 calls across 11 runs => 0.2798 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.