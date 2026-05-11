# AI Handoff – Odds-2

Dette dokument er skrevet til en ny ChatGPT-samtale, så projektet kan fortsætte uden at genopbygge kontekst.

## Projektets mål

Byg et gratis, GitHub-baseret betting research-system til fodbold, der kan:

- hente gratis historiske data
- generere pre-match model predictions
- sammenligne modelens fair odds med market odds/proxy odds
- logge predictions
- settle predictions automatisk
- beregne CLV
- evaluere performance, risk og calibration
- bruge Gemini API til meta-review, ikke til magiske picks
- køre automatisk via GitHub Actions

Systemet må ikke fremstilles som profitabelt eller klar til real-money betting, før CLV, sample size og forward-test dokumenterer det.

## Vigtigste principper

1. Arbejd i store batches, så brugeren ikke skal bekræfte hvert lille trin.
2. Når brugeren skriver at workflow er kørt, skal AI selv tjekke repoets outputfiler.
3. Fokus er endemålet, ikke over-engineering.
4. Ret fejl hurtigt, men fortsæt fremdrift.
5. Brug Gemini API hvor det giver mening: meta-review, diagnostics, prioritering og analyse. Ikke som direkte odds-orakel.
6. Hold real-money frarådet indtil systemet har positiv/neutral CLV, nok sample og lav leakage-risk.
7. Skeln altid mellem:
   - historical proxy research
   - paper forward-testing
   - real-money readiness

## Workflow

Primært workflow:

`.github/workflows/free-data-stack.yml`

Det kører:

- manuelt via `workflow_dispatch`
- ved push til main
- automatisk hver 12. time via cron: `0 */12 * * *`

Workflowet henter data, bygger modellen, logger predictions, forsøger settlement, beregner CLV og skriver rapporter i `output/latest/`.

## Centrale outputfiler at læse først

Læs disse i starten af en ny samtale:

1. `output/latest/free_data_status.md`
2. `output/latest/project_goal_readiness_report.md`
3. `output/latest/project_handoff_report.md`
4. `output/latest/project_status_report.md`
5. `output/latest/daily_decision_report.md`
6. `output/latest/gemini_ai_review.md`
7. `output/latest/model_adjustment_recommendation.md`
8. `output/latest/forward_test_readiness_report.md`
9. `output/latest/data_leakage_report.md`
10. `output/latest/clv_trend_report.md`
11. `output/latest/probability_band_report.md`
12. `output/latest/odds_api_io_forward_prices.md`
13. `output/latest/forward_price_coverage_report.md`
14. `output/latest/paper_test_log_status.md`
15. `output/latest/proxy_candidate_observations.md`
16. `output/latest/proxy_candidate_explanation_report.md`

## Kendt status ved denne handoff

Seneste sikre status i samtalen:

- Workflow havde kørt grønt flere gange.
- Systemet har historical proxy research, automatic forward price proxy, paper-test picks, proxy-candidate observations og readiness reports.
- Gemini API virkede og skrev `gemini_ai_review.md`.
- Gemini vurderede systemet som paper-test-ready, men med negativ CLV og behov for calibration.
- Systemets største svaghed er ikke længere pipeline, men model quality/calibration/CLV og forward sample size.
- Systemet er IKKE klar til real-money betting.
- Systemet bør fortsat være paper/research-only.

## Odds-API.io status og regler

Projektet har nu en forsigtig Odds-API.io integration.

Se også:

`ODDS_API_IO_NOTES.md`

Vigtig dokumentation brugeren fandt:

- AI-ready docs: `https://docs.odds-api.io/llms-full.txt`
- OpenAPI spec: `https://docs.odds-api.io/api-reference/openapi.json`
- Base URL: `https://api.odds-api.io/v3`
- Auth: `apiKey` som query parameter

Relevante endpoints:

- `GET /events/search?apiKey=KEY&query=TEAM` søger upcoming events og returnerer op til 10.
- `GET /odds?apiKey=KEY&eventId=EVENT_ID&bookmakers=Bet365,Unibet` henter odds for én event.
- `GET /odds/multi?apiKey=KEY&eventIds=ID1,ID2,ID3&bookmakers=Bet365,Unibet` henter odds for op til 10 events i ét kald.
- `GET /bookmakers` kræver ikke auth og kan bruges til at validere bookmaker-navne.
- `GET /events?apiKey=KEY&sport=football&bookmaker=Bet365` kan finde events med Bet365-dækning, men workflowet prioriterer p.t. model-covered `/events/search`.
- `GET /value-bets?...` må kun bruges som diagnostik senere, ikke som direkte signal.
- Dropping odds kan kræve paid plan og må ikke være afhængighed på free-plan.

Aktuel strategi:

1. Byg model-covered forward fixture predictions.
2. Vælg search queries fra `forward_fixture_predictions.csv` først.
3. Fallback til `football_data_upcoming_fixtures.csv`.
4. Brug `/events/search` på op til `ODDS_API_IO_MAX_PRICE_EVENTS` queries.
5. Saml event IDs.
6. Brug `/odds/multi` én gang for de valgte event IDs.
7. Parse `EventResponse.bookmakers -> markets -> odds -> home/draw/away`.
8. Skriv output som paper/proxy-only.

Aktuelle workflow caps:

- `ODDS_API_IO_MAX_CALLS=6`
- `ODDS_API_IO_MAX_EVENTS=10`
- `ODDS_API_IO_MAX_PRICE_EVENTS=3`
- `API_FOOTBALL_MAX_CALLS=0`

Forventet typisk Odds-API.io forbrug:

- op til 3 search calls
- 1 multi-odds call
- typisk 2-4 calls/run, max 6

Vigtige outputfiler:

- `output/latest/odds_api_io_forward_prices.md`
- `output/latest/odds_api_io_forward_price_status.csv`
- `output/latest/odds_api_io_forward_prices.csv`
- `output/latest/odds_api_io_forward_fixtures.csv`
- `output/latest/forward_price_coverage_report.md`
- `output/latest/forward_price_coverage_summary.csv`

Odds-API.io output må ikke åbne real-money gate alene.

## Vigtigste eksisterende funktioner

Data:

- football-data.co.uk historical data
- multi-league ingestion
- multi-season ingestion
- ClubElo snapshot
- Football-Data upcoming odds proxy
- Odds-API.io capped fresh API proxy

Model:

- Poisson model
- probability shrinkage
- market proxy odds
- automatic forward value snapshots
- EV calculation
- proxy candidate observations
- candidate filtering
- confidence tiers

Tracking:

- prediction logging
- settlement
- CLV tracking
- paper-test logging
- deduped paper-test reporting
- forward price coverage reporting
- performance reports
- bankroll simulation
- risk reports

Diagnostics:

- market alignment
- model health
- probability bands
- probability distribution
- league performance
- signal performance
- filter feedback
- sample size
- sample reliability
- data leakage
- forward-test readiness
- daily decision
- Gemini AI review
- project handoff
- proxy candidate explanation
- forward price coverage

## Aktuelle strategiske fokusområder

Næste udvikling bør handle om:

1. Øge fresh API coverage forsigtigt uden at spilde API-kald.
2. Bruge deduped paper-test counts i alle readiness vurderinger.
3. Få flere settled forward rows.
4. Probability calibration.
5. Reducere overconfidence, især store underdog/away-EV spikes.
6. Forbedre CLV.
7. Skelne historisk proxy-evaluering fra ægte forward-testing.
8. Gøre forward paper tracking mere ægte.
9. League-specific filters eller calibration når sample er større.

Undgå lige nu:

- real-money betting alerts
- for tung UI
- paid-plan-only endpoints som afhængighed
- at bruge Odds-API.io value-bets direkte som bettingforslag
- komplicerede enterprise-løsninger
- at tilføje flere features før calibration, CLV og coverage forbedres

## Typiske fejl der er opstået

De fleste fejl skyldtes:

- schema drift mellem scripts
- nye rapporter der forventede kolonner, som ikke fandtes endnu
- tomme CSV/parquet filer
- workflow-rækkefølge
- GitHub auto-commit race conditions
- forkerte filnavne i workflow
- API-endpoints der returnerer tomme data, selv om kaldet er teknisk OK
- paper-test log inflation via dubletter

Når der opstår fejl:

1. Tjek seneste `free_data_status.md`.
2. Tjek `odds_api_io_forward_prices.md`, hvis det handler om odds.
3. Tjek hvilken ny rapport/script der lige blev tilføjet.
4. Tjek om scriptet forventer forkerte kolonner.
5. Gør scripts robuste over for tomme/manglende data.
6. Commit rettelsen og lad workflow køre igen.

## Gemini-regel

Gemini skal bruges til:

- meta-review af projektstatus
- modelkritik
- prioritering af næste udvikling
- fortolkning af diagnostics
- calibration/action-plan forslag

Gemini skal ikke bruges til:

- direkte at vælge bets uden data
- at overskrive statistiske rapporter
- at anbefale real-money betting alene

## Beslutningsregel

Hvis `daily_decision_report.md` siger andet end paper-track, skal picks ignoreres som bettingforslag.

Hvis `data_leakage_report.md` har risiko over low, skal resultater tolkes som proxy research, ikke forward validation.

Hvis CLV er negativ, er systemet research-only.

Hvis `project_goal_readiness_report.md` ikke har nok deduped forward observations og settled forward rows, er systemet ikke real-money ready.

## Næste konkrete handling

Start næste samtale med at læse statusfilerne og tjek seneste workflow-output. Derefter:

1. Tjek om `/odds/multi` virker i `odds_api_io_forward_prices.md`.
2. Tjek fresh API coverage i `forward_price_coverage_report.md`.
3. Tjek deduped paper-test rows i `paper_test_log_status.md`.
4. Ret fejl hurtigt.
5. Fortsæt med probability calibration og forward-test separation.
