# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-19T14:43:11.841052+00:00
Latest run calls used: 8 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Bournemouth, Bournemouth, Charleroi, Genk, Westerlo
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 50
remaining ratio: 0.5
x-ratelimit-reset: 2026-05-19T15:34:23Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 8 calls across 1 runs => 8.0 req/hr
- Last 6h: 8 calls across 1 runs => 1.3333 req/hr
- Last 12h: 8 calls across 1 runs => 0.6667 req/hr
- Last 24h: 16 calls across 3 runs => 0.6667 req/hr
- Last 72h: 52 calls across 7 runs => 0.7222 req/hr
- Last 168h: 194 calls across 23 runs => 1.1548 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.