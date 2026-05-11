# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Manual odds are optional fallback only and are not treated as a blocker in this development phase.

Upcoming fixture rows: 1
Historical market proxy rows: 30
Manual forward rows: 0
Configured forward sources: 1
Enabled forward sources: 0
Automatic forward price rows: 0
Has upcoming fixtures: True
Has automatic forward odds/proxy: False
Has historical market proxy: True
Manual fallback mode: parked_optional_fallback
Automatic forward status: automatic_forward_not_ready
Blocker: only_historical_market_proxy_available_not_forward_valid
Next development step: replace_historical_market_proxy_for_forward_testing

## Interpretation

Fixtures are available, but there is no automatic forward price source yet. Historical closing-market proxy must remain research-only.