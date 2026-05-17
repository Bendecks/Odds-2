# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-17T13:03:30.175078+00:00
Latest run calls used: 14 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Como, Genoa, Juventus, Pisa, Roma, Anderlecht, Man United, La Coruna, AZ Alkmaar, Heerenveen
Latest priced event rows: 10
Latest errors/status rows: 59

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 28
remaining ratio: 0.28
x-ratelimit-reset: 2026-05-17T13:54:52Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 14 calls across 1 runs => 14.0 req/hr
- Last 6h: 14 calls across 1 runs => 2.3333 req/hr
- Last 12h: 19 calls across 2 runs => 1.5833 req/hr
- Last 24h: 44 calls across 4 runs => 1.8333 req/hr
- Last 72h: 68 calls across 8 runs => 0.9444 req/hr
- Last 168h: 310 calls across 48 runs => 1.8452 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.