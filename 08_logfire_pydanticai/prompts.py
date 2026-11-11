import logfire
from logfire import VariablesOptions
from dotenv import load_dotenv
import os


load_dotenv()

logfire.configure(
    api_key=os.environ["LOGFIRE_API_KEY"],
    variables=VariablesOptions())


def get_prompt(
    name: str = "coach_agent_instructions",
    default: str = "jokey assistant",
    lable: str = "production"
):

    name = "coach_agent_instructions"

    prompt = logfire.var(
        name=f"prompt__{name}",
        type=str,
        default=default)

    prompt.refresh_sync(force=True)

    resolved = prompt.get(lable=lable)
    return resolved.value


if __name__ == "__main__":
    prompt = get_prompt(lable="dev")
    print(prompt)
