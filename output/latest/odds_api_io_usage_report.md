# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-12T12:34:18.628173+00:00
Latest run calls used: 4 / 8
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: FC Epitsentr Kamianets-Podilskyi
Latest priced event rows: 10
Latest errors/status rows: 20

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 88
remaining ratio: 0.88
x-ratelimit-reset: 2026-05-12T13:33:31Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 4 calls across 1 runs => 4.0 req/hr
- Last 6h: 28 calls across 9 runs => 4.6667 req/hr
- Last 12h: 43 calls across 14 runs => 3.5833 req/hr
- Last 24h: 131 calls across 28 runs => 5.4583 req/hr
- Last 72h: 131 calls across 28 runs => 1.8194 req/hr
- Last 168h: 131 calls across 28 runs => 0.7798 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.