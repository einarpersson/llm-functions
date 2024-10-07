#!/usr/bin/env bash
set -e

# @describe Fetch the latest news from SVT's RSS feed.

main() {
    echo "Fetching latest news from SVT RSS feed..." >> "$LLM_OUTPUT"
    
    # Fetch the RSS feed and parse it
    rss_content=$(curl -s https://www.svt.se/rss.xml | xmllint --format -)
    
    # Extract and format news items
    echo "$rss_content" | awk '
    /<item>/,/<\/item>/ {
        if (/<title>/) {
            gsub(/<\/?title>/, "")
            title = $0
        }
        if (/<link>/) {
            gsub(/<\/?link>/, "")
            link = $0
        }
        if (/<\/item>/) {
            print "Title: " title
            print "Link: " link
            print ""
        }
    }
    ' >> "$LLM_OUTPUT"
    
    echo "News items fetched successfully." >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"