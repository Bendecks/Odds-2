# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-14T19:03:40.632740+00:00
Latest run calls used: 8 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Valencia, Girona, Real Madrid
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 79
remaining ratio: 0.79
x-ratelimit-reset: 2026-05-14T20:01:53Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 8 calls across 1 runs => 8.0 req/hr
- Last 6h: 12 calls across 2 runs => 2.0 req/hr
- Last 12h: 16 calls across 3 runs => 1.3333 req/hr
- Last 24h: 19 calls across 4 runs => 0.7917 req/hr
- Last 72h: 254 calls across 42 runs => 3.5278 req/hr
- Last 168h: 254 calls across 42 runs => 1.5119 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.