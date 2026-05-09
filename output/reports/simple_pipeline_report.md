# Odds 2 — Simple Gemini Pipeline

Generated: 2026-05-09T16:32:37Z
- Analysis version: simple_decision_v5_deduped_source_audit
- Files processed: 5
- Raw matches: 54
- Valid matches: 54
- Unique valid matches: 44
- Duplicate matches removed: 10
- Decision matches: 12
- Rejected matches: 0
- Gemini decision records: 1
- PAPER_BET logged: 0
- Blocked decisions: 1
- Passes returned: 12
- Decision error: `None`
- Grounding sources: 0

No PAPER_BET passed safety gates.

## Blocked Gemini suggestions

### Randers FC vs OB
- Suggested selection: PASS
- Blocked by safety: `prohibited_source_used`
- Verified source tiers: `['tier1', 'tier1', 'tier1', 'prohibited', 'prohibited']`
- Redirect source count: 5
- Value case: The Bet365 odds of 2.2 for a Randers FC home win appear to be overvalued. Randers FC is in poor recent form (1 win, 1 draw, 3 losses in their last 5 Superliga games) and has struggled against OB in recent head-to-head matches (OB won 3, drew 1, lost 1 of their last 5 encounters). Furthermore, Randers FC will be without Oliver Jones due to a knee injury and Cyril Edudzi due to a red card suspension, while OB only has Nicolas Bürgy suspended. This combination of poor form, recent H2H dominance by OB, and Randers' more significant absences makes the odds for an OB win or draw (Double Chance X2) a value proposition.
- Evidence sources:
  - injury | Tipsbladet.dk | verified=tier1 | declared=tier1 | https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERQlvYFcS2Kdy4WQeulQeHndrug44NHIi1Ydcv7BZsjyUcLgKaB-Lds4y2woJlLLyA7yQO8b35nZU5YUeowWA9WcOvBufHk-4R0YD51shnVayrHDfjwiZFMSWGR2CrW9_YJ32eb-ckFQ== | Randers FC will be without Oliver Jones due to a knee injury (doubtful).
  - suspension | Tipsbladet.dk | verified=tier1 | declared=tier1 | https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQERQlvYFcS2Kdy4WQeulQeHndrug44NHIi1Ydcv7BZsjyUcLgKaB-Lds4y2woJlLLyA7yQO8b35nZU5YUeowWA9WcOvBufHk-4R0YD51shnVayrHDfjwiZFMSWGR2CrW9_YJ32eb-ckFQ== | Randers FC will be without Cyril Edudzi due to a red card suspension.
  - suspension | Tipsbladet.dk | verified=tier1 | declared=tier1 | https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuJ2J3lsrWM_AyR5iSqnEYjUCS3VnMU0qWjm0rfKgoWc8SU9dX5zsPuEiS3oQppTMn1MfWNouyc2YCGWYgdaQOLSZdix8fHHv8m7lk_rr0TZQIuQnk_wQQXPGNOv34aWw== | OB will be without Nicolas Bürgy due to a red card suspension.
  - form | FootyStats | verified=prohibited | declared=tier2 | https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEM6TI6B_v0AHot7iY0Z3aZ9dTdFkWJfrDRx4ZUSUv8TFHK6UXX5paD69Qw5DyxwFt0Ej_8B3ieR9KvBvyPsKjmZvjslkVAmIaSyzcjGFx8S0erPARewealawiqJIe-2UpbLTCfy2Y= | Randers FC has poor recent form in the Superliga, with only 1 win, 1 draw, and 3 losses in their last 5 games.
  - form | FootyStats | verified=prohibited | declared=tier3 | https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv7McXnIIkPXztVhw3ewjclqb3q7Cl2b_Tl-Hj6dPdUTIj_X1mnVu9tIL9EH14AwH8qFC8kQasW7A0GNeStfklWvW4IzBnkUx-KW5h9WfolZQhr5MSJKXG7M_QdeWf7vFTsfrCfA8lttH3JSbN6bn-GHG0Tlu7wgogOw== | OB has a strong recent head-to-head record against Randers FC, winning 3, drawing 1, and losing 1 of their last 5 encounters.

## Pass reasons
- FC Nordsjælland vs FC Midtjylland: insufficient edge — FC Midtjylland is in better form and higher in the table, but FC Nordsjælland has a strong recent H2H record against them. Conflicting signals and lack of clear value.
- Vejle vs FC Fredericia: insufficient edge — Vejle is in very poor form, and Fredericia has a recent H2H edge. However, Fredericia's own form is also poor (many draws), and injury reports are conflicting from Tier 3 sources.
- Silkeborg IF vs FC København: insufficient edge — FC København is the stronger team but has significant injuries. Silkeborg is in good form but has a poor overall H2H. Odds for FCK are not exceptionally low, and the situation is too balanced for a clear value pick.
- Brøndby vs AGF: insufficient edge — AGF is stronger and highly motivated for the title, but has several key injuries. Brøndby has poor form but home advantage. Conflicting factors make a clear value pick difficult.
- Viborg vs Sønderjyske: stale information — Match scheduled for May 8, 2026, which has already passed.
- Hull vs Millwall: stale information — Match scheduled for May 8, 2026, which has already passed.
- Middlesbrough vs Southampton: stale information — Match scheduled for May 9, 2026, 13:30 local time. Current UTC time is 4:30 PM on May 9, indicating the match has already been played.
- Liverpool vs Chelsea: stale information — Match scheduled for May 9, 2026, 13:30 local time. Current UTC time is 4:30 PM on May 9, indicating the match has already been played.
- Sunderland vs Man Utd: stale information — Match scheduled for May 9, 2026, 16:00 local time. Current UTC time is 4:30 PM on May 9, indicating the match has already been played.
- Fulham vs Bournemouth: stale information — Match scheduled for May 9, 2026, 16:00 local time. Current UTC time is 4:30 PM on May 9, indicating the match has already been played.
- Brighton vs Wolverhampton: stale information — Match scheduled for May 9, 2026, 16:00 local time. Current UTC time is 4:30 PM on May 9, indicating the match has already been played.
- Randers FC vs OB: blocked_by_safety:prohibited_source_used — Randers FC is in poor form (1W 1D 3L in last 5 Superliga games) and has a worse injury/suspension situation (1 injured, 1 suspended) compared to OB (1 suspended). OB has a strong recent H2H record against Randers (3W 1D 1L in last 5 encounters).

## Duplicate matches removed
- FC Nordsjælland vs FC Midtjylland: kept inbox/possible_bets/20260509-075325_possible_bets_1486.pdf, removed inbox/possible_bets/20260509-075323_possible_bets_1632.pdf
- Vejle vs FC Fredericia: kept inbox/possible_bets/20260509-075325_possible_bets_1486.pdf, removed inbox/possible_bets/20260509-075323_possible_bets_1632.pdf
- Silkeborg IF vs FC København: kept inbox/possible_bets/20260509-075325_possible_bets_1486.pdf, removed inbox/possible_bets/20260509-075323_possible_bets_1632.pdf
- Brøndby vs AGF: kept inbox/possible_bets/20260509-075325_possible_bets_1486.pdf, removed inbox/possible_bets/20260509-075323_possible_bets_1632.pdf
- Randers FC vs OB: kept inbox/possible_bets/20260509-075325_possible_bets_1486.pdf, removed inbox/possible_bets/20260509-075323_possible_bets_1632.pdf
- Liverpool vs Chelsea: kept inbox/possible_bets/20260509-075323_possible_bets_1632.pdf, removed inbox/possible_bets/20260509-075321_possible_bets_4179.pdf
- Brighton vs Wolverhampton: kept inbox/possible_bets/20260509-075323_possible_bets_1632.pdf, removed inbox/possible_bets/20260509-075321_possible_bets_4179.pdf
- Fulham vs Bournemouth: kept inbox/possible_bets/20260509-075323_possible_bets_1632.pdf, removed inbox/possible_bets/20260509-075321_possible_bets_4179.pdf
- Sunderland vs Man Utd: kept inbox/possible_bets/20260509-075323_possible_bets_1632.pdf, removed inbox/possible_bets/20260509-075321_possible_bets_4179.pdf
- Man City vs Brentford: kept inbox/possible_bets/20260509-075323_possible_bets_1632.pdf, removed inbox/possible_bets/20260509-075321_possible_bets_4179.pdf

## Gemini grounding sources
No grounding sources returned or parsed.

## Grounding debug
`{"top_level_keys": ["candidates", "usageMetadata", "modelVersion", "responseId"], "candidate_keys": ["content", "finishReason", "index", "groundingMetadata"], "grounding_metadata_keys": ["searchEntryPoint", "webSearchQueries"], "text_preview": "```json\n{\n \"analysis_version\": \"simple_decision_v5_deduped_source_audit\",\n \"picks\": [\n  {\n   \"match_id\": \"match_896ed38f36252862\",\n   \"match\": \"Randers FC vs OB\",\n   \"selection\": \"X2\",\n   \"selection_label\": \"draw_or_away\",\n   \"odds\": 1.64,\n   \"decision\": \"PAPER_BET\",\n   \"confidence_score\": 0.5,\n   \"stake_units\": 0.5,\n   \"value_case\": \"The Bet365 odds of 2.2 for a Randers FC home win appear to be overvalued. Randers FC is in poor recent form (1 win, 1 draw, 3 losses in their last 5 Superliga games) and has struggled against OB in recent head-to-head matches (OB won 3, drew 1, lost 1 of their last 5 encounters). Furthermore, Randers FC will be without Oliver Jones due to a knee injury and Cyril Edudzi due to a red card suspension, while OB only has Nicolas Bürgy suspended. This combination of poor form, recent H2H dominance by OB, and Randers' more significant absences makes the odds for an OB win or draw (Double Chance X2) a value proposition.\",\n   \"evidence_summary\": \"Randers FC is in "}`
