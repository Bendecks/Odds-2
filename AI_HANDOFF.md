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
2. `output/latest/project_handoff_report.md`
3. `output/latest/project_status_report.md`
4. `output/latest/daily_decision_report.md`
5. `output/latest/gemini_ai_review.md`
6. `output/latest/model_adjustment_recommendation.md`
7. `output/latest/forward_test_readiness_report.md`
8. `output/latest/data_leakage_report.md`
9. `output/latest/clv_trend_report.md`
10. `output/latest/probability_band_report.md`

## Kendt status ved denne handoff

Seneste sikre status i samtalen:

- Workflow havde kørt grønt flere gange.
- Systemet havde ca. 189 logged predictions og 189 settled predictions.
- Gemini API virkede og skrev `gemini_ai_review.md`.
- Gemini vurderede systemet som paper-test-ready, men med negativ CLV og behov for calibration.
- Systemets største svaghed er ikke længere pipeline, men model quality/calibration/CLV.
- Systemet er IKKE klar til real-money betting.
- Systemet bør fortsat være paper/research-only.

## Vigtigste eksisterende funktioner

Data:

- football-data.co.uk historical data
- multi-league ingestion
- multi-season ingestion
- ClubElo snapshot

Model:

- Poisson model
- probability shrinkage
- market proxy odds
- EV calculation
- candidate filtering
- confidence tiers

Tracking:

- prediction logging
- settlement
- CLV tracking
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

## Aktuelle strategiske fokusområder

Næste udvikling bør handle om:

1. Probability calibration
2. Reducere overconfidence, især i højere probability bands
3. Forbedre CLV
4. Skelne historisk proxy-evaluering fra ægte forward-testing
5. Gøre forward paper tracking mere ægte
6. Eventuelt begynde på league-specific filters eller calibration

Undgå lige nu:

- real-money betting alerts
- for tung UI
- live odds scraping
- komplicerede enterprise-løsninger
- at tilføje flere features før calibration og CLV forbedres

## Typiske fejl der er opstået

De fleste fejl skyldtes:

- schema drift mellem scripts
- nye rapporter der forventede kolonner, som ikke fandtes endnu
- tomme CSV/parquet filer
- workflow-rækkefølge
- GitHub auto-commit race conditions
- forkerte filnavne i workflow

Når der opstår fejl:

1. Tjek seneste `free_data_status.md`.
2. Tjek hvilken ny rapport/script der lige blev tilføjet.
3. Tjek om scriptet forventer forkerte kolonner.
4. Gør scripts robuste over for tomme/manglende data.
5. Commit rettelsen og lad workflow køre igen.

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

## Næste konkrete handling

Start næste samtale med at læse statusfilerne og tjek seneste workflow-output. Derefter fortsæt med probability calibration og forward-test separation.
