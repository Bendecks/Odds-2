# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T21:00:28.976705+00:00
Latest run calls used: 4 / 6
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Napoli, Tottenham, Vallecano
Latest priced event rows: 0
Latest errors/status rows: 3

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 83
remaining ratio: 0.83
x-ratelimit-reset: 2026-05-11T21:17:32Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 21 calls across 6 runs => 21.0 req/hr
- Last 6h: 21 calls across 6 runs => 3.5 req/hr
- Last 12h: 21 calls across 6 runs => 1.75 req/hr
- Last 24h: 21 calls across 6 runs => 0.875 req/hr
- Last 72h: 21 calls across 6 runs => 0.2917 req/hr
- Last 168h: 21 calls across 6 runs => 0.125 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.