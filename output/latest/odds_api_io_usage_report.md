# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T15:05:38.398270+00:00
Latest run calls used: 7 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: PFC Cherno More Varna, AL Faisaly (Jor), Kifisia, Panetolikos
Latest priced event rows: 10
Latest errors/status rows: 20

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 85
remaining ratio: 0.85
x-ratelimit-reset: 2026-05-12T16:04:33Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 7 calls across 1 runs => 7.0 req/hr
- Last 6h: 18 calls across 4 runs => 3.0 req/hr
- Last 12h: 51 calls across 15 runs => 4.25 req/hr
- Last 24h: 142 calls across 30 runs => 5.9167 req/hr
- Last 72h: 142 calls across 30 runs => 1.9722 req/hr
- Last 168h: 142 calls across 30 runs => 0.8452 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.