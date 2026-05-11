from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

raw_dir = Path('data/raw/football_data_upcoming')
output_dir = Path('output/latest')
raw_dir.mkdir(parents=True, exist_ok=True)
output_dir.mkdir(parents=True, exist_ok=True)

# Football-Data upcoming fixtures page links to fixtures.csv for upcoming matches.
# This is a delayed/free market proxy, not live odds and not a real-money source.
SOURCE_URLS = [
    'https://www.football-data.co.uk/fixtures.csv',
]

expected_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'source_name', 'source_type', 'market_home_odds', 'market_draw_odds',
    'market_away_odds', 'price_captured_at_utc', 'source_quality', 'raw_source_url'
]

bookmaker_sets = [
    ('B365H', 'B365D', 'B365A', 'football_data_bet365_proxy'),
    ('PSH', 'PSD', 'PSA', 'football_data_pinnacle_proxy'),
    ('MaxH', 'MaxD', 'MaxA', 'football_data_max_market_proxy'),
    ('AvgH', 'AvgD', 'AvgA', 'football_data_average_market_proxy'),
    ('BbAvH', 'BbAvD', 'BbAvA', 'football_data_bookmaker_average_proxy'),
]

league_map = {
    'E0': 'premier_league',
    'E1': 'championship',
    'D1': 'bundesliga',
    'SP1': 'la_liga',
    'I1': 'serie_a',
    'F1': 'ligue_1',
}

rows = []
errors = []
fetched_at = datetime.now(timezone.utc).isoformat()
raw_frames = []

for url in SOURCE_URLS:
    try:
        df = pd.read_csv(url)
        df['raw_source_url'] = url
        raw_frames.append(df)
    except Exception as exc:
        errors.append({'url': url, 'error': repr(exc)})

if raw_frames:
    raw = pd.concat(raw_frames, ignore_index=True)
else:
    raw = pd.DataFrame()

raw.to_csv(raw_dir / 'football_data_upcoming_raw.csv', index=False)

if len(raw):
    for _, row in raw.iterrows():
        home = row.get('HomeTeam') or row.get('Home') or row.get('Home Team')
        away = row.get('AwayTeam') or row.get('Away') or row.get('Away Team')
        date = row.get('Date') or row.get('MatchDate') or row.get('DateTime')
        time = row.get('Time') or row.get('KO') or ''
        div = row.get('Div') or row.get('League') or 'unknown'

        for h_col, d_col, a_col, source_name in bookmaker_sets:
            if h_col not in raw.columns or d_col not in raw.columns or a_col not in raw.columns:
                continue
            home_odds = pd.to_numeric(row.get(h_col), errors='coerce')
            draw_odds = pd.to_numeric(row.get(d_col), errors='coerce')
            away_odds = pd.to_numeric(row.get(a_col), errors='coerce')
            if pd.isna(home_odds) or pd.isna(draw_odds) or pd.isna(away_odds):
                continue
            if min(home_odds, draw_odds, away_odds) <= 1:
                continue

            fixture_id = f"fd_{div}_{date}_{home}_{away}".replace(' ', '_').replace('/', '-')
            rows.append({
                'fixture_id': fixture_id,
                'match_date': date,
                'match_time': time,
                'home_team': home,
                'away_team': away,
                'league': league_map.get(str(div), str(div)),
                'source_name': source_name,
                'source_type': 'delayed_market_proxy',
                'market_home_odds': round(float(home_odds), 4),
                'market_draw_odds': round(float(draw_odds), 4),
                'market_away_odds': round(float(away_odds), 4),
                'price_captured_at_utc': fetched_at,
                'source_quality': 'free_delayed_fixture_odds_proxy',
                'raw_source_url': row.get('raw_source_url'),
            })

prices = pd.DataFrame(rows)
for col in expected_columns:
    if col not in prices.columns:
        prices[col] = None
prices = prices[expected_columns]
prices.to_csv(raw_dir / 'football_data_upcoming_odds.csv', index=False)
prices.to_csv(output_dir / 'football_data_upcoming_odds.csv', index=False)

summary = {
    'raw_rows': int(len(raw)),
    'proxy_price_rows': int(len(prices)),
    'sources_attempted': len(SOURCE_URLS),
    'errors': int(len(errors)),
    'source_quality': 'free_delayed_market_proxy',
}
pd.DataFrame([summary]).to_csv(output_dir / 'football_data_upcoming_odds_status.csv', index=False)

markdown = [
    '# Football-Data Upcoming Odds Proxy',
    '',
    'Free delayed market proxy. Not live odds and not real-money ready.',
    '',
    f"Raw rows: {summary['raw_rows']}",
    f"Proxy price rows: {summary['proxy_price_rows']}",
    f"Sources attempted: {summary['sources_attempted']}",
    f"Errors: {summary['errors']}",
    '',
]

if len(prices):
    for _, item in prices.head(30).iterrows():
        markdown.append(
            f"- {item['match_date']} {item['match_time']} | {item['home_team']} vs {item['away_team']} | "
            f"{item['source_name']} | {item['market_home_odds']}/{item['market_draw_odds']}/{item['market_away_odds']}"
        )
else:
    markdown.append('No usable proxy odds rows were available from Football-Data fixtures source.')

if errors:
    markdown.extend(['', '## Errors', ''])
    for error in errors:
        markdown.append(f"- {error['url']}: {error['error']}")

(output_dir / 'football_data_upcoming_odds.md').write_text('\n'.join(markdown), encoding='utf-8')
print(summary)
