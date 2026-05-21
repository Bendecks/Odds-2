# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-21T14:48:39.302532+00:00
Latest run calls used: 9 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Atromitos, Kifisia, Panetolikos, Anderlecht, Gent, Mechelen
Latest priced event rows: 6
Latest errors/status rows: 74

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 39
remaining ratio: 0.39
x-ratelimit-reset: 2026-05-21T15:39:27Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 9 calls across 1 runs => 9.0 req/hr
- Last 6h: 9 calls across 1 runs => 1.5 req/hr
- Last 12h: 9 calls across 1 runs => 0.75 req/hr
- Last 24h: 15 calls across 2 runs => 0.625 req/hr
- Last 72h: 42 calls across 7 runs => 0.5833 req/hr
- Last 168h: 109 calls across 15 runs => 0.6488 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.