# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-13T14:12:23.709825+00:00
Latest run calls used: 5 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Levadeiakos, Volos NFC
Latest priced event rows: 10
Latest errors/status rows: 70

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 86
remaining ratio: 0.86
x-ratelimit-reset: 2026-05-13T15:11:23Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 5 calls across 1 runs => 5.0 req/hr
- Last 6h: 18 calls across 2 runs => 3.0 req/hr
- Last 12h: 32 calls across 3 runs => 2.6667 req/hr
- Last 24h: 100 calls across 9 runs => 4.1667 req/hr
- Last 72h: 235 calls across 38 runs => 3.2639 req/hr
- Last 168h: 235 calls across 38 runs => 1.3988 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.