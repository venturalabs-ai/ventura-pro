---
name: rule-router
description: Select the minimum Ventura Pro rule files relevant to a concrete engineering task. Use when deciding whether microservices mlops performance or pyspark guidance should be loaded. Do not use when the task is installing the agent or editing rule content.
---

# Rule router

- Read the task and identify the actual engineering domain before loading rules.
- Load `microservices.md` only for service boundaries events APIs resilience or distributed-system design.
- Load `mlops.md` only for experiment tracking model lifecycle serving or ML operations.
- Load `performance.md` only for measured performance diagnosis profiling or optimization.
- Load `pyspark.md` only for Spark or distributed data-processing work.
- Combine rule files only when the task genuinely crosses domains.
- Avoid loading unrelated rules merely because they contain general engineering advice.
