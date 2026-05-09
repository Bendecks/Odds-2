# Odds 2 — Simple Gemini Pipeline

Generated: 2026-05-09T17:50:45Z
- Analysis version: simple_decision_v5_deduped_source_audit
- Files processed: 5
- Raw matches: 5
- Valid matches: 5
- Unique valid matches: 5
- Duplicate matches removed: 0
- Decision matches: 5
- Rejected matches: 0
- Gemini decision records: 0
- PAPER_BET logged: 0
- Blocked decisions: 0
- Passes returned: 5
- Decision error: `None`
- Grounding sources: 8

No PAPER_BET passed safety gates.

## Pass reasons
- FC Nordsjælland vs FC Midtjylland: json_not_stable — Gemini structure output was not valid JSON; fail-closed PASS.
- Vejle vs FC Fredericia: json_not_stable — Gemini structure output was not valid JSON; fail-closed PASS.
- Silkeborg IF vs FC København: json_not_stable — Gemini structure output was not valid JSON; fail-closed PASS.
- Brøndby vs AGF: json_not_stable — Gemini structure output was not valid JSON; fail-closed PASS.
- Randers FC vs OB: json_not_stable — Gemini structure output was not valid JSON; fail-closed PASS.

## Duplicate matches removed

## Gemini grounding sources
- plbold.dk — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHPyPkyY1iJ7mHQyfV9l6Dn6RkuiUlntbGznq8qm1BDzYQRRpYq0nRZgmkN8SY4tTYOLVEOQ_ISuEIei45uRUBjxQBdIzbtxhSgpc7pe6757fKH9_m3qRU_egPg4sSoMqrtNPa8OYjkBrlnC2qN_dGlzaVRgFh0UKUASXc5WVb4gtl-mFwUrG0e
- fcm.dk — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH3A6fMpd9Ywdwx7gmYwZQHU1Mjqj6gf_jIxa2LoLoxpm3WrlzJqlLkSMlgUrlNq7YrBS6W1yMQOBV2sT-dPNMCmiG9vIwNTLlbd6MZlFTVRFnYS6GyAxLbRZ-QyvGb9xQn316VCzXC
- fcm.dk — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjQkKl0mcGm6jGkre_JXzLsePFkPywPFc54Yz6TEluC5_LIokbDcPiAwx2A11C6EPjdemz4amQ34ItwXA_k_OOBODiJ1Z97UAb4duuXu-3Wq18JrmVu8NSOpI6GBVBQkkKagDBrBHEk7oUsBL4yIKDshc=
- fcm.dk — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEynxAmZrb9-8gKaFU7jI9WUm4-XFrCTjv7dkyDypAuCRCcx9LnIhXZ2W4aYQeJzh7h7EYJA9-tE-h45tqrjCHMK_Zkrnh8mAhhdAOsQ5DbbKF378rpk1fKrRgd0deB2oUCxrFGozju-W3UopX1benvTa4U4SoiAQJx8Inl
- brondby.com — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH65IS54kgNP8dUof2iESH27x8KjoNrL5dMewkApYaK3yHpvDeRQcVo61AzcBZanMC8YuZnzof-iMOMdhpgLlkqjur0AOtX_SWx7U-cL1g_9IX_BTPKiw_IasPLaknn83Y0Zj_-YFJVpMIKxEjCx-0z_N9PnsBA0uQjCNaPKbshFWbIvkKBG-L7wVgRRajtrNqSNS-ASQ==
- campo.dk — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHelLO1fW_O2pa4GuMxHtMAbRHCVBAZAw0E5s7uMS37L4l6hIfXNjbkm5mQQPPaPk9t_JIgUY2yOwjv4uW8pQV1YyUm6xoLVe9zEpoh02-Z354sVAy2tNlt3bmC95ir23xGwqx3WOCzYOGE4vhfN7RIkytxDKk1J3h7MQEkQC6JpulWKp9xLqU=
- tipsbladet.dk — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6Ykr348a8boAXKqj3yUa1wIHWIe2B8ex4w20PJz_FBJ5Em2UL1nSFDgfMpK7gbU8_IDcsgJmiQ1_2yjJ2J4lMZ5w6idHfPNTNUWAzOo3N4uEDtXb8Lypf6BsbMkMVOJczjLQhl46CBk0R
- spilxperten.com — vertexaisearch.cloud.google.com — https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErBOX2299WUD_LxhVxa8L8MLghQn3diBjRx6KQIslst8OGhSJiCrw1BGeuWsIjMOTTUfI-Ol17cEZJt-_4Wpj5eA--4ca918AvzF3tZ1XT1CRmALZIDkHBvsOm-XymJOfW5b_Y573IfrFFQ65QWeogoo-plX1Z3EY_3Xr2j4yOSMV31bCob_KjqhUYnODThUSS_GOIrQ==

## Grounding debug
`{"top_level_keys": ["candidates", "usageMetadata", "modelVersion", "responseId"], "candidate_keys": ["content", "finishReason", "index", "groundingMetadata"], "grounding_metadata_keys": ["searchEntryPoint", "groundingChunks", "groundingSupports", "webSearchQueries"], "text_preview": "```json\n{\n \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n \"picks\": [\n  {\n   \"match_id\": \"match_30ab4dd80c4e3756\",\n   \"match\": \"FC Nordsjælland vs FC Midtjylland\",\n   \"selection\": \"1\",\n   \"selection_label\": \"home\",\n   \"odds\": 2.87,\n   \"decision\": \"PAPER_BET\",\n   \"confidence_score\": 0.5,\n   \"stake_units\": 0.5,\n   \"value_case\": \"FC Midtjylland is severely hampered by an extensive injury list, particularly in their attacking department, with key players like Mikael Uhre out for the season and Franculino not fully fit, among others. Despite FC Nordsjælland also having some injuries, they boast a strong home record against FC Midtjylland, being unbeaten in their last nine home encounters and having secured two home wins against them this season. The odds of 2.87 for a home win appear to undervalue FC Nordsjælland's historical home dominance in this fixture and FC Midtjylland's current weakened state.\",\n   \"evidence_summary\": \"FCM has a significant injury crisis, especially i", "grounded_text_preview": "```json\n{\n \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n \"picks\": [\n  {\n   \"match_id\": \"match_30ab4dd80c4e3756\",\n   \"match\": \"FC Nordsjælland vs FC Midtjylland\",\n   \"selection\": \"1\",\n   \"selection_label\": \"home\",\n   \"odds\": 2.87,\n   \"decision\": \"PAPER_BET\",\n   \"confidence_score\": 0.5,\n   \"stake_units\": 0.5,\n   \"value_case\": \"FC Midtjylland is severely hampered by an extensive injury list, particularly in their attacking department, with key players like Mikael Uhre out for the season and Franculino not fully fit, among others. Despite FC Nordsjælland also having some injuries, they boast a strong home record against FC Midtjylland, being unbeaten in their last nine home encounters and having secured two home wins against them this season. The odds of 2.87 for a home win appear to undervalue FC Nordsjælland's historical home dominance in this fixture and FC Midtjylland's current weakened state.\",\n   \"evidence_summary\": \"FCM has a significant injury crisis, especially in attack, while FCN has a strong home H2H record against FCM.\",\n   \"evidence_items\": [\n    {\n     \"type\": \"injury\",\n     \"signal\": \"FC Midtjylland has an extensive injury list including Denil Castillo", "structured_text_preview": "{\n  \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n  \"picks\": [],\n  \"passes\": [\n    {\n      \"match_id\": \"match_30ab4dd80c4e3756\",\n      \"match\": \"FC Nordsjælland vs FC Midtjylland\",\n      \"reason\": \"json_not_stable\",\n      \"short_note\": \"Analyst output was malformed, all matches passed.\"\n    },\n    {\n      \"match_id\": \"match_fa7f1b2dd0fbe2c6\",\n      \"match\": \"Vejle vs FC Freder", "structure_parse_error": "Expecting ',' delimiter: line 10 column 6 (char 310)"}`
