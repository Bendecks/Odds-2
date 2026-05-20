# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-20T14:43:21.170799+00:00
Latest run calls used: 8 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Atromitos, Kifisia, Panetolikos, Anderlecht, Gent, Mechelen, Brighton and Hove Albion
Latest priced event rows: 0
Latest errors/status rows: 8

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 0
remaining ratio: 0.0
x-ratelimit-reset: 2026-05-20T15:33:31Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 8 calls across 1 runs => 8.0 req/hr
- Last 6h: 8 calls across 1 runs => 1.3333 req/hr
- Last 12h: 8 calls across 1 runs => 0.6667 req/hr
- Last 24h: 11 calls across 2 runs => 0.4583 req/hr
- Last 72h: 30 calls across 6 runs => 0.4167 req/hr
- Last 168h: 105 calls across 16 runs => 0.625 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.