# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T21:16:37.460068+00:00
Latest run calls used: 5 / 10
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Napoli, Tottenham, Vallecano
Latest priced event rows: 0
Latest errors/status rows: 3

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 68
remaining ratio: 0.68
x-ratelimit-reset: 2026-05-11T21:17:32Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 27 calls across 7 runs => 27.0 req/hr
- Last 6h: 31 calls across 8 runs => 5.1667 req/hr
- Last 12h: 31 calls across 8 runs => 2.5833 req/hr
- Last 24h: 31 calls across 8 runs => 1.2917 req/hr
- Last 72h: 31 calls across 8 runs => 0.4306 req/hr
- Last 168h: 31 calls across 8 runs => 0.1845 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.