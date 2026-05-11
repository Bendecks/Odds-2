import hashlib
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

predictions_path = output_dir / 'forward_fixture_predictions.csv'
prices_path = output_dir / 'football_data_upcoming_odds.csv'
value_path = output_dir / 'automatic_forward_value_snapshots.csv'

expected_columns = [
    'snapshot_id', 'prediction_id', 'fixture_id', 'match_date', 'match_time',
    'home_team', 'away_team', 'league', 'sample_phase', 'source_name', 'source_type',
    'source_quality', 'selection', 'market_odds', 'fair_odds', 'probability',
    'market_implied_probability', 'probability_edge', 'ev', 'match_confidence',
]


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
    return ' '.join(text.split())


def similarity(a, b) -> float:
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


predictions = safe_read_csv(predictions_path)
prices = safe_read_csv(prices_path)
rows = []

if len(predictions) and len(prices):
    for _, pred in predictions.iterrows():
        pred_date = str(pred.get('match_date'))
        candidates = prices[prices['match_date'].astype(str) == pred_date].copy() if 'match_date' in prices.columns else prices.copy()

        best_price_rows = []
        for _, price in candidates.iterrows():
            home_sim = similarity(pred.get('home_team'), price.get('home_team'))
            away_sim = similarity(pred.get('away_team'), price.get('away_team'))
            match_confidence = round((home_sim + away_sim) / 2, 4)
            if match_confidence >= 0.74:
                best_price_rows.append((match_confidence, price))

        for match_confidence, price in best_price_rows:
            markets = [
                ('home', price.get('market_home_odds'), pred.get('fair_home_odds'), pred.get('home_win_probability')),
                ('draw', price.get('market_draw_odds'), pred.get('fair_draw_odds'), pred.get('draw_probability')),
                ('away', price.get('market_away_odds'), pred.get('fair_away_odds'), pred.get('away_win_probability')),
            ]
            fixture_id = pred.get('fixture_id') or price.get('fixture_id')
            for selection, market_odds, fair_odds, probability in markets:
                market_odds = pd.to_numeric(market_odds, errors='coerce')
                fair_odds = pd.to_numeric(fair_odds, errors='coerce')
                probability = pd.to_numeric(probability, errors='coerce')
                if pd.isna(market_odds) or pd.isna(fair_odds) or pd.isna(probability):
                    continue
                if market_odds <= 1 or probability <= 0:
                    continue

                ev = float(probability) * float(market_odds) - 1
                implied = 1 / float(market_odds)
                prediction_id = pred.get('prediction_id')
                snapshot_key = f"{prediction_id}|{price.get('source_name')}|{selection}|{market_odds}"
                snapshot_id = hashlib.sha256(snapshot_key.encode('utf-8')).hexdigest()[:20]

                rows.append({
                    'snapshot_id': snapshot_id,
                    'prediction_id': prediction_id,
                    'fixture_id': fixture_id,
                    'match_date': pred.get('match_date'),
                    'match_time': pred.get('match_time'),
                    'home_team': pred.get('home_team'),
                    'away_team': pred.get('away_team'),
                    'league': pred.get('league'),
                    'sample_phase': 'automatic_forward_price_proxy',
                    'source_name': price.get('source_name'),
                    'source_type': price.get('source_type'),
                    'source_quality': price.get('source_quality'),
                    'selection': selection,
                    'market_odds': round(float(market_odds), 4),
                    'fair_odds': round(float(fair_odds), 4),
                    'probability': round(float(probability), 6),
                    'market_implied_probability': round(float(implied), 6),
                    'probability_edge': round(float(probability) - float(implied), 6),
                    'ev': round(float(ev), 6),
                    'match_confidence': match_confidence,
                })

snapshots = pd.DataFrame(rows)
for col in expected_columns:
    if col not in snapshots.columns:
        snapshots[col] = None
snapshots = snapshots[expected_columns]
snapshots.to_csv(value_path, index=False)
snapshots.to_parquet(output_dir / 'automatic_forward_value_snapshots.parquet', index=False)

summary = {
    'forward_prediction_rows': int(len(predictions)),
    'proxy_price_rows': int(len(prices)),
    'value_snapshot_rows': int(len(snapshots)),
    'positive_ev_rows': int((pd.to_numeric(snapshots['ev'], errors='coerce') > 0).sum()) if len(snapshots) else 0,
    'source_type': 'delayed_market_proxy',
    'real_money_ready': False,
}
pd.DataFrame([summary]).to_csv(output_dir / 'automatic_forward_value_snapshot_summary.csv', index=False)

markdown = [
    '# Automatic Forward Value Snapshots',
    '',
    'Delayed/free market proxy joined to forward probability predictions.',
    'Not live odds, not Bet365 direct, and not real-money ready.',
    '',
    f"Forward prediction rows: {summary['forward_prediction_rows']}",
    f"Proxy price rows: {summary['proxy_price_rows']}",
    f"Value snapshot rows: {summary['value_snapshot_rows']}",
    f"Positive EV rows: {summary['positive_ev_rows']}",
    '',
]

if len(snapshots):
    display = snapshots.sort_values('ev', ascending=False).head(30)
    for _, row in display.iterrows():
        markdown.append(
            f"- {row['match_date']} | {row['home_team']} vs {row['away_team']} | "
            f"sel={str(row['selection']).upper()} | src={row['source_name']} | odds={row['market_odds']} | "
            f"prob={row['probability']} | EV={row['ev']} | match={row['match_confidence']}"
        )
else:
    markdown.append('No automatic forward value snapshots were built. Check proxy odds availability and team/date matching.')

(output_dir / 'automatic_forward_value_snapshots.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
