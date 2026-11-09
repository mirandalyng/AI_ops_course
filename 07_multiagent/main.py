from agents import coach_agent, ClientDeps
import asyncio


async def main(prompt: str, **kwargs):
    result = await coach_agent.run(prompt, **kwargs)
    print(result.output)


if __name__ == "__main__":
    client = ClientDeps(
        name="Bobby",
        goal="Looking for study and work opertunities within data engineering",
        experience_lvl="intermidiate",
        weekly_hours=16,
        current_role="It supporter"
    )

    asyncio.run(
        main(
            "Im learning python and want to become a data engineer. What should I do?",
            deps=client,
        ),
    )
