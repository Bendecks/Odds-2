# Odds 2 — Simple Gemini Pipeline

Generated: 2026-05-09T17:58:15Z
- Analysis version: simple_decision_v5_deduped_source_audit
- Files processed: 5
- Raw matches: 5
- Valid matches: 5
- Unique valid matches: 5
- Duplicate matches removed: 0
- Decision matches: 5
- Rejected matches: 0
- Gemini decision records: 1
- PAPER_BET logged: 0
- Blocked decisions: 1
- Passes returned: 5
- Decision error: `None`
- Grounding sources: 0

No PAPER_BET passed safety gates.

## Blocked Gemini suggestions

### Vejle vs FC Fredericia
- Suggested selection: PASS
- Blocked by safety: `no_verified_tier1_source`
- Verified source tiers: `['unknown', 'unknown', 'unknown']`
- Redirect source count: 3
- Value case: Vejle is in very poor form, having lost 4 of their last 5 matches, and is significantly impacted by multiple key injuries. In contrast, FC Fredericia has no reported unavailable players and has shown better recent form, making the odds for an away win appear undervalued.
- Evidence sources:
  - form | FotMob | verified=unknown | declared=tier2 | https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFRFgV-AFp7cSpH_7YvvoNmRdhyVgE0xUWTq6_Tp48TnbD8m9VDO1TjfvmrXtBlqY5ZW85ZahDN1yuqWQA9unDAk-RCHF1ZpD2QP8GVZIri49XNHGQYwyzZZ4qxnO6mzd2aJLIuaH7rDEMxdxD60pEthW9t | Vejle has lost 4 of their last 5 matches in the Superligaen Relegation Group, including a 1-0 loss to Randers FC and a 3-0 loss to FC København.
  - injury | FotMob | verified=unknown | declared=tier2 | https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEALu4yUC7ck1wbGPB9TG9FaqAMYbMhOHJzR57wWP93tpQyEdhRnaNMWmqBp0A8oiXsRd-rmylqxpOYLvk0dKvXu3Em55FN1SMwCGaEOwEcNDpefMsUHN_SZgS1Whfq31u11EexmQxNwnQoudXkisQA4en4JbXnxS_vgAm4 | Vejle Boldklub has several unavailable players due to injury, including Damian van Bruggen, Stefan Velkov, Lundrim Hetemi, Tobias Lauritsen, Anders K. Jacobsen, and Ransford Amoo.
  - lineup | FotMob | verified=unknown | declared=tier2 | https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEALu4yUC7ck1wbGPB9TG9FaqAMYbMhOHJzR57wWP93tpQyEdhRnaNMWmqBp0A8oiXsRd-rmylqxpOYLvk0dKvXu3Em55FN1SMwCGaEOwEcNDpefMsUHN_SZgS1Whfq31u11EexmQxNwnQoudXkisQA4en4JbXnxS_vgAm4 | FC Fredericia has no unavailable players reported.

## Pass reasons
- FC Nordsjælland vs FC Midtjylland: conflicting signals — Conflicting injury reports for FC Midtjylland from different source tiers, making it difficult to assess their true strength. Insufficient clear edge.
- Silkeborg IF vs FC København: odds too low — FC København's odds are too low (1.8) given Silkeborg's recent good form, despite FCK's dominant head-to-head win. Injury status for FCK not clearly established from Tier 2 sources.
- Brøndby vs AGF: insufficient evidence — Mixed recent form for both teams and while Brøndby has a good home head-to-head record, there isn't enough strong, verifiable evidence to confidently back a selection.
- Randers FC vs OB: insufficient evidence — Lack of strong form indicators, recent head-to-head data, or significant injury news from Tier 2 sources for either team to make a confident pick.
- Vejle vs FC Fredericia: blocked_by_safety:no_verified_tier1_source — Vejle has lost 4 of their last 5 matches and has several key players out due to injury. FC Fredericia has no reported injuries and has shown better recent form.

## Duplicate matches removed

## Gemini grounding sources
No grounding sources returned or parsed.

## Grounding debug
`{"top_level_keys": ["candidates", "usageMetadata", "modelVersion", "responseId"], "candidate_keys": ["content", "finishReason", "index", "groundingMetadata"], "grounding_metadata_keys": ["searchEntryPoint", "webSearchQueries"], "text_preview": "```json\n{\n \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n \"picks\": [\n  {\n   \"match_id\": \"match_fa7f1b2dd0fbe2c6\",\n   \"match\": \"Vejle vs FC Fredericia\",\n   \"selection\": \"2\",\n   \"selection_label\": \"away\",\n   \"odds\": 2.15,\n   \"decision\": \"PAPER_BET\",\n   \"confidence_score\": 0.5,\n   \"stake_units\": 0.5,\n   \"value_case\": \"Vejle is in very poor form, having lost 4 of their last 5 matches, and is significantly impacted by multiple key injuries. In contrast, FC Fredericia has no reported unavailable players and has shown better recent form, making the odds for an away win appear undervalued.\",\n   \"evidence_summary\": \"Vejle has lost 4 of their last 5 matches and has several key players out due to injury. FC Fredericia has no reported injuries and has shown better recent form.\",\n   \"evidence_items\": [\n    {\n     \"type\": \"form\",\n     \"signal\": \"Vejle has lost 4 of their last 5 matches in the Superligaen Relegation Group, including a 1-0 loss to Randers FC and a 3-0 loss to FC Køben", "grounded_text_preview": "```json\n{\n \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n \"picks\": [\n  {\n   \"match_id\": \"match_fa7f1b2dd0fbe2c6\",\n   \"match\": \"Vejle vs FC Fredericia\",\n   \"selection\": \"2\",\n   \"selection_label\": \"away\",\n   \"odds\": 2.15,\n   \"decision\": \"PAPER_BET\",\n   \"confidence_score\": 0.5,\n   \"stake_units\": 0.5,\n   \"value_case\": \"Vejle is in very poor form, having lost 4 of their last 5 matches, and is significantly impacted by multiple key injuries. In contrast, FC Fredericia has no reported unavailable players and has shown better recent form, making the odds for an away win appear undervalued.\",\n   \"evidence_summary\": \"Vejle has lost 4 of their last 5 matches and has several key players out due to injury. FC Fredericia has no reported injuries and has shown better recent form.\",\n   \"evidence_items\": [\n    {\n     \"type\": \"form\",\n     \"signal\": \"Vejle has lost 4 of their last 5 matches in the Superligaen Relegation Group, including a 1-0 loss to Randers FC and a 3-0 loss to FC København.\",\n     \"supports_selection\": true,\n     \"importance\": \"high\",\n     \"source_tier\": \"tier2\",\n     \"source_type\": \"sports_media\",\n     \"source_name\": \"FotMob\",\n     \"source_url\": \"https://vertexais", "structured_text_preview": "{\n \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n \"picks\": [\n  {\n   \"match_id\": \"match_fa7f1b2dd0fbe2c6\",\n   \"match\": \"Vejle vs FC Fredericia\",\n   \"selection\": \"2\",\n   \"selection_label\": \"away\",\n   \"odds\": 2.15,\n   \"decision\": \"PAPER_BET\",\n   \"confidence_score\": 0.5,\n   \"stake_units\": 0.5,\n   \"value_case\": \"Vejle is in very poor form, having lost 4 of their last 5 matches, and is significantly impacted by multiple key injuries. In contrast, FC Fredericia has no reported unavailable players and has shown better recent form, making the odds for an away win appear undervalued.\",\n   \"evidence_summary\": \"Vejle has lost 4 of their last 5 matches and has several key players out due to injury. FC Fredericia has no reported injuries and has shown better recent form.\",\n   \"evidence_items\": [\n    {\n     \"type\": \"form\",\n     \"signal\": \"Vejle has lost 4 of their last 5 matches in the Superligaen Relegation Group, including a 1-0 loss to Randers FC and a 3-0 loss to FC København.\",\n     \"supports_selection\": true,\n     \"importance\": \"high\",\n     \"source_tier\": \"tier2\",\n     \"source_type\": \"sports_media\",\n     \"source_name\": \"FotMob\",\n     \"source_url\": \"https://vertexaisearch.cl"}`
