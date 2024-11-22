#!/usr/bin/env bash
set -e

# @describe List all available Anki tags

main() {
    if apy tag; then
        echo "Listed all Anki tags" >> "$LLM_OUTPUT"
    fi
}

eval "$(argc --argc-eval "$0" "$@")"