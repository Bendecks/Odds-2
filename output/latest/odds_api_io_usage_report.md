# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-28T02:29:04.720097+00:00
Latest run calls used: 3 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 57
remaining ratio: 0.57
x-ratelimit-reset: 2026-05-28T02:57:51Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 3 calls across 1 runs => 3.0 req/hr
- Last 6h: 3 calls across 1 runs => 0.5 req/hr
- Last 12h: 5 calls across 2 runs => 0.4167 req/hr
- Last 24h: 8 calls across 3 runs => 0.3333 req/hr
- Last 72h: 18 calls across 6 runs => 0.25 req/hr
- Last 168h: 56 calls across 12 runs => 0.3333 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.