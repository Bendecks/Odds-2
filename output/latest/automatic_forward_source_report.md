# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.

Upcoming fixture rows: 1137
Fixture team rows unmatched: 2158
Ready for model-fixture join: False
Automatic forward price rows: 351
odds-api.io price rows: 35
Football-Data price rows: 316
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- 1. FC Bocholt | suggestion=nan | type=unmatched
- RW Oberhausen | suggestion=nan | type=unmatched
- 1. FC Cologne II | suggestion=nan | type=unmatched
- FC Schalke 04 II | suggestion=Schalke 04 | type=suggested_alias_needed
- 1. FC Heidenheim | suggestion=Heidenheim | type=suggested_alias_needed
- FSV Mainz | suggestion=nan | type=unmatched
- 1. FC Lokomotive Leipzig | suggestion=nan | type=unmatched
- FC Magdeburg II | suggestion=nan | type=unmatched
- 1 FC Nuremberg II | suggestion=nan | type=unmatched
- SpVgg Hankofen-Hailing | suggestion=nan | type=unmatched
- 1. FC Saarbrucken | suggestion=nan | type=unmatched
- Hansa Rostock | suggestion=nan | type=unmatched
- 1. FC Schweinfurt 05 | suggestion=nan | type=unmatched
- Erzgebirge Aue | suggestion=nan | type=unmatched
- 1. FC Slovacko Uherske Hradiste | suggestion=nan | type=unmatched
- FK Mlada Boleslav | suggestion=nan | type=unmatched
- A-Xiii Auhof Center | suggestion=nan | type=unmatched
- WAF Vorwarts Brigittenau | suggestion=nan | type=unmatched
- ABC FC RN | suggestion=nan | type=unmatched
- Sousa EC PB | suggestion=nan | type=unmatched
- AC Goianiense GO | suggestion=nan | type=unmatched
- Cerrado EC GO | suggestion=nan | type=unmatched
- AC Horsens | suggestion=nan | type=unmatched
- Hvidovre IF | suggestion=nan | type=unmatched
- AC Oulu | suggestion=nan | type=unmatched
- Turun Palloseura | suggestion=nan | type=unmatched
- AC Virtus | suggestion=nan | type=unmatched
- SP La Fiorita | suggestion=nan | type=unmatched
- Academica de Coimbra | suggestion=nan | type=unmatched
- CD Trofense | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.