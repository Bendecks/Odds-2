# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T21:58:41.592004+00:00
Latest run calls used: 7 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Huesca, Napoli, Tottenham, Vallecano, Benfica, Estrela
Latest priced event rows: 0
Latest errors/status rows: 7

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 0
remaining ratio: 0.0
x-ratelimit-reset: 2026-05-11T22:22:15Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 71 calls across 9 runs => 71.0 req/hr
- Last 6h: 88 calls across 14 runs => 14.6667 req/hr
- Last 12h: 88 calls across 14 runs => 7.3333 req/hr
- Last 24h: 88 calls across 14 runs => 3.6667 req/hr
- Last 72h: 88 calls across 14 runs => 1.2222 req/hr
- Last 168h: 88 calls across 14 runs => 0.5238 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.