# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-13T12:27:10.368262+00:00
Latest run calls used: 13 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Levadeiakos, Volos NFC, Olympiakos, PAOK, Brest, Espanol, Villarreal, Manchester City, Hearts, Lens, Man City, Motherwell
Latest priced event rows: 0
Latest errors/status rows: 13

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 0
remaining ratio: 0.0
x-ratelimit-reset: 2026-05-13T12:54:34Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 13 calls across 1 runs => 13.0 req/hr
- Last 6h: 13 calls across 1 runs => 2.1667 req/hr
- Last 12h: 27 calls across 2 runs => 2.25 req/hr
- Last 24h: 103 calls across 10 runs => 4.2917 req/hr
- Last 72h: 230 calls across 37 runs => 3.1944 req/hr
- Last 168h: 230 calls across 37 runs => 1.369 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.