# Ventura Pro — Evaluation Policy

## Blocking offline eval

`python scripts/run_evals.py`

The current gate validates agent/rule presence, required engineering sections and unsupported absolute claims. It is reproducible and provider-independent.

## Semantic engineering evals

Before publishing quantitative claims, evaluations must use fixed repositories/tasks and record:

- dataset/case version;
- model/provider/version;
- tool permissions;
- temperature/seed where supported;
- build/test commands;
- pass/fail criteria;
- security findings;
- token/cost measurements.

Recommended task groups: seeded bug fixes, code review, API implementation, refactoring, performance, test generation, security remediation and regression.

A green offline contract gate does not by itself establish production-grade code-generation quality.
