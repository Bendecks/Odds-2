# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.

Upcoming fixture rows: 447
Fixture team rows unmatched: 890
Ready for model-fixture join: False
Automatic forward price rows: 49
odds-api.io price rows: 49
Football-Data price rows: 0
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- 1. FC Lokomotive Leipzig | suggestion=nan | type=unmatched
- FC Wurzburger Kickers | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Parma Calcio 1913 U20 | suggestion=nan | type=unmatched
- AL Karkh | suggestion=nan | type=unmatched
- Al Shorta SC | suggestion=nan | type=unmatched
- AL Minaa | suggestion=nan | type=unmatched
- AL Talaba | suggestion=nan | type=unmatched
- AL Naft Maysan | suggestion=nan | type=unmatched
- Al Quwa Al Jawiya | suggestion=nan | type=unmatched
- Al-Fahaheel | suggestion=nan | type=unmatched
- Al-Salmiya SC | suggestion=nan | type=unmatched
- Assyriska FF | suggestion=nan | type=unmatched
- Vasalunds IF | suggestion=nan | type=unmatched
- Atletico Mineiro MG | suggestion=nan | type=unmatched
- EC Vitoria BA | suggestion=nan | type=unmatched
- Auckland FC Reserves | suggestion=nan | type=unmatched
- Auckland United FC | suggestion=nan | type=unmatched
- Birkenhead United AFC | suggestion=nan | type=unmatched
- East Coast Bays | suggestion=nan | type=unmatched
- CA Aldosivi Reserve | suggestion=nan | type=unmatched
- CA Talleres de Cordoba Reserve | suggestion=nan | type=unmatched
- CA Lanus | suggestion=nan | type=unmatched
- CA Platense | suggestion=nan | type=unmatched
- CA Piauiense PI | suggestion=nan | type=unmatched
- Santos FC SP | suggestion=nan | type=unmatched
- CA River Plate (Arg) | suggestion=nan | type=unmatched
- San Lorenzo de Almagro Res. | suggestion=nan | type=unmatched
- CA Sarmiento de Junin | suggestion=nan | type=unmatched
- Rosario Central Reserve | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.