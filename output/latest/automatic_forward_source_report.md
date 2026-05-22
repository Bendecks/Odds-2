# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.

Upcoming fixture rows: 778
Fixture team rows unmatched: 1489
Ready for model-fixture join: False
Automatic forward price rows: 195
odds-api.io price rows: 57
Football-Data price rows: 138
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- 9 de Octubre FC | suggestion=nan | type=unmatched
- Manta FC | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Atalanta BC | suggestion=Atalanta | type=suggested_alias_needed
- Aarhus Fremad | suggestion=nan | type=unmatched
- Aalborg BK | suggestion=nan | type=unmatched
- AB Gladsaxe | suggestion=nan | type=unmatched
- HIK Hellerup | suggestion=nan | type=unmatched
- AC Omonia Nicosia | suggestion=nan | type=unmatched
- Apollon Limassol | suggestion=nan | type=unmatched
- ADO Den Haag | suggestion=nan | type=unmatched
- PEC Zwolle | suggestion=nan | type=unmatched
- Afturelding | suggestion=nan | type=unmatched
- Throttur Reykjavik | suggestion=nan | type=unmatched
- Ajel de Rufisque | suggestion=nan | type=unmatched
- ASC Linguere | suggestion=nan | type=unmatched
- Al Jazira (UAE) | suggestion=nan | type=unmatched
- Al Ain FC | suggestion=nan | type=unmatched
- Aris Limassol FC | suggestion=nan | type=unmatched
- AEK Larnaca | suggestion=nan | type=unmatched
- Arsenal de Sarandi | suggestion=nan | type=unmatched
- CA Villa San Carlos | suggestion=nan | type=unmatched
- AS Armee | suggestion=nan | type=unmatched
- FC Brakna | suggestion=nan | type=unmatched
- AS Real Bamako | suggestion=nan | type=unmatched
- FC Diarra | suggestion=nan | type=unmatched
- ASAC Concorde | suggestion=nan | type=unmatched
- Garde | suggestion=nan | type=unmatched
- Athlone Town AFC | suggestion=nan | type=unmatched
- Cork City FC | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.