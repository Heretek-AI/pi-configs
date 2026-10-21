#!/usr/bin/env bash
# Launch script for Android Kotlin / Jetpack Compose Mobile Specialist (android-mobile-spec)
set -e

echo "=== Initializing Specialist: Android Kotlin / Jetpack Compose Mobile Specialist [android-mobile-spec] ==="
export PI_SKIP_VERSION_CHECK=1
export PI_SPECIALIST_SLUG="android-mobile-spec"
export PI_CONFIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

pi --config "$PI_CONFIG_DIR/.pi/settings.json" --agents-file "$PI_CONFIG_DIR/AGENTS.md" "$@"
