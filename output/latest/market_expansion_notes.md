# Market and Sport Expansion Notes

Current active betting model: football 1X2 / full-time result, Bet365 only.

Expansion rule: use existing raw Odds-API.io responses first. Do not spend extra requests just to explore markets unless we explicitly decide to run an inventory test.

Priority order:
1. Football Over/Under 2.5 – best fit with current goals model.
2. Football Both Teams To Score – possible after checking expected goals quality.
3. Football handicap/spread – later, higher modelling risk.
4. Other sports – inventory only until a sport-specific model exists.

Do not mix non-football markets into the current paper-pick log until they have their own model, filters, and settlement report.