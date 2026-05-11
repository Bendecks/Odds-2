# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T21:22:56.226049+00:00
Latest run calls used: 10 / 10
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Huesca, Napoli, Tottenham, Vallecano, Benfica, Estrela, Gil Vicente, Guimaraes
Latest priced event rows: 0
Latest errors/status rows: 7

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 90
remaining ratio: 0.9
x-ratelimit-reset: 2026-05-11T22:22:15Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 34 calls across 7 runs => 34.0 req/hr
- Last 6h: 41 calls across 9 runs => 6.8333 req/hr
- Last 12h: 41 calls across 9 runs => 3.4167 req/hr
- Last 24h: 41 calls across 9 runs => 1.7083 req/hr
- Last 72h: 41 calls across 9 runs => 0.5694 req/hr
- Last 168h: 41 calls across 9 runs => 0.244 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.