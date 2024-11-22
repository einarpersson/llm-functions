#!/usr/bin/env bash
set -e

# @describe List all available Anki tags

main() {
    apy tag >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"
