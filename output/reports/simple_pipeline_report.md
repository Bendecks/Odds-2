# Odds 2 — Simple Gemini Pipeline

Generated: 2026-05-09T18:52:36Z
- Analysis version: simple_decision_v5_deduped_source_audit
- Files processed: 5
- Raw matches: 17
- Valid matches: 17
- Unique valid matches: 17
- Duplicate matches removed: 0
- Decision matches: 12
- Rejected matches: 0
- Gemini decision records: 1
- PAPER_BET logged: 0
- Blocked decisions: 1
- Passes returned: 12
- Decision error: `None`
- Grounding sources: 2

No PAPER_BET passed safety gates.

## Blocked Gemini suggestions

### FC Nordsjælland vs FC Midtjylland
- Suggested selection: PASS
- Blocked by safety: `no_verified_tier1_source`
- Verified source tiers: `['unknown', 'unknown']`
- Redirect source count: 0
- Value case: short
- Evidence sources:
  - form | analyst_notes | verified=unknown | declared=unknown | https://example.com/analyst_notes | FC Midtjylland is in better recent form (D-W-W-W-D) compared to FC Nordsjælland (D-W-D-L-D) in their last five league games.
  - context | analyst_notes | verified=unknown | declared=unknown | https://example.com/analyst_notes | FC Midtjylland has a superior historical head-to-head record against FC Nordsjælland, winning 23 out of

## Pass reasons
- FC Nordsjælland vs FC Midtjylland: blocked_by_safety:no_verified_tier1_source — FC Midtjylland is in better recent form and has a superior historical head-to-head record.
- Vejle vs FC Fredericia: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Silkeborg IF vs FC København: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Brøndby vs AGF: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Randers FC vs OB: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Burnley vs Aston Villa: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Crystal Palace vs Everton: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Nottm Forest vs Newcastle: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- West Ham vs Arsenal: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Tottenham vs Leeds: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Millwall vs Hull: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Real Sociedad vs Real Betis: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.

## Duplicate matches removed

## Gemini grounding sources
- footystats.org — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUFhqTFtOGDZQJl9WH8dKGa1BFIZ-EJWGz_sC6t7ZOkRfkjJfxvQEAveevrV19W688OB1Tvw6WIsiVjWyzHyfdTMw_l3fP2U3nAMm06WqPCQ-uC31h5nnWJK-brGc20R9S_StlZggprrEYLHlHrpN52MSDDQbnrJj-wnfN5MLH5hdO-L1vlA==
- fotmob.com — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFDvXZS-bmD1ifCEznq1XeYM64M5JVHwYBFdaNH0hfPyXPEmMGYXagSqmniHXPUvXaaeSPUzOR11BlKL3g2543fUiuvaUcL_ReCg2IoQGupLvshlbb82-y8LwZduxAdmTJGpl_wBfglo6NGc_k1DjSFIKY=

## Grounding debug
`{"top_level_keys": ["candidates", "usageMetadata", "modelVersion", "responseId"], "candidate_keys": ["content", "finishReason", "index", "groundingMetadata"], "grounding_metadata_keys": ["searchEntryPoint", "groundingChunks", "groundingSupports", "webSearchQueries"], "text_preview": "FC Nordsjælland vs FC Midtjylland\nMATCH_ID: match_01c571330e7f8dc7 | MATCH: FC Nordsjælland vs FC Midtjylland | SELECTION_OR_PASS: 2 | ODDS: 2.15\n*   FC Midtjylland is in better recent form (D-W-W-W-D) compared to FC Nordsjælland (D-W-D-L-D) in their last five league games.\n*   FC Midtjylland has a superior historical head-to-head record against FC Nordsjælland, winning 23 out of ", "grounded_text_preview": "FC Nordsjælland vs FC Midtjylland\nMATCH_ID: match_01c571330e7f8dc7 | MATCH: FC Nordsjælland vs FC Midtjylland | SELECTION_OR_PASS: 2 | ODDS: 2.15\n*   FC Midtjylland is in better recent form (D-W-W-W-D) compared to FC Nordsjælland (D-W-D-L-D) in their last five league games.\n*   FC Midtjylland has a superior historical head-to-head record against FC Nordsjælland, winning 23 out of ", "structured_text_preview": "{\n  \"analysis_version\": \"simple_decision_v7_concise_grounded_notes\",\n  \"picks\": [\n    {\n      \"match_id\": \"match_01c571330e7f8dc7\",\n      \"match\": \"FC Nordsjælland vs FC Midtjylland\",\n      \"selection\": \"2\",\n      \"selection_label\": \"away\",\n      \"odds\": 2.15,\n      \"decision\": \"PAPER_BET\",\n      \"confidence_score\": 0.0,\n      \"stake_units\": 0.0,\n      \"value_case\": \"short\",\n      \"evidence_summary\": \"FC Midtjylland is in better recent form and has a superior historical head-to-head record.\",\n      \"evidence_items\": [\n        {\n          \"type\": \"form\",\n          \"signal\": \"FC Midtjylland is in better recent form (D-W-W-W-D) compared to FC Nordsjælland (D-W-D-L-D) in their last five league games.\",\n          \"supports_selection\": true,\n          \"importance\": \"medium\",\n          \"source_tier\": \"unknown\",\n          \"source_type\": \"unknown\",\n          \"source_name\": \"analyst_notes\",\n          \"source_url\": \"https://example.com/analyst_notes\",\n          \"published_or_checked_date\": \"\"\n        },\n        {\n          \"type\": \"context\",\n          \"signal\": \"FC Midtjylland has a superior historical head-to-head record against FC Nordsjælland, winning 23 out of\",\n          \"supports_select"}`
