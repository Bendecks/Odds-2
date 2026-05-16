# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.

Upcoming fixture rows: 991
Fixture team rows unmatched: 1862
Ready for model-fixture join: False
Automatic forward price rows: 357
odds-api.io price rows: 41
Football-Data price rows: 316
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- 1. FC Heidenheim | suggestion=Heidenheim | type=suggested_alias_needed
- FSV Mainz | suggestion=nan | type=unmatched
- 1. FC Slovacko Uherske Hradiste | suggestion=nan | type=unmatched
- FK Mlada Boleslav | suggestion=nan | type=unmatched
- A-Xiii Auhof Center | suggestion=nan | type=unmatched
- WAF Vorwarts Brigittenau | suggestion=nan | type=unmatched
- ABC FC RN | suggestion=nan | type=unmatched
- Sousa EC PB | suggestion=nan | type=unmatched
- AC Goianiense GO | suggestion=nan | type=unmatched
- Cerrado EC GO | suggestion=nan | type=unmatched
- AC Oulu | suggestion=nan | type=unmatched
- Turun Palloseura | suggestion=nan | type=unmatched
- AC Virtus | suggestion=nan | type=unmatched
- SP La Fiorita | suggestion=nan | type=unmatched
- Academica de Coimbra | suggestion=nan | type=unmatched
- CD Trofense | suggestion=nan | type=unmatched
- ACV Assen | suggestion=nan | type=unmatched
- Koninklijke HFC | suggestion=nan | type=unmatched
- AD Alcorcon | suggestion=nan | type=unmatched
- Marbella FC | suggestion=nan | type=unmatched
- AD Cabofriense RJ | suggestion=nan | type=unmatched
- Serrano FC RJ | suggestion=nan | type=unmatched
- AD Ceuta | suggestion=nan | type=unmatched
- Malaga CF | suggestion=nan | type=unmatched
- AD Comerciantes FC | suggestion=nan | type=unmatched
- Deportivo Binacional FC | suggestion=nan | type=unmatched
- ADO 20 Heemskerk | suggestion=nan | type=unmatched
- VV Scherpenzeel | suggestion=nan | type=unmatched
- AE Larissa FC | suggestion=nan | type=unmatched
- Atromitos Athinon | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.