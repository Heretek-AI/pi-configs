---
name: cache-streaming-eng/kafka-topic-and-consumer-tuning
description: Specialized capabilities and operational workflow for Distributed Cache & Event Streaming Engineer
---

<!-- Source: Extracted & refactored from Wave 1 audits for Pi Standalone Specialist Fleet -->

# Skill: cache-streaming-eng/kafka-topic-and-consumer-tuning

## Purpose
Provides concrete step-by-step guidance, automated checks, and command references for `cache-streaming-eng` in the Architecture, Cloud & Infrastructure Guild.

## Verification Protocols
1. Run pre-flight checks:
   ```bash
   redis-cli ping
   ```
2. Execute core operations adhering to Redis key schemas, TTL cache eviction policies, Kafka topic configs, consumer group offset handlers, streaming serialization schemas (Avro/Protobuf), and cache-stampede mitigation logic..
3. Run self-correction verification:
   ```bash
   Verifies Kafka topic partition counts, retention windows, and consumer group error handling via integration test suites (`npm test -- --grep 'cache|streaming'`).
   ```

## Quality Gates
- Zero warnings on static analysis.
- Full compliance with cache-streaming-eng boundaries.
- Exit code 0 required on all diagnostic commands.
