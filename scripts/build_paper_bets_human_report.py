from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
log_path = Path('data/predictions/paper_test_log.jsonl')
settled_path = output_dir / 'settled_predictions.csv'
current_path = output_dir / 'paper_test_picks.csv'
report_path = output_dir / 'paper_bets_human_report.md'
summary_path = output_dir / 'paper_bets_human_summary.csv'


def safe_read_csv(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except Exception:
        return pd.DataFrame()


def safe_read_jsonl(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame()
    try:
        return pd.read_json(path, lines=True)
    except Exception:
        return pd.DataFrame()


def clean(value, fallback=''):
    if pd.isna(value):
        return fallback
    text = str(value).strip()
    if text.lower() in {'nan', 'none', 'nat'}:
        return fallback
    return text


def nice_selection(value):
    text = clean(value).lower()
    if text == 'home':
        return 'Hjemmesejr'
    if text == 'draw':
        return 'Uafgjort'
    if text == 'away':
        return 'Udebanesejr'
    return clean(value, 'Ukendt spil')


def nice_status(row):
    status = clean(row.get('settlement_status')).lower()
    if status == 'settled':
        won = row.get('won')
        if str(won).lower() == 'true' or won is True:
            return 'Vundet'
        if str(won).lower() == 'false' or won is False:
            return 'Tabt'
        return 'Afgjort'
    return 'Afventer'


def format_number(value, digits=2, fallback='?'):
    parsed = pd.to_numeric(value, errors='coerce')
    if pd.isna(parsed):
        return fallback
    return f'{float(parsed):.{digits}f}'


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', utc=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(value, errors='coerce', dayfirst=True)
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def make_bet_key(row):
    return '|'.join([
        clean(parse_date(row.get('match_date'))),
        clean(row.get('home_team')).lower(),
        clean(row.get('away_team')).lower(),
        clean(row.get('selection')).lower(),
    ])


def dedupe_bets(df: pd.DataFrame) -> pd.DataFrame:
    if not len(df):
        return df
    work = df.copy()
    work['human_bet_key'] = work.apply(make_bet_key, axis=1)
    sort_cols = []
    if 'paper_test_score' in work.columns:
        work['paper_test_score_num'] = pd.to_numeric(work['paper_test_score'], errors='coerce').fillna(0)
        sort_cols.append('paper_test_score_num')
    if 'created_at_utc' in work.columns:
        sort_cols.append('created_at_utc')
    if sort_cols:
        ascending = [False if col == 'paper_test_score_num' else False for col in sort_cols]
        work = work.sort_values(sort_cols, ascending=ascending)
    return work.drop_duplicates('human_bet_key', keep='first')


current = safe_read_csv(current_path)
log = safe_read_jsonl(log_path)
settled = safe_read_csv(settled_path)

current = dedupe_bets(current)
log = dedupe_bets(log)

settled_keys = set()
settled_forward = pd.DataFrame()
if len(settled):
    settled = settled.copy()
    settled['human_bet_key'] = settled.apply(make_bet_key, axis=1)
    settled_forward = settled[settled.get('settlement_status', '').astype(str).str.lower() == 'settled'].copy()
    settled_keys = set(settled_forward['human_bet_key'].dropna().astype(str).tolist())

if len(log):
    log = log.copy()
    log['human_bet_key'] = log.apply(make_bet_key, axis=1)
    pending = log[~log['human_bet_key'].isin(settled_keys)].copy()
else:
    pending = pd.DataFrame()

# If current picks exist, prefer showing those as the immediate active list, but keep pending-log count in summary.
current_display = current.copy()
if len(current_display):
    current_display['human_bet_key'] = current_display.apply(make_bet_key, axis=1)
    current_display = current_display[~current_display['human_bet_key'].isin(settled_keys)].copy()

won_count = 0
lost_count = 0
roi_units = 0.0
if len(settled_forward):
    won_series = settled_forward.get('won', pd.Series(dtype=object)).astype(str).str.lower()
    won_count = int((won_series == 'true').sum())
    lost_count = int((won_series == 'false').sum())
    roi_units = float(pd.to_numeric(settled_forward.get('roi_units'), errors='coerce').fillna(0).sum())

summary = {
    'current_visible_picks': int(len(current_display)),
    'logged_unique_paper_picks': int(len(log)),
    'pending_logged_picks': int(len(pending)),
    'settled_paper_picks_found': int(len(settled_forward)),
    'won': won_count,
    'lost': lost_count,
    'roi_units': round(roi_units, 3),
    'has_forward_settlement': bool(len(settled_forward) > 0),
}
pd.DataFrame([summary]).to_csv(summary_path, index=False)

lines = [
    '# Paper bets – enkelt overblik',
    '',
    'Dette er det menneskelige overblik over paper bets. Det er stadig kun test og ikke rigtige anbefalinger.',
    '',
    '## Kort status',
    '',
    f"- Aktuelle viste paper picks: **{summary['current_visible_picks']}**",
    f"- Unikke loggede paper picks: **{summary['logged_unique_paper_picks']}**",
    f"- Afventer i loggen: **{summary['pending_logged_picks']}**",
    f"- Afgjorte fundet i settled-filen: **{summary['settled_paper_picks_found']}**",
    f"- Vundne: **{summary['won']}**",
    f"- Tabte: **{summary['lost']}**",
    f"- Samlet ROI i units: **{summary['roi_units']}**",
    '',
]

lines.extend(['## Aktuelle paper picks', ''])
if len(current_display):
    for _, row in current_display.head(20).iterrows():
        lines.extend([
            f"### {clean(row.get('home_team'), 'Ukendt hjemmehold')} vs {clean(row.get('away_team'), 'Ukendt udehold')}",
            f"- Dato: **{clean(row.get('match_date'), 'Ukendt')}**",
            f"- Spil: **{nice_selection(row.get('selection'))}**",
            f"- Odds: **{format_number(row.get('market_odds'))}**",
            f"- Status: **Afventer**",
            f"- Type: **{clean(row.get('paper_test_tier'), 'paper observation')}**",
            f"- Note: **{clean(row.get('paper_test_reason'), 'Kun paper-test')}**",
            '',
        ])
else:
    lines.append('Der er ingen aktuelle viste paper picks lige nu.')
    lines.append('')

lines.extend(['## Afgjorte paper picks', ''])
if len(settled_forward):
    display_settled = settled_forward.copy()
    if 'match_date' in display_settled.columns:
        display_settled['parsed_date'] = display_settled['match_date'].apply(parse_date)
        display_settled = display_settled.sort_values('parsed_date', ascending=False, na_position='last')
    for _, row in display_settled.head(30).iterrows():
        lines.extend([
            f"### {clean(row.get('home_team'), 'Ukendt hjemmehold')} vs {clean(row.get('away_team'), 'Ukendt udehold')}",
            f"- Dato: **{clean(row.get('match_date'), 'Ukendt')}**",
            f"- Spil: **{nice_selection(row.get('selection'))}**",
            f"- Odds: **{format_number(row.get('market_odds', row.get('opening_market_odds')))}**",
            f"- Resultat: **{nice_status(row)}**",
            f"- Kampens udfald: **{clean(row.get('match_result'), 'Ukendt')}**",
            f"- ROI: **{format_number(row.get('roi_units'), digits=2)} units**",
            '',
        ])
else:
    lines.append('Der er endnu ingen af de nye paper picks, som tydeligt er settled her.')
    lines.append('')

lines.extend(['## Afventer i loggen', ''])
if len(pending):
    pending_display = pending.copy()
    if 'match_date' in pending_display.columns:
        pending_display['parsed_date'] = pending_display['match_date'].apply(parse_date)
        pending_display = pending_display.sort_values('parsed_date', ascending=True, na_position='last')
    for _, row in pending_display.head(30).iterrows():
        lines.append(
            f"- **{clean(row.get('match_date'), 'Ukendt dato')}** – {clean(row.get('home_team'), 'Ukendt')} vs {clean(row.get('away_team'), 'Ukendt')} – {nice_selection(row.get('selection'))} @ {format_number(row.get('market_odds'))}"
        )
else:
    lines.append('Ingen afventende loggede paper picks fundet.')
lines.append('')

lines.extend([
    '## Hvad betyder det?',
    '',
    '- **Aktuelle paper picks** er dem systemet ville følge lige nu.',
    '- **Afventer** betyder, at kampen ikke er tydeligt afgjort i systemet endnu.',
    '- **Afgjorte paper picks** er dem, hvor systemet har fundet resultat og win/loss.',
    '- Rapporten er lavet til overblik. De tekniske filer ligger stadig ved siden af, men du behøver normalt ikke åbne dem.',
])

report_path.write_text('\n'.join(lines), encoding='utf-8')
print(summary)
