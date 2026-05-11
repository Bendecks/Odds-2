# Odds-API.io Integration Notes

This project uses Odds-API.io only as a cautious paper/proxy forward-testing data source.
It must not be used to generate real-money betting recommendations until project readiness gates are met.

## Base URL

`https://api.odds-api.io/v3`

## Authentication

API key is passed as query parameter:

`?apiKey=$ODDS_API_IO_KEY`

Never commit keys.

## Current project usage

Environment variables used by the GitHub workflow:

- `ODDS_API_IO_KEY`
- `ODDS_API_IO_MAX_CALLS`
- `ODDS_API_IO_MAX_EVENTS`
- `ODDS_API_IO_MAX_PRICE_EVENTS`
- `ODDS_API_IO_BOOKMAKERS`
- optional: `ODDS_API_IO_SEARCH_QUERY`

Current cautious call strategy:

1. Build model-covered upcoming fixture predictions.
2. Use `/events/search` for model-covered team names.
3. Collect up to `ODDS_API_IO_MAX_PRICE_EVENTS` event IDs.
4. Use `/odds/multi` once for selected event IDs.
5. Parse `bookmakers -> markets -> odds -> home/draw/away`.
6. Store rows as paper/proxy prices only.

## Relevant endpoints

### Search upcoming events

`GET /events/search?apiKey=KEY&query=TEAM`

Docs summary: searches upcoming events using a text query and returns up to 10 results.

Important fields:

- `id`
- `home`
- `away`
- `date`
- `league.name`
- `league.slug`
- `sport.name`
- `sport.slug`
- `status`
- `bookmakerCount`

### Get event by ID

`GET /events/{id}?apiKey=KEY`

Useful for debugging one selected event, not usually used in workflow.

### Get odds for one event

`GET /odds?apiKey=KEY&eventId=EVENT_ID&bookmakers=Bet365,Unibet`

Response shape:

- `id`
- `home`
- `away`
- `date`
- `league`
- `sport`
- `status`
- `bookmakerIds`
- `bookmakers`
- `urls`

`bookmakers` shape:

```text
bookmakers[bookmakerName] -> list[market]
market.name -> e.g. ML, Moneyline, Match Winner, Full Time Result, 1X2
market.odds -> list[outcome]
outcome.home
outcome.draw
outcome.away
```

### Get odds for multiple events

`GET /odds/multi?apiKey=KEY&eventIds=ID1,ID2,ID3&bookmakers=Bet365,Unibet`

Best practice says to use this instead of one `/odds` request per event.
Up to 10 events per request.

Current project uses this endpoint to reduce request count.

### Get bookmakers

`GET /bookmakers`

No auth required. Response fields:

- `name`
- `active`

Useful to verify exact bookmaker names such as `Bet365`, `Unibet`, `1xbet` / `1xBet`.

### Events endpoint with bookmaker filter

Best practices say this is valid:

`GET /events?apiKey=KEY&sport=football&bookmaker=Bet365`

This returns only events with Bet365 odds. It may be useful later for broader discovery, but current workflow prioritizes `/events/search` because it targets model-covered fixtures.

### Value bets

`GET /value-bets?apiKey=KEY&bookmaker=Bet365&includeEventDetails=true`

This must not be used as a direct betting signal in this project yet. It can be used later as a diagnostic/comparison source only.

### Paid endpoints

Dropping odds may require Starter plan or higher. Do not rely on it for the current free-plan workflow.

## Best-practice notes applied

- Use batch endpoints: `/odds/multi` for selected event IDs.
- Limit bookmakers: only configured bookmakers, currently Bet365 and 1xbet unless changed.
- Cache/store raw responses in `data/raw/odds_api_io`.
- Track usage via `odds_api_io_forward_price_status.csv`.
- Hard cap API calls via environment variables.
- Treat missing odds as status rows, not fatal errors.
- Keep all outputs paper/proxy-only.

## Current non-goals

- No real-money betting features.
- No direct promotion from Odds-API.io value-bets endpoint to candidate bets.
- No paid-plan-only endpoints as required dependencies.
