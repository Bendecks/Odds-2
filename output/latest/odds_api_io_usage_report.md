# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T18:19:12.763074+00:00
Latest run calls used: 13 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Asteras Tripolis, Kifisia, Panetolikos, Celta, Betis, Aberdeen, Dundee United, Kilmarnock, Osasuna, Levadeiakos, Volos NFC, Olympiakos
Latest priced event rows: 0
Latest errors/status rows: 13

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 0
remaining ratio: 0.0
x-ratelimit-reset: 2026-05-12T18:43:40Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 13 calls across 1 runs => 13.0 req/hr
- Last 6h: 35 calls across 5 runs => 5.8333 req/hr
- Last 12h: 59 calls across 13 runs => 4.9167 req/hr
- Last 24h: 162 calls across 32 runs => 6.75 req/hr
- Last 72h: 162 calls across 32 runs => 2.25 req/hr
- Last 168h: 162 calls across 32 runs => 0.9643 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.