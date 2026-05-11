# Free Odds Source Research

Goal: identify free sources that can support automatic forward paper-testing without manual Bet365 upload.

## Current integrated source

### Football-Data fixtures.csv

Status: integrated as delayed market proxy.

Strengths:
- No API key.
- Free downloadable CSV.
- Includes fixture-level 1X2 odds when available.
- Already normalized into `football_data_upcoming_odds.csv` and `automatic_forward_prices.csv`.

Limits:
- Delayed/non-live.
- Weekend odds are generally collected Friday afternoon; midweek odds Tuesday.
- Suitable for proxy paper-testing only.
- Not real-money ready.

Priority: keep as baseline source.

## Candidate source 1: odds-api.io

Status: not integrated.

Claimed free tier:
- 100 requests/hour.
- Live and pre-match odds.
- Multiple bookmakers, but free plan may be limited to 2 bookmakers depending pricing page.
- REST JSON API.
- Requires API key.

Potential use:
- Best next API candidate if a free key is acceptable.
- Could provide fresher forward odds than Football-Data.

Risks:
- Need key management.
- Need verify bookmaker/football coverage on actual account.
- Terms/free-tier limitations may change.

Priority: high.

## Candidate source 2: API-Football

Status: not integrated.

Claimed free tier:
- 100 requests/day.
- Includes pre-match odds and in-play odds endpoints.
- Requires API key.

Potential use:
- Good fallback odds API if 100 requests/day is enough.
- Also provides fixtures/results data, so could simplify source stack.

Risks:
- Request limit is tight.
- Free plan has season limitations.
- Need map league IDs and bookmaker fields.

Priority: medium-high.

## Candidate source 3: SharpAPI

Status: not integrated.

Claimed free tier from comparison material:
- 12 requests/minute.
- 2 sportsbooks.
- 60-second delay.
- REST access.

Potential use:
- Could be useful if soccer coverage and EU football markets are actually available on free tier.

Risks:
- Needs direct verification from provider docs/account.
- May be more US-sports oriented.
- Not yet validated for EPL/European football 1X2.

Priority: medium.

## Candidate source 4: The Odds API

Status: not integrated.

Observed free tier:
- Limited free access.
- Current visible free plan appears restricted to NBA/MLB moneylines and US sportsbooks.
- Soccer requires paid tier on visible pricing.

Potential use:
- Good paid source later, not currently ideal for this zero-cost project.

Priority: low for now.

## Recommended next integration order

1. Keep Football-Data as the no-key baseline proxy.
2. Add optional `ODDS_API_IO_KEY` adapter for odds-api.io.
3. Add optional `API_FOOTBALL_KEY` adapter if odds-api.io is insufficient.
4. Only revisit The Odds API if budget or requirements change.

## Guardrails

- All free/proxy odds remain `paper-test only` until enough forward validation exists.
- No real-money readiness from any unvalidated source.
- Every source should write `source_quality`, `source_type`, `price_captured_at_utc`, and `real_money_ready=False` in downstream reports.
