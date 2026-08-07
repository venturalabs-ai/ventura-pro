# Regras de MLOps

- Todo experimento deve ser logado no MLflow (params, metrics, artifacts, model).
- Usar Model Registry com stages (None → Staging → Production).
- Packaging preferido: BentoML.
- Serving: BentoML / KServe / TorchServe / Vertex AI / Azure ML.
- Deploy sempre com estratégia segura (Shadow → Canary → Blue/Green).
- Versionar juntos: código + dados + modelo.
- Implementar monitoramento de data drift e concept drift.
- Separar ambiente de treino e de serving.
- Feature Store quando houver múltiplos modelos compartilhando features.
- Reproducibility: seed + environment lock.
- Alinhamento cloud: Google → Vertex AI + MLflow; Microsoft → Azure ML + MLflow; IBM → watsonx + MLflow; SAP → SAP AI Core + generative AI Hub.
