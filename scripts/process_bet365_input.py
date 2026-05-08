import json
import os
import pathlib
from datetime import datetime, timezone

from extract_pdf import extract_file
from normalize_time import parse_capture_time
from parse_bet365_1x2 import parse_events_from_extraction
from tracker import read_tracker, append_records
from dedupe import dedupe_observations
from market_state import build_market_state, write_market_state
from report import write_latest_report
from ids import file_record_id

ROOT = pathlib.Path('.')
INBOX = ROOT / 'inbox' / 'possible_bets'
OUT_LATEST = ROOT / 'output' / 'latest'
OUT_LATEST.mkdir(parents=True, exist_ok=True)

SUPPORTED_EXTS = {'.pdf', '.txt', '.md', '.json'}
MAX_FILES = int(os.getenv('ODDS_MAX_FILES', '25'))
TIMEZONE = os.getenv('ODDS_TIMEZONE', 'Europe/Copenhagen')


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def list_input_files():
    if not INBOX.exists():
        return []
    files = [p for p in INBOX.rglob('*') if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS]
    files.sort(key=lambda p: p.name, reverse=True)
    return files[:MAX_FILES]


def write_json(path, data):
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(path).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')


def raw_file_record(extraction, capture):
    return {
        'record_type': 'raw_file_seen',
        'file_record_id': file_record_id(extraction.get('source_file'), extraction.get('file_id')),
        'file_id': extraction.get('file_id'),
        'source_file': extraction.get('source_file'),
        'capture': capture,
        'text_extraction': extraction.get('text_extraction'),
        'seen_at': utc_now()
    }


def main():
    files = list_input_files()
    generated_at = utc_now()
    parser_output = {
        'generated_at': generated_at,
        'phase': 'data_integrity_foundation_v1_1',
        'input_dir': str(INBOX),
        'files': [],
        'parser_errors': []
    }
    all_observations = []
    tracker_records_to_append = []

    for path in files:
        try:
            extraction = extract_file(path)
            capture = parse_capture_time(extraction.get('text') or '', TIMEZONE)
            file_summary = {k: v for k, v in extraction.items() if k not in {'text', 'lines'}}
            file_summary['capture'] = capture
            parser_output['files'].append(file_summary)
            tracker_records_to_append.append(raw_file_record(extraction, capture))

            observations, errors = parse_events_from_extraction(extraction, capture, TIMEZONE)
            all_observations.extend(observations)
            for err in errors:
                parser_output['parser_errors'].append(err)
        except Exception as exc:
            parser_output['parser_errors'].append({
                'record_type': 'parser_error',
                'source_file': str(path),
                'error': str(exc)[:1000],
                'seen_at': utc_now()
            })

    previous = read_tracker()
    deduped, dedupe_report = dedupe_observations(all_observations, previous)
    tracker_records_to_append.extend(deduped)
    appended = append_records(tracker_records_to_append)

    parser_output['summary'] = {
        'files_processed': len(files),
        'observations_raw': len(all_observations),
        'records_appended': appended,
        'dedupe_report': dedupe_report
    }

    # Build latest market state from previous records + the just-created deduped records.
    market_state = build_market_state(previous + tracker_records_to_append)
    write_market_state(market_state)

    write_json(OUT_LATEST / 'parser_output.json', parser_output)
    write_json(OUT_LATEST / 'observations.json', deduped)
    write_json(OUT_LATEST / 'dedupe_report.json', dedupe_report)
    report_path = write_latest_report(parser_output, deduped, dedupe_report, market_state=market_state)
    print(f'Odds 2 Data Integrity V1.1 OK | files={len(files)} observations={len(deduped)} appended={appended} markets={market_state["summary"]["markets_total"]} report={report_path}')


if __name__ == '__main__':
    main()
