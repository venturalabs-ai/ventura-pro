# Ventura Pro

**Ventura Pro** é um agente **Engenheiro de Software Pleno / Staff Engineer**
especialista em Python para o [opencode](https://opencode.ai), parte do
estúdio Gerde. Ele projeta e constrói sistemas modernos de alta escala com
foco em arquitetura de microsserviços, performance extrema, pipelines de dados
massivos, MLOps e DevOps.

Conhecimento alinhado às práticas de **Google**, **Microsoft**, **IBM**,
**Oracle** e **SAP**.

## Domínios de Excelência

1. **Arquitetura de Microsserviços** — FastAPI (ASGI) + event-driven,
   DDD/Bounded Contexts, Database per Service.
2. **Performance extrema** — asyncio, uvloop, anyio, drivers async nativos,
   profiling antes de otimizar.
3. **Pipelines de dados massivos** — PySpark (DataFrames, AQE), Delta Lake,
   Medallion Architecture, dlt, Prefect/Airflow.
4. **MLOps e IA em produção** — PyTorch, Scikit-learn, MLflow, BentoML,
   Vertex AI, Azure ML, SAP AI Core.
5. **Integração de legados + cloud** — Google Cloud, Azure, IBM Cloud, Oracle
   Cloud, SAP BTP.
6. **DevOps / IaC / Containers** — Docker multi-stage, Kubernetes,
   Terraform/Pulumi com Python.
7. **CLIs robustas, testes complexos, segurança e confiabilidade.**

## Instalação

Copie o diretório `.opencode/` para a raiz do projeto opencode onde o agente
deve estar disponível:

```powershell
# a partir da raiz do seu projeto
Copy-Item -Recurse .opencode\agent\ventura-pro.md seu-projeto\.opencode\agent\
Copy-Item -Recurse .opencode\rules\* seu-projeto\.opencode\rules\
```

Em seguida, ative o agente no `opencode.json` do projeto:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "ventura-pro"
}
```

Reinicie o opencode e selecione **Ventura Pro** no seletor de agentes (Tab).

## Conteúdo

```
.
├── README.md
├── .opencode/
│   ├── agent/
│   │   └── ventura-pro.md   # definição e prompt do agente
│   └── rules/
│       ├── microservices.md # regras de microsserviços (DDD, outbox, K8s)
│       ├── mlops.md         # regras de MLOps (MLflow, Model Registry)
│       ├── performance.md   # regras de performance (async, uvloop)
│       └── pyspark.md       # regras de PySpark (AQE, Delta Lake)
```

## Princípios

- Código limpo: PEP 8 + Google Python Style Guide + Clean Code.
- Type hints rigorosos em 100% do código novo + Pydantic v2.
- Performance first: profiling antes de otimizar.
- Segurança e confiabilidade: secrets management, circuit breakers, retries
  com budget, timeouts, observability.
- Observabilidade (OpenTelemetry) desde o primeiro commit.
- Nunca hardcode secrets; testes (pytest + pytest-asyncio) e logging
  estruturado (JSON) sempre.

## Licença

[MIT](LICENSE)
