import json
import pathlib
from collections import Counter, defaultdict

REPORT_DIR = pathlib.Path('output/reports')
REPORT_DIR.mkdir(parents=True, exist_ok=True)


def write_latest_report(parser_output, observations, dedupe_report):
    lines = [
        '# Odds 2 — Data Integrity Report', '',
        f'Generated: {parser_output.get("generated_at")}', '',
        '## Summary',
        f'- Files processed: {len(parser_output.get("files") or [])}',
        f'- Observations parsed: {len(observations)}',
        f'- Dedupe report: `{json.dumps(dedupe_report, ensure_ascii=False)}`', '',
    ]

    status_counts = Counter(o.get('status') for o in observations)
    dedupe_counts = Counter(o.get('dedupe_status') for o in observations)
    confidence_counts = Counter(((o.get('parser_confidence') or {}).get('status')) for o in observations)

    lines.extend([
        '## Counts',
        f'- Status: `{dict(status_counts)}`',
        f'- Dedupe: `{dict(dedupe_counts)}`',
        f'- Parser confidence: `{dict(confidence_counts)}`', '',
        '## Files',
    ])
    for f in parser_output.get('files') or []:
        tx = f.get('text_extraction') or {}
        lines.extend([
            '',
            f'### {f.get("source_file")}',
            f'- Extraction method: {tx.get("method")}',
            f'- Has text layer: {tx.get("has_text_layer")}',
            f'- Line count: {tx.get("line_count")}',
            f'- Layout hash: {tx.get("layout_hash")}',
            f'- Extraction confidence: {tx.get("extraction_confidence")}',
            f'- Warnings: {tx.get("warnings")}',
        ])

    lines.extend(['', '## Parsed observations by event'])
    grouped = defaultdict(list)
    for o in observations:
        ev = o.get('event') or {}
        key = f'{ev.get("home")} vs {ev.get("away")} | {((o.get("event_time") or {}).get("raw_display"))}'
        grouped[key].append(o)
    if not grouped:
        lines.append('No observations parsed.')
    for key, rows in grouped.items():
        first = rows[0]
        conf = first.get('parser_confidence') or {}
        lines.extend(['', f'### {key}', f'- Event UTC: {(first.get("event_time") or {}).get("utc")}', f'- Parser confidence: {conf.get("total")} ({conf.get("status")})', f'- Dedupe statuses: `{dict(Counter(r.get("dedupe_status") for r in rows))}`'])
        for r in rows:
            m = r.get('market') or {}
            lines.append(f'  - {m.get("line")} / {m.get("selection")} @ {m.get("odds")} | {r.get("dedupe_status")} | {r.get("status")}')

    path = REPORT_DIR / 'latest_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)
