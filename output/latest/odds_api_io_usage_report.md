# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T21:21:57.467746+00:00
Latest run calls used: 14 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Asteras Tripolis, Kifisia, Panetolikos, Celta, Betis, Aberdeen, Dundee United, Kilmarnock, Osasuna, Levadeiakos, Volos NFC, Olympiakos
Latest priced event rows: 10
Latest errors/status rows: 59

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 33
remaining ratio: 0.33
x-ratelimit-reset: 2026-05-12T21:55:16Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 14 calls across 1 runs => 14.0 req/hr
- Last 6h: 34 calls across 3 runs => 5.6667 req/hr
- Last 12h: 52 calls across 7 runs => 4.3333 req/hr
- Last 24h: 145 calls across 25 runs => 6.0417 req/hr
- Last 72h: 176 calls across 33 runs => 2.4444 req/hr
- Last 168h: 176 calls across 33 runs => 1.0476 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.