from pathlib import Path
from difflib import get_close_matches

import pandas as pd

output_dir = Path('output/latest')
model_dir = Path('data/model')
config_dir = Path('data/config')
config_dir.mkdir(parents=True, exist_ok=True)

fixtures_path = output_dir / 'upcoming_fixtures.csv'
ratings_path = model_dir / 'team_strengths.csv'
alias_path = config_dir / 'team_aliases.csv'

expected_alias_columns = ['source_team', 'model_team', 'note']


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def norm(value) -> str:
    text = str(value or '').lower().strip()
    for token in ['fc', 'afc', 'cf', '.', ',']:
        text = text.replace(token, '')
    text = text.replace('&', 'and')
    text = ' '.join(text.split())
    return text


fixtures = safe_read_csv(fixtures_path)
ratings = safe_read_csv(ratings_path)
aliases = safe_read_csv(alias_path)

if len(aliases) == 0:
    aliases = pd.DataFrame(columns=expected_alias_columns)
for col in expected_alias_columns:
    if col not in aliases.columns:
        aliases[col] = None
aliases = aliases[expected_alias_columns]
aliases.to_csv(alias_path, index=False)

model_team_col = 'team' if 'team' in ratings.columns else ratings.columns[0] if len(ratings.columns) else 'team'
model_teams = sorted(ratings[model_team_col].dropna().astype(str).unique().tolist()) if len(ratings) else []
model_norm_map = {norm(team): team for team in model_teams}
alias_map = {norm(row['source_team']): row['model_team'] for _, row in aliases.dropna(subset=['source_team', 'model_team']).iterrows()}

rows = []

if len(fixtures):
    for _, fixture in fixtures.iterrows():
        for side in ['home_team', 'away_team']:
            source_team = fixture.get(side)
            normalized = norm(source_team)
            match_type = 'unmatched'
            matched_team = None
            suggestion = None

            if normalized in alias_map:
                matched_team = alias_map[normalized]
                match_type = 'alias'
            elif normalized in model_norm_map:
                matched_team = model_norm_map[normalized]
                match_type = 'exact_normalized'
            else:
                close = get_close_matches(normalized, list(model_norm_map.keys()), n=1, cutoff=0.78)
                if close:
                    suggestion = model_norm_map[close[0]]
                    match_type = 'suggested_alias_needed'

            rows.append({
                'fixture_id': fixture.get('fixture_id'),
                'match_date': fixture.get('match_date'),
                'match_time': fixture.get('match_time'),
                'side': side,
                'source_team': source_team,
                'normalized_source_team': normalized,
                'matched_model_team': matched_team,
                'match_type': match_type,
                'suggested_model_team': suggestion,
            })

report = pd.DataFrame(rows)
expected_columns = [
    'fixture_id', 'match_date', 'match_time', 'side', 'source_team',
    'normalized_source_team', 'matched_model_team', 'match_type', 'suggested_model_team'
]
for col in expected_columns:
    if col not in report.columns:
        report[col] = None
report = report[expected_columns]
report.to_csv(output_dir / 'fixture_model_match_report.csv', index=False)

matched = int(report['matched_model_team'].notna().sum()) if len(report) else 0
unmatched = int((report['matched_model_team'].isna()).sum()) if len(report) else 0
suggested = int((report['match_type'] == 'suggested_alias_needed').sum()) if len(report) else 0

summary = {
    'fixture_rows': int(len(fixtures)),
    'team_rows_checked': int(len(report)),
    'matched_team_rows': matched,
    'unmatched_team_rows': unmatched,
    'suggested_alias_rows': suggested,
    'ready_for_model_fixture_join': bool(len(report) > 0 and unmatched == 0),
}
pd.DataFrame([summary]).to_csv(output_dir / 'fixture_model_match_summary.csv', index=False)

markdown = [
    '# Fixture Model Match Report',
    '',
    f"Fixture rows: {summary['fixture_rows']}",
    f"Team rows checked: {summary['team_rows_checked']}",
    f"Matched team rows: {summary['matched_team_rows']}",
    f"Unmatched team rows: {summary['unmatched_team_rows']}",
    f"Suggested alias rows: {summary['suggested_alias_rows']}",
    f"Ready for model-fixture join: {summary['ready_for_model_fixture_join']}",
    '',
]

if len(report):
    markdown.extend(['## Unmatched / suggested aliases', ''])
    subset = report[report['matched_model_team'].isna()].copy()
    if len(subset):
        for _, row in subset.iterrows():
            markdown.append(
                f"- {row['source_team']} | side={row['side']} | suggestion={row['suggested_model_team']} | type={row['match_type']}"
            )
    else:
        markdown.append('All fixture teams match the model team table.')
else:
    markdown.append('No fixtures available to match.')

(output_dir / 'fixture_model_match_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(summary)
