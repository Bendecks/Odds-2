# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T02:14:31.156668+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 0

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 92
remaining ratio: 0.92
x-ratelimit-reset: 2026-05-12T03:13:44Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 3 calls across 1 runs => 3.0 req/hr
- Last 6h: 87 calls across 14 runs => 14.5 req/hr
- Last 12h: 91 calls across 15 runs => 7.5833 req/hr
- Last 24h: 91 calls across 15 runs => 3.7917 req/hr
- Last 72h: 91 calls across 15 runs => 1.2639 req/hr
- Last 168h: 91 calls across 15 runs => 0.5417 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.