import os
from openai import OpenAI

def run(
    prompt: str):
    """Use DeepSeek-R1 model to generate a reasoned response.
    Args:
        prompt: The user's prompt/question to reason about
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

        # Extract just the message content from the response
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"
