# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-11T20:10:18.788507+00:00
Latest run calls used: 4 / 6
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Napoli, Tottenham, Vallecano
Latest priced event rows: 1
Latest errors/status rows: 2

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 31
remaining ratio: 0.31
x-ratelimit-reset: 2026-05-11T20:13:08Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 4 calls across 1 runs => 4.0 req/hr
- Last 6h: 4 calls across 1 runs => 0.6667 req/hr
- Last 12h: 4 calls across 1 runs => 0.3333 req/hr
- Last 24h: 4 calls across 1 runs => 0.1667 req/hr
- Last 72h: 4 calls across 1 runs => 0.0556 req/hr
- Last 168h: 4 calls across 1 runs => 0.0238 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.