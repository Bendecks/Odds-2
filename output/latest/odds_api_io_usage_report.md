# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T21:42:07.886989+00:00
Latest run calls used: 10 / 10
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Huesca, Napoli, Tottenham, Vallecano, Benfica, Estrela, Gil Vicente
Latest priced event rows: 1
Latest errors/status rows: 6

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 30
remaining ratio: 0.3
x-ratelimit-reset: 2026-05-11T22:22:15Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 64 calls across 10 runs => 64.0 req/hr
- Last 6h: 71 calls across 12 runs => 11.8333 req/hr
- Last 12h: 71 calls across 12 runs => 5.9167 req/hr
- Last 24h: 71 calls across 12 runs => 2.9583 req/hr
- Last 72h: 71 calls across 12 runs => 0.9861 req/hr
- Last 168h: 71 calls across 12 runs => 0.4226 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.