# HANDOFF – Odds-2 betting paper-test project

This file is the handoff for continuing the project in a new ChatGPT conversation. Treat it as first source of truth together with latest files in `output/latest/`.

## User goal

Build a free/low-cost automated football betting evaluation system. The user only bets at Bet365, so the forward paper-test pipeline must be Bet365-only. Real-money betting is NOT active. Current phase is paper-test / observation.

## Operating rules

- Use free sources and capped API calls.
- Manual Bet365 upload is parked.
- Keep real-money gates closed until enough settled paper-test evidence exists.
- Do not confuse baseline coverage observations with strong model signals.
- Continue in batches and ask user input only when strictly necessary.

## Repository

- Repo: `Bendecks/Odds-2`
- Workflow: `.github/workflows/free-data-stack.yml`
- Outputs: `output/latest/`
- Paper log: `data/predictions/paper_test_log.jsonl`

## APIs / data sources

Active:

1. `Odds-API.io`
   - Secret: `ODDS_API_IO_KEY`
   - Used for upcoming Bet365 events and Bet365 odds.
   - Current workflow settings:
     - `ODDS_API_IO_EVENTS_BOOKMAKER=Bet365`
     - `ODDS_API_IO_BOOKMAKERS=Bet365`
     - `ODDS_API_IO_MAX_CALLS=8`
     - `ODDS_API_IO_MAX_EVENTS=100`
     - `ODDS_API_IO_EVENTS_MAX_PAGES=4`
     - `ODDS_API_IO_MAX_PRICE_EVENTS=30`
     - `ODDS_API_IO_EXTRA_MULTI_CALLS=3`
   - Rate-limit headers are captured.

2. `football-data.co.uk`
   - Free historical data source.
   - Used for historical results/odds/model inputs.

3. `ClubElo`
   - Free rating/team-strength source.

4. `Gemini API`
   - Secret: `GEMINI_API_KEY`
   - Used for AI review/diagnostics, not odds.

Available but off:

5. `API-Football`
   - Secret: `API_FOOTBALL_KEY`
   - Current workflow setting: `API_FOOTBALL_MAX_CALLS=0`
   - Keep off unless needed; possible later use: settlement/fixtures/results.

## Workflow schedule

Runs every 12 hours and manually:

```yaml
schedule:
  - cron: '0 */12 * * *'
```

## Current pipeline status

Working Bet365-only paper-test pipeline exists:

- Bet365-only forward odds fetch works.
- 30 Bet365 price rows per good run were achieved.
- 90 value snapshots per good run were achieved.
- Paper-test picks are generated and logged.
- Human-readable paper-bets report exists.
- Youth/U/reserve filtering was added in human report and in Odds-API price-quality filter.
- Market inventory diagnostics were added to inspect raw Odds-API responses without extra API calls.

Latest known good numbers before final handoff work:

- `odds-api.io forward prices: 30`
- `Automatic forward value snapshots: 90`
- `Paper test picks output: 7`
- `Valid forward paper test log: 36+`
- Bet365-only confirmed: `source_counts: {'odds_api_io_Bet365_ML': 90}`

Re-read latest numbers from `output/latest/` after next workflow run.

## Important files

Human overview:

- `scripts/build_paper_bets_human_report.py`
- Output:
  - `output/latest/paper_bets_human_report.md`
  - `output/latest/paper_bets_human_summary.csv`
  - `output/latest/paper_bets_human_excluded.md`

Odds-API fetch/extension:

- `scripts/fetch_odds_api_io_forward_prices.py`
- `scripts/extend_odds_api_io_forward_prices.py`

Price quality:

- `scripts/filter_odds_api_io_forward_prices_quality.py`
- Accepts only direct home/away/date matches.
- Rejects swapped home/away.
- Rejects youth/U/reserve/academy/B-team/II rows.
- Rejection status: `rejected_youth_or_reserve_match`.

Youth/reserve pre-filter:

- `scripts/filter_youth_reserve_value_snapshots.py`
- Created, but workflow update wiring it in was blocked. May be optional because price-quality filter now rejects earlier.

Discovery diagnostics:

- `scripts/build_odds_api_io_discovery_efficiency_report.py`
- Outputs:
  - `output/latest/odds_api_io_discovery_efficiency_report.md`
  - `output/latest/odds_api_io_discovery_efficiency_summary.csv`
  - `output/latest/odds_api_io_discovery_efficiency_by_source.csv`
  - `output/latest/odds_api_io_top_event_match_candidates.csv`

Market expansion diagnostics:

- `scripts/build_odds_api_io_market_inventory_report.py`
- Scans raw Odds-API odds responses already fetched; no extra API calls.
- Outputs:
  - `output/latest/odds_api_io_market_inventory_report.md`
  - `output/latest/odds_api_io_market_inventory.csv`
  - `output/latest/odds_api_io_market_inventory_summary.csv`
  - `output/latest/market_expansion_notes.md`

## Active market

Currently active paper-test market is only football full-time result / 1X2 / match winner:

- home
- draw
- away

Raw Odds-API responses may contain more markets, but active parser only stores:

- `market_home_odds`
- `market_draw_odds`
- `market_away_odds`

## Market and sport expansion policy

The user wants ongoing investigation of other markets/sports if possible within existing requests/calls.

Current policy:

- Do not activate new markets directly in paper picks.
- First collect market inventory from raw responses already fetched.
- Best next market candidate: football Over/Under 2.5, if Bet365 raw data includes it.
- BTTS may be possible later.
- Handicap/spread should wait until reliable goal-difference model exists.
- Other sports stay inventory-only until each sport has separate model, filters, and settlement report.

## Human-facing files to check

Primary:

- `output/latest/paper_bets_human_report.md`

Supporting:

- `output/latest/paper_test_picks.md`
- `output/latest/paper_test_log_status.md`
- `output/latest/paper_bets_human_excluded.md`
- `output/latest/odds_api_io_price_quality_report.md`
- `output/latest/odds_api_io_discovery_efficiency_report.md`
- `output/latest/odds_api_io_market_inventory_report.md`
- `output/latest/market_expansion_notes.md`

Machine-readable:

- `output/latest/paper_test_picks.csv`
- `output/latest/paper_test_log_latest.csv`
- `data/predictions/paper_test_log.jsonl`
- `output/latest/settled_predictions.csv`
- `output/latest/paper_bets_human_summary.csv`
- `output/latest/odds_api_io_market_inventory_summary.csv`

## Settlement status

Earlier check showed new forward paper-picks were not clearly settled yet. `settled_predictions.csv` mostly contained older historical predictions at that time. The human report now includes a settled section, but settlement quality must be verified after the next workflow run.

Check:

- `output/latest/paper_bets_human_report.md`
- `output/latest/paper_test_log_status.md`
- `output/latest/settled_predictions.csv`
- `output/latest/performance_report.md` if present
- `output/latest/signal_performance_report.md` if present

If forward paper-picks still are not settled, next priority is improving settlement. Use existing free result sources first; consider `API-Football` only with low call cap.

## Known issue: youth/reserve teams

System was sensitive to youth/reserve teams. User found U23/reserve-like matches in paper picks. A kickoff mismatch was also observed for an U23 game. Treat this as a serious matching/filtering issue.

Mitigations added:

1. Human report hides U-/reserve rows.
2. Price-quality filter rejects U-/reserve rows before accepted price rows.

Filter terms include:

- `U23`, `U21`, `U19`, other `Uxx`
- `under xx`
- `reserve`, `reserves`, `reserver`
- `youth`
- `academy`
- `B team`
- `II`

Verify after next workflow run that these rows are gone from:

- `output/latest/odds_api_io_forward_prices.csv`
- `output/latest/automatic_forward_value_snapshots.csv`
- `output/latest/paper_test_picks.csv`
- `output/latest/paper_bets_human_report.md`

and rejected in:

- `output/latest/odds_api_io_forward_prices_rejected.csv`
- `output/latest/odds_api_io_price_quality_report.md`

## Important recent commits

- `bd06f486e1cf1bfa9a2402a5f2421e60cbff2820` – Restrict forward odds pipeline to Bet365
- `4cdd421db9fb453717a0c5a4a9271bdb90b27b1a` – Add human-readable paper bets report
- `43201be2f7b98c9b68bb6ceb3ae4e2552b795ae1` – Run human-readable paper bets report
- `5ad7e5967e5c081c0c00df2977960fa5bbe102c3` – Show kickoff time in human paper bets report
- `42db5bf6b98789c5225d1dcd313dbc98f27d3690` – Hide youth and reserve teams in human paper report
- `a23d76dd8fb7e652871144b3ae727c98dc841743` – Filter youth and reserve rows before paper picks (script created, workflow not wired)
- `bb31f5632c311a5a0f1dad5b852f63a3b0cae78b` – Reject youth and reserve matches in odds price quality filter
- `65c2c865a3ed33256bf45cec46025dd743f1d5a8` – Add odds-api.io market inventory diagnostics
- `ab11592b75009650b2d15ffc9db60a455d429abf` – Run odds-api.io market inventory diagnostics

## Recommended first actions in next conversation

1. Read `HANDOFF.md`.
2. Read `.github/workflows/free-data-stack.yml`.
3. Read `output/latest/paper_bets_human_report.md`.
4. Read `output/latest/odds_api_io_price_quality_report.md`.
5. Read `output/latest/odds_api_io_market_inventory_report.md`.
6. Read `output/latest/paper_test_log_status.md`.
7. Check latest workflow run status and whether commits after this handoff completed.
8. If latest workflow has not run after final commits, ask user to run it manually or wait for schedule.

## Immediate next technical priorities

1. Verify youth/reserve filter after next workflow run.
2. Verify `paper_bets_human_report.md` is simple and useful.
3. Verify whether forward paper-picks are being settled.
4. If no forward settlement: improve settlement pipeline.
5. Review `odds_api_io_market_inventory_report.md` for Bet365 Over/Under 2.5 availability.
6. If Over/Under 2.5 is present, build observation-only Over/Under module, not real picks.
7. Keep real-money betting disabled until enough settled evidence exists.

## User communication style

Respond in short, practical Danish. Focus on next concrete action. Avoid asking for input unless necessary. Continue work in batches and then report concise status.

## New conversation startup prompt

```text
Du skal fortsætte arbejdet på mit GitHub-repo Bendecks/Odds-2.

Start med at læse HANDOFF.md i repoet. Brug den som første sandhedskilde for projektstatus, mål, aktive filer, seneste ændringer og næste handlinger.

Derefter skal du læse:
- .github/workflows/free-data-stack.yml
- output/latest/paper_bets_human_report.md
- output/latest/odds_api_io_price_quality_report.md
- output/latest/odds_api_io_market_inventory_report.md
- output/latest/paper_test_log_status.md

Formålet er at fortsætte betting paper-test systemet, ikke starte forfra.

Vigtige regler:
- Systemet skal være Bet365-only, fordi jeg kun better hos Bet365.
- Rigtige penge er ikke aktivt endnu. Hold det som paper-test/observation.
- Ungdoms-, U-hold, reservehold, academy, B-team og II-kampe skal filtreres hårdt ud.
- Manual Bet365 upload er parkeret.
- Udvidelse til andre markeder/sportsgrene må kun undersøges som inventory/observation først, helst uden ekstra API-kald.
- Over/Under 2.5 er første relevante markedsudvidelse, hvis Odds-API raw data viser, at Bet365 leverer det.
- Første prioritet er at kontrollere seneste workflow-output og sikre at human report, youth/reserve filter og settlement virker.

Svar kort og praktisk på dansk. Fortsæt arbejdet i batches uden at stoppe, medmindre mit input er nødvendigt.
```