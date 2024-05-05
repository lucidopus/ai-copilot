from pydantic import BaseModel, Field


class Conversation(BaseModel):
    conversation_history: str = Field(
        description="The conversation history",
    )
    calling_purpose: str = Field(
        description="Purpose of the call",
    )
