---
name: analytics-metrics-eng/clickhouse-schema-and-aggregation-optimization
description: Specialized capabilities and operational workflow for Product Telemetry, ClickHouse & Real-time Metrics Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: analytics-metrics-eng/clickhouse-schema-and-aggregation-optimization

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `analytics-metrics-eng` in the Data, Machine Learning & Code Hygiene Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   clickhouse-client --query 'EXPLAIN ...'
   ```
2. Execute core operations adhering to ClickHouse DDL schemas (`clickhouse/migrations/**`), Materialized View definitions, telemetry event JSON schemas (`events/*.json`), and analytical query benchmarks..
3. Run self-correction verification:
   ```bash
   Runs `clickhouse-client` query validation against schemas; verifies that partition keys prevent massive part churn and materialized views maintain deterministic aggregations.
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with analytics-metrics-eng boundaries.
- Exit code 0 required on all diagnostic commands.
