# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T07:30:03.745947+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 20

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 30
remaining ratio: 0.3
x-ratelimit-reset: 2026-05-12T07:49:01Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 21 calls across 7 runs => 21.0 req/hr
- Last 6h: 36 calls across 12 runs => 6.0 req/hr
- Last 12h: 124 calls across 26 runs => 10.3333 req/hr
- Last 24h: 124 calls across 26 runs => 5.1667 req/hr
- Last 72h: 124 calls across 26 runs => 1.7222 req/hr
- Last 168h: 124 calls across 26 runs => 0.7381 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.