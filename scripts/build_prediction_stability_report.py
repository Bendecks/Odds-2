from pathlib import Path

import pandas as pd

predictions_dir = Path('data/predictions')
output_dir = Path('output/latest')

parquet_files = sorted(predictions_dir.glob('*.parquet'))
jsonl_files = sorted(predictions_dir.glob('*.jsonl'))

markdown = [
    '# Prediction Stability Report',
    '',
]

frames = []

for file in parquet_files:
    try:
        df = pd.read_parquet(file)

        if 'prediction_id' in df.columns:
            frames.append(df)

    except Exception:
        continue

for file in jsonl_files:
    try:
        df = pd.read_json(file, lines=True)

        if 'prediction_id' in df.columns:
            frames.append(df)

    except Exception:
        continue

if frames:
    merged = pd.concat(frames, ignore_index=True)

    for col in ['ev', 'probability']:
        if col not in merged.columns:
            merged[col] = 0.0

    merged['ev'] = pd.to_numeric(merged['ev'], errors='coerce')
    merged['probability'] = pd.to_numeric(merged['probability'], errors='coerce')

    stability = (
        merged.groupby('prediction_id')
        .agg(
            snapshots=('prediction_id', 'size'),
            avg_ev=('ev', 'mean'),
            ev_std=('ev', 'std'),
            avg_probability=('probability', 'mean'),
            probability_std=('probability', 'std'),
        )
        .reset_index()
    )

    stability['ev_std'] = stability['ev_std'].fillna(0)
    stability['probability_std'] = stability['probability_std'].fillna(0)

    stable = stability[
        (stability['ev_std'] < 0.05)
        & (stability['probability_std'] < 0.04)
    ]

    unstable = stability[
        (stability['ev_std'] >= 0.05)
        | (stability['probability_std'] >= 0.04)
    ]

    stability.to_csv(output_dir / 'prediction_stability_report.csv', index=False)

    markdown.extend([
        f'Total tracked predictions: {len(stability)}',
        f'Stable predictions: {len(stable)}',
        f'Unstable predictions: {len(unstable)}',
        '',
    ])

    if len(unstable):
        markdown.append('## Most unstable predictions')
        markdown.append('')

        for _, row in unstable.sort_values('ev_std', ascending=False).head(10).iterrows():
            markdown.append(
                f"- {row['prediction_id']} | ev_std={row['ev_std']:.4f} | prob_std={row['probability_std']:.4f}"
            )
else:
    markdown.append('No prediction history available yet.')

(output_dir / 'prediction_stability_report.md').write_text('\n'.join(markdown), encoding='utf-8')

print(markdown)
