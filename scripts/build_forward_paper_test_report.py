from pathlib import Path
import re

import pandas as pd

output_dir = Path('output/latest')
current_path = output_dir / 'paper_test_picks.csv'
log_path = Path('data/predictions/paper_test_log.jsonl')
settled_path = output_dir / 'settled_predictions.csv'
report_path = output_dir / 'forward_paper_test_report.md'
summary_path = output_dir / 'forward_paper_test_summary.csv'

EXCLUDED_PATTERN = re.compile(r'(\bu\s?\d{2}\b|\bunder\s?\d{2}\b|\breserve\b|\breserves\b|\breserver\b|\byouth\b|\bacademy\b|\bb\s?team\b|\bii\b)', re.IGNORECASE)
FORWARD_PHASES = {'paper_forward_test', 'live_forward_snapshot', 'upcoming_fixture', 'automatic_forward_price_proxy'}


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


def parse_dt(row):
    date = clean(row.get('match_date'))
    time = clean(row.get('match_time'))
    candidate = f'{date} {time}'.strip()
    parsed = pd.to_datetime(candidate, errors='coerce', utc=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(candidate, errors='coerce', dayfirst=True)
    return parsed


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', utc=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(value, errors='coerce', dayfirst=True)
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def nice_time(value):
    text = clean(value)
    if not text:
        return 'Ukendt'
    parsed = pd.to_datetime(text, errors='coerce', utc=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(text, errors='coerce')
    if pd.isna(parsed):
        if len(text) >= 5 and text[2] == ':':
            return text[:5]
        return text
    return parsed.strftime('%H:%M')


def nice_selection(value):
    text = clean(value).lower()
    if text == 'home':
        return 'Hjemmesejr'
    if text == 'draw':
        return 'Uafgjort'
    if text == 'away':
        return 'Udebanesejr'
    return clean(value, 'Ukendt spil')


def format_number(value, digits=2, fallback='?'):
    parsed = pd.to_numeric(value, errors='coerce')
    if pd.isna(parsed):
        return fallback
    return f'{float(parsed):.{digits}f}'


def is_excluded_match(row) -> bool:
    text = ' '.join([clean(row.get('home_team')), clean(row.get('away_team')), clean(row.get('league'))])
    return bool(EXCLUDED_PATTERN.search(text))


def is_forward_row(row) -> bool:
    phase = clean(row.get('sample_phase'))
    return phase in FORWARD_PHASES or phase == ''


def make_event_key(row):
    date = clean(parse_date(row.get('match_date')))
    home = normalize_team(row.get('home_team'))
    away = normalize_team(row.get('away_team'))
    return f'{date}|{home}|{away}'


def make_bet_key(row):
    return f'{make_event_key(row)}|{clean(row.get("selection")).lower()}'


def normalize_team(value):
    text = clean(value).lower()
    replacements = {
        'rc celta de vigo': 'celta',
        'celta de vigo': 'celta',
        'levante ud': 'levante',
        'ath madrid': 'atletico madrid',
        'real sociedad': 'sociedad',
        'sociedad': 'sociedad',
        'ath bilbao': 'athletic bilbao',
        'paris sg': 'psg',
        'paris saint germain': 'psg',
        'vallecano': 'rayo vallecano',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    for token in [' fc', ' cf', ' afc', ' sc', '.', ',', '&']:
        text = text.replace(token, ' ')
    return ' '.join(text.split())


def filter_forward(df: pd.DataFrame) -> pd.DataFrame:
    if not len(df):
        return df
    work = df.copy()
    work = work[work.apply(is_forward_row, axis=1)].copy()
    work['is_youth_or_reserve'] = work.apply(is_excluded_match, axis=1)
    work = work[~work['is_youth_or_reserve']].copy()
    work['parsed_kickoff'] = work.apply(parse_dt, axis=1)
    # Drop old historical rows from the forward report. Keep only 2026+ or unknown future rows.
    if 'match_date' in work.columns:
        parsed_dates = pd.to_datetime(work['match_date'], errors='coerce', utc=True)
        fallback_dates = pd.to_datetime(work['match_date'], errors='coerce', dayfirst=True)
        parsed_dates = parsed_dates.fillna(fallback_dates)
        work = work[(parsed_dates.isna()) | (parsed_dates.dt.year >= 2026)].copy()
    return work


def dedupe_current(df: pd.DataFrame) -> pd.DataFrame:
    if not len(df):
        return df
    work = df.copy()
    work['event_key'] = work.apply(make_event_key, axis=1)
    work['bet_key'] = work.apply(make_bet_key, axis=1)
    work['score_num'] = pd.to_numeric(work.get('paper_test_score', 0), errors='coerce').fillna(0)
    work['ev_num'] = pd.to_numeric(work.get('ev', 0), errors='coerce').fillna(0)
    work = work.sort_values(['score_num', 'ev_num'], ascending=False)
    work = work.drop_duplicates('bet_key', keep='first')
    # For current report readability: max 2 picks per same normalized event.
    work['event_rank'] = work.groupby('event_key').cumcount() + 1
    work = work[work['event_rank'] <= 2].copy()
    return work.drop(columns=['event_rank'], errors='ignore')


def tier_label(value):
    text = clean(value)
    mapping = {
        'priority_proxy_observation': 'Prioritet observation',
        'volume_observation': 'Volumen observation',
        'negative_ev_control_observation': 'Kontrol-observation',
        'baseline_coverage_observation': 'Baseline-observation',
        'suppressed_band_proxy_observation': 'Suppressed observation',
    }
    return mapping.get(text, text or 'Observation')


current = filter_forward(safe_read_csv(current_path))
log = filter_forward(safe_read_jsonl(log_path))
settled = filter_forward(safe_read_csv(settled_path))

current = dedupe_current(current)
if len(current) and 'parsed_kickoff' in current.columns:
    current = current.sort_values(['parsed_kickoff', 'paper_test_score'], ascending=[True, False], na_position='last')

settled_forward = pd.DataFrame()
if len(settled) and 'settlement_status' in settled.columns:
    settled_forward = settled[settled['settlement_status'].astype(str).str.lower() == 'settled'].copy()
    if len(settled_forward):
        settled_forward['bet_key'] = settled_forward.apply(make_bet_key, axis=1)
        settled_forward = settled_forward.drop_duplicates('bet_key', keep='last')

settled_keys = set(settled_forward['bet_key'].astype(str).tolist()) if len(settled_forward) and 'bet_key' in settled_forward.columns else set()
if len(log):
    log['bet_key'] = log.apply(make_bet_key, axis=1)
    pending_log = log[~log['bet_key'].isin(settled_keys)].copy()
    pending_log = pending_log.drop_duplicates('bet_key', keep='last')
else:
    pending_log = pd.DataFrame()

won_count = 0
lost_count = 0
roi_units = 0.0
if len(settled_forward):
    won_series = settled_forward.get('won', pd.Series(dtype=object)).astype(str).str.lower()
    won_count = int((won_series == 'true').sum())
    lost_count = int((won_series == 'false').sum())
    roi_units = float(pd.to_numeric(settled_forward.get('roi_units'), errors='coerce').fillna(0).sum())

summary = {
    'current_forward_picks': int(len(current)),
    'logged_forward_picks_2026_plus': int(len(log)),
    'pending_forward_picks': int(len(pending_log)),
    'settled_forward_picks': int(len(settled_forward)),
    'won_forward': won_count,
    'lost_forward': lost_count,
    'roi_units_forward': round(roi_units, 3),
}
pd.DataFrame([summary]).to_csv(summary_path, index=False)

lines = [
    '# Forward paper-test rapport',
    '',
    'Ren rapport for nye Bet365-forward paper-picks. Gamle historiske 2025-rækker er ikke med her.',
    'Dette er stadig paper-test og ikke rigtige anbefalinger.',
    '',
    '## Kort status',
    '',
    f"- Aktuelle forward picks: **{summary['current_forward_picks']}**",
    f"- Loggede forward picks fra 2026+: **{summary['logged_forward_picks_2026_plus']}**",
    f"- Afventer forward picks: **{summary['pending_forward_picks']}**",
    f"- Settled forward picks: **{summary['settled_forward_picks']}**",
    f"- Vundne forward: **{summary['won_forward']}**",
    f"- Tabte forward: **{summary['lost_forward']}**",
    f"- ROI forward: **{summary['roi_units_forward']} units**",
    '',
    '## Aktuelle forward paper-picks',
    '',
]

if len(current):
    for _, row in current.iterrows():
        lines.extend([
            f"### {clean(row.get('home_team'), 'Ukendt hjemmehold')} vs {clean(row.get('away_team'), 'Ukendt udehold')}",
            f"- Dato: **{clean(row.get('match_date'), 'Ukendt')}**",
            f"- Kampstart: **{nice_time(row.get('match_time'))}**",
            f"- Liga: **{clean(row.get('league'), 'Ukendt')}**",
            f"- Spil: **{nice_selection(row.get('selection'))}**",
            f"- Odds: **{format_number(row.get('market_odds'))}**",
            f"- Model probability: **{format_number(row.get('probability'), digits=3)}**",
            f"- EV: **{format_number(row.get('ev'), digits=3)}**",
            f"- Edge: **{format_number(row.get('probability_edge'), digits=3)}**",
            f"- Type: **{tier_label(row.get('paper_test_tier'))}**",
            '',
        ])
else:
    lines.append('Ingen aktuelle forward paper-picks fundet.')
    lines.append('')

lines.extend(['## Afventer i forward-loggen', ''])
if len(pending_log):
    if 'parsed_kickoff' in pending_log.columns:
        pending_log = pending_log.sort_values('parsed_kickoff', ascending=True, na_position='last')
    for _, row in pending_log.tail(60).iterrows():
        lines.append(
            f"- **{clean(row.get('match_date'), 'Ukendt dato')} kl. {nice_time(row.get('match_time'))}** – {clean(row.get('home_team'), 'Ukendt')} vs {clean(row.get('away_team'), 'Ukendt')} – {nice_selection(row.get('selection'))} @ {format_number(row.get('market_odds'))} – {tier_label(row.get('paper_test_tier'))}"
        )
else:
    lines.append('Ingen afventende forward-picks fundet.')
lines.append('')

lines.extend(['## Settled forward picks', ''])
if len(settled_forward):
    for _, row in settled_forward.tail(40).iterrows():
        won = str(row.get('won')).lower() == 'true'
        result = 'Vundet' if won else 'Tabt'
        lines.append(
            f"- **{clean(row.get('match_date'), 'Ukendt dato')}** – {clean(row.get('home_team'), 'Ukendt')} vs {clean(row.get('away_team'), 'Ukendt')} – {nice_selection(row.get('selection'))} @ {format_number(row.get('market_odds', row.get('opening_market_odds')))} – **{result}** – ROI {format_number(row.get('roi_units'), digits=2)}"
        )
else:
    lines.append('Ingen settled forward-picks endnu i den rene forward-rapport.')
lines.append('')

lines.extend([
    '## Brug denne rapport til',
    '',
    '- At se de aktuelle paper-test picks uden historisk støj.',
    '- At følge om de nye Bet365-forward picks bliver settled.',
    '- At vurdere volumen før reglerne strammes igen.',
])

report_path.write_text('\n'.join(lines), encoding='utf-8')
print(summary)
