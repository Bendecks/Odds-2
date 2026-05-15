# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-15T02:30:28.362250+00:00
Latest run calls used: 5 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 58
remaining ratio: 0.58
x-ratelimit-reset: 2026-05-15T03:04:15Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 5 calls across 1 runs => 5.0 req/hr
- Last 6h: 5 calls across 1 runs => 0.8333 req/hr
- Last 12h: 13 calls across 2 runs => 1.0833 req/hr
- Last 24h: 24 calls across 5 runs => 1.0 req/hr
- Last 72h: 168 calls across 28 runs => 2.3333 req/hr
- Last 168h: 259 calls across 43 runs => 1.5417 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.