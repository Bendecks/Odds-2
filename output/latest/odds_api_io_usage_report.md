# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-14T02:31:15.942047+00:00
Latest run calls used: 3 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 8
Latest errors/status rows: 72

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 83
remaining ratio: 0.83
x-ratelimit-reset: 2026-05-14T03:30:03Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 3 calls across 1 runs => 3.0 req/hr
- Last 6h: 3 calls across 1 runs => 0.5 req/hr
- Last 12h: 3 calls across 1 runs => 0.25 req/hr
- Last 24h: 21 calls across 3 runs => 0.875 req/hr
- Last 72h: 238 calls across 39 runs => 3.3056 req/hr
- Last 168h: 238 calls across 39 runs => 1.4167 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.