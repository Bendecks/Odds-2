from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
config_dir = Path('data/manual')
config_dir.mkdir(parents=True, exist_ok=True)

fixtures_path = output_dir / 'upcoming_fixtures.csv'
template_path = config_dir / 'manual_odds_template.csv'
latest_template_path = output_dir / 'manual_odds_template.csv'

expected_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'bookmaker', 'market_home_odds', 'market_draw_odds', 'market_away_odds',
    'odds_captured_at_utc', 'odds_source_note'
]

if fixtures_path.exists() and fixtures_path.stat().st_size > 0:
    try:
        fixtures = pd.read_csv(fixtures_path)
    except Exception:
        fixtures = pd.DataFrame()
else:
    fixtures = pd.DataFrame()

rows = []
if len(fixtures):
    for _, row in fixtures.iterrows():
        rows.append({
            'fixture_id': row.get('fixture_id'),
            'match_date': row.get('match_date'),
            'match_time': row.get('match_time'),
            'home_team': row.get('home_team'),
            'away_team': row.get('away_team'),
            'league': row.get('league'),
            'bookmaker': 'bet365_manual',
            'market_home_odds': '',
            'market_draw_odds': '',
            'market_away_odds': '',
            'odds_captured_at_utc': '',
            'odds_source_note': 'Fill manually from Bet365 pre-match 1X2 odds. Observation only.',
        })

template = pd.DataFrame(rows)
for col in expected_columns:
    if col not in template.columns:
        template[col] = None
template = template[expected_columns]

template.to_csv(template_path, index=False)
template.to_csv(latest_template_path, index=False)

markdown = [
    '# Manual Odds Template',
    '',
    'Use this only for forward paper-testing. Do not use for real-money betting.',
    'Fill the three 1X2 odds columns from Bet365 before kickoff, then commit/update the CSV if paper-testing manually.',
    '',
    f'Template rows: {len(template)}',
    '',
]

if len(template):
    for _, row in template.iterrows():
        markdown.append(
            f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | bookmaker={row['bookmaker']}"
        )
else:
    markdown.append('No upcoming fixtures available, so no odds template rows were generated.')

(output_dir / 'manual_odds_template.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Generated manual odds template with {len(template)} rows')
