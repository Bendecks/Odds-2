# Odds-API.io Extra Multi-Odds Batches

Adds extra /odds/multi calls after the primary fetch, using already discovered bookmaker-filtered events.
Only direct home/away/date matches are selected. Swapped matches are not selected here.

Existing price rows before extra: 10
Extra selected event rows: 70
Extra price rows: 0
Combined price rows: 10
Extra calls used: 1 / 5
Max total price events: 80
Minimum direct match confidence: 0.72
Latest rate-limit remaining: 0
Errors/status rows: 1


## Errors / Status

- extra_multi_odds_request_or_parse: RuntimeError('HTTP 429: {"error":"You have exceeded your rate limit of 100 requests per hour. It resets in 23 minutes and 52 seconds."}')