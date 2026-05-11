import hashlib
from difflib import SequenceMatcher
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')

predictions_path = output_dir / 'forward_fixture_predictions.csv'
prices_path = output_dir / 'automatic_forward_prices.csv'
fallback_prices_path = output_dir / 'football_data_upcoming_odds.csv'
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
    replacements = {
        'hotspur': '',
        'united': '',
        'utd': '',
        'town': '',
        'city': '',
        'fc': '',
        'afc': '',
        'cf': '',
        '.': '',
        ',': '',
        '&': 'and',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return ' '.join(text.split())


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', dayfirst=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(value, errors='coerce')
    if pd.isna(parsed):
        return None
    return parsed.date().isoformat()


def similarity(a, b) -> float:
    na = norm(a)
    nb = norm(b)
    if not na or not nb:
        return 0.0
    if na == nb:
        return 1.0
    if na in nb or nb in na:
        return 0.92
    return SequenceMatcher(None, na, nb).ratio()


predictions = safe_read_csv(predictions_path)
prices = safe_read_csv(prices_path)
if len(prices) == 0:
    prices = safe_read_csv(fallback_prices_path)
rows = []
match_diagnostics = []

if len(predictions) and len(prices):
    predictions['parsed_match_date'] = predictions['match_date'].apply(parse_date) if 'match_date' in predictions.columns else None
    prices['parsed_match_date'] = prices['match_date'].apply(parse_date) if 'match_date' in prices.columns else None

    for _, pred in predictions.iterrows():
        pred_date = pred.get('parsed_match_date')
        candidates = prices[prices['parsed_match_date'] == pred_date].copy() if pred_date else prices.copy()

        if len(candidates) == 0:
            candidates = prices.copy()

        best_price_rows = []
        best_diag = {
            'prediction_id': pred.get('prediction_id'),
            'match_date': pred.get('match_date'),
            'home_team': pred.get('home_team'),
            'away_team': pred.get('away_team'),
            'candidate_rows': int(len(candidates)),
            'best_home_team': None,
            'best_away_team': None,
            'best_match_confidence': 0.0,
            'matched_rows': 0,
            'matched_odds_api_io_rows': 0,
        }

        for _, price in candidates.iterrows():
            home_sim = similarity(pred.get('home_team'), price.get('home_team'))
            away_sim = similarity(pred.get('away_team'), price.get('away_team'))
            match_confidence = round((home_sim + away_sim) / 2, 4)
            if match_confidence > best_diag['best_match_confidence']:
                best_diag.update({
                    'best_home_team': price.get('home_team'),
                    'best_away_team': price.get('away_team'),
                    'best_match_confidence': match_confidence,
                })
            if match_confidence >= 0.68:
                best_price_rows.append((match_confidence, price))

        best_diag['matched_rows'] = int(len(best_price_rows))
        best_diag['matched_odds_api_io_rows'] = int(sum(1 for _, p in best_price_rows if 'odds_api_io' in str(p.get('source_name'))))
        match_diagnostics.append(best_diag)

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

match_diag = pd.DataFrame(match_diagnostics)
match_diag.to_csv(output_dir / 'automatic_forward_value_match_diagnostics.csv', index=False)

source_counts = snapshots['source_name'].value_counts().to_dict() if len(snapshots) and 'source_name' in snapshots.columns else {}
odds_api_io_snapshot_rows = int(snapshots['source_name'].astype(str).str.contains('odds_api_io', na=False).sum()) if len(snapshots) else 0
summary = {
    'forward_prediction_rows': int(len(predictions)),
    'proxy_price_rows': int(len(prices)),
    'value_snapshot_rows': int(len(snapshots)),
    'positive_ev_rows': int((pd.to_numeric(snapshots['ev'], errors='coerce') > 0).sum()) if len(snapshots) else 0,
    'matched_prediction_rows': int((match_diag['matched_rows'] > 0).sum()) if len(match_diag) and 'matched_rows' in match_diag.columns else 0,
    'odds_api_io_snapshot_rows': odds_api_io_snapshot_rows,
    'source_counts': str(source_counts),
    'source_type': 'combined_automatic_forward_market_proxy',
    'real_money_ready': False,
}
pd.DataFrame([summary]).to_csv(output_dir / 'automatic_forward_value_snapshot_summary.csv', index=False)

markdown = [
    '# Automatic Forward Value Snapshots',
    '',
    'Combined automatic forward market proxy joined to forward probability predictions.',
    'Includes Football-Data delayed proxy and capped odds-api.io single-event proxy when available.',
    'Not live/full-market coverage and not real-money ready.',
    '',
    f"Forward prediction rows: {summary['forward_prediction_rows']}",
    f"Proxy price rows: {summary['proxy_price_rows']}",
    f"Matched prediction rows: {summary['matched_prediction_rows']}",
    f"Value snapshot rows: {summary['value_snapshot_rows']}",
    f"odds-api.io snapshot rows: {summary['odds_api_io_snapshot_rows']}",
    f"Positive EV rows: {summary['positive_ev_rows']}",
    f"Source counts: {summary['source_counts']}",
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
    if len(match_diag):
        markdown.extend(['', '## Best match diagnostics', ''])
        for _, row in match_diag.head(20).iterrows():
            markdown.append(
                f"- {row.get('home_team')} vs {row.get('away_team')} | candidates={row.get('candidate_rows')} | "
                f"best={row.get('best_home_team')} vs {row.get('best_away_team')} | confidence={row.get('best_match_confidence')}"
            )

(output_dir / 'automatic_forward_value_snapshots.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
