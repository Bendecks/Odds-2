# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T21:39:16.789225+00:00
Latest run calls used: 13 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Asteras Tripolis, Kifisia, Panetolikos, Celta, Betis, Aberdeen, Dundee United, Kilmarnock, Osasuna, Levadeiakos, Volos NFC, Olympiakos
Latest priced event rows: 0
Latest errors/status rows: 13

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 0
remaining ratio: 0.0
x-ratelimit-reset: 2026-05-12T21:55:16Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 41 calls across 3 runs => 41.0 req/hr
- Last 6h: 61 calls across 5 runs => 10.1667 req/hr
- Last 12h: 79 calls across 9 runs => 6.5833 req/hr
- Last 24h: 142 calls across 24 runs => 5.9167 req/hr
- Last 72h: 203 calls across 35 runs => 2.8194 req/hr
- Last 168h: 203 calls across 35 runs => 1.2083 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.