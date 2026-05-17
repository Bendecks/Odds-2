# Automatic Forward Source Report

Purpose: distinguish true automatic forward inputs from historical market proxy and paused manual fallback.
Football-Data and odds-api.io prices are treated as paper-test proxy prices until validated.

Upcoming fixture rows: 465
Fixture team rows unmatched: 843
Ready for model-fixture join: False
Automatic forward price rows: 271
odds-api.io price rows: 60
Football-Data price rows: 211
Automatic forward status: automatic_forward_not_ready
Blocker: fixture_model_team_matching_incomplete
Next development step: add_team_aliases_for_upcoming_fixtures

## Team matching

- 07 Vestur Sorvagur | suggestion=nan | type=unmatched
- NSI Runavik | suggestion=nan | type=unmatched
- 1. FC Magdeburg | suggestion=nan | type=unmatched
- 1 FC Kaiserslautern | suggestion=nan | type=unmatched
- 9 de Octubre FC | suggestion=nan | type=unmatched
- CD El Nacional | suggestion=nan | type=unmatched
- ACF Fiorentina | suggestion=Fiorentina | type=suggested_alias_needed
- Lazio Rome | suggestion=nan | type=unmatched
- FC Abdysh-Ata | suggestion=nan | type=unmatched
- FC Alay | suggestion=nan | type=unmatched
- AC Prato 1908 | suggestion=nan | type=unmatched
- ASD Seravezza Pozzi Calcio | suggestion=nan | type=unmatched
- AC Vigasio | suggestion=nan | type=unmatched
- Obermais | suggestion=nan | type=unmatched
- AD Cantolao | suggestion=nan | type=unmatched
- Carlos Mannucci | suggestion=nan | type=unmatched
- AEK | suggestion=nan | type=unmatched
- Olympiakos | suggestion=nan | type=unmatched
- AEK Athens | suggestion=nan | type=unmatched
- Olympiacos Piraeus | suggestion=nan | type=unmatched
- Af Elbasani | suggestion=nan | type=unmatched
- KF Egnatia Rrogozhine | suggestion=nan | type=unmatched
- AGF Aarhus | suggestion=nan | type=unmatched
- Viborg FF | suggestion=nan | type=unmatched
- Aguilas FC | suggestion=nan | type=unmatched
- Utebo FC | suggestion=nan | type=unmatched
- AL Bataeh | suggestion=nan | type=unmatched
- Shabab AL Ahli Dubai Club | suggestion=nan | type=unmatched
- AL Wahda FC | suggestion=nan | type=unmatched
- AL Dhafra U23 | suggestion=nan | type=unmatched

## Interpretation

Fixtures are available, but team matching must be fixed before forward model snapshots can be generated.