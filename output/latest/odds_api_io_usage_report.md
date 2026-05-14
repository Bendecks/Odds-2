# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-14T13:52:32.377751+00:00
Latest run calls used: 4 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Valencia
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 82
remaining ratio: 0.82
x-ratelimit-reset: 2026-05-14T14:51:16Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 4 calls across 1 runs => 4.0 req/hr
- Last 6h: 8 calls across 2 runs => 1.3333 req/hr
- Last 12h: 11 calls across 3 runs => 0.9167 req/hr
- Last 24h: 16 calls across 4 runs => 0.6667 req/hr
- Last 72h: 246 calls across 41 runs => 3.4167 req/hr
- Last 168h: 246 calls across 41 runs => 1.4643 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.