from pydantic_ai import Agent
from data_models import Movie
from model import setup_model

agent = Agent(model=setup_model('nvidia/nemotron-3.5-super-vl-120b-a12b'),
              output_type=Movie)


# be ablel to rin as standalone script
# __name__ is __main__ when run directly
# __name__ is agents when imported
if __name__ == "__main__":
    movie = agent.run_sync("I'll be back")
    print(movie)

    # RUN IN PYTHON SCRIPT
    # instruction where output_type is now
    # it is also possible to run with asyncio and await

    # movie = agent.run_sync("I'll be back")
    # print(movie)

    # uv run agent in terminal to try out
