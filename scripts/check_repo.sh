#!/usr/bin/env bash
# Thin wrapper: run the repo guardrail checks from anywhere. Args pass through,
# e.g. scripts/check_repo.sh --checks a,b,c
set -euo pipefail
cd "$(dirname "$0")/.."
exec python3 scripts/check_repo.py "$@"
