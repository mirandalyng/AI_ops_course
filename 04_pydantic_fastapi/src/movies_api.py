from fastapi import FastAPI
from pydantic_ai import Agent
from dotenv import load_dotenv
from utils import query_duckdb
from data_models import Movie, Prompt
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider
import os

load_dotenv()


def setup_model(model_name):

    return OpenAIChatModel(
        # this is found in nvida - choose model and copy model
        model_name=model_name,
        provider=OpenAIProvider(
            base_url="https://integrate.api.nvidia.com/v1",
            # from .env, getenv(api_key) funkar också
            api_key=os.environ["NVIDIA_API_KEY"]
        ),

    )


agent = Agent(model=setup_model('nvidia/nemotron-3.5-super-vl-120b-a12b'),
              output_type=Movie)


app = FastAPI()


@app.get("/movies")
# Async is not needed in fastAPI (its default) but is market anyways to show api endpoint
async def read_movies():
    movies = query_duckdb("FROM movies;")
    # dataframe but will return it / make it into dict
    return movies.to_dict(orient="records")


# post data
@app.post("/movie")
async def create_movie(query: Prompt):
    result = await agent.run(query.prompt)
    movie = result.output

    query_duckdb(
        "INSERT INTO movies VALUES (?,?,?,?)",
        parameters=(movie.title, movie.year, movie.genre, movie.rating)
    )
    return movie
