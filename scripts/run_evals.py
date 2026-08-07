from pathlib import Path

TARGET = Path('.opencode/agent/ventura-pro.md')
REQUIRED = [
    '# Ventura Pro',
    '## Domínios de Excelência',
    '## Princípios Obrigatórios',
    '## Processo de Trabalho',
    '## Qualidade, Segurança e Confiabilidade',
    '## Restrições',
]
FORBIDDEN = [
    'certificado por google',
    'certificado pela microsoft',
    '100% seguro',
    'zero vulnerabilidades',
]

failures = []
if not TARGET.exists():
    failures.append(f'missing {TARGET}')
else:
    text = TARGET.read_text(encoding='utf-8')
    if len(text) < 3000:
        failures.append('agent definition unexpectedly short')
    for section in REQUIRED:
        if section not in text:
            failures.append(f'missing required section: {section}')
    lowered = text.lower()
    for claim in FORBIDDEN:
        if claim in lowered:
            failures.append(f'unsupported absolute claim: {claim}')
    for rules_file in [
        '.opencode/rules/microservices.md',
        '.opencode/rules/mlops.md',
        '.opencode/rules/performance.md',
        '.opencode/rules/pyspark.md',
    ]:
        if not Path(rules_file).exists():
            failures.append(f'missing rule file: {rules_file}')

if failures:
    print('AGENT EVALS: FAIL')
    for failure in failures:
        print(f'- {failure}')
    raise SystemExit(1)

print('AGENT EVALS: PASS (contract/schema baseline)')
