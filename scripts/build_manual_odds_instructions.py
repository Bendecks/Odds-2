from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
template_path = output_dir / 'manual_odds_template.csv'

markdown = [
    '# Manual Odds Entry Instructions',
    '',
    'Purpose: create real forward paper-test snapshots from Bet365 pre-match 1X2 odds.',
    '',
    'Do not stake real money from this system.',
    '',
    '## What to fill',
    '',
    'Open `data/manual/manual_odds_template.csv` and fill these columns only:',
    '',
    '- `market_home_odds`',
    '- `market_draw_odds`',
    '- `market_away_odds`',
    '- `odds_captured_at_utc`',
    '',
    'Use decimal odds from Bet365 1X2 / Full Time Result before kickoff.',
    '',
    '## Current rows needing odds',
    '',
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


template = safe_read_csv(template_path)

if len(template):
    for col in ['market_home_odds', 'market_draw_odds', 'market_away_odds']:
        if col not in template.columns:
            template[col] = None
        template[col] = pd.to_numeric(template[col], errors='coerce')
    missing = template[template[['market_home_odds', 'market_draw_odds', 'market_away_odds']].isna().any(axis=1)]
    if len(missing):
        for _, row in missing.iterrows():
            markdown.append(f"- {row.get('match_date')} {row.get('match_time')} | {row.get('home_team')} vs {row.get('away_team')}")
    else:
        markdown.append('No rows need odds. Manual template appears complete.')
else:
    markdown.append('No manual odds template rows available yet.')

markdown.extend([
    '',
    '## After filling odds',
    '',
    'Run the workflow again. Expected result:',
    '',
    '- `manual_forward_snapshots` becomes greater than 0',
    '- `paper_test_picks` may become greater than 0',
    '- `candidate_bets` may still remain 0, which is acceptable',
])

(output_dir / 'manual_odds_instructions.md').write_text('\n'.join(markdown), encoding='utf-8')
print('Generated manual odds instructions')
