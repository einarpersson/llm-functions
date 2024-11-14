#!/usr/bin/env bash
set -e

# @describe Add a new note to Anki with front and back text
# @option --front! The front text of the card
# @option --back! The back text of the card

main() {
    if apy add-single "$argc_front" "$argc_back"; then
        "Added new Anki note with front: '$argc_front' and back: '$argc_back'" >> "$LLM_OUTPUT"
    fi
}

eval "$(argc --argc-eval "$0" "$@")"
