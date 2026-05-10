import json
import os
import urllib.error
import urllib.request
from pathlib import Path

output_dir = Path('output/latest')
output_dir.mkdir(parents=True, exist_ok=True)

api_key = os.getenv('GEMINI_API_KEY')
model = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')

source_files = [
    output_dir / 'project_status_report.md',
    output_dir / 'operational_decision_report.md',
    output_dir / 'human_action_report.md',
    output_dir / 'market_alignment_report.md',
    output_dir / 'probability_calibration_layer.md',
    output_dir / 'probability_calibration_rules.csv',
    output_dir / 'clv_trend_report.md',
    output_dir / 'clv_band_report.md',
    output_dir / 'signal_suppression_rules.md',
    output_dir / 'rule_action_summary.md',
    output_dir / 'phase_performance_report.md',
    output_dir / 'calibration_action_plan.md',
    output_dir / 'daily_betting_card.md',
]

context_parts = []

for path in source_files:
    if path.exists():
        context_parts.append(f'## {path.name}\n{path.read_text(encoding="utf-8")[:4000]}')

context = '\n\n'.join(context_parts) or 'No project status context available.'

fallback = [
    '# Gemini AI Review',
    '',
    'Gemini review was not generated.',
    '',
]

if not api_key:
    fallback.append('Reason: GEMINI_API_KEY is not available in this environment.')
    (output_dir / 'gemini_ai_review.md').write_text('\n'.join(fallback), encoding='utf-8')
    print('No GEMINI_API_KEY available; wrote fallback report.')
    raise SystemExit(0)

prompt = f"""
You are reviewing an automated football betting research system.

Rules:
- Do not recommend real-money betting.
- Treat historical proxy research, paper forward-testing and real-money readiness as separate states.
- Focus on model quality, CLV, calibration, market alignment, sample size, signal suppression and operational risks.
- Be concise and practical.
- Return Markdown only.

Produce:
1. Current system status
2. Biggest weakness
3. Best next development step
4. Readiness: observe-only, paper-test-ready, or experimental-ready
5. One concrete change to prioritize next
6. Whether the current suppression rules look too strict, too loose, or reasonable
7. Whether the probability calibration layer looks too aggressive, too weak, or reasonable
8. Which probability band should be protected, suppressed, or monitored next

Project state:
{context}
"""

payload = {
    'contents': [
        {
            'role': 'user',
            'parts': [
                {'text': prompt}
            ],
        }
    ],
    'generationConfig': {
        'temperature': 0.2,
        'maxOutputTokens': 1100,
    },
}

candidate_models = [
    model,
    'gemini-1.5-flash',
    'gemini-2.0-flash',
]

seen = set()
errors = []

for candidate_model in candidate_models:
    if candidate_model in seen:
        continue
    seen.add(candidate_model)

    url = f'https://generativelanguage.googleapis.com/v1beta/models/{candidate_model}:generateContent?key={api_key}'

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'},
            method='POST',
        )

        with urllib.request.urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode('utf-8'))

        text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text')

        if not text:
            errors.append(f'{candidate_model}: empty response')
            continue

        final_text = f'# Gemini AI Review\n\nModel used: `{candidate_model}`\n\n{text.strip()}\n'
        (output_dir / 'gemini_ai_review.md').write_text(final_text, encoding='utf-8')
        print(f'Gemini AI review generated with {candidate_model}.')
        raise SystemExit(0)

    except urllib.error.HTTPError as exc:
        try:
            body = exc.read().decode('utf-8')[:1000]
        except Exception:
            body = ''
        errors.append(f'{candidate_model}: HTTP {exc.code} {body}')
    except Exception as exc:
        errors.append(f'{candidate_model}: {repr(exc)}')

fallback.append('Reason: Gemini request failed or returned no usable text.')
fallback.append('')
fallback.append('Errors:')
for error in errors:
    fallback.append(f'- {error}')

(output_dir / 'gemini_ai_review.md').write_text('\n'.join(fallback), encoding='utf-8')
print('Gemini review failed; wrote fallback report.')
raise SystemExit(0)
