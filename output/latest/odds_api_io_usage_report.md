# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-16T13:05:41.827824+00:00
Latest run calls used: 11 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Celtic, Falkirk, Hibernian, Sociedad B
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 25
remaining ratio: 0.25
x-ratelimit-reset: 2026-05-16T13:56:57Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 11 calls across 1 runs => 11.0 req/hr
- Last 6h: 11 calls across 1 runs => 1.8333 req/hr
- Last 12h: 18 calls across 2 runs => 1.5 req/hr
- Last 24h: 18 calls across 2 runs => 0.75 req/hr
- Last 72h: 47 calls across 8 runs => 0.6528 req/hr
- Last 168h: 277 calls across 45 runs => 1.6488 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.