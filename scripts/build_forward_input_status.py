from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
manual_path = Path('data/manual/manual_odds_template.csv')
fixtures_path = output_dir / 'upcoming_fixtures.csv'
forward_path = output_dir / 'manual_forward_snapshots.parquet'

markdown = [
    '# Forward Input Status',
    '',
    'Manual Bet365 odds input is parked as an optional fallback. It is not an active development blocker.',
    'Current priority: automatic/free-data forward-testing sources and robust fixture/model matching.',
    '',
]


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def safe_read_parquet(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_parquet(path)
    except Exception:
        return pd.DataFrame()


fixtures = safe_read_csv(fixtures_path)
manual = safe_read_csv(manual_path)
forward = safe_read_parquet(forward_path)

filled_rows = 0
missing_rows = 0

if len(manual):
    for col in ['market_home_odds', 'market_draw_odds', 'market_away_odds']:
        if col not in manual.columns:
            manual[col] = None
        manual[col] = pd.to_numeric(manual[col], errors='coerce')

    complete_mask = manual[['market_home_odds', 'market_draw_odds', 'market_away_odds']].notna().all(axis=1)
    filled_rows = int(complete_mask.sum())
    missing_rows = int((~complete_mask).sum())

summary = {
    'upcoming_fixtures': int(len(fixtures)),
    'manual_template_rows': int(len(manual)),
    'manual_odds_complete_rows': filled_rows,
    'manual_odds_missing_rows': missing_rows,
    'manual_forward_snapshot_rows': int(len(forward)),
    'manual_odds_mode': 'optional_fallback_paused',
    'manual_odds_is_blocker': False,
    'ready_for_manual_forward_generation': bool(len(forward) > 0),
    'automatic_forward_source_needed': True,
}

pd.DataFrame([summary]).to_csv(output_dir / 'forward_input_status.csv', index=False)

markdown.extend([
    f"Upcoming fixtures: {summary['upcoming_fixtures']}",
    f"Manual template rows: {summary['manual_template_rows']}",
    f"Rows with complete manual odds: {summary['manual_odds_complete_rows']}",
    f"Rows missing manual odds: {summary['manual_odds_missing_rows']}",
    f"Manual forward snapshot rows: {summary['manual_forward_snapshot_rows']}",
    f"Manual odds mode: {summary['manual_odds_mode']}",
    f"Manual odds is blocker: {summary['manual_odds_is_blocker']}",
    f"Automatic forward source needed: {summary['automatic_forward_source_needed']}",
    '',
])

markdown.extend(['## Current automatic-forward blocker', ''])
if len(fixtures) == 0:
    markdown.append('No upcoming fixtures are available from the current free fixture source.')
else:
    markdown.append('Upcoming fixtures exist, but no automatic odds/proxy forward snapshot source is active yet.')

markdown.extend(['', '## Optional manual fallback status', ''])
if len(manual):
    incomplete = manual[manual[['market_home_odds', 'market_draw_odds', 'market_away_odds']].isna().any(axis=1)].copy()
    if len(incomplete):
        markdown.append('Manual odds are not required in the current phase. These rows are only kept for later fallback use:')
        for _, row in incomplete.head(20).iterrows():
            markdown.append(
                f"- {row.get('match_date')} {row.get('match_time')} | {row.get('home_team')} vs {row.get('away_team')}"
            )
    else:
        markdown.append('Manual odds rows are complete, but manual flow remains optional fallback only.')
else:
    markdown.append('No manual odds template rows are available yet.')

(output_dir / 'forward_input_status.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
