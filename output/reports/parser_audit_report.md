# Odds 2 — Parser Audit Report

Generated: 2026-05-09T09:05:16Z
- Audit version: parser_audit_v1_1x2_mapping
- Events checked: 59
- Events flagged: 25
- Flagged markets: 75
- Flag counts: `{"underround_below_1_00": 13, "overround_above_1_16": 10, "draw_odds_implausibly_low": 7, "draw_much_shorter_than_both_sides": 8, "draw_shortest_with_high_overround": 6, "overround_high_1_12_plus": 1}`


## Randers FC vs OB
- Severity: fail
- Event time UTC: 2026-05-09T17:00:00Z
- Source file: inbox/possible_bets/20260509-075325_possible_bets_1486.pdf
- Odds: `{"1": 2.87, "2": 3.9, "X": 3.2}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.9173}]`

## Arsenal vs Burnley
- Severity: fail
- Event time UTC: 2026-05-09T19:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 1.95, "2": 2.5, "X": 1.25}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.7128}, {"severity": "fail", "code": "draw_odds_implausibly_low", "detail": 1.25}, {"severity": "fail", "code": "draw_much_shorter_than_both_sides", "detail": {"home": 1.95, "draw": 1.25, "away": 2.5}}, {"severity": "warn", "code": "draw_shortest_with_high_overround", "detail": {"overround": 1.7128, "home": 1.95, "draw": 1.25, "away": 2.5}}]`

## Liverpool vs Chelsea
- Severity: fail
- Event time UTC: 2026-05-11T11:30:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 1.95, "2": 2.5, "X": 1.25}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.7128}, {"severity": "fail", "code": "draw_odds_implausibly_low", "detail": 1.25}, {"severity": "fail", "code": "draw_much_shorter_than_both_sides", "detail": {"home": 1.95, "draw": 1.25, "away": 2.5}}, {"severity": "warn", "code": "draw_shortest_with_high_overround", "detail": {"overround": 1.7128, "home": 1.95, "draw": 1.25, "away": 2.5}}]`

## Manchester United vs Nottm Forest
- Severity: fail
- Event time UTC: 2026-05-11T11:30:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 3.75, "2": 3.6, "X": 10.0}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.6444}]`

## FC Nordsjælland vs FC Midtjylland
- Severity: fail
- Event time UTC: 2026-05-11T12:00:00Z
- Source file: inbox/possible_bets/20260509-075325_possible_bets_1486.pdf
- Odds: `{"1": 2.87, "2": 3.9, "X": 3.2}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.9173}]`

## Vejle vs FC Fredericia
- Severity: fail
- Event time UTC: 2026-05-11T12:00:00Z
- Source file: inbox/possible_bets/20260509-075325_possible_bets_1486.pdf
- Odds: `{"1": 2.87, "2": 3.8, "X": 2.2}`
- Flags: `[{"severity": "fail", "code": "draw_much_shorter_than_both_sides", "detail": {"home": 2.87, "draw": 2.2, "away": 3.8}}]`

## Crystal Palace vs Everton
- Severity: fail
- Event time UTC: 2026-05-11T13:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 1.11, "2": 6.5, "X": 3.75}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.3214}]`

## Nottm Forest vs Newcastle
- Severity: fail
- Event time UTC: 2026-05-11T13:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 3.3, "2": 5.25, "X": 3.7}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.7638}]`

## Brighton vs Wolverhampton
- Severity: fail
- Event time UTC: 2026-05-11T14:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 3.6, "2": 4.75, "X": 1.33}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.2402}, {"severity": "fail", "code": "draw_odds_implausibly_low", "detail": 1.33}, {"severity": "fail", "code": "draw_much_shorter_than_both_sides", "detail": {"home": 3.6, "draw": 1.33, "away": 4.75}}, {"severity": "warn", "code": "draw_shortest_with_high_overround", "detail": {"overround": 1.2402, "home": 3.6, "draw": 1.33, "away": 4.75}}]`

## Everton vs Sunderland
- Severity: fail
- Event time UTC: 2026-05-11T14:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 5.5, "2": 2.6, "X": 1.61}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.1876}, {"severity": "fail", "code": "draw_odds_implausibly_low", "detail": 1.61}, {"severity": "fail", "code": "draw_much_shorter_than_both_sides", "detail": {"home": 5.5, "draw": 1.61, "away": 2.6}}, {"severity": "warn", "code": "draw_shortest_with_high_overround", "detail": {"overround": 1.1876, "home": 5.5, "draw": 1.61, "away": 2.6}}]`

## Fulham vs Bournemouth
- Severity: fail
- Event time UTC: 2026-05-11T14:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 2.8, "2": 5.25, "X": 2.7}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.918}]`

## Leeds vs Brighton
- Severity: fail
- Event time UTC: 2026-05-11T14:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 2.45, "2": 3.7, "X": 1.6}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.3034}, {"severity": "fail", "code": "draw_odds_implausibly_low", "detail": 1.6}, {"severity": "fail", "code": "draw_much_shorter_than_both_sides", "detail": {"home": 2.45, "draw": 1.6, "away": 3.7}}, {"severity": "warn", "code": "draw_shortest_with_high_overround", "detail": {"overround": 1.3034, "home": 2.45, "draw": 1.6, "away": 3.7}}]`

## Silkeborg IF vs FC København
- Severity: fail
- Event time UTC: 2026-05-11T14:00:00Z
- Source file: inbox/possible_bets/20260509-075325_possible_bets_1486.pdf
- Odds: `{"1": 3.5, "2": 3.6, "X": 3.9}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.8199}]`

## Sunderland vs Manchester United
- Severity: fail
- Event time UTC: 2026-05-11T14:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 1.85, "2": 3.6, "X": 1.27}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.6057}, {"severity": "fail", "code": "draw_odds_implausibly_low", "detail": 1.27}, {"severity": "fail", "code": "draw_much_shorter_than_both_sides", "detail": {"home": 1.85, "draw": 1.27, "away": 3.6}}, {"severity": "warn", "code": "draw_shortest_with_high_overround", "detail": {"overround": 1.6057, "home": 1.85, "draw": 1.27, "away": 3.6}}]`

## Wolverhampton vs Fulham
- Severity: fail
- Event time UTC: 2026-05-11T14:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 9.5, "2": 5.25, "X": 1.83}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.8422}, {"severity": "fail", "code": "draw_much_shorter_than_both_sides", "detail": {"home": 9.5, "draw": 1.83, "away": 5.25}}]`

## West Ham vs Arsenal
- Severity: fail
- Event time UTC: 2026-05-11T15:30:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 4.33, "2": 3.6, "X": 3.3}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.8118}]`

## Brøndby vs AGF
- Severity: fail
- Event time UTC: 2026-05-11T16:00:00Z
- Source file: inbox/possible_bets/20260509-075325_possible_bets_1486.pdf
- Odds: `{"1": 3.5, "2": 2.15, "X": 2.2}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.2054}]`

## Manchester City vs Brentford
- Severity: fail
- Event time UTC: 2026-05-11T16:30:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 1.6, "2": 1.72, "X": 1.66}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.8088}, {"severity": "fail", "code": "draw_odds_implausibly_low", "detail": 1.66}]`

## Newcastle vs West Ham
- Severity: fail
- Event time UTC: 2026-05-11T16:30:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 4.75, "2": 2.25, "X": 4.5}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.8772}]`

## Randers FC vs OB
- Severity: fail
- Event time UTC: 2026-05-11T17:00:00Z
- Source file: inbox/possible_bets/20260509-075325_possible_bets_1486.pdf
- Odds: `{"1": 1.8, "2": 3.1, "X": 2.3}`
- Flags: `[{"severity": "fail", "code": "overround_above_1_16", "detail": 1.3129}]`

## Arsenal vs Burnley
- Severity: fail
- Event time UTC: 2026-05-11T19:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 1.95, "2": 15.0, "X": 3.4}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.8736}]`

## Aston Villa vs Liverpool
- Severity: fail
- Event time UTC: 2026-05-11T19:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 3.75, "2": 3.6, "X": 3.6}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.8222}]`

## Manchester City vs Crystal Palace
- Severity: fail
- Event time UTC: 2026-05-11T19:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 4.0, "2": 3.9, "X": 4.0}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.7564}]`

## Tottenham vs Leeds
- Severity: fail
- Event time UTC: 2026-05-11T19:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 4.1, "2": 6.0, "X": 4.1}`
- Flags: `[{"severity": "fail", "code": "underround_below_1_00", "detail": 0.6545}]`

## Burnley vs Aston Villa
- Severity: warn
- Event time UTC: 2026-05-11T13:00:00Z
- Source file: inbox/possible_bets/20260509-073218_possible_bets_4032.pdf
- Odds: `{"1": 2.9, "2": 2.0, "X": 3.6}`
- Flags: `[{"severity": "warn", "code": "overround_high_1_12_plus", "detail": 1.1226}]`
