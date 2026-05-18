# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-18T14:58:35.895969+00:00
Latest run calls used: 4 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Leganes
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 59
remaining ratio: 0.59
x-ratelimit-reset: 2026-05-18T15:53:11Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 4 calls across 1 runs => 4.0 req/hr
- Last 6h: 4 calls across 1 runs => 0.6667 req/hr
- Last 12h: 4 calls across 1 runs => 0.3333 req/hr
- Last 24h: 7 calls across 2 runs => 0.2917 req/hr
- Last 72h: 58 calls across 7 runs => 0.8056 req/hr
- Last 168h: 317 calls across 50 runs => 1.8869 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.