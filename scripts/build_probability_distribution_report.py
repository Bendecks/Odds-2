from pathlib import Path

import pandas as pd

predictions_path = Path('output/latest/poisson_predictions.parquet')
output_dir = Path('output/latest')

markdown = [
    '# Probability Distribution Report',
    '',
]

if not predictions_path.exists():
    markdown.append('No predictions available.')
else:
    df = pd.read_parquet(predictions_path)

    probs = pd.concat([
        df['home_win_probability'],
        df['draw_probability'],
        df['away_win_probability'],
    ], ignore_index=True)

    probs = pd.to_numeric(probs, errors='coerce').dropna()

    summary = {
        'count': int(len(probs)),
        'mean_probability': round(float(probs.mean()), 4),
        'max_probability': round(float(probs.max()), 4),
        'min_probability': round(float(probs.min()), 4),
        'std_probability': round(float(probs.std()), 4),
    }

    markdown.extend([
        f"Count: {summary['count']}",
        f"Mean probability: {summary['mean_probability']}",
        f"Max probability: {summary['max_probability']}",
        f"Min probability: {summary['min_probability']}",
        f"Std probability: {summary['std_probability']}",
    ])

    if summary['max_probability'] > 0.75:
        markdown.append('WARNING: Model still produces highly confident outcomes.')
    else:
        markdown.append('Probability distribution is within conservative guardrails.')

    pd.DataFrame([summary]).to_csv(
        output_dir / 'probability_distribution_report.csv',
        index=False,
    )

(output_dir / 'probability_distribution_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
