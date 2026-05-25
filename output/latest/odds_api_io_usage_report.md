# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-25T02:43:11.974717+00:00
Latest run calls used: 2 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 73
remaining ratio: 0.73
x-ratelimit-reset: 2026-05-25T03:15:11Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 2 calls across 1 runs => 2.0 req/hr
- Last 6h: 2 calls across 1 runs => 0.3333 req/hr
- Last 12h: 2 calls across 1 runs => 0.1667 req/hr
- Last 24h: 2 calls across 1 runs => 0.0833 req/hr
- Last 72h: 20 calls across 4 runs => 0.2778 req/hr
- Last 168h: 67 calls across 12 runs => 0.3988 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.