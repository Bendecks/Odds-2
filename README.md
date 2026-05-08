# Odds 2

Data Integrity Foundation V1 for iPhone → bet365 PDF → GitHub Actions.

This repo intentionally starts with data quality, not betting rules.

## Phase 1 goal

1. Receive bet365 PDF/text input from iPhone.
2. Extract raw text and layout metadata.
3. Parse football 1X2 market observations.
4. Normalize all times to UTC while preserving local Denmark display time.
5. Canonical-match team names with alias/truncation/fuzzy logic.
6. Calculate deterministic parser confidence.
7. Generate stable event/market/observation IDs.
8. Detect duplicates, odds movement and parser conflicts.
9. Append an audit trail to `data/pick_tracker.jsonl`.
10. Write human-readable reports and debug text.

## Key outputs

- `output/latest/parser_output.json`
- `output/latest/observations.json`
- `output/latest/dedupe_report.json`
- `output/reports/latest_report.md`
- `data/pick_tracker.jsonl`
- `data/team_alias_suggestions.json`

## Workflow

Run GitHub Action: **Process bet365 input**.

Input folder:

```text
inbox/possible_bets/
```

Supported files in V1:

```text
.pdf
.txt
.md
.json
```

PDF extraction uses pypdf first, then PyMuPDF fallback. OCR/Gemini Vision is intentionally not active in Phase 1; files without a useful text layer are logged as extraction failures/shadow-only.
