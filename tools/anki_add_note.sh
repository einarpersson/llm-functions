#!/usr/bin/env bash
set -e

# @describe Add a new note to Anki with front and back text
# @option --front! The front text of the card
# @option --back! The back text of the card
# @option --tag Tags to add to the card (separate multiple tags with spaces, e.g. "tag1 tag2 tag3")

main() {
    # Add the note to Anki
    apy add-single ${argc_tag:+-t "$argc_tag"} "$argc_front" "$argc_back"
    
    # If we get here, the command succeeded (due to set -e)
    echo "Added new Anki note with front: '$argc_front' and back: '$argc_back'${argc_tag:+ and tag: '$argc_tag'}" >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"
