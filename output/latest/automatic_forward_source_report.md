# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data fixture odds are treated as delayed/free proxy prices: paper-test only, never real-money ready.

Upcoming fixture rows: 11
Fixture team rows checked: 22
Fixture team rows unmatched: 16
Ready for model-fixture join: False
Configured forward sources: 1
Enabled forward sources: 1
Automatic forward price rows: 33
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- Benfica | suggestion=nan | type=unmatched
- Sp Braga | suggestion=nan | type=unmatched
- Estrela | suggestion=nan | type=unmatched
- Famalicao | suggestion=nan | type=unmatched
- Gil Vicente | suggestion=nan | type=unmatched
- Arouca | suggestion=nan | type=unmatched
- Guimaraes | suggestion=nan | type=unmatched
- Casa Pia | suggestion=nan | type=unmatched
- Huesca | suggestion=nan | type=unmatched
- Sociedad B | suggestion=Sociedad | type=suggested_alias_needed
- Rio Ave | suggestion=nan | type=unmatched
- Sp Lisbon | suggestion=nan | type=unmatched
- Santa Clara | suggestion=nan | type=unmatched
- Nacional | suggestion=nan | type=unmatched
- Tondela | suggestion=nan | type=unmatched
- Moreirense | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.