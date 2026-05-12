# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T14:03:19.813657+00:00
Latest run calls used: 4 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Sur SC
Latest priced event rows: 0
Latest errors/status rows: 1

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 88
remaining ratio: 0.88
x-ratelimit-reset: 2026-05-12T15:01:13Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 4 calls across 1 runs => 4.0 req/hr
- Last 6h: 11 calls across 3 runs => 1.8333 req/hr
- Last 12h: 47 calls across 15 runs => 3.9167 req/hr
- Last 24h: 135 calls across 29 runs => 5.625 req/hr
- Last 72h: 135 calls across 29 runs => 1.875 req/hr
- Last 168h: 135 calls across 29 runs => 0.8036 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.