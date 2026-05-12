from pathlib import Path
import re

import pandas as pd

output_dir = Path('output/latest')
value_path = output_dir / 'automatic_forward_value_snapshots.parquet'
csv_path = output_dir / 'automatic_forward_value_snapshots.csv'
excluded_csv_path = output_dir / 'automatic_forward_value_snapshots_excluded_youth_reserve.csv'
report_path = output_dir / 'automatic_forward_value_snapshots_excluded_youth_reserve.md'
summary_path = output_dir / 'youth_reserve_filter_summary.csv'

EXCLUDED_PATTERN = re.compile(
    r'(\bu\s?\d{2}\b|\bunder\s?\d{2}\b|\breserve\b|\breserves\b|\breserver\b|\byouth\b|\bacademy\b|\bb\s?team\b|\bii\b)',
    re.IGNORECASE,
)


def safe_read_parquet(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_parquet(path)
    except Exception:
        return pd.DataFrame()


def clean(value):
    if pd.isna(value):
        return ''
    return str(value).strip()


def is_excluded(row) -> bool:
    text = ' '.join([
        clean(row.get('home_team')),
        clean(row.get('away_team')),
        clean(row.get('league')),
    ])
    return bool(EXCLUDED_PATTERN.search(text))


snapshots = safe_read_parquet(value_path)

if len(snapshots):
    work = snapshots.copy()
    work['excluded_youth_or_reserve'] = work.apply(is_excluded, axis=1)
    excluded = work[work['excluded_youth_or_reserve']].copy()
    kept = work[~work['excluded_youth_or_reserve']].copy()
    kept = kept.drop(columns=['excluded_youth_or_reserve'], errors='ignore')
    excluded.to_csv(excluded_csv_path, index=False)
    kept.to_parquet(value_path, index=False)
    kept.to_csv(csv_path, index=False)
else:
    kept = snapshots
    excluded = pd.DataFrame()
    pd.DataFrame().to_csv(excluded_csv_path, index=False)

summary = {
    'input_value_snapshot_rows': int(len(snapshots)),
    'kept_value_snapshot_rows': int(len(kept)),
    'excluded_youth_or_reserve_rows': int(len(excluded)),
    'filter_rule': 'exclude_u_teams_youth_reserve_academy_b_team_ii_before_paper_picks',
}
pd.DataFrame([summary]).to_csv(summary_path, index=False)

lines = [
    '# Youth / Reserve Filter Before Paper Picks',
    '',
    'These rows were removed before paper-test picks are selected and logged.',
    'Reason: youth, U-teams, reserve teams, academy teams and B-teams are too unstable for this pipeline.',
    '',
    f"Input value snapshot rows: {summary['input_value_snapshot_rows']}",
    f"Kept value snapshot rows: {summary['kept_value_snapshot_rows']}",
    f"Excluded rows: {summary['excluded_youth_or_reserve_rows']}",
    '',
]
if len(excluded):
    lines.append('## Excluded rows')
    lines.append('')
    for _, row in excluded.head(80).iterrows():
        lines.append(
            f"- {clean(row.get('match_date'))} {clean(row.get('match_time'))} | "
            f"{clean(row.get('home_team'))} vs {clean(row.get('away_team'))} | league={clean(row.get('league'))}"
        )
else:
    lines.append('No youth/reserve rows were found in this run.')

report_path.write_text('\n'.join(lines), encoding='utf-8')
print(summary)
