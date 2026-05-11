# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T21:35:54.150582+00:00
Latest run calls used: 10 / 10
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Huesca, Napoli, Tottenham, Vallecano, Benfica, Estrela, Gil Vicente
Latest priced event rows: 1
Latest errors/status rows: 6

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 50
remaining ratio: 0.5
x-ratelimit-reset: 2026-05-11T22:22:15Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 54 calls across 9 runs => 54.0 req/hr
- Last 6h: 61 calls across 11 runs => 10.1667 req/hr
- Last 12h: 61 calls across 11 runs => 5.0833 req/hr
- Last 24h: 61 calls across 11 runs => 2.5417 req/hr
- Last 72h: 61 calls across 11 runs => 0.8472 req/hr
- Last 168h: 61 calls across 11 runs => 0.3631 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.