# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T06:51:25.013383+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 20

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 86
remaining ratio: 0.86
x-ratelimit-reset: 2026-05-12T07:49:01Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 3 calls across 1 runs => 3.0 req/hr
- Last 6h: 18 calls across 6 runs => 3.0 req/hr
- Last 12h: 106 calls across 20 runs => 8.8333 req/hr
- Last 24h: 106 calls across 20 runs => 4.4167 req/hr
- Last 72h: 106 calls across 20 runs => 1.4722 req/hr
- Last 168h: 106 calls across 20 runs => 0.631 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.