---
name: data-pipeline-eng/duckdb-dbt-pipeline-execution
description: Specialized capabilities and operational workflow for Data Pipeline, dbt & Batch/Stream ETL Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: data-pipeline-eng/duckdb-dbt-pipeline-execution

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `data-pipeline-eng` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   dbt run
   ```
2. Execute core operations adhering to dbt project models (`dbt/models/**`), SQL transformations, schema tests (`schema.yml`), Parquet ingestion scripts, and ETL lineage graphs..
3. Run self-correction verification:
   ```bash
   Executes `dbt test` and verifies 100% of freshness checks, primary key uniqueness, and foreign key referential integrity constraints pass without warnings.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with data-pipeline-eng boundaries.
- Exit code 0 required on all diagnostic commands.
