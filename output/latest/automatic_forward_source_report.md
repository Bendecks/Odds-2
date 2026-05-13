# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.

Upcoming fixture rows: 18
Fixture team rows unmatched: 16
Ready for model-fixture join: False
Automatic forward price rows: 51
odds-api.io price rows: 0
Football-Data price rows: 51
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- Hearts | suggestion=nan | type=unmatched
- Falkirk | suggestion=nan | type=unmatched
- Levadeiakos | suggestion=nan | type=unmatched
- OFI Crete | suggestion=nan | type=unmatched
- Manchester City | suggestion=nan | type=unmatched
- Motherwell | suggestion=nan | type=unmatched
- Celtic | suggestion=nan | type=unmatched
- Olympiakos | suggestion=nan | type=unmatched
- Panathinaikos | suggestion=nan | type=unmatched
- PAOK | suggestion=nan | type=unmatched
- AEK | suggestion=nan | type=unmatched
- Rangers | suggestion=Angers | type=suggested_alias_needed
- Hibernian | suggestion=nan | type=unmatched
- Volos NFC | suggestion=nan | type=unmatched
- Aris | suggestion=nan | type=unmatched
- Oviedo | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.