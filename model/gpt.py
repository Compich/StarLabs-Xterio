from openai import OpenAI
from typing import Optional


def ask_chatgpt(
    api_key: str, messages: list[dict]
) -> str:
    """
    Send a message to ChatGPT and get a response.

    Args:
        api_key (str): OpenAI API key
        user_message (str): The message to send to ChatGPT
        system_prompt (Optional[str]): System prompt to set the behavior of ChatGPT

    Returns:
        str: ChatGPT's response
    """
    client = OpenAI(api_key=api_key)

    try:
        # Make the API call
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=messages
        )

        # Extract and return the response text
        return response.choices[0].message.content
    except Exception as e:
        return f"Error occurred: {str(e)}"
