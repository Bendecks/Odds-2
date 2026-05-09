import base64
import hashlib
import json
import os
import pathlib
from datetime import datetime, timezone

import requests

ROOT = pathlib.Path('.')
INBOX = ROOT / 'inbox' / 'possible_bets'
OUT_LATEST = ROOT / 'output' / 'latest'
OUT_DEBUG = ROOT / 'output' / 'debug_text'
OUT_LATEST.mkdir(parents=True, exist_ok=True)
OUT_DEBUG.mkdir(parents=True, exist_ok=True)

GEMINI_MODEL = os.getenv('GEMINI_PDF_MODEL', os.getenv('GEMINI_MODEL', 'gemini-2.5-flash'))
TIMEZONE = os.getenv('ODDS_TIMEZONE', 'Europe/Copenhagen')
MAX_FILES = int(os.getenv('ODDS_MAX_FILES', '10'))
SUPPORTED_EXTS = {'.pdf'}


def now_utc():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def file_id(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def list_pdfs():
    if not INBOX.exists():
        return []
    files = [p for p in INBOX.rglob('*') if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS]
    files.sort(key=lambda p: p.name, reverse=True)
    return files[:MAX_FILES]


def gemini_url():
    key = os.getenv('GEMINI_API_KEY')
    if not key:
        return None
    return f'https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={key}'


def prompt(source_file):
    return f'''You are reading a bet365 PDF/screenshot export visually.
Extract ONLY football 1X2 match odds visible in the PDF.

Return JSON only with this schema:
{{
  "source_file": "{source_file}",
  "timezone_assumed": "{TIMEZONE}",
  "matches": [
    {{
      "home_team": "string",
      "away_team": "string",
      "league": "string or unknown",
      "date_display": "string exactly as shown, or empty",
      "time_display": "HH:MM as shown/normalized",
      "odds_1": 0.0,
      "odds_x": 0.0,
      "odds_2": 0.0,
      "confidence": "low|medium|high",
      "notes": "short, mention if inferred"
    }}
  ],
  "parser_warnings": []
}}

Rules:
- 1 = home win, X = draw, 2 = away win.
- Do not guess odds if the table is unclear.
- If a row is not clearly a 1X2 football market, exclude it.
- If time text has extra digits like 14:006, normalize to 14:00 and add a warning.
- Use the date headers shown in the PDF when available.
- Keep team names exactly as displayed except obvious whitespace cleanup.
- Do not include markdown fences. JSON only.'''


def extract_json(text):
    raw = str(text or '').strip()
    if raw.startswith('```'):
        raw = raw.strip('`').replace('json\n', '', 1).replace('JSON\n', '', 1).strip()
    try:
        return json.loads(raw)
    except Exception:
        start, end = raw.find('{'), raw.rfind('}')
        if start >= 0 and end > start:
            return json.loads(raw[start:end + 1])
        raise


def parse_pdf(path):
    url = gemini_url()
    if not url:
        return {'source_file': str(path), 'error': 'missing_gemini_api_key', 'matches': []}
    pdf_bytes = path.read_bytes()
    body = {
        'contents': [{
            'role': 'user',
            'parts': [
                {'text': prompt(str(path))},
                {'inline_data': {'mime_type': 'application/pdf', 'data': base64.b64encode(pdf_bytes).decode('ascii')}}
            ]
        }],
        'generationConfig': {
            'temperature': 0,
            'responseMimeType': 'application/json',
            'maxOutputTokens': 8192
        }
    }
    try:
        resp = requests.post(url, json=body, timeout=120)
        if resp.status_code >= 400:
            return {'source_file': str(path), 'file_id': file_id(path), 'error': f'gemini_http_{resp.status_code}', 'response_text': resp.text[:2000], 'matches': []}
        data = resp.json()
        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
        (OUT_DEBUG / f'gemini_pdf_{file_id(path)}.txt').write_text(text, encoding='utf-8')
        parsed = extract_json(text)
        parsed['source_file'] = str(path)
        parsed['file_id'] = file_id(path)
        parsed['parser_source'] = 'gemini_pdf_vision'
        return parsed
    except Exception as exc:
        return {'source_file': str(path), 'file_id': file_id(path), 'error': str(exc)[:2000], 'matches': []}


def main():
    files = list_pdfs()
    outputs = [parse_pdf(path) for path in files]
    payload = {
        'generated_at': now_utc(),
        'parser_source': 'gemini_pdf_vision',
        'model': GEMINI_MODEL,
        'files_processed': len(files),
        'files': outputs,
        'summary': {
            'matches_total': sum(len(f.get('matches') or []) for f in outputs),
            'files_with_errors': sum(1 for f in outputs if f.get('error')),
        }
    }
    (OUT_LATEST / 'gemini_parser_output.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Gemini PDF parser OK | files={len(files)} matches={payload["summary"]["matches_total"]} errors={payload["summary"]["files_with_errors"]}')


if __name__ == '__main__':
    main()
