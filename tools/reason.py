import os
import re
from openai import OpenAI

def run(
    prompt: str):
    """Use DeepSeek-R1 model to generate a reasoned response.
    Args:
        prompt: The user's prompt/question to reason about
        show_thinking: Whether to show the thinking process in <think> tags
    """
    api_key = os.environ.get("KLUSTER_API_KEY")
    if not api_key:
        return "Error: KLUSTER_API_KEY environment variable not set"

    try:
        client = OpenAI(
            base_url="https://api.kluster.ai/v1",
            api_key=api_key
        )

        chat_completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )

        response = chat_completion.choices[0].message.content
        if response is None:
            return "Error: Received empty response from API"

        show_thinking = False
        
        # Remove thinking section if show_thinking is False
        if not show_thinking:
            response = re.sub(r'<think>.*?</think>\n*', '', response, flags=re.DOTALL)
        
        return response.strip()

    except Exception as e:
        return f"Error: {str(e)}"
