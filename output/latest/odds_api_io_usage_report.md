# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-06-01T17:25:46.288536+00:00
Latest run calls used: 4 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Chen, Yu Fei, Feng Y Z / Huang D P
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 62
remaining ratio: 0.62
x-ratelimit-reset: 2026-06-01T18:15:22Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 4 calls across 1 runs => 4.0 req/hr
- Last 6h: 4 calls across 1 runs => 0.6667 req/hr
- Last 12h: 4 calls across 1 runs => 0.3333 req/hr
- Last 24h: 8 calls across 2 runs => 0.3333 req/hr
- Last 72h: 23 calls across 6 runs => 0.3194 req/hr
- Last 168h: 55 calls across 14 runs => 0.3274 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.