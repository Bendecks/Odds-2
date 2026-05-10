import json
import os
import urllib.request
from pathlib import Path

output_dir = Path('output/latest')

api_key = os.getenv('GEMINI_API_KEY')
model = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash')

source_files = [
    output_dir / 'project_status_report.md',
    output_dir / 'operational_decision_report.md',
    output_dir / 'human_action_report.md',
    output_dir / 'market_alignment_report.md',
    output_dir / 'daily_betting_card.md',
]

context_parts = []

for path in source_files:
    if path.exists():
        context_parts.append(f'## {path.name}\n{path.read_text(encoding="utf-8")[:4000]}')

context = '\n\n'.join(context_parts)

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

Important constraints:
- Do not recommend real-money betting unless evidence is strong.
- Focus on model quality, CLV, calibration, market alignment, sample size and operational risks.
- Be concise and practical.
- Return Markdown.

Review this project state and produce:
1. Current system status
2. Biggest weakness
3. Best next development step
4. Whether this is observe-only, paper-test ready, or experimental-ready
5. One concrete change to prioritize next

Project state:
{context}
"""

payload = {
    'contents': [
        {
            'parts': [
                {'text': prompt}
            ]
        }
    ]
}

url = f'https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}'

try:
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={'Content-Type': 'application/json'},
        method='POST',
    )

    with urllib.request.urlopen(req, timeout=30) as response:
        data = json.loads(response.read().decode('utf-8'))

    text = data['candidates'][0]['content']['parts'][0]['text']

    (output_dir / 'gemini_ai_review.md').write_text(text, encoding='utf-8')

    print('Gemini AI review generated.')

except Exception as exc:
    fallback.append(f'Reason: Gemini request failed: {repr(exc)}')
    (output_dir / 'gemini_ai_review.md').write_text('\n'.join(fallback), encoding='utf-8')
    print(f'Gemini review failed: {exc}')
    raise SystemExit(0)
