# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T20:54:34.890048+00:00
Latest run calls used: 4 / 6
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Napoli, Tottenham, Vallecano
Latest priced event rows: 0
Latest errors/status rows: 4

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 87
remaining ratio: 0.87
x-ratelimit-reset: 2026-05-11T21:17:32Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 17 calls across 5 runs => 17.0 req/hr
- Last 6h: 17 calls across 5 runs => 2.8333 req/hr
- Last 12h: 17 calls across 5 runs => 1.4167 req/hr
- Last 24h: 17 calls across 5 runs => 0.7083 req/hr
- Last 72h: 17 calls across 5 runs => 0.2361 req/hr
- Last 168h: 17 calls across 5 runs => 0.1012 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.