from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

raw_dir = Path('data/raw/football_data_upcoming')
output_dir = Path('output/latest')
raw_dir.mkdir(parents=True, exist_ok=True)
output_dir.mkdir(parents=True, exist_ok=True)

SOURCE_URLS = ['https://www.football-data.co.uk/fixtures.csv']

price_columns = [
    'fixture_id', 'match_date', 'match_time', 'home_team', 'away_team', 'league',
    'source_name', 'source_type', 'market_home_odds', 'market_draw_odds',
    'market_away_odds', 'price_captured_at_utc', 'source_quality', 'raw_source_url'
]
fixture_columns = [
    'fixture_id', 'league', 'league_id', 'season', 'match_date', 'match_time',
    'home_team', 'away_team', 'source', 'fetched_at_utc'
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
fixture_rows = []
errors = []
fetched_at = datetime.now(timezone.utc).isoformat()
today = datetime.now(timezone.utc).date()
raw_frames = []


def parse_date(value):
    parsed = pd.to_datetime(value, errors='coerce', dayfirst=True)
    if pd.isna(parsed):
        parsed = pd.to_datetime(value, errors='coerce')
    return parsed


for url in SOURCE_URLS:
    try:
        df = pd.read_csv(url)
        df['raw_source_url'] = url
        raw_frames.append(df)
    except Exception as exc:
        errors.append({'url': url, 'error': repr(exc)})

raw = pd.concat(raw_frames, ignore_index=True) if raw_frames else pd.DataFrame()
raw.to_csv(raw_dir / 'football_data_upcoming_raw.csv', index=False)

if len(raw):
    for _, row in raw.iterrows():
        home = row.get('HomeTeam') or row.get('Home') or row.get('Home Team')
        away = row.get('AwayTeam') or row.get('Away') or row.get('Away Team')
        date = row.get('Date') or row.get('MatchDate') or row.get('DateTime')
        time = row.get('Time') or row.get('KO') or ''
        div = row.get('Div') or row.get('League') or 'unknown'
        parsed_date = parse_date(date)
        if pd.isna(parsed_date) or parsed_date.date() < today:
            continue

        league = league_map.get(str(div), str(div))
        fixture_id = f"fd_{div}_{parsed_date.date().isoformat()}_{home}_{away}".replace(' ', '_').replace('/', '-')

        fixture_rows.append({
            'fixture_id': fixture_id,
            'league': league,
            'league_id': str(div),
            'season': 'upcoming',
            'match_date': parsed_date.date().isoformat(),
            'match_time': time,
            'home_team': home,
            'away_team': away,
            'source': 'football_data_fixtures_proxy',
            'fetched_at_utc': fetched_at,
        })

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

            rows.append({
                'fixture_id': fixture_id,
                'match_date': parsed_date.date().isoformat(),
                'match_time': time,
                'home_team': home,
                'away_team': away,
                'league': league,
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
for col in price_columns:
    if col not in prices.columns:
        prices[col] = None
prices = prices[price_columns]
prices.to_csv(raw_dir / 'football_data_upcoming_odds.csv', index=False)
prices.to_csv(output_dir / 'football_data_upcoming_odds.csv', index=False)

fixtures = pd.DataFrame(fixture_rows).drop_duplicates(['fixture_id']) if fixture_rows else pd.DataFrame(columns=fixture_columns)
for col in fixture_columns:
    if col not in fixtures.columns:
        fixtures[col] = None
fixtures = fixtures[fixture_columns]
fixtures.to_csv(raw_dir / 'football_data_upcoming_fixtures.csv', index=False)
fixtures.to_csv(output_dir / 'football_data_upcoming_fixtures.csv', index=False)

summary = {
    'raw_rows': int(len(raw)),
    'upcoming_fixture_rows': int(len(fixtures)),
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
    f"Upcoming fixture rows: {summary['upcoming_fixture_rows']}",
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

fixture_markdown = [
    '# Football-Data Upcoming Fixtures',
    '',
    'Fixtures derived from Football-Data fixtures.csv. Used for automatic proxy forward modeling.',
    '',
    f"Upcoming fixture rows: {len(fixtures)}",
    '',
]
if len(fixtures):
    for _, item in fixtures.head(50).iterrows():
        fixture_markdown.append(f"- {item['match_date']} {item['match_time']} | {item['home_team']} vs {item['away_team']} | {item['league']}")
else:
    fixture_markdown.append('No upcoming Football-Data fixture rows available.')
(output_dir / 'football_data_upcoming_fixtures.md').write_text('\n'.join(fixture_markdown), encoding='utf-8')

print(summary)
