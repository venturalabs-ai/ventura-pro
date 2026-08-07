# Regras de PySpark

- DataFrames sempre (nunca RDDs em código novo).
- AQE obrigatório:
  - spark.sql.adaptive.enabled = true
  - spark.sql.adaptive.skewJoin.enabled = true
  - spark.sql.adaptive.coalescePartitions.enabled = true
- Preferir Delta Lake + Liquid Clustering (ou Iceberg + Parquet).
- Proibir Python UDFs (usar funções nativas ou Pandas UDF/Arrow).
- Schema explícito em todos os reads.
- Medallion Architecture (Bronze → Silver → Gold).
- Broadcast joins para tabelas pequenas.
- Evitar small files (OPTIMIZE + auto-compaction).
- Usar Kryo serializer.
- spark.sql.shuffle.partitions = auto (ou valor calculado).
- spark.sql.execution.arrow.pyspark.enabled = true.
- Predicate pushdown + partition pruning; MERGE (upsert) com Delta Lake.
- Orquestração: Prefect, Dagster, Airflow, Databricks Jobs.
- Qualidade de dados: Great Expectations, dbt tests.
