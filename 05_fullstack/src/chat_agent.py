from pydantic_ai import Agent
from constants import MODEL_SUPER
from model import setup_model
from data_models import ChatRequest, ChatResponse

chat_agent = Agent(
    model=setup_model(MODEL_SUPER),
    system_prompt="Be a joking programming nerd, always answer with a programming joke. Also add emojis in your language"
)


async def chat(request: ChatRequest):
    result = await chat_agent.run(request.question,
                                  message_history=request.message_history)

    return ChatResponse(
        response=result.output, message_history=result.all_messages()
    )
