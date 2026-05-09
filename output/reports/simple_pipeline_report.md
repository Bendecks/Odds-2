# Odds 2 — Simple Gemini Pipeline

Generated: 2026-05-09T18:09:01Z
- Analysis version: simple_decision_v5_deduped_source_audit
- Files processed: 5
- Raw matches: 17
- Valid matches: 17
- Unique valid matches: 17
- Duplicate matches removed: 0
- Decision matches: 12
- Rejected matches: 0
- Gemini decision records: 0
- PAPER_BET logged: 0
- Blocked decisions: 0
- Passes returned: 12
- Decision error: `None`
- Grounding sources: 0

No PAPER_BET passed safety gates.

## Pass reasons
- FC Nordsjælland vs FC Midtjylland: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Vejle vs FC Fredericia: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Silkeborg IF vs FC København: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Brøndby vs AGF: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Randers FC vs OB: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Burnley vs Aston Villa: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Crystal Palace vs Everton: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Nottm Forest vs Newcastle: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- West Ham vs Arsenal: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Tottenham vs Leeds: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Millwall vs Hull: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.
- Real Sociedad vs Real Betis: json_not_stable — Analyst output was malformed or incomplete, resulting in all picks being passed.

## Duplicate matches removed

## Gemini grounding sources
No grounding sources returned or parsed.

## Grounding debug
`{"top_level_keys": ["candidates", "usageMetadata", "modelVersion", "responseId"], "candidate_keys": ["content", "finishReason", "index", "groundingMetadata"], "grounding_metadata_keys": ["searchEntryPoint", "webSearchQueries"], "text_preview": "```json\n{\n \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n \"picks\": [\n  {\n   \"match_id\": \"match_86535972ce1080e6\",\n   \"match\": \"Vejle vs FC Fredericia\",\n   \"selection\": \"2\",\n   \"selection_label\": \"away\",\n   \"odds\": 2.15,\n   \"decision\": \"PAPER_BET\",\n   \"confidence_score\": 0.75,\n   \"stake_units\": 0.75,\n   \"value_case\": \"Vejle is in very poor form, winless in their last five league matches and conceding many goals. FC Fredericia, despite a tendency for draws, is in a much stronger league position and has avoided defeat in their last three encounters with Vejle. The odds of 2.15 for an away win seem to undervalue Fredericia's superior form and head-to-head advantage against a struggling Vejle side.\",\n   \"evidence_summary\": \"Vejle is winless in their last five league matches (1D, 4L) and has conceded 12 goals in that period. FC Fredericia is in better form (4D, 1L in last five) and is unbeaten in their last three head-to-head matches against Vejle. Fredericia also holds a si", "grounded_text_preview": "```json\n{\n \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n \"picks\": [\n  {\n   \"match_id\": \"match_86535972ce1080e6\",\n   \"match\": \"Vejle vs FC Fredericia\",\n   \"selection\": \"2\",\n   \"selection_label\": \"away\",\n   \"odds\": 2.15,\n   \"decision\": \"PAPER_BET\",\n   \"confidence_score\": 0.75,\n   \"stake_units\": 0.75,\n   \"value_case\": \"Vejle is in very poor form, winless in their last five league matches and conceding many goals. FC Fredericia, despite a tendency for draws, is in a much stronger league position and has avoided defeat in their last three encounters with Vejle. The odds of 2.15 for an away win seem to undervalue Fredericia's superior form and head-to-head advantage against a struggling Vejle side.\",\n   \"evidence_summary\": \"Vejle is winless in their last five league matches (1D, 4L) and has conceded 12 goals in that period. FC Fredericia is in better form (4D, 1L in last five) and is unbeaten in their last three head-to-head matches against Vejle. Fredericia also holds a significantly higher league position.\",\n   \"evidence_items", "structured_text_preview": "{\n  \"analysis_version\": \"simple_decision_v6_visible_markets_only\",\n  \"picks\": [],\n  \"passes\": [\n    {\n      \"match_id\": \"match_01c571330e7f8dc7\",\n      \"match\": \"FC Nordsjælland vs FC Midtjylland\",\n      \"reason\": \"json_not_stable\",\n      \"short_note\": \"Analyst output was malformed or incomplete, resulting in all picks being passed.\"\n    },\n    {\n      \"match_id\": \"match_86535972ce1080e6\",\n      \"match\": \"Vejle vs FC Fredericia\",\n      \"reason\": \"json_not_stable\",\n      \"short_note\": \"Analyst output was malformed or incomplete, resulting in all picks being passed.\"\n    },\n    {\n      \"match_id\": \"match_0aac60eb0f1f71cd\",\n      \"match\": \"Silkeborg IF vs FC København\",\n      \"reason\": \"json_not_stable\",\n      \"short_note\": \"Analyst output was malformed or incomplete, resulting in all picks being passed.\"\n    },\n    {\n      \"match_id\": \"match_0fdbf7d47e45b8de\",\n      \"match\": \"Brøndby vs AGF\",\n      \"reason\": \"json_not_stable\",\n      \"short_note\": \"Analyst output was malformed or incomplete, resulting in all picks being passed.\"\n    },\n    {\n      \"match_id\": \"match_05e26de40ea79b92\",\n      \"match\": \"Randers FC vs OB\",\n      \"reason\": \"json_not_stable\",\n      \"short_note\": \"Analyst ou"}`
