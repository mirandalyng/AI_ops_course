from fastapi import FastAPI
from dotenv import load_dotenv
from utils import query_duckdb
from data_models import Prompt
from agents import agent


load_dotenv()


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
