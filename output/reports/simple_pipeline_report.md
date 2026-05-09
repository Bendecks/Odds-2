# Odds 2 — Simple Gemini Pipeline

Generated: 2026-05-09T20:42:54Z
- Analysis version: simple_decision_v5_deduped_source_audit
- Files processed: 5
- Raw matches: 38
- Valid matches: 37
- Unique valid matches: 33
- Duplicate matches removed: 4
- Decision matches: 12
- Rejected matches: 1
- Gemini decision records: 1
- PAPER_BET logged: 1
- Blocked decisions: 0
- Passes returned: 11
- Decision error: `None`
- Grounding sources: 0

## PAPER_BET

### Randers FC vs OB
- Selection: 2
- Odds: 3.1
- Stake units: 0.5
- Confidence: 0.65
- Verified source tiers: `['unknown', 'unknown']`
- Value case: The odds of 3.1 for an away win offer good value considering OB's superior league position and recent head-to-head performance against a struggling Randers side.
- Evidence: OB's strong league form and recent dominant away win against Randers FC indicate value in the away odds.
- Evidence sources:
  - form | Danish Superligaen Official | verified=unknown | declared=tier2 |  | OB is significantly higher in the Danish Superligaen table with 49 points compared to Randers FC's 31 points.
  - form | Various Sports News | verified=unknown | declared=tier2 |  | OB recently secured a convincing 3-1 away victory against Randers FC on April 19, 2026.

## Pass reasons
- Tottenham vs Leeds: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Man City vs Crystal Palace: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Aston Villa vs Liverpool: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Millwall vs Hull: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Southampton vs Middlesbrough: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Rayo Vallecano vs Girona: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Celta Vigo vs Levante: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Real Betis vs Elche: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Osasuna vs Atletico Madrid: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Espanyol vs Athletic Bilbao: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.
- Villarreal vs Sevilla: no_pass_reason_returned — Gemini returned no explicit pass reason for this analyzed match.

## Duplicate matches removed
- Randers FC vs OB: kept inbox/possible_bets/20260509-205650_possible_bets_3646.pdf, removed inbox/possible_bets/20260509-200532_possible_bets_8036.pdf
- Tottenham vs Leeds: kept inbox/possible_bets/20260509-205650_possible_bets_3646.pdf, removed inbox/possible_bets/20260509-200532_possible_bets_8036.pdf
- Millwall vs Hull: kept inbox/possible_bets/20260509-205650_possible_bets_3646.pdf, removed inbox/possible_bets/20260509-200532_possible_bets_8036.pdf
- Rayo Vallecano vs Girona: kept inbox/possible_bets/20260509-205650_possible_bets_3646.pdf, removed inbox/possible_bets/20260509-200532_possible_bets_8036.pdf

## Gemini grounding sources
No grounding sources returned or parsed.

## Grounding debug
`{"top_level_keys": ["candidates", "usageMetadata", "modelVersion", "responseId"], "candidate_keys": ["content", "finishReason", "index", "groundingMetadata"], "grounding_metadata_keys": ["searchEntryPoint", "webSearchQueries"], "text_preview": "Here are the practical PICK/PASS decisions for the provided football matches:\n\nPICK | match_05e26de40ea79b92 | Randers FC vs OB | 2 | 3.1 | 0.65 | 0.5 units | OB is significantly higher in the Danish Superligaen table with 49 points compared to Randers FC's 31 points. OB also recently secured a convincing 3-1 away victory against Randers FC on April 19, 2026. The odds of 3.1 for an away win offer good value considering OB's superior league position and recent head-to-head performance against a struggling Randers side. [cite: 4, 8,", "grounded_text_preview": "Here are the practical PICK/PASS decisions for the provided football matches:\n\nPICK | match_05e26de40ea79b92 | Randers FC vs OB | 2 | 3.1 | 0.65 | 0.5 units | OB is significantly higher in the Danish Superligaen table with 49 points compared to Randers FC's 31 points. OB also recently secured a convincing 3-1 away victory against Randers FC on April 19, 2026. The odds of 3.1 for an away win offer good value considering OB's superior league position and recent head-to-head performance against a struggling Randers side. [cite: 4, 8,", "structured_text_preview": "{\n  \"analysis_version\": \"final_pick_decision_v1\",\n  \"summary\": {\n    \"matches_analyzed\": 1,\n    \"picks_count\": 1,\n    \"pass_count\": 0,\n    \"overall_note\": \"One pick identified based on strong form and head-to-head performance.\"\n  },\n  \"picks\": [\n    {\n      \"match_id\": \"match_05e26de40ea79b92\",\n      \"match\": \"Randers FC vs OB\",\n      \"selection\": \"2\",\n      \"selection_label\": \"away\",\n      \"odds\": 3.1,\n      \"decision\": \"PAPER_BET\",\n      \"confidence_score\": 0.65,\n      \"stake_units\": 0.5,\n      \"value_case\": \"The odds of 3.1 for an away win offer good value considering OB's superior league position and recent head-to-head performance against a struggling Randers side.\",\n      \"main_signals\": [\n        \"Superior League Position\",\n        \"Recent Head-to-Head Win\"\n      ],\n      \"evidence_summary\": \"OB's strong league form and recent dominant away win against Randers FC indicate value in the away odds.\",\n      \"evidence_items\": [\n        {\n          \"type\": \"form\",\n          \"signal\": \"OB is significantly higher in the Danish Superligaen table with 49 points compared to Randers FC's 31 points.\",\n          \"supports_selection\": true,\n          \"importance\": \"high\",\n          \"source"}`
