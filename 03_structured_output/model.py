from pydantic_ai import Agent
# Pga Nvida inte finns som modell
# Betyder ej att det är en öppen AI
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
import os
from dotenv import load_dotenv
load_dotenv()


def changeModel(model_name):

    return OpenAIChatModel(
        # this is found in nvida - choose model and copy model
        model_name=model_name,
        provider=OpenAIProvider(
            base_url="https://integrate.api.nvidia.com/v1",
            # from .env, getenv(api_key) funkar också
            api_key=os.environ["NVIDIA_API_KEY"]
        ),

    )
