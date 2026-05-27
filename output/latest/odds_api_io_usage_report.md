# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-27T15:00:39.831288+00:00
Latest run calls used: 2 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 5
Latest errors/status rows: 75

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 47
remaining ratio: 0.47
x-ratelimit-reset: 2026-05-27T15:24:03Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 2 calls across 1 runs => 2.0 req/hr
- Last 6h: 2 calls across 1 runs => 0.3333 req/hr
- Last 12h: 2 calls across 1 runs => 0.1667 req/hr
- Last 24h: 5 calls across 2 runs => 0.2083 req/hr
- Last 72h: 15 calls across 5 runs => 0.2083 req/hr
- Last 168h: 53 calls across 11 runs => 0.3155 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.