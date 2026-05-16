# Odds-API.io Usage Report

This report combines repo-estimated Odds-API.io usage with provider rate-limit headers when available.

Generated UTC: 2026-05-16T21:29:41.060513+00:00
Latest run calls used: 14 / 14
Latest endpoint mode: multi_event_documented_endpoint
Latest search queries: Celtic, Falkirk, Hibernian, Sociedad B, Bayern Munich, Ein Frankfurt, Freiburg, Heidenheim, Leverkusen
Latest priced event rows: 9
Latest errors/status rows: 45

## Provider rate-limit headers

x-ratelimit-limit: 100
x-ratelimit-remaining: 36
remaining ratio: 0.36
x-ratelimit-reset: 2026-05-16T21:38:06Z
retry-after: None

## Estimated repo-driven req/hr

- Last 1h: 14 calls across 1 runs => 14.0 req/hr
- Last 6h: 14 calls across 1 runs => 2.3333 req/hr
- Last 12h: 25 calls across 2 runs => 2.0833 req/hr
- Last 24h: 32 calls across 3 runs => 1.3333 req/hr
- Last 72h: 56 calls across 8 runs => 0.7778 req/hr
- Last 168h: 291 calls across 46 runs => 1.7321 req/hr

## Interpretation

- Provider headers are the best available source for current API-window limit/remaining/reset.
- Repo req/hr is still useful for estimating what this workflow alone consumes over time.
- Current workflow remains capped by ODDS_API_IO_MAX_CALLS and ODDS_API_IO_MAX_PRICE_EVENTS.