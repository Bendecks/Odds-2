import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
log_dir = Path('data/predictions')
log_dir.mkdir(parents=True, exist_ok=True)

odds_path = Path('data/manual/manual_odds_template.csv')
poisson_path = output_dir / 'poisson_predictions.parquet'
forward_path = output_dir / 'manual_forward_snapshots.parquet'
forward_csv_path = output_dir / 'manual_forward_snapshots.csv'

expected_columns = [
    'snapshot_id', 'prediction_id', 'event_id', 'created_at_utc',
    'league', 'season', 'sample_phase', 'market', 'selection',
    'match_date', 'match_time', 'home_team', 'away_team',
    'market_odds', 'fair_odds', 'probability', 'ev',
    'bookmaker', 'odds_captured_at_utc', 'odds_source_note',
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


def norm_team(value) -> str:
    return str(value or '').strip().lower().replace('&', 'and')


odds = safe_read_csv(odds_path)
predictions = safe_read_parquet(poisson_path)
rows = []
created_at = datetime.now(timezone.utc).isoformat()

if len(odds) and len(predictions):
    for col in ['market_home_odds', 'market_draw_odds', 'market_away_odds']:
        if col not in odds.columns:
            odds[col] = None
        odds[col] = pd.to_numeric(odds[col], errors='coerce')

    filled = odds.dropna(subset=['market_home_odds', 'market_draw_odds', 'market_away_odds']).copy()

    for _, odd_row in filled.iterrows():
        home = odd_row.get('home_team')
        away = odd_row.get('away_team')

        match = predictions[
            (predictions['home_team'].apply(norm_team) == norm_team(home))
            & (predictions['away_team'].apply(norm_team) == norm_team(away))
        ]

        if match.empty:
            continue

        pred = match.iloc[0]
        event_base = f"{odd_row.get('fixture_id')}|{odd_row.get('match_date')}|{home}|{away}"
        event_id = hashlib.sha256(event_base.encode('utf-8')).hexdigest()[:16]

        market_rows = [
            ('home', odd_row.get('market_home_odds'), pred.get('fair_home_odds'), pred.get('home_win_probability')),
            ('draw', odd_row.get('market_draw_odds'), pred.get('fair_draw_odds'), pred.get('draw_probability')),
            ('away', odd_row.get('market_away_odds'), pred.get('fair_away_odds'), pred.get('away_win_probability')),
        ]

        for selection, market_odds, fair_odds, probability in market_rows:
            market_odds = pd.to_numeric(market_odds, errors='coerce')
            fair_odds = pd.to_numeric(fair_odds, errors='coerce')
            probability = pd.to_numeric(probability, errors='coerce')

            if pd.isna(market_odds) or pd.isna(fair_odds) or pd.isna(probability) or market_odds <= 1:
                continue

            ev = (float(probability) * float(market_odds)) - 1
            prediction_key = f'{event_id}|1x2|{selection}'
            prediction_id = hashlib.sha256(prediction_key.encode('utf-8')).hexdigest()[:20]
            snapshot_key = f'{prediction_id}|manual|{created_at}|{round(float(market_odds), 4)}'
            snapshot_id = hashlib.sha256(snapshot_key.encode('utf-8')).hexdigest()[:20]

            rows.append({
                'snapshot_id': snapshot_id,
                'prediction_id': prediction_id,
                'event_id': event_id,
                'created_at_utc': created_at,
                'league': odd_row.get('league', 'unknown'),
                'season': odd_row.get('season', 'unknown'),
                'sample_phase': 'paper_forward_test',
                'market': '1x2',
                'selection': selection,
                'match_date': odd_row.get('match_date'),
                'match_time': odd_row.get('match_time'),
                'home_team': home,
                'away_team': away,
                'market_odds': round(float(market_odds), 4),
                'fair_odds': round(float(fair_odds), 4),
                'probability': round(float(probability), 6),
                'ev': round(float(ev), 6),
                'bookmaker': odd_row.get('bookmaker', 'manual'),
                'odds_captured_at_utc': odd_row.get('odds_captured_at_utc'),
                'odds_source_note': odd_row.get('odds_source_note'),
            })

forward = pd.DataFrame(rows)
for col in expected_columns:
    if col not in forward.columns:
        forward[col] = None
forward = forward[expected_columns]

forward.to_parquet(forward_path, index=False)
forward.to_csv(forward_csv_path, index=False)

markdown = [
    '# Manual Forward Snapshots',
    '',
    'Built from manually captured pre-match odds. Observation-only; not real-money recommendations.',
    '',
    f'Forward snapshot rows: {len(forward)}',
    '',
]

if len(forward):
    for _, row in forward.iterrows():
        markdown.append(
            f"- {row['match_date']} {row['match_time']} | {row['home_team']} vs {row['away_team']} | "
            f"selection={str(row['selection']).upper()} | odds={row['market_odds']} | prob={row['probability']} | EV={row['ev']}"
        )
else:
    markdown.append('No manual forward snapshots built. Fill data/manual/manual_odds_template.csv with pre-match 1X2 odds first.')

(output_dir / 'manual_forward_snapshots.md').write_text('\n'.join(markdown), encoding='utf-8')

print(f'Built {len(forward)} manual forward snapshot rows')
