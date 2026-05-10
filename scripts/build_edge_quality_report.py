from pathlib import Path

import pandas as pd

output_dir = Path('output/latest')
ev_path = output_dir / 'ev_results.parquet'

markdown = [
    '# Edge Quality Report',
    '',
]

if not ev_path.exists():
    markdown.append('No EV results available.')
else:
    df = pd.read_parquet(ev_path)

    edge_rows = []

    for market in [
        ('home_ev', 'home_win_probability'),
        ('draw_ev', 'draw_probability'),
        ('away_ev', 'away_win_probability'),
    ]:
        ev_col, prob_col = market

        if ev_col not in df.columns:
            continue

        subset = df[[ev_col, prob_col]].copy()
        subset[ev_col] = pd.to_numeric(subset[ev_col], errors='coerce')
        subset[prob_col] = pd.to_numeric(subset[prob_col], errors='coerce')

        positive = subset[subset[ev_col] > 0.05]

        edge_rows.append({
            'market': ev_col,
            'positive_edges': int(len(positive)),
            'avg_ev': round(float(positive[ev_col].mean()), 4) if len(positive) else None,
            'avg_probability': round(float(positive[prob_col].mean()), 4) if len(positive) else None,
        })

    report = pd.DataFrame(edge_rows)
    report.to_csv(output_dir / 'edge_quality_report.csv', index=False)

    markdown.append(f'Total edge groups: {len(report)}')
    markdown.append('')

    for _, row in report.iterrows():
        markdown.append(
            f"- {row['market']} | edges={row['positive_edges']} | avg_ev={row['avg_ev']} | avg_prob={row['avg_probability']}"
        )

(output_dir / 'edge_quality_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
