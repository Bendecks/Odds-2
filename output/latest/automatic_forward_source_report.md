# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.

Upcoming fixture rows: 136
Fixture team rows unmatched: 241
Ready for model-fixture join: False
Automatic forward price rows: 99
odds-api.io price rows: 21
Football-Data price rows: 78
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- Aberdeen | suggestion=nan | type=unmatched
- St Mirren | suggestion=nan | type=unmatched
- Al Hussein Irbid | suggestion=nan | type=unmatched
- Al Wehdat | suggestion=nan | type=unmatched
- Al Nassr Club | suggestion=nan | type=unmatched
- Al Hilal SFC | suggestion=nan | type=unmatched
- Asteras Tripolis | suggestion=nan | type=unmatched
- Panserraikos | suggestion=nan | type=unmatched
- Atletico Nacional Medellin | suggestion=nan | type=unmatched
- Internacional de Bogota. | suggestion=nan | type=unmatched
- Banos Ciudad de Fuego | suggestion=nan | type=unmatched
- Delfin SC | suggestion=nan | type=unmatched
- Beitar Jerusalem FC | suggestion=nan | type=unmatched
- Hapoel Be`er Sheva FC | suggestion=nan | type=unmatched
- Boston Legacy FC | suggestion=nan | type=unmatched
- Orlando Pride | suggestion=nan | type=unmatched
- Botev Plovdiv | suggestion=nan | type=unmatched
- FC Arda Kardzhali | suggestion=nan | type=unmatched
- CA Belgrano de Cordoba | suggestion=nan | type=unmatched
- Union de Santa Fe | suggestion=nan | type=unmatched
- CA Osasuna | suggestion=Osasuna | type=suggested_alias_needed
- Atletico Madrid | suggestion=nan | type=unmatched
- CD Real Santander | suggestion=nan | type=unmatched
- Boca Juniors de Cali | suggestion=nan | type=unmatched
- Levante | suggestion=nan | type=unmatched
- Central Espanol Reserve | suggestion=nan | type=unmatched
- Defensor Sporting | suggestion=nan | type=unmatched
- Cerro Largo FC | suggestion=nan | type=unmatched
- Boston River | suggestion=nan | type=unmatched
- Clyde FC | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.