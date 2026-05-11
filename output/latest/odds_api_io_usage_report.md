# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T21:48:53.959717+00:00
Latest run calls used: 10 / 10
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Huesca, Napoli, Tottenham, Vallecano, Benfica, Estrela, Gil Vicente
Latest priced event rows: 1
Latest errors/status rows: 6

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 2
remaining ratio: 0.02
x-ratelimit-reset: 2026-05-11T22:22:15Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 68 calls across 9 runs => 68.0 req/hr
- Last 6h: 81 calls across 13 runs => 13.5 req/hr
- Last 12h: 81 calls across 13 runs => 6.75 req/hr
- Last 24h: 81 calls across 13 runs => 3.375 req/hr
- Last 72h: 81 calls across 13 runs => 1.125 req/hr
- Last 168h: 81 calls across 13 runs => 0.4821 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.