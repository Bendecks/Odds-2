import json
import pathlib
from collections import Counter, defaultdict

REPORT_DIR = pathlib.Path('output/reports')
REPORT_DIR.mkdir(parents=True, exist_ok=True)
KNOWN_LAYOUTS_PATH = pathlib.Path('data/known_layouts.json')


def load_known_layout_hashes():
    if not KNOWN_LAYOUTS_PATH.exists():
        return set()
    try:
        data = json.loads(KNOWN_LAYOUTS_PATH.read_text(encoding='utf-8'))
    except Exception:
        return set()
    hashes = set()
    for layout in data.get('layouts') or []:
        for h in layout.get('layout_hashes') or []:
            hashes.add(h)
        if layout.get('layout_hash'):
            hashes.add(layout.get('layout_hash'))
    return hashes


def write_latest_report(parser_output, observations, dedupe_report, market_state=None):
    lines = [
        '# Odds 2 — Data Integrity Report', '',
        f'Generated: {parser_output.get("generated_at")}', '',
        '## Summary',
        f'- Files processed: {len(parser_output.get("files") or [])}',
        f'- Observations parsed this run: {len(observations)}',
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
    ])

    if market_state:
        summary = market_state.get('summary') or {}
        lines.extend([
            '## Latest Market State',
            f'- Markets total: {summary.get("markets_total")}',
            f'- Markets active: {summary.get("markets_active")}',
            f'- Markets with small-or-larger movement: {summary.get("markets_with_small_or_larger_movement")}',
            f'- Markets with significant movement: {summary.get("markets_with_significant_movement")}', '',
        ])
        sig = market_state.get('significant_movements') or []
        if sig:
            lines.append('### Significant movements')
            for m in sig[:20]:
                ev = m.get('event') or {}
                market = m.get('market') or {}
                ms = m.get('movement_summary') or {}
                lines.append(f'- {ev.get("home")} vs {ev.get("away")} | {market.get("line")} {market.get("selection")} | {ms.get("first_seen_odds")} → {ms.get("latest_seen_odds")} ({ms.get("movement_from_first")}, {ms.get("change_pct_from_first")})')
            lines.append('')

    known_hashes = load_known_layout_hashes()
    lines.append('## Files')
    for f in parser_output.get('files') or []:
        tx = f.get('text_extraction') or {}
        lh = tx.get('layout_hash')
        layout_status = 'known_layout' if lh in known_hashes else 'unknown_layout_warning'
        lines.extend([
            '',
            f'### {f.get("source_file")}',
            f'- Extraction method: {tx.get("method")}',
            f'- Has text layer: {tx.get("has_text_layer")}',
            f'- Line count: {tx.get("line_count")}',
            f'- Layout hash: {lh}',
            f'- Layout status: {layout_status}',
            f'- Extraction confidence: {tx.get("extraction_confidence")}',
            f'- Warnings: {tx.get("warnings")}',
        ])

    lines.extend(['', '## Parsed observations this run by event'])
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
            movement = r.get('odds_movement') or {}
            movement_text = ''
            if movement:
                movement_text = f' | movement: {movement.get("previous_odds")} → {movement.get("latest_odds")} ({movement.get("movement")}, {movement.get("change_pct")})'
            lines.append(f'  - {m.get("line")} / {m.get("selection")} @ {m.get("odds")} | {r.get("dedupe_status")} | {r.get("status")}{movement_text}')

    path = REPORT_DIR / 'latest_report.md'
    path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    return str(path)
