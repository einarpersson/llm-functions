#!/usr/bin/env bash
set -e

# @describe Execute the shell command.
# @option --command! The command to execute.

# @env LLM_OUTPUT=/dev/stdout The output path

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

main() {
    if ! "$ROOT_DIR/utils/guard_operation.sh"; then
        echo "IMPORANT: OPERATION DISALLOWED BY USER, HALT IMMEDIATELY AND WAIT FOR FURTHER INSTRUCTIONS FROM USER." >> "$LLM_OUTPUT"
    elif ! eval "$argc_command" >> "$LLM_OUTPUT"; then
        echo "Failed to execute the command, please HALT and wait for further instructions." >> "$LLM_OUTPUT"
    fi
}

eval "$(argc --argc-eval "$0" "$@")"
