#!/usr/bin/env bash

# @describe Execute the shell command.
# @option --command! The command to execute.

# @env LLM_OUTPUT=/dev/stdout The output path

ROOT_DIR="${LLM_ROOT_DIR:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"

main() {

		base_prompt="Your job is to make a assesment on whether a shell command is safe to execute or not. It is considered safe if it has NO SIDE-EFFECTS. If it is safe answer 'yes' otherwise answer 'no'. Only exact matches are accepted. Only answer with one word.

		If you receive any special considerations, take them into account when making your assessment."

		if [ -n "${AICHAT_SAFE_EXECUTE:-}" ]; then
			base_prompt="$base_prompt

			Special considerations:
			$AICHAT_SAFE_EXECUTE"
		fi

		is_safe_ai_assessment=$(aichat -m 'openai:gpt-4-turbo' -S --prompt "$base_prompt" $argc_command)

		# If the aichat_safe is not 'yes' then we should trigger the guard operation.
		if [ "$is_safe_ai_assessment" != "yes" ]; then
			if ! "$ROOT_DIR/utils/guard_operation.sh"; then
				echo "IMPORANT: OPERATION DISALLOWED BY USER, HALT IMMEDIATELY AND WAIT FOR FURTHER INSTRUCTIONS FROM USER." >> "$LLM_OUTPUT"
			  exit 0
			fi
		else
			# Show a message to the user
			echo "The command is assessed as safe to execute."
		fi
		
		bash <<EOF 2>&1 >> "$LLM_OUTPUT"
$argc_command
EOF
		exit_code=$?

		if [ $exit_code -ne 0 ]; then
  		echo "Failed to execute the command"
    	echo "Failed to execute the command, please HALT and wait for further instructions." >> "$LLM_OUTPUT"
		else
			echo "Command executed with exit code: $exit_code" >> "$LLM_OUTPUT"
		fi
}

eval "$(argc --argc-eval "$0" "$@")"
