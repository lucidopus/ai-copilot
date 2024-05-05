import uuid
import json

from groq import Groq

from utils.config import GROQ_API_KEY, GROQ_MODEL
from utils.prompts import SUGGESTION_PROMPT
from utils.models import StreamingContent


groq_client = Groq(api_key=GROQ_API_KEY)


def query_groq(messages: list):
    stream = groq_client.chat.completions.create(
        messages=messages,
        model=GROQ_MODEL,
        stream=True,
    )
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content is not None:
            data = StreamingContent(chunk_id=str(uuid.uuid4()), content=content)
            yield data.json()


def get_suggestions(CHAT_HISTORY: str, CALLING_PURPOSE: str):

    PROMPT = SUGGESTION_PROMPT.format(purpose=CALLING_PURPOSE)

    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": CHAT_HISTORY},
    ]

    return query_groq(messages)
