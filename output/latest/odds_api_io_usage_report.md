# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T21:31:35.328221+00:00
Latest run calls used: 14 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Asteras Tripolis, Kifisia, Panetolikos, Celta, Betis, Aberdeen, Dundee United, Kilmarnock, Osasuna, BC Olympiakos Piraeus, Levadeiakos, Volos NFC
Latest priced event rows: 10
Latest errors/status rows: 58

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 0
remaining ratio: 0.0
x-ratelimit-reset: 2026-05-12T21:55:16Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 28 calls across 2 runs => 28.0 req/hr
- Last 6h: 48 calls across 4 runs => 8.0 req/hr
- Last 12h: 66 calls across 8 runs => 5.5 req/hr
- Last 24h: 139 calls across 24 runs => 5.7917 req/hr
- Last 72h: 190 calls across 34 runs => 2.6389 req/hr
- Last 168h: 190 calls across 34 runs => 1.131 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.