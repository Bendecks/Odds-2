# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T07:10:55.319896+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 20

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 62
remaining ratio: 0.62
x-ratelimit-reset: 2026-05-12T07:49:01Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 12 calls across 4 runs => 12.0 req/hr
- Last 6h: 27 calls across 9 runs => 4.5 req/hr
- Last 12h: 115 calls across 23 runs => 9.5833 req/hr
- Last 24h: 115 calls across 23 runs => 4.7917 req/hr
- Last 72h: 115 calls across 23 runs => 1.5972 req/hr
- Last 168h: 115 calls across 23 runs => 0.6845 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.