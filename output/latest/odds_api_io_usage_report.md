# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T21:29:03.377488+00:00
Latest run calls used: 10 / 10
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Huesca, Napoli, Tottenham, Vallecano, Benfica, Estrela, Gil Vicente, Guimaraes
Latest priced event rows: 0
Latest errors/status rows: 7

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 70
remaining ratio: 0.7
x-ratelimit-reset: 2026-05-11T22:22:15Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 44 calls across 8 runs => 44.0 req/hr
- Last 6h: 51 calls across 10 runs => 8.5 req/hr
- Last 12h: 51 calls across 10 runs => 4.25 req/hr
- Last 24h: 51 calls across 10 runs => 2.125 req/hr
- Last 72h: 51 calls across 10 runs => 0.7083 req/hr
- Last 168h: 51 calls across 10 runs => 0.3036 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.