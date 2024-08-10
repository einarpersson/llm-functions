#!/usr/bin/env bash
set -e

# @describe List all tools on the system. This list is only for reference, they are not necessarily available in the current chat session. If you find a tool that you want to use, ask the user to enable it.
# This tool takes no arguments.

main() {
    grep -v '^#' ~/config/aichat/functions/tools.txt | sed 's/\.[^.]*$//' >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"
