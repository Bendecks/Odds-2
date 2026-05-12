# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T07:13:19.758539+00:00
Latest run calls used: 3 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: nan
Latest priced event rows: 10
Latest errors/status rows: 20

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 54
remaining ratio: 0.54
x-ratelimit-reset: 2026-05-12T07:49:01Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 15 calls across 5 runs => 15.0 req/hr
- Last 6h: 30 calls across 10 runs => 5.0 req/hr
- Last 12h: 118 calls across 24 runs => 9.8333 req/hr
- Last 24h: 118 calls across 24 runs => 4.9167 req/hr
- Last 72h: 118 calls across 24 runs => 1.6389 req/hr
- Last 168h: 118 calls across 24 runs => 0.7024 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.