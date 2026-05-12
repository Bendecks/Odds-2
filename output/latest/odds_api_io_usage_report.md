# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T03:48:28.084520+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 0

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 82
remaining ratio: 0.82
x-ratelimit-reset: 2026-05-12T04:42:36Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 6 calls across 2 runs => 6.0 req/hr
- Last 6h: 26 calls across 5 runs => 4.3333 req/hr
- Last 12h: 97 calls across 17 runs => 8.0833 req/hr
- Last 24h: 97 calls across 17 runs => 4.0417 req/hr
- Last 72h: 97 calls across 17 runs => 1.3472 req/hr
- Last 168h: 97 calls across 17 runs => 0.5774 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.