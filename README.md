# Ventura Pro

[![License](https://img.shields.io/github/license/venturalabs-ai/ventura-pro)](LICENSE)
[![OpenCode](https://img.shields.io/badge/OpenCode-agent-4B5563)](https://opencode.ai/)

**Ventura Pro** é um agente de engenharia de software para OpenCode, com foco em Python, arquitetura de sistemas, performance, dados, MLOps, DevOps, segurança e confiabilidade.

> O projeto reúne regras e prompts de engenharia inspirados em práticas públicas e amplamente adotadas na indústria. Não possui afiliação oficial com Google, Microsoft, IBM, Oracle, SAP ou outras empresas citadas como referência técnica.

## Domínios

1. Microsserviços e arquiteturas orientadas a eventos
2. FastAPI, ASGI e programação assíncrona
3. DDD, bounded contexts e integração entre serviços
4. Pipelines de dados com PySpark e Delta Lake
5. MLOps, rastreabilidade de experimentos e serving
6. Containers, Kubernetes e IaC
7. Observabilidade com logs, métricas e traces
8. Segurança, secrets management, retries, timeouts e circuit breakers
9. Testes, profiling e engenharia de performance

## Estrutura

```text
ventura-pro/
├── README.md
├── LICENSE
└── .opencode/
    ├── agent/
    │   └── ventura-pro.md
    └── rules/
        ├── microservices.md
        ├── mlops.md
        ├── performance.md
        └── pyspark.md
```

## Instalação

Copie o agente e as regras para o projeto OpenCode em que deseja utilizá-los:

```powershell
Copy-Item -Recurse .opencode\agent\ventura-pro.md seu-projeto\.opencode\agent\
Copy-Item -Recurse .opencode\rules\* seu-projeto\.opencode\rules\
```

Configure o agente padrão no `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "ventura-pro"
}
```

## Princípios de engenharia

- type hints rigorosos em código novo;
- Pydantic v2 para contratos e validação quando aplicável;
- profiling antes de otimização;
- secrets fora do código-fonte;
- observabilidade desde o desenho inicial;
- testes automatizados para comportamento crítico;
- logging estruturado;
- timeouts, retries limitados e circuit breakers em integrações remotas;
- documentação de trade-offs arquiteturais.

## Status

Repositório de **agente e regras de engenharia**, não uma aplicação executável independente. Validação deve ser feita no ambiente OpenCode e nos projetos em que o agente for instalado.

## Licença

MIT — consulte [LICENSE](LICENSE).

## Autor

Wemerson Mota de Oliveira — Ventura Labs AI

[GitHub](https://github.com/venturalabs-ai) · [LinkedIn](https://www.linkedin.com/in/wemerson-mota-de-oliveira-81aa8226/)
