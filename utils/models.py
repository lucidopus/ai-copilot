from typing import List

from pydantic import BaseModel, Field

from utils.enums import MessageType


class Utterance(BaseModel):
    role: MessageType
    content: str


class Conversation(BaseModel):
    conversation_history: List[Utterance] = Field(
        description="The conversation history",
    )
    calling_purpose: str = Field(
        description="Purpose of the call",
    )


class StreamingContent(BaseModel):
    chunk_id: str = Field(
        description="The chunk ID",
    )
    content: str = Field(
        description="The streamed content",
    )
