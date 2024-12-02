#!/usr/bin/env bash
set -e

# @describe Read the contents of a file at the specified path.
# Use this when you need to examine the contents of an existing file.

# @option --path! The path of the file to read

# @env LLM_OUTPUT=/dev/stdout The output path

main() {
    if [[ ! -f "$argc_path" ]]; then
        echo "Error: '$argc_path' is not a file or does not exist" >> "$LLM_OUTPUT"
    else
        cat "$argc_path" >> "$LLM_OUTPUT"
    fi
}

eval "$(argc --argc-eval "$0" "$@")"
