# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.

Upcoming fixture rows: 32
Fixture team rows unmatched: 57
Ready for model-fixture join: False
Automatic forward price rows: 33
odds-api.io price rows: 0
Football-Data price rows: 33
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- Benfica | suggestion=nan | type=unmatched
- Sp Braga | suggestion=nan | type=unmatched
- CDP Junior FC | suggestion=nan | type=unmatched
- Independiente Santa Fe | suggestion=nan | type=unmatched
- CR Flamengo RJ | suggestion=nan | type=unmatched
- Ferroviaria SP | suggestion=nan | type=unmatched
- Deportivo Saprissa | suggestion=nan | type=unmatched
- Sporting FC | suggestion=nan | type=unmatched
- Estrela | suggestion=nan | type=unmatched
- Famalicao | suggestion=nan | type=unmatched
- Gil Vicente | suggestion=nan | type=unmatched
- Arouca | suggestion=nan | type=unmatched
- Guimaraes | suggestion=nan | type=unmatched
- Casa Pia | suggestion=nan | type=unmatched
- Huesca | suggestion=nan | type=unmatched
- Sociedad B | suggestion=Sociedad | type=suggested_alias_needed
- Independiente Medellin | suggestion=nan | type=unmatched
- Fortaleza FC | suggestion=nan | type=unmatched
- Loud SC | suggestion=nan | type=unmatched
- Funkbol Clube | suggestion=nan | type=unmatched
- Millonarios FC | suggestion=nan | type=unmatched
- America de Cali Sa | suggestion=nan | type=unmatched
- Once Caldas Sa | suggestion=nan | type=unmatched
- Orsomarso SC | suggestion=nan | type=unmatched
- Piaui PI | suggestion=nan | type=unmatched
- Ferroviario AC CE | suggestion=nan | type=unmatched
- Rio Ave | suggestion=nan | type=unmatched
- Sp Lisbon | suggestion=nan | type=unmatched
- Santa Clara | suggestion=nan | type=unmatched
- Nacional | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.