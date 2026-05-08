import hashlib
import json
import pathlib
import re
from datetime import datetime, timezone

DEBUG_DIR = pathlib.Path('output/debug_text')
DEBUG_DIR.mkdir(parents=True, exist_ok=True)

PDF_EXTS = {'.pdf'}
TEXT_EXTS = {'.txt', '.md', '.json'}


def utc_now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def file_id(path: pathlib.Path) -> str:
    raw = f'{path.name}|{path.stat().st_size}|{int(path.stat().st_mtime)}'
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()[:16]


def normalize_lines(text: str):
    lines = []
    for line in str(text).splitlines():
        x = re.sub(r'\s+', ' ', line).strip()
        if x:
            lines.append(x)
    return lines


def layout_hash(lines):
    markers = []
    for line in lines[:80]:
        if re.search(r'[A-Za-zÆØÅæøå]', line) or re.search(r'\b1\s+X\s+2\b', line, re.I):
            markers.append(line[:80])
        if len(markers) >= 12:
            break
    joined = '|'.join(markers)
    return hashlib.sha256(joined.encode('utf-8')).hexdigest()[:16]


def save_debug_text(method, fid, text):
    path = DEBUG_DIR / f'{method}_{fid}.txt'
    path.write_text(text or '', encoding='utf-8')
    return str(path)


def extract_pypdf(path):
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    parts = []
    for page in reader.pages:
        parts.append(page.extract_text() or '')
    return '\n'.join(parts)


def extract_pymupdf(path):
    import fitz
    doc = fitz.open(str(path))
    parts = []
    block_rows = []
    for page_idx, page in enumerate(doc):
        # Text stream
        parts.append(page.get_text('text') or '')
        # Coordinate-aware debug blocks
        for b in page.get_text('blocks') or []:
            if len(b) >= 5:
                x0, y0, x1, y1, txt = b[:5]
                txt = re.sub(r'\s+', ' ', str(txt)).strip()
                if txt:
                    block_rows.append({'page': page_idx + 1, 'x0': round(x0, 2), 'y0': round(y0, 2), 'x1': round(x1, 2), 'y1': round(y1, 2), 'text': txt})
    return '\n'.join(parts), block_rows


def read_text(path):
    raw = path.read_text(encoding='utf-8', errors='replace')
    if path.suffix.lower() == '.json':
        try:
            obj = json.loads(raw)
            if isinstance(obj, dict):
                return str(obj.get('text') or obj.get('content') or obj.get('ocr_text') or raw)
        except Exception:
            pass
    return raw


def extract_file(path):
    path = pathlib.Path(path)
    fid = file_id(path)
    suffix = path.suffix.lower()
    warnings = []
    method = None
    text = ''
    block_rows = []
    fallback_used = False

    if suffix in TEXT_EXTS:
        text = read_text(path)
        method = 'plain_text'
    elif suffix in PDF_EXTS:
        pypdf_text = ''
        try:
            pypdf_text = extract_pypdf(path)
            save_debug_text('pypdf', fid, pypdf_text)
        except Exception as exc:
            warnings.append(f'pypdf_failed: {str(exc)[:200]}')

        if len(normalize_lines(pypdf_text)) >= 8:
            text = pypdf_text
            method = 'pypdf'
        else:
            fallback_used = True
            try:
                text, block_rows = extract_pymupdf(path)
                method = 'pymupdf'
                save_debug_text('pymupdf', fid, text)
                (DEBUG_DIR / f'pymupdf_blocks_{fid}.json').write_text(json.dumps(block_rows, ensure_ascii=False, indent=2), encoding='utf-8')
            except Exception as exc:
                warnings.append(f'pymupdf_failed: {str(exc)[:200]}')
                text = pypdf_text
                method = 'pypdf_failed_low_text'
    else:
        warnings.append(f'unsupported_extension: {suffix}')
        method = 'unsupported'

    lines = normalize_lines(text)
    has_text_layer = len(lines) >= 8
    if not has_text_layer:
        warnings.append('low_text_layer_or_empty_text')

    lh = layout_hash(lines)
    debug_path = save_debug_text(method or 'unknown', fid, text)
    extraction_confidence = 0.95 if has_text_layer and method in {'pypdf', 'pymupdf', 'plain_text'} else 0.35
    if fallback_used and method == 'pymupdf':
        extraction_confidence = 0.90

    return {
        'file_id': fid,
        'source_file': str(path),
        'extracted_at': utc_now(),
        'text': text,
        'lines': lines,
        'text_extraction': {
            'method': method,
            'has_text_layer': has_text_layer,
            'text_length': len(text or ''),
            'line_count': len(lines),
            'layout_hash': lh,
            'layout_version': 'unknown',
            'extraction_confidence': extraction_confidence,
            'fallback_used': fallback_used,
            'raw_text_debug_path': debug_path,
            'warnings': warnings,
        }
    }
