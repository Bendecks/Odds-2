from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path('output/bet365/latest')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

BASE_RAW = 'https://raw.githubusercontent.com/Bendecks/Odds-2/main/output/bet365/latest'
BASE_GITHUB = 'https://github.com/Bendecks/Odds-2/blob/main/output/bet365/latest'

files = [
    ('Multisport PDF', 'bet365_today_multisport_report.pdf', 'PDF-fil til iPhone'),
    ('Multisport HTML', 'bet365_today_multisport_report.html', 'Mobilvenlig HTML'),
    ('Multisport events CSV', 'bet365_today_multisport_events.csv', 'Events-data'),
    ('Multisport markets CSV', 'bet365_today_multisport_markets.csv', 'Alle markeder'),
    ('Multisport summary JSON', 'bet365_today_multisport_summary.json', 'Kort teknisk status'),
    ('Fodbold større ligaer PDF', 'bet365_today_major_odds_report.pdf', 'PDF kun fodbold'),
    ('Fodbold større ligaer HTML', 'bet365_today_major_odds_report.html', 'HTML kun fodbold'),
]

html_links = []
markdown_links = []
for title, filename, description in files:
    raw_url = f'{BASE_RAW}/{filename}'
    github_url = f'{BASE_GITHUB}/{filename}'
    html_links.append(
        f'<a class="card" href="{raw_url}"><strong>{title}</strong><span>{description}</span><small>{filename}</small></a>'
    )
    markdown_links.append(f'- [{title}]({raw_url}) — {description}')

now = datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'

html = f'''<!doctype html>
<html lang="da">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bet365 iPhone downloads</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 0; padding: 18px; background: #f6f6f6; color: #111; }}
    h1 {{ font-size: 28px; margin: 0 0 8px; }}
    p {{ color: #555; line-height: 1.4; }}
    .card {{ display: block; background: white; border-radius: 14px; padding: 16px; margin: 12px 0; text-decoration: none; color: #111; box-shadow: 0 1px 5px rgba(0,0,0,.08); }}
    .card strong {{ display: block; font-size: 18px; margin-bottom: 4px; }}
    .card span {{ display: block; color: #555; margin-bottom: 6px; }}
    .card small {{ color: #777; word-break: break-all; }}
  </style>
</head>
<body>
  <h1>Bet365 downloads</h1>
  <p>Tryk på en fil. PDF er lettest at gemme på iPhone. Hvis en fil ikke åbner, så brug Del → Gem i Arkiver.</p>
  <p>Opdateret: {now}</p>
  {''.join(html_links)}
</body>
</html>
'''

markdown = '# Bet365 iPhone downloads\n\n' + f'Opdateret: {now}\n\n' + '\n'.join(markdown_links) + '\n'

(OUTPUT_DIR / 'iphone_download_links.html').write_text(html, encoding='utf-8')
(OUTPUT_DIR / 'iphone_download_links.md').write_text(markdown, encoding='utf-8')

print('Wrote iPhone download links')
print(OUTPUT_DIR / 'iphone_download_links.html')
print(OUTPUT_DIR / 'iphone_download_links.md')
