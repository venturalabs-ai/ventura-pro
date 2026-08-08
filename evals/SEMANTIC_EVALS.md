# Semantic coding evals

The cases in `semantic_cases.jsonl` are versioned rubrics for externally generated Ventura Pro outputs. The scorer does not call a model and does not prove coding quality by itself.

```bash
python scripts/score_semantic_outputs.py --outputs reports/model-output.jsonl
```

Publishable results must include the OpenCode/runtime version, model/provider/version, configuration, date, repository commit, exact cases and exact outputs. Handwritten fixtures are only scorer tests and must not be reported as model performance.
