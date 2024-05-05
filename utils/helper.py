from groq import Groq

from utils.config import GROQ_API_KEY, GROQ_MODEL
from utils.prompts import SUGGESTION_PROMPT


groq_client = Groq(api_key=GROQ_API_KEY)


def query_groq(messages: list):
    stream = groq_client.chat.completions.create(
        messages=messages,
        model=GROQ_MODEL,
        stream=True,
    )

    response = ""

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content is not None:
            response += content
            # print(content, end="")

    return response


def get_suggestions(CHAT_HISTORY: str, CALLING_PURPOSE: str):

    PROMPT = SUGGESTION_PROMPT.format(purpose=CALLING_PURPOSE)

    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": CHAT_HISTORY},
    ]

    return query_groq(messages)
