import json
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
raw_dir = Path('data/raw/odds_api_io')
report_path = output_dir / 'odds_api_io_market_inventory_report.md'
summary_path = output_dir / 'odds_api_io_market_inventory_summary.csv'
markets_csv_path = output_dir / 'odds_api_io_market_inventory.csv'
sports_report_path = output_dir / 'market_expansion_notes.md'

raw_files = sorted(raw_dir.glob('odds_multi*_latest.json')) + sorted(raw_dir.glob('odds_multi_extra_*_latest.json'))

market_rows = []
market_counter = Counter()
bookmaker_counter = Counter()
sport_counter = Counter()
league_counter = Counter()
event_counter = 0


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None


def odds_response_items(payload):
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        if 'bookmakers' in payload and ('id' in payload or 'eventId' in payload or 'event_id' in payload):
            return [payload]
        for key in ['events', 'data', 'results', 'odds']:
            if isinstance(payload.get(key), list):
                return payload.get(key)
        values = [v for v in payload.values() if isinstance(v, dict) and 'bookmakers' in v]
        if values:
            return values
    return []


def clean(value):
    if value is None:
        return ''
    return str(value).strip()


def classify_market(name):
    text = clean(name).lower()
    if text in {'ml', 'moneyline', 'match winner', 'match_winner', 'full time result', 'fulltime result', '1x2', '3-way result'}:
        return '1X2 / Match result'
    if 'total' in text or 'over' in text or 'under' in text:
        return 'Goals total / Over-Under'
    if 'handicap' in text or 'spread' in text or 'asian' in text or 'hdp' in text:
        return 'Handicap / Spread'
    if 'both' in text and 'score' in text:
        return 'Both teams to score'
    if 'double chance' in text or text in {'1x', 'x2', '12'}:
        return 'Double chance'
    if 'correct score' in text:
        return 'Correct score'
    if 'half' in text or 'ht' in text:
        return 'Half-time / Period'
    return 'Other / Unknown'


def first_line_or_label(odds_items):
    if not odds_items:
        return ''
    first = odds_items[0]
    if not isinstance(first, dict):
        return ''
    for key in ['label', 'hdp', 'total', 'line', 'points']:
        if key in first and first.get(key) is not None:
            return clean(first.get(key))
    return ''

for raw_file in raw_files:
    payload = load_json(raw_file)
    for event in odds_response_items(payload):
        if not isinstance(event, dict):
            continue
        event_counter += 1
        event_id = clean(event.get('id') or event.get('eventId') or event.get('event_id'))
        home = clean(event.get('home'))
        away = clean(event.get('away'))
        sport = event.get('sport')
        league = event.get('league')
        sport_name = clean(sport.get('name') if isinstance(sport, dict) else sport) or 'unknown'
        league_name = clean(league.get('name') if isinstance(league, dict) else league) or 'unknown'
        sport_counter[sport_name] += 1
        league_counter[league_name] += 1
        bookmakers = event.get('bookmakers')
        if not isinstance(bookmakers, dict):
            continue
        for bookmaker_name, markets in bookmakers.items():
            bookmaker_counter[bookmaker_name] += 1
            if not isinstance(markets, list):
                continue
            for market in markets:
                if not isinstance(market, dict):
                    continue
                market_name = clean(market.get('name')) or 'unknown'
                odds_items = market.get('odds') or []
                if isinstance(odds_items, dict):
                    odds_items = [odds_items]
                market_type = classify_market(market_name)
                line_or_label = first_line_or_label(odds_items)
                market_counter[(bookmaker_name, market_name, market_type)] += 1
                market_rows.append({
                    'raw_file': raw_file.name,
                    'event_id': event_id,
                    'home_team': home,
                    'away_team': away,
                    'sport': sport_name,
                    'league': league_name,
                    'bookmaker': bookmaker_name,
                    'market_name': market_name,
                    'market_type': market_type,
                    'line_or_label': line_or_label,
                    'outcome_rows': len(odds_items),
                })

market_df = pd.DataFrame(market_rows)
market_df.to_csv(markets_csv_path, index=False)

if len(market_df):
    market_type_counts = market_df['market_type'].value_counts().to_dict()
    market_name_counts = market_df['market_name'].value_counts().head(30).to_dict()
    bet365_market_df = market_df[market_df['bookmaker'].astype(str).str.lower() == 'bet365']
    bet365_market_type_counts = bet365_market_df['market_type'].value_counts().to_dict()
    bet365_market_name_counts = bet365_market_df['market_name'].value_counts().head(30).to_dict()
else:
    market_type_counts = {}
    market_name_counts = {}
    bet365_market_type_counts = {}
    bet365_market_name_counts = {}

summary = {
    'raw_files_scanned': len(raw_files),
    'events_seen_in_raw_odds': event_counter,
    'market_rows_seen': int(len(market_df)),
    'unique_bookmakers': int(market_df['bookmaker'].nunique()) if len(market_df) else 0,
    'unique_market_names': int(market_df['market_name'].nunique()) if len(market_df) else 0,
    'bet365_market_rows': int(len(market_df[market_df['bookmaker'].astype(str).str.lower() == 'bet365'])) if len(market_df) else 0,
    'market_type_counts': str(market_type_counts),
    'bet365_market_type_counts': str(bet365_market_type_counts),
    'recommended_next_market': 'Over/Under 2.5 if present in Bet365 raw market inventory; otherwise continue inventory only.',
    'sports_expansion_recommendation': 'Do not activate new sports yet. Inventory only; build separate model per sport first.',
}
pd.DataFrame([summary]).to_csv(summary_path, index=False)

lines = [
    '# Odds-API.io Market Inventory',
    '',
    'Purpose: inspect the raw Odds-API.io odds responses we already fetch, without adding extra API calls.',
    'This report does not activate new markets. It only shows what may be available for future model expansion.',
    '',
    f"Raw files scanned: {summary['raw_files_scanned']}",
    f"Events seen in raw odds: {summary['events_seen_in_raw_odds']}",
    f"Market rows seen: {summary['market_rows_seen']}",
    f"Unique bookmakers: {summary['unique_bookmakers']}",
    f"Unique market names: {summary['unique_market_names']}",
    f"Bet365 market rows: {summary['bet365_market_rows']}",
    '',
    '## Market types found',
    '',
]
if market_type_counts:
    for name, count in market_type_counts.items():
        lines.append(f'- {name}: {count}')
else:
    lines.append('- No raw market data found yet.')

lines.extend(['', '## Bet365 market types found', ''])
if bet365_market_type_counts:
    for name, count in bet365_market_type_counts.items():
        lines.append(f'- {name}: {count}')
else:
    lines.append('- No Bet365 market data found yet.')

lines.extend(['', '## Most common Bet365 market names', ''])
if bet365_market_name_counts:
    for name, count in bet365_market_name_counts.items():
        lines.append(f'- {name}: {count}')
else:
    lines.append('- No Bet365 market names found yet.')

lines.extend(['', '## Expansion assessment', ''])
lines.extend([
    '- 1X2 / match result is already active.',
    '- Over/Under 2.5 is the first sensible expansion candidate because it can be derived from a goals/Poisson model.',
    '- Both Teams To Score may also be possible after goal expectation quality is checked.',
    '- Handicap/spread should wait until the model has a reliable goal-difference distribution and enough settled paper data.',
    '- New sports should stay inventory-only for now; each sport needs a separate probability model.',
])

report_path.write_text('\n'.join(lines), encoding='utf-8')

notes = [
    '# Market and Sport Expansion Notes',
    '',
    'Current active betting model: football 1X2 / full-time result, Bet365 only.',
    '',
    'Expansion rule: use existing raw Odds-API.io responses first. Do not spend extra requests just to explore markets unless we explicitly decide to run an inventory test.',
    '',
    'Priority order:',
    '1. Football Over/Under 2.5 – best fit with current goals model.',
    '2. Football Both Teams To Score – possible after checking expected goals quality.',
    '3. Football handicap/spread – later, higher modelling risk.',
    '4. Other sports – inventory only until a sport-specific model exists.',
    '',
    'Do not mix non-football markets into the current paper-pick log until they have their own model, filters, and settlement report.',
]
sports_report_path.write_text('\n'.join(notes), encoding='utf-8')

print(summary)
