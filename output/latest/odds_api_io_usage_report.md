# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-06-03T02:58:55.816012+00:00
Latest run calls used: 7 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Hoo P R / Lai P J, Pakistan Panthers, Indonesia, Pakistan, France
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 57
remaining ratio: 0.57
x-ratelimit-reset: 2026-06-03T03:42:26Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 7 calls across 1 runs => 7.0 req/hr
- Last 6h: 7 calls across 1 runs => 1.1667 req/hr
- Last 12h: 7 calls across 1 runs => 0.5833 req/hr
- Last 24h: 7 calls across 1 runs => 0.2917 req/hr
- Last 72h: 18 calls across 4 runs => 0.25 req/hr
- Last 168h: 51 calls across 12 runs => 0.3036 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.