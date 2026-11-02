from pydantic import BaseModel, Field
from pydantic_ai import ModelMessage


class ChatRequest(BaseModel):
    question: str = Field(description="user message oe question to JokeBot")

    message_history: list[ModelMessage] = []

    model_config = {
        "json_schema_extra": {"example": {"question": "tell me a joke about python"}}
    }


class ChatResponse(BaseModel):
    response: str = Field(
        description="JokeBots response including a programming joke and emojis")

    message_history: list[ModelMessage] = []
