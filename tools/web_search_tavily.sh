#!/usr/bin/env bash
set -e

# @describe Perform a web search using Tavily API to get up-to-date information or additional context.
# Use this when you need current information or feel a search could provide a better answer.

# @option --query! The query to search for.
# @flag --include-results Include an array of search results in the output, including urls, titles and brief content.

# @env TAVILY_API_KEY! The api key
# @env LLM_OUTPUT=/dev/stdout The output path The output path

main() {
    local jq_filter='{answer}'
    if [[ "$argc_include_results" == "1" ]]; then
        jq_filter='{answer, results}'
    fi

    curl -fsSL -X POST https://api.tavily.com/search \
        -H "content-type: application/json" \
        -d '
{
    "api_key": "'"$TAVILY_API_KEY"'",
    "query": "'"$argc_query"'",
    "include_answer": true
}' | \
    jq "$jq_filter" >> "$LLM_OUTPUT"
}

eval "$(argc --argc-eval "$0" "$@")"
