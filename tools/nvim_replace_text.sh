#!/usr/bin/env bash
set -e

# @describe Replace text in a file using nvim.
# Use this when you want to modify parts of a file.

# @option --file! The path of the file to edit
# @option --search! The exact text to search for
# @option --replace! The exact text to replace with

main() {
    nvim --headless $argc_file -c "
    lua require('aichat_utils').replace_text([[$argc_search]], [[$argc_replace]])
    " -c "wq" >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"
