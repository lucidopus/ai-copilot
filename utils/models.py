from pydantic import BaseModel, Field


class Conversation(BaseModel):
    conversation_history: str = Field(
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
