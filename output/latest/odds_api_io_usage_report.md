# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-16T02:12:39.322732+00:00
Latest run calls used: 7 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 41
remaining ratio: 0.41
x-ratelimit-reset: 2026-05-16T02:56:18Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 7 calls across 1 runs => 7.0 req/hr
- Last 6h: 7 calls across 1 runs => 1.1667 req/hr
- Last 12h: 7 calls across 1 runs => 0.5833 req/hr
- Last 24h: 12 calls across 2 runs => 0.5 req/hr
- Last 72h: 63 calls across 9 runs => 0.875 req/hr
- Last 168h: 266 calls across 44 runs => 1.5833 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.