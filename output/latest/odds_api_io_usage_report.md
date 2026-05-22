# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-22T02:39:28.738327+00:00
Latest run calls used: 5 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 59
remaining ratio: 0.59
x-ratelimit-reset: 2026-05-22T03:10:33Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 5 calls across 1 runs => 5.0 req/hr
- Last 6h: 5 calls across 1 runs => 0.8333 req/hr
- Last 12h: 14 calls across 2 runs => 1.1667 req/hr
- Last 24h: 14 calls across 2 runs => 0.5833 req/hr
- Last 72h: 39 calls across 6 runs => 0.5417 req/hr
- Last 168h: 101 calls across 14 runs => 0.6012 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.