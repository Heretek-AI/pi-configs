#!/usr/bin/env bash
# Launch script for Vector Embeddings, Hybrid Search & RAG Specialist (vector-rag-spec)
set -e

echo "=== Initializing Specialist: Vector Embeddings, Hybrid Search & RAG Specialist [vector-rag-spec] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="vector-rag-spec"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
