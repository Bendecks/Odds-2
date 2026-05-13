# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-13T02:29:41.024323+00:00
Latest run calls used: 14 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Levadeiakos, Volos NFC, Olympiakos, PAOK, Brest, Espanol, Hearts, Lens, Man City, Motherwell, Rangers, Santiago Wanderers
Latest priced event rows: 10
Latest errors/status rows: 68

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 81
remaining ratio: 0.81
x-ratelimit-reset: 2026-05-13T03:28:43Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 14 calls across 1 runs => 14.0 req/hr
- Last 6h: 55 calls across 4 runs => 9.1667 req/hr
- Last 12h: 82 calls across 7 runs => 6.8333 req/hr
- Last 24h: 126 calls across 21 runs => 5.25 req/hr
- Last 72h: 217 calls across 36 runs => 3.0139 req/hr
- Last 168h: 217 calls across 36 runs => 1.2917 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.