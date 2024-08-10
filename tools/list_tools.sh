#!/usr/bin/env bash
set -e

# @describe List all active tools by reading from tools.txt, filtering out commented lines, and stripping file extensions.
# This tool takes no arguments.

main() {
    grep -v '^#' ~/config/aichat/functions/tools.txt | sed 's/\.[^.]*$//' >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"
